from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Launch browser and set a small timeout for stability
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    print("Navigating to device360.in...")
    page.goto("https://device360.in/", timeout=60000)
    
    # Print page details for verification
    print(f"Page loaded: {page.title()}")
    
    # Wait for 5 seconds to observe the page
    page.wait_for_timeout(5000)
    
    browser.close()
    print("Test complete!")