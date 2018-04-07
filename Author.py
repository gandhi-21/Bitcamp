import wikipedia

Author = input("Enter Author's Name")

pg = wikipedia.page(Author)

text_file1 = open("Content.txt","w")
text_file1.write(pg.content)
text_file1.close()

text_file = open("Output.txt", "w")
text_file.write(Author)
text_file.close()

text_file2 = open("Author History.txt","w")
text_file2.write(wikipedia.summary(Author))
text_file2.close

print(wikipedia.summary(Author))
