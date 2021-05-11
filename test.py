from wordcloud import WordCloud
import matplotlib.pyplot as plt
import streamlit as st

import requests
def Displaying_data(txt):
  url = "https://hindityping.info/download/assets/Hindi-Fonts-Unicode/gargi.ttf"

  r = requests.get(url, allow_redirects=True)
  font_path="gargi.ttf"

  with open(font_path, "wb") as fw:
    fw.write(r.content)

  #text = "सुनिए कुलभूषण की दर्दभरी आपबीती... अन्य वीडियो देखें"
  text=txt
  
  wordcloud = WordCloud(max_font_size=50, max_words=100,regexp=r"[\u0900-\u097F]+", background_color="white",font_path=font_path).generate(text)
  wordcloud.generate(text)
  plt.figure(figsize=(100,100))
  fig,axes=plt.subplots()
  plt.imshow(wordcloud, interpolation="bilinear")
  #axes[1].imshow(wordcloud,interpolation='bilinear')
  plt.axis("off")
  #plt.show()
  st.pyplot(fig)
  callPolarity()

def callPolarity():
  url = "https://hindityping.info/download/assets/Hindi-Fonts-Unicode/gargi.ttf"

  r = requests.get(url, allow_redirects=True)
  font_path="gargi.ttf"

  with open(font_path, "wb") as fw:
    fw.write(r.content)

    #text = "सुनिए कुलभूषण की दर्दभरी आपबीती... अन्य वीडियो देखें"
  text="       सकारात्मक कण "
    
  wordcloud = WordCloud(max_font_size=50, max_words=100,regexp=r"[\u0900-\u097F]+", background_color="white",font_path=font_path).generate(text)
  wordcloud.generate(text)
  plt.figure(figsize=(100,100))
  fig,axes=plt.subplots()
  plt.imshow(wordcloud, interpolation="bilinear")
    #axes[1].imshow(wordcloud,interpolation='bilinear')
  plt.axis("off")
    #plt.show()
  st.pyplot(fig)

    
    