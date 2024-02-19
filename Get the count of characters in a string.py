print("Please enter a sentence you like and I will give the sum of each characters in your sentence : ")
par=str(input())

#Initialising dictionary
chrCount={}

#getting each character from the variable par
for i in par:
 #strip fuction will remove the pre and post spaces from a string variable
 if i.strip() == "":
  continue
 # if key already exist in dictionary chrCount. add 1 to the value of the element
 if(i in chrCount):
  chrCount[i]=chrCount[i]+1
 # newly adding an key with value as 1 into the dictionary chrCount
 else:
  chrCount[i]=1

print(chrCount)