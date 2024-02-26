import pytest
from list.list import list_filter

def test_list_filter():
    user_list = [1,'b', 3, 3, 5, 6, 'a', 'b', 'c']
    assert list_filter(user_list) == [1, 3, 3, 5, 6]

def test_list_filter_float():
    user_list = [1, 'b', 3.5, 3, 5, 6, 'a', 'b', 'c']
    assert list_filter(user_list) == [1, 3, 5, 6]

def test_empty_list():
    user_list = []
    assert list_filter(user_list) == []

def test_no_int():
    user_list = ['d', 'c', 'a', 4.2, 5.7]
    assert list_filter(user_list) == []

def test_all_int():
    user_list = [1, 6, 7, 9, 3]
    assert list_filter(user_list) == [1, 6, 7, 9, 3]

def test_zero():
    user_list = [0]
    assert list_filter(user_list) == [0]