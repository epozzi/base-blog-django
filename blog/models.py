from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
from django.db import models


class Posts(models.Model):

    CATEGORY_OPTIONS = [
        (1, 'Reviews' ),
        (2, 'Tutoriais'),
        (3, 'Dicas'),
        (4, 'Resultados'),
        (5, 'Pessoal')
    ]

    title = models.CharField(max_length=255, null=False, blank=False)
    sumary = RichTextField(null=False, blank=False)
    content = RichTextUploadingField(null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    category = MultiSelectField(choices=CATEGORY_OPTIONS, max_choices=5, max_length=10, null=False)
    publish = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title