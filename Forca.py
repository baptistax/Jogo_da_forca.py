import random
print('####### JOGO DA VELHA ########')
palavras = ['amarelo', 'amiga', 'amor', 'branco', 'cama', 'caneca', 'celular', 'clube', 'copo', 'elefante', 'escola',
            'estojo', 'geleia', 'limonada', 'janela', 'girafa', 'noite', 'parque', 'passarinho', 'peixe', 'pijama',
            'umbigo', 'acender', 'afilhado', 'ardiloso', 'caminho', 'basquete', 'chiclete', 'chuveiro', 'coelho',
            'esquerdo', 'impacto', 'quarentena', 'reportagem', 'sino', 'amendoim', 'banheiro', 'catapora', 'moeda']
desenho = []
palavra_vis = []
palavra_ocu =[]
let_errada = []
erros = 0


def reinicia():
    global desenho
    global palavra_vis
    global palavra_ocu
    global let_errada
    global erros
    desenho = ['                +------------------------+',
               '                |                        |',
               '                |                        |',
               '                |                        |',
               '                |                        |',
               '                                         |',
               '                                         |',
               '                                         |',
               '                                         |',
               '                                         |',
               '                                         |',
               '                                         |',
               '                                         |',
               '                                         |',
               '                                         |',
               '                                         |',
               '                                         |',
               '                                         |',
               '                                         |',
               '                                         |',
               '                                         |',
               '                                         |',
               '                                         |',
               '                                         |',
               '    ####################################################']
    palavra_vis = []
    palavra_ocu = []
    let_errada = []
    erros = 0


def limpa():
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')


def printar():
    global desenho
    global palavra_vis
    global let_errada
    global palavra_ocu
    limpa()
    for item in desenho:
        print(item)
    print('\n')
    if palavra_vis == palavra_ocu:
        jogar = input('Parabens, você ganhou!\nDeseja jogar novamente?(s/n): \n')
        if jogar == 's':
            menu()
        elif jogar == 'n':
            print('Fechando..')
            exit()
        else:
            print('Opção invalida.. fechando..')
            exit()
    for caracter in palavra_vis:
        print(caracter, end='')
    print('\n')
    if let_errada:
        print('Letras erradas:  ', end='')
        for letra in let_errada:
            print(letra + ' ', end='')
    letra = input('\nDigite a letra: ').lower().strip()
    if len(letra) != 1:
        print('Erro, mais ou menos de um caracter digitado')
    else:
        compara(letra)


def jogo():
    global escolhida
    global palavra_vis
    global palavra_ocu
    escolhida = random.choice(palavras)
    for letra in escolhida:
        palavra_ocu.append(letra + ' ')
        palavra_vis.append('_ ')
    printar()


def menu():
    comecar = input('Começar? (s/n)').lower().strip()
    if comecar == 's':
        reinicia()
        jogo()
    elif comecar == 'n':
        exit()
    else:
        print('Opção invalida, fechando.')
        exit()


def compara(letra):
    global palavra_vis
    global palavra_ocu
    global let_errada
    i = -1
    for let in palavra_ocu:
        i += 1
        if let == letra + ' ':
            palavra_vis[i] = letra + ' '
    if letra + " " not in palavra_vis:
        perde_ponto()
        let_errada.append(letra + ' ')
    printar()


def perde_ponto():
    global erros
    global escolhida
    if erros == 0:
        desenho[5] = '               +---+                     |'
        desenho[6] = '               |@ @|                     |'
        desenho[7] = '               | - |                     |'
        desenho[8] = '               +---+                     |'
        desenho[9] = '                 |                       |'
    elif erros == 1:
        desenho[10] = '                 |                       |'
        desenho[11] = '                 |                       |'
        desenho[12] = '                 |                       |'
        desenho[13] = '                 |                       |'
        desenho[14] = '                 |                       |'
        desenho[15] = '                 |                       |'
        desenho[16] = '                 |                       |'
    elif erros == 2:
        desenho[11] = '                /|                       |'
        desenho[12] = '               / |                       |'
        desenho[13] = '              /  |                       |'
    elif erros == 3:
        desenho[11] = '                /|\                      |'
        desenho[12] = '               / | \                     |'
        desenho[13] = '              /  |  \                    |'
    elif erros == 4:
        desenho[17] = '                  \                      |'
        desenho[18] = '                   \                     |'
        desenho[19] = '                    \>                   |'
    elif erros == 5:
        desenho[17] = '                / \                      |'
        desenho[18] = '               /   \                     |'
        desenho[19] = '             </     \>                   |'
    elif erros == 6:
        desenho[6] = '               |X X|                     |'
        desenho[7] = '               | p |                     |'

    elif erros == 7:
        print('Você perdeu! :(\nA palavra era: {}'.format(escolhida))
        jogar = input('Deseja jogar de novo?(s/n)\n')
        if jogar == 's':
            menu()
        elif jogar == 'n':
            print('Saindo..')
            exit()
        else:
            print('Opção invalida. fechando..')
            exit()
    erros += 1


menu()
