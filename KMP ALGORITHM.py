
#PROGRAM FOR FINDING INDEX OF PATTERN MATCH USING KMP ALGORITHM 

def KMPAlgo(P,S):
    M = len(P)
    N = len(S)
    lps=[]
    LPS(P,M,lps)
    print(lps)
    i=0
    j=0
    while (N-i)>=(M-j):
        if P[j]==S[i]:
            i+=1
            j+=1
            
        if j == M:
            print("Pattern Found",i-j)
            j=lps[j-1]
        elif i<N and P[j]!=S[i]:
            if j!=0:
                j=lps[j-1]
            else:
                i+=1
            
def LPS(P,M,lps):
    lps.append(0)
    j=0
    for i in range(1,M):
        if P[i]==P[j]:
            lps.append(j+1)
            j=j+1
        else:
            j=0
            lps.append(j)
    
if __name__=="__main__":
    S = "ABABACDEABABABCABCABCABDAA"
    P = "ABCAB"
    KMPAlgo(P,S)

OUTPUT:
[0, 0, 0, 1, 2]
Pattern Found 12
Pattern Found 15
Pattern Found 18
