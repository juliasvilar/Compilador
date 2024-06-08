%{
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char* nome;
    char* tipo;
} Variavel;

Variavel variaveis[100];
int num_variaveis = 0;

typedef struct {
    char* nome;
    char* tipo_retorno;
    char* tipos_parametros;
} Funcao;

Funcao funcoes[100];
int num_funcoes = 0;

bool verificarDeclaracaoVariavel(char* nome) {
    for (int i = 0; i < num_variaveis; i++) {
        if (strcmp(variaveis[i].nome, nome) == 0) {
            return true;
        }
    }
    return false;
}

bool verificarDeclaracaoFuncao(char* nome) {
    for (int i = 0; i < num_funcoes; i++) {
        if (strcmp(funcoes[i].nome, nome) == 0) {
            return true;
        }
    }
    return false;
}

bool verificarCompatibilidadeTipos(char* tipo1, char* tipo2) {
    return strcmp(tipo1, tipo2) == 0;
}

%}

%option noyywrap

...

declaracao_variavel : tipo ID ';' { 
                        if (verificarDeclaracaoVariavel($2)) {
                            printf("Erro semântico: Variável '%s' já foi declarada.\n", $2);
                        } else {
                            variaveis[num_variaveis].nome = strdup($2);
                            variaveis[num_variaveis].tipo = strdup($1);
                            num_variaveis++;
                        }
                    }
                    | tipo ID '=' expressao ';' { 
                        if (verificarDeclaracaoVariavel($2)) {
                            printf("Erro semântico: Variável '%s' já foi declarada.\n", $2);
                        } else {
                            variaveis[num_variaveis].nome = strdup($2);
                            variaveis[num_variaveis].tipo = strdup($1);
                            num_variaveis++;
                        }
                    }
                    ;

lista_parametros : /* vazio */ { $$ = strdup(""); } 
                 | lista_parametros ',' parametro { 
                        char* tipos_parametros = (char*)malloc(strlen($1) + strlen($3) + 2);
                        strcpy(tipos_parametros, $1);
                        strcat(tipos_parametros, ",");
                        strcat(tipos_parametros, $3);
                        $$ = tipos_parametros;
                    }
                 ;

parametro : tipo ID { 
                $$ = strdup($1);
            }
         ;

tipo : INT { $$ = "int"; }
     | FLOAT { $$ = "float"; }
     | CHAR { $$ = "char"; }
     | BOOL { $$ = "bool"; }
     ;

expressao : ...
          | ID { 
                if (!verificarDeclaracaoVariavel($1)) {
                    printf("Erro semântico: Variável '%s' não foi declarada.\n", $1);
                }
                $$ = variaveis[$1].tipo;
            }
          ...
          | INT { $$ = "int"; }
          | FLOAT { $$ = "float"; }
          | CHAR { $$ = "char"; }
          | BOOL { $$ = "bool"; }
          ...
          ;

%%
