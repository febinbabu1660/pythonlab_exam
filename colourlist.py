c_list1 = ["blue","black", "white", "green"]
c_list2 = ["black", "white", "green"]
print(c_list1)
print(c_list2)
c_list3 = []
n = len(c_list1)
print(n)
m = len(c_list2)
print(m)
for i in c_list1:
    for j in c_list2:
        if (i == j):
            c_list3.append(i)
        else:
            pass
print(c_list3)
