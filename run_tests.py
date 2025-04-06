import sys
import pytest
import glob

def run_tests():
    test_files = glob.glob("tests/test_*.py")
    overall_result = 0
    for test_file in test_files:
        print(f"Running tests in {test_file}")
        result = pytest.main([test_file])
        if result != 0:
            print(f"Tests in {test_file} failed with exit code {result}.")
            overall_result = result  # Record the last non-zero result
        else:
            print(f"Tests in {test_file} passed.")
    if overall_result != 0:
        print("Some tests failed.")
    else:
        print("All tests passed.")
    sys.exit(overall_result)

if __name__ == "__main__":
    run_tests()
