import spacy
import pt_core_news_sm
npl = spacy.load('pt_core_news-sm')

doc = npl('Oi, tudo bem?')

print([w.text, w.pos for w in doc])