#! /usr/bin/python
# -*- coding: UTF-8 -*-
"""
Global variables for base module
"""
from django.utils.translation import ugettext_lazy as _
from django.conf import LazySettings

settings = LazySettings()


def get_from_settings_or_default(var_name, default):
    try:
        return settings.__getattr__(var_name)
    except AttributeError:
        return default


# Items by page on paginator views
ITEMS_BY_PAGE = 10

CREATE_SUFFIX = "_create"
LIST_SUFFIX = "_list"
DETAIL_SUFFIX = "_detail"
UPDATE_SUFFIX = "_update"
DELETE_SUFFIX = "_delete"

API_SUFFIX = "_api"
style = "base_django/flexbox"

# Messages
OBJECT_CREATED_SUCCESSFULLY = _("Object created successfully")
OBJECT_UPDATED_SUCCESSFULLY = _("Object updated successfully")
OBJECT_DELETED_SUCCESSFULLY = _("Object deleted successfully")

BASE_MODELS_TRANSLATION_NAME = _("Name")
BASE_MODELS_TRANSLATION_DESCRIPTION = _("Description")
BASE_MODELS_TRANSLATION_SLUG = _("Slug")
BASE_MODELS_TRANSLATION_CREATED = _("Created")
BASE_MODELS_TRANSLATION_MODIFIED = _("Modified")
BASE_MODELS_TRANSLATION_ACTIVE = _("Active")

CONFIGURING_APPLICATION = _("Configuring application {}")
CREATING_PERMISSION_WITH_NAME = _("Creating Permission with name {}")
CREATING_GROUP_WITH_NAME = _("Creating Group with name {}")

MENSAGEM_PREFIX = "MENSAGEM"

MENSAGEM_VERBOSE_NAME = _("Mensagem")
MENSAGEM_VERBOSE_NAME_PLURAL = _("Mensagem")

MENSAGEM_LIST_URL_NAME = MENSAGEM_PREFIX + LIST_SUFFIX
MENSAGEM_CREATE_URL_NAME = MENSAGEM_PREFIX + CREATE_SUFFIX
MENSAGEM_DETAIL_URL_NAME = MENSAGEM_PREFIX + DETAIL_SUFFIX
MENSAGEM_UPDATE_URL_NAME = MENSAGEM_PREFIX + UPDATE_SUFFIX
MENSAGEM_DELETE_URL_NAME = MENSAGEM_PREFIX + DELETE_SUFFIX
MENSAGEM_LIST_JSON_URL_NAME = MENSAGEM_PREFIX + '_list_json'

FUNCIONARIO_PREFIX = "FUNCIONARIO"

FUNCIONARIO_VERBOSE_NAME = _("Funcionario")
FUNCIONARIO_VERBOSE_NAME_PLURAL = _("Funcionario")

FUNCIONARIO_LIST_URL_NAME = FUNCIONARIO_PREFIX + LIST_SUFFIX
FUNCIONARIO_CREATE_URL_NAME = FUNCIONARIO_PREFIX + CREATE_SUFFIX
FUNCIONARIO_DETAIL_URL_NAME = FUNCIONARIO_PREFIX + DETAIL_SUFFIX
FUNCIONARIO_UPDATE_URL_NAME = FUNCIONARIO_PREFIX + UPDATE_SUFFIX
FUNCIONARIO_DELETE_URL_NAME = FUNCIONARIO_PREFIX + DELETE_SUFFIX
FUNCIONARIO_LIST_JSON_URL_NAME = FUNCIONARIO_PREFIX + '_list_json'

MARCA_PREFIX = "MARCA"

MARCA_VERBOSE_NAME = _("Marca")
MARCA_VERBOSE_NAME_PLURAL = _("Marca")

MARCA_LIST_URL_NAME = MARCA_PREFIX + LIST_SUFFIX
MARCA_CREATE_URL_NAME = MARCA_PREFIX + CREATE_SUFFIX
MARCA_DETAIL_URL_NAME = MARCA_PREFIX + DETAIL_SUFFIX
MARCA_UPDATE_URL_NAME = MARCA_PREFIX + UPDATE_SUFFIX
MARCA_DELETE_URL_NAME = MARCA_PREFIX + DELETE_SUFFIX
MARCA_LIST_JSON_URL_NAME = MARCA_PREFIX + '_list_json'
