#!/usr/bin/python
# -*- coding: UTF-8 -*-
from django.contrib.auth.models import User
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
    usuario = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE)
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


class Cliente(models.Model):
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    usuario = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE)
    nome_empresa = models.CharField(max_length=255, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    numero = models.CharField(max_length=255, blank=True, null=True)
    bairro = models.CharField(max_length=255, blank=True, null=True)
    cidade = models.CharField(max_length=255, blank=True, null=True)
    estado = models.CharField(max_length=255, blank=True, null=True)
    cep = models.CharField(max_length=255, blank=True, null=True)
    cnpj = models.CharField(max_length=255, blank=True, null=True)

    def get_name(self):
        return self.nome_empresa

    def get_address(self):
        return self.endereco + ', ' + self.numero + ', ' + self.bairro + ', ' + self.cidade + ', ' + self.estado + ', ' + self.cep

    def __str__(self):
        return "%s" % self.nome_empresa

    def __unicode__(self):
        return "%s" % self.nome_empresa


STATUS_CHOICES = (('Aguardando', 'Aguardando'), ('Em andamento',
                                                 'Em andamento'), ('Finalizado', 'Finalizado'))


class Solicitacao(models.Model):
    class Meta:
        verbose_name = 'Solicitacao'
        verbose_name_plural = 'Solicitacoes'

    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(
        max_length=255, blank=True, null=True, choices=STATUS_CHOICES, default='Aguardando')
    data_cadastro = models.DateTimeField(auto_now_add=True)
    produto = models.CharField(max_length=255, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.cliente.nome_empresa

    def __unicode__(self):
        return self.cliente.nome_empresa
