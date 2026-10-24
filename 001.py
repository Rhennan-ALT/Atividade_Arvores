"""
Questão 1 — Catálogo de produtos da loja
RESPOSTA: AVL
Execute:  python questao1.py
"""
from arvores import relatorio, escala

CHAVES = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]


def main():
    relatorio("QUESTÃO 1 — Catálogo de produtos (busca dominante, carga crescente)",
              CHAVES, mostrar_log=True)
    escala("crescente")
    print("RESPOSTA: (X) AVL    ( ) Rubro-Negra")


if __name__ == "__main__":
    main()