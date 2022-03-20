# file = open("bear.txt")
# content = file.read()
# file.close()
# print (content[:89])

# with open("bear.txt") as file:
#     content = file.read()

# print (content[:89]) 

# def count_char(character, file_path):
#     with open(file_path) as file:
#         content = file.read()
#     return (content.count(character))

# print (count_char ('b',"bear.txt"))


with open("data.txt","a+") as file:
    file.seek(0)
    content = file.read()
    file.write(content)
    file.write(content)

