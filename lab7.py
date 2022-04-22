# Apriori Algo

min_support = 50
min_confidence = 70

def popping(C):
    popitem = []
    for key, value in C.items():
        val = (value/length)*100
        if val < min_support:
            popitem.append(key)
        else:
            C[key] = val
    
    for i in popitem:
        C.pop(i)
    
    return C

def operation(c_prev, leng):
    C = {}
    itemset = []
    for i in c_prev.keys():
        for j in c_prev.keys():
            myset = frozenset([i, j]) if isinstance(i, int) else i.union(j)
            if len(myset) == leng and myset not in itemset:
                itemset.append(myset)
    
    for myset in itemset:
        if myset not in C.keys():
            C[myset] = 0
        
        for j in dataset.values():
            if myset.issubset(j):
                C[myset] += 1
    return C
        
def printing(dict):
    for key, value in dict.items():
        print(key,"->",value)

def frequents(C1,C2,C3): 
    mysets = []
    for i in C1.keys():
        j = frozenset([i])
        mysets.append(j)
    
    for i in C2.keys():
        mysets.append(i)
    
    for i in C3.keys():
        mysets.append(i)
    
    print("\nFrequent Itemsets are ====>\n" ,mysets)
    return mysets

dataset = {
    1 : {1,3,4},
    2 : {2,3,5},
    3 : {1,2,3,5},
    4 : {2,5}
}
length = len(dataset)

print("TID\t Items")
printing(dataset)

##################### C1
C1 = {}
itemset1 = []
for i in dataset.values():
    for item in i:
        if item not in C1.keys():
            C1[item] = 1
            itemset1.append(item)
        else:
            C1[item] += 1
            
items_length = len(C1)

print("\nCanditates 1:")
printing(C1)

L1 = popping(C1)
print("\nItemsets after Pruning 1:")
printing(L1)
    
################################ C2

C2 = operation(C1,2)
print("\nCanditates 2:")
printing(C2)
L2 = popping(C2)
print("\nItemsets after Pruning 2:")
printing(L2)

################## C3
C3 = operation(C2,3)
print("\nCanditates 3:")
printing(C3)
L3 = popping(C3)
print("\nItemsets after Pruning 3:")
printing(L3)

############### C4

itemset4 = []
for i in C3.keys():
    for j in itemset1:
        if isinstance(j, int):
            j = set([j])
        myset = i.union(j)
        if len(myset) == 4 and myset not in itemset4:
            itemset4.append(myset)

C4 = {}
for myset in itemset4:
    if myset not in C4.keys():
        C4[myset] = 0
    
    for j in dataset.values():
        if myset.issubset(j):
            C4[myset] += 1

print("\nCanditates 4:")
printing(C4)

pop4 = []
for key, value in C4.items():
    val = (value/length)*100
    if val == 0:
        pop4.append(key)
    else:
        C4[key] = val

for i in pop4:
    C4.pop(i)

print("\nItemsets after Pruning 4:")
printing(C4)

####################### CONFIDENCE
mysets = frequents(C1, C2, C3)
setlist = []
for i in mysets:
    for j in mysets:
        if i != j and len(i) == 1 and len(j) == 1:
            myset = i.union(j)
            num = 0
            den1 = 0
            den2 = 0
            for data in dataset.values():
                if myset.issubset(data):
                    num += 1
                if i.issubset(data):
                    den1 += 1
                if j.issubset(data):
                    den2 += 1
            val1 = (num/den1)*100
            val2 = (num/den2)*100
            if val1 >= min_confidence and [i, j, val1] not in setlist:
                setlist.append([i,j, val1])
            if val2 >= min_confidence and [j, i, val2] not in setlist:
                setlist.append([j,i, val2])
        elif i != j and len(i) <= 2 and len(j) <= 1 and i.isdisjoint(j):
            myset = i.union(j)
            num = den = 0
            for data in dataset.values():
                if myset.issubset(data):
                    num += 1
                if i.issubset(data):
                    den += 1
            val = (num/den)*100
            if val >= 70:
                setlist.append([i,j, val])

print("\nThe association rules are : \n", setlist)