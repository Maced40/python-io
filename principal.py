import contatos_utils

try: 
    # contatos = contatos_utils.csv_para_contatos('dados/contatos.csv')
    # contatos_utils.contatos_para_pickle(contatos, 'dados/contatos.pickle') #p ou pickle para indicar que eh um arquivo binario de disco

    # contatos = contatos_utils.pickle_para_contatos('dados/contatos.pickle')
    # contatos_utils.contatos_para_json(contatos, 'dados/contatos.json')

    contatos = contatos_utils.json_para_contatos('dados/contatos.json')

    for contato in contatos:
        print(f'{contato.id} - {contato.nome} - {contato.email}')

except FileNotFoundError:
    print('Arquivo nao encontrado.')

except PermissionError:
    print('Sem permissao de escrita.')