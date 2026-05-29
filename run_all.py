import subprocess

def run_tests():
    # List of your test files
    test_files = ["test_site.py", "booking_test.py"]
    
    print("--- Starting Automation Test Suite ---")
    
    for test in test_files:
        print(f"\nRunning {test}...")
        try:
            # Runs the test file as a sub-process
            result = subprocess.run(["python", test], capture_output=True, text=True)
            if result.returncode == 0:
                print(f"PASSED: {test}")
            else:
                print(f"FAILED: {test}")
                print(result.stderr)
        except Exception as e:
            print(f"ERROR: Could not execute {test}. {e}")
            
    print("\n--- Test Suite Complete ---")

if __name__ == "__main__":
    run_tests()