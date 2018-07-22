from nltk import Nonterminal


class FeaturedNonTerminal:
    symbol = None
    features = None
    depLeft = None
    depRight = None
    depWord = None

    def __init__(self, sym, features):
        self.symbol = Nonterminal(sym)
        self.features = features
        self.depLeft = None
        self.depRight = None
        self.depWord = ""

    def __str__(self):
        return str(self.symbol) + " "
        # + str(self.features)

    def __eq__(self, other):
        vars = self.features.keys()
        for var in vars:
            if var not in other.features.keys():
                return False
        return self.symbol == other.symbol

    def setFeatures(self, new_features):
        self.features = new_features

    def setDepLeft(self, dep_left):
        self.depLeft = dep_left

    def setDepRight(self, dep_right):
        self.depRight = dep_right

    def setDepWord(self, dep_word):
        self.depWord = dep_word

    def print_all(self, level=0):
        ret = ""
        if self.depLeft is not None and self.depRight is not None:
            ret += "\t" * level + str(self) + "\n"
            ret += self.depLeft.print_all(level + 1)
            ret += self.depRight.print_all(level + 1)
        else:
            ret += "\t" * level + str(self) + " "
            ret += "-> " + self.depWord + "\n"
        return ret

    def yodify(self):
        aux = None
        if str(self.symbol) == "S":
            if self.depLeft is not None and self.depRight is not None:
                vp_subtree = self.depRight
                self.swap_vp_args(vp_subtree)
                self.swap_npsubtree_vpleft(self, vp_subtree)
                self.print_all()
        else:
            print("albero di parsing non valido!")


    def swap_vp_args(self, vp_subtree):
        if vp_subtree.depLeft is not None and vp_subtree.depRight is not None:
            aux_node = vp_subtree.depRight
            vp_subtree.depRight = vp_subtree.depLeft
            vp_subtree.depLeft = aux_node

    def swap_npsubtree_vpleft(self, root, vp_subtree):
        if vp_subtree.depLeft is not None and vp_subtree.depRight is not None:
            aux_node = vp_subtree.depLeft
            vp_subtree.depLeft = root.depLeft
            root.depLeft = aux_node