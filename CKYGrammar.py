from nltk import featstruct
from FeaturedNonTerminal import FeaturedNonTerminal
import re


class CKYGrammar:
    productions = []

    def __init__(self, grammar):
        prods = grammar.productions()
        for p in prods:
            parts = str(p).split(" -> ")
            production = None
            production = CKYProduction(parts[0], parts[1])
            self.productions.append(production)

    def printGrammar(self):
        for p in self.productions:
            print(str(p)+"\n")


class CKYProduction:
    left_hand = None
    right_hand = None

    def __init__(self, left, right):
        self.left_hand = self.buildFeaturedNT(left)
        self.right_hand = []
        if "[" in str(right):
            pattern = re.compile("^\w*\[(.*)\]\s")
            match_right_symbols = pattern.match(right)
            first_right_symbol = match_right_symbols.group(0).replace(" ","")
            right_symbols = []
            patternR = re.compile("\w*\[.*\]\s")
            second_right_symbol = patternR.split(right)
            if len(second_right_symbol) == 2:
                second_right_symbol = second_right_symbol[1]
            right_symbols.append(first_right_symbol)
            right_symbols.append(second_right_symbol)
            for symbol in right_symbols:
                rhs = self.buildFeaturedNT(symbol)
                self.right_hand.append(rhs)
        else:
            right_parts = right.split(" | ")
            for i in range(len(right_parts)):
                right_symbol = right_parts[i]
                self.right_hand.append(right_symbol.replace("'", ""))

    def buildFeaturedNT(self, symbol):
        s = symbol.split("[")[0]
        left_feats = "[" + symbol.split("[")[1]
        reader = featstruct.FeatStructReader()
        features = reader.fromstring(left_feats, fstruct=None)
        featured_nt = FeaturedNonTerminal(s, features)
        return featured_nt

    def __str__(self):
        left = str(self.left_hand) + " -> "
        right = ""
        for r in self.right_hand:
            right += str(r) + " "
        return left + right
