from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
# Create your models here.

class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.SmallIntegerField(default=0)
    def update_rating(self):
        PostRat = self.post_set.aggregate(postRating=Sum('rating'))
        pRat = 0
        pRat += PostRat.get('postRating')

        CommRate = self.authorUser.comment_set.aggregate(commentRating=Sum('rating'))
        cRat = 0
        cRat += CommRate.get('commentRating')

        self.rating = pRat * 3 + cRat
        self.save()

class Category(models.Model):
    category = models.CharField(max_length=64, unique=True)

class Post(models.Model):
    postAuthor = models.ForeignKey(Author, on_delete=models.CASCADE)

    NEWS = 'NW'
    ARTICLE = 'AR'
    choose_post = (
        (NEWS, "Новость"),
        (ARTICLE, "Статья")
    )
    postType = models.CharField(max_length=2, choices=choose_post, default=ARTICLE)

    date_creation = models.DateTimeField(auto_now_add=True)
    postCategory = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=128)
    text = models.TextField()
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[0:123] + '...'


class PostCategory(models.Model):
    bondPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    bondCategory = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
