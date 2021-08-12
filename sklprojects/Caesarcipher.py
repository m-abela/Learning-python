sentence = input("input a text")
shift = int(input("how much you wann go bro"))
times = len(sentence)
list = []
for i in range(times):
    shifter = ord(sentence[i]) + shift
    print(shifter)
    if shifter > 90 and shifter < 97:
        shifter = shifter - 26
    if shifter > 122:
        shifter = shifter - 26
    if shifter == 32+shift:
        shifter = shifter - shift

    list.append(chr(shifter))

print(list)
