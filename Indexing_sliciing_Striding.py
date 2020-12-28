digits=[0,1,2,3,4,5,6,7,8,9]
#negative indexing-->you can count back from the list!!! -1-->can access last element
#:-->range of elemnts
digits=[0,1,2,3,4,5,6,7,8,9]
name='poda patti'
print(digits[-1])
print(digits[-len(digits)])
print(digits[0:3])#slicing in python
#0-->inclusive
#3-->exclusive
print(name[:4])
#striding
#incorporates 2 semicolons
#can mention interval
print(digits[::-1])
#always look on striding direction
#- means slicing is going to left

for i in range(len(digits)):
  print(digits[:i])
window_size=3
for i in range(len(digits)-(window_size-1)):
  print(digits[i:i+window_size])
