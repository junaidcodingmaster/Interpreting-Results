import pandas as pd
import matplotlib.pyplot as plt

# Import the csv file created in project 134
df = pd.read_csv('./gravity.csv')

# Make a list of the star's name, Mass, Radius, Distance and Gravity
data = df[['Star_name', 'Mass', 'Radius', 'Distance', 'Gravity']]

# Create a 2x2 grid of plots
fig, axs = plt.subplots(2, 2)

# Set the window title
fig.suptitle("Star Data")

# Plot the bar chart for Star name vs Mass
axs[0, 0].bar(data["Star_name"], data["Mass"])
axs[0, 0].set_title("Star name vs Mass")

# Plot the bar chart for Star name vs Radius
axs[0, 1].bar(data["Star_name"], data["Radius"])
axs[0, 1].set_title("Star name vs Radius")

# Plot the bar chart for Star name vs Distance
axs[1, 0].bar(data["Star_name"], data["Distance"])
axs[1, 0].set_title("Star name vs Distance(from Earth)")

# Plot the bar chart for Star name vs Gravity
axs[1, 1].bar(data["Star_name"], data["Gravity"])
axs[1, 1].set_title("Star name vs Gravity")

# Show the plots
plt.show()

print("\nStar name vs Mass -> Plotted! - ✅")
print("\nStar name vs Radius -> Plotted! - ✅")
print("\nStar name vs Distance(from Earth) -> Plotted! - ✅")
print("\nStar name vs Gravity -> Plotted! - ✅")

# Interpretation:
# The plots shows the variation of mass, radius, distance and gravity among the different stars.
# As we can see from the plots, some stars have higher mass, radius, distance and gravity than others.
# Author: Junaid (https://abujuni.dev)



