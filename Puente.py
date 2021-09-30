from reticulado import Reticulado
from barra import Barra
from graficar3d import ver_reticulado_3d
from constantes import *
from math import sqrt
from secciones import Circular

import numpy as np
#Inicializar modelo


#Nodos

#Tablero
def Puente():
    ret = Reticulado()
    
    L = 6.*m_
    H = L*sqrt(3)/2*m_
    B = 4.*m_

    ret.agregar_nodo(0*L,B,19.18)        # Nodo 0  (punto 7)
    ret.agregar_nodo(0*L,0,19.18)        # Nodo 1
    ret.agregar_nodo(1*L,B,19.18)        # Nodo 2
    ret.agregar_nodo(1*L,0,19.18)        # Nodo 3
    ret.agregar_nodo(2*L,B,19.18)        # Nodo 4
    ret.agregar_nodo(2*L,0,19.18)        # Nodo 5
    ret.agregar_nodo(3*L,B,19.18)        # Nodo 6
    ret.agregar_nodo(3*L,0,19.18)        # Nodo 7
    ret.agregar_nodo(4*L,B,19.18)        # Nodo 8
    ret.agregar_nodo(4*L,0,19.18)        # Nodo 9
    ret.agregar_nodo(5*L,B,19.18)        # Nodo 10
    ret.agregar_nodo(5*L,0,19.18)        # Nodo 11
    ret.agregar_nodo(6*L,B,19.18)        # Nodo 12
    ret.agregar_nodo(6*L,0,19.18)        # Nodo 13
    ret.agregar_nodo(7*L,B,19.18)        # Nodo 14
    ret.agregar_nodo(7*L,0,19.18)        # Nodo 15
    ret.agregar_nodo(8*L,B,19.18)        # Nodo 16
    ret.agregar_nodo(8*L,0,19.18)        # Nodo 17
    ret.agregar_nodo(9*L,B,19.18)        # Nodo 18
    ret.agregar_nodo(9*L,0,19.18)        # Nodo 19
    ret.agregar_nodo(10*L,B,19.18)        # Nodo 20
    ret.agregar_nodo(10*L,0,19.18)        # Nodo 21
    ret.agregar_nodo(11*L,B,19.18)        # Nodo 22
    ret.agregar_nodo(11*L,0,19.18)        # Nodo 23
    ret.agregar_nodo(12*L,B,19.18)        # Nodo 24
    ret.agregar_nodo(12*L,0,19.18)        # Nodo 25
    ret.agregar_nodo(13*L,B,19.18)        # Nodo 26
    ret.agregar_nodo(13*L,0,19.18)        # Nodo 27
    ret.agregar_nodo(14*L,B,19.18)        # Nodo 28
    ret.agregar_nodo(14*L,0,19.18)        # Nodo 29
    ret.agregar_nodo(15*L,B,19.18)        # Nodo 30
    ret.agregar_nodo(15*L,0,19.18)        # Nodo 31
    ret.agregar_nodo(16*L,B,19.18)        # Nodo 32
    ret.agregar_nodo(16*L,0,19.18)        # Nodo 33
    ret.agregar_nodo(17*L,B,19.18)        # Nodo 34
    ret.agregar_nodo(17*L,0,19.18)        # Nodo 35
    ret.agregar_nodo(18*L,B,19.18)        # Nodo 36
    ret.agregar_nodo(18*L,0,19.18)        # Nodo 37
    ret.agregar_nodo(19*L,B,19.18)        # Nodo 38
    ret.agregar_nodo(19*L,0,19.18)        # Nodo 39
    ret.agregar_nodo(20*L,B,19.18)       # Nodo 40
    ret.agregar_nodo(20*L,0,19.18)       # Nodo 41
    
    
    
    #Laterales:
    
    ret.agregar_nodo(1*L/2,B,19.18+H)        # Nodo 42
    ret.agregar_nodo(1*L/2,0,19.18+H)        # Nodo 43
    ret.agregar_nodo(3*L/2,B,19.18+H)        # Nodo 44
    ret.agregar_nodo(3*L/2,0,19.18+H)        # Nodo 45
    ret.agregar_nodo(5*L/2,B,19.18+H)        # Nodo 46
    ret.agregar_nodo(5*L/2,0,19.18+H)        # Nodo 47
    ret.agregar_nodo(7*L/2,B,19.18+H)        # Nodo 48
    ret.agregar_nodo(7*L/2,0,19.18+H)        # Nodo 49
    ret.agregar_nodo(9*L/2,B,19.18+H)        # Nodo 50
    ret.agregar_nodo(9*L/2,0,19.18+H)        # Nodo 51
    ret.agregar_nodo(11*L/2,B,19.18+H)        # Nodo 52
    ret.agregar_nodo(11*L/2,0,19.18+H)        # Nodo 53
    ret.agregar_nodo(13*L/2,B,19.18+H)        # Nodo 54
    ret.agregar_nodo(13*L/2,0,19.18+H)        # Nodo 55
    ret.agregar_nodo(15*L/2,B,19.18+H)        # Nodo 56
    ret.agregar_nodo(15*L/2,0,19.18+H)        # Nodo 57
    ret.agregar_nodo(17*L/2,B,19.18+H)        # Nodo 58
    ret.agregar_nodo(17*L/2,0,19.18+H)        # Nodo 59
    ret.agregar_nodo(19*L/2,B,19.18+H)        # Nodo 60
    ret.agregar_nodo(19*L/2,0,19.18+H)        # Nodo 61
    ret.agregar_nodo(21*L/2,B,19.18+H)        # Nodo 62
    ret.agregar_nodo(21*L/2,0,19.18+H)        # Nodo 63
    ret.agregar_nodo(23*L/2,B,19.18+H)        # Nodo 64
    ret.agregar_nodo(23*L/2,0,19.18+H)        # Nodo 65
    ret.agregar_nodo(25*L/2,B,19.18+H)        # Nodo 66
    ret.agregar_nodo(25*L/2,0,19.18+H)        # Nodo 67
    ret.agregar_nodo(27*L/2,B,19.18+H)        # Nodo 68
    ret.agregar_nodo(27*L/2,0,19.18+H)        # Nodo 69
    ret.agregar_nodo(29*L/2,B,19.18+H)        # Nodo 70
    ret.agregar_nodo(29*L/2,0,19.18+H)        # Nodo 71
    ret.agregar_nodo(31*L/2,B,19.18+H)        # Nodo 72
    ret.agregar_nodo(31*L/2,0,19.18+H)        # Nodo 73
    ret.agregar_nodo(33*L/2,B,19.18+H)        # Nodo 74
    ret.agregar_nodo(33*L/2,0,19.18+H)        # Nodo 75
    ret.agregar_nodo(35*L/2,B,19.18+H)        # Nodo 76
    ret.agregar_nodo(35*L/2,0,19.18+H)        # Nodo 77
    ret.agregar_nodo(37*L/2,B,19.18+H)        # Nodo 78
    ret.agregar_nodo(37*L/2,0,19.18+H)        # Nodo 79
    ret.agregar_nodo(39*L/2,B,19.18+H)        # Nodo 80
    ret.agregar_nodo(39*L/2,0,19.18+H)        # Nodo 81
    
    
    #Tablero(medios):
    
    ret.agregar_nodo(1*L/2,B/2,19.18)        # Nodo 82
    ret.agregar_nodo(3*L/2,B/2,19.18)        # Nodo 83
    ret.agregar_nodo(5*L/2,B/2,19.18)        # Nodo 84
    ret.agregar_nodo(7*L/2,B/2,19.18)        # Nodo 85
    ret.agregar_nodo(9*L/2,B/2,19.18)        # Nodo 86
    ret.agregar_nodo(11*L/2,B/2,19.18)        # Nodo 87
    ret.agregar_nodo(13*L/2,B/2,19.18)        # Nodo 88
    ret.agregar_nodo(15*L/2,B/2,19.18)        # Nodo 89
    ret.agregar_nodo(17*L/2,B/2,19.18)        # Nodo 90
    ret.agregar_nodo(19*L/2,B/2,19.18)        # Nodo 91
    ret.agregar_nodo(21*L/2,B/2,19.18)        # Nodo 92
    ret.agregar_nodo(23*L/2,B/2,19.18)        # Nodo 93
    ret.agregar_nodo(25*L/2,B/2,19.18)        # Nodo 94
    ret.agregar_nodo(27*L/2,B/2,19.18)        # Nodo 95
    ret.agregar_nodo(29*L/2,B/2,19.18)        # Nodo 96
    ret.agregar_nodo(31*L/2,B/2,19.18)        # Nodo 97
    ret.agregar_nodo(33*L/2,B/2,19.18)        # Nodo 98
    ret.agregar_nodo(35*L/2,B/2,19.18)        # Nodo 99
    ret.agregar_nodo(37*L/2,B/2,19.18)        # Nodo 100
    ret.agregar_nodo(39*L/2,B/2,19.18)        # Nodo 101



