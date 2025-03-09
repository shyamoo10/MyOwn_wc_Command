import sys

file= open("test.txt","rb")
content=  file.read()
file_text=open("test.txt","r",encoding="utf-8")
content_txt=  file_text.read()




if sys.argv[1]=="ccwc":
    if sys.argv[2]=="-c":
        print(len(content))
    elif sys.argv[2]=="-l":
        line_count= content_txt.split("\n")
        print(len(line_count))    
    else:
        print("syntax error,use correct flags")  
else:
    print("syntax error,use ccwc")          





