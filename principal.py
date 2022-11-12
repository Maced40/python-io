try: #estamos indicando: tenta isso daqui python
    arquivo_contato = open('dados/contatos.csv', encoding='latin_1', mode='w+') #podemos definir o encoding adicionando oa parâmetro encoding=''
    #ao definirmos w+ ou a+, caso o arquivo não exista, ele criará um novo

    # readline() - melhor para a questão de memória
    #read lines()

    for linha in arquivo_contato:
        print(linha, end='') #tiramos a quebra de linha

except FileNotFoundError: #uma excessão, ou seja, caso o path não exista, exibir esta mensagem
    print('Arquivo não encontrado.')

except PermissionError:
    print('Sem permissão de escrita.')

finally: #estamos falando: independentemente do que você tentar, finaliza com isso
    arquivo_contato.close()