# Project Name: Web Scraper with Streamlit

## Description:

This Python script fetches manga data (name, genre, description, and rating) from the website "https://www.mangaupdates.com/whatsnew.html?year=2024" and displays it in a user-friendly Streamlit web app. The app includes a search bar to filter results by genre and displays ratings as progress bars.

## Key Features:

Web scraping of manga data from MangaUpdates.com
Data cleaning and processing using pandas
Interactive Streamlit web app with a search bar
Genre filtering based on user input
Progress bar visualization of manga ratings

## Requirements:

Python 3.x
pandas library
requests library
beautifulsoup4 library
streamlit library
Installation:

Make sure you have Python 3.x installed.

Open a terminal or command prompt.

Install the required libraries:

Bash
`pip install pandas requests beautifulsoup4 streamlit`
Use code with caution.

## Usage:

Save the code as web_scraper.py.

Run the script from the terminal:

Bash
`streamlit run web_scraper.py`
Use code with caution.

A Streamlit app will open in your web browser, displaying the scraped manga data.

Use the search bar to filter results by genre.

### Explanation of the Code:

Import Libraries:

requests: Used for making HTTP requests to the website.
pandas: Used for data manipulation and creating DataFrames.
streamlit: Used for building the web app.
BeautifulSoup: Used for parsing HTML content from the website.
Scrape Manga Data:

The script defines the URL to scrape and fetches the HTML content using requests.get.
Beautiful Soup is used to parse the HTML and find relevant elements.
The script extracts manga information like name, genre, description elements, and bold elements containing ratings.
Process Data:

A pandas DataFrame is created to store the extracted data in a structured format.
Functions are defined to extract descriptions and ratings from the scraped elements.
The DataFrame is filtered to keep only manga with a rating below 10.
Build Streamlit App:

A search bar is added using st.text_input to allow users to filter by genre.
The filtered DataFrame is displayed using st.dataframe with custom column configurations:
ListColumn for genre
ProgressColumn for rating
CSS styles are added using st.markdown to make the DataFrame and search bar take up the full browser height.
Contributing:

Feel free to fork this repository and make improvements! You can add features like:

Scraping data from other websites
Filtering by additional criteria (e.g., release date)
Implementing pagination for displaying large datasets
Adding user authentication for creating personalized watchlists
License:

This project is licensed under the MIT License. See the LICENSE file for details.

I hope this README provides a clear and comprehensive overview of the code and its functionality.


**This ReadMe was generated with Gemini**