import spacy
nlp = spacy.load('en_core_web_sm')
from spacy.matcher import Matcher
import pandas as pd

def extract_tech(text):
    doc = nlp(text)
    skills = []
    if len(text.split()) == 1:
        pattern = [{'POS': 'PROPN'}]
        matcher = Matcher(nlp.vocab)
        matcher.add("Prop", [pattern])
        matches = matcher(doc)
        for match_id, start, end in matches:
            span = doc[start:end]
            skills.append(span.text)
            
    elif len(text.split()) == 2:
        pattern = [[{'POS': 'PROPN'}, {'POS': 'PROPN'}],
                    [{'POS': 'NOUN'}, {'POS': 'VERB'}],
                   [{'POS': 'PROPN'}, {'POS': 'NOUN'}],
                   [{'POS': 'NOUN'}, {'POS': 'NUM'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'SYM'}, {'POS': 'PROPN'}, {'POS': 'SYM'}, {'POS': 'PROPN'}]]
        matcher = Matcher(nlp.vocab)
        matcher.add("Prop1", [pattern[0]])
        matcher.add("Prop12", [pattern[1]])
        matcher.add("Prop13", [pattern[2]])
        matcher.add("Prop14", [pattern[3]])
        matcher.add("Prop15", [pattern[4]])
        matches = matcher(doc)
        for match_id, start, end in matches:
            span = doc[start:end]
            skills.append(span.text)
            
    elif len(text.split()) == 3:
        pattern = [[{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}],
                   [{'POS': 'NOUN'}, {'POS': 'CCONJ'}, {'POS': 'NOUN'}],
                   [{'POS': 'PROPN'}, {'POS': 'SYM'}, {'POS': 'PROPN'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}],
                   [{'POS': 'NOUN'}, {'POS': 'NOUN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'NOUN'}]]
        matcher = Matcher(nlp.vocab)
        matcher.add("Prop2", [pattern[0]])
        matcher.add("Prop21", [pattern[1]])
        matcher.add("Prop22", [pattern[2]])
        matcher.add("Prop23", [pattern[3]])
        matcher.add("Prop24", [pattern[4]])
        matcher.add("Prop25", [pattern[5]])
        matcher.add("Prop26", [pattern[6]])
        matches = matcher(doc)
        for match_id, start, end in matches:
            span = doc[start:end]
            skills.append(span.text)
            
    elif len(text.split()) == 4:
        pattern = [[{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}],
                   [{'POS': 'NOUN'}, {'POS': 'ADP', 'OP': '?'}, {'POS': 'NOUN'}, {'POS': 'NOUN'}],
                   [{'POS': 'NOUN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'SYM'}, {'POS': 'PROPN'}], 
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}],
                   [{'POS': 'NOUN'}, {'POS': 'PUNCT'}, {'POS': 'NOUN'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}],
                   [{'POS': 'NUM'}, {'POS': 'PROPN'}, {'POS': 'SYM'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'NOUN'}, {'POS': 'NOUN'}, {'POS': 'NOUN'}]]
        matcher = Matcher(nlp.vocab)
        matcher.add("Prop2", [pattern[0]])
        matcher.add("Prop21",[pattern[1]])
        matcher.add("Prop22", [pattern[2]])
        matcher.add("Prop23", [pattern[3]])
        matcher.add("Prop24", [pattern[4]])
        matcher.add("Prop25", [pattern[5]])
        matcher.add("Prop26", [pattern[6]])
        matcher.add("Prop27", [pattern[7]])
        matcher.add("Prop28", [pattern[8]])
        matcher.add("Prop29", [pattern[9]])
        matches = matcher(doc)
        for match_id, start, end in matches:
            span = doc[start:end]
            skills.append(span.text)
            
    elif len(text.split()) == 5:
        pattern = [[{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'CCONJ'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}],
                   [{'POS': 'NOUN'}, {'POS': 'SYM'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'CCONJ'}, {'POS': 'NOUN'}],
                   [{'POS': 'PROPN'}, {'POS': 'ADJ'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'NOUN'}],
                   [{'POS': 'PROPN'}, {'POS': 'ADJ'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}],
                   [{'POS': 'NOUN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}],
                   [{'POS': 'PROPN'}, {'POS': 'SYM'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'CCONJ'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}]]
                                                                                                              
        matcher = Matcher(nlp.vocab)
        matcher.add("Prop3", [pattern[0]])
        matcher.add("Prop31", [pattern[1]])
        matcher.add("Prop32", [pattern[2]])
        matcher.add("Prop33", [pattern[3]])
        matcher.add("Prop34", [pattern[4]])
        matcher.add("Prop35", [pattern[5]])
        matcher.add("Prop36", [pattern[6]])
        matcher.add("Prop37", [pattern[7]])
        matches = matcher(doc)
        for match_id, start, end in matches:
            span = doc[start:end]
            skills.append(span.text)
            
    elif len(text.split()) == 6:
        pattern = [[{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'NOUN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'ADJ'}, {'POS': 'NOUN'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'CCONJ'}, {'POS': 'PROPN'}, {'POS': 'NOUN'}],
                   [{'POS': 'NOUN'}, {'POS': 'NOUN'}, {'POS': 'PUNCT'}, {'POS': 'NOUN'}, {'POS': 'CCONJ'}, {'POS': 'NOUN'}],
                   [{'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'NOUN'}, {'POS': 'NOUN'}, {'POS': 'NOUN'}]]
        matcher = Matcher(nlp.vocab)
        matcher.add("Prop4", [pattern[0]])
        matcher.add("Prop41", [pattern[1]])
        matcher.add("Prop42", [pattern[2]])
        matcher.add("Prop43", [pattern[3]])
        matcher.add("Prop44", [pattern[4]])
        matches = matcher(doc)
        for match_id, start, end in matches:
            span = doc[start:end]
            skills.append(span.text)
            
    return skills
