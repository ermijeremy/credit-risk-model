import pytest
from credit-risk-model.src.tests.py import clean_amount

def test_clean_amount_removes_commas():
    assert clean_amount("1,000") == 1000.0
    assert clean_amount("12,345.67") == 12345.67

def test_clean_amount_handles_non_numeric():
    assert clean_amount("N/A") is None
    assert clean_amount("") is None
