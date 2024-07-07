# Web Scraping Program

## Description
This is a web scraping program where the user needs to enter the URL of the website from which they want to scrape data and see it in an organized way. Note that:
- If the response code is `200`, it means the website can be accessed and the data can be scraped.
- If the response code is `401`, it means the website cannot be accessed (401 typically means unauthorized access, so it might be 403 for forbidden or another status code if access is denied).

After entering the website URL, you need to specify what you want to scrape. For example, you can scrape all `<p>` tag details from a `<div>` with the class `text`. After scraping is done, a new HTML file will be created called `scraped.html`, where you can see the scraped data. Ensure that you don't have any existing HTML file with that name to avoid overwriting.

## How to Use
1. **Run the Program**: Execute the program to start the web scraping process.
2. **Enter Website URL**: The program will prompt you to enter the URL of the website you want to scrape.
3. **Check Response Code**: 
   - `200` indicates successful access and that data can be scraped.
   - `401` or other error codes indicate access issues or unauthorized access.
4. **Specify Data to Scrape**: Enter the details of the elements you want to scrape (e.g., all `<p>` tags within a `<div>` with the class `text`).
5. **View Scraped Data**: After scraping, a new HTML file named `scraped.html` will be created. You can open this file to view the scraped data.

### Running the Program
To run the web scraping program, execute the following command:
```bash
python web_scrap1.py
