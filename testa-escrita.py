arquivo_contatos = open('dados/contatos-escrita.csv', encoding='latin-1', mode='w+') #estamos indicando o modo de escrita
#(só que sem sobrescrever o arquivo). Por default, o python abre arquivos no modo leitura (r)

contatos = ['11,Carol,carol@carol.com.br\n',
            '12,Ana,ana@ana.com.br\n',
            '13,Tais,tais@tais.com.br\n',
            '14,Felipe,felipe@felipe.com.br\n']

for contato in contatos:
    arquivo_contatos.write(contato)

#arquivo_contatos.close() precisamos indicar que não estamos mais trabalhando com o arquivo para ele aí sim inserir o texto

arquivo_contatos.flush() #já aqui forçamos ele a inserir os elementos mesmo com o arquivo aberto

arquivo_contatos.seek(0) #estamos mandando o python inserir os conteúdo na 1°linha do arquivo
#esse comando se baseia no número de caracteres

arquivo_contatos.seek(28) #vai começar do contato da Ana
arquivo_contatos.write('12,Ana,ana@ana.com.br\n'.upper()) #upper para deixar as letras maiúsculas
arquivo_contatos.flush()
arquivo_contatos.seek(0) #para percorrer do começo da linha

#se tentarmos fazer isso no modo a+ de arquivo, não dará exatamente certo, visto que ele sempre posiciona o ponteiro no final
#logo, nossos seeks não servem pra nada

#input('Pressione <Enter> para encerrar o programa')

for linha in arquivo_contatos:
    print(linha) #estamos tentando percorrer o arquivo