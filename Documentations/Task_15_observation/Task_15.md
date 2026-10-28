# Task 15: Numerical Differentiation

## 1. Objective
The aim is to estimate a vehicle's speed using GPS position measurements recorded at different times.

## 2. Inputs
The program uses time in seconds and vehicle position in metres.

## 3. Mathematical Operations
The program calculates speed using forward, central and backward differences. It divides the change in position by the change in time. Matplotlib displays the estimated speeds in a graph.

## 4. Original Output
The estimated speeds range from 4.80 m/s at 0 seconds to 8.00 m/s at 6 seconds.

## 5. Modified Input
I changed the position at 4 seconds from 22.7 metres to 24.0 metres.

## 6. Observation
Changing the position measurement affects the estimated speeds around 3, 4 and 5 seconds. The speed estimates at 0, 1, 2 and 6 seconds remain unchanged.

## 7. Interpretation
The graph shows that the vehicle's estimated speed generally increases over time. Numerical differentiation helps estimate speed when position measurements are available but a speed formula is not.

## 8. Related Real-World Problem
This method can be used by a GPS tracking system to estimate a vehicle's speed from recorded positions.

## 9. Assumptions
The time and position measurements are assumed to be accurate. The estimated speeds are approximations based on the available measurements.

## 10. New Input Data
The position at 4 seconds was increased from 22.7 metres to 24.0 metres.

## 11. Modified Output
The estimated speeds at 3, 4 and 5 seconds become 6.90 m/s, 6.95 m/s and 7.00 m/s respectively.

## 12. Interpretation of the Modified Problem
Changing one GPS position affects nearby speed estimates because the numerical method uses neighboring measurements. This shows why inaccurate GPS data can affect estimated vehicle speeds.
