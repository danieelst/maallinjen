import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src.calculations import distribution
from matplotlib.ticker import MaxNLocator

# Set default style of graphs
def set_default_style(fig, ax):
  fig.patch.set_facecolor((0.0, 0.0, 0.0))
  ax.set_facecolor((0.0, 0.0, 0.0))
  ax.tick_params(axis='y', colors='white', grid_linestyle='dashed', left=False)
  ax.tick_params(axis='x', colors='white', grid_linestyle='dashed', bottom=False)
  plt.grid(True)

# Draw a graph based on a given result table
def draw_graph(df, title):

  # Builds the rightmost labels in the graph
  def build_labels(labels, y_val, label):
    if y_val in labels:
      labels[y_val] = f'{labels[y_val]} {label}'
    else:
      labels[y_val] = label
    return labels

  fig, ax = plt.subplots()
  set_default_style(fig,ax)

  labels = {}

  # Plot each column
  for x in df.columns:
    plt.plot(df.index, df[x], alpha=1.0, label=x)
    y = df.iloc[-1][x]
    labels = build_labels(labels, y, x)

  # Place the rightmost labels
  for y in labels:
    ax.annotate(labels[y], xy=(1,y), xytext=(6,0), color='white',
                xycoords = ax.get_yaxis_transform(), textcoords="offset points",
                size=14, ha='center', va='bottom')

  plt.rcParams["axes.prop_cycle"] = plt.cycler('color', plt.cm.hsv(np.linspace(0,1,len(df.columns))))
  plt.xlim(xmin=0.0)
  plt.xticks(df.index)
  ax.yaxis.set_major_locator(MaxNLocator(integer=True))
  plt.title(title, color='white')
  plt.legend(facecolor='black', framealpha=1, labelcolor='white', loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=5)
  plt.show()

# Draw a graph of the probability distribution
def draw_distribution():
  fig, ax = plt.subplots()
  set_default_style(fig, ax)
  df = pd.DataFrame([distribution(0,i) for i in range(0,6)])
  plt.plot(df.index, df[0])
  plt.xticks(df.index)
  plt.title('Probability distribution used for accuracy calculations', color='white')
  plt.ylabel('%', color='white')
  plt.xlabel('Offset', color='white')
  plt.show()
