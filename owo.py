import re

def aRL():
    huh = "w"
    wha = ""
    butt = input("qq: ")
    return re.sub("(?:r|l)", "w", butt,)
    #print(wha)
    #return wha
def aR(wha):
    vowel_loweruw = "w"
    vowel_lowerin = wha
    #vowel_lowerin = input("qq: ")
    return re.sub('n([aeiou])',"Ny",vowel_lowerin,1)
    #result = prog.match(vowel_lowerin)

        #wha = wha + x
    #print(wha)

print(aR(aRL()))
#aRL()
