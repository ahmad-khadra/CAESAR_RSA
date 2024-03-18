

def decrypt(cipher, key):
    plain_list = []
    step1_list = []
    step2_list = []
    step3_list = []
    cipher = cipher.upper()
    for l in cipher:
        if ord(l) >= 65 and ord(l) <= 90:
            position = ord(l)  # ord("")
            step1_list.append(str(position))
            newl = position - key
            step2_list.append(str(newl))
            if newl < 65:
                newl = (newl + 26)
                char_newl = chr(newl)
                step3_list.append(str(newl))
            else:
                char_newl = chr(newl)
                step3_list.append(str(newl))
        else:
            newl = l
            char_newl = l
            step1_list.append(str(newl))
            step2_list.append(str(newl))

        plain_list.append(char_newl)
    t = ''.join(plain_list)
    step1_list = ' '.join(step1_list)
    step2_list = ' '.join(step2_list)
    step3_list = ' '.join(step3_list)

    return step1_list, step2_list, step3_list, t

#####################################################

def encrypt(txt, key):
    cipher_list = []
    step1_list = []
    step2_list = []
    step3_list = []
    txt = txt.upper()
    for l in txt:
        if ord(l) >= 65 and ord(l) <= 90:
            position = ord(l)  # ord("")
            step1_list.append(str(position))
            newl = position + key
            step2_list.append(str(newl))
            if newl > 90:
                newl = (newl % 91) + 65
                char_newl = chr(newl)
                step3_list.append(str(newl))

            else:
                char_newl = chr(newl)
                step3_list.append(str(newl))
        else:
            char_newl = l
            step1_list.append(str(char_newl))
            step2_list.append(str(char_newl))

        cipher_list.append(char_newl)
    t = ''.join(cipher_list)
    step1_list = ' '.join(step1_list)
    step2_list = ' '.join(step2_list)
    step3_list = ' '.join(step3_list)

    return step1_list, step2_list, step3_list, t

def attack(cipher):
    results = []
    for i in range(1,26):
        decrypt_steps = decrypt(cipher, i)
        plain = decrypt_steps[-1]
        results.append(plain)
    return results