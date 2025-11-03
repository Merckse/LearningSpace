"""
Tests for data analysis solutions
"""

import pytest
import sys
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for testing
import matplotlib.pyplot as plt

# Add solutions directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'solutions'))

from data_analysis import numpy_basics, pandas_basics, data_visualization


class TestNumpyBasics:
    """Test NumPy operations"""
    
    def test_create_array_from_list(self):
        arr = numpy_basics.create_array_from_list([1, 2, 3, 4, 5])
        assert isinstance(arr, np.ndarray)
        assert arr.tolist() == [1, 2, 3, 4, 5]
    
    def test_create_zeros_array(self):
        arr = numpy_basics.create_zeros_array((2, 3))
        assert arr.shape == (2, 3)
        assert np.all(arr == 0)
    
    def test_create_range_array(self):
        arr = numpy_basics.create_range_array(0, 10, 2)
        assert arr.tolist() == [0, 2, 4, 6, 8]
    
    def test_reshape_array(self):
        arr = np.array([1, 2, 3, 4, 5, 6])
        reshaped = numpy_basics.reshape_array(arr, (2, 3))
        assert reshaped.shape == (2, 3)
    
    def test_array_statistics(self):
        arr = np.array([1, 2, 3, 4, 5])
        stats = numpy_basics.array_statistics(arr)
        assert stats['mean'] == 3.0
        assert stats['min'] == 1.0
        assert stats['max'] == 5.0
    
    def test_matrix_multiplication(self):
        a = np.array([[1, 2], [3, 4]])
        b = np.array([[5, 6], [7, 8]])
        result = numpy_basics.matrix_multiplication(a, b)
        assert result.tolist() == [[19, 22], [43, 50]]
    
    def test_normalize_array(self):
        arr = np.array([10, 20, 30, 40, 50])
        normalized = numpy_basics.normalize_array(arr)
        assert normalized.tolist() == [0.0, 0.25, 0.5, 0.75, 1.0]
    
    def test_boolean_indexing(self):
        arr = np.array([1, 5, 3, 8, 2, 9])
        result = numpy_basics.boolean_indexing(arr, 4)
        assert result.tolist() == [5, 8, 9]


class TestPandasBasics:
    """Test Pandas operations"""
    
    def test_create_dataframe_from_dict(self):
        df = pandas_basics.create_dataframe_from_dict({'A': [1, 2, 3], 'B': [4, 5, 6]})
        assert df.shape == (3, 2)
        assert list(df.columns) == ['A', 'B']
    
    def test_filter_dataframe(self):
        df = pd.DataFrame({'A': [1, 5, 3], 'B': [4, 2, 6]})
        filtered = pandas_basics.filter_dataframe(df, 'A', 2)
        assert filtered.shape[0] == 2
    
    def test_group_and_aggregate(self):
        df = pd.DataFrame({'Category': ['A', 'B', 'A'], 'Value': [10, 20, 30]})
        result = pandas_basics.group_and_aggregate(df, 'Category', 'Value', 'sum')
        assert result['A'] == 40
        assert result['B'] == 20
    
    def test_handle_missing_values_drop(self):
        df = pd.DataFrame({'A': [1, np.nan, 3], 'B': [4, 5, 6]})
        result = pandas_basics.handle_missing_values(df, 'drop')
        assert result.shape[0] == 2
    
    def test_handle_missing_values_fill(self):
        df = pd.DataFrame({'A': [1, np.nan, 3], 'B': [4, 5, 6]})
        result = pandas_basics.handle_missing_values(df, 'fill_mean')
        assert not result['A'].isna().any()
    
    def test_merge_dataframes(self):
        df1 = pd.DataFrame({'ID': [1, 2], 'Name': ['Alice', 'Bob']})
        df2 = pd.DataFrame({'ID': [1, 2], 'Age': [25, 30]})
        merged = pandas_basics.merge_dataframes(df1, df2, 'ID')
        assert merged.shape == (2, 3)
    
    def test_sort_dataframe(self):
        df = pd.DataFrame({'A': [3, 1, 2]})
        sorted_df = pandas_basics.sort_dataframe(df, 'A')
        assert sorted_df['A'].tolist() == [1, 2, 3]
    
    def test_add_calculated_column(self):
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        result = pandas_basics.add_calculated_column(df, 'C', lambda x: x['A'] + x['B'])
        assert result['C'].tolist() == [5, 7, 9]
    
    def test_pivot_table_summary(self):
        df = pd.DataFrame({'A': ['X', 'X', 'Y'], 'B': ['P', 'Q', 'P'], 'C': [1, 2, 3]})
        pivot = pandas_basics.pivot_table_summary(df, 'C', 'A', 'B')
        assert pivot.shape == (2, 2)


class TestDataVisualization:
    """Test data visualization functions"""
    
    def test_create_line_plot(self):
        fig = data_visualization.create_line_plot([1, 2, 3], [1, 4, 9])
        assert isinstance(fig, plt.Figure)
        plt.close(fig)
    
    def test_create_bar_chart(self):
        fig = data_visualization.create_bar_chart(['A', 'B', 'C'], [10, 20, 15])
        assert isinstance(fig, plt.Figure)
        plt.close(fig)
    
    def test_create_histogram(self):
        fig = data_visualization.create_histogram(np.random.randn(100))
        assert isinstance(fig, plt.Figure)
        plt.close(fig)
    
    def test_create_scatter_plot(self):
        fig = data_visualization.create_scatter_plot([1, 2, 3], [1, 4, 9])
        assert isinstance(fig, plt.Figure)
        plt.close(fig)
    
    def test_create_box_plot(self):
        fig = data_visualization.create_box_plot([[1, 2, 3], [2, 3, 4]], ['A', 'B'])
        assert isinstance(fig, plt.Figure)
        plt.close(fig)
    
    def test_create_heatmap(self):
        data = np.array([[1, 2], [3, 4]])
        fig = data_visualization.create_heatmap(data)
        assert isinstance(fig, plt.Figure)
        plt.close(fig)
    
    def test_create_subplots(self):
        data = [{'x': [1, 2], 'y': [1, 4]}, {'x': [1, 2], 'y': [2, 3]}]
        fig = data_visualization.create_subplots(data, ['line', 'scatter'])
        assert isinstance(fig, plt.Figure)
        plt.close(fig)
    
    def test_create_correlation_matrix_plot(self):
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
        fig = data_visualization.create_correlation_matrix_plot(df)
        assert isinstance(fig, plt.Figure)
        plt.close(fig)
