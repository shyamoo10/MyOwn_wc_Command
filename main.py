import sys

file= open("test.txt","rb")
content=  file.read()


if sys.argv[1]=="ccwc":
    if sys.argv[2]=="-c":
        print(len(content))
    else:
        print("syntax error,use correct flags")  
else:
    print("syntax error,use ccwc")          





