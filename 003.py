"""
Questão 3 — Tabela de símbolos de um compilador
RESPOSTA: AVL
Execute:  python questao3.py
"""
from arvores import relatorio, escala

CHAVES = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 55, 65]


def main():
    relatorio("QUESTÃO 3 — Tabela de símbolos (busca dominante, chaves aleatórias)",
              CHAVES, mostrar_log=True)
    escala("aleatoria")
    print("RESPOSTA: (X) AVL    ( ) Rubro-Negra")


if __name__ == "__main__":
    main()