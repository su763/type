# visualization.py
import matplotlib.pyplot as plt

def display_bar_chart(data):
    """Display a bar chart with sample data."""
    categories = list(data.keys())
    values = list(data.values())
    
    plt.figure(figsize=(10, 5))
    plt.bar(categories, values)
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.title('Sample Data Visualization')
    plt.show()

if __name__ == "__main__":
    sample_data = {"Category A": 10, "Category B": 15, "Category C": 7}
    display_bar_chart(sample_data)
