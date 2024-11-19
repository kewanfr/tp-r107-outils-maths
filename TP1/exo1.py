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

# print(euclide_etendu(210, 55))
# print(euclide_etendu(275, 78))