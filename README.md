# TWITTER SCRAPING


## Approach: 

1. By using the “snscrape” Library, Scrape the twitter data from Twitter  --> [ filename: Twitter_Scraping_PythonScripting.ipynb ]
2. Create a dataframe with date, id, url, tweet content, user,reply count, retweet count,language, source, like count.  --> [ filename:    Twitter_Scraping_PythonScripting.ipynb ]
3. Store each collection of data into a document into Mongodb along with the hashtag or key word we use to  Scrape from twitter.   --> [ filename: Twitter_Scraping_MongoDB.ipynb ]
4. Create a GUI using streamlit that should contain the feature to enter the keyword or Hashtag to be searched, limit the tweet count need to be scraped.
    After scraping, the data needs to be displayed in the page and download the data into csv and json format.
      --> [ filename: Twitter_Scraping_Streamlit.ipynb ]
      --> [ filename: Twitter_Scraping_Streamlit.py ]
