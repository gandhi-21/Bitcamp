import wikipedia

Author = input("Enter Author's Name")

text_file = open("Output.txt", "w")
text_file.write(Author)
text_file.close()


print(wikipedia.summary(Author))
