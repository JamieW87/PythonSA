#Import libraries. textblob is the sentiment analyser. tweepy imports tweets
#matplotlib is the graph tool used to plot the output
from textblob import TextBlob
import tweepy
import matplotlib.pyplot as plt

#Function that collects the percentages
def percentage(part, whole):
    return 100 * float(part)/float(whole)

#Setting variables for the auth information that allows us to access twitters API
consumerKey = "3DOvT3TjEgd16Yk7xvNxNjUMQ"
consumerSecret = "DeMxglGqNdO9A1xwE8PfI4IMTPFnL6jAihxunsA45zlxfwW9bk"
accessToken = "381544613-Zda1F8KbIZ0q1Eyz1azIpllKu9eimHaUkJNZpioa"
accessTokenSecret = "GwtenTAoU3Bki2F1MvnbNRxm3XahX0O8vRx8eFqC8SVoR"

#Connects to the twitter API
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

#Sets the user inputs. The keyword and how many tweets to display.
searchTerm = input("Enter Keyword/Hashtag to Search: ")
noOfSearchTerms = int(input("Set how many tweets you would like to analyse: "))

tweets = tweepy.Cursor(api.search, q=searchTerm).items(noOfSearchTerms)
    
positive = 0
negative = 0
neutral = 0
polarity = 0

for tweet in tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity

    if (analysis.sentiment.polarity == 0):
        neutral += 1
    elif (analysis.sentiment.polarity < 0.00):
        negative += 1
    elif (analysis.sentiment.polarity > 0.00):
        positive += 1
    
#Shows the percentages of how many tweets per emotion per how many search terms.
positive = percentage(positive, noOfSearchTerms)
negative = percentage(negative, noOfSearchTerms)
neutral = percentage(neutral, noOfSearchTerms)
polarity = percentage(polarity, noOfSearchTerms)

#Formats the polarity to show to 2 decimal places
positive = format(positive, '.2f')
negative = format(negative, '.2f')
neutral = format(neutral, '.2f')

print("How people are reacting on " + searchTerm + "by analyzing" + str(noOfSearchTerms) + " Tweets.")
if (polarity == 0 ):
    print("Neutral")
elif (polarity < 0.00 ):
    print("Negative")
elif (polarity > 0.00 ):
    print("Postitive")

#For in-python pie chart
labels = ['Positive [' + str(positive)+ '%]'], ['Neutral [' + str(neutral)+ '%]'], ['Negative [' + str(negative)+ '%]']
sizes = [positive, neutral, negative]
colors = ['yellowgreen', 'gold', 'red']
patches, texts = plt.pie(sizes, colors=colors, startangle=90)
plt.legend(patches, labels, loc="best")
plt.title('How people are reacting on '+searchTerm+' by analysing '+str(noOfSearchTerms)+' tweets.')
plt.axis('equal')
plt.tight_layout()
plt.show()
    
