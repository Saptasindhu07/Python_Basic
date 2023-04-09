def rank_indicator(input_list,c):
    l=sorted(input_list)
    count1=0
    greatest=l[0]
    for i in l:
        if i>greatest:            #ASCII Comparison
            greatest=i
            count1+=1
            if greatest==c:
                break
            else:
                pass
        else:
            pass
    print("The rank of the letter ",c," is ",count1)
import math
word=input("Enter word with spaces between each letter: ").split()
word1=word.copy()                
copy=word.copy()
copy.sort()
length=len(word)
z=True                            #Primary Counter
count2=0                          #Secondary Counter
count3=0                          #SUM COUNTER
h=[]
while z==True:
    for i in copy:
        if i==word[count2]:
            copy.remove(i)
            count2+=1
            break 
        else:
            count3+=math.factorial(len(copy)-1)
    if count2==len(word)-1:
        z=False
final_word=("".join(word))
print("The Rank of the word ",final_word," is ",count3+1)
    

    