from playwright.sync_api import sync_playwright

def reproduce_bug():
    with sync_playwright() as p:
        browser = p.webkit.launch(headless=False)
        ipad_gen7 = p.devices["iPad (gen 7)"]
        context = browser.new_context(**ipad_gen7)
        page = context.new_page()
        
        page.on("console", lambda msg: print(f"Console Log [{msg.type()}]: {msg.text()}"))
        page.on("pageerror", lambda error: print(f"Page Error: {error}"))
        browser.on("disconnected", lambda: print("⚠️ Browser Disconnected"))

        page.goto("https://playwright.com")
        page.wait_for_timeout(10000)
        browser.close()

if __name__ == "__main__":
    reproduce_bug()
