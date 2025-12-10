from lib.diary_entry import *

"""
When the program initialises with a title and contents
We get the title and contents back
"""
def test_diary_entry_initialisation():
    diary_entry = DiaryEntry("Monday", "Today was great")
    assert diary_entry.title == "Monday"
    assert diary_entry.contents == "Today was great"

"""
Initialising with a three word entry, 
returns word count of three
(count_words)"""
def test_three_word_contents_returns_three():
    diary_entry = DiaryEntry("Monday", "Today was great")
    assert diary_entry.count_words() == 3

