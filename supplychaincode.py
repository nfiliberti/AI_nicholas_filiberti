import numpy as np
# lead time in days
MIN_LEAD_TIME = 1  

class Product:
    def __init__(self, product_id, name, demand_forecasting_model, production_requirements, transportation_constraints):
        self.product_id = product_id
        self.name = name
        self.demand_forecasting_model = demand_forecasting_model
        self.production_requirements = production_requirements
        self.transportation_constraints = transportation_constraints

class Node:
    def __init__(self, location, cost, heuristic):
        self.location = location
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def compare_nodes(node):
    return node.cost + node.heuristic

def astar(graph, start, goal):
    open_set = [Node(start, 0, heuristic(start, goal))]
    closed_set = set()
    while open_set:
        current_node = min(open_set, key = compare_nodes)
        open_set.remove(current_node)
        if current_node.location == goal:
            return current_node
        closed_set.add(current_node.location)
        for neighbor, cost in graph[current_node.location].items():
            if neighbor not in closed_set:
                neighbor_node = Node(neighbor, current_node.cost + cost, heuristic(neighbor, goal))
                open_set.append(neighbor_node)
    return None

def heuristic(node, goal):
    # Example heuristic: Manhattan distance 
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

def demand_forecasting(product):
    # This function could use a time series forecasting model based on historical sales data for the product
    historical_sales_data = np.random.randint(100, 1000, size = 12)  # Example: Monthly sales data for the past year
    forecast = np.mean(historical_sales_data)  # Example: Simple average forecast
    return int(forecast)

def inventory_management(demand, inventory):
    order_quantity = max(demand - inventory, 0)  
    return order_quantity

def production_planning(product):
    print("Production planning for ", product.name)
    print("Production requirements:", product.production_requirements)
    print("Generating production schedule...")
    production_schedule = {'Day 1': 'Produce 100 units', 'Day 2': 'Produce 150 units', 'Day 3': 'Produce 200 units',}
    for day, activity in production_schedule.items():
        print(day, "-", activity)

# Supplier Evaluation Function
def evaluate_suppliers(supplier_performance):
    delivery_weight = 0.5
    quality_weight = 0.5
    performance_scores = {}
    for supplier, performance in supplier_performance.items():
        performance_scores[supplier] = (delivery_weight * performance['Delivery Reliability']) + (quality_weight * performance['Product Quality'])
    best_supplier = max(performance_scores, key=performance_scores.get)
    return best_supplier

# Negotiation
def negotiate_terms(supplier_performance, initial_terms):
    adjusted_terms = {}
    for supplier, performance in supplier_performance.items():
        adjusted_unit_price = initial_terms['Unit Price'] * (1 - (1 - performance['Delivery Reliability']))
        adjusted_lead_time = initial_terms['Lead Time'] - int(performance['Product Quality'] * 2)
        adjusted_lead_time = max(adjusted_lead_time, MIN_LEAD_TIME)
        adjusted_terms[supplier] = {'Unit Price': adjusted_unit_price, 'Lead Time': adjusted_lead_time}
    return adjusted_terms

# Function for supplier management
def supplier_management(product):
    print("Supplier management for ", product.name)
    print("Evaluating suppliers...")
    suppliers = ['Supplier A', 'Supplier B', 'Supplier C']
    supplier_performance = {}
    for supplier in suppliers:
        supplier_performance[supplier] = {'Delivery Reliability': np.random.uniform(0.7, 0.95),'Product Quality': np.random.uniform(0.8, 0.98)}
    print("Supplier performance:", supplier_performance)
    best_supplier = evaluate_suppliers(supplier_performance)
    print("Best supplier:", best_supplier)
    initial_terms = {'Unit Price': 1.0, 'Lead Time': 10}
    adjusted_terms = negotiate_terms(supplier_performance, initial_terms)
    print("Adjusted terms:", adjusted_terms)
    print("Established regular communication and performance monitoring.")

# Example graph representing transportation network
graph = {
    (0, 0): {(0, 1): 5, (1, 0): 10, (2, 0): 8},
    (0, 1): {(0, 0): 5, (1, 0): 3, (1, 1): 7, (1, 2): 6},
    (1, 0): {(0, 0): 10, (0, 1): 3, (1, 1): 2},
    (1, 1): {(0, 1): 7, (1, 0): 2, (1, 2): 9},
    (2, 0): {(0, 0): 8, (1, 2): 4, (2, 1): 12},
    (1, 2): {(0, 1): 6, (1, 1): 9, (2, 0): 4, (2, 1): 5},
    (2, 1): {(2, 0): 12, (1, 2): 5}
}

start = (0, 0)
goal = (2, 1)

# Main function to simulate supply chain management process for multiple products
def supply_chain_management(products):
    for product in products:
        demand = demand_forecasting(product)
        inventory = np.random.randint(0, 500)  
        order_quantity = inventory_management(demand, inventory)
        production_planning(product)
        supplier_management(product)
        result = astar(graph, start, goal)
        print("Product:", product.name)
        print("Demand Forecast:", demand)
        print("Order Quantity:", order_quantity)
        if result:
            print("Optimal Path:", result.location)
            print("Total Cost:", result.cost)
        else:
            print("No path found")
        print()

product1 = Product(1, "Product 1", "Demand Forecasting Model 1", "Production Requirements 1", "Transportation Constraints 1")
product2 = Product(2, "Product 2", "Demand Forecasting Model 2", "Production Requirements 2", "Transportation Constraints 2")
product3 = Product(3, "Product 3", "Demand Forecasting Model 3", "Production Requirements 3", "Transportation Constraints 3")

supply_chain_management([product1, product2, product3])