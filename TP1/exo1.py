def divV0(a, b):
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

    return (q, r)