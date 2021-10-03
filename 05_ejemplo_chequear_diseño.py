from reticulado import Reticulado
from barra import Barra
from graficar3d import ver_reticulado_3d
from constantes import *
from math import sqrt
from secciones import SeccionICHA
from secciones import Circular


import numpy as np
# L = 6.*m_
# H = 3.*m_
# B = 4.*m_
L = 6.*m_
H = sqrt(23)*m_
B = 4.*m_

q = 400*kgf_/m_**2

F = B*L*q

x = 5.075777986710320100e+00 
z = 4.281724747887941618e+01
#Inicializar modelo
ret = Reticulado()

#Nodos
#############################
ret.agregar_nodo(0*L+x,B,z)        # Nodo 0 (Nodo 7 par)
ret.agregar_nodo(0*L+x,0,z)        # Nodo 1 (Nodo 7 impar)
ret.agregar_nodo(1*L+x,B,z)        # Nodo 2
ret.agregar_nodo(1*L+x,0,z)        # Nodo 3
ret.agregar_nodo(2*L+x,B,z)        # Nodo 4
ret.agregar_nodo(2*L+x,0,z)        # Nodo 5
ret.agregar_nodo(3*L+x,B,z)        # Nodo 6
ret.agregar_nodo(3*L+x,0,z)        # Nodo 7
ret.agregar_nodo(4*L+x,B,z)        # Nodo 8
ret.agregar_nodo(4*L+x,0,z)        # Nodo 9
ret.agregar_nodo(5*L+x,B,z)        # Nodo 10
ret.agregar_nodo(5*L+x,0,z)        # Nodo 11
ret.agregar_nodo(6*L+x,B,z)        # Nodo 12
ret.agregar_nodo(6*L+x,0,z)        # Nodo 13
ret.agregar_nodo(7*L+x,B,z)        # Nodo 14
ret.agregar_nodo(7*L+x,0,z)        # Nodo 15
ret.agregar_nodo(8*L+x,B,z)        # Nodo 16
ret.agregar_nodo(8*L+x,0,z)        # Nodo 17
ret.agregar_nodo(9*L+x,B,z)        # Nodo 18
ret.agregar_nodo(9*L+x,0,z)        # Nodo 19
ret.agregar_nodo(10*L+x,B,z)        # Nodo 20
ret.agregar_nodo(10*L+x,0,z)        # Nodo 21
ret.agregar_nodo(11*L+x,B,z)        # Nodo 22
ret.agregar_nodo(11*L+x,0,z)        # Nodo 23
ret.agregar_nodo(12*L+x,B,z)        # Nodo 24
ret.agregar_nodo(12*L+x,0,z)        # Nodo 25
ret.agregar_nodo(13*L+x,B,z)        # Nodo 26
ret.agregar_nodo(13*L+x,0,z)        # Nodo 27
ret.agregar_nodo(14*L+x,B,z)        # Nodo 28
ret.agregar_nodo(14*L+x,0,z)        # Nodo 29
ret.agregar_nodo(15*L+x,B,z)        # Nodo 30
ret.agregar_nodo(15*L+x,0,z)        # Nodo 31
ret.agregar_nodo(16*L+x,B,z)        # Nodo 32
ret.agregar_nodo(16*L+x,0,z)        # Nodo 33
ret.agregar_nodo(17*L+x,B,z)        # Nodo 34
ret.agregar_nodo(17*L+x,0,z)        # Nodo 35
ret.agregar_nodo(18*L+x,B,z)        # Nodo 36
ret.agregar_nodo(18*L+x,0,z)        # Nodo 37
ret.agregar_nodo(19*L+x,B,z)        # Nodo 38
ret.agregar_nodo(19*L+x,0,z)        # Nodo 39
ret.agregar_nodo(20*L+x,B,z)       # Nodo 40
ret.agregar_nodo(20*L+x,0,z)       # Nodo 41


#Tablero(medios):

ret.agregar_nodo(1*L/2+x,B/2,z)        # Nodo 42
ret.agregar_nodo(3*L/2+x,B/2,z)        # Nodo 43
ret.agregar_nodo(5*L/2+x,B/2,z)        # Nodo 44
ret.agregar_nodo(7*L/2+x,B/2,z)        # Nodo 45
ret.agregar_nodo(9*L/2+x,B/2,z)        # Nodo 46
ret.agregar_nodo(11*L/2+x,B/2,z)        # Nodo 47
ret.agregar_nodo(13*L/2+x,B/2,z)        # Nodo 48
ret.agregar_nodo(15*L/2+x,B/2,z)        # Nodo 49
ret.agregar_nodo(17*L/2+x,B/2,z)        # Nodo 50
ret.agregar_nodo(19*L/2+x,B/2,z)        # Nodo 51
ret.agregar_nodo(21*L/2+x,B/2,z)        # Nodo 52
ret.agregar_nodo(23*L/2+x,B/2,z)        # Nodo 53
ret.agregar_nodo(25*L/2+x,B/2,z)        # Nodo 54
ret.agregar_nodo(27*L/2+x,B/2,z)        # Nodo 55
ret.agregar_nodo(29*L/2+x,B/2,z)        # Nodo 56
ret.agregar_nodo(31*L/2+x,B/2,z)        # Nodo 57
ret.agregar_nodo(33*L/2+x,B/2,z)        # Nodo 58
ret.agregar_nodo(35*L/2+x,B/2,z)        # Nodo 59
ret.agregar_nodo(37*L/2+x,B/2,z)        # Nodo 60
ret.agregar_nodo(39*L/2+x,B/2,z)        # Nodo 61

