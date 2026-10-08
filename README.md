# 3D Simple Harmonic Motion Simulator

A real-time 3D physics simulation and numerical integration model of a Spring-Mass Harmonic Oscillator built using Python and VPython. 

This project demonstrates the application of the **Euler-Cromer (Semi-Implicit Euler)** algorithm to model simple harmonic motion while conserving mechanical energy over long time steps and preventing numerical instability.

---

## 🔬 Physics & Mathematics

The system is governed by Hooke's Law and Newton's Second Law:

$$F = -k(x - x_0) = m \cdot a$$

$$a(x) = \frac{-k(x - x_0)}{m}$$

Where:
* $m$ = Mass of the block ($\text{kg}$)
* $k$ = Spring stiffness constant ($\text{N/m}$)
* $x_0$ = Equilibrium position ($\text{m}$)
* $x$ = Current horizontal displacement ($\text{m}$)

### Numerical Integration: Euler-Cromer Method
Standard Euler integration introduces artificial energy into oscillatory systems, causing the amplitude to grow indefinitely. To maintain physical energy conservation, this simulation utilizes the **Euler-Cromer algorithm**:

1. **Update Velocity First:**  
   $$v_{t+\Delta t} = v_t + a(x_t) \cdot \Delta t$$

2. **Update Position using NEW Velocity:**  
   $$x_{t+\Delta t} = x_t + v_{t+\Delta t} \cdot \Delta t$$








---

## 🛠️ Features

* **Real-Time 3D Visualization:** Dynamic 3D graphics rendering a helical spring, mass block, fixed wall, and base floor.
* **Live Graphical Analysis:** Side-by-side $x(t)$ position-time plot using VPython `gcurve`.
* **Optimized Rendering Loop:** Direct vector updates to eliminate frame latency and micro-stuttering.

---

## 🚀 Getting Started

### Prerequisites

* Python 3.8+
* `vpython` library

### Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/spring-mass-oscillator.git](https://github.com/your-username/spring-mass-oscillator.git)
   cd spring-mass-oscillator
