import os

restaurante = ['Pizza', 'Sushi']

def exibir_nome_do_programa():
    print('sabor express')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    os.system('cls')
    # os.system('clear') 
    print('Finalizando o app')

def opcao_invalida():
    print('Opção invalidade\n')
    input('Digite qualquer tecla para voltar ao menu principal')
    main()

def cadastrar_novo_restaurante()
    os.system('cls')
    print('cadastro de novo restaurante\n')
    nome_do_restaurante = input('Digite o nome do restaurante: ')
    restaurante.append(nome_do_restaurante)
    print(f'o restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    input('\ndigite qualquer tecla para voltar ao menu principal')
    main()

def listar_restaurantes():
    os.system('cls')
    print('listando os restaurantes\n')
    
    for restaurante in restaurantes:
        print(f'.{restaurantes}')

    input('\ndigite qualquer tecla para voltar ao menu principal')
    main()


def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção:'))

        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()
        elif opcao_escolhida == 3: 
            print('Ativar restaurante')
        elif opcao_escolhida == 4: 
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if _name_ == '_main_':
    main()
