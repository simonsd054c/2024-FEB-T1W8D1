readme_file = open("readme.txt", "r")

content = readme_file.read()

print(content + "add this string")

# readme_file.write("write this at the end of the file")

# print(readme_file.read())

readme_file.close()

# readme_file.write("hello again")