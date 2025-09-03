## Date monday sep 1 2025

started with the project initialized the setups and now planning for the scrapper
for the scrapper the functional requirements are to :
input the user queries and output with :
title, price, rating, url, image_url, and snippet(short review/ description)
lets set the limit for 25 products per query per site 
and save these results in jsonl inside of data/scraper_results/.

### Design choices: 
scraping method; Use headless browser (Playwright/ Puppeteer) or http requests +parser
selectors: Inspect Amazon/Flipkart search pages, identify consistent CSS/XPath for: Product title Price Rating Link Thumbnail image
Pagination: Collect 1–2 result pages only (configurable).
Throttling: Add 2–4 sec delay between requests to avoid blocking.

### Data Schema :
{
  "id": "amazon_12345",
  "source": "amazon",
  "query": "laptops under 70k for AI work",
  "title": "Lenovo ThinkPad XYZ",
  "price": 68999,
  "rating": 4.3,
  "url": "https://amazon.in/product/123",
  "image_url": "https://...",
  "snippet": "Great for professionals, comes with RTX 4050..."
}


#### This scraper will be our data entry agent in Blonde


