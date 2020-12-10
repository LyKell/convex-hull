from geometrie import distance


def points_a_droite(points, debut, fin):
	"""Renvoie les point de la liste points situés à droite du segment
	 [debut, fin]."""
	res = []
	for p in points:
		if distance(debut, fin, p) > 0:
			res.append(p)
	return res


def plus_eloigne(debut, fin, points):
	"""Renvoie le point de la liste points le plus éloigné du segment
	 [debut, fin]."""
	max_dist = 0
	for point in points:
		if point != debut and point != fin:
			dist = distance(debut, fin, point)
			if dist > max_dist:
				max_dist = dist
				max_point = point
	return max_point


def quickhull_aux(points, debut, fin):
	lstPoints = points_a_droite(points, debut, fin)
	if len(lstPoints) == 0:
		return [debut, fin]
	r = plus_eloigne(debut, fin, points)
	res1 = quickhull_aux(points, debut, r)
	res2 = quickhull_aux(points, r, fin)
	return res1 + res2


def quickhull(points):
	p = min(points)
	q = max(points)
	res1 = quickhull_aux(points, p, q)
	res2 = quickhull_aux(points, q, p)
	return res1 + res2


