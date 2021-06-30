print("-------倒三角-------------")
for i in range(5):
    for j in range(0,5-i):
        print("*",end=" ")
    print("")
print("--------正三角------------")
for i in range(5):
    for j in range(0,i):
        print("*",end=" ")
    print("")
print("---------等边三角-------------")
for i in range(5):
    for j in range(0,5-i):
        print(end=" ")
    for k in range(5-i,5):
        print("*",end=" ")
    print("")
print("----------右对齐倒三角----------")
for i in range(5):
    for j in range(0,i):
        print(" ",end=" ")
    for j in range(0,5-i):
        print("*", end=" ")
    print("")
print("----------右对齐正三角-------")
for i in range(5):
    for j in range(0,5-i):
        print(" ",end=" ")
    for j in range(0,i):
        print("*", end=" ")
    print("")
print("-------------菱形----------")
for i in range(5):
    for j in range(0,5-i):
        print(end=" ")
    for k in range(5-i,5):
        print("*",end=" ")
    print("")
for i in range(5):
    for j in range(0, i):
        print("", end=" ")
    for j in range(0, 5 - i):
        print("*", end=" ")
    print("")
print("-------------------------")