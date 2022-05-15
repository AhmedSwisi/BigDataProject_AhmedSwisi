import twint 
import pandas as pd
c=twint.Config()
c.Search=['The Batman']
c.Limit=30000  
c.Store_csv=True
c.Lang="en"
c.Output="the_batman_tweets_en.csv"
twint.run.Search(c)
df=pd.read_csv("the_batman_tweets_en.csv")
df['tweet']


