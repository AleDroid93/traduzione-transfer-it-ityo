from CKYTable import CKYTable, CKYCell


def cky(words, grammar):
    table = CKYTable(words)
    j = 1
    while j <= len(words):
        heads = fetch_word_heads(words[j - 1], grammar.productions)
        for h in heads:
            h.setDepWord(words[j - 1])
        cell = CKYCell()
        cell.setNonTerminals(heads)
        table.put(j - 1, j, cell)
        i = j - 2
        while i >= 0:
            k = i + 1
            while k <= j - 1:
                cell_contentB = table.get(i, k)
                cell_contentC = table.get(k, j)
                heads = fetch_cell_heads(cell_contentB, cell_contentC, grammar.productions)
                new_cell = table.get(i, j)
                new_cell.setNonTerminals(heads)
                table.put(i, j, new_cell)
                k += 1
            i -= 1
        j += 1
    return table


def fetch_cell_heads(listB, listC, productions):
    heads = []
    for itemB in listB.nonTerminals:
        for itemC in listC.nonTerminals:
            h = fetch_nonterminals_head(itemB, itemC, productions)
            for sym in h:
                sym.setDepLeft(itemB)
                sym.setDepRight(itemC)
                heads.append(sym)
    return heads


def fetch_nonterminals_head(itemB, itemC, productions):
    heads = []
    for prod in productions:
        rh = prod.right_hand
        lh_fts = prod.left_hand.features
        if len(rh) == 2:
            fst = rh[0]
            snd = rh[1]
            cond1 = str(fst.symbol) == str(itemB.symbol)
            cond2 = str(snd.symbol) == str(itemC.symbol)
            if cond1 and cond2:
                left_set = set(prod.left_hand.features.keys())
                setB = set(itemB.features.keys())
                setC = set(itemC.features.keys())
                union = setB.union(setC)
                res = union.difference(left_set)
                if len(res) == 0:
                    unification = None
                    try:
                        unification = prod.left_hand.features.unify(itemB.features.unify(itemC.features))
                        lh_unified = prod.left_hand
                        lh_unified.setFeatures(unification)
                        # heads.append(prod.left_hand)
                        heads.append(lh_unified)
                    except ValueError:
                        print("Parsing inconsistente!")
                        exit(1)
    return heads


def fetch_word_heads(word, productions):
    heads = []
    for prod in productions:
        if len(prod.right_hand) == 1 and str(word) == prod.right_hand[0]:
            heads.append(prod.left_hand)
    return heads