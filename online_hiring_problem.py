import random #importing random library 
n = int(input("enter number of employees : ")) 
#creating a list of n elements from 1 to n and shuffling it randomly

l = [i for i in range(1,n+1)]
random.shuffle(l)
best = l[0] #considering a base best from the random list

#using the method that if something is better than the base best make it best and continue this until all elements are exhausted
for i in range(1,int(n/2.71)+1):
    if l[i] > best:
        best = l[i]
 
#another condition that if best s greater than the number that follows just after it, then we hire the best       
if best > l[(int(n/2.71)+1)] :
    print(f"hire {best}")
    
#if its not the case, then we hire the last person in the list    
else :
    print(f"hire {l[-1]}")    

print(l) #printing the list of total people for reference
