class DiaryEntry: 
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents 
        self.entry = self.title + self.contents

    def count_words(self):
        return len(self.contents.split())