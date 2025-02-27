# Playwright WebKit Bug: Black Screen in Headed Mode with `is_mobile=True`

## **Issue**
When running Playwright WebKit in **headed mode** with `is_mobile=True`, the browser window turns black.

## **Steps to Reproduce**
1. Make venv:
   ```sh
   python -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   playwright install
2. Run the script:
  ```
   python repro.py
  ```

