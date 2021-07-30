from django.core.management import BaseCommand


class Command(BaseCommand):

    help = 'Test basic commands with suppress'
    requires_system_checks = []
    suppressed_base_arguments = {
        '-v', '--traceback', '--settings', '--pythonpath', '--no-color',
        '--force-color', '--version'
    }

    def handle(self, *labels, **options):
        print('EXECUTE:WithSuppressCommand options=%s' % sorted(options.items()))
