from gensim.summarization import summarize
import nltk
from textblob import TextBlob 
# nltk.download()

para = '''Dr. APJ Abdul Kalam was indeed one of the most humble, intelligent, wise, selfless, 
loving, and lovable leaders ever born. He was born on 15 October 1931 in Rameswaram, 
Tamil Nadu. He was the 11th President of India and served the country for one term. 
Not only this, but he also is one of the most famous scientists who have worked with highly
famous organizations like DRDO (Defense Research and Development Organization)
and ISRO (Indian Space Research Organization) in his career.

He was a true gem and a person with no haters. But let us first know a little more about him. 
His full name was Avul Pakir Jainulabdeen Abdul Kalam. He was born in a middle-class 
Muslim family. Since the beginning of his days, he was a very hardworking and diligent person.
In his early childhood, he helped his family to earn livelihood along with the studies. 
Being very intelligent and promising, he started his career and life soon.'''

# words = nltk.word_tokenize(para)
# print(len(words))

def get_summary(para):
    summary = summarize(para, word_count=100)
    title = summarize(para, word_count=10)
    return summary, title


def find_Sentiment(val):                                                                                                               
    if val<=0.1 and val>-0.1:
        return 'Neutral'
    elif val>0.1:
        return 'Positive'
    else:
        return 'Negative'

def get_sentiment(para):                                                      
    sent = []                                                                    
    
    sentences = nltk.sent_tokenize(para)
    for sentence in sentences:
      analysis = TextBlob(sentence)
      sentiment = find_Sentiment(analysis.sentiment.polarity)
    #   print(sentiment)
      sent.append(sentiment)
    return sent

summary, title = get_summary(para)
print("SUMMARY: " + summary)
print("TITLE: " + title)
sentiment_answer = max(get_sentiment(summary))
print('SENTIMENT: ' + sentiment_answer)