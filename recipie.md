 ```python
 User story, the Diary, is able to look across all DiaryEntrys 
 provide the user with the best entry to read in the time available

TESTING 
"""
When two diary entries are made
We get a list of both diary entries
(integration)"""
    diary = Diary()
    contents_1 = DiaryEntry("Monday", "Today great")
    contents_2 = DiaryEntry("Tuesday", "Holiday really really fun fun")
    assert diary.all() == [contents_1, contents_2]

"""
When two diary entries are made
We can get total word count of both diary entries
(integration)"""
    diary = Diary()
    contents_1 = DiaryEntry("Monday", "Today was great")
    contents_2 = DiaryEntry("Tuesday", "Holiday really really fun fun")
    assert diary.count_words() == 10

"""
When two diary entries are made
we can get total reading time of both diaries 
(integration)"""
    diary = Diary()
    contents_1 = DiaryEntry("Monday", "Today was great")
    contents_2 = DiaryEntry("Tuesday", "Holiday really really fun fun")
    assert diary.reading_time(2) == 5



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

    def count_words(self):
        # Returns:      integer, number of words in all diary entries
    
    def reading_time(self, wpm):
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