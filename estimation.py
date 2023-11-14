# Done by Rafael Gil
# Nº Mec. 118377
# November 2023


import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Data from experimental analysis
num_vertices = np.array(list(range(4, 26)))
exhaustive_times = np.array([
    0.0001389, 0.0002294, 0.0002922, 0.00068979, 0.0015438, 0.0049507,
    0.0095575, 0.0229472, 0.0453573, 0.1089745, 0.2192243, 0.7063999,
    1.1780833, 2.5152729, 6.2236802, 12.5995052, 26.0108515, 56.2371403,
    120.9686704, 395.7680206, 855.8324934, 1366.1357973
])
greedy_times = np.array([
    0.0045344, 0.0081493, 0.0075021, 0.009448, 0.0097511, 0.0120359,
    0.0109243, 0.0134678, 0.0148012, 0.0153767, 0.0192595, 0.0276222,
    0.0295291, 0.0236615, 0.0450665, 0.0322919, 0.0360631, 0.0327581,
    0.0364963, 0.1048222, 0.0706066, 0.0385439
])

# We know that the exhaustive is exponential and that the greedy is polynomial, due to the formal analysis
def exponential_model(x, a, b):
    return a * np.exp(b * x)

def polynomial_model(x, a, b, c):
    return a * x**2 + b * x + c

# Fit the models to the data
exponential_params, _ = curve_fit(exponential_model, num_vertices, exhaustive_times)
polynomial_params, _ = curve_fit(polynomial_model, num_vertices, greedy_times)

# Predicted values using the fitted models
exponential_predicted = exponential_model(num_vertices, *exponential_params)
polynomial_predicted = polynomial_model(num_vertices, *polynomial_params)

# Plot
plt.figure(figsize=(10, 6))
plt.scatter(num_vertices, exhaustive_times, label='Exhaustive Data', marker='o')
plt.plot(num_vertices, exponential_predicted, label='Exponential Fit (Exhaustive)', linestyle='--')
plt.scatter(num_vertices, greedy_times, label='Greedy Data', marker='o')
plt.plot(num_vertices, polynomial_predicted, label='Polynomial Fit (Greedy)', linestyle='--')
plt.xlabel('Number of Vertices')
plt.ylabel('Execution Time (s)')
plt.title('Execution Time vs. Number of Vertices with Fitted Models')
plt.yscale('log')
plt.legend()
plt.grid(True)
plt.show()

# Do the extrapolation to predict 
# Size for the grasphs of the prediction 
larger_input_sizes = np.arange(26, 51)

exponential_predicted_larger = exponential_model(larger_input_sizes, *exponential_params)
polynomial_predicted_larger = polynomial_model(larger_input_sizes, *polynomial_params)

# Display the extrapolated values
print("Extrapolated Execution Times (Exponential Model):")
for size, time in zip(larger_input_sizes, exponential_predicted_larger):
    print(f"N. Vertex: {size}, Predicted Time: {time:.6f} seconds")

print("\nExtrapolated Execution Times (Polynomial Model):")
for size, time in zip(larger_input_sizes, polynomial_predicted_larger):
    print(f"N. Vertex: {size}, Predicted Time: {time:.6f} seconds")


# Get the formulas of the extrapolation
a_exp, b_exp = exponential_params

a_poly, b_poly, c_poly = polynomial_params

exponential_formula = f"Execution Time = {a_exp:.6f} * exp({b_exp:.6f} * N)"

polynomial_formula = f"Execution Time = {a_poly:.6f} * N^2 + {b_poly:.6f} * N + {c_poly:.6f}"

print("Exponential Formula: \n", exponential_formula)
print("Polynomial Formula: \n", polynomial_formula)
