#!/usr/bin/python
# -*- coding: UTF-8 -*-
from django.db import models

# Create your models here.

ASSUNTO_CHOICES = (
    ('Financeiro', 'Financeiro'),
    ('Suprimentos', 'Suprimentos'),
    ('Suporte', 'Suporte'),
    ('Outros', 'Outros')
)


class Mensagem(models.Model):
    class Meta:
        verbose_name = 'Mensagem'
        verbose_name_plural = 'Mensagens'

    nome = models.CharField(max_length=255)
    email = models.EmailField()
    nome_empresa = models.CharField(max_length=100, blank=True, null=True)
    telefone = models.CharField(max_length=20)
    assunto = models.CharField(max_length=100, choices=ASSUNTO_CHOICES)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    def __unicode__(self):
        return self.nome


class Funcionario(models.Model):
    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'

    nome = models.CharField(max_length=255)
    cargo = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    facebook_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    def __unicode__(self):
        return self.nome


class Marca(models.Model):
    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    nome = models.CharField(max_length=255)
    image_url = models.URLField(blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    def __unicode__(self):
        return self.nome
