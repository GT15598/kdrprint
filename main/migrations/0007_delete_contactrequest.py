from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_contactrequest'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ContactRequest',
        ),
    ]