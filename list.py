#Technically a data structure, but think it as a data type
#not a primitve data type
#collection of things in order
l=[1,2,3]
print(l)
lis=[1,'string',1.4,[1,2,3]]
print(lis)
#indexing is applicable in string
print(lis[1])
#append-->adding to the end of the list
names=['jo','james','john']
names.append('gary')  #gary will be appended as the last name

names.insert(0,'poda')  #to insert wherever as we want
print(names)

names.remove('jo') #to remove an element from list
names.reverse() # to reverse a list

numbers=[6,4,2]
print(numbers)#prints normaly
numbers.sort() #sorts in ascending normally
for number in number: #i.e a list is iterable, we can iterate through each element and do what we need!
  print(number)
