from winsound import Beep
from time import sleep
print('Escolha a velocidade de tradução:\n1 - rápido\n2 - lento')

if int(input('Velocidade: ')) == 1:
    vel = 2
else:
    vel = 1

texto = str(input('Texto para ser traduzido [sem acentos]')).strip().lower()
morse = {'m': '--', ',': '--..--', '.': '.-.-.-', '1': '.----', '0': '-----',
         '3': '...--', '2': '..---', '5': '.....', '4': '....-', '7': '--...',
         '6': '-....', '9': '---.', '8': '---..', '?': '..--..', 'a': '.-',
         'c': '-.-.', 'b': '-...', 'e': '.', 'd': '-..', 'g': '--.',
         'f': '..-.', 'i': '..', 'h': '....', 'k': '-.-', 'j': '.---',
         'l': '.-..', 'o': '---', 'n': '-.', 'q': '--.-', 'p': '.--.',
         's': '...', 'r': '.-.', 'u': '..-', 't': '-', 'w': '.--', 'v': '...-',
         'y': '-.--', 'x': '-..-', 'z': '--..', '': '\n'}

for i in texto:
    print(i, morse[i])
    for j in range(len(morse[i])):
        if morse[i][j] == '.':
            Beep(500, 50 * vel)
            sleep(0.1*vel)
        elif morse[i][j] == '-':
            Beep(500, 150 * vel)
            sleep(0.1 * vel)
        else:
            sleep(0.3 * vel)
    sleep(0.3 * vel)
