def array_diff(a, b):
    if len(a) == 0:
        return []
        
    for i in b:
        while (i in a):
          a.remove(i)
                
    return a
