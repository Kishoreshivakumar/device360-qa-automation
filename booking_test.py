import time
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    # Add a small delay to ensure your internet connection is active
    print("Waiting for network to stabilize...")
    time.sleep(2) 
    
    try:
        # Add a longer timeout for the navigation to account for slow connections
        page.goto("https://device360.in/", timeout=60000) 
        page.get_by_role("button", name="CHECK INSTANT PRICING").click()
        
        page.screenshot(path="step_1_success.png")
        print("Successfully clicked pricing button.")
        
    except Exception as e:
        page.screenshot(path="error_capture.png")
        print(f"FAILED: {e}")
    finally:
        browser.close()