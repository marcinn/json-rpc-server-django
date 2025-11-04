from django.conf import settings
import django
from django.core.management import call_command
from django.core.management.base import CommandError
from django.test import TestCase
from io import StringIO
import sys

settings.configure(
    INSTALLED_APPS=[
        'jsonrpcdjango',
    ],
    SECRET_KEY='test',
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        }
    },
    TEMPLATES=[
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'APP_DIRS': True,
        },
    ]
)
django.setup()

class TestJsonRpcDoc(TestCase):

    def test_no_service_path(self):
        with self.assertRaises(CommandError):
            call_command('jsonrpcdoc')

    def test_too_many_service_paths(self):
        with self.assertRaises(CommandError):
            call_command('jsonrpcdoc', 'path1', 'path2')

    def test_html_format(self):
        out = StringIO()
        sys.stdout = out
        call_command('jsonrpcdoc', 'tests.test_service.service', format='html')
        sys.stdout = sys.__stdout__
        output = out.getvalue()
        self.assertIn('<h1>API</h1>', output)
        self.assertIn('<pre>add(a, b)</pre>', output)

    def test_tracwiki_format(self):
        out = StringIO()
        sys.stdout = out
        call_command('jsonrpcdoc', 'tests.test_service.service', format='tracwiki')
        sys.stdout = sys.__stdout__
        output = out.getvalue()
        self.assertIn('= API =', output)
        self.assertIn('<pre>add(a, b)</pre>', output)
