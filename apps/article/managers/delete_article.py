from django.contrib.auth.models import User

from apps.article.models import Article


class DeleteArticle:

    def __init__(self) -> None:
        self.owner_delete = True

    def permisson_delete(self, user: User, article: Article) -> bool:
        if user.id and article.author_id:
            return True
        else:
            return False
