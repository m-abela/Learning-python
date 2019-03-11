sentence = input("input a text")
times = len(sentence)
list = []

for shift in range (26):

    for i in range(times):
        shifter = ord(sentence[i]) + shift
        if shifter > 90 and shifter < 97:
            shifter = shifter - 26
        if shifter > 122:
            shifter = shifter - 26
        if shifter == 32+shift:
            shifter = shifter - shift
        list.append(chr(shifter))
    print(list)
    del list[:]
print(list)
