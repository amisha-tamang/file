



a=open("people1-exercise.txt","r")
for i in a:
    if "delhi" in a:
        a=open("delhi.txt","a")
        a.write(i)
    elif "shimla" in a:
        a=open("shimla.txt","a")
        a.write(i)
    else:
        a=open("others.txt","a")
        a.write(i)
a.close()



# a=lambda a,b:a+b
# b=a(5,6)
# print(b)

# def sum(name,age):
#     print(name)
#     print(age)
# sum("amisah",17)

# from os import name


# def num(name,age):
#     print(name)
#     print(age)
# num(name="amisha")

# def num(name,age=19):
#     print(name)
#     print(age)
# num("amisha")