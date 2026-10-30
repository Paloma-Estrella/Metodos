'''
s = 24
f = 3500
v = 2
X = 100

def Ganancia (s,f,v,X):
	Resultado_Ganancia = ((s*X)-(f+(v*X)))
	return Resultado_Ganancia

def Punto_Equilibrio (s,f,v):
	Resultado_PEquilibrio = (f/(s-v))
	return Resultado_PEquilibrio

ganancia_calculada = Ganancia(s, f, v, X)
pe_calculado = Punto_Equilibrio(s, f, v)

print(f"Resultado de Ganancia: ${ganancia_calculada}")
print(f"Resultado de Punto de Equilibrio: ${pe_calculado}")
'''
def Ganancia(s: float, f: float, v: float, X: float):
    Resultado_Ganancia = ((s * X) - (f + (v * X)))
    return Resultado_Ganancia

def Punto_Equilibrio(s: float, f: float, v: float):
    Resultado_PEquilibrio = (f / (s - v))
    return Resultado_PEquilibrio
