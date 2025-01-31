"""
admin.py
"""

from django.contrib import admin

from nephr_audit.models import AuditTag, NephrAuditInfo, NephrAuditLog

# Register your models here.

admin.site.register(AuditTag)
