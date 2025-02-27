from playwright.sync_api import sync_playwright

def print_mobile_context():
    with sync_playwright() as p:
        browser = p.webkit.launch(headless=False)
        ipad = p.devices["iPad (gen 7)"]
        # Create a mobile context
        context = browser.new_context(
            #viewport={"width": 768, "height": 1024},  # iPad 7th Gen
            #is_mobile=True,
            #device_scale_factor=2
            **ipad
        )
        page = context.new_page()

        # Print viewport size (use `page.viewport_size()` instead)
        print(f"Viewport Size: {page.viewport_size}")

        # Print User-Agent
        user_agent = page.evaluate("navigator.userAgent")
        print(f"User-Agent: {user_agent}")

        # Print if touch is enabled
        touch_support = page.evaluate("'ontouchstart' in window")
        print(f"Touch Support Enabled: {touch_support}")

        # Print Device Scale Factor (Using JS Evaluation)
        scale_factor = page.evaluate("window.devicePixelRatio")
        print(f"Device Scale Factor: {scale_factor}")

        # Print navigator platform
        platform = page.evaluate("navigator.platform")
        print(f"Navigator Platform: {platform}")

        # Print navigator language
        language = page.evaluate("navigator.language")
        print(f"Navigator Language: {language}")

        # Print window screen properties
        screen_width = page.evaluate("window.screen.width")
        screen_height = page.evaluate("window.screen.height")
        screen_avail_width = page.evaluate("window.screen.availWidth")
        screen_avail_height = page.evaluate("window.screen.availHeight")
        print(f"Screen Width: {screen_width}, Screen Height: {screen_height}")
        print(f"Available Screen Width: {screen_avail_width}, Available Screen Height: {screen_avail_height}")

        # Print CSS media query (checking if it's really mobile)
        is_mobile_css = page.evaluate("window.matchMedia('(max-width: 812px)').matches")
        print(f"CSS Media Query Mobile: {is_mobile_css}")

        # Print other navigator properties
        hardware_concurrency = page.evaluate("navigator.hardwareConcurrency")
        print(f"CPU Cores (Threads): {hardware_concurrency}")

        # Print full `window.navigator` object
        full_navigator = page.evaluate("JSON.stringify(navigator, null, 2)")
        print(f"Full navigator object:\n{full_navigator}")

        # Navigate to the web app
        page.goto("http://192.168.50.1/control")
        page.wait_for_timeout(10000)

        browser.close()

if __name__ == "__main__":
    print_mobile_context()