"""
Data Visualization Tasks

Practice creating visualizations with matplotlib and seaborn.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


def create_line_plot(x, y, title="Line Plot", xlabel="X", ylabel="Y"):
    """
    Create a simple line plot.
    
    Args:
        x (list/array): X-axis values
        y (list/array): Y-axis values
        title (str): Plot title
        xlabel (str): X-axis label
        ylabel (str): Y-axis label
        
    Returns:
        matplotlib.figure.Figure: The figure object
        
    Example:
        >>> fig = create_line_plot([1, 2, 3], [1, 4, 9])
        >>> plt.close(fig)
    """
    # TODO: Create a line plot with labels and title
    # Use plt.subplots() to create figure
    # Return the figure object
    pass


def create_bar_chart(categories, values, title="Bar Chart"):
    """
    Create a bar chart.
    
    Args:
        categories (list): Category names
        values (list): Values for each category
        title (str): Chart title
        
    Returns:
        matplotlib.figure.Figure: The figure object
        
    Example:
        >>> fig = create_bar_chart(['A', 'B', 'C'], [10, 20, 15])
        >>> plt.close(fig)
    """
    # TODO: Create a bar chart
    pass


def create_histogram(data, bins=10, title="Histogram"):
    """
    Create a histogram.
    
    Args:
        data (list/array): Data to plot
        bins (int): Number of bins
        title (str): Plot title
        
    Returns:
        matplotlib.figure.Figure: The figure object
        
    Example:
        >>> fig = create_histogram(np.random.randn(100))
        >>> plt.close(fig)
    """
    # TODO: Create a histogram
    pass


def create_scatter_plot(x, y, title="Scatter Plot"):
    """
    Create a scatter plot.
    
    Args:
        x (list/array): X-axis values
        y (list/array): Y-axis values
        title (str): Plot title
        
    Returns:
        matplotlib.figure.Figure: The figure object
        
    Example:
        >>> fig = create_scatter_plot([1, 2, 3], [1, 4, 9])
        >>> plt.close(fig)
    """
    # TODO: Create a scatter plot
    pass


def create_box_plot(data, labels=None, title="Box Plot"):
    """
    Create a box plot for multiple datasets.
    
    Args:
        data (list of lists): Multiple datasets
        labels (list): Labels for each dataset
        title (str): Plot title
        
    Returns:
        matplotlib.figure.Figure: The figure object
        
    Example:
        >>> fig = create_box_plot([[1, 2, 3], [2, 3, 4]], ['A', 'B'])
        >>> plt.close(fig)
    """
    # TODO: Create a box plot
    pass


def create_heatmap(data, title="Heatmap"):
    """
    Create a heatmap using seaborn.
    
    Args:
        data (2D array/DataFrame): Data for heatmap
        title (str): Plot title
        
    Returns:
        matplotlib.figure.Figure: The figure object
        
    Example:
        >>> data = np.array([[1, 2], [3, 4]])
        >>> fig = create_heatmap(data)
        >>> plt.close(fig)
    """
    # TODO: Create a heatmap using seaborn
    pass


def create_subplots(data_list, plot_types):
    """
    Create a figure with multiple subplots.
    
    Args:
        data_list (list): List of data dictionaries, each containing plot data
        plot_types (list): List of plot types ('line', 'bar', 'scatter')
        
    Returns:
        matplotlib.figure.Figure: The figure object
        
    Example:
        >>> data = [{'x': [1, 2], 'y': [1, 4]}, {'x': [1, 2], 'y': [2, 3]}]
        >>> fig = create_subplots(data, ['line', 'scatter'])
        >>> plt.close(fig)
    """
    # TODO: Create multiple subplots in a grid
    pass


def create_correlation_matrix_plot(df):
    """
    Create a correlation matrix heatmap for a DataFrame.
    
    Args:
        df (pd.DataFrame): DataFrame with numerical columns
        
    Returns:
        matplotlib.figure.Figure: The figure object
        
    Example:
        >>> df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        >>> fig = create_correlation_matrix_plot(df)
        >>> plt.close(fig)
    """
    # TODO: Calculate correlation matrix and create heatmap
    pass
