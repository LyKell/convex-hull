from geometrie import distance


def graham(points):
	points = sorted(points)
	res1 = []
	for p in points:
		while len(res1) >= 2 and distance(res1[-1], res1[-2], p) > 0:
			res1.pop()
		res1.append(p)

	points.reverse()
	res2 = []
	for p in points:
		while len(res2) >= 2 and distance(res2[-1], res2[-2], p) > 0:
			res2.pop()
		res2.append(p)

	print(res1)
	print(res2)
	return res1 + res2