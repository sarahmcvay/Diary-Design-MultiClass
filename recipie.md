 ```python
 User story, the Diary, is able to look across all DiaryEntrys 
 provide the user with the best entry to read in the time available

TESTING EXAMPLES
"""
When two diary entries are made
We get a list of both diary entries
(integration)"""
    diary = Diary()
    entry_1 = DiaryEntry("Monday", "Today great")
    entry_2 = DiaryEntry("Tuesday", "Holiday really really fun fun")
    assert diary.all() == [contents_1, contents_2]

"""
When two diary entries are made
We can get total word count of both diary entries
(integration)"""
    diary = Diary()
    entry_1 = DiaryEntry("Monday", "Today was great")
    entry_2 = DiaryEntry("Tuesday", "Holiday really really fun fun")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.count_words() == 10

"""
When two diary entries are given
we can get total reading time of both diaries entries
(integration)"""
    diary = Diary()
    entry_1 = DiaryEntry("Monday", "Today was great one two three")
    entry_2 = DiaryEntry("Tuesday", "Holiday is really fun")
    wpm = 2
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.reading_time(2) == 5

"""
When two diary entries are given one long one short, we can 
return the instance of diary entry which can be best read in the time the reader has
i.e. ignore the long one it is too long for the time we have. 
(integration)"""
    diary = Diary()
    entry_1 = DiaryEntry("Monday", "One two three")
    entry_2 = DiaryEntry("Tuesday", "One two three four five six seven")
    wpm = 2
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.find_best_entry_for_reading_time(2, 2) == entry_1

"""
When two diary entries are given, we will 
return most appropriate, so the longest, if we have time to read it
(integration)"""
    diary = Diary()
    entry_1 = DiaryEntry("Monday", "One two three")
    entry_2 = DiaryEntry("Tuesday", "One two three four five six seven")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.find_best_entry_for_reading_time(2, 5) == entry_2
#   (2, wpm ; 5, minutes to read) 

"""
When two diary entries are given, we will 
return most appropriate, so the longest, if we have time to read it
(integration)"""
def test_longest_entries_returned_if_time_to_read_the_entry_check():
    diary = Diary()
    entry_1 = DiaryEntry("Wednesday", "One two three four five six seven")
    entry_2 = DiaryEntry("Thursday", "One two three")
    entry_3 = DiaryEntry("Friday", "Fun day")
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    assert diary.find_best_entry_for_reading_time(2, 5) == entry_1 
#   (2, wpm ; 5, minutes to read) 

CLASS SIGNATURES 

class Diary:
    def __init__(self):
        # Parameters:   entry, on instance of DiaryEntry
        # Returns:      nothing
        # Side effects: adds the entry to the entries list 

    def add(self, entry):
        # Parameters: entry, an instance of DiaryEntry
        # Returns nothing
        # Side effects: adds entry to the entries list 
    
    def all(self):
        # Returns:      list of instances of DiaryEntry

    def count_all_words(self):
        # Returns:      integer, number of words in all diary entries
    
    def reading_total_time(self, wpm):
        # Parameters:   wpm, integer
        # Returns:      integer, estimate of reading time in minutes
        # if reader reads all diary entries

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:   wpm, integer 
        #               minutes, integer, number of minutes the reader has
        # Returns:      instance of DiaryEntry that is closest to the length the user could read
        # must not be over. 


class DiaryEntry: 
    def __init__(self, title, contents):
        # Parameters:   title and contents, both strings
        # Side Effects: sets title and contents properties 
    
    def count_words(self):
        # Returns:      integer, number of words in the contents
    
    def reading_time(self, wpm):
        # Parameters:   wpm, integer
        # Returns:      integer, reading time in minutes for the contents

    def reading_chunk(self, wpm, minutes):
        # Parameters:   wpm
        #               minutes, integer, numer of minutes the user has
        # Returns: string the user could read in given number of minutes
```