# initializing list
test_list = [1, 3, 5, 6, 3, 5, 6, 1]
print ("The original list is : " +  str(test_list))
res = []
for i in test_list:
    if i not in res:
        res.append(i)
  
# printing list after removal 
print ("The list after removing duplicates : " + str(res))
