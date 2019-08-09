def spliter(message):
    list1 = []
    for i in message:
        list1.append(i)
    return list1


def cesar(number, message):
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    string = ''
    list1 = spliter(message)
    if number > 0 and number < 27:
        for i in list1:
            string += letters[letters.index(letters[i]) + letters[number]]
    else:
        return None
    return string



num = 5
text = "família de endereços, uma tupla de quatro tuplas é usada, onde flowinfo e scopeid representam os membros e em C. Para métodos de módulo, flowinfo e scopeid podem ser omitidos apenas para compatibilidade com versões anteriores. Observe, no entanto, que a omissão do scopeid pode causar problemas na manipulação de endereços IPv6 com escopo definido"
print(cesar(num, text))
