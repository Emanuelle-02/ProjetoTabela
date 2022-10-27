from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=250)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField(max_length=150)
    carga_horaria = models.IntegerField()
    registro = models.ManyToManyField(Aluno, through='Aluno_Disciplina')

    def __str__(self):
        return self.nome

class Aluno_Disciplina(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    data_matricula = models.DateField()
    periodo = models.CharField(max_length=50)