import math

# AVL

class NoAVL:
    def __init__(self, chave):
        self.chave = chave
        self.esq = None
        self.dir = None
        self.h = 1


class AVL:
    nome = "AVL"

    def __init__(self):
        self.raiz = None
        self.rotacoes = 0
        self.ajustes = 0
        self.log = []

    @staticmethod
    def _h(no):
        return no.h if no else 0

    def _atualiza(self, no):
        no.h = 1 + max(self._h(no.esq), self._h(no.dir))
        self.ajustes += 1

    def _fb(self, no):
        return self._h(no.esq) - self._h(no.dir)

    def _rot_dir(self, y):
        x = y.esq
        y.esq = x.dir
        x.dir = y
        y.h = 1 + max(self._h(y.esq), self._h(y.dir))
        x.h = 1 + max(self._h(x.esq), self._h(x.dir))
        self.rotacoes += 1
        return x

    def _rot_esq(self, x):
        y = x.dir
        x.dir = y.esq
        y.esq = x
        x.h = 1 + max(self._h(x.esq), self._h(x.dir))
        y.h = 1 + max(self._h(y.esq), self._h(y.dir))
        self.rotacoes += 1
        return y

    def inserir(self, chave):
        self.raiz = self._ins(self.raiz, chave)

    def _ins(self, no, chave):
        if no is None:
            return NoAVL(chave)
        if chave < no.chave:
            no.esq = self._ins(no.esq, chave)
        elif chave > no.chave:
            no.dir = self._ins(no.dir, chave)
        else:
            return no
        self._atualiza(no)
        fb = self._fb(no)
        if fb > 1:                                   
            if self._fb(no.esq) < 0:                 
                self.log.append(f"rotação dupla ESQ-DIR no nó {no.chave} (inserindo {chave})")
                no.esq = self._rot_esq(no.esq)
            else:
                self.log.append(f"rotação simples à DIREITA no nó {no.chave} (inserindo {chave})")
            return self._rot_dir(no)
        if fb < -1:                                  
            if self._fb(no.dir) > 0:                 
                self.log.append(f"rotação dupla DIR-ESQ no nó {no.chave} (inserindo {chave})")
                no.dir = self._rot_dir(no.dir)
            else:
                self.log.append(f"rotação simples à ESQUERDA no nó {no.chave} (inserindo {chave})")
            return self._rot_esq(no)
        return no

    def altura(self):
        return self._h(self.raiz)

    def buscar(self, chave):
        """Retorna nº de comparações para achar a chave."""
        no, c = self.raiz, 0
        while no:
            c += 1
            if chave == no.chave:
                return c
            no = no.esq if chave < no.chave else no.dir
        return c

    def desenhar(self):
        return _desenhar(self.raiz, lambda n: (n.esq, n.dir), lambda n: str(n.chave))



# Rubro-Negra (CLRS)

VERMELHO, PRETO = "V", "P"


class NoRB:
    def __init__(self, chave, cor, nil=None):
        self.chave = chave
        self.cor = cor
        self.esq = nil
        self.dir = nil
        self.pai = nil


class RubroNegra:
    nome = "Rubro-Negra"

    def __init__(self):
        self.nil = NoRB(None, PRETO)
        self.nil.esq = self.nil.dir = self.nil.pai = self.nil
        self.raiz = self.nil
        self.rotacoes = 0
        self.ajustes = 0       
        self.log = []

    def _rot_esq(self, x):
        y = x.dir
        x.dir = y.esq
        if y.esq is not self.nil:
            y.esq.pai = x
        y.pai = x.pai
        if x.pai is self.nil:
            self.raiz = y
        elif x is x.pai.esq:
            x.pai.esq = y
        else:
            x.pai.dir = y
        y.esq = x
        x.pai = y
        self.rotacoes += 1

    def _rot_dir(self, y):
        x = y.esq
        y.esq = x.dir
        if x.dir is not self.nil:
            x.dir.pai = y
        x.pai = y.pai
        if y.pai is self.nil:
            self.raiz = x
        elif y is y.pai.dir:
            y.pai.dir = x
        else:
            y.pai.esq = x
        x.dir = y
        y.pai = x
        self.rotacoes += 1

    def _cor(self, no, cor):
        if no.cor != cor:
            no.cor = cor
            self.ajustes += 1

    def inserir(self, chave):
        z = NoRB(chave, VERMELHO, self.nil)
        y, x = self.nil, self.raiz
        while x is not self.nil:
            y = x
            if chave == x.chave:
                return
            x = x.esq if chave < x.chave else x.dir
        z.pai = y
        if y is self.nil:
            self.raiz = z
        elif chave < y.chave:
            y.esq = z
        else:
            y.dir = z
        self._conserta(z)

    def _conserta(self, z):
        while z.pai.cor == VERMELHO:
            avo = z.pai.pai
            if z.pai is avo.esq:
                tio = avo.dir
                if tio.cor == VERMELHO:                       
                    self.log.append(f"recolore pai/tio de {z.chave} (caso 1)")
                    self._cor(z.pai, PRETO)
                    self._cor(tio, PRETO)
                    self._cor(avo, VERMELHO)
                    z = avo
                else:
                    if z is z.pai.dir:                        
                        z = z.pai
                        self.log.append(f"rotação ESQ no nó {z.chave} (caso 2)")
                        self._rot_esq(z)
                    self._cor(z.pai, PRETO)                   
                    self._cor(z.pai.pai, VERMELHO)
                    self.log.append(f"rotação DIR no nó {z.pai.pai.chave} (caso 3)")
                    self._rot_dir(z.pai.pai)
            else:
                tio = avo.esq
                if tio.cor == VERMELHO:
                    self.log.append(f"recolore pai/tio de {z.chave} (caso 1)")
                    self._cor(z.pai, PRETO)
                    self._cor(tio, PRETO)
                    self._cor(avo, VERMELHO)
                    z = avo
                else:
                    if z is z.pai.esq:
                        z = z.pai
                        self.log.append(f"rotação DIR no nó {z.chave} (caso 2)")
                        self._rot_dir(z)
                    self._cor(z.pai, PRETO)
                    self._cor(z.pai.pai, VERMELHO)
                    self.log.append(f"rotação ESQ no nó {z.pai.pai.chave} (caso 3)")
                    self._rot_esq(z.pai.pai)
        self.raiz.cor = PRETO

    def _alt(self, no):
        return 0 if no is self.nil else 1 + max(self._alt(no.esq), self._alt(no.dir))

    def altura(self):
        return self._alt(self.raiz)

    def buscar(self, chave):
        no, c = self.raiz, 0
        while no is not self.nil:
            c += 1
            if chave == no.chave:
                return c
            no = no.esq if chave < no.chave else no.dir
        return c

    def desenhar(self):
        nil = self.nil
        return _desenhar(
            self.raiz if self.raiz is not nil else None,
            lambda n: (n.esq if n.esq is not nil else None, n.dir if n.dir is not nil else None),
            lambda n: f"{n.chave}({n.cor})",
        )


