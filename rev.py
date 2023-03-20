
def spin_words(s):
    for i in s.split(" "):
        print(len(i))
        if len(i) >= 5:
            s = s.replace(i, i[::-1])
    return(s)


print(spin_words("Hey fellow warriors"))
