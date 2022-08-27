 dict = {}
with open("ALice.txt", "r") as f:
        for line in f:
            for word in line.split(" "):
                if word != "":
                    if word in dict:
                        number = dict.get(word) + 1
                        dict.update({word: number})
                    else:
                        dict.update({word: 1})
    max = 1
    mostword = None
    for word in dict:
        if dict.get(word) > max:
            max = dict.get(word)
            mostword = word
    print(mostword, max)
