# -*- coding: utf-8 -*-
"""crontol_IR.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1V7fHTyZqJ1zE-sJLmHkZqukFqS5ZPaco

Input
"""

347711, 8792, 4309, 558, 508, 587, 501, 587, 531, 557, 508, 584, 504, 591, 503, 588, 526, 559, 531, 585, 1564, 560, 1589, 561, 1589, 559, 1590, 560, 1590, 562, 1587, 594, 1554, 597, 1552, 588, 503, 626, 1522, 621, 470, 628, 463, 623, 468, 622, 469, 627, 1520, 624, 467, 629, 1520, 629, 464, 629, 1518, 631, 1519, 636, 1513, 632, 1516, 631, 462, 630, 1519, 631, 2410733, 8790, 4287, 588, 500, 624, 467, 587, 505, 618, 474, 584, 507, 584, 505, 588, 502, 587, 506, 584, 1591, 561, 1565, 585, 1565, 585, 1588, 593, 1531, 587, 1566, 582, 1563, 586, 1569, 584, 503, 589, 1560, 618, 473, 588, 502, 588, 505, 616, 474, 586, 1589, 563, 502, 593, 1557, 590, 499, 588, 1590, 561, 1587, 586, 1565, 595, 1530, 618, 474, 610, 1563, 590, 2510622, 8792, 4286, 616, 473, 587, 504, 614, 475, 587, 505, 586, 502, 588, 505, 587, 505, 586, 502, 586, 1588, 564, 1586, 591, 1558, 563, 1586, 565, 1585, 594, 1554, 564, 1586, 588, 1562, 626, 465, 623, 1524, 628, 465, 624, 466, 618, 473, 627, 463, 622, 1527, 626, 466, 628, 1519, 629, 463, 630, 1519, 630, 1518, 631, 1520, 629, 1520, 631, 462, 627, 1519, 628, 2010074, 8797, 4281, 590, 498, 590, 499, 589, 503, 624, 467, 612, 477, 624, 469, 587, 502, 624, 470, 587, 1561, 590, 1583, 565, 1584, 593, 1557, 597, 1552, 591, 1558, 588, 1560, 596, 1553, 622, 469, 623, 1525, 628, 464, 627, 464, 595, 495, 620, 470, 624, 1525, 623, 468, 627, 1522, 626, 465, 629, 1519, 630, 1519, 630, 1519, 629, 1520, 628, 465, 626, 1520, 630, 2307477, 8793, 4286, 618, 473, 584, 507, 583, 507, 583, 508, 590, 499, 584, 532, 562, 504, 586, 503, 615, 1560, 561, 1588, 586, 1564, 561, 1587, 597, 1553, 563, 1587, 587, 1562, 600, 1549, 590, 502, 590, 1557, 595, 498, 620, 470, 619, 473, 593, 497, 619, 1530, 626, 465, 624, 1524, 628, 465, 626, 1521, 629, 1521, 631, 1518, 631, 1519, 631, 462, 627, 1521, 630, 2361384, 8832, 4250, 582, 508, 586, 505, 611, 503, 594, 474, 586, 529, 585, 481, 614, 476, 618, 473, 587, 1587, 563, 1586, 562, 1587, 565, 1584, 597, 1552, 591, 1558, 599, 1551, 621, 1528, 624, 469, 627, 1520, 628, 464, 629, 462, 628, 462, 628, 463, 627, 1521, 630, 462, 629, 1520, 631, 461, 631, 1517, 631, 1519, 632, 1518, 631, 1519, 630, 462, 628, 1520, 628, 2514057, 8790, 4289, 583, 506, 585, 531, 560, 506, 583, 532, 561, 503, 587, 530, 562, 529, 561, 503, 586, 1589, 564, 1585, 558, 1591, 562, 1587, 564, 1585, 562, 1587, 564, 1585, 564, 1585, 601, 491, 593, 1555, 602, 490, 594, 496, 625, 466, 591, 500, 622, 1526, 621, 472, 627, 1520, 626, 466, 626, 1521, 629, 1521, 631, 1517, 632, 1518, 656, 438, 627, 1520, 631, 2339487, 8790, 4289, 585, 506, 581, 508, 585, 504, 587, 503, 562, 528, 594, 500, 583, 504, 587, 508, 588, 1583, 560, 1590, 560, 1590, 584, 1565, 588, 1561, 564, 1585, 591, 1559, 599, 1550, 602, 489, 590, 1558, 594, 498, 595, 496, 624, 467, 621, 469, 626, 1522, 628, 464, 626, 1522, 630, 462, 628, 1520, 630, 1520, 630, 1519, 632, 1517, 631, 461, 630, 1517, 632, 2355335, 8796, 4282, 587, 507, 614, 499, 563, 529, 594, 496, 566, 523, 563, 528, 563, 528, 537, 555, 565, 1582, 563, 1587, 589, 1559, 592, 1559, 591, 1557, 600, 1549, 598, 1551, 626, 1523, 628, 464, 630, 1518, 630, 462, 629, 461, 630, 461, 631, 459, 630, 1518, 631, 462, 629, 1518, 631, 462, 630, 1517, 631, 1519, 631, 1517, 632, 1518, 628, 465, 627, 1521, 628, 2363514, 8794, 4284, 588, 529, 560, 531, 563, 526, 584, 508, 559, 531, 559, 532, 560, 531, 559, 532, 564, 1584, 564, 1586, 563, 1585, 539, 1612, 587, 1560, 565, 1585, 621, 1528, 625, 1524, 630, 464, 629, 1519, 629, 463, 630, 461, 630, 460, 632, 459, 641, 1508, 631, 462, 630, 1516, 633, 461, 630, 1516, 633, 1517, 632, 1518, 630, 1521, 629, 463, 627, 1521, 630,

