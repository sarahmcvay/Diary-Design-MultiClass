from lib.diary import *
from lib.diary_entry import *

"""
When two diary entries are made
We get a list of both diary entries
(integration)"""
def test_two_diary_entries_creates_list_of_both_in_diary():
    diary = Diary()
    entry_1 = DiaryEntry("Monday", "Today great")
    entry_2 = DiaryEntry("Tuesday", "Holiday really really fun fun")
    diary.add(entry_1)
    diary.add(entry_2)
    result = diary.all()
    assert result == [entry_1, entry_2]