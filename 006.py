"""
Questão 6 — Fila de processos do escalonador
RESPOSTA: Rubro-Negra
Execute:  python questao6.py
"""
from arvores import relatorio, escala

CHAVES = [40, 20, 60, 10, 30, 50, 70, 5, 15, 25, 35, 45]


def main():
    relatorio("QUESTÃO 6 — Fila do escalonador (escrita extrema, caminho crítico)",
              CHAVES, mostrar_log=True)
    escala("aleatoria")
    print("RESPOSTA: ( ) AVL    (X) Rubro-Negra")


if __name__ == "__main__":
    main()