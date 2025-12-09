
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