#Superiores(medios):

ret.agregar_nodo(1*L/2+x,B/2,z+H)        # Nodo 62
ret.agregar_nodo(3*L/2+x,B/2,z+H)        # Nodo 63
ret.agregar_nodo(5*L/2+x,B/2,z+H)        # Nodo 64
ret.agregar_nodo(7*L/2+x,B/2,z+H)        # Nodo 65
ret.agregar_nodo(9*L/2+x,B/2,z+H)        # Nodo 66
ret.agregar_nodo(11*L/2+x,B/2,z+H)        # Nodo 67
ret.agregar_nodo(13*L/2+x,B/2,z+H)        # Nodo 68
ret.agregar_nodo(15*L/2+x,B/2,z+H)        # Nodo 69
ret.agregar_nodo(17*L/2+x,B/2,z+H)        # Nodo 70
ret.agregar_nodo(19*L/2+x,B/2,z+H)        # Nodo 71
ret.agregar_nodo(21*L/2+x,B/2,z+H)        # Nodo 72
ret.agregar_nodo(23*L/2+x,B/2,z+H)        # Nodo 73
ret.agregar_nodo(25*L/2+x,B/2,z+H)        # Nodo 74
ret.agregar_nodo(27*L/2+x,B/2,z+H)        # Nodo 75
ret.agregar_nodo(29*L/2+x,B/2,z+H)        # Nodo 76
ret.agregar_nodo(31*L/2+x,B/2,z+H)        # Nodo 77
ret.agregar_nodo(33*L/2+x,B/2,z+H)        # Nodo 78
ret.agregar_nodo(35*L/2+x,B/2,z+H)        # Nodo 79
ret.agregar_nodo(37*L/2+x,B/2,z+H)        # Nodo 80
ret.agregar_nodo(39*L/2+x,B/2,z+H)        # Nodo 81




#Apoyos:
ret.agregar_nodo(-1.404922251873611572e+01,0,4.281724747887941618e+01)        # Nodo 82
ret.agregar_nodo(-1.131707961280499219e+01,0,4.281724747887941618e+01)        # Nodo 83
ret.agregar_nodo(-8.584936706873868673e+00,0,4.281724747887941618e+01)        # Nodo 84
ret.agregar_nodo(-5.852793800942746039e+00,0,4.281724747887941618e+01)        # Nodo 85
ret.agregar_nodo(-3.120651004297338993e+00,0,4.281724747887941618e+01)        # Nodo 86
ret.agregar_nodo(-3.885080000090714303e-01,0,4.281724747887941618e+01)        # Nodo 87
ret.agregar_nodo(2.343634807564907163e+00,0,4.281724747887941618e+01)         # Nodo 88
ret.agregar_nodo(5.075777986710320100e+00,0,4.281724747887941618e+01)         # Nodo 89
ret.agregar_nodo(7.261492147526644736e+00,0,4.117796173532074278e+01)         # Nodo 90
ret.agregar_nodo(9.447206472271542310e+00,0,3.844581882938962281e+01)        # Nodo 91
ret.agregar_nodo(1.203126941841552444e+01,0,3.589392741239155527e+01)        # Nodo 92
ret.agregar_nodo(1.557551065670554635e+01,0,3.425652848672371675e+01)        # Nodo 93
ret.agregar_nodo(1.987061142983234419e+01,0,3.306472622258439742e+01)        # Nodo 94
ret.agregar_nodo(2.477708327459076898e+01,0,3.129976846249586231e+01)        # Nodo 95
ret.agregar_nodo(3.111720940566445037e+01,0,2.931484806276514021e+01)        # Nodo 96
ret.agregar_nodo(3.873145234877593168e+01,0,2.795682878137194294e+01)        # Nodo 97
ret.agregar_nodo(4.682869826836961380e+01,0,2.594085812394389023e+01)        # Nodo 98
ret.agregar_nodo(5.443343663273993371e+01,0,2.459114127841323238e+01)        # Nodo 99
ret.agregar_nodo(6.256338958148909768e+01,0,2.488153583002742408e+01)        # Nodo 100  Nodo18
ret.agregar_nodo(6.804476221508502931e+01,0,2.363405959703677794e+01)        # Nodo 101
ret.agregar_nodo(7.403904003641143561e+01,0,2.417869370676238816e+01)        # Nodo 102
ret.agregar_nodo(7.939304016773286321e+01,0,2.613017923446748370e+01)        # Nodo 103
ret.agregar_nodo(8.338472827472728000e+01,0,2.754290694540905093e+01)        # Nodo 104
ret.agregar_nodo(8.840793693585601432e+01,0,2.914731579191635191e+01)        # Nodo 105
ret.agregar_nodo(9.359720524280722032e+01,0,3.134224945968302478e+01)        # Nodo 106
ret.agregar_nodo(1.001543482170419139e+02,0,3.516724734227227600e+01)        # Nodo 107
ret.agregar_nodo(1.078043483536490612e+02,0,3.899224741057584254e+01)        # Nodo 108
ret.agregar_nodo(1.170936342338148819e+02,0,4.008510457294829621e+01)        # Nodo 109
ret.agregar_nodo(1.225579200456771218e+02,0,4.281724747887941618e+01)        # Nodo 110 (Nodo28impar)
ret.agregar_nodo(1.252900629516082489e+02,0,4.281724747887941618e+01)        # Nodo 111
ret.agregar_nodo(1.280222058575393760e+02,0,4.281724747887941618e+01)        # Nodo 112
ret.agregar_nodo(1.307543487634704888e+02,0,4.281724747887941618e+01)        # Nodo 113
ret.agregar_nodo(1.334864916694016301e+02,0,4.281724747887941618e+01)        # Nodo 114
ret.agregar_nodo(1.362186345753327430e+02,0,4.281724747887941618e+01)        # Nodo 115
ret.agregar_nodo(1.389507774812638559e+02,0,4.281724747887941618e+01)        # Nodo 116

