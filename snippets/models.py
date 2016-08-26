from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    """
    Model containing a code snippet.

    Fields:
    created - Creation date autopoplulated with now.
    title - User provided title for the snippet.
    code - Code text making up the body of the snippet.
    linenos - Boolean for displaying/hiding line numbers in the snippet.
    language - Coding language of the snippet.
    style - Pygmentize formatting style for the snippet.
    """
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    def __str__(self):
        if self.title:
            return self.title
        else:
            return self

    class Meta:
        """
        Provides field to use for ordering upon data retrieval.
        """
        ordering = ('created',)
