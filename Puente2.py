from reticulado import Reticulado
from barra import Barra
from graficar3d import ver_reticulado_3d
from constantes import *
from math import sqrt
from secciones import Circular

import numpy as np
#Inicializar modelo



def Puente():
    ret = Reticulado()
    
    L = 6.*m_
    H = sqrt(23)*m_
    B = -4.*m_

    x = 5.075777986710320100e+00 
    z = 4.281724747887941618e+01
    
    #Nodos

    #Tablero
    #                x , y , z
    ret.agregar_nodo(0*L+x,B,z)        # Nodo 0  (punto 7)
    ret.agregar_nodo(0*L+x,0,z)        # Nodo 1
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
    ret.agregar_nodo(6.256338958148909768e+01,0,2.488153583002742408e+01)        # Nodo 100
    ret.agregar_nodo(6.804476221508502931e+01,0,2.363405959703677794e+01)        # Nodo 101
    ret.agregar_nodo(7.403904003641143561e+01,0,2.417869370676238816e+01)        # Nodo 102
    ret.agregar_nodo(7.939304016773286321e+01,0,2.613017923446748370e+01)        # Nodo 103
    ret.agregar_nodo(8.338472827472728000e+01,0,2.754290694540905093e+01)        # Nodo 104
    ret.agregar_nodo(8.840793693585601432e+01,0,2.914731579191635191e+01)        # Nodo 105
    ret.agregar_nodo(9.359720524280722032e+01,0,3.134224945968302478e+01)        # Nodo 106
    ret.agregar_nodo(1.001543482170419139e+02,0,3.516724734227227600e+01)        # Nodo 107
    ret.agregar_nodo(1.078043483536490612e+02,0,3.899224741057584254e+01)        # Nodo 108
    ret.agregar_nodo(1.170936342338148819e+02,0,4.008510457294829621e+01)        # Nodo 109
    ret.agregar_nodo(1.225579200456771218e+02,0,4.281724747887941618e+01)        # Nodo 110
    ret.agregar_nodo(1.252900629516082489e+02,0,4.281724747887941618e+01)        # Nodo 111
    ret.agregar_nodo(1.280222058575393760e+02,0,4.281724747887941618e+01)        # Nodo 112
    ret.agregar_nodo(1.307543487634704888e+02,0,4.281724747887941618e+01)        # Nodo 113
    ret.agregar_nodo(1.334864916694016301e+02,0,4.281724747887941618e+01)        # Nodo 114
    ret.agregar_nodo(1.362186345753327430e+02,0,4.281724747887941618e+01)        # Nodo 115
    ret.agregar_nodo(1.389507774812638559e+02,0,4.281724747887941618e+01)        # Nodo 116
    
    
    

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
    
    #barras verticales (diagonales)
    
    ret.agregar_barra(Barra(62, 0, circular_200_4)) #61
    ret.agregar_barra(Barra(62, 1, circular_200_4)) #62
    ret.agregar_barra(Barra(62, 2, circular_200_4)) #63
    ret.agregar_barra(Barra(62, 3, circular_200_4)) #64
    
    ret.agregar_barra(Barra(63, 2, circular_200_4)) #65
    ret.agregar_barra(Barra(63, 3, circular_200_4)) #66
    ret.agregar_barra(Barra(63, 4, circular_200_4)) #67
    ret.agregar_barra(Barra(63, 5, circular_200_4)) #68

    ret.agregar_barra(Barra(64, 4, circular_200_4)) #69
    ret.agregar_barra(Barra(64, 5, circular_200_4)) #70
    ret.agregar_barra(Barra(64, 6, circular_200_4)) #71
    ret.agregar_barra(Barra(64, 7, circular_200_4)) #72
    
    ret.agregar_barra(Barra(65, 6, circular_200_4)) #73
    ret.agregar_barra(Barra(65, 7, circular_200_4)) #74
    ret.agregar_barra(Barra(65, 8, circular_200_4)) #75
    ret.agregar_barra(Barra(65, 9, circular_200_4)) #76

    ret.agregar_barra(Barra(66, 8, circular_200_4)) #77
    ret.agregar_barra(Barra(66, 9, circular_200_4)) #78
    ret.agregar_barra(Barra(66, 10, circular_200_4)) #79
    ret.agregar_barra(Barra(66, 11, circular_200_4)) #80

    ret.agregar_barra(Barra(67, 10, circular_200_4)) #81
    ret.agregar_barra(Barra(67, 11, circular_200_4)) #82
    ret.agregar_barra(Barra(67, 12, circular_200_4)) #83
    ret.agregar_barra(Barra(67, 13, circular_200_4)) #84

    ret.agregar_barra(Barra(68, 12, circular_200_4)) #85
    ret.agregar_barra(Barra(68, 13, circular_200_4)) #86
    ret.agregar_barra(Barra(68, 14, circular_200_4)) #87
    ret.agregar_barra(Barra(68, 15, circular_200_4)) #88
    
    ret.agregar_barra(Barra(69, 14, circular_200_4)) #89
    ret.agregar_barra(Barra(69, 15, circular_200_4)) #90
    ret.agregar_barra(Barra(69, 16, circular_200_4)) #91
    ret.agregar_barra(Barra(69, 17, circular_200_4)) #92

    ret.agregar_barra(Barra(70, 16, circular_200_4)) #93
    ret.agregar_barra(Barra(70, 17, circular_200_4)) #94
    ret.agregar_barra(Barra(70, 18, circular_200_4)) #95
    ret.agregar_barra(Barra(70, 19, circular_200_4)) #96
    
    ret.agregar_barra(Barra(71, 18, circular_200_4)) #97
    ret.agregar_barra(Barra(71, 19, circular_200_4)) #98
    ret.agregar_barra(Barra(71, 20, circular_200_4)) #99
    ret.agregar_barra(Barra(71, 21, circular_200_4)) #100
    
    ret.agregar_barra(Barra(72, 20, circular_200_4)) #101
    ret.agregar_barra(Barra(72, 21, circular_200_4)) #102
    ret.agregar_barra(Barra(72, 22, circular_200_4)) #103
    ret.agregar_barra(Barra(72, 23, circular_200_4)) #104

    ret.agregar_barra(Barra(73, 22, circular_200_4)) #105
    ret.agregar_barra(Barra(73, 23, circular_200_4)) #106
    ret.agregar_barra(Barra(73, 24, circular_200_4)) #107
    ret.agregar_barra(Barra(73, 25, circular_200_4)) #108

    ret.agregar_barra(Barra(74, 24, circular_200_4)) #109
    ret.agregar_barra(Barra(74, 25, circular_200_4)) #110
    ret.agregar_barra(Barra(74, 26, circular_200_4)) #111
    ret.agregar_barra(Barra(74, 27, circular_200_4)) #112

    ret.agregar_barra(Barra(75, 26, circular_200_4)) #113
    ret.agregar_barra(Barra(75, 27, circular_200_4)) #114
    ret.agregar_barra(Barra(75, 28, circular_200_4)) #115
    ret.agregar_barra(Barra(75, 29, circular_200_4)) #116

    ret.agregar_barra(Barra(76, 28, circular_200_4)) #117
    ret.agregar_barra(Barra(76, 29, circular_200_4)) #118
    ret.agregar_barra(Barra(76, 30, circular_200_4)) #119
    ret.agregar_barra(Barra(76, 31, circular_200_4)) #120

    ret.agregar_barra(Barra(77, 30, circular_200_4)) #121
    ret.agregar_barra(Barra(77, 31, circular_200_4)) #122
    ret.agregar_barra(Barra(77, 32, circular_200_4)) #123
    ret.agregar_barra(Barra(77, 33, circular_200_4)) #124

    ret.agregar_barra(Barra(78, 32, circular_200_4)) #125
    ret.agregar_barra(Barra(78, 33, circular_200_4)) #126
    ret.agregar_barra(Barra(78, 34, circular_200_4)) #127
    ret.agregar_barra(Barra(78, 35, circular_200_4)) #128

    ret.agregar_barra(Barra(79, 34, circular_200_4)) #129
    ret.agregar_barra(Barra(79, 35, circular_200_4)) #130
    ret.agregar_barra(Barra(79, 36, circular_200_4)) #131
    ret.agregar_barra(Barra(79, 37, circular_200_4)) #132

    ret.agregar_barra(Barra(80, 36, circular_200_4)) #133
    ret.agregar_barra(Barra(80, 37, circular_200_4)) #134
    ret.agregar_barra(Barra(80, 38, circular_200_4)) #135
    ret.agregar_barra(Barra(80, 39, circular_200_4)) #136

    ret.agregar_barra(Barra(81, 38, circular_200_4)) #137
    ret.agregar_barra(Barra(81, 39, circular_200_4)) #138
    ret.agregar_barra(Barra(81, 40, circular_200_4)) #139
    ret.agregar_barra(Barra(81, 41, circular_200_4)) #140

    #barras diagonales tablero
    
    ret.agregar_barra(Barra(42, 0, circular_200_4)) #141
    ret.agregar_barra(Barra(42, 1, circular_200_4)) #142
    ret.agregar_barra(Barra(42, 2, circular_200_4)) #143
    ret.agregar_barra(Barra(42, 3, circular_200_4)) #144
    
    ret.agregar_barra(Barra(43, 2, circular_200_4)) #145
    ret.agregar_barra(Barra(43, 3, circular_200_4)) #146
    ret.agregar_barra(Barra(43, 4, circular_200_4)) #147
    ret.agregar_barra(Barra(43, 5, circular_200_4)) #148

    ret.agregar_barra(Barra(44, 4, circular_200_4)) #149
    ret.agregar_barra(Barra(44, 5, circular_200_4)) #150
    ret.agregar_barra(Barra(44, 6, circular_200_4)) #151
    ret.agregar_barra(Barra(44, 7, circular_200_4)) #152
    
    ret.agregar_barra(Barra(45, 6, circular_200_4)) #153
    ret.agregar_barra(Barra(45, 7, circular_200_4)) #154
    ret.agregar_barra(Barra(45, 8, circular_200_4)) #155
    ret.agregar_barra(Barra(45, 9, circular_200_4)) #156

    ret.agregar_barra(Barra(46, 8, circular_200_4)) #157
    ret.agregar_barra(Barra(46, 9, circular_200_4)) #158
    ret.agregar_barra(Barra(46, 10, circular_200_4)) #159
    ret.agregar_barra(Barra(46, 11, circular_200_4)) #160

    ret.agregar_barra(Barra(47, 10, circular_200_4)) #161
    ret.agregar_barra(Barra(47, 11, circular_200_4)) #162
    ret.agregar_barra(Barra(47, 12, circular_200_4)) #163
    ret.agregar_barra(Barra(47, 13, circular_200_4)) #164

    ret.agregar_barra(Barra(48, 12, circular_200_4)) #165
    ret.agregar_barra(Barra(48, 13, circular_200_4)) #166
    ret.agregar_barra(Barra(48, 14, circular_200_4)) #167
    ret.agregar_barra(Barra(48, 15, circular_200_4)) #168
    
    ret.agregar_barra(Barra(49, 14, circular_200_4)) #169
    ret.agregar_barra(Barra(49, 15, circular_200_4)) #170
    ret.agregar_barra(Barra(49, 16, circular_200_4)) #171
    ret.agregar_barra(Barra(49, 17, circular_200_4)) #172

    ret.agregar_barra(Barra(50, 16, circular_200_4)) #173
    ret.agregar_barra(Barra(50, 17, circular_200_4)) #174
    ret.agregar_barra(Barra(50, 18, circular_200_4)) #175
    ret.agregar_barra(Barra(50, 19, circular_200_4)) #176
    
    ret.agregar_barra(Barra(51, 18, circular_200_4)) #177
    ret.agregar_barra(Barra(51, 19, circular_200_4)) #178
    ret.agregar_barra(Barra(51, 20, circular_200_4)) #179
    ret.agregar_barra(Barra(51, 21, circular_200_4)) #180
    
    ret.agregar_barra(Barra(52, 20, circular_200_4)) #181
    ret.agregar_barra(Barra(52, 21, circular_200_4)) #182
    ret.agregar_barra(Barra(52, 22, circular_200_4)) #183
    ret.agregar_barra(Barra(52, 23, circular_200_4)) #184

    ret.agregar_barra(Barra(53, 22, circular_200_4)) #185
    ret.agregar_barra(Barra(53, 23, circular_200_4)) #186
    ret.agregar_barra(Barra(53, 24, circular_200_4)) #187
    ret.agregar_barra(Barra(53, 25, circular_200_4)) #188
    
    ret.agregar_barra(Barra(54, 24, circular_200_4)) #189
    ret.agregar_barra(Barra(54, 25, circular_200_4)) #190
    ret.agregar_barra(Barra(54, 26, circular_200_4)) #191
    ret.agregar_barra(Barra(54, 27, circular_200_4)) #192

    ret.agregar_barra(Barra(55, 26, circular_200_4)) #193
    ret.agregar_barra(Barra(55, 27, circular_200_4)) #194
    ret.agregar_barra(Barra(55, 28, circular_200_4)) #195
    ret.agregar_barra(Barra(55, 29, circular_200_4)) #196

    ret.agregar_barra(Barra(56, 28, circular_200_4)) #197
    ret.agregar_barra(Barra(56, 29, circular_200_4)) #198
    ret.agregar_barra(Barra(56, 30, circular_200_4)) #199
    ret.agregar_barra(Barra(56, 31, circular_200_4)) #200

    ret.agregar_barra(Barra(57, 30, circular_200_4)) #201
    ret.agregar_barra(Barra(57, 31, circular_200_4)) #202
    ret.agregar_barra(Barra(57, 32, circular_200_4)) #203
    ret.agregar_barra(Barra(57, 33, circular_200_4)) #204

    ret.agregar_barra(Barra(58, 32, circular_200_4)) #205
    ret.agregar_barra(Barra(58, 33, circular_200_4)) #206
    ret.agregar_barra(Barra(58, 34, circular_200_4)) #207
    ret.agregar_barra(Barra(58, 35, circular_200_4)) #208

    ret.agregar_barra(Barra(59, 34, circular_200_4)) #209
    ret.agregar_barra(Barra(59, 35, circular_200_4)) #210
    ret.agregar_barra(Barra(59, 36, circular_200_4)) #211
    ret.agregar_barra(Barra(59, 37, circular_200_4)) #212

    ret.agregar_barra(Barra(60, 36, circular_200_4)) #213
    ret.agregar_barra(Barra(60, 37, circular_200_4)) #214
    ret.agregar_barra(Barra(60, 38, circular_200_4)) #215
    ret.agregar_barra(Barra(60, 39, circular_200_4)) #216

    ret.agregar_barra(Barra(61, 38, circular_200_4)) #217
    ret.agregar_barra(Barra(61, 39, circular_200_4)) #218
    ret.agregar_barra(Barra(61, 40, circular_200_4)) #219
    ret.agregar_barra(Barra(61, 41, circular_200_4)) #220
    
    #barras superiores horizontales
    
    ret.agregar_barra(Barra(62, 63, circular_200_4)) #221
    ret.agregar_barra(Barra(63, 64, circular_200_4)) #222
    ret.agregar_barra(Barra(64, 65, circular_200_4)) #223
    ret.agregar_barra(Barra(65, 66, circular_200_4)) #224
    ret.agregar_barra(Barra(66, 67, circular_200_4)) #221
    ret.agregar_barra(Barra(67, 68, circular_200_4)) #222
    ret.agregar_barra(Barra(68, 69, circular_200_4)) #223
    ret.agregar_barra(Barra(69, 70, circular_200_4)) #224
    ret.agregar_barra(Barra(70, 71, circular_200_4)) #225
    ret.agregar_barra(Barra(71, 72, circular_200_4)) #226
    ret.agregar_barra(Barra(72, 73, circular_200_4)) #227
    ret.agregar_barra(Barra(73, 74, circular_200_4)) #228
    ret.agregar_barra(Barra(74, 75, circular_200_4)) #229
    ret.agregar_barra(Barra(74, 76, circular_200_4)) #230
    ret.agregar_barra(Barra(76, 77, circular_200_4)) #231
    ret.agregar_barra(Barra(77, 78, circular_200_4)) #232
    ret.agregar_barra(Barra(78, 79, circular_200_4)) #232
    ret.agregar_barra(Barra(79, 80, circular_200_4)) #233
    ret.agregar_barra(Barra(80, 81, circular_200_4)) #234
    
    





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


