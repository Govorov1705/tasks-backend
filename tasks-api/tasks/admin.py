from django.contrib import admin
from django import forms

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    readonly_fields = (
        'date_created',
        'date_updated'
    )

    def formfield_for_dbfield(self, db_field, **kwargs):
        """
        Заменяет widget поля description на Textarea
        """
        formfield = super(TaskAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'description':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        return formfield

admin.site.register(Task, TaskAdmin)
