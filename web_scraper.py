"""
**Assignment: Building a Simple Web Scraper**
**Objective:**
In this assignment, you will create a simple web scraper using Python. You will use the `requests` library to fetch the HTML content of a webpage and `BeautifulSoup` library to parse the HTML and extract useful information from it.
**Instructions:**
1. Install the required libraries (`requests` and `BeautifulSoup`) using pip if you haven't already installed them.
   ```
   pip install requests beautifulsoup4
   ```
2. Write a Python script named `web_scraper.py`.
3. Your script should have the following functionalities:
   - Prompt the user to input a URL of a webpage.
   - Fetch the HTML content of the webpage using the `requests` library.
   - Parse the HTML content using `BeautifulSoup`.
   - Extract specific information from the webpage (e.g., titles, headings, links, etc.).
   - Display the extracted information to the user.
4. Test your script with different URLs to ensure it works correctly.
**Example Output:**
```
Enter the URL of the webpage you want to scrape: https://example.com
Extracted Information:
Title: Example Domain
Headings:
- Heading 1: This domain is established to be used for illustrative examples in documents.
- Heading 2: You may use this domain in examples without prior coordination or asking for permission.
Links:
- Link 1: https://www.iana.org/domains/example
- Link 2: https://www.example.com
...
```
**Submission Guidelines:**
- Submit your `web_scraper.py` file.
- Provide any additional instructions or notes if necessary.
**Note:** Ensure your code is properly commented and follows best practices for readability and maintainability.
"""

import requests
from bs4 import BeautifulSoup


def fetch_html_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for any HTTP error status
        print(response.text)
        return response.text
    except requests.RequestException as e:
        print("Error fetching webpage content:", e)
        return None


def extract_information(html_content):
    if html_content is None:
        return None, None, None

    soup = BeautifulSoup(html_content, 'html.parser')

    # Extracting title
    title = soup.title.string.strip() if soup.title else "No title found"

    # Extracting headings
    headings = {}
    for heading in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        headings[heading.name] = heading.text.strip()

    # Extracting links
    links = [link.get('href') for link in soup.find_all('a') if link.get('href')]

    return title, headings, links


def display_information(title, headings, links):
    print("\nExtracted Information:")
    print("Title:", title)

    if headings:
        print("Headings:")
        for tag, heading in headings.items():
            print(f"- {tag.capitalize()}: {heading}")

    if links:
        print("Links:")
        for idx, link in enumerate(links, start=1):
            print(f"- Link {idx}: {link}")


def main():
    url = input("Enter the URL of the webpage you want to scrape: ")
    html_content = fetch_html_content(url)
    title, headings, links = extract_information(html_content)
    if title:
        display_information(title, headings, links)
    else:
        print("No information extracted. Please check the URL and try again.")


if __name__ == "__main__":
    main()
























