# MCP-Playwright-Demo
🚀 AI + MCP + Playwright Tool

Where AI stops talking and starts interacting with real web pages.

This project demonstrates how MCP (Model Context Protocol) allows an AI to safely control a browser via Playwright — clicking buttons, filling forms, reading content, and executing JavaScript — without giving direct system access.

✨ Why This Matters

AI can interact with real web pages ✅

Controlled, permission-based automation ✅

Today it’s a demo for simple browsing tasks, tomorrow it can handle QA workflows, scraping, testing, and cloud automation ✅

| Component           | Role                                            |
| ------------------- | ----------------------------------------------- |
| `playwright_mcp.py` | MCP server exposing browser tools               |
| MCP                 | Bridge that lets AI call async Python functions |
| AI Client           | The “brain” that triggers web interactions      |


@mcp.tool()
async def navigate(url: str) -> str:
    """Navigate to the given URL"""
    await _ensure_browser()
    await page.goto(url, wait_until="domcontentloaded")
    title = await page.title()
    return f"Navigated to: {url}\nPage title: {title}"


Other tools include:

click(selector) → click elements

fill(selector, value) → fill input fields

evaluate_js(script) → run JS on the page

get_text() → get page content

get_current_url() → get URL

get_page_title() → get title



Setup Instructions

Install Python

https://www.python.org/downloads/

Install dependencies

pip install playwright fastmcp

python -m playwright install

Run MCP Server

python playwright_mcp.py

Configure AI Client

{
  "mcpServers": {
    "playwright-mcp-server": {
      "command": "python",
      "args": ["playwright_mcp.py"]
    }
  }
}

🌍 Potential Use Cases

Web QA Automation

Form filling and data submission

Scraping / data collection

Cross-browser testing
