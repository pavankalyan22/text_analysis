# Helper functions required for text analysis 
from textstat.textstat import textstatistics
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import sent_tokenize
import re


lemma = WordNetLemmatizer()
stop_words = stopwords.words('english')

def polarity_score(x, y):
     output = (y - x)/((y + x) + 0.000001)
     return  output


def subjectivity_score(x,y,z):
     output =  ((y + x)/ ((z) + 0.000001))
     return output


## Function to remove stopwords
def text_prep(x):
     corp      = str(x).lower() 
     corp      = re.sub('[^a-zA-Z]+',' ', corp).strip() 
     tokens    = word_tokenize(corp)
     words     = [t for t in tokens if t not in stop_words]
     lemmatize = [lemma.lemmatize(w) for w in words]
     return lemmatize
## Function to calculate total sentences
def total_sentences(x):
     number_of_sentences = sent_tokenize(x)
     return  len(number_of_sentences)
## Function to calculate average word count
def average_word_count(x):
     filtered = ''.join(filter(lambda x: x not in '".,;!-:', x))# removing ! mark if present
     words    = [word for word in filtered.split() if word]
     avg      = sum(map(len, words))/len(words)
     return avg
## Returns syllabe count
def syllables_count(word):
    	return textstatistics().syllable_count(word)

# Returns the average number of syllables per
# word in the text
def avg_syllables_per_word(x):
	syllable = syllables_count(x)
	return syllable

# Returns the count of personal pronoun in the text
def personal_pronoun(x):
     pronoun_list = 'I|we|my|ours|us'
     personal_pronoun_count = len(re.findall(pronoun_list, x, flags=re.IGNORECASE))
    
     return personal_pronoun_count
# Returns the count of complex word in the text
def complex_word_count(x):
     complex_words_set=set()
     for word in x:
          syllable_count = syllables_count(str(x))
          if (syllable_count >= 2):
                complex_words_set.add(word)

     return complex_words_set
# Returns the percentage of complex words in the text
def percentage_of_complex_words(x):
     return float(len(complex_word_count(x))/len(x))
# Returns fog index
def fog_index(x,y):
     return 0.4 * ( y+ percentage_of_complex_words(x))

