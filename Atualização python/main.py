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
    try:
        parser.parser.parse(data)
        print("A análise sintática foi concluída sem erros.")
    except Exception as e:
        print("Erro sintático:", e)

def test_semantic_analyzer():
    semantic.adicionarVariavel("x", "int")
    semantic.adicionarVariavel("y", "float")

    data = '''
    int main() { 
        h = 10;
        int x;
        float y;
        x = 10;
        y = 3.14;

        z = soma(x, y);
        a = 5;
        x = "texto";
        printf("Hello, world!");
        return 0;
    }
    '''

    if semantic.analisarCodigo(data):
        print("O código é semanticamente correto.")
    else:
        print("Houve um erro na análise semântica.")

if __name__ == "__main__":
    print("Testando o analisador léxico:")
    test_lexer()

    print("\nTestando o analisador sintático:")
    test_parser()

    print("\nTestando o analisador semântico:")
    test_semantic_analyzer()
