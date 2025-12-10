class DiaryEntry: 
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents 
        self.entry = self.title + self.contents

    def count_words(self):
        return len(self.contents.split())

    def reading_time(self, wpm):
        self.wpm = wpm
        content_count = len((self.contents).split())
        return content_count / self.wpm