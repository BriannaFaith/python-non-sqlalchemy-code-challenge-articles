class Article:
    all = []
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise Exception("Author must be of type Author.")
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be of type Magazine.")
        if not isinstance(title, str) or not 5 <= len(title) <= 50:
            raise Exception("Title must be between 5 and 50 characters.")
        self.author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)

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
        value.articles().append(self)

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        self._magazine = value
        value.articles().append(self)

class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Author name must be a non-empty string.")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        print("Before new articles", self._articles)
        existing_articles = [article for article in self._articles if article.magazine == magazine and article.title == title]
        if existing_articles:
            return existing_articles[0]

        new_article = Article(self, magazine, title)
        self._articles.append(new_article)
        print("After new article," , self._articles)
        return new_article

    def topic_areas(self):
        return list(set(article.magazine.category for article in self._articles.values())) if self._articles else None


class Magazine:
    def __init__(self, name, category):
        if not isinstance(name,str) and not (2 <= len(name) < 16):
            raise Exception("Name for magazine must be a string between 2 and 16 characters.")
        if not isinstance(category,str) and len(category) == 0:
            raise Exception("Category must be a non-empty string")

        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name
    @property
    def category(self):
        return self._category

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        author_count = {}
        for article in self._articles:
            author_count[article.author] = author_count.get(article.author, 0) + 1
        return [author for author, count in author_count.items() if count > 2]

author = Author("John Doe")
magazine = Magazine("Tech Magazine", "Technology")
article = author.add_article(magazine, 'C Programming')
article.magazine = magazine
author = Author("Carry Bradshaw")
magazine_1 = Magazine("Vogue", "Fashion")
magazine_2 = Magazine("AD", "Architecture & Design")

print("Article Title:", article.title)
print("Article Author:", article.author.name)
print("Article Magazine:", article.magazine.name)
print("Article Category:", article.magazine.category)