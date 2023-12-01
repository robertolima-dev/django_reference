from django.contrib.auth.models import User

from apps.article.models import Article


class UpdateArticle:

    def __init__(self) -> None:
        self.owner_update = True

    def permisson_update(self, user: User, article: Article) -> bool:
        if user.id and article.author_id:
            return True
        else:
            return False
