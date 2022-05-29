def soft_skills(text):
    doc = nlp(text)
    soft_skills = []
    if len(text.split()) == 1:
        pattern = [{'POS': 'NOUN'}]
        matcher = Matcher(nlp.vocab)
        matcher.add("soft", [pattern])
        matches = matcher(doc)
        for match_id, start, end in matches:
            span = doc[start:end]
            soft_skills.append(span.text)
    elif len(text.split()) == 2:
        pattern = [[{'POS': 'ADJ'}, {'POS': 'NOUN'}],
                   [{'POS': 'NOUN'}, {'POS': 'NOUN'}]]
        matcher = Matcher(nlp.vocab)
        matcher.add("soft", [pattern[0]])
        matcher.add("soft", [pattern[1]])
        matches = matcher(doc)
        for match_id, start, end in matches:
            span = doc[start:end]
            soft_skills.append(span.text)
    elif len(text.split()) == 3:
        pattern = [{'POS':'NOUN'},{'POS': 'PART'}, {'POS': 'VERB'}]
        matcher = Matcher(nlp.vocab)
        matcher.add("soft", [pattern])
        matches = matcher(doc)
        for match_id, start, end in matches:
            span = doc[start:end]
            soft_skills.append(span.text)
    return soft_skills
