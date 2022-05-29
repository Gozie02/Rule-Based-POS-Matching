from Technical Skills import extract_tech
import spacy
nlp = spacy.load('en_core_web_sm')
from spacy.matcher import Matcher
import pandas as pd
df = pd.read_csv(r"C:/Users/uchei/OneDrive/Desktop/Raw_Skills_Dataset.csv")

df1['Skills'] = df['RAW DATA'].apply(lambda x: extract_tech(x))
df1 = df1[df1.apply(len) > 0]
