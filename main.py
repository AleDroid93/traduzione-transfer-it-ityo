from nltk import data, parse
from CKYGrammar import CKYGrammar
from CKY import cky


def do_nltk_parsing(sentences):
    parser = parse.load_parser('venv/simple_grammar.fcfg', trace=2)
    for sentence in sentences:
        tokens = sentence.split()
        trees = parser.parse(tokens)
        for tree in trees:
            print(tree)


def main():
    grammar = data.load('venv/simple_grammar.fcfg')
    isCNF = grammar.is_chomsky_normal_form()
    sentences = ['Skywalker corre veloce', 'Il futuro di questo ragazzo è nebuloso',
                 'Tu hai molto da apprendere ancora']
    # do_nltk_parsing(sentences)
    if isCNF:
        for sentence in sentences:
            g = CKYGrammar(grammar)
            tokens = sentence.split()
            print("\n===== Parsing Italiano =====\n")
            parsing_table = cky(tokens, g)
            parsing_root = parsing_table.get(0, len(tokens)).nonTerminals[0]
            print(parsing_root.print_all())
            print("\n===== Parsing Italiano Yodish  =====\n")
            parsing_root.yodify()
            print(parsing_root.print_all())
            g.productions.clear()
    else:
        print("La grammatica in input non è in Forma Normale di Chomsky.")


if __name__ =="__main__":
    main()