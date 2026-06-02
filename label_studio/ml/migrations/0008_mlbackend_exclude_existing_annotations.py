from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ml', '0007_auto_20240314_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='mlbackend',
            name='exclude_existing_annotations',
            field=models.BooleanField(
                default=False,
                help_text=(
                    'If true, during interactive preannotation only the tool-created prompt region will be sent to '
                    'the ML Backend. Other preexisting annotations will not be included in the request context.'
                ),
                verbose_name='exclude_existing_annotations',
            ),
        ),
    ]
