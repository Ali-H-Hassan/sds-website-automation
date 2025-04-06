import json
import subprocess
import pytest

# This fixture runs Lighthouse on the SDS homepage and returns the parsed JSON report.
@pytest.fixture(scope="session")
def lighthouse_report(tmp_path_factory):
    url = "https://s-d-s.co.uk/"
    # Create a temporary directory using tmp_path_factory
    temp_dir = tmp_path_factory.mktemp("lighthouse")
    output_file = temp_dir / "lighthouse_report.json"
    # Command to run Lighthouse in headless mode with JSON output.
    # Ensure that Lighthouse is installed globally (npm install -g lighthouse).
    command = [
        "lighthouse",
        url,
        "--output=json",
        f"--output-path={str(output_file)}",
        "--chrome-flags=--headless"
    ]
    subprocess.run(command, check=True)
    
    with open(output_file, "r") as f:
        report = json.load(f)
    return report

def test_accessibility_lighthouse(lighthouse_report):
    # Extract the accessibility score (a value between 0 and 1) and convert it to a percentage.
    accessibility_score = lighthouse_report["categories"]["accessibility"]["score"] * 100
    threshold = 90  # Set the threshold as 90%
    print(f"Lighthouse Accessibility Score: {accessibility_score}%")
    assert accessibility_score >= threshold, (
        f"Accessibility score {accessibility_score}% is below the acceptable threshold of {threshold}%."
    )
