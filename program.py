try:
    x = int(input("Введите число:"))
    x+= 5
    print(x)
except ValueError:
    print("Введите лучше число")
else :
    print("Finally")




try:
    x = int(input("Введите число:"))
    a = [1,6, 8, 22, 0]

    print(a[x])
except IndexError:
    print("Введите другое число")
else :
    print("Finally")