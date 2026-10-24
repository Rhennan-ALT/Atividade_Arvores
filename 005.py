"""
Questão 5 — Importação de cadastro (IPTU) já ordenado
RESPOSTA: AVL
Execute:  python questao5.py
"""
from arvores import relatorio, escala

CHAVES = [1, 2, 3, 4, 5, 6, 7]


def main():
    relatorio("QUESTÃO 5 — Cadastro ordenado (carga única, busca permanente)",
              CHAVES, mostrar_log=True)
    escala("crescente")
    print("RESPOSTA: (X) AVL    ( ) Rubro-Negra")


if __name__ == "__main__":
    main()