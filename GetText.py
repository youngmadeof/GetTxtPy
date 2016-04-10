file = open(r "insert\file\path\here","r")
content = file.read()
getLine = file.readlines()

def findTxt(x):
    if x in content:
        print("Yes")
    else:
        print("All clear here")

findTxt("enter arg")
