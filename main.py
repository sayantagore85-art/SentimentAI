# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import string
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

import tokenize

text = open('read.txt',encoding='utf-8').read()
lower_case = text.lower()
cleaned_text =lower_case.translate(str.maketrans('', '', string.punctuation))
tokenized_words = word_tokenize(cleaned_text,"english")


#stop_words =["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
           #   "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
           #   "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
          #    "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
           #   "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
          #    "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
        #      "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
        #      "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
        #      "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
        #      "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
final_words = []
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)

emotion_list=[]
with open('emotions.txt','r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",",'').replace("'", '').strip()
        word, emotion = clear_line.split(':')

        if word in final_words:
         emotion_list.append(emotion)
print(emotion_list)
w= Counter(emotion_list)
print(w)
def sentiment_analysis(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    neg=score['neg']
    pos=score['pos']
    if neg > pos:
        print("negative")
    elif pos > neg:
        print("positive")
sentiment_analysis(cleaned_text)
fig , ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()