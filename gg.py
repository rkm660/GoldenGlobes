import urllib2
from bs4 import BeautifulSoup
import json
import nltk
import re


tweets = []
categories = [
"best motion picture",
"best director",
"best actor",
"best actress",
"best supporting actor",
"best supporting actress",
"best screenplay",
"best original score",
"best original song",
"best foreign language film",
"best animated feature film",
"cecil b. demille award",
"best drama series",
"best comedy series",
"best actor in a television drama series",
"best actor in a television comedy series",
"best actress in a television drama series",
"best actress in a television drama series",
"best limited series or motion picture",
"best actor in a limited series or motion picture made for television",
"best actress in a limited series or motion picture made for television",
"best supporting actor in a limited series or motion picture made for television",
"best supporting actress in a limited series or motion picture made for television"]


def isActor(actor):
        url = "http://www.imdb.com/find?q=" + actor.replace(" ","%20") + "&&s=nm&&exact=true"
        try:
            content = urllib2.urlopen(url).read()
            soup = BeautifulSoup(content)
            raw = soup.find_all('table', attrs={'class':'findList'})[0].find('a')
            img = raw.find('img')
            if (raw and img['src'] != "http://ia.media-imdb.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB379389446_.png"):
                return True
            else:
                return False
        except:
            return False


def getRawTweets():
     print('start')
     jsonobj = json.load(open('gg15mini.json','r'))
     print('done')
     for i in range(100000):
         tweets.append(jsonobj[i]['text'])
     print('appended')


def isCat(tweet):
    t = tweet.lower()
    for c in categories:
        if c in t:
            return tweet
            break
    return ''
    
            
def getConsecCaps(tweet):
    if (tweet):
        pattern = r'(?=((?<![A-Za-z.])[A-Z][a-z.]*[\s-][A-Z][a-z.]*))'
        return (re.findall(pattern, tweet))