ret.agregar_nodo(1.225579200456771218e+02,B,4.281724747887941618e+01)        # Nodo 117 (Nodo28par)

#Nodos Torre:

ret.agregar_nodo(9*L+x,B,z-L)        # Nodo 118
ret.agregar_nodo(9*L+x,0,z-L)        # Nodo 119
ret.agregar_nodo(10*L+x,B,z-L)        # Nodo 120
ret.agregar_nodo(10*L+x,0,z-L)        # Nodo 121
ret.agregar_nodo(9*L+x,B,z-2*L)        # Nodo 122
ret.agregar_nodo(9*L+x,0,z-2*L)        # Nodo 123
ret.agregar_nodo(10*L+x,B,z-2*L)        # Nodo 124
ret.agregar_nodo(10*L+x,0,z-2*L)        # Nodo 125
ret.agregar_nodo(9*L+x,B,2.488153583002742408e+01)        # Nodo 126
ret.agregar_nodo(9*L+x,0,2.488153583002742408e+01)        # Nodo 127
ret.agregar_nodo(10*L+x,B,2.488153583002742408e+01)        # Nodo 128
ret.agregar_nodo(10*L+x,0,2.488153583002742408e+01)        # Nodo 129
ret.agregar_nodo(6.256338958148909768e+01,B,2.488153583002742408e+01)        # Nodo 130

ret.agregar_nodo(19*L/2+x,B,z-L/2)        # Nodo 131
ret.agregar_nodo(19*L/2+x,0,z-L/2)        # Nodo 132
ret.agregar_nodo(10*L+x,B/2,z-L/2)        # Nodo 133
ret.agregar_nodo(9*L+x,B/2,z-L/2)        # Nodo 134
ret.agregar_nodo(19*L/2+x,B,z-3*L/2)        # Nodo 135
ret.agregar_nodo(19*L/2+x,0,z-3*L/2)        # Nodo 136
ret.agregar_nodo(10*L+x,B/2,z-3*L/2)        # Nodo 137
ret.agregar_nodo(9*L+x,B/2,z-3*L/2)        # Nodo 138
ret.agregar_nodo(19*L/2+x,B,z-5*L/2)        # Nodo 139
ret.agregar_nodo(19*L/2+x,0,z-5*L/2)        # Nodo 140
ret.agregar_nodo(10*L+x,B/2,z-5*L/2)        # Nodo 141
ret.agregar_nodo(9*L+x,B/2,z-5*L/2)        # Nodo 142
ret.agregar_nodo(19*L/2+x,B/2,z-L)        # Nodo 143
ret.agregar_nodo(19*L/2+x,B/2,z-2*L)        # Nodo 144
ret.agregar_nodo(19*L/2+x,B/2,2.488153583002742408e+01)        # Nodo 145



#blue: #0000FF
#turquoise1: #00F5FF
#violetred1: #FF3E96
#yellow1: #FFFF00
#green1: #00FF00

#Secciones de las barras

# seccion_grande = SeccionICHA("[]350x150x37.8", color="#3A8431")#, debug=True)
# seccion_chica = SeccionICHA("[]80x40x8", color="#A3500B")


#Crear y agregar las barras
#########################

#Barras 4 mts tablero (eje Y)
P1 = Circular(200*mm_, 4*mm_, color="#0000FF")

ret.agregar_barra(Barra(0, 1, P1)) #0
ret.agregar_barra(Barra(2, 3, P1)) #1
ret.agregar_barra(Barra(4, 5, P1)) #2
ret.agregar_barra(Barra(6, 7, P1)) #3
ret.agregar_barra(Barra(8, 9, P1)) #4
ret.agregar_barra(Barra(10,11, P1)) #5
ret.agregar_barra(Barra(12, 13, P1)) #6
ret.agregar_barra(Barra(14, 15, P1)) #7
ret.agregar_barra(Barra(16, 17, P1)) #8
ret.agregar_barra(Barra(18, 19, P1)) #9
ret.agregar_barra(Barra(20, 21, P1)) #10
ret.agregar_barra(Barra(22, 23, P1)) #11
ret.agregar_barra(Barra(24, 25, P1)) #12
ret.agregar_barra(Barra(26, 27, P1)) #13
ret.agregar_barra(Barra(28, 29, P1)) #14
ret.agregar_barra(Barra(30, 31, P1)) #15
ret.agregar_barra(Barra(32, 33, P1)) #16
ret.agregar_barra(Barra(34, 35, P1)) #17
ret.agregar_barra(Barra(36, 37, P1)) #18
ret.agregar_barra(Barra(38, 39, P1)) #19
ret.agregar_barra(Barra(40, 41, P1)) #20


