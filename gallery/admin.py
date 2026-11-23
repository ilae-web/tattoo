from django.contrib import admin
from .models import ArtPiece

@admin.register(ArtPiece)
class ArtPieceAdmin(admin.ModelAdmin):
    list_display = ('title', 'style', 'price', 'uploaded_by', 'is_approved')
    list_filter = ('is_approved', 'style')
    search_fields = ('title', 'style')
