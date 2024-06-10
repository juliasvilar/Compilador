import ply.yacc as yacc
from lexer import tokens

def p_program(p):
    'program : declaration_list'
    pass

def p_declaration_list(p):
    '''declaration_list : declaration_list declaration
                        | declaration'''
    pass

def p_declaration(p):
    '''declaration : var_declaration
                   | fun_declaration'''
    pass

def p_var_declaration(p):
    '''var_declaration : type_specifier ID SEMICOLON
                       | type_specifier ID ASSIGN expression SEMICOLON'''
    pass

def p_type_specifier(p):
    '''type_specifier : INT
                      | FLOAT
                      | DOUBLE
                      | CHAR
                      | BOOLEAN'''
    pass

def p_fun_declaration(p):
    'fun_declaration : type_specifier ID LPAREN params RPAREN compound_stmt'
    pass

def p_params(p):
    '''params : param_list
              | VOID'''
    pass

def p_param_list(p):
    '''param_list : param_list COMMA param
                  | param'''
    pass

def p_param(p):
    'param : type_specifier ID'
    pass

def p_compound_stmt(p):
    'compound_stmt : LBRACE local_declarations statement_list RBRACE'
    pass

def p_local_declarations(p):
    '''local_declarations : local_declarations var_declaration
                          | empty'''
    pass

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | empty'''
    pass

def p_statement(p):
    '''statement : expression_stmt
                 | compound_stmt
                 | selection_stmt
                 | iteration_stmt
                 | return_stmt
                 | print_stmt'''
    pass

def p_expression_stmt(p):
    '''expression_stmt : expression SEMICOLON
                       | SEMICOLON'''
    pass

def p_selection_stmt(p):
    '''selection_stmt : IF LPAREN expression RPAREN statement ELSE statement
                      | IF LPAREN expression RPAREN statement'''
    pass

def p_iteration_stmt(p):
    '''iteration_stmt : WHILE LPAREN expression RPAREN statement
                      | FOR LPAREN expression_stmt expression_stmt expression RPAREN statement'''
    pass

def p_return_stmt(p):
    '''return_stmt : RETURN SEMICOLON
                   | RETURN expression SEMICOLON'''
    pass

def p_print_stmt(p):
    '''print_stmt : PRINTF LPAREN TEXTO RPAREN SEMICOLON
                  | PRINTF LPAREN expression RPAREN SEMICOLON'''
    pass

def p_expression(p):
    '''expression : assignment
                  | simple_expression'''
    pass

def p_assignment(p):
    '''assignment : var ASSIGN expression
                  | var ADD_ASSIGN expression
                  | var SUB_ASSIGN expression
                  | var MUL_ASSIGN expression
                  | var DIV_ASSIGN expression
                  | var MOD_ASSIGN expression'''
    pass

def p_var(p):
    '''var : ID
           | ID LBRACKET expression RBRACKET'''
    pass

def p_simple_expression(p):
    '''simple_expression : additive_expression relop additive_expression
                         | additive_expression'''
    pass

def p_relop(p):
    '''relop : GE
             | LE
             | GT
             | LT
             | EQ
             | NE'''
    pass

def p_additive_expression(p):
    '''additive_expression : additive_expression addop term
                           | term'''
    pass

def p_addop(p):
    '''addop : PLUS
             | MINUS'''
    pass

def p_term(p):
    '''term : term mulop factor
            | factor'''
    pass

def p_mulop(p):
    '''mulop : TIMES
             | DIVIDE
             | MOD'''
    pass

def p_factor(p):
    '''factor : LPAREN expression RPAREN
              | var
              | call
              | NUM_INT
              | NUM_DEC
              | TEXTO'''
    pass

def p_call(p):
    'call : ID LPAREN args RPAREN'
    pass

def p_args(p):
    '''args : arg_list
            | empty'''
    pass

def p_arg_list(p):
    '''arg_list : arg_list COMMA expression
                | expression'''
    pass

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    print(f"Syntax error at '{p.value}'")

parser = yacc.yacc()
