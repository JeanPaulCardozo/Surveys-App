from django.contrib import admin
from .models import Question, Choice

# Register your models here.
# StackedInline usado para mostrar los campos uno debajo de otro
# TabularInline para mostrar los campos en tablas
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    """Custom order questions in admin section"""
    # Set Custom Fields order.
    # fields = ["pub_date", "question_text"]

    # Get Fields By groups
    fieldsets = [
        (None, {"fields":  ["question_text"]}),
        ("Date Information", {"fields":  ["pub_date"], "classes": ["collapse"]})
    ]
    inlines = [ChoiceInline] # Editar el modelo hijo
    list_display = ["question_text", "pub_date", "was_published_recently"] # modificar vista del modelo Questions
    list_filter = ["pub_date"] # Filter by pub_date
    search_fields = ["question_text"] # Search by question_text



admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
