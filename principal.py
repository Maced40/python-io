arquivo_contato = open('dados/contatos.csv') #podemos definir o encoding adicionando oa parâmetro encoding=''

# readline() - melhor para a questão de memória
#read lines()

for linha in arquivo_contato:
    print(linha, end='') #tiramos a quebra de linha