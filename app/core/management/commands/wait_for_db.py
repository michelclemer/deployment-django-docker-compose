"""
Django command to wait for the database to be available.
"""
import time

from django.core.management.base import BaseCommand
from django.db.utils import OperationalError
from psycopg2 import OperationalError as Pyscopg20pError


class Command(BaseCommand):
    """Django command to wait fr database."""

    def handle(self, *args, **options):
        """Entrypoint for command."""
        self.stdout.write("waiting for database...")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Pyscopg20pError, OperationalError):
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)
        self.stdout.write("Database ready!")