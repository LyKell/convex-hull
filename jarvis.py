from geometrie import distance


def sommet_suivant(points, p):
	if p == points[0]:
		res = points[1]
	else:
		res = points[0]

	for q in points:
		if distance(p, res, q) > 0:
			res = q
	return res


def jarvis(points):
	premier = min(points)
	suivant = sommet_suivant(points, premier)
	res = [premier]
	
	while premier != suivant:
		res.append(suivant)
		suivant = sommet_suivant(points, res[-1])

	return res