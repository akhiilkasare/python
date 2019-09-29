
def getdate():
    import datetime
    return datetime.datetime.now()


while True:
    x = int(input("Enter your choice 1.Rohan\n2.harry\n3.hammad"))

    if x == 1:
        a = int(input("1.food\n 2.retrive_data"))
        if a == 1:
            value = input("type here\n")
            f = open("/home/akhil/Desktop/rohan.txt", "a")
            f.write(value)

        elif a == 2:
            b = open("/home/akhil/Desktop/rohan.txt","r")
            j = b.read()
            print(j)
            pass

        else:
            print("sucessfully written")

    if x == 2:
        a = int(input("1.food\n 2.retrive_data"))
        if a == 1:
            value = input("type here\n")
            f = open("/home/akhil/Desktop/harry.txt", "a")
            f.write(value)
        elif a == 2:
            b = open("/home/akhil/Desktop/harry.txt","rt")
            y = b.read()
            print(y)
            pass
        else:
            print("sucessful")

    if x == 3:
        a = int(input("1.food\n 2.retrive_data"))
        if a == 1:
            value = input("type here\n")
            f = open("/home/akhil/Desktop/hammad.txt", "a")
            f.write(value)
        elif a == 2:
            b = open("/home/akhil/Desktop/hammad.txt","rt")
            k = b.read()
            print(k)
            pass
        else:
            print("sucessful")
    else:
        print("sucessful")
