'Ferramentas para lidar com a entrada de dados pelo usuário.'


def validar_num_anais(numero: str) -> bool:
    ''' 
    Valida número dos anais fornecido pelo usuário.\n
    Se usuário não fornecer número inteiro, levanta ValueError.
    Se fornecer número fora do intervalo 1-6 (anais disponíveis), levanta AssertionError.\n  
    Retorna True ou False.
    '''
    try:
        numero = int(numero)
        assert 0 < numero < 7
        print('Número válido.')
        return True
    except(ValueError, AssertionError):
        print('Insira um número referente a anais disponíveis (de 1 a 6).')
        return False


def processar_nums_pag(entrada_nums: str) -> list:
    '''
    Processa os dados inseridos em resposta à solicitação de pegar_nums_pag().\n
    Separa string nas vírgulas, considerando cada valor da lista gerada uma página individual ou
    um intervalo (#-#).\n
    Páginas individuais são convertidas para int e adicionadas à lista final.
    Intervalos são separados no hífen, considerando o primeiro valor da lista gerada a página
    inicial do intervalo e o último, a página final. Tais valores são convertidos para int e
    usados para gerar uma lista de páginas no intervalo.\n
    Levanta exceção ValueError se qualquer tentativa de conversão para int falhar, informando
    ao usuário que os dados são inválidos e chamando pegar_nums_pag novamente.\n
    Retorna lista de números de páginas (int).
    '''

    lista_nums = []
    try:

        for item in entrada_nums.split(','):
            # Caso item seja intervalo (#-#), adiciona as págs. nele à lista
            if '-' in item:
                paginas = (int(pag) for pag in item.split('-'))
                intervalo = range(paginas[0] - 1, paginas[-1])
                lista_nums += [num for num in intervalo]
                continue
            lista_nums += [int(item) - 1]

        return lista_nums

    except:
        print('Entrada de dados inválida.\n')
        return pegar_nums_pag()


def pegar_nums_pag() -> list | None:
    '''
    Solicita que o usuário defina números das páginas com as quais trabalhar.\n
    Retorna None caso usuário não defina números das páginas, o que levará à extração de
    todas as páginas do arquivo; caso contrário, passa a entrada de dados como argumento
    à função processar_nums_pag e retorna a lista de números de páginas (int) resultante.
    '''

    # region
    entrada_nums = input('''Digite as páginas a extrair, separadas por VÍRGULAS.
Use HÍFENS para definir INTERVALOS. Ex.: 1,3,5-9
Observe a paginação DO ARQUIVO, não do sumário.
Aperte ENTER sem digitar nada para extrair todas as páginas.\n''')
    # endregion

    return processar_nums_pag(entrada_nums) if entrada_nums else None