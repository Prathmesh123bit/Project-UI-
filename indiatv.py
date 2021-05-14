from bs4 import BeautifulSoup
import streamlit as st
import requests
import csv
import pandas as pd
from csv import reader
from trial import display_data
from wordclouddata import Displaying_data

def web_Scrapping(urls):
    st.markdown("<h1 style='text-align: center; color: white;'>Polarity Classification</h1>", unsafe_allow_html=True)
    summary = []
    session = requests.Session()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G920A) AppleWebKit (KHTML, like Gecko) Chrome Mobile Safari (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html)'
        }
    

    for row in urls :
        st.text_input("URL",row)
        response = session.get(row, headers=headers)
        source = requests.get(row).text
        soup = BeautifulSoup(source, 'lxml')
        headline_ele = soup.find(class_='artsubject')
        print("Headline")
        headline = st.text_input("Headline",headline_ele.text)
        description_ele = soup.find(class_='content')
        st.write("  ")
        description = description_ele.find_all("p")
        for item in description:
            summary.append(item.text)
        str1 = ''.join(summary)
        x = str1.split('।')
        y = str1.replace("।", ".\n")
        print(y)
        st.text_area("Description",y,1000)
        y.split('.') 
        Sentence_break=y.replace('.','.\n')
       # st.text(rand)
       
        st.write("\t\t\t\tPolarity")
        cols=st.beta_columns(4)
        cols[0].write(Sentence_break)
        cols[2].write("Polarity")
        st.write(len(y))
        st.markdown("""<br>""",True)
        #display_data(Sentence_break)
        Displaying_data(y)
        
