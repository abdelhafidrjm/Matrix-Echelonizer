def echelon(n , m, mat):
# initialization
    k = 0
    p = 0
    
    while (k < n) and (p < m):
        # intialization of the pivot
        pivot = mat[k][p]
        
        # check if pivot is null
        while pivot == 0:
            l = k
            while mat[l][p] == 0 and l < n:
                l += 1 
                
            if l < n:
                # alterning the two lines
                for r in range(p, m):
                    swap = mat[k][r]
                    mat[k][r] = mat[l][r]
                    mat[l][r] = swap
                pivot = mat[k][p]
            else:
                # no pivot in this column so next one
                if p < m - 1:
                    p += 1
                    pivot = mat[k][p]
                # all the columns are null so it is already reduced
                else:
                    return mat
                
# Li <- Li + aLj
        for i in range(k+1, n):
            alpha = -mat[i][p] / pivot
            for j in range(p, m):
                mat[i][j] = mat[i][j] + alpha * mat[k][j]
                
# Next pivot
        k += 1
        p += 1
        
# Return the reduced matrix
    return mat
        
    

print("Bienvenue à l'echelonizer matriciel calculator!")
print("Souhaitez-vous \n 1) échelonner une matrice? \n 2)Voir comment le programme fonctionne? \n 3)Quitter")
response = int(input("Select (1 or 2): "))

#match response:
    # case 1:
    #     print("saisez la taille de matrice")
    #     n, m = int(input("n = ")), int(input("m = "))
    #     mat = [[]]
    #     print("Saisez la matrice: ")
    #     for i in range(n):
    #         for j in range(m):
    #             mat[i][j] = input(f"a{i}{j} = ")
        
if response == 1 or response == 2:
        n = 3
        m = 3
        mat = [
            [0, 1, 2],
            [7, 0, 4],
            [0, 5, 6]
        ]

        # TEMPORARRY
        print("Je suis désolé car je n'ai pas encore ajouté d'interface dynamique, donc nous allons nous en tenir à la deuxième option.")
        
        print("\n-------matrice-------")
        for i in range(n):
            for j in range(m):
                print(f"|{mat[i][j]:+.2f}", end="|")
            print("\n---------------------")

        matEchelone = echelon(n, m, mat)
        print("\n--matrice échelonnée-")
        for i in range(n):
            for j in range(m):
                print(f"|{matEchelone[i][j]:+.2f}", end="|")
            print("\n---------------------")
            
        print("bye-bye")

else:
    print("bye-bye")