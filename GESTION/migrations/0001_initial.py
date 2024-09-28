# Generated by Django 4.2.5 on 2024-05-06 11:30

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=25)),
                ('prenom', models.CharField(max_length=30)),
                ('email', models.EmailField(default='guru@guruacademy.xyz', max_length=254, unique=True)),
                ('telephone', models.CharField(max_length=20)),
                ('quartier', models.CharField(max_length=15)),
                ('ville', models.CharField(max_length=16)),
                ('pays', models.CharField(max_length=15)),
                ('CNI', models.CharField(max_length=50)),
                ('passport', models.CharField(default='none', max_length=25)),
                ('matricule', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('mot_de_passe', models.CharField(default='guru@2025', max_length=25)),
                ('photo_profil', models.ImageField(blank=True, null=True, upload_to='document')),
                ('piece_identite', models.FileField(blank=True, null=True, upload_to='document')),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_categories', models.CharField(max_length=20, unique=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Contrat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_contrat', models.CharField(max_length=20)),
                ('code_contrat', models.CharField(max_length=7, unique=True)),
                ('lettre_commande', models.FileField(blank=True, null=True, upload_to='document')),
                ('id_admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GESTION.administrateur')),
            ],
        ),
        migrations.CreateModel(
            name='Formations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_formation', models.CharField(max_length=35)),
                ('description', models.TextField()),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=35, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Stagiaires',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=25)),
                ('prenom', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telephone', models.CharField(max_length=20)),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
                ('id_admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GESTION.administrateur')),
                ('id_formation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='GESTION.formations')),
            ],
        ),
        migrations.CreateModel(
            name='Salaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salaire', models.CharField(max_length=20)),
                ('id_admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GESTION.administrateur')),
            ],
        ),
        migrations.CreateModel(
            name='Projet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_projet', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('id_admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GESTION.administrateur')),
            ],
        ),
        migrations.CreateModel(
            name='Employes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=25)),
                ('prenom', models.CharField(max_length=30)),
                ('email', models.EmailField(default='employes@guruacademy.xyz', max_length=254, unique=True)),
                ('telephone', models.CharField(max_length=20)),
                ('quartier', models.CharField(max_length=15)),
                ('ville', models.CharField(max_length=16)),
                ('pays', models.CharField(max_length=15)),
                ('CNI', models.CharField(max_length=50)),
                ('passport', models.CharField(default='none', max_length=25)),
                ('matricule', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('mot_de_passe', models.CharField(default='employes@2025', max_length=25)),
                ('photo_profil', models.ImageField(blank=True, null=True, upload_to='document')),
                ('piece_identite', models.FileField(blank=True, null=True, upload_to='document')),
                ('id_admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GESTION.administrateur')),
                ('id_categories', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='GESTION.categories')),
                ('id_contrat', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='GESTION.contrat')),
            ],
        ),
        migrations.CreateModel(
            name='document_important',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_document', models.CharField(max_length=100)),
                ('piece_document', models.FileField(blank=True, null=True, upload_to='document')),
                ('id_admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GESTION.administrateur')),
            ],
        ),
        migrations.CreateModel(
            name='Demande_stagiaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=40)),
                ('prenom', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(max_length=30)),
                ('motif_stage', models.CharField(max_length=200)),
                ('lettre_stage', models.FileField(blank=True, null=True, upload_to='document')),
                ('validation', models.CharField(default='En attente', max_length=20)),
                ('message', models.TextField()),
                ('id_admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GESTION.administrateur')),
                ('id_formation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GESTION.formations')),
            ],
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(default='none', max_length=25)),
                ('prenom', models.CharField(default='none', max_length=30)),
                ('nom_entreprise', models.CharField(default='none', max_length=25)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telephone', models.CharField(max_length=20)),
                ('quartier', models.CharField(max_length=15)),
                ('ville', models.CharField(max_length=16)),
                ('pays', models.CharField(max_length=15)),
                ('CNI', models.CharField(default='none', max_length=50)),
                ('code_NIF', models.CharField(default='none', max_length=35, unique=True)),
                ('photo_profil', models.ImageField(blank=True, default='none', null=True, upload_to='document')),
                ('piece_identite', models.FileField(blank=True, default='none', null=True, upload_to='document')),
                ('id_admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GESTION.administrateur')),
                ('id_contrat', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='GESTION.contrat')),
            ],
        ),
    ]