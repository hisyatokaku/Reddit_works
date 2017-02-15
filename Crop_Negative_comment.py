#coding:utf-8
import requests
import requests.auth
import praw
from praw.models import MoreComments

TARGET_SUB = "askreddit"
LOG_DIR    = 


def get_comments_scores(reddit,subreddit):
    submission = reddit.submission(id='%s'%(subreddit.id))
    submission.comments.replace_more(limit=None)
    comment_queue = submission.comments[:]
    res = []
    counter = 0
    while comment_queue:
        counter += 1
        comment = comment_queue.pop()
        if isinstance(comment,MoreComments):
            continue
        res.append(comment)
        #print comment.score,comment.body
        #print comment.body
        comment_queue.extend(comment.replies)
        if counter % 100 == 0:
            print "processed:{}".format(counter)
    return res


def get_subreddit(reddit,TARGET):
    subreddit = reddit.subreddit(TARGET)
    counter = 0
    res = []
    for submission in subreddit.hot(limit = 10):
        res.append(submission)
    return res

def get_reddit():
    client_auth =
    post_data =
    headers =
    
    response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
    response.json()
    my_user_agent = 
    my_client_id = 
    my_client_secret = 
    
    my_username = 
    my_password = 

    reddit = praw.Reddit(user_agent=my_user_agent,
                         client_id=my_client_id,
                         client_secret=my_client_secret,
                         username=my_username,
                         password=my_password)
    return reddit

def main():

    reddit = get_reddit()
    subreddits = get_subreddit(reddit,TARGET_SUB)    
    comments_list = get_comments_scores(reddit,subreddits[0])

    with open(LOG_DIR+str(subreddits[0].title),'w') as f:
        for comment in comments_list:
            score = comment.score
            com = comment.body
            com = com.replace('\n',' ')
            f.write(str(score)+' ')
            f.write(com.encode('utf-8'))
            f.write('\n')

if __name__ =="__main__":
    main()
