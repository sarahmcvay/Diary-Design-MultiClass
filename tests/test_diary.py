from lib.diary import *
import pytest

""" 
Initially there is an empty list of entries
(diary)"""
def test_initially_empty_list():
    diary = Diary()
    assert diary.all() == []

"""
Test initially word count is zero
(diary)"""
def test_initially_word_zero():
    diary = Diary()
    assert diary.count_all_words() == 0

"""
Initially reading total time should raise an error
"""
def test_initially_reading_time_raises_error():
    diary = Diary()
    with pytest.raises(Exception) as e:
        diary.reading_total_time(2)  #remember to add wpm to the test
    assert str(e.value) == "No entries added yet"

