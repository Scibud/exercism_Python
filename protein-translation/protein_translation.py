def proteins(strand):

    # Find the length of strand 
    length = len(strand)

    #Initilize the list to save
    pro=[]
    trans =[]

    #Initilize dict to save and for checking codons
    codon= {'AUG':'Methionine', 'UUU':'Phenylalanine', 'UUC':'Phenylalanine', 'UUA':'Leucine',
            'UUG':'Leucine','UCU':'Serine', 'UCC':'Serine', 'UCA':'Serine', 'UCG':'Serine',
            'UAU':'Tyrosine', 'UAC':'Tyrosine', 'UGU':'Cysteine', 'UGC':'Cysteine',
            'UGG':'Tryptophan'
            }
         
    #Make a list of sliced 3 letter codons
    for i in range (0,length,3):
        pro.append(strand [i]+strand[i+1]+strand[i+2])
    

    #Compare with dict and stop when a STOP codon appear
    trans_length = len(pro)
    for j in range(trans_length):
        if pro[j] in['UAA','UAG','UGA']:
            break
        trans.append(codon[pro[j]])
        
    return trans

