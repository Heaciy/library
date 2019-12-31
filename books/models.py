from django.db import models


class Author(models.Model):
    """The name of the first author of the title, if applicable."""
    name = models.CharField(max_length=20)
    # books = models.ManyToManyField()
    description = models.TextField(default='', blank=True)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        ordering = ['name', ]

    def __str__(self):
        return self.name


class Publisher(models.Model):
    """	The name of the publishing company for this item."""
    name = models.CharField(max_length=20)
    # books = models.ManyToManyField()
    description = models.TextField(default='', blank=True)

    class Meta:
        verbose_name = 'Publisher'
        verbose_name_plural = 'Publishers'

    def __str__(self):
        return self.name


class Subjects(models.Model):
    """A comma-separated list of the subject authority records
    associated with the title, including Motion Pictures,
    Computer Programming, etc. Typically these are highly specific."""
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Subjects'
        verbose_name_plural = 'Subjects'
        ordering = ['name', ]

    def __str__(self):
        return self.name


class ItemType(models.Model):
    """Horizon item type. Look up value descriptions in HorizonCodes
    using CodeType "ItemType"."""
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'ItemType'
        verbose_name_plural = 'ItemTypes'

    def __str__(self):
        return self.name


class ItemCollection(models.Model):
    """Collection code for this item. Look up value descriptions in:
    Integrated Library System (ILS) Data Dictionary"""
    name = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'ItemCollection'
        verbose_name_plural = 'ItemCollections'

    def __str__(self):
        return self.name


class ItemLocation(models.Model):
    """
    Location that owned the item at the time of snapshot. 3-letter code.
    Note: as of 2017, some items are "FLOATING" which means they don't necessarily belong to a specific branch.
    Location of given copy could change based on where the item is returned."""
    name = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'ItemCollection'
        verbose_name_plural = 'ItemCollections'

    def __str__(self):
        return self.name


class Book(models.Model):
    STATUS_FLOAT = 1
    STATUS_NA = 0
    STATUS_ITEMS = (
        (STATUS_FLOAT, 'Floating'),
        (STATUS_NA, 'NA')
    )
    # The unique identifier for a cataloged item within the Library's Integrated Library System (ILS).
    bibnum = models.PositiveIntegerField(verbose_name='Bibnum')
    # The full title of an item.
    title = models.CharField(max_length=40, verbose_name='Title')
    author = models.ManyToManyField(Author, verbose_name='Author', blank=True)
    # Comma-delimited list of ISBN(s) for this title.
    isbn = models.CharField(max_length=60, verbose_name='ISBN', default='', blank=True)
    # Date (year) of publication.
    publicationyear = models.PositiveIntegerField(verbose_name='PublicationYear', blank=True)
    publisher = models.ForeignKey(Publisher, verbose_name='Publisher', on_delete=models.DO_NOTHING, blank=True)
    subjects = models.ManyToManyField(Subjects, verbose_name='Subjects', blank=True)
    itemtype = models.ForeignKey(ItemType, verbose_name='ItemType', on_delete=models.DO_NOTHING)
    itemcollection = models.ForeignKey(ItemCollection, verbose_name='ItemCollection', on_delete=models.DO_NOTHING)
    # Label that indicates if an item floats.
    floatingitem = models.PositiveIntegerField(default=STATUS_NA, choices=STATUS_ITEMS, verbose_name='FloatingItem')
    itemlocation = models.ForeignKey(ItemLocation, verbose_name='ItemLocation', on_delete=models.DO_NOTHING)
    # The date when this item count was collected from the ILS (Horizon).
    reportdate = models.DateField(verbose_name='ReportYear')
    # The number of items in this location, collection, item type, and item status as of the report date.
    itemcount = models.PositiveIntegerField(verbose_name='ItemCount')

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ['bibnum', ]

    def __str__(self):
        return '<Book[{}]: {}>'.format(self.id, self.title.split(' / ')[0])
