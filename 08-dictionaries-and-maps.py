n=int(input())
phonebook = dict()

for ele in range(0,n):
    entry = str(input()).split(' ')
    name = entry[0]
    phone = entry[1]
    phonebook[name] = phone

for i in range(0,n):
    name=input()
    if name in phonebook:
        print("{}={}".format(name,phonebook[name]))
    else:
        print("Not found")
