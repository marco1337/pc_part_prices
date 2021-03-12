import requests
from bs4 import BeautifulSoup
import streamlit as st
import pandas as pd



"""
# Precios de Componentes de PC
## Memory Kings
"""


headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"
}

URL = 'https://www.memorykings.com.pe/listados/1128/videos-nvidia-geforce-rtx3060-3070-3080-3090'
page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')
contents = soup.find_all("div", {"class": "content"})

all_rows = []
for content in contents:
    title_text = content.find("h4")
    precio = content.find("div", {"class": "price"})
    if title_text == None or precio == None:
        continue
    #print(title_text.text)
    #print(precio.text)
    row_to_add = [title_text.text,precio.text]
    all_rows.append(row_to_add)

df = pd.DataFrame(all_rows, columns=['Producto', 'Precio'])
st.write(df)