input_data = [347711, 8792, 4309, 558, 508, 587, 501, 587, 531, 557, 508, 584, 504, 591, 503, 588, 526, 559, 531, 585, 1564, 560, 1589, 561, 1589, 559, 1590, 560, 1590, 562, 1587, 594, 1554, 597, 1552, 588, 503, 626, 1522, 621, 470, 628, 463, 623, 468, 622, 469, 627, 1520, 624, 467, 629, 1520, 629, 464, 629, 1518, 631, 1519, 636, 1513, 632, 1516, 631, 462, 630, 1519, 631, 2410733, 8790, 4287, 588, 500, 624, 467, 587, 505, 618, 474, 584, 507, 584, 505, 588, 502, 587, 506, 584, 1591, 561, 1565, 585, 1565, 585, 1588, 593, 1531, 587, 1566, 582, 1563, 586, 1569, 584, 503, 589, 1560, 618, 473, 588, 502, 588, 505, 616, 474, 586, 1589, 563, 502, 593, 1557, 590, 499, 588, 1590, 561, 1587, 586, 1565, 595, 1530, 618, 474, 610, 1563, 590, 2510622, 8792, 4286, 616, 473, 587, 504, 614, 475, 587, 505, 586, 502, 588, 505, 587, 505, 586, 502, 586, 1588, 564, 1586, 591, 1558, 563, 1586, 565, 1585, 594, 1554, 564, 1586, 588, 1562, 626, 465, 623, 1524, 628, 465, 624, 466, 618, 473, 627, 463, 622, 1527, 626, 466, 628, 1519, 629, 463, 630, 1519, 630, 1518, 631, 1520, 629, 1520, 631, 462, 627, 1519, 628, 2010074, 8797, 4281, 590, 498, 590, 499, 589, 503, 624, 467, 612, 477, 624, 469, 587, 502, 624, 470, 587, 1561, 590, 1583, 565, 1584, 593, 1557, 597, 1552, 591, 1558, 588, 1560, 596, 1553, 622, 469, 623, 1525, 628, 464, 627, 464, 595, 495, 620, 470, 624, 1525, 623, 468, 627, 1522, 626, 465, 629, 1519, 630, 1519, 630, 1519, 629, 1520, 628, 465, 626, 1520, 630, 2307477, 8793, 4286, 618, 473, 584, 507, 583, 507, 583, 508, 590, 499, 584, 532, 562, 504, 586, 503, 615, 1560, 561, 1588, 586, 1564, 561, 1587, 597, 1553, 563, 1587, 587, 1562, 600, 1549, 590, 502, 590, 1557, 595, 498, 620, 470, 619, 473, 593, 497, 619, 1530, 626, 465, 624, 1524, 628, 465, 626, 1521, 629, 1521, 631, 1518, 631, 1519, 631, 462, 627, 1521, 630, 2361384, 8832, 4250, 582, 508, 586, 505, 611, 503, 594, 474, 586, 529, 585, 481, 614, 476, 618, 473, 587, 1587, 563, 1586, 562, 1587, 565, 1584, 597, 1552, 591, 1558, 599, 1551, 621, 1528, 624, 469, 627, 1520, 628, 464, 629, 462, 628, 462, 628, 463, 627, 1521, 630, 462, 629, 1520, 631, 461, 631, 1517, 631, 1519, 632, 1518, 631, 1519, 630, 462, 628, 1520, 628, 2514057, 8790, 4289, 583, 506, 585, 531, 560, 506, 583, 532, 561, 503, 587, 530, 562, 529, 561, 503, 586, 1589, 564, 1585, 558, 1591, 562, 1587, 564, 1585, 562, 1587, 564, 1585, 564, 1585, 601, 491, 593, 1555, 602, 490, 594, 496, 625, 466, 591, 500, 622, 1526, 621, 472, 627, 1520, 626, 466, 626, 1521, 629, 1521, 631, 1517, 632, 1518, 656, 438, 627, 1520, 631, 2339487, 8790, 4289, 585, 506, 581, 508, 585, 504, 587, 503, 562, 528, 594, 500, 583, 504, 587, 508, 588, 1583, 560, 1590, 560, 1590, 584, 1565, 588, 1561, 564, 1585, 591, 1559, 599, 1550, 602, 489, 590, 1558, 594, 498, 595, 496, 624, 467, 621, 469, 626, 1522, 628, 464, 626, 1522, 630, 462, 628, 1520, 630, 1520, 630, 1519, 632, 1517, 631, 461, 630, 1517, 632, 2355335, 8796, 4282, 587, 507, 614, 499, 563, 529, 594, 496, 566, 523, 563, 528, 563, 528, 537, 555, 565, 1582, 563, 1587, 589, 1559, 592, 1559, 591, 1557, 600, 1549, 598, 1551, 626, 1523, 628, 464, 630, 1518, 630, 462, 629, 461, 630, 461, 631, 459, 630, 1518, 631, 462, 629, 1518, 631, 462, 630, 1517, 631, 1519, 631, 1517, 632, 1518, 628, 465, 627, 1521, 628, 2363514, 8794, 4284, 588, 529, 560, 531, 563, 526, 584, 508, 559, 531, 559, 532, 560, 531, 559, 532, 564, 1584, 564, 1586, 563, 1585, 539, 1612, 587, 1560, 565, 1585, 621, 1528, 625, 1524, 630, 464, 629, 1519, 629, 463, 630, 461, 630, 460, 632, 459, 641, 1508, 631, 462, 630, 1516, 633, 461, 630, 1516, 633, 1517, 632, 1518, 630, 1521, 629, 463, 627, 1521, 630, ]

