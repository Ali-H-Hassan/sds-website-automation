import json
import subprocess
import pytest

# Generate Lighthouse report for the website
@pytest.fixture(scope="session")
def lighthouse_report(tmp_path_factory):
    url = "https://s-d-s.co.uk/"
    temp_dir = tmp_path_factory.mktemp("lighthouse")
    output_file = temp_dir / "lighthouse_report.json"
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

# Check if the accessibility score meets the threshold
def test_accessibility_lighthouse(lighthouse_report):
    score = lighthouse_report["categories"]["accessibility"]["score"] * 100
    threshold = 90
    print(f"Lighthouse Accessibility Score: {score}%")
    assert score >= threshold, f"Score {score}% is below threshold {threshold}%."
