from Soft Skills import soft_skills
import spacy
nlp = spacy.load('en_core_web_sm')
from spacy.matcher import Matcher
import pandas as pd
df = pd.read_csv(r"C:/Users/uchei/OneDrive/Desktop/Raw_Skills_Dataset.csv")
df2['Soft Skills'] = df['RAW DATA'].apply(lambda x:soft_skills(x))
#eliminate all empty values
df2 = df2[df2.apply(len) > 0]
