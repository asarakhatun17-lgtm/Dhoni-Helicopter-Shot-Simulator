import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- 1. SETTING UP THE PITCH ---
v0 = 35.0  # Ball ki initial speed
angle_deg = 45.0  # Best angle for Sixer!
g = 9.8 
angle_rad = np.radians(angle_deg)

# --- 2. THE PHYSICS ---
T = (2 * v0 * np.sin(angle_rad)) / g
t = np.linspace(0, T, num=100) # Time ke 100 frames
x = v0 * np.cos(angle_rad) * t
y = (v0 * np.sin(angle_rad) * t) - (0.5 * g * t**2)

# --- 3. DRAWING THE STADIUM ---
fig, ax = plt.subplots(figsize=(10, 5))
ax.set_xlim(0, max(x) + 10) # X-axis ki limit
ax.set_ylim(0, max(y) + 10) # Y-axis ki limit
ax.set_title("🚁 MS Dhoni's Animated Helicopter Shot 🏏", fontsize=14, fontweight='bold')
ax.set_xlabel("Distance (Meters)", fontsize=12)
ax.set_ylabel("Height (Meters)", fontsize=12)
ax.grid(True, linestyle='--', alpha=0.7)
ax.axhline(y=0, color='black', linewidth=3) # Ground

# THE BOUNDARY LINE CHALLENGE 🚩
ax.axvline(x=75, color='red', linestyle='-', linewidth=3, label="Boundary Rope (75m)")

# Ball aur Trajectory ki line create karna (Abhi khali hain)
line, = ax.plot([], [], color='blue', linewidth=2, label="Trajectory")
ball, = ax.plot([], [], 'ro', markersize=10) # 'ro' matlab Red Dot (Ball)
ax.legend()

# --- 4. THE MAGIC ANIMATION ---
def update(frame):
    # Har frame par line aur ball ki position update hogi
    line.set_data(x[:frame], y[:frame])
    # Ball ke liye x[frame] aur y[frame] ko list (sequence) mein wrap kiya hai
    ball.set_data([x[frame]], [y[frame]]) 
    return line, ball

# FuncAnimation library code ko animate karti hai
ani = FuncAnimation(fig, update, frames=len(t), interval=30, blit=True)

# Action! 🎬
plt.show()
