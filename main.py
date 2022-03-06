import time

epoch = time.time()

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

f = open('words.txt', 'r')
valid = f.read().split('\n')
f.close()

words = ['ab', 'cb', 'deffg', 'e', 'chij', 'cb', 'dhb']
accepted = []

key = []

count = 0
pct = 0

for word in words:
    for char in word:
        if [char, None] not in key:
            key.append([char, None])

for a in range(len(alphabet)):
    key[0][1] = alphabet[a]

    for b in range(len(alphabet)):     
        active = alphabet[a]

        key[1][1] = alphabet[b]
        if alphabet[b] in active:
            continue

        for c in range(len(alphabet)):     
            active = alphabet[a] + alphabet[b]

            key[2][1] = alphabet[c]
            if alphabet[c] in active:
                continue

            for d in range(len(alphabet)):     
                active = alphabet[a] + alphabet[b] + alphabet[c]

                key[3][1] = alphabet[d]
                if alphabet[d] in active:
                    continue

                for e in range(len(alphabet)):     
                    active = alphabet[a] + alphabet[b] + alphabet[c] + alphabet[d]

                    key[4][1] = alphabet[e]
                    if alphabet[e] in active:
                        continue

                    for f in range(len(alphabet)):     
                        active = alphabet[a] + alphabet[b] + alphabet[c] + alphabet[d] + alphabet[e]

                        key[5][1] = alphabet[f]
                        if alphabet[f] in active:
                            continue

                        for g in range(len(alphabet)):     
                            active = alphabet[a] + alphabet[b] + alphabet[c] + alphabet[d] + alphabet[e] + alphabet[f]

                            key[6][1] = alphabet[g]
                            if alphabet[g] in active:
                                continue

                            for h in range(len(alphabet)):     
                                active = alphabet[a] + alphabet[b] + alphabet[c] + alphabet[d] + alphabet[e] + alphabet[f] + alphabet[g]

                                key[7][1] = alphabet[h]
                                if alphabet[h] in active:
                                    continue

                                for i in range(len(alphabet)):     
                                    active = alphabet[a] + alphabet[b] + alphabet[c] + alphabet[d] + alphabet[e] + alphabet[f] + alphabet[g] + alphabet[h]

                                    key[8][1] = alphabet[i]
                                    if alphabet[i] in active:
                                        continue
                                    
                                    for j in range(len(alphabet)):
                                        active = alphabet[a] + alphabet[b] + alphabet[c] + alphabet[d] + alphabet[e] + alphabet[f] + alphabet[g] + alphabet[h] + alphabet[i]

                                        key[9][1] = alphabet[j]
                                        if alphabet[j] in active:
                                            continue

                                        count += 1
                                        pct += (1/5311735)*100
                                        print(pct)

                                        # check words
                                        flag = True
                                        for word in words:
                                            temp = ''
                                            for char in word:
                                                for i in range(len(key)):
                                                    if key[i][0] == char:
                                                        temp += key[i][1]
                                                        break

                                            if temp not in valid:
                                                flag = False
                                                break

                                        temp = ''
                                        for i in range(len(key)):
                                            temp += key[i][1]
                                        
                                        if flag:
                                            accepted.append(temp)
                                            #print('VALID WORD: ' + temp)

f = open('valid.txt', 'w')

for i in range(len(accepted)):
    temp = ''
    for word in words:
        for char in word:
            #find replacement
            for n in range(len(key)):
                if key[n][0] == char:
                    temp += accepted[i][n]
                    break
        temp += ' '
    f.write(temp + '\n')

f.close()

epoch = time.time() - epoch
print('Done :)')
print(epoch)