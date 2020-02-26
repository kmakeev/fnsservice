from fns.classes import parse_folder
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
import os


class Command(BaseCommand):
    help = "Import XML from default folder"

    def handle(self, *args, **options):
        in_dir = os.path.join(settings.BASE_DIR, '..\\data\\in')
        out_dir = os.path.join(settings.BASE_DIR, '..\\data\\out')
        parse_folder(in_dir, out_dir)

