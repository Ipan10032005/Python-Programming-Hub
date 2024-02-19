tup1 = ('Andre', 'Nina');
tup2 = (1,2,3)

#Creating a new tuple from two tuples 
tup3 = tup1 + tup2
print ("tup3 :", tup3)

#Creating a new tuple by adding tuple values
tup4 = (1,2,3,) + ('a','b','c')
print("tup4 :", tup4)

#Print length of tup4
print("Length of tup4 :", len(tup4))

#Repeating a value in a tuple
tup5 = ('a')*8
print("tup5 : ", tup5)

#Check value in tuple
print ("Is '2' present in tup4 ? ", 2 in tup4)

#Looping a Tuple
for x in tup4: 
    print(x),