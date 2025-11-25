import math

PUNTOS = [
    (2, 3), (5, 4), (9, 6), (4, 7), (8, 1), (7, 2), (12, 5), (14, 3), (3, 10),
    (6, 8), (11, 11), (13, 9), (15, 6), (18, 2), (17, 7), (19, 4), (21, 3),
    (20, 8), (23, 5), (25, 7), (24, 1), (26, 4), (30, 2), (28, 9), (31, 7),
    (34, 6), (33, 3), (36, 8), (38, 5)
]

def distancia_sq(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

def fuerza_bruta_closest_pair(puntos):
    n = len(puntos)
    min_dist_sq = float('inf')
    p_min_1, p_min_2 = None, None
    for i in range(n):
        for j in range(i + 1, n):
            dist_sq = distancia_sq(puntos[i], puntos[j])
            if dist_sq < min_dist_sq:
                min_dist_sq = dist_sq
                p_min_1, p_min_2 = puntos[i], puntos[j]
    return min_dist_sq, p_min_1, p_min_2

def combinar_franja(franja_puntos, min_dist_sq):
    p_min_1, p_min_2 = None, None
    franja_puntos.sort(key=lambda p: p[1]) 
    for i in range(len(franja_puntos)):
        for j in range(i + 1, min(i + 7, len(franja_puntos))): 
            if (franja_puntos[j][1] - franja_puntos[i][1])**2 >= min_dist_sq:
                break
            dist_sq = distancia_sq(franja_puntos[i], franja_puntos[j])
            if dist_sq < min_dist_sq:
                min_dist_sq = dist_sq
                p_min_1, p_min_2 = franja_puntos[i], franja_puntos[j]
    return min_dist_sq, p_min_1, p_min_2

def closest_pair_recursive(puntos_x):
    n = len(puntos_x)
    if n <= 3:
        return fuerza_bruta_closest_pair(puntos_x)

    mitad = n // 2
    punto_medio = puntos_x[mitad] 
    
    dist_l_sq, p_l_1, p_l_2 = closest_pair_recursive(puntos_x[:mitad])
    dist_r_sq, p_r_1, p_r_2 = closest_pair_recursive(puntos_x[mitad:])

    if dist_l_sq < dist_r_sq:
        min_dist_sq, p_min_1, p_min_2 = dist_l_sq, p_l_1, p_l_2
    else:
        min_dist_sq, p_min_1, p_min_2 = dist_r_sq, p_r_1, p_r_2
    
    delta = math.sqrt(min_dist_sq)
    franja_puntos = [p for p in puntos_x if abs(p[0] - punto_medio[0]) < delta]
    
    dist_c_sq, p_c_1, p_c_2 = combinar_franja(franja_puntos, min_dist_sq)

    if dist_c_sq < min_dist_sq:
        return dist_c_sq, p_c_1, p_c_2
    else:
        return min_dist_sq, p_min_1, p_min_2


print("1. CÁLCULO DE DISTANCIA MÍNIMA CON FUERZA BRUTA (O(n^2))")
min_sq_brute, p_b_1, p_b_2 = fuerza_bruta_closest_pair(PUNTOS)
print(f"Pares más cercanos: {p_b_1} y {p_b_2}")
print(f"Distancia Mínima: {math.sqrt(min_sq_brute):.3f} (Raíz de {min_sq_brute})")

print("\n2. ALGORITMO DIVIDE Y VENCERÁS (O(n log n)) ")
puntos_ordenados_x = sorted(PUNTOS, key=lambda p: p[0])
min_sq_dv, p_dv_1, p_dv_2 = closest_pair_recursive(puntos_ordenados_x)
print("El código superior implementa la solución recursiva de Divide y Vencerás.")
print(f"Resultado D&V (Verificación): Pares {p_dv_1} y {p_dv_2}, Distancia: {math.sqrt(min_sq_dv):.3f}")

print("\n--- 3. Y 4. COMPARACIÓN DE TIEMPOS Y EXPLICACIÓN ---")
print("Complejidad de Fuerza Bruta (O(n^2)): Lenta, compara todos los pares.")
print("Complejidad de Divide y Vencerás (O(n log n)): Rápida.")
print("La complejidad baja porque la fase de Combinación reduce la búsqueda en la franja de O(n^2) a O(n) al solo comparar cada punto con un número constante (máx. 7) de vecinos, lo que resulta en un tiempo total de O(n log n).")