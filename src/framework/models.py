"""Base Models for models."""
from decimal import Decimal
from itertools import chain
from typing import Set

from django.utils import timezone

__all__ = ['AbstractBaseModel']

import inspect
from datetime import datetime

from django.db import models


class AbstractBaseModel(models.Model):
    """Base Model class for all models within the connect application.
    """

    # Identifier for the database record.
    id = models.AutoField(primary_key=True, serialize=False)
    # The date and time the database record was created stored in the timezone
    # format specified in django settings field- TIME_ZONE.
    created_date: datetime = models.DateTimeField(default=timezone.now, serialize=False)
    # The date and time the database record was modified stored in the timezone
    # format specified in django settings field- TIME_ZONE.
    last_modified_date: datetime = models.DateTimeField(default=timezone.now, serialize=False)

    def to_dict(self):
        opts = self._meta
        data = {}
        for f in chain(opts.concrete_fields, opts.private_fields):
            field_value = f.value_from_object(self)

            if field_value is not None:
                if isinstance(field_value, datetime):
                    field_value = field_value.isoformat()

                if isinstance(field_value, Decimal):
                    field_value = float(field_value)

                data[f.name] = field_value
                if isinstance(f, models.ForeignKey):
                    data[f.name] = {'id': field_value}

        for f in opts.many_to_many:
            data[f.name] = [i.id for i in f.value_from_object(self)]
        return data

    class Meta:
        """Meta information about model
        This model is abstract and will not have a table created in db.
        """

        abstract = True
        app_label = 'framework'

    _validation_exclusions: set = {"created_date", "last_modified_date"}
    _last_modified_date_field_name = 'last_modified_date'
