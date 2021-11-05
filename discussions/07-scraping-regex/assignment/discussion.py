# discussion.py


import os
import numpy as np
import pandas as pd
import requests
import time
from bs4 import BeautifulSoup
import re


# ---------------------------------------------------------------------
# QUESTION 1
# ---------------------------------------------------------------------


def get_website_urls():
    """
    Get all the website URLs

    :Example:
    >>> urls = get_website_urls()
    >>> len(urls)
    50
    >>> 'catalogue' in urls[0]
    True
    """
    ...


# ---------------------------------------------------------------------
# QUESTION 2
# ---------------------------------------------------------------------


def book_categories():
    """
    Get all the book categories and return them as a list

    :Example:
    >>> categories = book_categories()
    >>> len(categories)
    50
    >>> 'Classics' in categories
    True
    """
    ...


# ---------------------------------------------------------------------
# QUESTION 3
# ---------------------------------------------------------------------


def duplicate_words(s):
    """
    Provide a list of all words that are duplicates in an input sentence.
    Assume that the sentences are lower case.

    :Example:
    >>> duplicate_words('let us plan for a horror movie movie this weekend')
    ['movie']
    >>> duplicate_words('I like surfing')
    []
    >>> duplicate_words('the class class is good but the tests tests are hard')
    ['class', 'tests']
    """
    ...


# ---------------------------------------------------------------------
# QUESTION 4
# ---------------------------------------------------------------------


def laptop_details(df):
    """
    Given a df with product description - Return df with added columns of 
    processor (i3, i5), generation (9th Gen, 10th Gen), 
    storage (512 GB SSD, 1 TB HDD), display_in_inch (15.6 inch, 14 inch)

    :Example:
    >>> df = pd.read_csv('data/laptop_details.csv')
    >>> new_df = laptop_details(df)
    >>> new_df.shape
    (21, 5)
    >>> new_df['processor'].nunique()
    3
    """
    ...
