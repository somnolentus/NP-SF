from django.core.management.base import BaseCommand, CommandError
from news.models import Category, Post


class Command(BaseCommand):
    help = 'Wipes all posts in a category'

    def add_arguments(self, parser):
        parser.add_argument('category', type=str)

    def handle(self, *args, **kwargs):
        answer = input(f'Вы правда хотите удалить все статьи в категории {kwargs["category"]}? [yes/no]')

        if answer != 'yes':
            self.stdout.write(self.style.ERROR('Отмена операции'))

        try:
            category = Category.objects.get(name=kwargs["category"])
            Post.objects.filter(category=category).delete()
            self.stdout.write(self.style.SUCCESS(f'All posts in {category.name} category have been deleted.'))
        except Post.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Could not find category'))