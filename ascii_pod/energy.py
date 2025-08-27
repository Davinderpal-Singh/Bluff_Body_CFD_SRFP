import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# --- Load Data ---
B = np.load('B.npy')
Amp_test = np.load('Amp_test.npy')  # shape: (modes, timesteps)
times = np.loadtxt('times.txt')

# --- POD Energy Computation ---
C = np.matmul(B.T, B) / B.shape[1]
S, _ = np.linalg.eig(C)
S = np.real(S)  # In case of small imaginary due to numerical errors
S = np.sort(S)[::-1]  # Descending order

Energy = S**2
Energy = Energy / np.sum(Energy)  # Normalize

# Save energy
np.save('Energy.npy', Energy)

# --- Cumulative Energy ---
cum_energy = np.cumsum(Energy)

# Plot POD Energy
plt.figure(figsize=(10, 6))
plt.bar(np.arange(1, len(Energy)+1), Energy)
plt.xlabel('Modes')
plt.ylabel('Energy Content')
plt.title('POD Mode Energy')
plt.yscale('log')  # use log scale to make smaller values visible
plt.grid()
plt.savefig('energy_plot.png', dpi=300, bbox_inches='tight')

# Plot cumulative energy
plt.figure(figsize=(11, 6))
plt.plot(np.arange(1, len(cum_energy)+1), cum_energy, marker='o',markersize=3)
plt.xlabel('Number of Modes')
plt.ylabel('Cumulative Energy')
plt.title('Cumulative Energy vs Modes')
plt.grid()
plt.savefig('cumulative_energy.png', dpi=300, bbox_inches='tight')

# --- Print how many modes contribute ---
thresholds = [0.90, 0.95, 0.99, 0.995, 0.999]
print("\nModes required to capture energy thresholds:")
for t in thresholds:
    idx = np.argmax(cum_energy >= t)
    print(f"{t*100:.1f}% energy -> {idx+1} modes (Modes: {list(range(1, idx+2))})")

# --- Plot All 10 Mode Amplitudes in One Plot ---
plt.figure(figsize=(14, 7))
for i in range(10):
    plt.plot(times, Amp_test[i], label=f'Mode {i+1}')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('POD Mode Amplitudes vs Time (First 10 Modes)')
plt.legend()
plt.grid()
plt.savefig('amplitudes_vs_time.png', dpi=300, bbox_inches='tight')

# --- Subplots: One per mode ---
fig, axes = plt.subplots(5, 2, figsize=(14, 12), sharex=True)
axes = axes.flatten()
for i in range(10):
    axes[i].plot(times, Amp_test[i])
    axes[i].set_title(f'Mode {i+1}')
    axes[i].set_ylabel('Amplitude')
    axes[i].grid()
axes[-1].set_xlabel('Time')
plt.tight_layout()
plt.savefig('amplitudes_subplots.png', dpi=300, bbox_inches='tight')

# --- Animate First 10 Mode Amplitudes ---
fig, ax = plt.subplots(figsize=(10, 6))
lines = [ax.plot([], [], label=f'Mode {i+1}')[0] for i in range(10)]
ax.set_xlim(times[0], times[-1])
ax.set_ylim(np.min(Amp_test[:10]), np.max(Amp_test[:10]))
ax.set_xlabel("Time")
ax.set_ylabel("Amplitude")
ax.set_title("Animated POD Mode Amplitudes")
ax.legend()
ax.grid()

def init():
    for line in lines:
        line.set_data([], [])
    return lines

def update(frame):
    for i, line in enumerate(lines):
        line.set_data(times[:frame], Amp_test[i, :frame])
    return lines

ani = animation.FuncAnimation(fig, update, frames=len(times), init_func=init,
                              blit=True, interval=50)

# Save animation as GIF (Pillow backend)
ani.save('amplitudes_animation.gif', fps=30)

print("\n✅ All plots and animation saved successfully.")

