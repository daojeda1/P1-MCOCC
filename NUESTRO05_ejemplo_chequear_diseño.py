from reticulado import Reticulado
from barra import Barra
from graficar3d import ver_reticulado_3d
from constantes import *
from math import sqrt
from secciones import SeccionICHA
from Puente2 import Puente
import numpy as np

L = 6.*m_
H = 3.*m_
B = 4.*m_

q = 400*kgf_/m_**2

F = B*L*q

#Inicializar modelo
# ret = Reticulado()

#Nodos
# ret.agregar_nodo(0    ,0,0)
# ret.agregar_nodo(L    ,0,0)
# ret.agregar_nodo(2*L  ,0,0)
# ret.agregar_nodo(L/2  ,B/2,sqrt(3)*H)
# ret.agregar_nodo(3*L/2,B/2,sqrt(3)*H)
# ret.agregar_nodo(0    ,B,0)
# ret.agregar_nodo(L    ,B,0)
# ret.agregar_nodo(2*L  ,B,0)
ret = Puente()



#Secciones de las barras

# seccion_grande = SeccionICHA("[]350x150x37.8", color="#3A8431")#, debug=True)
# seccion_chica = SeccionICHA("[]80x40x8", color="#A3500B")


# Crear y agregar las barras
# ret.agregar_barra(Barra(0, 1, seccion_chica)) #0
# ret.agregar_barra(Barra(1, 2, seccion_chica)) #1
# ret.agregar_barra(Barra(3, 4, seccion_grande)) #2
# ret.agregar_barra(Barra(0, 3, seccion_grande)) #3
# ret.agregar_barra(Barra(3, 1, seccion_chica)) #4
# ret.agregar_barra(Barra(1, 4, seccion_chica)) #5
# ret.agregar_barra(Barra(4, 2, seccion_grande)) #6
# ret.agregar_barra(Barra(5, 6, seccion_chica)) #7
# ret.agregar_barra(Barra(6, 7, seccion_chica)) #8
# ret.agregar_barra(Barra(5, 3, seccion_grande)) #9
# ret.agregar_barra(Barra(3, 6, seccion_chica)) #10
# ret.agregar_barra(Barra(6, 4, seccion_chica)) #11
# ret.agregar_barra(Barra(4, 7, seccion_grande)) #12
# ret.agregar_barra(Barra(0, 5, seccion_chica)) #13
# ret.agregar_barra(Barra(1, 6, seccion_chica)) #14
# ret.agregar_barra(Barra(2, 7, seccion_chica)) #15
# ret.agregar_barra(Barra(0, 6, seccion_chica)) #15
# ret.agregar_barra(Barra(1, 5, seccion_chica)) #15
# ret.agregar_barra(Barra(6, 2, seccion_chica)) #15
# ret.agregar_barra(Barra(1, 7, seccion_chica)) #15


#Crear restricciones
for nodo in [0,5]:
	ret.agregar_restriccion(nodo, 0, 0)
	ret.agregar_restriccion(nodo, 1, 0)
	ret.agregar_restriccion(nodo, 2, 0)

for nodo in [2,7]:
	ret.agregar_restriccion(nodo, 1, 0)
	ret.agregar_restriccion(nodo, 2, 0)




#Visualizar y comprobar las secciones
opciones_nodos = {
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
opciones_barras = {
        "estilo_barras" : "-",
        "color_barras" : [138/255,89/255,0/255],#8F652F
        "grosor_barras" : 1,
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
        "color_barras_por_seccion": True,
    }
ver_reticulado_3d(ret,opciones_barras=opciones_barras, opciones_nodos = opciones_nodos)

# exit(0)



#Resolver el problema peso_propio
ret.ensamblar_sistema(factor_peso_propio=[0.,0.,-1.], factor_cargas=0.0)
ret.resolver_sistema()
f_D = ret.obtener_fuerzas()


#Agregar fuerzas tablero
ret.agregar_fuerza(0, 2, -F/4)
ret.agregar_fuerza(5, 2, -F/4)
ret.agregar_fuerza(2, 2, -F/4)
ret.agregar_fuerza(7, 2, -F/4)
ret.agregar_fuerza(1, 2, -F/2)
ret.agregar_fuerza(6, 2, -F/2)

#Resolver el problema peso_propio
ret.ensamblar_sistema(factor_peso_propio=[0.,0.,0], factor_cargas=1.0)
ret.resolver_sistema()
f_L = ret.obtener_fuerzas()



#Visualizar f_L en el reticulado

ver_reticulado_3d(ret, 
	opciones_nodos=opciones_nodos, 
	opciones_barras=opciones_barras,
	titulo="Carga Viva")


#Visualizar f_L en el reticulado


ver_reticulado_3d(ret, 
	opciones_nodos=opciones_nodos, 
	opciones_barras=opciones_barras,
	titulo="Carga Muerta")


#Calcular carga ultima (con factores de mayoracion)
fu = 1.2*f_D + 1.6*f_L



#Visualizar combinacion en el reticulado

ver_reticulado_3d(ret, 
	opciones_nodos=opciones_nodos, 
	opciones_barras=opciones_barras,
	titulo="1.2D + 1.6L")





cumple = ret.chequear_diseño(fu, ϕ=0.9)

if cumple:
	print(":)  El reticulado cumple todos los requisitos")
else:
	print(":(  El reticulado NO cumple todos los requisitos")

#Calcular factor de utilizacion para las barras
factores_de_utilizacion = ret.obtener_factores_de_utilizacion(fu, ϕ=0.9)


#Visualizar FU en el reticulado


ver_reticulado_3d(ret, 
	opciones_nodos=opciones_nodos, 
	opciones_barras=opciones_barras,
	titulo="Factor Utilizacion")


ret.guardar("05_ejemplo_chequear_diseño.h5")