# Generated by Django 2.1.7 on 2019-03-31 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avalicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Classificacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel', models.IntegerField()),
                ('descricao', models.CharField(max_length=60)),
            ],
            options={
                'ordering': ['nivel'],
            },
        ),
        migrations.CreateModel(
            name='CoreSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FonteInformacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Pergunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=4)),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='perguntas', to='app.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Qualificador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricaoProblema', models.TextField(blank=True, null=True)),
                ('avaliacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Avalicao')),
                ('fonteInformacao', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.FonteInformacao')),
                ('pergunta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.Pergunta')),
            ],
        ),
        migrations.CreateModel(
            name='RespostaQualificador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classificacao', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.Classificacao')),
                ('qualificador', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.Qualificador')),
                ('resposta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='respostas_qualificadores', to='app.Resposta')),
            ],
        ),
        migrations.AddField(
            model_name='categoria',
            name='classificacoes',
            field=models.ManyToManyField(to='app.Classificacao'),
        ),
        migrations.AddField(
            model_name='categoria',
            name='coreSet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categorias', to='app.CoreSet'),
        ),
        migrations.AddField(
            model_name='categoria',
            name='qualificadores',
            field=models.ManyToManyField(to='app.Qualificador'),
        ),
        migrations.AddField(
            model_name='avalicao',
            name='coreSet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avaliacoes', to='app.CoreSet'),
        ),
        migrations.AddField(
            model_name='avalicao',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avaliacoes_paciente', to='app.Pessoa'),
        ),
        migrations.AddField(
            model_name='avalicao',
            name='terapeuta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avaliacoes_terapeuta', to='app.Pessoa'),
        ),
    ]