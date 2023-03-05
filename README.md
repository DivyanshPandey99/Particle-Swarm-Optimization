# Particle Swarm Optimization Simulation

This project is a simulation of the Particle Swarm Optimization algorithm, used to find the location of food. It is built using the Pygame library and involves particles with velocity, x and y positions.

## Installation

To run the simulation, you will need to install the Pygame library. You can do this using pip:

```
pip install pygame random
```

## How it Works

The Particle Swarm Optimization algorithm is a heuristic optimization technique used to solve complex optimization problems. In this simulation, the problem is to find the location of the food.

Each particle in the simulation represents a possible solution to the problem. The particles move around the screen with a velocity that is adjusted based on their own best solution so far, as well as the best solution of the entire swarm.

In this way, the particles explore the solution space, moving towards better and better solutions. Eventually, they should converge on the location of the food, at which point the simulation will end.

## Output

![](https://github.com/DivyanshPandey99/Particle-Swarm-Optimization/blob/master/output.png)

## References

[Particle swarm optimization algorithm: an overview - Wang, Tan and Liu](https://kpfu.ru/staff_files/F_1407356997/overview.pdf)
