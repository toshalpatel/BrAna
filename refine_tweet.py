f = open('tweets_apple.txt','r')

tweet=[]
with open('tweets_apple.txt','r',encoding='ISO-8859-1') as f:
    tweet.append( f.readlines())
print(tweet)
