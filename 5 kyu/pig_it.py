from string import punctuation

def pig_it(text):
    text = text.split()
    return_text = []

    for word in text:
        a = word[0]
        b = word[1:]
        for i in [a, b]:
            if i in punctuation:
                continue
        new_sentence = b + a + "ay"
        return_text.append(new_sentence)

    return ' '.join(return_text)
