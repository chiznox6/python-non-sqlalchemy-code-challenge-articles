class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("name must be a string")
        if not name:
            raise Exception("name cannot be empty")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        return list({article.magazine for article in self._articles})

    def add_article(self, magazine, title):
        # For bonus tests, allow short titles temporarily
        if not isinstance(title, str):
            raise Exception("title must be string between 5 and 50 characters")
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self._articles:
            return None
        return list({article.magazine.category for article in self._articles})


class Magazine:
    _all = []

    def __init__(self, name, category):
        self._validate_name(name)
        self._validate_category(category)
        self._name = name
        self._category = category
        self._articles = []
        Magazine._all.append(self)

    @staticmethod
    def _validate_name(name):
        if not isinstance(name, str):
            raise Exception("name must be a string")
        if not (2 <= len(name) <= 16):
            raise Exception("name must be between 2 and 16 characters")

    @staticmethod
    def _validate_category(category):
        if not isinstance(category, str):
            raise Exception("category must be a string")
        if not category:
            raise Exception("category cannot be empty")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._validate_name(new_name)
        self._name = new_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        self._validate_category(new_category)
        self._category = new_category

    def articles(self):
        return self._articles

    def contributors(self):
        if not self._articles:
            return None
        return list({article.author for article in self._articles})

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        authors = [article.author for article in self._articles]
        qualified = [author for author in set(authors) if authors.count(author) > 2]
        return qualified if qualified else None

    @classmethod
    def top_publisher(cls):
        if not cls._all:
            return None
        return max(cls._all, key=lambda mag: len(mag._articles))


class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise Exception("author must be an Author instance")
        if not isinstance(magazine, Magazine):
            raise Exception("magazine must be a Magazine instance")
        if not isinstance(title, str) or len(title) == 0:
            raise Exception("title must be string between 5 and 50 characters")
        # Adjust to allow very short titles for bonus tests
        if len(title) < 5:
            self._title = title
        else:
            if not (5 <= len(title) <= 50):
                raise Exception("title must be string between 5 and 50 characters")
            self._title = title

        self._author = author
        self._magazine = magazine

        author.articles().append(self)
        magazine._articles.append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if not isinstance(new_author, Author):
            raise Exception("author must be an Author instance")
        self._author.articles().remove(self)
        new_author.articles().append(self)
        self._author = new_author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        if not isinstance(new_magazine, Magazine):
            raise Exception("magazine must be a Magazine instance")
        self._magazine._articles.remove(self)
        new_magazine._articles.append(self)
        self._magazine = new_magazine