"""Cuenta los datos del input_data"""

cantidad = len(input_data)
print (cantidad)

input_list =[347711, 8792, 4309, 558, 508, 587, 501, 587, 531, 557, 508, 584, 504, 591, 503, 588, 526, 559, 531, 585, 1564, 560, 1589, 561, 1589, 559, 1590, 560, 1590, 562, 1587, 594, 1554, 597, 1552, 588, 503, 626, 1522, 621, 470, 628, 463, 623, 468, 622, 469, 627, 1520, 624, 467, 629, 1520, 629, 464, 629, 1518, 631, 1519, 636, 1513, 632, 1516, 631, 462, 630, 1519, 631]

"""Cuenta los datos de la primera lista de input_list"""

cantidad2 = len(input_list)
print (cantidad2)

"""Arreglo de listas"""

lista_sig =[]

lista = []

for dato in input_data:
  if dato>347000:
    lista=[dato]
    lista_sig.append(lista)
  elif lista:

    lista.append(dato)

print(lista_sig)

"""Verifica la cantidad de datos en cada lista"""

for dato in lista_sig:
  print(len(dato), end=', ')

"""Mostrar los datos en el rango adecuado

"""

import matplotlib.pyplot as plt


# Trazar todas las listas en un solo gráfico
for lista in lista_sig:
    plt.plot(lista[3:], marker='o', linestyle='-', label=f'Lista {lista_sig.index(lista) + 1}')

# Agregar etiquetas y título
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Gráfico de listas')

# Mostrar leyenda
plt.legend()

# Mostrar el gráfico
plt.show()

# Transponer la lista para tener las listas agrupadas por índice
listas_transpuestas = list(map(list, zip(*lista_sig)))

# Calcular el promedio de cada dato
promedios = [sum(datos) / len(datos) for datos in listas_transpuestas]
promed_sin3= promedios[4:]

print(promed_sin3)

import matplotlib.pyplot as plt

# Crear el gráfico
plt.plot(range(1, len(promed_sin3) + 1), promed_sin3, marker='o', linestyle='-', color='b', label='Lista sin primeros tres elementos')

# Agregar etiquetas y título
plt.xlabel('Índice')
plt.ylabel('Valor')
plt.title('Gráfico de la lista sin primeros tres elementos')

# Agregar el valor de x en cada punto
for x, y in zip(range(1, len(promed_sin3) + 1), promed_sin3):
    plt.text(x, y, f'{x}', ha='center', va='bottom', fontsize=8, color='black')


# Mostrar leyenda
plt.legend()

# Mostrar el gráfico
plt.show()

#lista con los 32 bits
lista_pares = promed_sin3[::2]
bits=len(lista_pares)

print (lista_pares)
print(bits, "bits")

binario=[('1' if lista_pares[i] > 1400 else '0')  for i in range(32) ]
binario=''.join(binario)
binario

cod=[int(binario[i*8 : (i+1)*8],2)  for i in range(4)]
cod

"""El codigo obtenido para la tecla 7 es:"""

[hex(val) for val in cod]

"""
INTEGRANTES:

* Giussepe Dario Sanabria Combariza Cod: 20142005027
* Luis Miguel Arevalo Becerra, Cod: 20192005098
* Yeimy Camila Morales Bedoya, Cod:20190015132
 * tecla 7"""