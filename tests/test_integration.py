from lib.diary import *
from lib.diary_entry import *

"""
When two diary entries are made
We get a list of both diary entries
(integration)"""
def test_two_diary_entries_creates_list_of_both_in_diary():
    diary = Diary()
    entry_1 = DiaryEntry("Monday", "Today was great one two three")
    entry_2 = DiaryEntry("Tuesday", "Holiday really fun four five six")
    diary.add(entry_1)
    diary.add(entry_2)
    result = diary.all()
    assert result == [entry_1, entry_2]

"""
When two diary entries are made
We can get total word count of both contents diary entries
(integration)"""
def test_two_entries_returns_total_word_count():
    diary = Diary()
    entry_1 = DiaryEntry("Monday", "Today was great one two three")
    entry_2 = DiaryEntry("Tuesday", "Holiday really fun four five six")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.count_all_words() == 12

"""
When two diary entries are given
we can get total reading time of both diaries entries
(integration)
"""
def test_get_total_reading_time_of_both_entries():
    diary = Diary()
    entry_1 = DiaryEntry("Monday", "Today was great one two three")
    entry_2 = DiaryEntry("Tuesday", "Holiday is really fun")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.reading_total_time(2) == 5

"""
When two diary entries are given, we can 
return the instance of diary entry which can be best read in the time the reader has
(integration)"""
def test_best_reading_time_found():
    diary = Diary()
    entry_1 = DiaryEntry("Monday", "One two three")
    entry_2 = DiaryEntry("Tuesday", "One two three four five six seven")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.find_best_entry_for_reading_time(2, 2) == entry_1