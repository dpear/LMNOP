import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from openai import OpenAI
from .prefixes import *

MODEL = 'gpt-3.5-turbo'

def ask(question, client, code=False):
    """
    Sends a question to the OpenAI chat model and prints the response.

    Parameters:
        question (str): The prompt for the chat model.
        client (OpenAI): A client instance initialized with an API key.

    Returns:
        str: The response from the chat model.
        
    Example:
        client = OpenAI(api_key="YOUR_API_KEY")
        ask(question="what is a bagel", client=client)
    """
    
    if code: question = question + '. provide code only. no descriptions'
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": question}],
        model=MODEL,
    )
    out = response.choices[0].message.content
    print('a')
    return out

def summarize_col(df, col_name, max_items_shown=10):
    """
    Prints a summary of a specific column in the dataframe.

    Parameters:
        df (DataFrame): The dataframe containing the column.
        col_name (str): The name of the column to summarize.
        max_items_shown (int): Maximum number of unique items to show.

    Outputs:
        Summary of the column to the console.
    """
    print(f"Column: {col_name}")
    print("=" * 32)
    a_col = df[col_name]
    unique_values = a_col.unique()
    unique_count = len(unique_values)

    if a_col.is_unique:
        print(f"All {unique_count} values are unique.")
    else:
        print(f"There are {unique_count} unique value(s) out of {len(a_col)} total values.")

    display_values = ' '.join(unique_values[:max_items_shown])
    trail = '...' if unique_count > max_items_shown else ''
    print(f"Sample values: {display_values} {trail}")
    print(f"Data type: {a_col.dtype}\n")

def find_problem_headers(df):
    """
    Identifies and prints problematic column headers in the dataframe.

    Parameters:
        df (DataFrame): The dataframe to check headers on.

    Outputs:
        Invalid column headers, if any.
    """
    
    print("Finding column headers with characters other than a-zA-Z0-9._")
    invalid_cols = df.columns[df.columns.str.contains(r'[^a-zA-Z0-9._ ]', regex=True)]
    if invalid_cols.empty:
        print("No invalid column headers found.")
    else:
        print(f"Invalid column headers found: {invalid_cols}")
        
    return invalid_cols

def scrub_headers(df, lower_case=True):
    """
    Cleans column headers by replacing non-alphanumeric characters with underscores and optionally converting to lowercase.

    Parameters:
        df (DataFrame): The dataframe whose headers to clean.
        lower_case (bool): Whether to convert headers to lowercase.

    Returns:
        DataFrame: The dataframe with cleaned headers.
    """
    
    originals = df.columns
    df.columns = df.columns.str.replace(r'[^a-zA-Z0-9_]', '_', regex=True)
    df.columns = df.columns.str.replace(r'__+', '_', regex=True)
    df.columns = df.columns.str.strip('_')
    if lower_case:
        df.columns = df.columns.str.lower()
        
    # Report changes made
    for i in range(len(originals)):
        if originals[i] != df.columns[i]:
            print(f'{originals[i]} --> {df.columns[i]}')

    return df

def find_problem_records(df):
    """
    Identifies records with leading or trailing whitespace.

    Parameters:
        df (DataFrame): The dataframe to check.

    Returns:
        DataFrame: Records with problematic data.
    """
    
    print("Finding records with leading or trailing whitespace.")

    problem_records = df[df.apply(lambda x: x.str.contains(r'^\s|\s$', na=False).any(), axis=1)]
    if problem_records.empty:
        print("No problem records found.")
    else:
        print("Problem records found:")
        return problem_records

def scrub_problem_records(df):
    """
    Removes leading and trailing whitespace from string fields in the dataframe.

    Parameters:
        df (DataFrame): The dataframe to clean.

    Returns:
        DataFrame: The cleaned dataframe.
    """
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    return df

def visualize_col(df, col_name):
    """
    Generates a bar plot for the value counts of a specified column.

    Parameters:
        df (DataFrame): The dataframe containing the column.
        col_name (str): The name of the column to visualize.
    """
    sns.barplot(x=df[col_name].value_counts().index, y=df[col_name].value_counts().values)
    plt.title(f"Value Counts for {col_name}")
    plt.ylabel("Counts")
    plt.xlabel(col_name)
    plt.xticks(rotation=45)
    plt.show()

def visualize_two_cols(df, col_name1, col_name2):
    """
    Generates a stacked bar plot for the counts of two categorical columns.

    Parameters:
        df (DataFrame): The dataframe containing the columns.
        col_name1 (str): The first column to group by.
        col_name2 (str): The second column to group by.
    """
    counts = df.groupby([col_name1, col_name2]).size().unstack(fill_value=0)
    counts.plot(kind='bar', stacked=True)
    plt.xlabel(col_name1)
    plt.ylabel('Number of Observations')
    plt.title(f'Observations by {col_name1} and {col_name2}')
    plt.xticks(rotation=45)
    plt.show()

