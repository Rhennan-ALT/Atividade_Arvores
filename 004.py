"""
Questão 4 — Índice de sessões ativas
RESPOSTA: Rubro-Negra
Execute:  python questao4.py
"""
from arvores import relatorio, escala

CHAVES = [42, 17, 63, 9, 28, 55, 74, 3, 21, 38, 50, 70]


def main():
    relatorio("QUESTÃO 4 — Índice de sessões ativas (escrita dominante, IDs aleatórios)",
              CHAVES, mostrar_log=True)
    escala("aleatoria")
    print("RESPOSTA: ( ) AVL    (X) Rubro-Negra")


if __name__ == "__main__":
    main()