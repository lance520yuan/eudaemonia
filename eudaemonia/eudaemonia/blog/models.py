from django.db import models


class Article(models.Model):
    blog_id = models.AutoField('ID',primary_key=True)
    blog_title = models.CharField(max_length=1000)
    blog_date = models.DateField(auto_now=True)
    blog_writer = models.CharField(max_length=300)
    blog_tags = models.CharField(max_length=100, default="others")
    blog_look = models.IntegerField(default=0)
    blog_website = models.ForeignKey("Website", on_delete=models.CASCADE)
    blog_neirong = models.TextField()

    def __str__(self):
        return self.blog_title


class Website(models.Model):
    website_name = models.CharField(max_length=20)
    website_id = models.AutoField('ID', primary_key=True)


class Commit(models.Model):
    commit_id = models.AutoField('ID', primary_key=True)
    commit_neirong =models.TextField()
    commit_time = models.DateField(auto_now=True)
    commit_blog = models.ForeignKey("Article", on_delete=models.CASCADE)
    commit_user = models.ForeignKey("User", on_delete=models.CASCADE)


class User(models.Model):

    def __str__(self):
        return self.user_name

    user_id = models.AutoField('ID', primary_key=True)
    user_name = models.CharField(max_length=10)
    user_email = models.EmailField(max_length=75)