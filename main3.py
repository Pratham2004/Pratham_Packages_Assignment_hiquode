from task3.math_ops import get_mean, get_median, get_mode
from task3.visuals import bar_chart

data = [4, 2, 4, 6, 2, 4, 7, 5]

print("Mean  :", get_mean(data))
print("Median:", get_median(data))
print("Mode  :", get_mode(data))

labels = ["A", "B", "C", "D"]
values = [10, 15, 7, 12]
bar_chart(labels, values, title="Demo Bar Chart")