from django.db import migrations, models


def clear_duplicate_phones(apps, schema_editor):
    User = apps.get_model('users', 'User')
    phones = set()
    for user in User.objects.exclude(phone='').order_by('id'):
        if user.phone in phones:
            user.phone = ''
            user.save(update_fields=['phone'])
        else:
            phones.add(user.phone)


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_friendrequest'),
    ]

    operations = [
        migrations.RunPython(clear_duplicate_phones, migrations.RunPython.noop),
        migrations.AddConstraint(
            model_name='user',
            constraint=models.UniqueConstraint(
                condition=~models.Q(('phone', '')),
                fields=('phone',),
                name='unique_user_phone',
            ),
        ),
    ]
