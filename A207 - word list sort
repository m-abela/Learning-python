words = []
f = open("words.txt", 'r')
words = f.read().strip().split("\n")
words.sort()
f.close()
f = open("words.txt", "w")
for i in range(len(words)):
    f.writelines(words[i])
f.close()
