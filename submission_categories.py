import praw
import pandas as pd

reddit = praw.Reddit(client_id = 'kKsgTaGVryypEw', client_secret = 'OtWk7p0-rqatKMyzYqkbkYoRAeafYA', username ='rscraper4work', password = 'purplepanda', user_agent='pelotonv1')

subreddit = reddit.subreddit('facebook')

hot_peloton = subreddit.controversial(limit=None)

author_list = []
id_list = []
link_flair_text_list = []
num_comments_list = []
score_list = []
title_list = []
upvote_ratio_list = []
selftext_list = []
created_utc_list = []

for sub in hot_peloton:
        author_list.append(sub.author)
        id_list.append(sub.id)
        link_flair_text_list.append(sub.link_flair_text)
        num_comments_list.append(sub.num_comments)
        score_list.append(sub.score)
        title_list.append(sub.title)
        upvote_ratio_list.append(sub.upvote_ratio)
        selftext_list.append(sub.selftext)
        created_utc_list.append(sub.created_utc)

df = pd.DataFrame({'ID':id_list, 
                   'Author':author_list, 
                   'Title':title_list,
                   'Count_of_Comments':num_comments_list,
                   'Upvote_Count':score_list,
                   'Upvote_Ratio':upvote_ratio_list,
                   'Flair':link_flair_text_list,
                   'Text':selftext_list,
                   'Created':created_utc_list,
                  })
df.to_csv('facebook_categories_controversial.csv', index = False)