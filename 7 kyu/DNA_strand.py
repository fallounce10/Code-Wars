def DNA_strand(dna):
    dna_dict = {'A': 'T',
                'T': 'A',
                'G': 'C',
                'C': 'G'}
    
    comp_string = ""
    list_key = [i for i in dna_dict.keys()]
    
    for i in dna:
        if i in list_key:
            comp_string += dna_dict[i]
    
    return comp_string
