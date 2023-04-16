# Generated by Django 3.1.14 on 2022-12-21 10:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('citizenship', models.CharField(blank=True, max_length=20, null=True)),
                ('address_type', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=20, null=True)),
                ('city', models.CharField(blank=True, max_length=20, null=True)),
                ('pincode', models.IntegerField(blank=True, null=True)),
                ('state', models.CharField(blank=True, max_length=20, null=True)),
                ('country', models.CharField(blank=True, max_length=20, null=True)),
                ('update_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', models.FileField(blank=True, null=True, upload_to='media/profile_photo')),
                ('primary_contact', models.IntegerField(blank=True)),
                ('alternate_contact', models.IntegerField(blank=True)),
                ('dob', models.DateTimeField(max_length=10)),
                ('mother_tounge', models.CharField(max_length=10)),
                ('location', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=10)),
                ('marital_status', models.CharField(max_length=10)),
                ('about_profile', models.CharField(max_length=100)),
                ('main_origin', models.CharField(max_length=50)),
                ('otp', models.PositiveIntegerField()),
                ('update_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('address', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myfirstapp.address')),
            ],
        ),
        migrations.CreateModel(
            name='Customer_expectation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exp_min_age', models.IntegerField()),
                ('exp_max_age', models.IntegerField()),
                ('exp_height', models.FloatField(max_length=20)),
                ('exp_marital_status', models.CharField(max_length=20)),
                ('exp_mother_tounge', models.CharField(max_length=20)),
                ('exp_eating_habit', models.CharField(max_length=20)),
                ('exp_smoking_habbit', models.CharField(max_length=20)),
                ('exp_drinking_habbit', models.CharField(max_length=20)),
                ('exp_religion', models.CharField(max_length=20)),
                ('exp_caste', models.CharField(max_length=20)),
                ('exp_subcaste', models.CharField(max_length=20)),
                ('exp_star', models.CharField(max_length=20)),
                ('exp_dosh', models.CharField(max_length=20)),
                ('exp_rashi', models.CharField(max_length=20)),
                ('exp_mangalik', models.CharField(max_length=20)),
                ('exp_education', models.CharField(max_length=20)),
                ('exp_city', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Family_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_member_in_family', models.PositiveIntegerField(blank=True, null=True)),
                ('relationship', models.CharField(max_length=20)),
                ('married_status', models.CharField(max_length=20)),
                ('profession', models.CharField(max_length=20)),
                ('family_type', models.CharField(max_length=20)),
                ('education', models.CharField(max_length=20)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Photo_id',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_id', models.IntegerField()),
                ('status', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Physical_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.PositiveIntegerField()),
                ('weight', models.PositiveIntegerField()),
                ('blood_group', models.CharField(max_length=20)),
                ('body_type', models.CharField(max_length=20)),
                ('complexion', models.CharField(max_length=20)),
                ('smoke_habbit', models.CharField(max_length=20)),
                ('drinking_habbit', models.CharField(max_length=20)),
                ('physical_detail_updated_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Professional_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heighst_education', models.CharField(max_length=20)),
                ('heighst_educatio_stream', models.CharField(max_length=20)),
                ('profession', models.CharField(max_length=20)),
                ('office_address', models.CharField(max_length=20)),
                ('annual_income', models.CharField(max_length=20)),
                ('professional_detail_update_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Religious',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('religion', models.CharField(max_length=20)),
                ('caste', models.CharField(max_length=20)),
                ('subcaste', models.CharField(max_length=20)),
                ('star', models.CharField(max_length=20)),
                ('rashi', models.CharField(max_length=20)),
                ('dosh', models.CharField(max_length=20)),
                ('manglik', models.CharField(max_length=20)),
                ('religious_update_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='System_feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_no', models.DecimalField(decimal_places=1, max_digits=10)),
                ('email', models.EmailField(max_length=50)),
                ('feedback', models.CharField(max_length=300)),
                ('remark', models.CharField(max_length=30)),
                ('remark_by', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(max_length=30)),
                ('Customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myfirstapp.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Profile_feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=300)),
                ('remark', models.CharField(max_length=30)),
                ('remark_by', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(max_length=20)),
                ('Customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myfirstapp.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Image_gallary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('Customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myfirstapp.customer')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='customer_expectation',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myfirstapp.customer_expectation'),
        ),
        migrations.AddField(
            model_name='customer',
            name='family_info',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myfirstapp.family_info'),
        ),
        migrations.AddField(
            model_name='customer',
            name='photo_id',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myfirstapp.photo_id'),
        ),
        migrations.AddField(
            model_name='customer',
            name='physical_details',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myfirstapp.physical_details'),
        ),
        migrations.AddField(
            model_name='customer',
            name='professional_detail',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myfirstapp.professional_detail'),
        ),
        migrations.AddField(
            model_name='customer',
            name='religious',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myfirstapp.religious'),
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
