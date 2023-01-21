#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing libraries

import streamlit as st
import camelot as cam
import pandas as pd
import json
import subprocess
import os
import base64
import snscrape.modules.twitter as sntwitter


# In[2]:


# Assigning a title for our GUI

st.title("Lets Scrape some Tweets")
#st.subheader("Twitter Scraper")

st.image("./wp4056133-twitter-wallpapers.jpg")


# In[3]:


# Creating a Streamlit form

with st.form(key = 'Twitter Form'):
    name = st.text_input(label = 'Please enter your Keyword/ hashtag')
    file_name = st.text_input('Name your file')
    submit = st.form_submit_button(label = 'Next')


# In[4]:


# Creating columns under Streamlit form

col1, col2 = st.columns(2)

with col1:
    with st.form('CSV Download'):
        down1 = st.radio('Do you want to Download CSV?', ['Yes', 'No'])
        number1 = st.slider(label='How many Tweets to produce', min_value=0, max_value=500, step = 10)
        submitted1 = st.form_submit_button('Submit 1')

with col2:
    with st.form('JSON Downlaod'):
        down2 = st.radio('Do you want to Download JSON?', ['Yes', 'No'])
        number2 = st.slider(label='How many Tweets to produce', min_value=0, max_value=500, step = 10)
        submitted2 = st.form_submit_button('Submit 2')


# In[5]:


if col1 == 'Yes':
    # byte object into a PDF file 
    with open("input.csv", "wb") as f:
        base64_pdf = base64.b64encode(input_csv.read()).decode('utf-8')
        f.write(base64.b64decode(base64_csv))
    f.close()
else:
    print('Try Again')


# In[6]:


if col2 == 'Yes':
    # byte object into a PDF file 
    with open("input.json", "wb") as f:
        base64_pdf = base64.b64encode(input_json.read()).decode('utf-8')
        f.write(base64.b64decode(base64_json))
    f.close()
else:
    print('Try Again')


# In[7]:


# Scraping required items from the hashtag

scraper = sntwitter.TwitterSearchScraper('#python')

tweets = []

for i, tweet in enumerate(scraper.get_items()):
    data = [
        tweet.date,
        tweet.id,
        tweet.url,
        tweet.rawContent,
        tweet.user.username,
        tweet.replyCount,
        tweet.retweetCount,
        tweet.lang,
        tweet.source,
        tweet.likeCount
    ]
    tweets.append(data)
    if i > 500:
        break


# In[8]:


# Converting the data into a DataFrame and assigning it to a variable

table = pd.DataFrame(tweets, columns = ["date", "id", "url", "rawContent", "username", "replyCount", "retweetCount", "lang", "source",  "likeCount",])

# display the output after parsing 
st.write(table)


# In[9]:


if len(table) > 0:
       output_df = st.dataframe(table)


# In[12]:


# Adding Streamlit Download Button

st.download_button("Download CSV",
                   "input.csv",
                   "text.csv",
                   key = 'download-csv',)


# In[ ]:




