import wikipedia

a= wikipedia.search("HELLO")
print(a)
b = wikipedia.summary("HELLO" , sentences = 2)
print(b)