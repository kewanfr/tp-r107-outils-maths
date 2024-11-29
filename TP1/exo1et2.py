def division(a, b):
    """
    Entrées:
        - a, int, dividende de l'opération
        - b, int, diviseur de l'opération

    Sorties:
        - q, int, quotient de la division euclidienne
        - r, int, reste de la division euclidienne

    Rôle: Effectue une division euclidienne
    """
    
    # Initie le quotient et le reste
    q = 0
    r = a
    
    # Tant que le reste est supérieur au diviseur
    while r >= b:
        # Augmente le quotient
        q += 1
        
        # Retire le diviseur au reste
        r -= b

    return q, r

def euclide(a, b):

    if a <= b or b == 0:
        return None
    
    q, r = division(a, b)

    if r == 0:
        return b
    
    return euclide(b, r)

# print(euclide(60, 36))
# print(euclide(125, 90))

def euclide_etendu(a, b, u0 = 1, u1 = 0, v0 = 0, v1 = 1):
    if not a > b and not b > 0:
        return None

    q, r = division(a, b)

    if r == 0:
        return b, u1, v1
    
    return euclide_etendu(b, r, u1, u0 - q*u1, v1, v0 - q*v1)


import exo1
import math

lp = [2, 3, 5, 7, 11, 13]


def liste_premiers(n):
    """
    Renvoie la liste des nombres premiers inférieurs à n
    """

    nb_test = lp[len(lp) - 1] + 1
    while nb_test < n:
        
        est_divisible = False
        nbP = lp[0]
        i = 0
        p = False

        while nbP <= math.sqrt(nb_test):
            _, r = division(nb_test, nbP)
            # print(nb_test, nbP, q, r)
            if r == 0:
                est_divisible = True

            i += 1
            nbP = lp[i]

        if not est_divisible:
            lp.append(nb_test)

        nb_test += 1

    return lp

def est_premier(n):
    """
    Renvoie si un nombre est premier
    """
    premier = False

    lp = liste_premiers(n)

    for el in lp:
        if el == n:
            premier = True

    return premier

def nEmePremier(n):
    """
    Renvoie le n-ême nombre premier
    """
    if len(lp) >= n:
        return lp[n - 1]
    
    nb_test = lp[len(lp) - 1] + 1
    while len(lp) < n:
        
        est_divisible = False
        nbP = lp[0]
        i = 0

        while nbP <= math.sqrt(nb_test):
            _, r = division(nb_test, nbP)

            if r == 0:
                est_divisible = True

            i += 1
            nbP = lp[i]

        if not est_divisible:
            lp.append(nb_test)

        nb_test += 1
    
    return lp[n - 1]
