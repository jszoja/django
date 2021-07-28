from django.core.management import BaseCommand


class Command(BaseCommand):

    help = 'Test basic commands with suppress'
    requires_system_checks = []
    suppressed_base_arguments = {'--verbosity', '--traceback', '--settings', '--pythonpath', '--no-color', '--force-color',
                                 '--version'}

    def add_arguments(self, parser):
        parser.add_argument('args', nargs='*')

    def handle(self, *labels, **options):
        print('EXECUTE:WithSuppressCommand labels=%s, options=%s' % (labels, sorted(options.items())))
