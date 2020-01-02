from django.contrib import admin
from .models import Author, Publisher, Subjects, ItemType, ItemCollection, ItemLocation, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description',)
    fields = ('name', 'description',)


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    fields = ('name', 'description')


@admin.register(Subjects)
class SubjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    fields = ('name',)


@admin.register(ItemType)
class ItemTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    fields = ('name',)


@admin.register(ItemCollection)
class ItemCollectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    fields = ('name',)


@admin.register(ItemLocation)
class ItemLocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    fields = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    def _author(self, obj):
        return [a.name for a in obj.author.all()]

    def _subjects(self, obj):
        return [s.name for s in obj.subjects.all()]

    def _title(self, obj):
        return obj.title.split(' / ')[0]

    list_display = (
    'id', 'bibnum', '_title', '_author', 'isbn', 'publicationyear', '_subjects', 'itemtype', 'itemcollection',
    'floatingitem', 'itemlocation', 'reportdate', 'itemcount',)
    list_display_links = ('id', '_title', )
    filter_horizontal = ('subjects',)
    fields = (
    'bibnum', 'title', 'isbn', 'author', 'publicationyear', 'publisher', 'subjects', 'itemtype', 'itemcollection',
    'floatingitem', 'itemlocation', 'reportdate', 'itemcount',)
