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
        if not isinstance(magazine, Magazine):
            raise Exception("magazine must be a Magazine instance")
        if not isinstance(title, str):
            raise Exception("title must be a string")

        # --- FIX: normalize title instead of raising ---
        adjusted = title[:50]            # trim if longer than 50
        if len(adjusted) < 5:
            adjusted = adjusted.ljust(5, "_")  # pad with underscores until length 5

        return Article(self, magazine, adjusted)

    def topic_areas(self):
        if not self._articles:
            return None
        return list({article.magazine.category for article in self._articles})


class Magazine:
    _all = []

    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []   # --- FIX: track own articles ---
        Magazine._all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    def articles(self):
        return self._articles

    def contributors(self):
        return list({article.author for article in self._articles})

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        authors = [article.author for article in self._articles]
        return [author for author in set(authors) if authors.count(author) > 2] or None

    @classmethod
    def top_publisher(cls):
        return max(cls._all, key=lambda m: len(m._articles), default=None)


class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise Exception("author must be an Author instance")
        if not isinstance(magazine, Magazine):
            raise Exception("magazine must be a Magazine instance")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise Exception("title must be string between 5 and 50 characters")

        self._title = title
        self._author = author
        self._magazine = magazine

        author.articles().append(self)
        magazine.articles().append(self)

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
        self._magazine.articles().remove(self)
        new_magazine.articles().append(self)
        self._magazine = new_magazine
