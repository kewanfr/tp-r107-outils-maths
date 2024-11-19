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
