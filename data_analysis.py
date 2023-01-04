# Code snippet for data analysis of different text files
import glob
import os
from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd
import helper as hp
# Initalizations
path = 'files2'
l={'neg','pos'}
text_analysis_list =[]
sia = SentimentIntensityAnalyzer()
# Loop for each text file
for filename in glob.glob(os.path.join(path, '*.txt')):
   with open(os.path.join(os.getcwd(), filename), 'r', encoding ="utf8",) as f:
       text = f.read()
       preprocess_text = hp.text_prep(text)
       Total_words = len(preprocess_text)
       data = ' '.join([str(elem) for elem in preprocess_text])
       result=sia.polarity_scores(data)
       neg_score = result['neg']
       pos_score = result['pos']
       d = {key: result[key] for key in l}
       d['POLARITY SCORE'] = hp.polarity_score(neg_score,pos_score)
       Total_words = len(preprocess_text)
       d['SUBJECTIVITY SCORE'] = hp.subjectivity_score(neg_score, pos_score, Total_words)
       average_sentence_length = float(Total_words / hp.total_sentences(text))
       d['AVG SENTENCE LENGTH'] = average_sentence_length
       d['PERCENTAGE OF COMPLEX WORDS'] = hp.percentage_of_complex_words(preprocess_text)
       d['FOG INDEX'] = hp.fog_index(preprocess_text, average_sentence_length)
       d['AVG NUMBER OF WORDS PER SENTENCE'] = (Total_words / hp.total_sentences(text))
       d['COMPLEX WORD COUNT'] = len(hp.complex_word_count(preprocess_text))
       d['WORD COUNT'] = Total_words
       d['SYLLABLE PER WORD'] = hp.avg_syllables_per_word(str(preprocess_text))
       d['PERSONAL PRONOUNS'] = hp.personal_pronoun(text)
       d['AVG WORD LENGTH'] = hp.average_word_count(text)
       text_analysis_list.append(d)

# Saving data into excel Output,xlsx
text_analysis_output = pd.DataFrame.from_dict(text_analysis_list)
df = pd.read_excel('Input.xlsx',index_col=False)
result = pd.concat([df,text_analysis_output], axis=1)
result.to_excel("Output.xlsx", index=False)