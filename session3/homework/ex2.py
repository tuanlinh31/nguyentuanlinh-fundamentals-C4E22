menu=["T-Shirt", "Sweater"]
while True:
    w=input(" what do you want (C, R, U, D)? ")
    if w == "R":
        print(*menu,sep=", ")
        break
    elif w =="C":
        menu.append("Jeans")
        print(*menu,sep=", ")
        break
    elif w =="U":
        menu.insert(1,"Skirt")
        print(*menu,sep=", ")
        break
    elif w =="D":
        menu.remove(2)
        print(*menu,sep=", ")
        break

        
        