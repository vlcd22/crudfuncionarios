from django.db import models

class Funcionario(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    cpf = models.CharField(max_length=11, null=False, blank=False)  # CPF como CharField, 11 dígitos
    email = models.EmailField(null=False, blank=False)
    remuneracao = models.CharField(max_length=100, null=False, blank=False)  # Remuneração como CharField

    def __str__(self):
        return self.nome