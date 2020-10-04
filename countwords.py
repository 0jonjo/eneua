import string

texto = open('anais1.txt', encoding='utf-8').read().lower()
ignore = open('ignore.txt', encoding='utf-8').read().lower()
for c in string.punctuation:
    texto = texto.replace(c, ' ')

palavras = texto.split()

wc = {}
for p in palavras:
    if p in ignore:
        wc[p] = 0
    if p in wc:
        wc[p] += 1
    else:
        wc[p] = 1

##def contador(dupla):
##    return dupla[1]

duplas = sorted(wc.items(),
                key=lambda dupla:dupla[1],
                reverse=True)
for dupla in duplas[:20]:
    print (dupla[0], dupla[1])