#Secciones de las barras
    circular_200_4 = Circular(200*mm_, 4*mm_, color="#3E701D")
    circular_200_8 = Circular(200*mm_, 8*mm_, color="#A3500B")
    
    #Crear y agregar las barras
    ret.agregar_barra(Barra(0, 1, circular_200_4)) #0
    ret.agregar_barra(Barra(2, 3, circular_200_4)) #1
    ret.agregar_barra(Barra(4, 5, circular_200_8)) #2
    ret.agregar_barra(Barra(6, 7, circular_200_8)) #3
    ret.agregar_barra(Barra(8, 9, circular_200_4)) #4
    ret.agregar_barra(Barra(10,11, circular_200_4)) #5
    ret.agregar_barra(Barra(12, 13, circular_200_8)) #6
    ret.agregar_barra(Barra(14, 15, circular_200_4)) #7
    ret.agregar_barra(Barra(16, 17, circular_200_4)) #8
    ret.agregar_barra(Barra(18, 19, circular_200_8)) #9
    ret.agregar_barra(Barra(20, 21, circular_200_4)) #10
    ret.agregar_barra(Barra(22, 23, circular_200_4)) #11
    ret.agregar_barra(Barra(24, 25, circular_200_8)) #12
    ret.agregar_barra(Barra(26, 27, circular_200_4)) #13
    ret.agregar_barra(Barra(28, 29, circular_200_4)) #14
    ret.agregar_barra(Barra(30, 31, circular_200_4)) #15
    ret.agregar_barra(Barra(32, 33, circular_200_4)) #16
    ret.agregar_barra(Barra(34, 35, circular_200_4)) #17
    ret.agregar_barra(Barra(36, 37, circular_200_4)) #18
    ret.agregar_barra(Barra(38, 39, circular_200_4)) #19
    ret.agregar_barra(Barra(40, 41, circular_200_4)) #20

    ret.agregar_barra(Barra(0, 2, circular_200_4)) #21
    ret.agregar_barra(Barra(2, 4, circular_200_4)) #22
    ret.agregar_barra(Barra(4, 6, circular_200_8)) #23
    ret.agregar_barra(Barra(6, 8, circular_200_8)) #24
    ret.agregar_barra(Barra(8, 10, circular_200_4)) #25
    ret.agregar_barra(Barra(10,12, circular_200_4)) #26
    ret.agregar_barra(Barra(12, 14, circular_200_8)) #27
    ret.agregar_barra(Barra(14, 16, circular_200_4)) #28
    ret.agregar_barra(Barra(16, 18, circular_200_4)) #29
    ret.agregar_barra(Barra(18, 20, circular_200_8)) #30
    ret.agregar_barra(Barra(20, 22, circular_200_4)) #31
    ret.agregar_barra(Barra(22, 24, circular_200_4)) #32
    ret.agregar_barra(Barra(24, 26, circular_200_8)) #33
    ret.agregar_barra(Barra(26, 28, circular_200_4)) #34
    ret.agregar_barra(Barra(28, 30, circular_200_4)) #35
    ret.agregar_barra(Barra(30, 32, circular_200_4)) #36
    ret.agregar_barra(Barra(32, 34, circular_200_4)) #37
    ret.agregar_barra(Barra(34, 36, circular_200_4)) #38
    ret.agregar_barra(Barra(36, 38, circular_200_4)) #39
    ret.agregar_barra(Barra(38, 40, circular_200_4)) #40
    
    ret.agregar_barra(Barra(1, 3, circular_200_4)) #41
    ret.agregar_barra(Barra(3, 5, circular_200_4)) #42
    ret.agregar_barra(Barra(5, 7, circular_200_8)) #43
    ret.agregar_barra(Barra(7, 9, circular_200_8)) #44
    ret.agregar_barra(Barra(9, 11, circular_200_4)) #45
    ret.agregar_barra(Barra(11,13, circular_200_4)) #46
    ret.agregar_barra(Barra(13, 15, circular_200_8)) #47
    ret.agregar_barra(Barra(15, 17, circular_200_4)) #48
    ret.agregar_barra(Barra(17, 19, circular_200_4)) #49
    ret.agregar_barra(Barra(19, 21, circular_200_8)) #50
    ret.agregar_barra(Barra(21, 23, circular_200_4)) #51
    ret.agregar_barra(Barra(23, 25, circular_200_4)) #52
    ret.agregar_barra(Barra(25, 27, circular_200_8)) #53
    ret.agregar_barra(Barra(27, 29, circular_200_4)) #54
    ret.agregar_barra(Barra(29, 31, circular_200_4)) #55
    ret.agregar_barra(Barra(31, 33, circular_200_4)) #56
    ret.agregar_barra(Barra(33, 35, circular_200_4)) #57
    ret.agregar_barra(Barra(35, 37, circular_200_4)) #58
    ret.agregar_barra(Barra(37, 39, circular_200_4)) #59
    ret.agregar_barra(Barra(39, 41, circular_200_4)) #60
    
    ret.agregar_barra(Barra(42, 43, circular_200_4)) #61
    ret.agregar_barra(Barra(44, 45, circular_200_8)) #62
    ret.agregar_barra(Barra(46, 47, circular_200_8)) #63
    ret.agregar_barra(Barra(48, 49, circular_200_4)) #64
    ret.agregar_barra(Barra(50, 51, circular_200_4)) #65
    ret.agregar_barra(Barra(52, 53, circular_200_8)) #66
    ret.agregar_barra(Barra(54, 55, circular_200_4)) #67
    ret.agregar_barra(Barra(56, 57, circular_200_4)) #68
    ret.agregar_barra(Barra(58, 59, circular_200_8)) #69
    ret.agregar_barra(Barra(60, 61, circular_200_4)) #70
    ret.agregar_barra(Barra(62, 63, circular_200_4)) #71
    ret.agregar_barra(Barra(64, 65, circular_200_8)) #72
    ret.agregar_barra(Barra(66, 67, circular_200_4)) #73
    ret.agregar_barra(Barra(68, 69, circular_200_4)) #74
    ret.agregar_barra(Barra(70, 71, circular_200_4)) #75
    ret.agregar_barra(Barra(72, 73, circular_200_4)) #76
    ret.agregar_barra(Barra(74, 75, circular_200_4)) #77
    ret.agregar_barra(Barra(76, 77, circular_200_4)) #78
    ret.agregar_barra(Barra(78, 79, circular_200_4)) #79
    ret.agregar_barra(Barra(80, 81, circular_200_4)) #80

    opcionesnodos = {
        "marcador_nodos": ".", 
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
    return(ver_reticulado_3d(ret,ver_nodos=True,
    ver_barras=True, zoom = 300, opciones_nodos = opcionesnodos,
    opciones_barras = opcionesbarras,tamaño_nueva_figura = [8, 8]), print(ret))

Puente()
# ver_reticulado_3d(ret)


