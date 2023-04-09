num=int(input("Enter a number: "))
reverse_numbers=[]
while num>0:
    reverse_numbers.append(num%10) #Storing values in reverse
    num=num//10
numbers=reverse_numbers[-1::-1] #Creating correct order
Output=[]
for i in range(len(numbers)-1):
    if numbers[i]-numbers[i+1]==1 or numbers[i]-numbers[i+1]==(-1):
        temp=[numbers[i],numbers[i+1]]
        Output.append(temp)
    else:
        pass
final_output=[]
for i in range(len(Output)):
    final_output.append(Output[i][0]*10+Output[i][1])
print("Consecutive numbers are: ")
print(final_output)
    

   