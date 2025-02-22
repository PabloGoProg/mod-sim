import numpy as np
from matplotlib import pyplot as plt

# Monte Carlo simulation in systems with aleatory variables
itrs = 1000 # Number of iterations

'''
  Example 1: Equivalent resistance
  Having a numver of resistances with same tolerance each, calculate the equivalent resistance (suposing they are in parallel)
'''
def calculate_equivalent_resistance() -> None:
  '''
    Calculate the equivalent resistance of a number of resistors in parallel
  '''
  
  # Random resistances between min and max resistance values
  random_resistances = np.random.uniform(min_resistance, max_resistance, num_of_resistors)
  r_eq = 1 / np.sum(1 / random_resistances)
  return r_eq

# Constants (Values acording to resistances0)
num_of_resistors = 5
resistance_value = 1000
tolerance = 0.2

min_resistance = resistance_value - (resistance_value * tolerance)
max_resistance = resistance_value + (resistance_value * tolerance)

print(f'Minimum resistance: {min_resistance} Ohms')
print(f'Maximum resistance: {max_resistance} Ohms')


# Simulations (Equivalent resistances)
itrs = np.array([calculate_equivalent_resistance() for _ in range(itrs)])

mean_resistance = np.mean(itrs)
starndard_deviation = np.std(itrs)
print(f'Mean resistance: {mean_resistance} Ohms')
print(f'Standard deviation: {starndard_deviation} Ohms')

# -------------------------------------

'''
  Example 2: Voltage divider
  Calculate the output voltage of a voltage divider circuit with two resistances
'''

v0 = 5
tolerance = 0.2
resistances = [32, 18]

def calculate_voltage_divider(resistances: list, tolerance: float, init_voltage: int) -> float:
  '''
    Calculate the output voltage of a voltage divider circuit
    Args:
      resistances: list of resistances
      tolerance: tolerance of resistances
      init_voltage: initial voltage of the circuit
    Returns:
      v_out: output voltage of the circuit
  '''
  
  # Random resistances between min and max resistance values
  random_resistances = [np.random.uniform(r - r * tolerance, r + r * tolerance) 
                        for r in resistances]
  
  r1, r2 = random_resistances
  v_out = r2 / (r1 + r2) * init_voltage # Output voltage
  return v_out
  
v_values = [calculate_voltage_divider(resistances, tolerance, v0) for _ in range(itrs)]

mean_voltage = np.mean(v_values)
standard_deviation = np.std(v_values)
print(f'Mean voltage: {mean_voltage} V')
print(f'Standard deviation: {standard_deviation} V')

plt.hist(v_values, bins=50, alpha=0.75, color='blue', edgecolor='black')
plt.title('Voltage divider')
plt.xlabel('Voltage (V)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
  




