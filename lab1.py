import numpy as np
from matplotlib import pyplot as plt

V1, V2 = 10, 0
r_expected = 1000
tolerance = 0.15

min_tolerance = r_expected - r_expected * tolerance
max_tolerance = r_expected + r_expected * tolerance

v_differences, middle_currents = [], []
while V1 >= 0 and V2 <= 10:
    v_differences.append(V1 - V2)
    
    resistances_with_tolerance = [np.random.uniform(min_tolerance, max_tolerance) for _ in range(5)]
    R1, R2, R3, R4, R5 = resistances_with_tolerance
    
    coeficients_matrix = np.array([
        [R1 + R4, -R4, 0],
        [-R4, R2 + R4 + R5, R5],
        [0, R5, R3 + R5]
    ])
    
    values = np.array([V1, 0, V2])
    currents = np.linalg.solve(coeficients_matrix, values)
    
    middle_currents.append(currents[1])
    
    V1 -= 0.1
    V2 += 0.1

# Convertir a arrays para manejo vectorizado
v_differences = np.array(v_differences)
middle_currents = np.array(middle_currents)

# Graficar positivos y negativos con diferentes colores
plt.figure(figsize=(8, 6))
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)  # Línea horizontal en y=0

# Filtrar valores positivos y negativos
pos_mask = middle_currents >= 0
neg_mask = middle_currents < 0

plt.plot(v_differences[pos_mask], middle_currents[pos_mask], color='blue', label='Current ≥ 0')
plt.plot(v_differences[neg_mask], middle_currents[neg_mask], color='red', label='Current < 0')

# Etiquetas y título
plt.xlabel('Voltage Difference (V)')
plt.ylabel('Middle Current (A)')
plt.title('Middle Current vs Voltage Difference')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

plt.show()
