import tkinter as tk

root = tk.Tk()
root.geometry("600x200")
root.title("Matrix Echelonizer")
root.config(background="#5094BE")


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
            while l < n and mat[l][p] == 0:
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
        
# response = 0
def ech(response):
    if response == 1 or response == 2:
        n = 3
        m = 3
        mat = [
            [0, 1, 2],
            [7, 0, 4],
            [0, 5, 6]
        ]

        # TEMPORARRY
        # print("Je suis désolé car je n'ai pas encore ajouté d'interface dynamique, donc nous allons nous en tenir à la deuxième option.")
        
        # print("\n-------matrice-------")
        # for i in range(n):
        #     for j in range(m):
        #         print(f"|{mat[i][j]:+.2f}", end="|")
        #     print("\n---------------------")

        # matEchelone = echelon(n, m, mat)
        # print("\n--matrice échelonnée-")
        # for i in range(n):
        #     for j in range(m):
        #         print(f"|{matEchelone[i][j]:+.2f}", end="|")
        #     print("\n---------------------")
            
            
        for i in range(n):
            for j in range(m):
                # Création du label avec les coordonnées en texte
                elementij = mat[i][j]
                element = tk.Label(root, text = elementij, borderwidth = 1, relief="solid", width = 10, height = 2)
                element.grid(row = i, column = j, padx = 5, pady = 5)

            
        bye.pack(anchor = "w")
    else:
        bye.pack(anchor = "w")
        
# def onClick(resp):
#     global response
#     response = resp
    
    



bienvenue = tk.Label(root, 
                  text = "Bienvenue à l'echelonizer matriciel calculator!\nSouhaitez-vous", 
                  bg = "#5094BE", 
                  fg = "#fff", 
                  font = ("Helvetica", 20)
                  ).pack(anchor = "w")



button1 = tk.Button(root, 
                    text = "1) échelonner une matrice?", 
                    command = lambda : ech(1)
                    ).pack(anchor = "w")

button2 = tk.Button(root, 
                    text = "2) voir comment le programme fonctionne?", 
                    command = lambda : ech(2)
                    ).pack(anchor = "w")

button3 = tk.Button(root, 
                    text = "3) quitter",
                    command = lambda : ech(3)
                    ).pack(anchor = "w")

element = tk.Label(root, text = "Matrice : ")

bye = tk.Label(root, 
                  text = "au revoir", 
                  bg = "#5094BE", 
                  fg = "#fff", 
                  font = ("Helvetica", 20)
                  )




















#match response:
    # case 1:
    #     print("saisez la taille de matrice")
    #     n, m = int(input("n = ")), int(input("m = "))
    #     mat = [[]]
    #     print("Saisez la matrice: ")
    #     for i in range(n):
    #         for j in range(m):
    #             mat[i][j] = input(f"a{i}{j} = ")
        