#Barras 6 mts tablero (eje X)
P2 = Circular(466*mm_, 8*mm_, color="#FF3E96")

ret.agregar_barra(Barra(0, 2, P2)) #21
ret.agregar_barra(Barra(2, 4, P2)) #22
ret.agregar_barra(Barra(4, 6, P2)) #23
ret.agregar_barra(Barra(6, 8, P2)) #24
ret.agregar_barra(Barra(8, 10, P2)) #25
ret.agregar_barra(Barra(10,12, P2)) #26
ret.agregar_barra(Barra(12, 14, P2)) #27
ret.agregar_barra(Barra(14, 16, P2)) #28
ret.agregar_barra(Barra(16, 18, P2)) #29
ret.agregar_barra(Barra(18, 20, P2)) #30
ret.agregar_barra(Barra(20, 22, P2)) #31
ret.agregar_barra(Barra(22, 24, P2)) #32
ret.agregar_barra(Barra(24, 26, P2)) #33
ret.agregar_barra(Barra(26, 28, P2)) #34
ret.agregar_barra(Barra(28, 30, P2)) #35
ret.agregar_barra(Barra(30, 32, P2)) #36
ret.agregar_barra(Barra(32, 34, P2)) #37
ret.agregar_barra(Barra(34, 36, P2)) #38
ret.agregar_barra(Barra(36, 38, P2)) #39
ret.agregar_barra(Barra(38, 40, P2)) #40
ret.agregar_barra(Barra(1, 3, P2)) #41
ret.agregar_barra(Barra(3, 5, P2)) #42
ret.agregar_barra(Barra(5, 7, P2)) #43
ret.agregar_barra(Barra(7, 9, P2)) #44
ret.agregar_barra(Barra(9, 11, P2)) #45
ret.agregar_barra(Barra(11,13, P2)) #46
ret.agregar_barra(Barra(13, 15, P2)) #47
ret.agregar_barra(Barra(15, 17, P2)) #48
ret.agregar_barra(Barra(17, 19, P2)) #49
ret.agregar_barra(Barra(19, 21, P2)) #50
ret.agregar_barra(Barra(21, 23, P2)) #51
ret.agregar_barra(Barra(23, 25, P2)) #52
ret.agregar_barra(Barra(25, 27, P2)) #53
ret.agregar_barra(Barra(27, 29, P2)) #54
ret.agregar_barra(Barra(29, 31, P2)) #55
ret.agregar_barra(Barra(31, 33, P2)) #56
ret.agregar_barra(Barra(33, 35, P2)) #57
ret.agregar_barra(Barra(35, 37, P2)) #58
ret.agregar_barra(Barra(37, 39, P2)) #59
ret.agregar_barra(Barra(39, 41, P2)) #60

#Barras aristas laterales piramide
P3 = Circular(466*mm_, 8*mm_, color="#00F5FF")

