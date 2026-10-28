# Task 17: Ordinary Differential Equations – Euler Method

## 1. Objective
To estimate how the temperature of a hot object decreases over time using Euler's method.

## 2. Inputs
- Ambient temperature: 25°C
- Initial temperature: 90°C
- Cooling constant: 0.12 per minute
- Time step: 1 minute
- Total time: 30 minutes

## 3. Mathematical Operation
The program uses Newton's law of cooling:

dT/dt = -k(T - T_ambient)

Euler's method updates the temperature using:

T_new = T_old + h × cooling_rate(T_old)

The program also calculates the exact temperature so that the two results can be compared.

## 4. Output and Interpretation
After 30 minutes, Euler's method estimates the temperature as 26.40°C. The exact solution is approximately 26.78°C.

The final absolute error is approximately 0.3720°C. The object cools toward the ambient temperature of 25°C.

## 5. Input Modification
Change the time step from `h = 1.0` to `h = 0.5`.

The new Euler estimate after 30 minutes is approximately 26.59°C. The exact result remains approximately 26.78°C, and the error decreases to approximately 0.1890°C.

This shows that using a smaller time step improves the accuracy of Euler's method for this example.

## 6. Related Real-World Application
The program can estimate how quickly hot food, a heated machine, or another hot object cools.

Assumption: The ambient temperature and cooling constant remain constant during the 30-minute period.

## 7. Conclusion
Euler's method approximates the solution of a differential equation by taking small steps through time. Smaller steps generally improve accuracy but require more calculations.
