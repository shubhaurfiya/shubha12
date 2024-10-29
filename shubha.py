import requests
from bs4 import BeautifulSoup

# Define the URL of the website you want to scrape
url = "https://example.com"  # Replace with the website you want to scrape

# Send a request to the website
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all the article titles (replace with the relevant HTML tags or classes for your website)
    titles = soup.find_all('h2')  # Assuming article titles are within <h2> tags
    
    # Print each title
    for idx, title in enumerate(titles, start=1):
        print(f"Title {idx}: {title.get_text(strip=True)}")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")