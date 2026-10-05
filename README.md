# Python Data Visualization with Matplotlib

This project contains seven Python programs that demonstrate different types of charts using Matplotlib. Each program uses sample data to practice plotting and chart customization.

## Objective

Learn how to visualize data using line charts, bar charts, pie charts, scatter plots, and histograms, and make them easier to understand with titles, labels, colors, markers, and legends.

## Programs

### 1. Basic Line Chart

Plots the relationship between two numerical lists:

- **X values:** 1, 2, 3, 4, 5
- **Y values:** 2, 4, 6, 8, 10
- **Style:** Pink line with square markers
- **Title:** My First Graph

The chart shows a linear relationship: each y value is twice its corresponding x value.

### 2. College Semester Scores — Bar Chart

Compares scores across five subjects using pink and purple bars.

| Subject | Score |
| --- | --- |
| OS | 88 |
| Python | 89 |
| Java | 78 |
| Networks | 79 |
| Data Analysis | 97 |

Data Analysis has the highest score, while Java has the lowest.

### 3. Newspaper Reading Survey — Line Chart

Displays newspaper visits throughout the week using an orange line with a line width of 5.

| Day | Visits |
| --- | --- |
| Monday | 200 |
| Tuesday | 233 |
| Wednesday | 201 |
| Thursday | 234 |
| Friday | 345 |
| Saturday | 456 |
| Sunday | 900 |

Sunday records the highest number of visits, while Monday records the lowest.

### 4. Website Visit Comparison — Multiple-Line Chart

Compares daily visit counts for two series, labeled **A** and **B**.

| Day | A | B |
| --- | --- | --- |
| Monday | 200 | 100 |
| Tuesday | 233 | 123 |
| Wednesday | 201 | 134 |
| Thursday | 234 | 101 |
| Friday | 345 | 45 |
| Saturday | 456 | 156 |
| Sunday | 900 | 600 |

An orange line represents A, and a green line represents B. A legend identifies both series. A has more visits on every day, and both series peak on Sunday.

### 5. Monthly Budget — Pie Chart

Shows how a monthly budget is divided among four categories.

| Category | Percentage |
| --- | --- |
| Rent | 40% |
| Groceries | 30% |
| Transport | 15% |
| Savings | 15% |

Percentages are displayed to one decimal place. The rent slice is separated slightly from the pie using the `explode` parameter to emphasize the largest allocation.

### 6. Website Visit Count — Scatter Plot

Displays daily website visits as individual blue points, using the values 200, 233, 201, 234, 345, 456, and 900 from Monday to Sunday.

Unlike the line-chart examples, this chart does not connect the points. Although the program defines a second list named `visit2`, only the `visits` list is plotted.

### 7. Frequency Distribution — Histogram

Shows the frequency distribution of the following numerical values:

```python
[40, 30, 15, 15, 22, 23, 67, 55, 46, 34]
```

- **Bins:** 10
- **Bar color:** Red
- **Edge color:** Black
- **X-axis:** Value
- **Y-axis:** Frequency
- **Title:** My First Histogram

The histogram groups numerical values into intervals and shows how many observations fall within each interval.

## Matplotlib Functions Used

| Function | Purpose |
| --- | --- |
| `plt.plot()` | Create line charts |
| `plt.bar()` | Create a bar chart |
| `plt.pie()` | Create a pie chart |
| `plt.scatter()` | Create a scatter plot |
| `plt.hist()` | Create a histogram |
| `plt.xlabel()` | Add an x-axis label |
| `plt.ylabel()` | Add a y-axis label |
| `plt.title()` | Add a chart title |
| `plt.legend()` | Identify labeled data series |
| `plt.grid()` | Add grid lines |
| `plt.show()` | Display the chart |

**Code note:** In the first program, move `plt.grid()` before `plt.show()` so the grid is added before the chart is displayed.

## Learning Outcomes

- Select chart types for comparisons, trends, proportions, and distributions.
- Customize plots using colors, markers, line styles, and line widths.
- Add titles, axis labels, legends, and percentage labels.
- Compare multiple data series on the same chart.

All values are sample data included directly in the programs.

