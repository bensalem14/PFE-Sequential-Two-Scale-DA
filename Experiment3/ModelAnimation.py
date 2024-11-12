import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# Load data from CSV file
csv_filename = 'GenData/True/Full/ToyModel6.csv'
df = pd.read_csv(csv_filename)


# Create a figure and axis
fig, ax = plt.subplots()

# Initialize empty plot object
line_Xe, = ax.plot([], [], label='Xe')

# Set up the axes
ax.set_xlim(0, df['t'].max() + 1)
ax.set_ylim(0, df['Xe'].max() + 1)
ax.set_xlabel('Time (t)')
ax.set_ylabel('Xe')
ax.set_title('Evolution of Xe over Time')
ax.legend()

# Animation function
def animate(frame):
    line_Xe.set_data(df['t'][:frame], df['Xe'][:frame])
    return line_Xe,

# Create animation with interval (e.g., 200 milliseconds)
ani = animation.FuncAnimation(fig, animate, frames=1000, interval=20)

# Display the animation
plt.grid(True)
plt.show()