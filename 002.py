"""
Questão 2 — Log de eventos do app Mumbuca
RESPOSTA: Rubro-Negra
Execute:  python questao2.py
"""
from arvores import relatorio, escala

CHAVES = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]


def main():
    relatorio("QUESTÃO 2 — Log de eventos (escrita dominante, chaves crescentes)",
              CHAVES, mostrar_log=True)
    escala("crescente")
    print("RESPOSTA: ( ) AVL    (X) Rubro-Negra")


if __name__ == "__main__":
    main()