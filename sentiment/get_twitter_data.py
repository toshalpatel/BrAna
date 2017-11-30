import argparse
import urllib
import urllib2
import json
import datetime
import random
import os
import pickle
from datetime import timedelta
import oauth2

class TwitterData:
    #start __init__
    def __init__(self):
        self.currDate = datetime.datetime.now()
        self.weekDates = []
        self.weekDates.append(self.currDate.strftime("%Y-%m-%d"))
        for i in range(1,7):
            dateDiff = timedelta(days=-i)
            newDate = self.currDate + dateDiff
            self.weekDates.append(newDate.strftime("%Y-%m-%d"))
        #end loop
    #end

    #start getWeeksData
    def getTwitterData(self, keyword, time):
        self.weekTweets = {}
        if(time == 'lastweek'):
            for i in range(0,6):
                params = {'since': self.weekDates[i+1], 'until': self.weekDates[i]}
                self.weekTweets[i] = self.getData(keyword, params)
            #end loop
            
            #Write data to a pickle file
            filename = 'data/weekTweets/weekTweets_'+urllib.unquote(keyword.replace("+", " "))+'_'+str(int(random.random()*10000))+'.txt'
            outfile = open(filename, 'wb')        
            pickle.dump(self.weekTweets, outfile)        
            outfile.close()
        elif(time == 'today'):
            for i in range(0,1):
                params = {'since': self.weekDates[i+1], 'until': self.weekDates[i]}
                self.weekTweets[i] = self.getData(keyword, params)
            #end loop
        return self.weekTweets
    '''
        inpfile = open('data/weekTweets/weekTweets_obama_7303.txt')
        self.weekTweets = pickle.load(inpfile)
        inpfile.close()
        return self.weekTweets
    '''
    #end
    
    
    
    #start getTwitterData
    def getData(self, keyword, params = {}):
        tweet=[]
        count=0
        with open('tweets_apple.txt','r',encoding='ISO-8859-1') as f:
          if count<50:
            tweet.append( f.readlines())
            count=count+1
        print "number of tweets: 50"
    #end    

#end class
