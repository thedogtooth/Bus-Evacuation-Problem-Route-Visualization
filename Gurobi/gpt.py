import gurobipy as gp
from gurobipy import GRB

# Create a new model
model = gp.Model("bus_evacuations")

# Example parameters
locations = range(3)
buses = range(3)
capacity = [50] * 3  # Bus capacities
people = [100] * 3  # People at each location
travel_times = [[10, 20, 30], [20, 10, 15], [30, 25, 10]]  # Travel times between locations and buses

# Variables
x = model.addVars(buses, locations, vtype=GRB.BINARY, name="x")
y = model.addVars(buses, vtype=GRB.CONTINUOUS, name="y")

# Objective: Minimize the maximum evacuation time
model.setObjective(gp.quicksum(travel_times[i][j] * x[i, j] for i in buses for j in locations), GRB.MINIMIZE)

# Constraints
for j in locations:
    model.addConstr(gp.quicksum(x[i, j] for i in buses) == 1)  # Assign exactly one bus to each location

for i in buses:
    model.addConstr(gp.quicksum(people[j] * x[i, j] for j in locations) <= capacity[i])  # Bus capacity

# Optimize model
model.optimize()

# Output results
for i in buses:
    for j in locations:
        print(x[i, j])
        if x[i, j].x > 0.5:  # Check if the variable is set
            print(f"Bus {i} will evacuate from location {j}")

print(f"Optimal objective value: {model}")
