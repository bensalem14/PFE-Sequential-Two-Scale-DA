import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to update the plot for each frame
def update(frame):
    plt.clf()
    frame1=frame+8000
    # Scatter plot for current particle position
    
    plt.scatter(df.iloc[frame]['Xe1'], df.iloc[frame]['Xe2'], label='Micro-Particle')
    plt.scatter(df.iloc[frame1]['X01'], df.iloc[frame1]['X02'], label='Macro-Particle')
    # Trajectory plot up to the current frame
    plt.plot(df.iloc[:frame + 1]['Xe1'], df.iloc[:frame + 1]['Xe2'], color='blue', linestyle='dashed', label='Micro-Trajectory')
    plt.plot(df.iloc[:frame1 + 1]['X01'], df.iloc[:frame1 + 1]['X02'], color='red', linestyle='dashed', label='Macro-Trajectory')

    plt.title(f'MacroTime: {df.iloc[frame1]["t"]} MicroTime: {df.iloc[frame]["t"]}')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()

# Load data from CSV file
csv_filename = 'GenData/True/Full/4D_Tokamak.csv'
df = pd.read_csv(csv_filename)

# Set up the figure and axis
fig, ax = plt.subplots()

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=10, repeat=False)

#ani.save('Experiment2/Animation/particle_animation.mp4', writer='pillow', fps=10)
writergif = animation.PillowWriter(fps=30)
ani.save('Animation/particle1.gif',writer=writergif)
# Show the animation
plt.show()
