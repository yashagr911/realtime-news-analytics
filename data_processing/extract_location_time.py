import spacy

nlp = spacy.load("en_core_web_sm")

def extract_locations(text):
    doc = nlp(text)
    locations = [ent.text for ent in doc.ents if ent.label_ == "GPE"]
    return locations

# print(extract_locations("well, i just wanna go to Germany soon"))