class Publication:
    def __init__(self, title, author):
        self._title = title
        self._author = author

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}"


class Book(Publication):
    def __init__(self, title, author, number_of_pages):
        super().__init__(title, author)
        self.number_of_pages = number_of_pages

    @property
    def number_of_pages(self):
        return self._number_of_pages

    @number_of_pages.setter
    def number_of_pages(self, value):
        if value <= 0:
            print("The number of pages must be positive")
            self._number_of_pages = 0
        else:
            self._number_of_pages = value

    def display_info(self):
        super().display_info()
        print(f"Number of Pages: {self.number_of_pages}")

    def __str__(self):
        return f"{super().__str__()}\nNumber of Pages: {self.number_of_pages}"


class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.issue_number = issue_number

    @property
    def issue_number(self):
        return self._issue_number

    @issue_number.setter
    def issue_number(self, value):
        if value <= 0:
            print("The issue number must be positive")
            self._issue_number = 0
        else:
            self._issue_number = value

    def display_info(self):
        super().display_info()
        print(f"Issue Number: {self.issue_number}")

    def __str__(self):
        return f"{super().__str__()}\nIssue Number: {self.issue_number}"


# Create objects
publication1 = Publication("School Rules", "Principal Johnson")
publication2 = Publication("Teacher Handbook", "School Office")

book1 = Book("Python Programming", "John Smith", 320)
book2 = Book("Science Explorer", "Maria Lopez", 0)

magazine1 = Magazine("Tech Weekly", "Emma Brown", 12)
magazine2 = Magazine("Campus News", "David Lee", -2)

# Display information
materials = [publication1, publication2, book1, book2, magazine1, magazine2]

for item in materials:
    print(f"{type(item).__name__}:")
    print(item)
    print("-" * 30) 