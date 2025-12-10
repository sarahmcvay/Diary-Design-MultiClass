
class Diary():
    def __init__(self):
        self.entries = []
        # self.count = count 

    def add(self, entry):
        self.entries.append(entry)

    def all(self):
        return self.entries 
    
    def count_all_words(self):
        # total = 0
        # for entry in self.entries: 
        #     total += entry.count_words()
        # return total 
        word_counts = [entry.count_words() for entry in self.entries]
        return sum(word_counts)

    def reading_total_time(self, wpm):
        if self.entries == []:
            raise Exception("No entries added yet")
        word_count = self.count_all_words()
        return int(word_count / wpm)

    def find_best_entry_for_reading_time(self, wpm, minutes):
        words_user_can_read = int(wpm * minutes) 
        most_readable = None
        longest_found_so_far = 0
        for entry in self.entries: 
            if entry.count_words() <= words_user_can_read:
                if entry.count_words() > longest_found_so_far:
                    most_readable = entry
                    longest_found_so_far = entry.count_words()
        return most_readable


        # This returns an entry, but not necessarily the longest
        # readable_entries = []
        # for entry in self.entries: 
        #     if entry.count_words() <= words_user_can_read:
        #         readable_entries.append(entry)
        #         return sorted_entries[0]
        # Think there would be a way to sort
        # sorted_entries = readable_entries.sort()

        


        
