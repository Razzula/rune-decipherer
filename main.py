import time

alphabet = ['a','b','c','ch','d','e','ei','f','g','h','i','ie','j','k','l','m','n','o','p','q','r','s','t','th','u','v','w','x','y','z','zh']

f = open('words.txt', 'r')
valid = f.read().lower().split('\n')
f.close()

sentence = input("> ")
exempt = [',', '.',' ']

words = []
temp = ''
for char in sentence:
    if char == ' ':
        if temp not in words:
            words.append(temp)
        temp = ''
    elif char in exempt:
        continue #trim punctuation
    else:
        temp += char
if temp not in words:
    words.append(temp)
words.sort(key=len)

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

    temp = ''
    for char in sentence:
        for n in range(len(key)):
            if key[n][0] == char:
                #temp += key[n][1]
                break
        if char in exempt:
            temp += char
        else:
            temp += key[n][1]

    f.write(temp + '\n')
    global count
    count += 1

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
    for i in range(len(alphabet)):
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

count = 0
epoch = time.time()

f = open('./out/' + sentence + '.txt', 'w')
recurse()
f.close()

epoch = time.time() - epoch
print('Done :D')
print(str(count) + ' matches')
print('in ' + str(epoch) + 's')