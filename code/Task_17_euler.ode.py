
import numpy as np
import matplotlib.pyplot as plt

# Newton's law of cooling
# dT/dt = -k(T - T_ambient)

T_ambient = 25.0
T_initial = 90.0
k = 0.12

h = 0.5  # Time step in minutes
end_time = 30.0

def cooling_rate(T):
    return -k * (T - T_ambient)

# Create time values
time = np.arange(0, end_time + h, h)

# Store the temperature values
temperature = np.zeros_like(time)
temperature[0] = T_initial

# Apply Euler's method
for i in range(len(time) - 1):
    temperature[i + 1] = (
        temperature[i] + h * cooling_rate(temperature[i])
    )

# Calculate the exact solution for comparison
exact = T_ambient + (
    T_initial - T_ambient
) * np.exp(-k * time)

# Display results
print(f"Euler temperature after 30 min: {temperature[-1]:.2f} C")
print(f"Exact temperature after 30 min: {exact[-1]:.2f} C")
print(
    f"Final absolute error: "
    f"{abs(temperature[-1] - exact[-1]):.4f} C"
)

# Plot the results
plt.plot(time, temperature, marker="o", label="Euler")
plt.plot(time, exact, label="Exact solution")
plt.xlabel("Time (minutes)")
plt.ylabel("Temperature (C)")
plt.title("Cooling of a hot object")
plt.legend()
plt.grid(True)
plt.show()
