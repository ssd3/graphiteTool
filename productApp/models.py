# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Category(models.Model):
    categoryid = models.AutoField(db_column='CategoryID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=32)  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Category'


class Product(models.Model):
    productid = models.BigAutoField(db_column='ProductID', primary_key=True)  # Field name made lowercase.
    categoryid = models.ForeignKey(Category, models.DO_NOTHING, db_column='CategoryID')  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=48)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Product'


class User(models.Model):
    userid = models.AutoField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=16)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=32)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=32)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=48, blank=True, null=True)  # Field name made lowercase.
    active = models.BooleanField(db_column='Active')  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created')  # Field name made lowercase.
    isadmin = models.BooleanField(db_column='IsAdmin')  # Field name made lowercase.
    isstaff = models.BooleanField(db_column='IsStaff')  # Field name made lowercase.
    issupplier = models.BooleanField(db_column='IsSupplier')  # Field name made lowercase.
    isbuyer = models.BooleanField(db_column='IsBuyer')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'User'



