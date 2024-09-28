# Generated by Django 4.2.5 on 2024-05-07 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GESTION', '0002_remove_demande_stagiaire_id_admin_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clients',
            name='id_admin',
        ),
        migrations.RemoveField(
            model_name='clients',
            name='id_contrat',
        ),
        migrations.RemoveField(
            model_name='contrat',
            name='id_admin',
        ),
        migrations.RemoveField(
            model_name='demande_stagiaire',
            name='id_formation',
        ),
        migrations.RemoveField(
            model_name='demande_stagiaire',
            name='id_utilisateur',
        ),
        migrations.RemoveField(
            model_name='document_important',
            name='id_admin',
        ),
        migrations.RemoveField(
            model_name='employes',
            name='id_admin',
        ),
        migrations.RemoveField(
            model_name='employes',
            name='id_categories',
        ),
        migrations.RemoveField(
            model_name='employes',
            name='id_contrat',
        ),
        migrations.RemoveField(
            model_name='projet',
            name='id_admin',
        ),
        migrations.RemoveField(
            model_name='salaire',
            name='id_admin',
        ),
        migrations.RemoveField(
            model_name='stagiaires',
            name='id_admin',
        ),
        migrations.RemoveField(
            model_name='stagiaires',
            name='id_formation',
        ),
        migrations.DeleteModel(
            name='Administrateur',
        ),
        migrations.DeleteModel(
            name='Categories',
        ),
        migrations.DeleteModel(
            name='Clients',
        ),
        migrations.DeleteModel(
            name='Contrat',
        ),
        migrations.DeleteModel(
            name='Demande_stagiaire',
        ),
        migrations.DeleteModel(
            name='document_important',
        ),
        migrations.DeleteModel(
            name='Employes',
        ),
        migrations.DeleteModel(
            name='Formations',
        ),
        migrations.DeleteModel(
            name='Projet',
        ),
        migrations.DeleteModel(
            name='Salaire',
        ),
        migrations.DeleteModel(
            name='Stagiaires',
        ),
        migrations.DeleteModel(
            name='Utilisateur',
        ),
    ]
