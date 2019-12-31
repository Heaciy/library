from django.contrib import admin
from .models import Author, Publisher, Subjects, ItemType, ItemCollection, ItemLocation, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    fields = ('name', 'description',)


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    fields = ('name', 'description')


@admin.register(Subjects)
class SubjectsAdmin(admin.ModelAdmin):
    play_list = ('name',)
    fields = ('name',)


@admin.register(ItemType)
class ItemTypeAdmin(admin.ModelAdmin):
    play_list = ('name',)
    fields = ('name',)


@admin.register(ItemCollection)
class ItemCollectionAdmin(admin.ModelAdmin):
    play_list = ('name',)
    fields = ('name',)


@admin.register(ItemLocation)
class ItemLocationAdmin(admin.ModelAdmin):
    play_list = ('name',)
    fields = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    play_list = ('bibnum', 'title', 'author', 'isbn', 'publicationyear', 'publisher', 'subjects', 'itemtype',
                 'itemcollection', 'floatingitem', 'itemlocation', 'reportdate', 'itemcount',)
    fields = ('bibnum', 'title', 'author', 'isbn', 'publicationyear', 'publisher', 'subjects', 'itemtype',
                 'itemcollection', 'floatingitem', 'itemlocation', 'reportdate', 'itemcount',)
