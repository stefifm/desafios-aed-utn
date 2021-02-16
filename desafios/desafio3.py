print("Desafío 3")

import soporte


# def arreglos(v):
#     num = []
#     cont = []
#     for i in range(len(v)):
#         if i == v[i]:
#             cont[i] += 1
#         else:
#             num.append(v[i])
#             cont.append(1)
#     return num, cont




def busqueda_lineal(v, x):
    r = -1
    for i in range(len(v)):
        if x == v[i]:
            r = i
    return r

# def orden_sort(v):
#     #algoritmo de selección directa
#     n = len(v)
#     for i in range(n-1):
#         for j in range(i+1, n):
#             if v[i] > v[j]:
#                 v[i], v[j] = v[j], v[i]
#     return v


def test():
    v = soporte.vector_known_range(300000)
    # v = soporte.vector_unknown_range(300000)
    # num = []
    # cont = []
    #
    #
    # for x in v:
    #     i = busqueda_lineal(num, x)
    #     if i != -1:
    #         cont[i] += 1
    #     else:
    #         num.append(x)
    #         cont.append(1)

    c = [0] * 300000
    dif = 0
    modal = 0
    frecuencia = 0
    for x in v:
        c[x] += 1
    for n in range(len(c)):
        if c[n] != 0:
            dif += 1
        if c[n] > frecuencia:
            frecuencia = c[n]
            modal = n



    print(dif)
    print(modal)
    print(frecuencia)

test()