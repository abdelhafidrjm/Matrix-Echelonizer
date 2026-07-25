import tkinter as tk

root = tk.Tk()
root.maxsize(500, 500)
root.title("Matrix Echelonizer")
root.config(background="#8925B3")

n = 0
m = 0

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
                for r in range(p, m): mat[k][r], mat[l][r] = mat[l][r], mat[k][r]
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
        
# Function that display matrices
def display(n, m, matrix, title, parent):
    title.grid(row = 0, column = 0, columnspan = m, sticky = "n")
    for i in range(n):
        for j in range(m):
            element = tk.Label(parent, text = matrix[i][j], borderwidth = 1, relief="solid", width = 5, height = 2)
            element.grid(row = i+1, column = j, padx = 5, pady = 5)
        
# def saisez():
#     global n, m
#     n = n.get()
#     m = m.get()
        
def ech(response):
    global n, m
    if response == 1:
        # ligne = tk.Label(lc, text = "Saisez le nombre des lignes")
        # ligne.grid(row = 0, column=0)
        # n = tk.Entry(lc).grid(row = 0, column = 1)
        # ligne = tk.Label(lc, text = "Saisez le nombre des lignes")
        # ligne.grid(row = 1, column = 0)
        # m = tk.Entry(lc).grid(row = 1, column = 1)
        # submitButton = tk.Button(lc, text = "Saisez les", command = saisez)
        # submitButton.grid(row = 2, column = 0, columnspan = 2)
        # lc.pack()
        pass
    
    elif response == 2:
        n = 3
        m = 3
        mat = [
            [0, 1, 2],
            [7, 0, 4],
            [0, 5, 6]
            ]
            
        title = tk.Label(matrice, text = "La Matrice : ", font = ("Arial", 15, "bold"))
        display(n, m, mat, title, matrice)
                
        tk.Label(matrices, text = "→", font = ("Arial", 20), bg = "#8925B3").grid(row = 0, column = 1) 
                
        titleE = tk.Label(matriceE, text = "L'Echelonement : ", font = ("Arial", 15, "bold"))
        display(n, m, echelon(n, m, mat), titleE, matriceE)
        
        # disabling the button so it stops redesplaying the example
        button2.config(state = "disabled")

            
    # bye.pack(anchor = "w")
            
    
    

bienvenue = tk.Label(root, 
                  text = "Bienvenue à l'echelonizer matriciel calculator!\nSouhaitez-vous", 
                  bg = "#8925B3", 
                  fg = "#fff", 
                  font = ("Helvetica", 18)
                  ).pack(anchor = "w")

# input
buttons = tk.Frame(root)
buttons.columnconfigure(0, weight = 1)


button1 = tk.Button(buttons, 
                    text = "1) échelonner une matrice?", 
                    command = lambda : ech(1),
                    width = 35,
                    anchor="w", 
                    relief = "raised", 
                    borderwidth = 5, 
                    )
button1.grid(row = 0, column = 0, sticky = "w")

button2 = tk.Button(buttons, 
                    text = "2) voir comment le programme fonctionne?", 
                    command = lambda : ech(2), 
                    width = 35,
                    anchor="w", 
                    relief = "raised", 
                    borderwidth = 5
                    )
button2.grid(row = 1, column = 0, sticky = "w")

button3 = tk.Button(buttons, 
                    text = "3) quitter",
                    width = 35, 
                    command = root.destroy,
                    anchor="w", 
                    relief = "raised", 
                    borderwidth = 5
                    )
button3.grid(row = 2, column = 0, sticky = "w")

buttons.pack(padx = 5, pady = 5, anchor = "w")


lc = tk.Frame(root)
matrices = tk.Frame(root)

matrice = tk.Frame(matrices)
matriceE = tk.Frame(matrices)

matrices.columnconfigure(0, weight = 1)
matrices.columnconfigure(1, weight = 2)
matrices.columnconfigure(2, weight = 1)
matrices.config(bg = "#8925B3")

matrice.grid(row = 0, column = 0, padx = 5, pady = 5)
matriceE.grid(row = 0, column = 2, padx = 5, pady = 5)
matrices.pack()

root.mainloop()