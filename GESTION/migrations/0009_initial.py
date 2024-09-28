# Generated by Django 4.2.5 on 2024-05-07 21:03

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('GESTION', '0008_remove_clients_id_admin_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_categories', models.CharField(max_length=20, unique=True)),
                ('description', models.TextField()),
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
                ('date_add', models.DateTimeField(auto_now=True)),
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
                ('photo_profil', models.ImageField(blank=True, null=True, upload_to='document')),
                ('piece_identite', models.FileField(blank=True, null=True, upload_to='document')),
                ('date_add', models.DateTimeField(auto_now=True)),
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
                ('date_add', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=35, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=15)),
                ('date_add', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Administrateur_g',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
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
                ('date_add', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
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
                ('date_add', models.DateTimeField(auto_now=True)),
                ('id_admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('id_formation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='GESTION.formations')),
            ],
        ),
        migrations.CreateModel(
            name='Salaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salaire', models.CharField(max_length=20)),
                ('id_employe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GESTION.employes')),
            ],
        ),
        migrations.CreateModel(
            name='Projet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_projet', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('date_add', models.DateTimeField(auto_now=True)),
                ('id_admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='employes',
            name='id_admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='employes',
            name='id_categories',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='GESTION.categories'),
        ),
        migrations.CreateModel(
            name='Document_important',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_document', models.CharField(max_length=100)),
                ('piece_document', models.FileField(blank=True, null=True, upload_to='document')),
                ('date_add', models.DateTimeField(auto_now=True)),
                ('id_admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
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
                ('date_add', models.DateTimeField(auto_now=True)),
                ('id_formation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GESTION.formations')),
                ('id_utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GESTION.utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='Contratemployes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_contrat', models.CharField(max_length=20)),
                ('code_contrat', models.CharField(max_length=7, unique=True)),
                ('lettre_commande', models.FileField(blank=True, null=True, upload_to='document')),
                ('date_add', models.DateTimeField(auto_now=True)),
                ('id_employe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GESTION.employes')),
            ],
        ),
        migrations.CreateModel(
            name='Contratclients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_contrat', models.CharField(max_length=20)),
                ('code_contrat', models.CharField(max_length=7, unique=True)),
                ('lettre_commande', models.FileField(blank=True, null=True, upload_to='document')),
                ('date_add', models.DateTimeField(auto_now=True)),
                ('id_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GESTION.clients')),
            ],
        ),
        migrations.AddField(
            model_name='clients',
            name='id_admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