ret.agregar_barra(Barra(62, 0, P3)) #61
ret.agregar_barra(Barra(62, 1, P3)) #62
ret.agregar_barra(Barra(62, 2, P3)) #63
ret.agregar_barra(Barra(62, 3, P3)) #64
ret.agregar_barra(Barra(63, 2, P3)) #65
ret.agregar_barra(Barra(63, 3, P3)) #66
ret.agregar_barra(Barra(63, 4, P3)) #67
ret.agregar_barra(Barra(63, 5, P3)) #68
ret.agregar_barra(Barra(64, 4, P3)) #69
ret.agregar_barra(Barra(64, 5, P3)) #70
ret.agregar_barra(Barra(64, 6, P3)) #71
ret.agregar_barra(Barra(64, 7, P3)) #72
ret.agregar_barra(Barra(65, 6, P3)) #73
ret.agregar_barra(Barra(65, 7, P3)) #74
ret.agregar_barra(Barra(65, 8, P3)) #75
ret.agregar_barra(Barra(65, 9, P3)) #76
ret.agregar_barra(Barra(66, 8, P3)) #77
ret.agregar_barra(Barra(66, 9, P3)) #78
ret.agregar_barra(Barra(66, 10, P3)) #79
ret.agregar_barra(Barra(66, 11, P3)) #80
ret.agregar_barra(Barra(67, 10, P3)) #81
ret.agregar_barra(Barra(67, 11, P3)) #82
ret.agregar_barra(Barra(67, 12, P3)) #83
ret.agregar_barra(Barra(67, 13, P3)) #84
ret.agregar_barra(Barra(68, 12, P3)) #85
ret.agregar_barra(Barra(68, 13, P3)) #86
ret.agregar_barra(Barra(68, 14, P3)) #87
ret.agregar_barra(Barra(68, 15, P3)) #88
ret.agregar_barra(Barra(69, 14, P3)) #89
ret.agregar_barra(Barra(69, 15, P3)) #90
ret.agregar_barra(Barra(69, 16, P3)) #91
ret.agregar_barra(Barra(69, 17, P3)) #92
ret.agregar_barra(Barra(70, 16, P3)) #93
ret.agregar_barra(Barra(70, 17, P3)) #94
ret.agregar_barra(Barra(70, 18, P3)) #95
ret.agregar_barra(Barra(70, 19, P3)) #96
ret.agregar_barra(Barra(71, 18, P3)) #97
ret.agregar_barra(Barra(71, 19, P3)) #98
ret.agregar_barra(Barra(71, 20, P3)) #99
ret.agregar_barra(Barra(71, 21, P3)) #100
ret.agregar_barra(Barra(72, 20, P3)) #101
ret.agregar_barra(Barra(72, 21, P3)) #102
ret.agregar_barra(Barra(72, 22, P3)) #103
ret.agregar_barra(Barra(72, 23, P3)) #104
ret.agregar_barra(Barra(73, 22, P3)) #105
ret.agregar_barra(Barra(73, 23, P3)) #106
ret.agregar_barra(Barra(73, 24, P3)) #107
ret.agregar_barra(Barra(73, 25, P3)) #108
ret.agregar_barra(Barra(74, 24, P3)) #109
ret.agregar_barra(Barra(74, 25, P3)) #110
ret.agregar_barra(Barra(74, 26, P3)) #111
ret.agregar_barra(Barra(74, 27, P3)) #112
ret.agregar_barra(Barra(75, 26, P3)) #113
ret.agregar_barra(Barra(75, 27, P3)) #114
ret.agregar_barra(Barra(75, 28, P3)) #115
ret.agregar_barra(Barra(75, 29, P3)) #116
ret.agregar_barra(Barra(76, 28, P3)) #117
ret.agregar_barra(Barra(76, 29, P3)) #118
ret.agregar_barra(Barra(76, 30, P3)) #119
ret.agregar_barra(Barra(76, 31, P3)) #120
ret.agregar_barra(Barra(77, 30, P3)) #121
ret.agregar_barra(Barra(77, 31, P3)) #122
ret.agregar_barra(Barra(77, 32, P3)) #123
ret.agregar_barra(Barra(77, 33, P3)) #124
ret.agregar_barra(Barra(78, 32, P3)) #125
ret.agregar_barra(Barra(78, 33, P3)) #126
ret.agregar_barra(Barra(78, 34, P3)) #127
ret.agregar_barra(Barra(78, 35, P3)) #128
ret.agregar_barra(Barra(79, 34, P3)) #129
ret.agregar_barra(Barra(79, 35, P3)) #130
ret.agregar_barra(Barra(79, 36, P3)) #131
ret.agregar_barra(Barra(79, 37, P3)) #132
ret.agregar_barra(Barra(80, 36, P3)) #133
ret.agregar_barra(Barra(80, 37, P3)) #134
ret.agregar_barra(Barra(80, 38, P3)) #135
ret.agregar_barra(Barra(80, 39, P3)) #136
ret.agregar_barra(Barra(81, 38, P3)) #137
ret.agregar_barra(Barra(81, 39, P3)) #138
ret.agregar_barra(Barra(81, 40, P3)) #139
ret.agregar_barra(Barra(81, 41, P3)) #140

#Barras diagonales tablero
P4 = Circular(210*mm_, 5*mm_, color="#00FF00")

