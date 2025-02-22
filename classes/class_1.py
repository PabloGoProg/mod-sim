import numpy as np

V1, V2 = 5, 10
R1, R2, R3, R4, R5 = 2, 5, 7, 2, 10

coeficients_matrix = np.array([
  [R1 + R4, -R4, 0],
  [-R4, R2 + R4 + R5, R5],
  [0, R5, R3 + R5]
])

values = np.array([V1, 0, V2])
currents = abs(np.linalg.solve(coeficients_matrix, values))

resistor_currents = np.array([
  currents[0],
  currents[1],
  currents[2],
  currents[0] - currents[1],
  currents[2] - currents[1],
])

resistor_voltages = resistor_currents * np.array([R1, R2, R3, R4, R5])
potentials = resistor_voltages * resistor_currents

for idx, current in enumerate(currents):
  print(f'Current I{idx + 1}: {current} A')
print('')
  
for idx, current in enumerate(resistor_currents):
  print(f'Resistor I{idx + 1}: {current} A')
print('')
  
for idx, voltage in enumerate(resistor_voltages):
  print(f'Resistor V{idx + 1}: {voltage} V')
print('')
  
for idx, potential in enumerate(potentials):
  print(f'Potential P{idx + 1 }: {potential} W')
print('Total power: ', potentials.sum(), 'W')
