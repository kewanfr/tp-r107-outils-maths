import exo1
import math

lp = [2, 3, 5, 7, 11, 13]

def primalite(p):
    """
    Rôle: Vérifie la primalité d'un nombre p

    Entrée: - p, int, le nombre dont on veut vérifier la primalité

    Sortie: - est_premier, bool, est True si p est premier, False sinon
    """

    if p in lp:
        return True

    est_premier = True
    i = 0
    while est_premier and i < len(lp) and lp[i] <= math.sqrt(p):

        # if lp[i] > math.sqrt(p):
        #     premier = False

        q, r = exo1.division(p, lp[i])

        # print(q, r, p, lp[i], i)
        if r == 0:
            est_premier = False

        i += 1

    # if est_premier:
    #     lp.append(p)

    return est_premier

def premier(n):
    """
    Rôle: Cherche le nombre premier de rang n

    Entrée: - n, int, le rang dont on veut le nombre premier correspondant

    Sortie: - p, int, n-ième nombre premier
    """

    p = None

    if n < len(lp) - 1:
        return lp[n]
    
    for i in range(len(n)):
        
        

    return

print(primalite(15))
print(primalite(12))
print(primalite(11))
print(primalite(23))
print(primalite(29))
print(primalite(97))
print(210, primalite(337))
print(premier(2))
print(premier(1))
print(lp)