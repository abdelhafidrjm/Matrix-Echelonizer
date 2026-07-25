#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void echelon(int n, int m, float mat[n][m]) {
    int k = 0;
    int p = 0;
    float swap = 0;

    while ((k < n) && (p < m)) {
        float pivot = mat[k][p];

        while (pivot == 0) {
            int l = k;
            while (l < n && mat[l][p] == 0) l++;
            if (l < n) {
                for (int r = p; r < m; r++) {
                    swap = mat[k][r];
                    mat[k][r] = mat[l][r];
                    mat[l][r] = swap;
                }
                pivot = mat[k][p];
            } else {
                if (p < m - 1) {
                    p++;
                    pivot = mat[k][p];
                } else {
                    return;
                }
            }
        }
        for (int i = k + 1; i < n; i++) {
            float alpha = -mat[i][p] / pivot;
            for (int j = p; j < m; j++) mat[i][j] = mat[i][j] + alpha * mat[k][j];
        }

        k++;
        p++;
    }
}

int main() {

    printf("Bienvenue a l'echelonizer matriciel calculator!");

    int n = 3;
    int m = 3;
    float mat[3][3] = {
        {1, 5, 6},
        {4, 3, 3},
        {1, 2, 4}
    };
    printf("Je suis desole car je n'ai pas encore ajoute d'interface dynamique, donc nous allons nous en tenir a la deuxiwme option.");
      
    printf("\n-------matrice-------\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            printf("|%+.2f|", mat[i][j]);
        }
        printf("\n---------------------\n");
    }

    echelon(n, m, mat);

    printf("\n--matrice echelonnee-\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            printf("|%+.2f|", mat[i][j]);
        }
        printf("\n---------------------\n");
    }

    printf("bye-bye");

    return 0;
}