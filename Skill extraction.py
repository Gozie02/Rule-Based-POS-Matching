def extract_tech(text):
    doc = nlp(text)
    skills = []
    if len(text.split()) == 1:
        pattern = [[{'POS': 'PROPN'}],
                   [{'POS': 'INTJ'}],
                   [{'POS': 'VERB'}],
                   [{'POS': 'ADJ'}],
                   [{'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'NOUN'}],
                   [{'POS': 'ADV'}],
                   [{'POS': 'PROPN'}, {'POS': 'SYM'}, {'POS': 'NOUN'}],
                   [{'POS': 'VERB'}, {'POS': 'PUNCT'}, {'POS': 'VERB'}]]
        matcher = Matcher(nlp.vocab)
        matcher.add('rule_1', pattern, on_match = None)
        matches = matcher(doc)
        for match_id, start, end in matches:
            span = doc[start:end]
            skills.append(span.text)
            
    elif len(text.split()) == 2:
        pattern = [[{'POS': 'PROPN'}, {'POS': 'PROPN'}],
                   [{'POS': 'ADJ'}, {'POS': 'ADJ'}],
                   [{'POS': 'NOUN'}, {'POS': 'VERB'}],
                   [{'POS': 'PROPN'}, {'POS': 'NOUN'}],
                   [{'POS': 'NOUN'}, {'POS': 'NUM'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'SYM'}, {'POS': 'PROPN'}, {'POS': 'SYM'}, {'POS': 'PROPN'}],
                   [{'POS': 'VERB'}, {'POS': 'PROPN'}, {'POS': 'SYM'}, {'POS': 'PROPN'}],
                   [{'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}],
                   [{'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}],
                   [{'POS': 'PROPN'}, {'POS': 'VERB'}],
                   [{'POS': 'INTJ'}, {'POS': 'NOUN'}],
                   [{'POS': 'NUM'}, {'POS': 'NOUN'}],
                   [{'POS': 'NOUN'}, {'POS': 'PROPN'}],
                   [{'POS': 'ADJ'}, {'POS': 'PROPN'}],
                   [{'POS': 'PROPN'}, {'POS': 'ADJ'}, {'POS': 'ADJ'}, {'POS': 'NOUN'}],
                   [{'POS': 'ADP'}, {'POS': 'NOUN'}],
                   [{'POS': 'ADJ'}, {'POS': 'VERB'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}],
                   [{'POS': 'PROPN'}, {'POS': 'ADP'}],
                   [{'POS': 'VERB'}, {'POS': 'NOUN'}],
                   [{'POS': 'VERB'}, {'POS': 'VERB'}],
                   [{'POS': 'PROPN'}, {'POS': 'PUNCT'}],
                   [{'POS': 'VERB'}, {'POS': 'PROPN'}],
                   [{'POS': 'NOUN'}, {'POS': 'PUNCT'}, {'POS': 'ADP'}, {'POS': 'PUNCT'}, {'POS': 'NOUN'}, {'POS': 'NOUN'}],
                   [{'POS': 'PROPN'}, {'POS': 'SYM'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}],
                   [{'POS': 'NOUN'}, {'POS': 'SYM'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}],
                   [{'POS': 'PROPN'}, {'POS': 'SYM'}, {'POS': 'NOUN'}, {'POS': 'PUNCT'}, {'POS': 'NOUN'}, {'POS': 'NOUN'}],
                   [{'POS': 'PUNCT'}, {'POS': 'PROPN'}],
                   [{'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}]]
        matcher = Matcher(nlp.vocab)
        matcher.add('rule_2', pattern, on_match = None)
        matches = matcher(doc)
        for match_id, start, end in matches:
            span = doc[start:end]
            skills.append(span.text)
            
    elif len(text.split()) == 3:
        pattern = [[{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'NUM'}],
                   [{'POS': 'NOUN'}, {'POS': 'CCONJ'}, {'POS': 'NOUN'}],
                   [{'POS': 'PROPN'}, {'POS': 'SYM'}, {'POS': 'PROPN'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}],
                   [{'POS': 'NOUN'}, {'POS': 'NOUN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}],
                   [{'POS': 'NOUN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'NOUN'}, {'POS': 'PUNCT'}],
                   [{'POS': 'NOUN'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'NOUN'}],
                   [{'POS': 'NOUN'}, {'POS': 'NOUN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}],
                   [{'POS': 'ADJ'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'SYM'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}],
                   [{'POS': 'PROPN'}, {'POS': 'SYM'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}],
                   [{'POS': 'NOUN'}, {'POS': 'ADP'}, {'POS': 'NOUN'}],
                   [{'POS': 'PROPN'}, {'POS': 'ADP'}, {'POS': 'NOUN'}],
                   [{'POS': 'NOUN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}],
                   [{'POS': 'NOUN'}, {'POS': 'PROPN'}, {'POS': 'NOUN'}],
                   [{'POS': 'NOUN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'VERB'}],
                   [{'POS': 'PROPN'}, {'POS': 'NOUN'}, {'POS': 'NOUN'}],
                   [{'POS': 'PROPN'}, {'POS': 'NOUN'}, {'POS': 'PROPN'}],
                   [{'POS': 'NOUN'}, {'POS': 'VERB'}, {'POS': 'NOUN'}],
                   [{'POS': 'VERB'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}],
                   [{'POS': 'ADV'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}],
                   [{'POS': 'NOUN'}, {'POS': 'PROPN'}, {'POS': 'VERB'}],
                   [{'POS': 'NOUN'}, {'POS': 'PUNCT'}, {'POS': 'NOUN'}],
                   [{'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'X'}],
                   [{'POS': 'PROPN'}, {'POS': 'ADJ'}, {'POS': 'NOUN'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}],
                   [{'POS': 'PROPN'},{'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}],
                   [{'POS': 'PROPN'},{'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'SYM'}, {'POS': 'PROPN'}, {'POS': 'SYM'}, {'POS': 'PROPN'}, {'POS': 'SYM'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}]]
        matcher = Matcher(nlp.vocab)
        matcher.add('rule_3', pattern, on_match = None)
        matches = matcher(doc)
        for match_id, start, end in matches:
            span = doc[start:end]
            skills.append(span.text)
            
    elif len(text.split()) == 4:
        pattern = [[{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}],
                   [{'POS': 'PROPN'}, {'POS': 'VERB'}, {'POS': 'NOUN'}, {'POS': 'NOUN'}],
                   [{'POS': 'NOUN'}, {'POS': 'ADP', 'OP': '?'}, {'POS': 'NOUN'}, {'POS': 'NOUN'}],
                   [{'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'VERB'}, {'POS': 'NOUN'}],
                   [{'POS': 'ADJ'}, {'POS': 'AUX'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}],
                   [{'POS': 'NOUN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'SYM'}, {'POS': 'PROPN'}], 
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}],
                   [{'POS': 'NOUN'}, {'POS': 'PUNCT'}, {'POS': 'NOUN'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}],
                   [{'POS': 'NUM'}, {'POS': 'PROPN'}, {'POS': 'SYM'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'NOUN'}, {'POS': 'NOUN'}, {'POS': 'NOUN'}]]
        matcher = Matcher(nlp.vocab)
        matcher.add('rule_4', pattern, on_match = None)
        matches = matcher(doc)
        for match_id, start, end in matches:
            span = doc[start:end]
            skills.append(span.text)
            
    elif len(text.split()) == 5:
        pattern = [[{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'CCONJ'}, {'POS': 'PROPN'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'CCONJ'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}],
                   [{'POS': 'PROPN'}, {'POS': 'AUX'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}],
                   [{'POS': 'NOUN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}],
                   [{'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}],
                   [{'POS': 'NOUN'}, {'POS': 'VERB'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}],
                   [{'POS': 'NOUN'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}],
                   [{'POS': 'NOUN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'NOUN'}, {'POS': 'PUNCT'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'NOUN'}, {'POS': 'NOUN'}, {'POS': 'NOUN'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}],
                   [{'POS': 'PROPN'}, {'POS': 'NOUN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}],
                   [{'POS': 'NOUN'}, {'POS': 'NOUN'}, {'POS': 'ADP'}, {'POS': 'PROPN'}, {'POS': 'NUM'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'ADP'}, {'POS': 'PROPN'}],
                   [{'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'CCONJ'}, {'POS': 'NOUN'}],
                   [{'POS': 'NOUN'}, {'POS': 'SYM'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'CCONJ'}, {'POS': 'NOUN'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'ADP'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}],
                   [{'POS': 'PROPN'}, {'POS': 'ADJ'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'NOUN'}],
                   [{'POS': 'PROPN'}, {'POS': 'ADJ'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}],
                   [{'POS': 'NOUN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}],
                   [{'POS': 'PROPN'}, {'POS': 'SYM'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'CCONJ'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}]]
                                                                                                              
        matcher = Matcher(nlp.vocab)
        matcher.add('rule_5', pattern, on_match = None)
        matches = matcher(doc)
        for match_id, start, end in matches:
            span = doc[start:end]
            skills.append(span.text)
            
    elif len(text.split()) == 6:
        pattern = [[{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'ADP'}, {'POS': 'PROPN'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'CCONJ'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'NUM'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'NOUN'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'CCONJ'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}],
                   [{'POS': 'VERB'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'NOUN'}],
                   [{'POS': 'PROPN'}, {'POS': 'NUM'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'NOUN'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'ADP'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'NOUN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}],
                   [{'POS': 'ADJ'}, {'POS': 'SYM'}, {'POS': 'ADJ'}, {'POS': 'SYM'}, {'POS': 'ADJ'}, {'POS': 'NOUN'}],
                   [{'POS': 'NOUN'}, {'POS': 'ADP'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'ADJ'}, {'POS': 'NOUN'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'CCONJ'}, {'POS': 'PROPN'}, {'POS': 'NOUN'}],
                   [{'POS': 'NOUN'}, {'POS': 'NOUN'}, {'POS': 'PUNCT'}, {'POS': 'NOUN'}, {'POS': 'CCONJ'}, {'POS': 'NOUN'}],
                   [{'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'NOUN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}],
                   [{'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'NOUN'}, {'POS': 'NOUN'}, {'POS': 'NOUN'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}],
                   [{'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'NOUN'}, {'POS': 'PUNCT'}, {'POS': 'NOUN'}, {'POS': 'SYM'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'CCONJ'}, {'POS': 'PROPN'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'NOUN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'ADJ'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'NOUN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'X'}, {'POS': 'PUNCT'}],
                   [{'POS': 'NOUN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'ADP'}, {'POS': 'PROPN'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PUNCT'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'NUM'}, {'POS': 'NOUN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}],
                   [{'POS': 'NOUN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'ADP'}, {'POS': 'NOUN'}],
                   [{'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'NOUN'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'NOUN'}],
                   [{'POS': 'ADJ'}, {'POS': 'NOUN'}, {'POS': 'NOUN'}, {'POS': 'CCONJ'}, {'POS': 'NOUN'}, {'POS': 'PROPN'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'CCONJ'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS':'PROPN'}]]
        matcher = Matcher(nlp.vocab)
        matcher.add('rule_6', pattern, on_match = None)
        matches = matcher(doc)
        for match_id, start, end in matches:
            span = doc[start:end]
            skills.append(span.text)
    
    elif len(text.split()) == 7:
        pattern = [[{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'ADP'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}],
                   [{'POS': 'PROPN'}, {'POS': 'VERB'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'CCONJ'}, {'POS': 'VERB'}],
                   [{'POS': 'NOUN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'NUM'}, {'POS': 'PUNCT'}, {'POS': 'ADJ'}, {'POS': 'PROPN'}],
                   [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PUNCT'}, {'POS': 'CCONJ'}, {'POS': 'NOUN'}]]
        matcher = Matcher(nlp.vocab)
        matcher.add('rule_7', pattern, on_match = None)
        matches = matcher(doc)
        for match_id, start, end in matches:
            span = doc[start:end]
            skills.append(span.text)
    return skills
