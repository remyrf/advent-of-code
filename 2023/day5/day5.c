#include <_stdio.h>
#include <stdio.h>

#define BUF_SIZE 4096

int main(void) {
    char line[BUF_SIZE];

    FILE *file = fopen("input.txt", "r");
    for (int i = 0; fgets(line, BUF_SIZE, file); i++) {
        printf("%s", line);
    }

    return 0;
}
