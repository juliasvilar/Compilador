import ply.yacc as yacc
from lexer import tokens

def p_programa(p):
    'programa : declaracoes'
    p[0] = p[1]

def p_declaracoes(p):
    '''declaracoes : declaracao
                   | declaracoes declaracao'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[2])
        p[0] = p[1]

def p_declaracao(p):
    '''declaracao : declaracao_variavel
                  | declaracao_funcao
                  | comentario'''
    p[0] = p[1]

def p_declaracao_variavel(p):
    '''declaracao_variavel : tipo ID ';' 
                           | tipo ID '=' expressao ';' '''
    if len(p) == 4:
        p[0] = ('declaracao_variavel', p[1], p[2])
    else:
        p[0] = ('declaracao_variavel', p[1], p[2], p[4])

def p_tipo(p):
    '''tipo : INT
            | FLOAT
            | DOUBLE
            | CHAR
            | BOOLEAN'''
    p[0] = p[1]

def p_declaracao_funcao(p):
    '''declaracao_funcao : tipo ID '(' parametros ')' bloco'''
    p[0] = ('declaracao_funcao', p[1], p[2], p[4], p[6])

def p_parametros(p):
    '''parametros : parametro
                  | parametros ',' parametro'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[3])
        p[0] = p[1]

def p_parametro(p):
    '''parametro : tipo ID'''
    p[0] = ('parametro', p[1], p[2])

def p_bloco(p):
    'bloco : "{" declaracoes "}"'
    p[0] = p[2]

def p_comentario(p):
    'comentario : COMENTARIO'
    pass

def p_expressao(p):
    '''expressao : atribuicao
                 | expressao_logica
                 | expressao_relacional
                 | expressao_aritmetica'''
    p[0] = p[1]

def p_atribuicao(p):
    '''atribuicao : ID '=' expressao
                  | ID ADD_ASSIGN expressao
                  | ID SUB_ASSIGN expressao
                  | ID MUL_ASSIGN expressao
                  | ID DIV_ASSIGN expressao
                  | ID MOD_ASSIGN expressao
                  | ID LAND_ASSIGN expressao
                  | ID LOR_ASSIGN expressao'''
    p[0] = ('atribuicao', p[2], p[1], p[3])

def p_expressao_logica(p):
    '''expressao_logica : expressao_relacional
                        | expressao_logica LAND expressao_relacional
                        | expressao_logica LOR expressao_relacional
                        | LNOT expressao_relacional'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[2], p[1], p[3])

def p_expressao_relacional(p):
    '''expressao_relacional : expressao_aritmetica
                            | expressao_aritmetica '>' expressao_aritmetica
                            | expressao_aritmetica GE expressao_aritmetica
                            | expressao_aritmetica '<' expressao_aritmetica
                            | expressao_aritmetica LE expressao_aritmetica
                            | expressao_aritmetica NE expressao_aritmetica
                            | expressao_aritmetica EQ expressao_aritmetica'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[2], p[1], p[3])

def p_expressao_aritmetica(p):
    '''expressao_aritmetica : expressao_multiplicativa
                             | expressao_aritmetica '+' expressao_multiplicativa
                             | expressao_aritmetica '-' expressao_multiplicativa'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[2], p[1], p[3])

def p_expressao_multiplicativa(p):
    '''expressao_multiplicativa : expressao_unaria
                                  | expressao_multiplicativa '*' expressao_unaria
                                  | expressao_multiplicativa '/' expressao_unaria
                                  | expressao_multiplicativa '%' expressao_unaria'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[2], p[1], p[3])

def p_expressao_unaria(p):
    '''expressao_unaria : expressao_postfix
                         | '-' expressao_unaria
                         | INCREMENT expressao_postfix
                         | DECREMENT expressao_postfix'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[1], p[2])

def p_expressao_postfix(p):
    '''expressao_postfix : primaria
                         | primaria '[' expressao ']'
                         | primaria '(' argumentos ')'
                         | primaria '.' ID
                         | primaria ARROW ID'''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = (p[2], p[1], p[3])
    else:
        p[0] = (p[1], p[3])

def p_primaria(p):
    '''primaria : ID
                | NUM_INT
                | NUM_DEC
                | TEXTO
                | '(' expressao ')' '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]

def p_argumentos(p):
    '''argumentos : expressoes
                  | '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = []

def p_expressoes(p):
    '''expressoes : expressao
                  | expressoes ',' expressao'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[3])
        p[0] = p[1]

def p_error(p):
    if p:
        print("Erro de sintaxe na entrada:", p)
    else:
        print("Erro de sintaxe: Fim inesperado do arquivo")

parser = yacc.yacc()

# Teste
data = '''
int main() {
    int a = 5;
    float b = 3.14;
    return 0;
}
'''

parser.parse(data)