ret.agregar_barra(Barra(42, 0, P4)) #141
ret.agregar_barra(Barra(42, 1, P4)) #142
ret.agregar_barra(Barra(42, 2, P4)) #143
ret.agregar_barra(Barra(42, 3, P4)) #144
ret.agregar_barra(Barra(43, 2, P4)) #145
ret.agregar_barra(Barra(43, 3, P4)) #146
ret.agregar_barra(Barra(43, 4, P4)) #147
ret.agregar_barra(Barra(43, 5, P4)) #148
ret.agregar_barra(Barra(44, 4, P4)) #149
ret.agregar_barra(Barra(44, 5, P4)) #150
ret.agregar_barra(Barra(44, 6, P4)) #151
ret.agregar_barra(Barra(44, 7, P4)) #152
ret.agregar_barra(Barra(45, 6, P4)) #153
ret.agregar_barra(Barra(45, 7, P4)) #154
ret.agregar_barra(Barra(45, 8, P4)) #155
ret.agregar_barra(Barra(45, 9, P4)) #156
ret.agregar_barra(Barra(46, 8, P4)) #157
ret.agregar_barra(Barra(46, 9, P4)) #158
ret.agregar_barra(Barra(46, 10, P4)) #159
ret.agregar_barra(Barra(46, 11, P4)) #160
ret.agregar_barra(Barra(47, 10, P4)) #161
ret.agregar_barra(Barra(47, 11, P4)) #162
ret.agregar_barra(Barra(47, 12, P4)) #163
ret.agregar_barra(Barra(47, 13, P4)) #164
ret.agregar_barra(Barra(48, 12, P4)) #165
ret.agregar_barra(Barra(48, 13, P4)) #166
ret.agregar_barra(Barra(48, 14, P4)) #167
ret.agregar_barra(Barra(48, 15, P4)) #168
ret.agregar_barra(Barra(49, 14, P4)) #169
ret.agregar_barra(Barra(49, 15, P4)) #170
ret.agregar_barra(Barra(49, 16, P4)) #171
ret.agregar_barra(Barra(49, 17, P4)) #172
ret.agregar_barra(Barra(50, 16, P4)) #173
ret.agregar_barra(Barra(50, 17, P4)) #174
ret.agregar_barra(Barra(50, 18, P4)) #175
ret.agregar_barra(Barra(50, 19, P4)) #176
ret.agregar_barra(Barra(51, 18, P4)) #177
ret.agregar_barra(Barra(51, 19, P4)) #178
ret.agregar_barra(Barra(51, 20, P4)) #179
ret.agregar_barra(Barra(51, 21, P4)) #180
ret.agregar_barra(Barra(52, 20, P4)) #181
ret.agregar_barra(Barra(52, 21, P4)) #182
ret.agregar_barra(Barra(52, 22, P4)) #183
ret.agregar_barra(Barra(52, 23, P4)) #184
ret.agregar_barra(Barra(53, 22, P4)) #185
ret.agregar_barra(Barra(53, 23, P4)) #186
ret.agregar_barra(Barra(53, 24, P4)) #187
ret.agregar_barra(Barra(53, 25, P4)) #188
ret.agregar_barra(Barra(54, 24, P4)) #189
ret.agregar_barra(Barra(54, 25, P4)) #190
ret.agregar_barra(Barra(54, 26, P4)) #191
ret.agregar_barra(Barra(54, 27, P4)) #192
ret.agregar_barra(Barra(55, 26, P4)) #193
ret.agregar_barra(Barra(55, 27, P4)) #194
ret.agregar_barra(Barra(55, 28, P4)) #195
ret.agregar_barra(Barra(55, 29, P4)) #196
ret.agregar_barra(Barra(56, 28, P4)) #197
ret.agregar_barra(Barra(56, 29, P4)) #198
ret.agregar_barra(Barra(56, 30, P4)) #199
ret.agregar_barra(Barra(56, 31, P4)) #200
ret.agregar_barra(Barra(57, 30, P4)) #201
ret.agregar_barra(Barra(57, 31, P4)) #202
ret.agregar_barra(Barra(57, 32, P4)) #203
ret.agregar_barra(Barra(57, 33, P4)) #204
ret.agregar_barra(Barra(58, 32, P4)) #205
ret.agregar_barra(Barra(58, 33, P4)) #206
ret.agregar_barra(Barra(58, 34, P4)) #207
ret.agregar_barra(Barra(58, 35, P4)) #208
ret.agregar_barra(Barra(59, 34, P4)) #209
ret.agregar_barra(Barra(59, 35, P4)) #210
ret.agregar_barra(Barra(59, 36, P4)) #211
ret.agregar_barra(Barra(59, 37, P4)) #212
ret.agregar_barra(Barra(60, 36, P4)) #213
ret.agregar_barra(Barra(60, 37, P4)) #214
ret.agregar_barra(Barra(60, 38, P4)) #215
ret.agregar_barra(Barra(60, 39, P4)) #216
ret.agregar_barra(Barra(61, 38, P4)) #217
ret.agregar_barra(Barra(61, 39, P4)) #218
ret.agregar_barra(Barra(61, 40, P4)) #219
ret.agregar_barra(Barra(61, 41, P4)) #220

#barras superiores horizontales
P5 = Circular(466*mm_, 8*mm_, color="#0000FF")

ret.agregar_barra(Barra(62, 63, P5)) #221
ret.agregar_barra(Barra(63, 64, P5)) #222
ret.agregar_barra(Barra(64, 65, P5)) #223
ret.agregar_barra(Barra(65, 66, P5)) #224
ret.agregar_barra(Barra(66, 67, P5)) #221
ret.agregar_barra(Barra(67, 68, P5)) #222
ret.agregar_barra(Barra(68, 69, P5)) #223
ret.agregar_barra(Barra(69, 70, P5)) #224
ret.agregar_barra(Barra(70, 71, P5)) #225
ret.agregar_barra(Barra(71, 72, P5)) #226
ret.agregar_barra(Barra(72, 73, P5)) #227
ret.agregar_barra(Barra(73, 74, P5)) #228
ret.agregar_barra(Barra(74, 75, P5)) #229
ret.agregar_barra(Barra(74, 76, P5)) #230
ret.agregar_barra(Barra(76, 77, P5)) #231
ret.agregar_barra(Barra(77, 78, P5)) #232
ret.agregar_barra(Barra(78, 79, P5)) #232
ret.agregar_barra(Barra(79, 80, P5)) #233
ret.agregar_barra(Barra(80, 81, P5)) #234

#Barras que llegan al nodo 28 de apoyo
P6 = Circular(466*mm_, 8*mm_, color="#FFFF00")

ret.agregar_barra(Barra(81, 117, P6)) #234
ret.agregar_barra(Barra(81, 110, P6)) #235
ret.agregar_barra(Barra(110, 61, P6)) #236
ret.agregar_barra(Barra(117, 61, P6)) #237

#Barras verticales Torre
P7 = Circular(466*mm_, 8*mm_, color="#4B0082")

