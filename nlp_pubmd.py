import nltk
import numpy
import matplotlib.pyplot as plt

with open("/Users/miguel/Desktop/data_from_pubmed.txt","r") as file:
    raw_papers = file.read().replace('\n', '') #opens the .txt file and converted in a string format

from nltk.tokenize import word_tokenize
token_words = nltk.word_tokenize(raw_papers)
fn_dt = nltk.Text(token_words) #tokenize all the words in file for further ooccurances search

target_words = ['cancer', 'acetylation', 'leukemia'] #set the target word for the dispersion plot

plt.figure(figsize=(20, 8)) #defines the size of the plot
fn_dt.dispersion_plot(target_words)
plt.savefig('a.svg') #saves the plot as a .svg file