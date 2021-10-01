from reticulado import Reticulado
from barra import Barra
from graficar3d import ver_reticulado_3d
from constantes import *
from math import sqrt
from secciones import SeccionICHA
from Puente import Puente
import numpy as np
import sys


ret = Puente()


nombre_archivo = "05_ejemplo_chequear_diseño.h5"

if len(sys.argv) > 1:
	nombre_archivo = sys.argv[1]


print(f"Abriendo: {nombre_archivo}" )

ret.abrir(nombre_archivo)



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
    # return(ver_reticulado_3d
ver_reticulado_3d(ret,opciones_nodos=opcionesnodos,opciones_barras=opcionesbarras)




#Resolver el problema peso_propio
ret.ensamblar_sistema(factor_peso_propio=[0.,0.,-1.], factor_cargas=0.0)
ret.resolver_sistema()
f_D = ret.obtener_fuerzas()


#Resolver el problema carga viva
ret.ensamblar_sistema(factor_peso_propio=[0.,0.,0], factor_cargas=1.0)
ret.resolver_sistema()
f_L = ret.obtener_fuerzas()



#Calcular carga ultima (con factores de mayoracion)
FU_caso1 = 1.4*f_D
FU_caso2 = 1.2*f_D + 1.6*f_L




cumple_caso1 = ret.chequear_diseño(FU_caso1, ϕ=0.9)
cumple_caso2 = ret.chequear_diseño(FU_caso2, ϕ=0.9)



#Revisar que cumple el diseño 
if cumple_caso1:
	print(":)  El reticulado cumple todos los requisitos 1.4 D")
else:
	print(":(  El reticulado NO cumple todos los requisitos 1.4 D")

if cumple_caso2:
	print(":)  El reticulado cumple todos los requisitos 1.2 D + 1.6 L")
else:
	print(":(  El reticulado NO cumple todos los requisitos 1.2 D + 1.6 L")


PESO_TOTAL = ret.calcular_peso_total()

print(f"\nPESO_TOTAL = {PESO_TOTAL} kg\n")

CARGA_VIVA_TOTAL = -400*9.81*117.48*4 

print(f"CARGA_VIVA_TOTAL = {CARGA_VIVA_TOTAL} N ")

CARGA_VIVA_APLICADA = 0.
for  nodo in ret.cargas:
	for gdl, val in ret.cargas[nodo]:
		if gdl == 2:
			CARGA_VIVA_APLICADA += val


print(f"CARGA_VIVA_APLICADA = {CARGA_VIVA_APLICADA} N ")

if abs(CARGA_VIVA_APLICADA - CARGA_VIVA_TOTAL) > 1e-3:
	print(f"\n\n***** CARGA VIVA APLICADA NO CORRESPONDE ***")


