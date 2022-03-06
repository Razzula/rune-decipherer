import time

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

f = open('words.txt', 'r')
valid = f.read().split('\n')
f.close()

words = ['ab', 'cb', 'deffg', 'e', 'chij', 'cb', 'dhb']
accepted = []

def bGoDeeper():
    #see if enough info for a word yet
    for word in words:
        flag = True
        temp = ''
        for char in word:
            if [char,None] in key:
                flag = False
                break
            #find replacement
            for n in range(len(key)):
                if key[n][0] == char:
                    temp += key[n][1]
                    break
        if flag: #if sufficeint data for a word
            #check if word is a valid word
            if temp not in valid:
                return False
    return True

def bWordsValid():
    final = ''
    for word in words:
        flag = True
        temp = ''
        #find replacement
        for char in word:
            for n in range(len(key)):
                if key[n][0] == char:
                    temp += key[n][1]
                    break
        #check if word is a valid word
        if temp not in valid:
            return
        final += temp + ' '
    print(key)
    f.write(final + '\n')

def recurse():
    priors = ''
    n = -1
    for i in range(len(key)):
        if key[i][1] == None:
            n = i
            break
        priors += key[i][1] + ' '
    # if all runes are assigned, don't go deeper
    if n == -1:
        bWordsValid()
        return

    # cycle all values of rune
    for i in range(23):
        rune = alphabet[i]
        if rune + ' ' in priors: #ensure rune is not duplicate
            continue
        key[n][1] = rune

        if bGoDeeper():
            recurse()
        key[n][1] = None

key = []
for word in words:
    for char in word:
        if [char, None] not in key:
            key.append([char, None])

epoch = time.time()

f = open('out.txt', 'w')
recurse()
f.close()

epoch = time.time() - epoch
print('Done :D')
print('in ' + str(epoch) + 's')