import lexer
import parser
import semantic

def test_lexer():
    data = '''
    int main () {
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
    # Adicionando algumas variáveis para teste
    semantic.adicionarVariavel("x", "int")
    semantic.adicionarVariavel("y", "float")

    # Exemplo de código com erros semânticos
    data = '''
    int main() {
        int x;
        float y;
        x = 10;
        y = 3.14;

        z = soma(x, y); // Erro: variável 'z' não declarada e tipos incompatíveis para a função 'soma'
        a = 5; // Erro: variável 'a' não declarada
        x = "texto"; // Erro: atribuição de tipo incompatível (string para int)
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
