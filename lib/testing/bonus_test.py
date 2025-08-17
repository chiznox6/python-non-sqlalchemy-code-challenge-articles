from classes.many_to_many import Author, Magazine, Article

class TestBonus:
    def test_topic_areas_returns_none_if_no_articles(self):
        a = Author("John Doe")
        assert a.topic_areas() is None

    def test_article_titles_returns_none_if_no_articles(self):
        m = Magazine("Tech", "Technology")
        assert m.article_titles() is None

    def test_contributing_authors_returns_none_if_no_qualifying_authors(self):
        a = Author("John Doe")
        m = Magazine("Tech", "Technology")
        a.add_article(m, "AI1")
        a.add_article(m, "AI2")
        result = m.contributing_authors()
        assert result is None

    def test_top_publisher_returns_magazine_with_most_articles(self):
        a = Author("John Doe")
        m1 = Magazine("Tech", "Technology")
        m2 = Magazine("Health", "Health")
        a.add_article(m1, "AI1")
        a.add_article(m1, "AI2")
        a.add_article(m2, "Nutrition")
        assert Magazine.top_publisher() == m1
