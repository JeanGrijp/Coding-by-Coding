def spliter(message):
    """
    Essa função recebe como parâmetro uma string, e retorna uma lista contendo cada letra do texto, como um elemento.
    """
    list1 = []
    for i in message:
        list1.append(i)
    return list1


def cesar(number, message):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    lettersUp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    nuns = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    
    if number > 26: # Verifica se o número da chave é maior que a quantidade de letras do alfabeto
        number = number%26 # o número passa a ser congruente ao número original em módulo 26
    string = ''
    list1 = spliter(message)
    dic = { # Apenas para não aparecer essas letras no texto, já que na tabela ASCII essas letras com acento são fora das outras letras
    "é":letters[letters.index("e") + number],
    "É":lettersUp[lettersUp.index("E") + number],
    "í":letters[letters.index("i") + number],
    "Í":lettersUp[lettersUp.index("I") + number],
    "á":letters[letters.index("a") + number],
    "à":letters[letters.index("a") + number],
    "ã":letters[letters.index("a") + number],
    "Á":lettersUp[lettersUp.index("A") + number],
    "À":lettersUp[lettersUp.index("A") + number],
    "Ã":lettersUp[lettersUp.index("A") + number]
    }
    if number > 0 and number < 27:
        for i in list1:
            if ord(i) >= 97 and ord(i) <= 122: # faz a verificação se a letra é minúscula
                string += letters[letters.index(i) + number]
            elif ord(i) >= 65 and ord(i) <= 90: # faz a verificação se a letra é maiúscula
                string += lettersUp[lettersUp.index(i) + number]
            elif ord(i) >= 48 and ord(i) <= 57:
                if number >= 0 and number <= 9:
                    string += nuns[nuns.index(i) + number]
                else:
                    aux = number%10
                    string += nuns[nuns.index(i) + aux]
            elif i in dic: # Verifica se i é um caractér especial. 
                string += dic[i]
            else:
                string += i
    else:
        return None
    return string


def descersar(number, message):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    lettersUp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    nuns = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    if number > 26: # Verifica se o número da chave é maior que a quantidade de letras do alfabeto
        number = number%26 # o número passa a ser congruente ao número original em módulo 26
    string = ''
    list1 = spliter(message)
    if number > 0 and number < 27:
        for i in list1:
            if ord(i) >= 97 and ord(i) <= 122: # faz a verificação se a letra é minúscula
                string += letters[letters.index(i) - number]
            elif ord(i) >= 65 and ord(i) <= 90: # faz a verificação se a letra é maiúscula
                string += lettersUp[lettersUp.index(i) - number]
            elif ord(i) >= 48 and ord(i) <= 57:
                if number >= 0 and number <= 9:
                    string += nuns[nuns.index(i) - number]
                else:
                    aux = number%10
                    string += nuns[nuns.index(i) - aux]
            else:
                string += i
    else:
        return None
    return string


num = 5
text = "ASCII — geralmente pronunciado — é um código binário que codifica um conjunto de 128 sinais: 95 sinais gráficos e 33 sinais de controle, utilizando portanto apenas 7 bits para representar todos os seus símbolos."
mais = cesar(num, text)
print(mais)
print(descersar(num, mais))
