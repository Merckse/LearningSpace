"""
Data Visualization Solutions
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


def create_line_plot(x, y, title="Line Plot", xlabel="X", ylabel="Y"):
    """Create line plot."""
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(x, y)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True, alpha=0.3)
    return fig


def create_bar_chart(categories, values, title="Bar Chart"):
    """Create bar chart."""
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(categories, values)
    ax.set_title(title)
    ax.set_xlabel("Categories")
    ax.set_ylabel("Values")
    return fig


def create_histogram(data, bins=10, title="Histogram"):
    """Create histogram."""
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.hist(data, bins=bins, edgecolor='black')
    ax.set_title(title)
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    return fig


def create_scatter_plot(x, y, title="Scatter Plot"):
    """Create scatter plot."""
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(x, y)
    ax.set_title(title)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.grid(True, alpha=0.3)
    return fig


def create_box_plot(data, labels=None, title="Box Plot"):
    """Create box plot."""
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.boxplot(data, tick_labels=labels)
    ax.set_title(title)
    ax.set_ylabel("Values")
    return fig


def create_heatmap(data, title="Heatmap"):
    """Create heatmap."""
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(data, annot=True, fmt='.2f', cmap='coolwarm', ax=ax)
    ax.set_title(title)
    return fig


def create_subplots(data_list, plot_types):
    """Create multiple subplots."""
    n_plots = len(data_list)
    fig, axes = plt.subplots(1, n_plots, figsize=(6 * n_plots, 5))
    
    if n_plots == 1:
        axes = [axes]
    
    for i, (data, plot_type) in enumerate(zip(data_list, plot_types)):
        ax = axes[i]
        
        if plot_type == 'line':
            ax.plot(data['x'], data['y'])
        elif plot_type == 'bar':
            ax.bar(data['x'], data['y'])
        elif plot_type == 'scatter':
            ax.scatter(data['x'], data['y'])
        
        ax.set_title(f'{plot_type.capitalize()} Plot {i+1}')
        ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    return fig


def create_correlation_matrix_plot(df):
    """Create correlation matrix heatmap."""
    fig, ax = plt.subplots(figsize=(10, 8))
    corr = df.corr()
    sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', 
                square=True, ax=ax)
    ax.set_title('Correlation Matrix')
    return fig
