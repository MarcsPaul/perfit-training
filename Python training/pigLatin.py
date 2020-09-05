def pyg(words):
    cnsnnt = ""
    for word in words:
        for i in range(0, len(word)):
            # a = word[i]
            if word[i] not in ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']:
                cnsnnt += (word[i])
            else:
                print(word[i:] + str(cnsnnt) + "ay", end=" ")
                cnsnnt = ""
                break



s = str(input("Enter a string"))
w = s.split()
# print(w)
pyg(w)


# trial sentence = "hello world full of witches and myths"
# desired output = "ellohay orldway ullfay ofay itchesway anday mythsay"
