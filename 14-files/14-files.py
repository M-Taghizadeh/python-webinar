### File Handling:    
    # "r" - Read - Default value. Opens a file for reading, error if the file does not exist
    # "a" - Append - Opens a file for appending, creates the file if it does not exist
    # "w" - Write  - Opens a file for writing, creates the file if it does not exist
    # "x" - Create - Creates the specified file, returns an error if the file exists
    # "b" - Binary - Binary mode (e.g. images)

# [READ]
f = open('content.txt', mode='r') 
# with open('content.txt', mode="r") as f:
#     print(f.read())


### read():
TEXT = f.read()
print(TEXT)

for text in TEXT:
    if(text == '\n'):
        print('endline')
    # print(text)


### readlines():
line_list = f.readlines()
print(line_list[2:10])
for line in f.readlines():
    print(line)


### readline():
print(f.readline())
print(f.readline())
print(f.readline())


# [WRITE] 
f = open("test.txt", mode="w")
text = 'python programming language'
f.write(text)
f.close()


# [APPEND]
f = open("test.txt", mode="a+")
text = ' python '
f.write(text)
f.close()


# [DELETE]
# delete file --> os.remove()
import os
if os.path.exists("test.txt"):
    print("file already exists")
    os.remove("test.txt")
    print("file deleted")
else:
    print("The file does not exist")


# delete folder --> os.rmdir()
# import os
# os.rmdir("test")