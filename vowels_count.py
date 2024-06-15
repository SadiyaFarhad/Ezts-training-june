
#Program for accurately  counting vowel 
#Identifies the vowel(s) with the highest frequency in the given strings for each name.
#If their is tie then also print it. in output


def count_vowel(s):
    dic={'A':0,'E':0,'I':0,'O':0,'U':0}
    for i in s:
        if i=='a' or i=='A':
            dic['A'] += 1
        elif i=='e' or i=='E':
            dic['E'] += 1
        elif i=='i' or i=='I':
            dic['I']+=1
        elif  i=='o' or i=='O':
            dic['O']+=1
        elif  i=='u' or i=='U':
            dic['U']+=1
    x=max(dic.values())
    
    result=[]
    for i,j in dic.items():
       if j==x:
           result.append(i)
    
    return result
i_p=[
     ["alex","How are you sandy"],
     ["sam","I like cooking"]
     ]
o_p={}
for i in i_p:
    
    o_p[i[0]]=count_vowel(i[1])
print(o_p)

#OUTPUT: {'alex': ['A', 'O'], 'sam': ['I']}
