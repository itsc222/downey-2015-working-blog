import nltk

sample_sentence = "Zimeng is handsome."

def analyze_text(input):
    tokens = nltk.word_tokenize(input)
    tagged = nltk.pos_tag(tokens)
    output = f"Tokenized and Tagged Sentence: {tagged}"
    # tagged = [nltk.pos_tag(word) for word in tokens] #This produces an error because the word_tokenized function requires a list as its parameter.
    # output = "Tokenized and Tagged Sentence:", tagged
    return(output)

print(analyze_text(sample_sentence))
    