# file = open("my_file.txt")
# content = file.read()
# print(content)
# file.close()
# działa tak samo jak poniższy kod, ale z with nie trzeba zamykać
# with open("my_file.txt") as file:
#     content = file.read()
#     print(content)
# with open("my_file.txt", mode="w") as file: #nadpisuje zawartosć
#     file.write("New text.")
#
# with open("my_file.txt", mode="a") as file: #dodaje do zawartości
#     file.write("\nNew text.")
#
# with open ("new_file.txt", mode = "w") as file:
#     file.write("New text.")
with open("/Users/koleb/Desktop/chalange.txt")as file:
    content = file.read()
    print(content)