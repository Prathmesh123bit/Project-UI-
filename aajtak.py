
import streamlit as st
import pandas as pd
import requests
from openpyxl import load_workbook
from bs4 import BeautifulSoup
from wordclouddata import Displaying_data


def web_Scrapping(urls):
    st.markdown("<h1 style='text-align: center; color: white;'>Polarity Classification</h1>", unsafe_allow_html=True)
    for url in urls:
        page=requests.get(url)
        page.text
        soup=BeautifulSoup(page.text,'html.parser')
        soup.find('div', class_='fedback-sec').decompose()
        headline_ele=soup.find("div",{'class':"content-area"}).h1.text
        print("headline:",headline_ele)
        print("\n")
        
        print("DESCRIPTION")
        print("\n")
        
        description_name=[]
        description_ele=soup.find_all("p")
        
        for item in description_ele:
            description_name.append(item.text)
      
    
        
        str1 = ''.join(description_name)


        x = str1.split('.')
    
        print("***********")
        
        print("\n")
        y = str1.replace(".", ".\n")

        print(y)
        print(url)
        st.text_input("URL",url)
        headline = st.text_input("Headline",headline_ele)

        st.text_area("Description",y,1000)

        print("\n")
       
        Sentence=y.replace('.','.\n')
        
        #st.write("\t\t\t\tPolarity")
        #cols=st.beta_columns(3)
        #cols[0].write(Sentence)
        #cols[2].write("Polarity")
        #st.write(len(y))      
    
    #if st.button("Anaalyze in Detail"):
     #   annalyze_in_detail(Sentence)
    st.markdown("""<br>""",True)
        
    Displaying_data(y)
#def annalyze_in_detail(Sentence):
    #st.write("Sentences")
    
        