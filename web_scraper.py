import requests
import pandas as pd
import streamlit as st 
from bs4 import BeautifulSoup



URL = "https://www.mangaupdates.com/whatsnew.html?year=2024"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="main_content")

manga_elements = results.find_all("div", class_="col-md-8")

data = []
for manga_element in manga_elements:
    name_element = manga_element.find("h3").get_text()
    genre_element =  manga_element.find("p").find_all(text=True)[1]
    description_array =  manga_element.find("p").find_all(text=True)[2:]
    b_element_array = [b.text for b in manga_element.find("p").find_all("b")]

    # print(name_element)
    # print(genre_element)
    # print(description_array)
    # print(b_element_array)

    item = {'manga_name':name_element, 'genre_element': genre_element, "description_array":description_array, "b_element_array":b_element_array}

    data.append(item)

df = pd.DataFrame(data)



# for index, row in df.iterrows():
#     # Access the value in a specific column
#     value = row['description_array']
#     description = ""

def extract_description(value):  
    description = ""
    for i in value:
        if i.startswith("Original_") or i.startswith("url_"):
            break
        else:
            description += i + ' '

    return description

df['description'] = df['description_array'].apply(extract_description)

def is_float(string):
  try:
    float(string)
    return True
  except ValueError:
    return False

def extract_rating(value):
    rating = 0
    for tag in value:
        if is_float(tag):
            rating = float(tag) 
            break
    return rating 

df['rating'] = df["b_element_array"].apply(extract_rating)


df = df[["manga_name","genre_element","description","rating"]]

manga_df = df[df['rating'] < 10.0]

search_term = st.text_input("Search for genre:")

if search_term:
    filtered_df = manga_df[manga_df['genre_element'].str.contains(search_term, case=False)]
else:
    filtered_df = manga_df


st.dataframe(
    filtered_df,
    column_config={
        "manga_name": "Manga Name",
        "genre_element": st.column_config.ListColumn(
            "List of Genre",
            help="List of Genre",
            width="medium",
        ),
        "description": "Manga Description",
        "rating": st.column_config.ProgressColumn(
            "Manga Rating",
            help="Manga Rating",
            format="%f",
            min_value=0,
            max_value=10,
        ),
    },
    hide_index=True,
)

# Set the height of the DataFrame and search bar to 100vh
st.markdown('<style>.st-dataframe { height: 100vh; }</style>', unsafe_allow_html=True)
st.markdown('<style>.st-bb { height: 100vh; }</style>', unsafe_allow_html=True)
