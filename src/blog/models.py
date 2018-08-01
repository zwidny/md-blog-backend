from django.db import models
from django.utils.translation import gettext as _
from .managers import BlogManager


class Blog(models.Model):
    owner = models.CharField(verbose_name=_("作者ID"), max_length=63, db_index=True)
    content = models.TextField(verbose_name=_("内容"))
    created = models.DateTimeField(verbose_name=_("创建时间"), auto_now_add=True)
    modified = models.DateTimeField(verbose_name=_("修改时间"), auto_now=True)
    objects = BlogManager()
