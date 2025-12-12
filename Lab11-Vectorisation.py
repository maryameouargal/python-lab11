# ETAPE 1
# Task 1.1 – Initialiser le projet
import numpy as np

# Task 1.2 – Définitions de base
A = np.array([5, 10, 15, 20])
B = np.array([1, 2, 3, 4])
print("A :", A)
print("B :", B)

# EATPE 2
#Task 2.1 – Addition, multiplication, exposant
addition = A + B
multiplication = A * B
puissances = A ** 2 
print("A + B =", addition)
print("A * B =", multiplication)
print("A ** 2 =", puissances)

# ETAPE 3
# Task 3.1 – Appliquer np.sin et np.log
angles = np.linspace(0, np.pi, 5)  
sinus = np.sin(angles)
logarithms = np.log(angles[1:])   

print("angles :", angles)
print("sin(angles) :", sinus)
print("log(angles[1:]) :", logarithms)

# Task 3.2– Explorer d’autres ufunc
print("exp(A) :", np.exp(A))
print("sqrt(B) :", np.sqrt(B))
print("abs(A - 10) :", np.abs(A - 10))
print("round(sin(angles), 3) :", np.round(sinus, 3))

# ETAPE 4
# Task 4.1– Créer un masque
masque = A > 10
print("Mask A > 10 :", masque)

# Task 4.2 – Filtrer les valeurs correspondantes
valeurs_filtrees = A[masque]
print("Values of A > 10 :", valeurs_filtrees)

#ETAPE 5 
print("Étape 5 – Broadcasting : principes et cas pratiques")

# Task 5.1 – Ajouter un scalaire
print("\n Task 5.1 – Ajouter un scalair")
addition_scalaire = A + 5
print("A + 5 =", addition_scalaire)

# Task 5.2– Addition d’un vecteur ligne à une matrice
print("\nTask 5.2– Addition d’un vecteur ligne à une matrice")
M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
vecteur_ligne = np.array([10, 20, 30])

print("Matrix M (shape {}):".format(M.shape))
print(M)
print("\nRow vector (shape {}):".format(vecteur_ligne.shape), vecteur_ligne)

resultat = M + vecteur_ligne
print("M + vecteur_ligne :\n", resultat)

# Task 5.3– Broadcasting colonne (optionnel)
print("\nTask 5.3– Broadcasting colonne (optionnel)")
vecteur_colonne = np.array([[10], [20], [30]])
resultat_colonne = M + vecteur_colonne
print("M + vecteur_colonne :\n", resultat_colonne)

# ETAPE 6
print("Étape 6 – Applications et vérifications")

# Task 6.1 – Calcul vectoriel global
print("\n Task 6.1 – Calcul vectoriel global")

C = (A * 2) + np.sin(A) - np.mean(A)
print("Opération composite sur A :", C)

# Task 6.2 – Filtrage après ufunc
print("\nTask 6.2 – Filtrage après ufunc")
log_A = np.log(A)
print("log(A) =", log_A)

masque_log = log_A > 2
print(" log(A) > 2:", log_A[masque_log])

# Task 6.3 – Contrôle des shapes
print("\nTask 6.3 – Contrôle des shapes")
print("Shape of A:", A.shape)
print("Shape of C:", C.shape)
print("Shape of log_A:", log_A.shape)

