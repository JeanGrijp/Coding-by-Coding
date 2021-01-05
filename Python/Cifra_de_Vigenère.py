def take_spaces_with_char(text):
    text = str(text)
    final_text = ""
    aux = ""
    for i in text:
        if ((ord(i) >= 65) and (ord(i) <= 90)) or ((ord(i) >= 97) and (ord(i) <= 122)):
            aux += i
        elif i != " ":
            aux += i
        elif i == " ":
            final_text += aux
            aux = ""
    final_text += aux
    return final_text


def take_spaces(text):
    text = str(text)
    final_text = ""
    aux = ""
    for i in text:
        if ((ord(i) >= 65) and (ord(i) <= 90)) or ((ord(i) >= 97) and (ord(i) <= 122)):
            aux += i
        else:
            final_text += aux
            aux = ""
    final_text += aux
    return final_text


def order(key, size):
    key = take_spaces(key)
    final_text = ""
    for i in range(size):
        for j in range(len(key)):
            if len(final_text) >= size:
                return final_text
            else:
                final_text += key[j]

def get_index_lower(letter1, letter2):
    row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    column = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    main = row + column
    num = row.index(letter1.lower()) #4
    num2 = row.index(letter2) #2
    for i in range(len(column)):
        if i == num2:
            aux = i + num
            return main[aux]


def get_index_upper(letter1, letter2):
    row_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    column_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    main = row_upper + column_upper
    num = row_upper.index(letter1.upper()) #4
    num2 = row_upper.index(letter2) #2
    for i in range(len(column_upper)):
        if i == num2:
            aux = i + num
            return main[aux]


def vigenere(key, message):
    row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    column = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    row_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    column_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    key = order(take_spaces(key), len(message))
    size = len(message)
    aux = ""
    final_text = ""
    for i in range(size):
        if message[i] != " ":
            if (message[i] in row):
                letter = get_index_lower(key[i], message[i])
                aux += letter
            elif (message[i] in row_upper):
                letter = get_index_upper(key[i], message[i])
                aux += letter
            else:
                final_text += message[i]
        else:
            final_text += message[i]
    return final_text
                


a = "terabyte"
b = 'Para cifrar, é usada uma tabela de alfabetos que consiste no alfabeto escrito 26 vezes em diferentes linhas, cada um deslocado ciclicamente do anterior por uma posição. As 26 linhas correspondem às 26 possíveis cifras de César. Uma palavra é escolhida como "palavra-chave", e cada letra desta palavra vai indicar a linha a ser utilizada para cifrar ou decifrar uma letra da mensagem.'
print(vigenere(a, b))