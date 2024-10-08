# Generated by Django 4.2.5 on 2024-05-13 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GESTION', '0014_alter_categories_nom_categories'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='administrateur_g',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='categories',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='clients',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='contratclients',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='contratemployes',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='demande_stagiaire',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='document_important',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='employes',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='formations',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='projet',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='salaire',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='stagiaires',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='utilisateur',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='employes',
            name='id_categories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GESTION.categories'),
        ),
    ]
