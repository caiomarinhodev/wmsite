#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.apps import apps
from django.contrib import admin

# Register your models here.

from app.models import *


class MensagemAdmin(admin.ModelAdmin):
    list_filter = []
    search_fields = (
        'id',
    )
    inlines = []
    list_display = ("id", "nome", "email", "nome_empresa", "telefone", "assunto", "mensagem")


admin.site.register(Mensagem, MensagemAdmin)


class FuncionarioAdmin(admin.ModelAdmin):
    list_filter = []
    search_fields = (
        'id',
    )
    inlines = []
    list_display = ("id", "nome", "cargo", "email", "telefone", "facebook_url", "instagram_url")


admin.site.register(Funcionario, FuncionarioAdmin)


class MarcaAdmin(admin.ModelAdmin):
    list_filter = []
    search_fields = (
        'id',
    )
    inlines = []
    list_display = ("id", "nome", "image_url")


admin.site.register(Marca, MarcaAdmin)
