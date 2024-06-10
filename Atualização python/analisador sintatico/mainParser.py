import ply.yacc as yacc
from lexer import lexer
import parser

parser = yacc.yacc(module=parser, write_tables=False)

data = '''
int main() {
    printf("Hello, world!");
    return 0;
}
'''

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)

result = parser.parse(data)
print(result)

parser.write_tables()
