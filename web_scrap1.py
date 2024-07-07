import requests
from bs4 import BeautifulSoup

# Scrapping the data

url = input('Enter url : ')
response = requests.get(url)

print(response)
soup = BeautifulSoup(response.content, 'html.parser')

s = soup.find('div', class_='GNDEQ-')
content = s.find_all('td')

# Writting the Scrapped Data to an html file(auto-generated)
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Scraped Data</title>
</head>
<body>
    <h1>Scraped Data from GeeksforGeeks</h1>
    <div>
"""

# appending the scrapped data to the html
for i in content:
    html_content += f"<p>{i.get_text()}</p>"

html_content += """
    </div>
</body>
</html>
"""

# Write the HTML content to a file
with open('scraped.html', 'w', encoding='utf-8') as file:
    file.write(html_content)

print("Data has been written to scraped.html")
