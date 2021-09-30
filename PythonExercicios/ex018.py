import math
ang = float(input('Digite um ângulo em graus: '))
ang_rad = math.radians(ang)
print('Ângulo {}°\nSeno: {:.3f}\nCosseno: {:.3f}\nTangente: {:.3f}'.format(ang, math.sin(ang_rad), math.cos(ang_rad), math.tan(ang_rad)))