# Utilitários

def construir(classe, chaves):
    arv = classe()
    for k in chaves:
        arv.inserir(k)
    return arv


def prof_media(arv, chaves):
    return sum(arv.buscar(k) for k in chaves) / len(chaves)


def limites(n):
    """Limites teóricos de altura (em níveis) para n nós."""
    avl = 1.44 * math.log2(n + 2) - 0.328   
    rb = 2 * math.log2(n + 1)               
    minimo = math.ceil(math.log2(n + 1))    
    return minimo, avl, rb


def relatorio(titulo, chaves, mostrar_arvores=True, mostrar_log=False):
    """Insere as chaves nas duas árvores e imprime a comparação."""
    n = len(chaves)
    avl = construir(AVL, chaves)
    rb = construir(RubroNegra, chaves)
    minimo, lim_avl, lim_rb = limites(n)

    print("=" * 72)
    print(titulo)
    print("=" * 72)
    print(f"Ordem de inserção ({n} chaves): {chaves}\n")

    print(f"{'Métrica':<34}{'AVL':>14}{'Rubro-Negra':>16}")
    print("-" * 64)
    print(f"{'Altura final (níveis)':<34}{avl.altura():>14}{rb.altura():>16}")
    print(f"{'Rotações totais':<34}{avl.rotacoes:>14}{rb.rotacoes:>16}")
    print(f"{'Rotações por inserção':<34}{avl.rotacoes / n:>14.2f}{rb.rotacoes / n:>16.2f}")
    print(f"{'Ajustes (AVL: nós revisitados /':<34}{'':>14}{'':>16}")
    print(f"{'          RB: recolorações)':<34}{avl.ajustes:>14}{rb.ajustes:>16}")
    print(f"{'Comparações médias por busca':<34}{prof_media(avl, chaves):>14.2f}{prof_media(rb, chaves):>16.2f}")
    print()
    print(f"Altura mínima possível p/ n={n}: {minimo} | "
          f"limite teórico AVL ≈ {lim_avl:.1f} | limite teórico RB ≈ {lim_rb:.1f}")

    if mostrar_log:
        print("\nPassos de reequilíbrio da AVL:")
        for linha in avl.log:
            print("  -", linha)
        print("\nPassos de reequilíbrio da Rubro-Negra:")
        for linha in rb.log:
            print("  -", linha)



def escala(ordem, n=20000, semente=7):

    import random
    import time

    chaves = list(range(1, n + 1))
    if ordem == "aleatoria":
        chaves = random.Random(semente).sample(range(10 * n), n)
    print("======================================================================== \n")
    print(f"--- Teste em escala: {n} chaves em ordem {ordem} ---")
    print(f"{'':<14}{'altura':>8}{'rot/ins':>10}{'ajustes/ins':>13}{'busca média':>13}{'tempo (s)':>11}")

    for classe in (AVL, RubroNegra):
        t0 = time.perf_counter()
        arv = construir(classe, chaves)
        dt = time.perf_counter() - t0
        print(f"{classe.nome:<14}{arv.altura():>8}{arv.rotacoes / n:>10.2f}"
              f"{arv.ajustes / n:>13.2f}{prof_media(arv, chaves):>13.2f}{dt:>11.2f}")
    print("(ajustes: AVL = nós revisitados p/ recalcular altura; RB = recolorações)\n")
    print("========================================================================")

