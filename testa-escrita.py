arquivo_contatos = open('dados/contatos-escrita.csv', encoding='latin-1', mode='a') #estamos indicando o modo de escrita
#(só que sem sobrescrever o arquivo). Por default, o python abre arquivos no modo leitura (r)

contato = '11,Carol,carol@carol.com.br\n'
arquivo_contatos.write(contato)
#nesse caso, se o arquivo não existir, o python cria um
