import os.path as path
import ferramentas_pdf as fp
import ferramentas_anais as fa
import gerenciamento_entrada as ge


# Definindo caminho relativo p/ anais
caminho_modulo_atual = path.abspath(__file__)
caminho_diretorio_atual = path.dirname(caminho_modulo_atual)
caminho_diretorio_anais = path.join(caminho_diretorio_atual, 'anais')
entrada_numero_anais = ge.pegar_num_anais()
caminho_arquivo_anais = path.join(
    caminho_diretorio_anais, f'anais_{entrada_numero_anais}.pdf')

# Selecionando págs.
nums_pag = ge.pegar_nums_pag()
# Extraindo texto
texto_pags = fp.extrair(caminho_arquivo_anais, nums_pag)
# Limpando texto
# fa.limpar_texto(texto_pags)
# Contando palavras e organizando contagem
contagem_organizada = fa.contar(texto_pags)

# TESTE
fa.escrever_completo(texto_pags, entrada_numero_anais)
fa.escrever_contagem(contagem_organizada, entrada_numero_anais)
