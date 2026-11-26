
import numpy as np
import matplotlib.pyplot as plt

# Generate x-axis values
x = np.linspace(-10, 10, 400)

# Define mathematical functions
sine = np.sin(x)
cosine = np.cos(x)
quadratic = x ** 2
cubic = x ** 3

# Ask the user to choose a graph
print("\n===== GRAPH PLOTTER =====")
print("1. Sine Wave")
print("2. Cosine Wave")
print("3. Quadratic Graph")
print("4. Cubic Graph")
print("5. Display All Graphs")

choice = input("\nEnter your choice (1-5): ")

# Create the graph
plt.figure(figsize=(10, 6))
plt.style.use("dark_background")

if choice == "1":
    plt.plot(x, sine, label="y = sin(x)", color="cyan")

elif choice == "2":
    plt.plot(x, cosine, label="y = cos(x)", color="magenta")

elif choice == "3":
    plt.plot(x, quadratic, label="y = x²", color="lime")

elif choice == "4":
    plt.plot(x, cubic, label="y = x³", color="orange")

elif choice == "5":
    plt.plot(x, sine, label="Sine", color="cyan")
    plt.plot(x, cosine, label="Cosine", color="magenta")
    plt.plot(x, quadratic, label="Quadratic", color="lime")
    plt.plot(x, cubic, label="Cubic", color="orange")

else:
    print("Invalid choice!")
    exit()

# Customize the graph
plt.title("MAKx - Mathematical Graph Plotter")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.axhline(0, color="white", linewidth=0.7)
plt.axvline(0, color="white", linewidth=0.7)
plt.grid(True, alpha=0.25)
plt.legend()

# Display the graph
plt.show()
