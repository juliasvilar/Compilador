import ply.lex as lex
import ply.yacc as yacc
from lexer import tokens
from parser import parser
from semantic_analyzer import *

def test_analyzers(data):
    # Executar o analisador léxico
    lexer = lex.lex()
    lexer.input(data)
    print("Tokens:")
    for tok in lexer:
        print(tok)

    # Executar o analisador sintático
    print("\nAnálise Sintática:")
    result = parser.parse(data)
    print(result)

    # Executar o analisador semântico (se houver)
    print("\nAnálise Semântica:")
    # Insira aqui o código para executar a análise semântica

# Teste
data = '''
int main() {
    int a = 5;
    float b = 3.14;
    return 0;
}
'''

test_analyzers(data)
