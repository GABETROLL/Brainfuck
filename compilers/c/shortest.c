#include <stdio.h>
int main(int c,char**v){for(;*v[1]&&*v[1]!=']';v[1]++){char*s=*v[1]==43?"(*p)++;":*v[1]==45?"(*p)--;":*v[1]==62?"p++;":*v[1]==60?"p--;":*v[1]==46?"putchar(*p);":*v[1]==44?"getchar();":"";if(*s)puts(s);else if(*v[1]==91){puts("while(*p){");v[1]++;main(c,v);puts("}");}}return 0;}