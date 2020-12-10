from random import gauss
from upemtk import *


# SAVANE Kévin, Groupe TP7
# TP8




# --- Fonctions de dessin ---

def dessine_point(p, couleur='blue'):
	"""
	Dessine le point p sous la forme d'un cercle de rayon 1 de couleur donnée.
	"""
	x, y = p
	tag = "p-{}-{}".format(x, y)
	cercle(x, y, 1, remplissage='black', couleur=couleur, tag=tag)


def efface_point(p):
	"""
	Efface le point p.
	"""
	x, y = p
	tag = "p-{}-{}".format(x, y)
	efface(tag)


def dessine_segment(p, q, couleur='black'):
	"""
	Dessine le segment [p, q] dans la couleur donnée.
	"""
	x1, y1 = p
	x2, y2 = q
	tag = tag_segment(p, q)
	segment = ligne(x1, y1, x2, y2, couleur=couleur, tag=tag)
	return segment


def efface_segment(p, q):
	"""
	Efface le segment [p, q].
	"""
	efface(tag_segment(p, q))


def tag_segment(p, q):
	"""
	Renvoie un identifiant upemtk pour le segment [p, q].
	"""
	x1, y1 = min(p, q)
	x2, y2 = max(q, q)
	return "s-{}-{}-{}-{}".format(x1, y1, x2, y2)


def dessine_polygone(points):
	"""
	Dessine le polygone donné par la liste points. Le premier et le
	dernier point est supposé distinct du premier.
	"""
	for i in range(len(points)):
		dessine_segment(points[i - 1], points[i])


# --- Fonctions de choix des points ---

def points_fixes():
	"""
	Dessine et renvoie une liste fixée de quelques points tenant dans une
	fenÃªtre 800x600.
	"""
	points = [(471, 417), (592, 222), (520, 398), (623, 405),
			  (476, 160), (383, 139), (387, 409), (511, 312),
			  (386, 125), (623, 201), (405, 293), (462, 301),
			  (321, 374), (181, 216), (334, 270), (257, 199)]
	for p in points:
		dessine_point(p)
	return points


def points_manuels():
	"""
	Dessine et renvoie une liste de points désignés par les clics gauches de
	l'utilisateur. Un clic droit indique la fin de la saisie de points.
	"""
	points = []
	x, y, type_clic = attente_clic()
	while type_clic == 'ClicGauche':
		dessine_point((x, y))
		points.append((x, y))
		x, y, type_clic = attente_clic()
	return points


def points_aleatoires(largeur, hauteur, nombre, mu=.5, gamma=.15):
	"""
	Dessine et renvoie une liste de points aléatoires distribués selon une
	loi normale centrée autour du point (largeur * mu, hauteur * mu), avec un
	écart-type de gamma dans chaque dimension.
	"""
	points = []
	for _ in range(nombre):
		x = max(0, min(largeur-1, int(gauss(largeur*mu, largeur*gamma))))
		y = max(0, min(hauteur-1, int(gauss(hauteur*mu, hauteur*gamma))))
		dessine_point((x, y))
		points.append((x, y))
	return points


def points_saisis():
	"""
	Dessine et renvoie une liste de points saisie par l'utilisateur.
	"""
	points = eval(input("Saisir une liste de points :\n"))
	assert isinstance(points, list)
	for p in mes_points:
		dessine_point(p)
	return points


# --- Programme principal ---

if __name__ == '__main__':
	from jarvis import jarvis
	from graham import graham
	from quickhull import quickhull

	# Création de la fenÃªtre
	largeur = 800
	hauteur = 600
	cree_fenetre(largeur, hauteur)

	# Choix des points
	saisie = input("Choix des points ?"
				   "([a]léatoire, [m]anuel, [f]ixé, [s]aisir) ? ")
	if saisie == "a":
		mes_points = points_aleatoires(largeur, hauteur, 100)
	elif saisie == "m":
		mes_points = points_manuels()
	elif saisie == "f":
		mes_points = points_fixes()
	else:
		mes_points = points_saisis()

	# Choix de l'algorithme
	algos = {'j': jarvis, 'g': graham, 'q': quickhull}
	reponse = input("Algorithme {} ? ".format(list(algos.keys())))
	algo = algos[reponse]

	# Lancement de l'algo et affichage du résultat
	enveloppe = algo(mes_points)  # Ã  remplacer par "enveloppe = algo(mes_points)"
	dessine_polygone(enveloppe)
	print("Cliquer sur la fenêtre pour sortir.")
	attente_clic()
	ferme_fenetre()










## Exercice 2

# Question 1

"""
Lorsque l'on entre qu'une seule valeur en paramètre pour la fonction min, elle va chercher le minimum dans l'argument unique.
Si on entre deux arguments, la fonction va renvoyer le minimum entre ces deux arguments.
Ainsi, si on entre juste une liste en premier argument, sans arguments optionnels, la valeur renvoyée sera le minimum de la liste.
Dans le cas d'une liste de points, la fonction min va d'abord chercher les points au plus petit abscisse. Si deux points ou plus ont le même plus petit abscisse,
la fonction min va ensuiter chercher le point à la plus petite ordonnée.
"""


## Exercice 3

# Question 2

"""
La fonction sorted utilisée sur une liste de points va d'abord trier les éléments par rapport à leur abscisse, dans l'ordre croissant.
Si deux points ou plus ont la même abscisse, sorted triera alors ces éléments par rapport à leur ordonnée, dans l'ordre croissant.
"""