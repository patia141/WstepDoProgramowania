#rozw z zajęć
sample_dict = {
 "name": "Kelly",
 "surname": "Jones",
 "age": 25,
 "salary": 8000,
 "city": "New york"}

for k, v in sample_dict.items():
    print(f'{k:<8} = {v:>8}') # wyrównaj do lewej/ do prawej strony

list = ["name", "age"]
'''D = {}
for k in list:
    for k2 in sample_dict.keys():
        if k == k2:
            D[k] = sample_dict[k]
            break
print(D)'''
#------------------
'''D = {}
for k in list:
    if k in sample_dict.keys():
        D[k] = sample_dict[k]
        
print(D)'''
D = {k:sample_dict[k] for k in list if k in sample_dict.keys()}
print(D)

'''for k in list:
    if k in sample_dict.keys():
        sample_dict.pop(k)
print(sample_dict)'''

'''for k in list:
    sample_dict.pop(k,None)
print("sample: ", sample_dict)'''

for k in sample_dict.values():
    if k == "Jones":
        print("istnieje")
        break
else:
    print("nie istnieje")

#if "Jones" in sample_dict.values():