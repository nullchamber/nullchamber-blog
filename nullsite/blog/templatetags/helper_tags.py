from django import template, forms
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.db.models import Count
import markdown
from ..models import Post

register = template.Library()


@register.filter
def format_post(post_text):
    paragraphs = post_text.split('\n')
    paragraphs = list(filter(lambda p: len(p) > 0, paragraphs))
    paragraphs = [p.replace('\t', '<p class="brand-dark">') for p in paragraphs]
    article = "</p>".join(paragraphs)
    return format_html(article)


@register.filter
def format_label(field_obj, classes):
    label = field_obj.label
    id_for_label = field_obj.id_for_label or ""
    return format_html(f'<label for="{id_for_label}" class="{classes}">{label}</label>')


@register.filter
def add_widget_css(form_field, css_class):
    classes = form_field.field.widget.attrs.get('class', '')
    return form_field.as_widget(attrs={'class': f"{classes} {css_class}"})


@register.filter
def is_textarea(form_field):
    return isinstance(form_field, forms.Textarea)
    

@register.simple_tag
def total_posts():
    return Post.published.count()


@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(
        total_comments=Count('comments')
    ).order_by('-total_comments')[:count]


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))


@register.inclusion_tag('blog/indev_modal.html')
def create_indev_modal(element_id):
    feature_name = element_id.split('-')[0].capitalize()
    return {'element_id': element_id, 'feature': feature_name}