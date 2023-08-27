import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd

def plot_recoltables(df: pd.DataFrame):
    
    # Calculate grid boundaries based on data range
    x_min, x_max = df['x'].min(), df['x'].max()
    y_min, y_max = df['y'].min(), df['y'].max()
    
    # Generate grid points
    x_grid = np.arange(np.floor(x_min), np.ceil(x_max) + 1)
    y_grid = np.arange(np.floor(y_min), np.ceil(y_max) + 1)
    
    # Create a figure
    fig = go.Figure()
    
    # Add integer grid using scatter traces
    for x in x_grid:
        fig.add_trace(go.Scatter(x=[x] * len(y_grid), y=y_grid, mode='markers', marker=dict(color='blue', size=3), showlegend=False))
    
    for y in y_grid:
        fig.add_trace(go.Scatter(x=x_grid, y=[y] * len(x_grid), mode='markers', marker=dict(color='blue', size=3), showlegend=False))
    
    # Add points from the DataFrame
    colors = ['red', 'black', 'green', 'purple']
    for i, zone in enumerate(df.zone.unique()):
        X = df[df.zone == zone]
        fig.add_trace(go.Scatter(x=X['x'], y=X['y'], mode='markers', marker=dict(color=colors[i]), name=zone))
    fig.update_yaxes(autorange="reversed")
    fig.update_layout(height=500)
    fig.show()    