from django.db import models
from django.db.models import Sum, Count
from django.contrib.auth.models import User

class QuestionManager(models.Manager):
    def popular(self):
        return self.prefetch_related('likes', 'author').order_by('-rating')

    def new(self):
        return self.prefetch_related('likes', 'author').order_by('-date')

    def with_tag(self, str):
        return self.prefetch_related('likes', 'author').filter(tags__name=str)

    def find_str(self, str):
        return self.prefetch_related('likes', 'author').filter(title=str)



class AnswerManager(models.Manager):
    def all(self, pk):
        return self.prefetch_related('likes', 'author').filter(question__id=pk).annotate(like_sum=Sum('likes__like'))


class TagManager(models.Manager):
    def popular(self):
        return self.annotate(count=Count('questions')).order_by('-count')


class ProfileManager(models.Manager):
    def best_answers(self):
        return self.annotate(count=Count('answers')).order_by('-count')



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True)

    objects = ProfileManager()

    def __str__(self):
        return self.user.__str__()

class Question(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='questions')
    text =  models.CharField(max_length=5000)
    rating = models.IntegerField(default=0, db_index=True)
    date = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', related_name='questions', blank=True)

    objects = QuestionManager()

    def __str__(self):
        return self.title


class Answer(models.Model):
    text =  models.CharField(max_length=5000)
    date = models.DateField(auto_now_add=True)
    correct = models.BooleanField(default=False)
    author = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='answers')

    objects = AnswerManager()
   
    def __str__(self):
        return self.text

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    objects = TagManager()

    def __str__(self):
        return self.name


class QuestionLikes(models.Model):
    LIKE_CHOICES = (('like', '1'), ('dis', '-1'))
    like = models.IntegerField(choices=LIKE_CHOICES, default=0)
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='likes')
    author = models.ForeignKey('Profile', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.like) + ' ' + self.question.__str__()


class AnswerLikes(models.Model):
    LIKE_CHOICES = (('like', '1'), ('dis', '-1'))
    like = models.IntegerField(choices=LIKE_CHOICES, default=0)
    answer = models.ForeignKey('Answer', on_delete=models.CASCADE, related_name='likes')
    author = models.ForeignKey('Profile', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.like) + ' ' + self.answer.__str__()