ret.agregar_barra(Barra(18, 118, P7)) #238
ret.agregar_barra(Barra(19, 119, P7)) #239
ret.agregar_barra(Barra(20, 120, P7)) #240
ret.agregar_barra(Barra(21, 121, P7)) #241
ret.agregar_barra(Barra(118, 122, P7)) #242
ret.agregar_barra(Barra(119, 123, P7)) #243
ret.agregar_barra(Barra(120, 124, P7)) #244
ret.agregar_barra(Barra(121, 125, P7)) #245
ret.agregar_barra(Barra(118, 122, P7)) #242
ret.agregar_barra(Barra(119, 123, P7)) #243
ret.agregar_barra(Barra(120, 124, P7)) #244
ret.agregar_barra(Barra(121, 125, P7)) #245
ret.agregar_barra(Barra(122, 126, P7)) #246
ret.agregar_barra(Barra(123, 127, P7)) #247
ret.agregar_barra(Barra(124, 128, P7)) #248
ret.agregar_barra(Barra(125, 129, P7)) #249

#Barras horizontales Torre
P8 = Circular(466*mm_, 8*mm_, color="#4B0082")

ret.agregar_barra(Barra(118, 119, P8)) #250
ret.agregar_barra(Barra(120, 121, P8)) #251
ret.agregar_barra(Barra(118, 120, P8)) #252
ret.agregar_barra(Barra(119, 121, P8)) #253
ret.agregar_barra(Barra(122, 123, P8)) #254
ret.agregar_barra(Barra(124, 125, P8)) #255
ret.agregar_barra(Barra(122, 124, P8)) #256
ret.agregar_barra(Barra(123, 125, P8)) #257
ret.agregar_barra(Barra(126, 127, P8)) #258
ret.agregar_barra(Barra(128, 129, P8)) #259
ret.agregar_barra(Barra(126, 130, P8)) #260
ret.agregar_barra(Barra(130, 128, P8)) #261
ret.agregar_barra(Barra(127, 100, P8)) #262
ret.agregar_barra(Barra(100, 129, P8)) #263

#Arriostramiento torre
P9 = Circular(466*mm_, 8*mm_, color="#4B0082")

ret.agregar_barra(Barra(131, 118, P9)) #264
ret.agregar_barra(Barra(131, 18, P9)) #265
ret.agregar_barra(Barra(131, 20, P9)) #266
ret.agregar_barra(Barra(131, 120, P9)) #267
ret.agregar_barra(Barra(132, 119, P9)) #268
ret.agregar_barra(Barra(132, 19, P9)) #269
ret.agregar_barra(Barra(132, 21, P9)) #270
ret.agregar_barra(Barra(132, 121, P9)) #271
ret.agregar_barra(Barra(133, 120, P9)) #272
ret.agregar_barra(Barra(133, 20, P9)) #273
ret.agregar_barra(Barra(133, 21, P9)) #274
ret.agregar_barra(Barra(133, 121, P9)) #275
ret.agregar_barra(Barra(134, 18, P9)) #276
ret.agregar_barra(Barra(134, 19, P9)) #277
ret.agregar_barra(Barra(134, 118, P9)) #278
ret.agregar_barra(Barra(134, 119, P9)) #279
ret.agregar_barra(Barra(135, 118, P9)) #280
ret.agregar_barra(Barra(135, 120, P9)) #281
ret.agregar_barra(Barra(135, 122, P9)) #282
ret.agregar_barra(Barra(135, 124, P9)) #283
ret.agregar_barra(Barra(136, 119, P9)) #284
ret.agregar_barra(Barra(136, 121, P9)) #285
ret.agregar_barra(Barra(136, 123, P9)) #286
ret.agregar_barra(Barra(136, 125, P9)) #287
ret.agregar_barra(Barra(137, 120, P9)) #288
ret.agregar_barra(Barra(137, 121, P9)) #289
ret.agregar_barra(Barra(137, 124, P9)) #290
ret.agregar_barra(Barra(137, 125, P9)) #291
ret.agregar_barra(Barra(138, 118, P9)) #292
ret.agregar_barra(Barra(138, 119, P9)) #293
ret.agregar_barra(Barra(138, 122, P9)) #294
ret.agregar_barra(Barra(138, 123, P9)) #295
ret.agregar_barra(Barra(139, 122, P9)) #296
ret.agregar_barra(Barra(139, 124, P9)) #297
ret.agregar_barra(Barra(139, 126, P9)) #298
ret.agregar_barra(Barra(139, 128, P9)) #299
ret.agregar_barra(Barra(140, 123, P9)) #300
ret.agregar_barra(Barra(140, 125, P9)) #301
ret.agregar_barra(Barra(140, 127, P9)) #302
ret.agregar_barra(Barra(140, 129, P9)) #303
ret.agregar_barra(Barra(141, 124, P9)) #304
ret.agregar_barra(Barra(141, 125, P9)) #305
ret.agregar_barra(Barra(141, 128, P9)) #306
ret.agregar_barra(Barra(141, 129, P9)) #307
ret.agregar_barra(Barra(142, 122, P9)) #308
ret.agregar_barra(Barra(142, 123, P9)) #309
ret.agregar_barra(Barra(142, 126, P9)) #310
ret.agregar_barra(Barra(142, 127, P9)) #311

