# Task 20: Random Numbers and Monte Carlo Methods

## 1. Objective
Estimate the probability that incoming demand exceeds a cloud server's capacity using random simulations.

## 2. Inputs
- Server capacity: 1000 demand units
- Mean demand: 850 units
- Standard deviation: 120 units
- Number of simulations: 100,000
- Random seed: 42

## 3. Mathematical operation
The program generates random demand values from a normal distribution. It checks whether each value exceeds the server capacity.

The estimated probability is:

Estimated probability = Number of overload cases / Total simulations

## 4. Output and interpretation
The estimated overload probability is 10.6160%. There are 10,616 simulated overload cases out of 100,000 simulations.

This estimates the risk of server demand exceeding its capacity under the assumed demand distribution.

The graph shows how the estimated probability changes as the number of simulations increases.

## 5. Modification of an input
I changed server capacity from 1000 to 900 demand units.

The estimated overload probability increases to approximately 33.5940%, or 33,594 overload cases out of 100,000 simulations.

This happens because a server with lower capacity is more likely to be overloaded.

## 6. Related real-world application
This program can help a cloud-service provider estimate overload risk and plan server capacity.

Assumptions:
- Demand follows a normal distribution.
- Mean demand and standard deviation remain constant.
- Each simulation represents a possible demand scenario.
- The model does not include changing demand patterns or automatic scaling.