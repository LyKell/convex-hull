def distance(p, q, r):
    """
    Renvoie le produit en croix des vecteurs pq et pr, qui est un nombre :
    - positif si r est à droite de la droite (p, q), négatif s'il est à gauche,
    nul si les trois points sont alignés ;
    - de valeur absolue d'autant plus grande que le point r est éloigné de la
    droite (p, q), pour p et q fixés (attention, ce n'est pas la distance
    euclidienne !).
    """
    xp, yp = p
    xq, yq = q
    xr, yr = r
    return (xq - xp) * (yr - yp) - (xr - xp) * (yq - yp)