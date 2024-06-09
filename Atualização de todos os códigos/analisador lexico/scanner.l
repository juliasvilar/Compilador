%{
#include "parser.h"
#include <stdio.h>
#include <string.h>
%}

%option noyywrap

DIGITO       [0-9]
LETRA        [a-zA-Z]
ID           [a-zA-Z_][a-zA-Z0-9_]*
NUM_INT      [0-9]+
NUM_DEC      [0-9]+\.[0-9]+
TEXTO        \"[^\"]*\"
COMENTARIO   \/\/.*
OPERADOR     [=+\-*/%&|!><]=?|\|\||&&|!=|>|>=|<|<=
SIMBOLO_ESP  [\(\)\[\]\{\},;#!?:.]
ESPACO       [ \t\n]

%%

void|scanf|printf { printf("PALAVRA_RES: %s\n", yytext); }
stdio|string|stdlib { printf("BIBLIOTECA: %s\n", yytext); }
int { yylval.str = strdup("int"); return INT; }
float { yylval.str = strdup("float"); return FLOAT; }
double { yylval.str = strdup("double"); return DOUBLE; }
char { yylval.str = strdup("char"); return CHAR; }
boolean { yylval.str = strdup("boolean"); return BOOLEAN; }
if|else { printf("CONDICIONAL: %s\n", yytext); }
for|while { printf("FUNCAO RECURSIVA: %s\n", yytext); }
return { printf("RETORNO: %s\n", yytext); }
main { printf("FUNCAO PRINCIPAL: %s\n", yytext); }

{ESPACO}     { /* Ignorar espaços */ }
{NUM_INT}    { yylval.str = strdup("int"); return NUM_INT; }
{NUM_DEC}    { yylval.str = strdup("float"); return NUM_DEC; }
{ID}         { yylval.str = strdup(yytext); return ID; }
{TEXTO}      { yylval.str = strdup(yytext); return TEXTO; }
{OPERADOR}   { printf("OPERADOR: %s\n", yytext); }
{SIMBOLO_ESP} { printf("SIMBOLO_ESP: %s\n", yytext); }
{COMENTARIO} { /* Ignorar comentários */ }
.            { printf("Erro: Caractere não reconhecido: %s\n", yytext); }

%%

int yywrap() {
    return 1;
}