#Riostras horizontales
ret.agregar_barra(Barra(143, 118, P9)) #312
ret.agregar_barra(Barra(143, 119, P9)) #313
ret.agregar_barra(Barra(143, 120, P9)) #314
ret.agregar_barra(Barra(143, 121, P9)) #315
ret.agregar_barra(Barra(144, 122, P9)) #316
ret.agregar_barra(Barra(144, 123, P9)) #317
ret.agregar_barra(Barra(144, 124, P9)) #318
ret.agregar_barra(Barra(144, 125, P9)) #319
ret.agregar_barra(Barra(145, 126, P9)) #320
ret.agregar_barra(Barra(145, 127, P9)) #321
ret.agregar_barra(Barra(145, 128, P9)) #322
ret.agregar_barra(Barra(145, 129, P9)) #323
ret.agregar_barra(Barra(145, 130, P9)) #324
ret.agregar_barra(Barra(145, 100, P9)) #325


#Crear restricciones
for nodo in [0,1]:
    ret.agregar_restriccion(nodo, 0, 0)
    ret.agregar_restriccion(nodo, 1, 0)
    ret.agregar_restriccion(nodo, 2, 0)

for nodo in [110,117]:
    ret.agregar_restriccion(nodo, 0, 0)
    ret.agregar_restriccion(nodo, 1, 0)
    ret.agregar_restriccion(nodo, 2, 0)

for nodo in [100,130,126,127,128,129,145]:
    ret.agregar_restriccion(nodo, 0, 0)
    ret.agregar_restriccion(nodo, 1, 0)
    ret.agregar_restriccion(nodo, 2, 0)





#Visualizar y comprobar las secciones
opciones_nodos = {
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
# import sys
# sys.exit()



#Resolver el problema peso_propio
ret.ensamblar_sistema(factor_peso_propio=[0.,0.,-1.], factor_cargas=0.0)
ret.resolver_sistema()
# f_D = ret.obtener_fuerzas()

###Problema de valores y vectores propios

import numpy.linalg as lin

Lamb, fi = lin.eigh(ret.Kff)

print (f"lambda = {Lamb}")

fi0 = np.zeros(ret.Nnodos*3)
fi0[ret.gdl_libres] = fi[:,0]

print(f"fi0 = {fi0}")



# import sys
# sys.exit()

#Agregar fuerzas tablero
#ret.agregar_fuerza(0, 2, -F/4)
#et.agregar_fuerza(5, 2, -F/4)
#ret.agregar_fuerza(2, 2, -F/4)
#ret.agregar_fuerza(7, 2, -F/4)
#ret.agregar_fuerza(1, 2, -F/2)
#ret.agregar_fuerza(6, 2, -F/2)

#Resolver el problema peso_propio
#ret.ensamblar_sistema(factor_peso_propio=[0.,0.,0], factor_cargas=1.0)
#ret.resolver_sistema()
#f_L = ret.obtener_fuerzas()



#Visualizar f_L en el reticulado
# opciones_nodos = {
# 	"usar_posicion_deformada": False,
# }

# opciones_barras = {
# 	"color_barras_por_dato": True,
# 	"ver_dato_en_barras" : True,
# 	"dato":f_L
# }

#ver_reticulado_3d(ret, 
#	opciones_nodos=opciones_nodos, 
#	opciones_barras=opciones_barras,
#	titulo="Carga Viva")


#Visualizar f_L en el reticulado
# opciones_nodos = {
# 	"usar_posicion_deformada": False,
# }

# opciones_barras = {
# 	"color_barras_por_dato": True,
# 	"ver_dato_en_barras" : True,
# 	"dato":f_D
# }

#ver_reticulado_3d(ret, 
#	opciones_nodos=opciones_nodos, 
#	opciones_barras=opciones_barras,
#	titulo="Carga Muerta")


#Calcular carga ultima (con factores de mayoracion)
#fu = 1.2*f_D + 1.6*f_L



#Visualizar combinacion en el reticulado
# opciones_nodos = {
# 	"usar_posicion_deformada": False,
# }

# opciones_barras = {
# 	"color_barras_por_dato": True,
# 	"ver_dato_en_barras" : True,
# 	"dato":fu
# }

# ver_reticulado_3d(ret, 
# 	opciones_nodos=opciones_nodos, 
# 	opciones_barras=opciones_barras,
# 	titulo="1.2D + 1.6L")





# cumple = ret.chequear_diseño(fu, ϕ=0.9)

# if cumple:
# 	print(":)  El reticulado cumple todos los requisitos")
# else:
# 	print(":(  El reticulado NO cumple todos los requisitos")

# #Calcular factor de utilizacion para las barras
# factores_de_utilizacion = ret.obtener_factores_de_utilizacion(fu, ϕ=0.9)


# #Visualizar FU en el reticulado
# # opciones_nodos = {
# # 	"usar_posicion_deformada": False,
# # 	# "factor_amplificacion_deformada": 1.,
# # }

# # opciones_barras = {
# # 	"color_barras_por_dato": True,
# # 	"ver_dato_en_barras" : True,
# # 	"dato":factores_de_utilizacion
# # }


# ver_reticulado_3d(ret, 
# 	opciones_nodos=opciones_nodos, 
# 	opciones_barras=opciones_barras,
# 	titulo="Factor Utilizacion")


# ret.guardar("05_ejemplo_chequear_diseño.h5")