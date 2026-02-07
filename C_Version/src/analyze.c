#include <stdio.h>
#include <stdlib.h>
#include "uthash.h"
#include <string.h>

struct Var {
    char* Name;
    char* Value;
    UT_hash_handle hh;
};
struct Var *vars = NULL;

void add_value(char* Name, char *Value) {
    struct Var *s;

    s = malloc(sizeof(struct Var));
    s->Name = Name;
    strcpy(s->Value, Value);
    HASH_ADD_STR( vars, Name, s );
}

void print(char* name) {
    printf("%s", name);
}

int main(int argc, char **argv) {
    const char* fname = "/home/kristiang/Krystalicks/C_Version/main.pk";
    FILE* fp = fopen(fname, "r");
    char line[256];
    char code[256] = "";

    while (fgets(line, sizeof(line), fp) != NULL) {
        strcpy(code, line);
    }

    printf("%c\n", code[0]);
    printf("%c\n", code[1]);
    printf("%c\n", code[2]);
    return 0;
}
