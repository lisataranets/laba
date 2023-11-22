text=str(input("Введите текст:"))
vse_slova=[]
one_slovo=""
for i in text:
    if i!=" " and i!="." and i!=",":
        one_slovo+=i
    else:
        if one_slovo!='':
            vse_slova.append(one_slovo)
            one_slovo=""
vse_slova.append(one_slovo)
len_max=vse_slova[0]
num=0
for n in range(len(vse_slova)):
    if len(vse_slova[n])>len(len_max):
        len_max=vse_slova[n]
        num=n
print("самое длинное слово:", vse_slova[num])
