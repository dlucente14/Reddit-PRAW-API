from IPython import display
import math
from pprint import pprint
import pandas as pd
import numpy as np
import nltk
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='darkgrid', context='talk', palette='Dark2')

import praw

reddit = praw.Reddit(client_id='S2go8WN6kexYRw',
                     client_secret='rDfhmuqlLH5hsAOwbDH7yFvoRHyFBg',
                     user_agent='pelotonv1')

headlines = set()

for submission in reddit.subreddit('facebook').controversial(limit=None):
    headlines.add(submission.selftext)
    display.clear_output()

from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

sia = SIA()
results = []

for line in headlines:
    pol_score = sia.polarity_scores(line)
    pol_score['headline'] = line
    results.append(pol_score)

pprint(results[:3], width=100)

df = pd.DataFrame.from_records(results)
df.head()

df['label'] = 0
df.loc[df['compound'] > 0.2, 'label'] = 1
df.loc[df['compound'] < -0.2, 'label'] = -1
df.head()

df2 = df[['headline', 'label']]
df2.to_csv('facebook_selftext_nlp_controversial.csv', mode='a', encoding='utf-8', index=False)