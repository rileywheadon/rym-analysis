from bs4 import BeautifulSoup

# Open and read the saved page.html
with open("pages/albums/2025/00.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Prettify the parsed HTML
pretty_html = soup.prettify()

# Print the prettified HTML
print(pretty_html)
