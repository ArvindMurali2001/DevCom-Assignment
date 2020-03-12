from uuid import uuid4
from django.db import models

class Author(models.Model):
    author_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    country = models.CharField(max_length=100)

    @property
    def full_name(self):
        "Returns the author's full name."
        return '%s %s' % (self.first_name, self.last_name)

class BookedUser(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    roll_number = models.IntegerField(max_length=9)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
   	mobile_number = models.IntegerField(max_length=10)
    email = models.CharField(max_length=50)

class Book(models.Model):
	book_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
	isbn_number = models.IntegerField(max_length=13)
	author_id = models.ForeignKey(Author, on_delete=models.CASCADE, default=uuid4)
	owner_id = models.ForeignKey(BookedUser,on_delete=models.CASCADE, default=uuid4)
	book_name = models.CharField(max_length=100)
	price = models.IntegerField(max_length=10)

class Transaction(models.Model):
	transaction_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
	book_id = models.ForeignKey(Book, on_delete=models.CASCADE, default=uuid4)
	borrower_id = models.ForeignKey(BookedUser,on_delete=models.CASCADE, default=uuid4)
	time_of_transaction = models.DateTimeField()