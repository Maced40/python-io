arquivo_contatos = open('dados/contatos-escrita.csv', encoding='latin-1', mode='w') #estamos indicando o modo de escrita
#(só que sem sobrescrever o arquivo). Por default, o python abre arquivos no modo leitura (r)

contatos = ['11,Carol,carol@carol.com.br\n',
            '12,Ana,ana@ana.com.br\n',
            '13,Tais,tais@tais.com.br\n',
            '14,Felipe,felipe@felipe.com.br\n']

for contato in contatos:
    arquivo_contatos.write(contato)

#arquivo_contatos.close() precisamos indicar que não estamos mais trabalhando com o arquivo para ele aí sim inserir o texto

arquivo_contatos.flush() #já aqui forçamos ele a inserir os elementos mesmo com o arquivo aberto

input('Pressione <Enter> para encerrar o programa')