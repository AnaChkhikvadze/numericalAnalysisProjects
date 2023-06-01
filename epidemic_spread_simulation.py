import numpy as np
import matplotlib.pyplot as plt

# Parameters
beta = 0.002  # Infection rate
gamma = 0.009  # Recovery rate
days = 100
dt = 1

# Initial conditions
S = [0] * (days + 1)
I = [0] * (days + 1)
R = [0] * (days + 1)
S[0] = 50
I[0] = 1
R[0] = 0

# Derivative functions
def dS(S, I):
    return -beta * S * I

def dI(S, I):
    return beta * S * I - gamma * I

def dR(I):
    return gamma * I

# ODE solvers
def forwardEuler(S, I, R, dt, days):
    for t in range(days):
        S[t + 1] = S[t] + dt * dS(S[t], I[t])
        I[t + 1] = I[t] + dt * dI(S[t], I[t])
        R[t + 1] = R[t] + dt * dR(I[t])

def backwardEuler(S, I, R, dt, days):
    for t in range(1, days + 1):
        S[t] = S[t - 1] + dt * dS(S[t - 1], I[t - 1])
        I[t] = I[t - 1] + dt * dI(S[t - 1], I[t - 1])
        R[t] = R[t - 1] + dt * dR(I[t - 1])
        S[t] = S[t - 1] + dt * dS(S[t], I[t])
        I[t] = I[t - 1] + dt * dI(S[t], I[t])
        R[t] = R[t - 1] + dt * dR(I[t])

def CrankNicolson(S, I, R, dt, days):
    for t in range(1, days + 1):
        S[t] = S[t - 1] + dt * dS(S[t - 1], I[t - 1])
        I[t] = I[t - 1] + dt * dI(S[t - 1], I[t - 1])
        R[t] = R[t - 1] + dt * dR(I[t - 1])
        S[t] = S[t - 1] + (dt / 2) * (dS(S[t], I[t]) + dS(S[t - 1], I[t - 1]))
        I[t] = I[t - 1] + (dt / 2) * (dI(S[t], I[t]) + dI(S[t - 1], I[t - 1]))
        R[t] = R[t - 1] + (dt / 2) * (dR(I[t]) + dR(I[t - 1]))

def RK2(S, I, R, dt, days):
    for t in range(1, days + 1):
        Sk1 = dt * dS(S[t - 1], I[t - 1])
        Sk2 = dt * dS(S[t - 1] + Sk1, I[t - 1] + Sk1)
        S[t] = S[t - 1] + 0.5 * (Sk1 + Sk2)
        Ik1 = dt * dI(S[t - 1], I[t - 1])
        Ik2 = dt * dI(S[t - 1] + Ik1, I[t - 1] + Ik1)
        I[t] = I[t - 1] + 0.5 * (Ik1 + Ik2)
        Rk1 = dt * dR(I[t - 1])
        Rk2 = dt * dR(I[t - 1] + Rk1)
        R[t] = R[t - 1] + 0.5 * (Rk1 + Rk2)

def RK4(S, I, R, dt, days):
    for t in range(1, days + 1):
        Sk1 = dt * dS(S[t - 1], I[t - 1])
        Sk2 = dt * dS(S[t - 1] + 0.5 * Sk1, I[t - 1] + 0.5 * Sk1)
        Sk3 = dt * dS(S[t - 1] + 0.5 * Sk2, I[t - 1] + 0.5 * Sk2)
        Sk4 = dt * dS(S[t - 1] + Sk3, I[t - 1] + Sk3)
        S[t] = S[t - 1] + (1 / 6) * (Sk1 + 2 * Sk2 + 2 * Sk3 + Sk4)
        Ik1 = dt * dI(S[t - 1], I[t - 1])
        Ik2 = dt * dI(S[t - 1] + 0.5 * Ik1, I[t - 1] + 0.5 * Ik1)
        Ik3 = dt * dI(S[t - 1] + 0.5 * Ik2, I[t - 1] + 0.5 * Ik2)
        Ik4 = dt * dI(S[t - 1] + Ik3, I[t - 1] + Ik3)
        I[t] = I[t - 1] + (1 / 6) * (Ik1 + 2 * Ik2 + 2 * Ik3 + Ik4)
        Rk1 = dt * dR(I[t - 1])
        Rk2 = dt * dR(I[t - 1] + 0.5 * Rk1)
        Rk3 = dt * dR(I[t - 1] + 0.5 * Rk2)
        Rk4 = dt * dR(I[t - 1] + Rk3)
        R[t] = R[t - 1] + (1 / 6) * (Rk1 + 2 * Rk2 + 2 * Rk3 + Rk4)

# Solve using Crank-Nicolson method
CrankNicolson(S, I, R, dt, days)

# Visualize
t = np.linspace(0, days * dt, days + 1)
plt.plot(t, S, color="blue", label="Susceptible")
plt.plot(t, I, color="green", label="Infected")
plt.plot(t, R, color="red", label="Recovered")
plt.xlabel("Days")
plt.ylabel("Number of People")
plt.title("Epidemic Spread")
plt.legend()
plt.grid(True)
plt.show()
