#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def ensure_mysql_database_exists():
    database_name = 'employee_db'
    user = 'root'
    password = 'jaihind'
    host = '127.0.0.1'
    port = 3306

    try:
        import MySQLdb

        connection = MySQLdb.connect(
            host=host,
            user=user,
            passwd=password,
            port=port,
            charset='utf8mb4',
        )
        cursor = connection.cursor()
        cursor.execute(
            f"CREATE DATABASE IF NOT EXISTS `{database_name}` "
            "CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"
        )
        cursor.close()
        connection.close()
    except Exception:
        pass


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'employee_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    ensure_mysql_database_exists()
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
