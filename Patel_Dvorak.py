# Milan Patel
# Dvorak.py


qwerty = [' ', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', 'z',
          'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/']
dvorak = [' ', "'", ',', '.', 'p', 'y', 'f', 'g', 'c', 'r', 'l', 'a', 'o', 'e', 'u', 'i', 'd', 't', 'n', 's', '-', ';',
          'q', 'j', 'k', 'x', 'b', 'm', 'w', 'v', 'z']

dvorakText = ",. jab dak. a ,rbe.pugs ycm. cb jrmlgy.p ojc.bj.v"

sentence = ""
spot = 0
while spot < len(dvorakText):
    in_spot = 0
    while in_spot < len(dvorak):
        if dvorakText[spot] == dvorak[in_spot]:
            term = in_spot
            sentence += qwerty[term]
        in_spot += 1
    spot += 1
print(sentence)
