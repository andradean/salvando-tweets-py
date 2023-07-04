import tweepy as tw
import pandas as pd
import time
import sqlite3

consumer_key = ''
consumer_secret = ''
bearer_token = ''
access_token = ''
access_token_secret = ''

client = tw.Client(bearer_token,consumer_key, consumer_secret, access_token, access_token_secret)

con = sqlite3.connect('BD_podpah.db')
cur = con.cursor()

start = '2023-07-15T08:00:00Z'
end = '2023-07-15T16:00:00Z'

response = client.search_recent_tweets(query='podpah',max_results=100,start_time=start,end_time=end)

dados = response.data

cur.execute('CREATE TABLE registros (texto TEXT,RT TEXT)')

for i in dados:
    texto = i.text
    if (texto[:2] == 'RT'):
        RT = 'S'
    else:
        RT = 'N'
    
    cur.execute("INSERT INTO registros (texto,RT) VALUES (?,?)",(texto,RT))
    
con.commit()        
con.close()