import pytest

from classes.many_to_many import Article
from classes.many_to_many import Magazine
from classes.many_to_many import Author


class TestAuthor:
    """Author in many_to_many.py"""

    def test_has_name(self):
        """Author is initialized with a name"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine = Magazine("Vogue", "Fashion")
        Article(author_1, magazine, "How to wear a tutu with style")
        Article(author_2, magazine, "Dating life in NYC")

        assert author_1.name == "Carry Bradshaw"
        assert author_2.name == "Nathaniel Hawthorne"

    def test_name_is_immutable(self):
        a = Author("John Doe")
        with pytest.raises(AttributeError):
            a.name = "Jane"

    def test_articles_returns_list(self):
        a = Author("John Doe")
        m = Magazine("Tech", "Technology")
        Article(a, m, "AI Advances")
        Article(a, m, "Robotics")
        assert isinstance(a.articles(), list)
        assert all(isinstance(i, Article) for i in a.articles())

    def test_magazines_returns_unique_list(self):
        a = Author("John Doe")
        m1 = Magazine("Tech", "Technology")
        m2 = Magazine("HealthMag", "Health")
        Article(a, m1, "AI Advances")
        Article(a, m2, "Nutrition")
        assert m1 in a.magazines()
        assert m2 in a.magazines()
        assert len(a.magazines()) == 2

    def test_add_article_creates_article(self):
        a = Author("John Doe")
        m = Magazine("Tech", "Technology")
        new_article = a.add_article(m, "New AI")
        assert isinstance(new_article, Article)
        assert new_article in a.articles()

    def test_topic_areas_returns_unique_categories(self):
        a = Author("John Doe")
        m1 = Magazine("Tech", "Technology")
        m2 = Magazine("HealthMag", "Health")
        a.add_article(m1, "AI Advances")
        a.add_article(m2, "Nutrition")
        assert "Technology" in a.topic_areas()
        assert "Health" in a.topic_areas()
