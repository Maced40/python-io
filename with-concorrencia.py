contato_carol = '11,Carol,carol@carol.com.br\n'
contato_andreza = '12,Andreza,andreza@andreza.com.br\n'

with open('dados/contatos-escrita.csv', encoding='latin_1', mode='a') as arquivo1: #o arquivo abre e fecha dentro dessa
    #operação/escopo, logo, não poderá ser manipulado fora dela
    arquivo1.write(contato_carol)
    
with open('dados/contatos-escrita.csv', encoding='latin_1', mode='a') as arquivo2:
    arquivo2.write(contato_andreza)

