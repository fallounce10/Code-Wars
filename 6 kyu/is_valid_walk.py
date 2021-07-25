def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    
    pos_i = 0
    pos_j = 0
    
    for i in walk:
        if i == 'n':
            pos_i += 1
        elif i == 's':
            pos_i -= 1
        elif i == 'e':
            pos_j -= 1
        elif i == 'w':
            pos_j += 1
                
    return (pos_i, pos_j) == (0,0)
