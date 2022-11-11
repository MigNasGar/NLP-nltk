import nltk
import numpy
import matplotlib as mpl
mpl.use('tkagg')
import matplotlib.pyplot as plt

with open("data_from_pubmed.txt","r" ,encoding='utf-8') as file:
    raw_papers = file.read().replace('\n', '') #opens the .txt file and converted in a string format

from nltk.tokenize import word_tokenize
token_words = nltk.word_tokenize(raw_papers)
fn_dt = nltk.Text(token_words) #tokenize all the words in file for further ooccurances search

target_words = ['cancer', 'acetylation', 'leukemia'] #set the target word for the dispersion plot

plt.figure(figsize=(30, 12), dpi=200) #defines the size and resolution of the plot
word_plot = fn_dt.dispersion_plot(target_words)
plt.plot(word_plot)
plt.show() #shows the plot