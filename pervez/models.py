from django.db import models
from embed_video.fields import EmbedVideoField
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Cls(models.Model):
    img = models.CharField(max_length=200, null=True, blank=True)
    quote = models.TextField(null=True, blank=True)
    clss = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.clss)


class Subject(models.Model):
    sub_type = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.sub_type

class Notes(models.Model):
    clss = models.ForeignKey(Cls, null=True, on_delete=models.CASCADE)
    sub = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    notes = models.CharField(max_length=200, null=True)
    notesfile = models.FileField(null=True)

    def __str__(self):
        return self.notes + " " + str(self.clss)

class QuestionAnswer(models.Model):
    clss = models.ForeignKey(Cls, on_delete=models.CASCADE)
    sub = models.ForeignKey(Subject, null=True, on_delete=models.CASCADE)
    question_desc = models.CharField(max_length=200, null=True)
    question = models.FileField(null=True, blank=True)
    answer_desc = models.CharField(max_length=200, null=True, blank=True)
    answers = models.FileField(null=True, blank=True)


    def __str__(self):
        return "qna "+ str(self.sub) + " " + str(self.clss)


class Lecture_chapter(models.Model):
    chapter = models.CharField(max_length=200, null=True, blank=True)
    clss = models.ForeignKey(Cls, on_delete=models.CASCADE, null=True,  blank=True)
    sub = models.ForeignKey(Subject, on_delete=models.CASCADE, max_length=200, null=True)

    def __str__(self):
        return self.chapter + " " + str(self.clss)

class SubTopic(models.Model):
    chapter = models.ForeignKey(Lecture_chapter, null=True, on_delete=models.CASCADE)
    sub_topic = models.CharField(max_length=200, null=True, blank=True)
    extras = RichTextUploadingField(null=True, blank=True)
    vedio = EmbedVideoField(null=True, blank=True)

    def __str__(self):
        return str(self.chapter) + self.sub_topic

class Recommendations(models.Model):
    title = models.CharField(max_length=200, null=True)
    vedio = EmbedVideoField(null=True, blank=True)

    def __str__(self):
        return str(self.title) + 'Vedio'

class Blogs(models.Model):
    title = models.CharField(max_length=200)
    short_content = models.TextField(null=True)
    url = models.CharField(max_length=500)

    def __str__(self):
        return str(self.title) + " - Blog"