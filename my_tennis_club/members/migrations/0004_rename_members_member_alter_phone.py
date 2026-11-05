from django.db import migrations, models


class Migration(migrations.Migration):
    """Rename the model to singular `Member`, store phone numbers as text, and add default ordering."""

    dependencies = [
        ("members", "0003_members_joined_date_members_phone"),
    ]

    operations = [
        migrations.RenameModel(old_name="members", new_name="Member"),
        migrations.AlterModelOptions(name="member", options={"ordering": ["lastname", "firstname"]}),
        migrations.AlterField(
            model_name="member",
            name="phone",
            field=models.CharField(blank=True, default="", max_length=20),
        ),
        migrations.AlterField(
            model_name="member",
            name="joined_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]
