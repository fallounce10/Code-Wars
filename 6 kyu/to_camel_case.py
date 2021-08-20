def to_camel_case(text):
    word = text.replace("-", " ").replace("_", " ")
    word = word.split()
    if len(text) == 0:
        return text
    
    return word[0] + ''.join(i.capitalize() for i in word[1:])
