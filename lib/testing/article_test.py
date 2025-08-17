import pytest
from classes.many_to_many import Author, Magazine, Article

class TestArticle:
    def test_article_has_title_author_magazine(self):
        a = Author("John Doe")
        m = Magazine("Tech", "Technology")
        art = Article(a, m, "AI Advances")
        assert art.title == "AI Advances"
        assert art.author == a
        assert art.magazine == m

    def test_title_must_be_string_between_5_and_50_chars(self):
        a = Author("John Doe")
        m = Magazine("Tech", "Technology")
        with pytest.raises(Exception):
            Article(a, m, "No")
        with pytest.raises(Exception):
            Article(a, m, "T"*60)

    def test_title_is_immutable(self):
        a = Author("John Doe")
        m = Magazine("Tech", "Technology")
        art = Article(a, m, "AI Advances")
        with pytest.raises(AttributeError):
            art.title = "Changed"

    def test_author_must_be_author_instance(self):
        m = Magazine("Tech", "Technology")
        with pytest.raises(Exception):
            Article("NotAuthor", m, "AI Advances")

    def test_magazine_must_be_magazine_instance(self):
        a = Author("John Doe")
        with pytest.raises(Exception):
            Article(a, "NotMagazine", "AI Advances")
