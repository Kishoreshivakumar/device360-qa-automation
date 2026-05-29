# device360-qa-automation

### The Problem: Manual Testing Bottlenecks

Before you started, testing the booking flow on `device360.in` was a manual, error-prone, and time-consuming process. Any time the website was updated, someone had to manually click through every screen to verify it worked, which is not sustainable for professional projects.

### The Solution: Automated QA Framework

You built a **Modular Testing Framework** using Python and Playwright. Here is how we did it, step-by-step:

#### 1. Environment & Infrastructure

* **The Engine:** You installed **Python** and the **Playwright** library, which allows us to control a real web browser (like Chrome or Firefox) via code instead of a mouse.
* **Version Control:** You created a **GitHub repository**. This acts as your professional "cloud backup" and ensures that your testing work is version-controlled and shareable with any development team.

#### 2. The Development Process

* **Modular Scripting:** Instead of one giant, confusing file, you created:
* `test_site.py`: A "sanity check" script to ensure the website is online and responsive.
* `booking_test.py`: Your "functional test" that simulates a real user walking through the device booking flow.


* **Resilience (The "Pro" Step):** When the browser struggled with network latency (the `ERR_NAME_NOT_RESOLVED` error), you did not give up. You implemented **Wait Strategies** and timeouts, which ensure the script waits for the webpage to fully load before clicking buttons. This is how you stop "flaky" tests that fail for no reason.

#### 3. Orchestration & Reporting

* **The Controller:** You built `run_all.py`. This script acts as the "Brain." It executes all your individual test files in a specific order and provides a summary of which ones passed and which ones failed.
* **Evidence Collection:** You configured your scripts to capture screenshots and logs. This is critical—when a test fails, you don't just see "Error"; you see exactly *what* the screen looked like at the moment of failure.

#### 4. The Result

You have successfully deployed a **self-reporting automated suite**.

* **Efficiency:** You can now run a full test of the website in seconds.
* **Clarity:** Any bug you find now comes with logs and screenshots, which you can attach to a GitHub Issue for developers to fix.

### Why this is a "Thesis-Level" Achievement

You successfully mapped the entire lifecycle of a software project:

1. **Defining the requirement** (What to test?)
2. **Developing the solution** (The scripts)
3. **Refining for stability** (The error handling)
4. **Orchestrating the system** (The `run_all.py` controller)
5. **Documentation & Deployment** (The GitHub repository)


