from django.core.management.templates import TemplateCommand
import inflection


class Command(TemplateCommand):
    help = (
        "Creates CRUD api structure for the given api name in the current directory."
        )
    missing_args_message = "You must provide an application name."

    def add_arguments(self, parser):
        parser.add_argument('name', help='Name of the api.')
        parser.add_argument('directory', nargs='?', help='Optional destination directory')
        parser.add_argument('--template', help='The path or URL to load the template from.')
        parser.add_argument(
            '--extension', '-e', dest='extensions',
            action='append', default=['py'],
            help='The file extension(s) to render (default: "py"). '
                 'Separate multiple extensions with commas, or use '
                 '-e multiple times.'
        )
        parser.add_argument(
            '--name', '-n', dest='files',
            action='append', default=[],
            help='The file name(s) to render. Separate multiple file names '
                 'with commas, or use -n multiple times.'
        )

    def handle(self, **options):
        app_name = options.pop('name')
        target = options.pop('directory')
        class_name = inflection.camelize(app_name)
        plural_app_name = inflection.pluralize(app_name)
        api_name = app_name.split("_")
        model_name = ''.join(api_name)
        single_resource_name = ' '.join(api_name).capitalize()
        plural_resource_name = inflection.pluralize(single_resource_name)

        options['single_resource_name'] = single_resource_name
        options['model_name'] = model_name
        options['class_name'] = class_name
        options['plural_app_name'] = plural_app_name
        options['plural_resource_name'] = plural_resource_name
        if options['template'] is None:
            options['template'] = 'connect_api_templates/app_template'

        super().handle('app', app_name, target, **options)
