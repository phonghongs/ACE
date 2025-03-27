# Import necessary libraries
from crawl4ai import Crawl4AI
import time

# List of URLs to crawl
urls_to_crawl = [
    'https://example.com',
    'https://example2.com',
    'https://example3.com',
]

# Define a function to crawl the list of URLs
def crawl_urls(url_list):
    # Initialize the Crawl4AI object
    crawler = Crawl4AI()

    # Iterate over the list of URLs
    for url in url_list:
        print(f"Crawling URL: {url}")
        
        # Crawl the URL (You can add your logic for extracting the data here)
        data = crawler.crawl(url)  # Assuming the method `crawl` is used to get the data from the URL
        
        # Do something with the data (e.g., print it, store it, etc.)
        print(f"Data crawled from {url}: {data[:100]}...")  # Print first 100 characters of the data for demonstration

        # Pause for a moment between requests to avoid overloading the server
        time.sleep(2)  # Adjust the sleep time based on your needs

# Call the function with the list of URLs
crawl_urls(urls_to_crawl)
