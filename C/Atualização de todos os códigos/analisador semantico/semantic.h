#ifndef SEMANTIC_H
#define SEMANTIC_H

#include <stdbool.h>

typedef struct {
    char* nome;
    char* tipo;
} Variavel;

void adicionarVariavel(char* nome, char* tipo);
bool verificarDeclaracaoVariavel(char* nome);
bool verificarCompatibilidadeTipos(char* tipo1, char* tipo2);
char* obterTipoVariavel(char* nome);

typedef struct {
    char* nome;
    char* tipo_retorno;
    char* tipos_parametros;
} Funcao;

void adicionarFuncao(char* nome, char* tipo_retorno, char* tipos_parametros);
bool verificarDeclaracaoFuncao(char* nome);

#endif
