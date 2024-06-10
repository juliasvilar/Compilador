%{
#include <stdio.h>
#include <stdlib.h>
%}

%token TIPO ID NUM_INT NUM_DEC TEXTO COMENTARIO

%%

programa : declaracoes
         ;

declaracoes : declaracao
            | declaracoes declaracao
            ;

declaracao : declaracao_variavel
           | declaracao_funcao
           | declaracao_estrutura
           | comentario
           ;

declaracao_variavel : tipo ID ';'
                    | tipo ID '=' expressao ';'
                    ;

tipo : INT
     | FLOAT
     | DOUBLE
     | CHAR
     | BOOLEAN
     ;

declaracao_funcao : tipo ID '(' parametros ')' bloco
                  ;

parametros : parametro
           | parametros ',' parametro
           ;

parametro : tipo ID
          | tipo ID '[' ']'
          | tipo ELLIPSIS ID
          ;

bloco : '{' declaracoes '}'
      ;

comentario : COMENTARIO
           ;

expressao : atribuicao
          ;

atribuicao : ID '=' expressao
           | ID ADD_ASSIGN expressao
           | ID SUB_ASSIGN expressao
           | ID MUL_ASSIGN expressao
           | ID DIV_ASSIGN expressao
           | ID MOD_ASSIGN expressao
           | ID LAND_ASSIGN expressao
           | ID LOR_ASSIGN expressao
           | ID '=' ID
           | ID ADD_ASSIGN ID
           | ID SUB_ASSIGN ID
           | ID MUL_ASSIGN ID
           | ID DIV_ASSIGN ID
           | ID MOD_ASSIGN ID
           | ID LAND_ASSIGN ID
           | ID LOR_ASSIGN ID
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
           | empty
           ;

expressoes : expressao
           | expressoes ',' expressao
           ;

empty:
    ;

%%
