from lexer import lexer

# Código de teste
data = '''
int main() {
    printf("Hello, world!");
    return 0;
}
'''

# Alimente o lexer com o código de teste
lexer.input(data)

# Tokenize e imprima os tokens
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
