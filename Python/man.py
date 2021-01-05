def escreve_no_arquivo(dicionario):
    with open("elementos.txt", "a") as arquivo:
        for i, j in dicionario.items():
            for x in j:
                arquivo.write(x)
                arquivo.write("\n")