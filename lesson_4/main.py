list1 = [-1, "hi", 2, {}, (1,2)]
list2 = [-10, "hi2", 20, {3,4}, (10,30)]
print(list1)
print(list2)
list1.append("new1")
list1.insert(0, "head1")
list2.append("new2")
list2.insert(0, "head2")
print(list1)
print(list2)
list1.extend(list2)
print(list1)
