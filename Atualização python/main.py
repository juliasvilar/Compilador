import lexer
import parser
import semantic

def test_lexer():
    data = '''
    int main() {
        printf("Hello, world!");
        return 0;
    }
    '''

    lexer.lexer.input(data)

    while True:
        tok = lexer.lexer.token()
        if tok is None:
            break
        print(tok)

def test_parser():
    data = '''
    int main() {
        printf("Hello, world!");
        return 0;
    }
    '''

    parser.parser.parse(data)

def test_semantic_analyzer():
    # Coloque seu código de teste para o analisador semântico aqui
    pass

if __name__ == "__main__":
    print("Testando o analisador léxico:")
    test_lexer()

    print("\nTestando o analisador sintático:")
    test_parser()

    print("\nTestando o analisador semântico:")
    test_semantic_analyzer()
