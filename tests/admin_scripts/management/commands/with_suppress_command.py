from django.core.management import BaseCommand
import argparse


class Command(BaseCommand):

    help = 'Test basic commands with suppress'
    requires_system_checks = []
    suppressed_base_arguments = {
        '-v', '--traceback', '--settings', '--pythonpath', '--no-color',
        '--force-color', '--version', 'file'
    }

    def add_arguments(self, parser):
        super().add_arguments(parser)

        def add_base_argument(parser, *args, **kwargs):
            """
            Call the parser's add_argument() method, suppressing the help text
            according to BaseCommand.suppressed_base_arguments.
            """
            for arg in args:
                if arg in self.suppressed_base_arguments:
                    kwargs['help'] = argparse.SUPPRESS
                    break
            parser.add_argument(*args, **kwargs)

        add_base_argument(parser, 'file', nargs='?', help='input file')

    def handle(self, *labels, **options):
        print('EXECUTE:WithSuppressCommand options=%s' % sorted(options.items()))
