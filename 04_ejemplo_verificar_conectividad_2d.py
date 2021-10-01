from reticulado import Reticulado
from barra import Barra
from graficar2d import ver_reticulado_2d
from constantes import *
from math import sqrt
from secciones import Circular
from Puente import Puente
L = 2.*m_
import numpy as np

#Inicializar modelo
# ret = Reticulado()

# #Nodos
# ret.agregar_nodo(0,0)
# ret.agregar_nodo(L,0)
# ret.agregar_nodo(2*L,0)
# ret.agregar_nodo(L/2,sqrt(3)/L)
# ret.agregar_nodo(3*L/2,sqrt(3)/L)

# #Secciones de las barras
# circular_200_4 = Circular(200*mm_, 4*mm_)
# circular_200_8 = Circular(200*mm_, 8*mm_)

# #Crear y agregar las barras
# ret.agregar_barra(Barra(0, 1, circular_200_4)) #0
# ret.agregar_barra(Barra(1, 2, circular_200_4)) #1
# ret.agregar_barra(Barra(3, 4, circular_200_8)) #2
# ret.agregar_barra(Barra(0, 3, circular_200_8)) #3
# # ret.agregar_barra(Barra(3, 1, circular_200_4)) #4
# ret.agregar_barra(Barra(1, 4, circular_200_4)) #5
# ret.agregar_barra(Barra(4, 2, circular_200_8)) #6
ret = Puente()
#Crear restricciones
ret.agregar_restriccion(0, 0, 0)
ret.agregar_restriccion(0, 1, 0)
ret.agregar_restriccion(2, 1, 0)

#Fijar todos los nodos en Z
for n in range(ret.Nnodos):
	ret.agregar_restriccion(n, 2, 0.)

#Cargar el nodo 4 en la direccion 1 (Y)
ret.agregar_fuerza(4, 1, -100*KN_)

#Visualizar y comprobar las secciones
opciones_barras = {
	"ver_secciones_en_barras": True,
}
ver_reticulado_2d(ret,opciones_barras=opciones_barras)

#Resolver el problema
ret.ensamblar_sistema()
ret.resolver_sistema()
f = ret.obtener_fuerzas()

#Ver todo el reticulado en texto
print(ret)

#Visualizar resultados de fuerzas y nodos 
opcionesnodos = {
        "marcador_nodos": "o", 
        "ver_numeros_de_nodos": False,
        "color_nodos": "k",
        "color_borde_nodos": [0.7,0.7,0.7],
        "usar_posicion_deformada": False,
        "factor_amplificacion_deformada": 1.,
        "datos_desplazamientos_nodales": None,
        "ver_cargas": False
    }
    
    #Opciones para nodos
opcionesbarras = {
        "estilo_barras" : "-",
        "color_barras" : [138/255,89/255,0/255],#8F652F
        "grosor_barras" : 2,
        "ver_numeros_de_barras" : False,
        "color_barras_por_dato" : False,
        "ver_dato_en_barras" : False,
        "formato_dato_en_barras" : "4.2f",
        "color_barra_min" : np.array([1, 0, 0]),
        "color_barra_max" : np.array([0, 0, 1]),
        "color_barra_cero" : np.array([0, 0, 0]),
        "color_fondo" : np.array([1, 1, 1, 0.5]),
        "usar_posicion_deformada": False,
        "factor_amplificacion_deformada": 1.,
        "datos_desplazamientos_nodales": None,
        "ver_secciones_en_barras": False,
        "color_barras_por_seccion": False,
    }

ver_reticulado_2d(ret, 
	opciones_nodos=opcionesnodos, 
	opciones_barras=opcionesbarras)

Kff = ret.Kff

from scipy.linalg import eigh

w,v = eigh(Kff)

print(w)
print(v)

modo = 0

ret.u[ret.gdl_libres] = v[:,modo]
opciones_nodos = {
	"usar_posicion_deformada": False,
	"factor_amplificacion_deformada": 0.4,
}
ver_reticulado_2d(ret, opciones_nodos=opcionesnodos)