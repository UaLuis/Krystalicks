#include <stdio.h>
#include "uthash.h"

typedef struct Var {
    char* Name;
    char* Value;
    UT_hash_handle hh;
};
Var *vars = NULL;

void add_value(Var *s)

void print(char* name) {
    printf("%s", name);
}

int main(int argc, char **argv) {
    const char* fname = "/home/kristiang/Krystalicks/C_Version/main.pk";
    FILE* fp = fopen(fname, "r");
    char line[256];
    //char Text[256];

    while (fgets(line, sizeof(line), fp) != NULL)
        //strcpy(Text, line);
        //
    //printf(Text);
    return 0;
}
