from nltk.corpus import sentiwordnet as swn
import nltk

#nltk.download('sentiwordnet')
#nltk.download('wordnet')
frase = swn.senti_synsets('GOOD')
print(frase)