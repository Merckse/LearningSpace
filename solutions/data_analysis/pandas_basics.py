"""
Pandas Basics Solutions
"""

import pandas as pd
import numpy as np


def create_dataframe_from_dict(data_dict):
    """Create DataFrame from dictionary."""
    return pd.DataFrame(data_dict)


def filter_dataframe(df, column, threshold):
    """Filter DataFrame."""
    return df[df[column] > threshold]


def group_and_aggregate(df, group_column, agg_column, agg_func='mean'):
    """Group and aggregate data."""
    return df.groupby(group_column)[agg_column].agg(agg_func)


def handle_missing_values(df, strategy='drop'):
    """Handle missing values."""
    if strategy == 'drop':
        return df.dropna()
    elif strategy == 'fill_mean':
        return df.fillna(df.mean())
    return df


def merge_dataframes(df1, df2, on_column):
    """Merge two DataFrames."""
    return pd.merge(df1, df2, on=on_column)


def sort_dataframe(df, column, ascending=True):
    """Sort DataFrame."""
    return df.sort_values(by=column, ascending=ascending)


def add_calculated_column(df, new_column, calculation):
    """Add calculated column."""
    df = df.copy()
    df[new_column] = calculation(df)
    return df


def pivot_table_summary(df, values, index, columns, aggfunc='mean'):
    """Create pivot table."""
    return pd.pivot_table(df, values=values, index=index, 
                         columns=columns, aggfunc=aggfunc)
