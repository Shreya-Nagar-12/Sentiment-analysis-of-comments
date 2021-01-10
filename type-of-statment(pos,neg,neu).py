#Sentiment Analysis using VADER(Valance Aware Dictonary and sEntiment Reasoner)

#lexicon and rule based sentiment analysis tool that not only tells given word is +ve or -ve
# but also tells +ve or -ve score of that word.

#pip install vaderSentiment

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#function to print sentiment of given word/sentence
def sentiment_scores(sentence): 

    # Create a SentimentIntensityAnalyzer object. 
    sid_obj = SentimentIntensityAnalyzer() 

    # polarity_scores method of SentimentIntensityAnalyzer 
    # object gives a sentiment dictionary. 
    # which contains pos, neg, neu, and compound scores. 
    sentiment_dict = sid_obj.polarity_scores(sentence) 
     
    print("Overall sentiment dictionary is : ", sentiment_dict) 

    print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative") 

    print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral") 

    print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive") 

    print("Sentence Overall Rated As", end = " ") 

    # decide sentiment as positive, negative and neutral 
    if sentiment_dict['compound'] >= 0.05 : 
        print("Positive") 
  
    elif sentiment_dict['compound'] <= - 0.05 : 
        print("Negative") 

    else : 
        print("Neutral") 

  
 # Driver code 
sentence = input()
sentiment_scores(sentence) 

#OR

print("\n1st statement :") 
sentence = "I am very happy today" 
sentiment_scores(sentence) 

print("\n2nd Statement :") 
sentence = "study is going on as usual"
sentiment_scores(sentence) 

print("\n3rd Statement :") 
sentence = "Today i met an accident."
sentiment_scores(sentence) 