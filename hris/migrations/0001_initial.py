# Generated by Django 4.0.2 on 2022-02-28 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssignmentT',
            fields=[
                ('assignment_id', models.AutoField(primary_key=True, serialize=False)),
                ('worker_id', models.IntegerField(blank=True, null=True)),
                ('project_id', models.IntegerField(blank=True, null=True)),
                ('role', models.CharField(blank=True, max_length=30, null=True)),
                ('base_pay', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('biodata', models.TextField()),
                ('medical_report', models.TextField(blank=True, null=True)),
                ('nbi_clearance', models.TextField(blank=True, null=True)),
                ('contract', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'assignment_t',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ProjectT',
            fields=[
                ('project_id', models.AutoField(primary_key=True, serialize=False)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('project_title', models.CharField(max_length=50)),
                ('project_type', models.CharField(blank=True, max_length=30, null=True)),
                ('project_location', models.CharField(blank=True, max_length=100, null=True)),
                ('client', models.CharField(blank=True, max_length=50, null=True)),
                ('client_contact_number', models.CharField(blank=True, max_length=16, null=True)),
                ('project_in_charge', models.CharField(blank=True, max_length=50, null=True)),
                ('project_in_charge_contact_number', models.CharField(blank=True, max_length=16, null=True)),
            ],
            options={
                'db_table': 'project_t',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UserT',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('user_type', models.CharField(max_length=10)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'user_t',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='WorkerT',
            fields=[
                ('worker_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=30)),
                ('contact_number', models.CharField(blank=True, max_length=16, null=True)),
            ],
            options={
                'db_table': 'worker_t',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='EvaluationReportT',
            fields=[
                ('eval_id', models.AutoField(primary_key=True, serialize=False)),
                ('overall_rating', models.DecimalField(blank=True, decimal_places=2, max_digits=2, null=True)),
                ('worker_strength', models.CharField(blank=True, max_length=180, null=True)),
                ('areas_of_improvement', models.CharField(blank=True, max_length=180, null=True)),
                ('plan_of_action', models.CharField(blank=True, max_length=180, null=True)),
                ('knowledge_of_work', models.IntegerField(blank=True, null=True)),
                ('attendance', models.IntegerField(blank=True, null=True)),
                ('volume_of_output', models.IntegerField(blank=True, null=True)),
                ('attitude', models.IntegerField(blank=True, null=True)),
                ('eassignment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hris.assignmentt')),
            ],
            options={
                'db_table': 'evaluation_report_t',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='assignmentt',
            name='aproject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hris.projectt'),
        ),
        migrations.AddField(
            model_name='assignmentt',
            name='aworker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hris.workert'),
        ),
    ]
