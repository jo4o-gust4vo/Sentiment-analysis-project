from nltk.corpus import sentiwordnet as swn #importing the sentiwordnet
from nltk.tag.perceptron import PerceptronTagger #importing a tagger
from nltk.tokenize import word_tokenize #of course tokenizing the input
from operator import itemgetter
import nltk
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_por')
type = {
    "JJ": "a",
    "VBP": "v",
    "VBZ": "v",
    "VBN": "v",
    "VBG": "v",
    "VBD": "v",
    "NN": "n",
    "RB": "r",
}

def Polarity(textEN):
    try:
        if textEN is not None:
            textEN = textEN.lower()
            pos = 0
            neg = 0
            obj = 0
            tagger=PerceptronTagger() #init the tagger in default mode
            for word, tag in tagger.tag(word_tokenize(textEN)): #change the sentences for other stuff
                if tag == "JJ" or tag == "VBP" or tag == "VBZ" or tag == "VBN" or tag == "VBPG" or tag == "VBD" or \
                        tag == "NN" or tag == "RB": #check if the word is an adjective
                    synset = list(swn.senti_synsets(word, type[tag])) #get the most likely synset
                    for s in synset:
                        if s.obj_score() < 1:
                            pos += s.pos_score()
                            neg += s.neg_score()
                            obj += s.obj_score()

            if pos == neg:
                return 'neutral'
            else:
                result = [("positive", pos), ("negative", neg)]
                result = sorted(result, key=itemgetter(1), reverse=True)
                result = itemgetter(0)(result[0])
                return result
        else:
            return ''
    except Exception as e:
        return e
    

print(Polarity('odeio'))