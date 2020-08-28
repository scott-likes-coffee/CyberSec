#!/usr/bin/python3

###empty lists to be added to 
list0 = []
list1 = []
list2 = []
###one list to rule them all
table = [list0, list1, list2]
###count=0 as a starting off point for operation
count = 0
###for each item(in this case lists) in table: do this
for t in table:
###for each integer in this range (4), add a string to the list(count*4) add the next i in range (4) plus 1
    for i in range(4):
        t.append(str((count*4) + i + 1))
###join these operations together to be read left to right based on ""
    print("".join(t))
### add 1 to count and restart
    count += 1


