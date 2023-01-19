import numpy as np

class LinearOscillator:
    def __init__(self, mass=1, spring_constant=1, initial_position=0, initial_velocity=0):
        self.mass = mass
        self.spring_constant = spring_constant
        self.position = initial_position
        self.velocity = initial_velocity
        
    def update(self, dt):
        acceleration = -self.spring_constant / self.mass * self.position
        self.velocity += acceleration * dt
        self.position += self.velocity * dt

noise_amplitude = 0.1
noise = np.random.normal(0, noise_amplitude, size=num_timesteps)

oscillator = LinearOscillator()
for i in range(num_timesteps):
    oscillator.position += noise[i]
    oscillator.update(dt)
    positions.append(oscillator.position)
    velocities.append(oscillator.velocity)
    
import matplotlib.pyplot as plt

plt.plot(times, positions)
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.show()
