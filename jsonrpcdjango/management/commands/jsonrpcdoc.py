from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
import sys
import json

import logging
log = logging.getLogger(__name__)


def render_template(template, meta):
    from django.template.loader import render_to_string
    return render_to_string(template, meta)



class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('service_path', nargs=1, type=str)
        parser.add_argument('-u', '--url', action='store', default='', dest='api_url',
                    help='API URL prefix')
        parser.add_argument('-f', '--format', action='store', default='html', dest='format',
                    help='Output format')
        parser.add_argument('-t', '--title', action='store', default='API', dest='title',
                    help='Title of generated document')

    def handle(self, *args, **options):
        service_path = options['service_path'][0]

        from jsonrpcdjango.loader import load_service_instance
        from jsonrpcserver.introspection import introspect

        service_meta = introspect(load_service_instance(service_path), 
                options['api_url'])
        ctx = {
                'service': service_meta,
                'title': options['title'],
                }
        template_name = 'jsonrpc/introspection.%s' % options['format']
        output = render_template(template_name, ctx)
        sys.stdout.write(output)
        sys.stdout.flush()

