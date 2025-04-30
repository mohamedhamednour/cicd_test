# app/tests/test_payment_features.py
import pytest


@pytest.mark.django_db
def test_sum():

    assert 1 + 1 == 2
    assert 2 + 2 == 4
