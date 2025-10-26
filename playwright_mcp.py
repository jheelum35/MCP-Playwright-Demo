import asyncio
from playwright.async_api import async_playwright, Browser, Page
from mcp.server.fastmcp import FastMCP

browser: Browser = None
page: Page = None
playwright_instance = None

mcp = FastMCP("playwright-mcp-server")

async def _ensure_browser():
    """ Ensure browser and page are initialized"""
    global browser, page, playwright_instance
    
    if browser is None or page is None:
        playwright_instance = await async_playwright().start()
        browser = await playwright_instance.chromium.launch(headless=False)
        page = await browser.new_page()
        
@mcp.tool()
async def navigate(url: str) -> str:
    "Navigate to the given URL"
    
    try:
        await _ensure_browser()
        await page.goto(url, wait_until="domcontentloaded")
        title = await page.title()
        return f"Navigated to: {url}\n Page title: {title}"
    except Exception as e:
        return f"Error navigating to {url}: {e}"
    
@mcp.tool()
async def click(selector: str) -> str:
    "Click an element on the page"
    
    try:
        await _ensure_browser()
        await page.click(selector)
        return f"Clicked the element : {selector}"
    except Exception as e:
        return f"Error clicking element {selector}: {e}"
    
@mcp.tool()
async def fill(selector: str, value: str) -> str:
    "Fill an input field with text on the page"
    
    try:
        await _ensure_browser()
        await page.fill(selector, value)
        return f"Filled the element : {selector} with {value}"
    except Exception as e:
        return f"Error filling the element {selector}: {e}"
    
@mcp.tool()
async def evaluate_js(script: str) -> str:
    "Execute Javascript on the current page"
    
    try:
        await _ensure_browser()
        result = await page.evaluate(script)
        return f"Javascript result {result}"
    except Exception as e:
        return f"Error filling javascript: {e}"

@mcp.tool()
async def get_text() -> str:
    """Get visible text content from the current page."""
    try:
        await _ensure_browser()
        text = await page.locator("body").inner_text()
        if len(text) > 2000:
            text = text[:2000] + "\n... (truncated)"
        return f"Page text content:\n\n{text}"
    except Exception as e:
        return f"Error getting text: {e}"
    
@mcp.tool()
async def get_current_url() -> str:
    """Get the current page URL."""
    try:
        await _ensure_browser()
        url = page.url
        return f"Current URL: {url}"
    except Exception as e:
        return f"Error getting current URL: {e}"

@mcp.tool()
async def get_page_title() -> str:
    """Get the current page title."""
    try:
        await _ensure_browser()
        title = await page.title()
        return f"Page title: {title}"
    except Exception as e:
        return f"Error getting page title: {e}"    

if __name__ == "__main__":
    try:
        mcp.run()
    finally:
        if browser:
            asyncio.run(browser.close())
        if playwright_instance:
            asyncio.run(playwright_instance.stop())
        print("Playwright MCP Server is running and resources are cleaned up.")