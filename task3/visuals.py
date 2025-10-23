import matplotlib.pyplot as plt

def bar_chart(labels, values, title="Bar Chart", xlabel="Items", ylabel="Values"):
  
    plt.figure(figsize=(6, 4))
    plt.bar(labels, values, color='skyblue')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.show()