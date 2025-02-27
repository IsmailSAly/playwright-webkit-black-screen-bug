from playwright.sync_api import sync_playwright

def reproduce_bug():
    with sync_playwright() as p:
        browser = p.webkit.launch(headless=False)
        context = browser.new_context(
            viewport={"width": 375, "height": 812},
            is_mobile=True  # This causes WebKit to turn black
        )
        page = context.new_page()
        page.goto("https://playwright.com")
	page.wait_for_timeout(10000)
        browser.close()

if __name__ == "__main__":
    reproduce_bug()
