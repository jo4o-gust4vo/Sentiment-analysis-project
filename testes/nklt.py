from nltk.corpus import sentiwordnet as swn
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
#nltk.download('punkt')

'''
nltk.word_tokenize('Oi, tudo bem!')


print(nltk.word_tokenize('Oi, tudo bem!'))
print(nltk.sent_tokenize('oi, tudo bem!'))

'''

#nltk.download('vader_lexicon')


'''sia = SentimentIntensityAnalyzer()

sentimentos = sia.polarity_scores('love')

print(sentimentos)'''

# importa a biblioteca
import nltk

# baixa as stopwords
nltk.download('stopwords')

# para escolher as stopwords do português adicionamos a opçaõ de língua "portuguese"
stopwords = nltk.corpus.stopwords.words('portuguese')