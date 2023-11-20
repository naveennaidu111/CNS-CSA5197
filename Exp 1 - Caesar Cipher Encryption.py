P="hello everyone"
print("Plain Text:",P)
k_value=int(input("Enter the value of k:"))
lst1= []
plaintext= []
for i in range(97,123):
    lst1.append(chr(i))
k=[]
for j in lst1:
    k.append(lst1.index(j))
for i in P:
    if i in lst1:
        plaintext.append(lst1.index(i))
cipher=[x+k_value for x in plaintext]
print("Cipher Text:")
for m in cipher:
    if m in k:
        print(lst1[m],end="")
