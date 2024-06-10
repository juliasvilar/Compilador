%{
#include <stdio.h>
#include <stdlib.h>
#include "semantic.h"

extern int yylex();
void yyerror(const char* s);

%}

%union {
    char* str;
}

%token <str> INT FLOAT DOUBLE CHAR BOOLEAN ID NUM_INT NUM_DEC TEXTO COMENTARIO

%type <str> tipo expressao

%start programa

%%

programa : declaracoes
         ;

declaracoes : declaracao
            | declaracoes declaracao
            ;

declaracao : declaracao_variavel
           | declaracao_funcao
           | comentario
           ;

declaracao_variavel : tipo ID ';' {
                        if (verificarDeclaracaoVariavel($2)) {
                            printf("Erro semântico: Variável '%s' já foi declarada.\n", $2);
                        } else {
                            adicionarVariavel($2, $1);
                        }
                    }
                    | tipo ID '=' expressao ';' {
                        if (verificarDeclaracaoVariavel($2)) {
                            printf("Erro semântico: Variável '%s' já foi declarada.\n", $2);
                        } else {
                            adicionarVariavel($2, $1);
                            if (!verificarCompatibilidadeTipos($1, $4)) {
                                printf("Erro semântico: Tipos incompatíveis na atribuição de '%s' a '%s'.\n", $4, $1);
                            }
                        }
                    }
                    ;

tipo : INT { $$ = "int"; }
     | FLOAT { $$ = "float"; }
     | DOUBLE { $$ = "double"; }
     | CHAR { $$ = "char"; }
     | BOOLEAN { $$ = "boolean"; }
     ;

declaracao_funcao : tipo ID '(' parametros ')' bloco {
                        if (verificarDeclaracaoFuncao($2)) {
                            printf("Erro semântico: Função '%s' já foi declarada.\n", $2);
                        } else {
                            adicionarFuncao($2, $1, $4);
                        }
                    }
                    ;

parametros : parametro
           | parametros ',' parametro
           ;

parametro : tipo ID { $$ = $1; }
          ;

bloco : '{' declaracoes '}'
      ;

comentario : COMENTARIO
           ;

expressao : atribuicao
          | expressao_logica
          | expressao_relacional
          | expressao_aritmetica
          ;

atribuicao : ID '=' expressao
           | ID ADD_ASSIGN expressao
           | ID SUB_ASSIGN expressao
           | ID MUL_ASSIGN expressao
           | ID DIV_ASSIGN expressao
           | ID MOD_ASSIGN expressao
           | ID LAND_ASSIGN expressao
           | ID LOR_ASSIGN expressao
           ;

expressao_logica : expressao_relacional
                 | expressao_logica LAND expressao_relacional
                 | expressao_logica LOR expressao_relacional
                 | LNOT expressao_relacional
                 ;

expressao_relacional : expressao_aritmetica
                     | expressao_aritmetica '>' expressao_aritmetica
                     | expressao_aritmetica GE expressao_aritmetica
                     | expressao_aritmetica '<' expressao_aritmetica
                     | expressao_aritmetica LE expressao_aritmetica
                     | expressao_aritmetica NE expressao_aritmetica
                     | expressao_aritmetica EQ expressao_aritmetica
                     ;

expressao_aritmetica : expressao_multiplicativa
                     | expressao_aritmetica '+' expressao_multiplicativa
                     | expressao_aritmetica '-' expressao_multiplicativa
                     ;

expressao_multiplicativa : expressao_unaria
                          | expressao_multiplicativa '*' expressao_unaria
                          | expressao_multiplicativa '/' expressao_unaria
                          | expressao_multiplicativa '%' expressao_unaria
                          ;

expressao_unaria : expressao_postfix
                | '-' expressao_unaria
                | INCREMENT expressao_postfix
                | DECREMENT expressao_postfix
                ;

expressao_postfix : primaria
                  | primaria '[' expressao ']'
                  | primaria '(' argumentos ')'
                  | primaria '.' ID
                  | primaria ARROW ID
                  ;

primaria : ID
         | NUM_INT
         | NUM_DEC
         | TEXTO
         | '(' expressao ')'
         ;

argumentos : expressoes
           | /* vazio */
           ;

expressoes : expressao
           | expressoes ',' expressao
           ;

%%

void yyerror(const char* s) {
    fprintf(stderr, "Erro de sintaxe: %s\n", s);
}

int main() {
    return yyparse();
}
