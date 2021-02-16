import math
import os.path
import pickle

# Calculo de la distancia entre dos puntos


class Point:
    def __init__(self, cx, cy, desc='p'):
        self.x = cx
        self.y = cy
        self.descripcion = desc


def to_string(point):
    r = str(point.descripcion) + '(' + str(point.x) + ', ' + str(point.y) + ')'
    return r


def distance_between(p1, p2):
    # calcular "delta y" y "delta x"
    dy = p2.y - p1.y
    dx = p2.x - p1.x

    # Distancia entre ellos... Pitágoras...
    return math.sqrt(pow(dx, 2) + pow(dy, 2))

def vector(fd):
    puntos = []
    if not os.path.exists(fd):
        print("El archivo no existe")
        return
    m = open(fd, "rb")
    t = os.path.getsize(fd)
    while m.tell() < t:
        p = pickle.load(m)
        puntos.append(p)
    m.close()
    return puntos

def display(vec):
    for i in range(len(vec)):
        print(to_string(vec[i]))

def calculo(puntos):
    dmax = 0
    dmin = distance_between(puntos[0], puntos[1])
    n = len(puntos)
    for i in range(0, n-1):
        for j in range(i+1, n):
            d = distance_between(puntos[i], puntos[j])
            if d < dmin:
                dmin = d
            if d > dmax:
                dmax = d
    return dmax, dmin


def principal():
    fd = "puntos.df4"
    puntos = vector(fd)
    dmax, dmin = calculo(puntos)
    print("Distancia maxima: ", dmax)
    print("Distancia minima: ",dmin)



if __name__ == "__main__":
    principal()