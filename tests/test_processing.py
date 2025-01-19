from src.processing import *

def test_filter_by_state_executed(dic_with_different_states, dic_with_expected_executed):
    assert filter_by_state(dic_with_different_states, 'EXECUTED') == dic_with_expected_executed

def test_filter_by_state_canceled(dic_with_different_states, dic_with_expected_canceled):
    assert filter_by_state(dic_with_different_states, 'CANCELED') == dic_with_expected_canceled

def test_sort_by_date_sorted_descend(dic_with_different_states, dic_with_expected_sorted_descent):
    assert sort_by_date(dic_with_different_states) == dic_with_expected_sorted_descent

def test_sort_by_date_sorted_ascend(dic_with_different_states, dic_with_expected_sorted_ascend):
    assert sort_by_date(dic_with_different_states, False) == dic_with_expected_sorted_ascend

def test_sort_by_date_sorted_ascend_dif_format(dic_with_different_date_format, dic_with_different_sorted_ascend_dif_format):
    assert sort_by_date(dic_with_different_date_format, False) == dic_with_different_sorted_ascend_dif_format

