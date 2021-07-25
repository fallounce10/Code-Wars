def is_isogram(string):
    my_dict = {}
    
    for i in range(len(string)):
        if string[i] not in my_dict:
            my_dict[string[i]] = 1
        else:
            my_dict[string[i]] += 1
        
    for v in my_dict.values():
        if v > 1:
            return False
    return True
