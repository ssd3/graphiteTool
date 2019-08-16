# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Audit(models.Model):
    auditid = models.BigAutoField(db_column='AuditID', primary_key=True)  # Field name made lowercase.
    tableid = models.SmallIntegerField(db_column='TableID')  # Field name made lowercase.
    actionid = models.SmallIntegerField(db_column='ActionID')  # Field name made lowercase.
    rowdata = models.TextField(db_column='RowData')  # Field name made lowercase. This field type is a guess.
    chain = models.CharField(db_column='Chain', max_length=32)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID')  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Audit'


class Category(models.Model):
    categoryid = models.AutoField(db_column='CategoryID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=32)  # Field name made lowercase.
    userid = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Category'


class Credit(models.Model):
    creditid = models.BigAutoField(db_column='CreditID', primary_key=True)  # Field name made lowercase.
    credittypeid = models.ForeignKey('Credittype', models.DO_NOTHING, db_column='CreditTypeID')  # Field name made lowercase.
    buyerid = models.IntegerField(db_column='BuyerID')  # Field name made lowercase.
    fromwarehouseid = models.IntegerField(db_column='FromWarehouseID', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created')  # Field name made lowercase.
    towarehouseid = models.IntegerField(db_column='ToWarehouseID', blank=True, null=True)  # Field name made lowercase.
    sent = models.DateTimeField(db_column='Sent', blank=True, null=True)  # Field name made lowercase.
    received = models.DateTimeField(db_column='Received', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Credit'


class Creditcomment(models.Model):
    creditcommentid = models.BigAutoField(db_column='CreditCommentID', primary_key=True)  # Field name made lowercase.
    creditid = models.ForeignKey(Credit, models.DO_NOTHING, db_column='CreditID')  # Field name made lowercase.
    comment = models.TextField(db_column='Comment')  # Field name made lowercase.
    userid = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CreditComment'


class Creditdetails(models.Model):
    creditdetailsid = models.BigAutoField(db_column='CreditDetailsID', primary_key=True)  # Field name made lowercase.
    creditid = models.ForeignKey(Credit, models.DO_NOTHING, db_column='CreditID')  # Field name made lowercase.
    productid = models.ForeignKey('Product', models.DO_NOTHING, db_column='ProductID')  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=10, decimal_places=2)  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=10, decimal_places=2)  # Field name made lowercase.
    pricetypeid = models.ForeignKey('Pricetype', models.DO_NOTHING, db_column='PriceTypeID')  # Field name made lowercase.
    userid = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CreditDetails'


class Creditloss(models.Model):
    creditlossid = models.AutoField(db_column='CreditLossID', primary_key=True)  # Field name made lowercase.
    creditid = models.ForeignKey(Credit, models.DO_NOTHING, db_column='CreditID')  # Field name made lowercase.
    losstypeid = models.ForeignKey('Losstype', models.DO_NOTHING, db_column='LossTypeID')  # Field name made lowercase.
    value = models.DecimalField(db_column='Value', max_digits=10, decimal_places=2)  # Field name made lowercase.
    userid = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CreditLoss'


class Credittype(models.Model):
    credittypeid = models.AutoField(db_column='CreditTypeID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=32)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=64, blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CreditType'


class Debit(models.Model):
    debitid = models.BigAutoField(db_column='DebitID', primary_key=True)  # Field name made lowercase.
    warehouseid = models.ForeignKey('Warehouse', models.DO_NOTHING, db_column='WarehouseID')  # Field name made lowercase.
    productid = models.ForeignKey('Product', models.DO_NOTHING, db_column='ProductID')  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=10, decimal_places=2)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=10, decimal_places=2)  # Field name made lowercase.
    pricetypeid = models.ForeignKey('Pricetype', models.DO_NOTHING, db_column='PriceTypeID')  # Field name made lowercase.
    discountid = models.ForeignKey('Discount', models.DO_NOTHING, db_column='DiscountID')  # Field name made lowercase.
    tracknumber = models.CharField(db_column='TrackNumber', unique=True, max_length=64)  # Field name made lowercase.
    statusid = models.ForeignKey('Status', models.DO_NOTHING, db_column='StatusID')  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Debit'


class Discount(models.Model):
    discountid = models.AutoField(db_column='DiscountID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=48)  # Field name made lowercase.
    value = models.DecimalField(db_column='Value', max_digits=10, decimal_places=2)  # Field name made lowercase.
    units = models.CharField(db_column='Units', max_length=5)  # Field name made lowercase.
    userid = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Discount'


class Losstype(models.Model):
    losstypeid = models.AutoField(db_column='LossTypeID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=64)  # Field name made lowercase.
    userid = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LossType'


class Pricetype(models.Model):
    pricetypeid = models.AutoField(db_column='PriceTypeID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=48)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=48, blank=True, null=True)  # Field name made lowercase.
    ratio = models.DecimalField(db_column='Ratio', max_digits=10, decimal_places=2)  # Field name made lowercase.
    userid = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PriceType'


class Product(models.Model):
    productid = models.BigAutoField(db_column='ProductID', primary_key=True)  # Field name made lowercase.
    categoryid = models.ForeignKey(Category, models.DO_NOTHING, db_column='CategoryID')  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=48)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Product'


class Productcomment(models.Model):
    productcommentid = models.BigAutoField(db_column='ProductCommentID', primary_key=True)  # Field name made lowercase.
    productid = models.ForeignKey(Product, models.DO_NOTHING, db_column='ProductID')  # Field name made lowercase.
    comment = models.TextField(db_column='Comment')  # Field name made lowercase.
    userid = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProductComment'


class Productdetails(models.Model):
    productdetailsid = models.BigAutoField(db_column='ProductDetailsID', primary_key=True)  # Field name made lowercase.
    productid = models.ForeignKey(Product, models.DO_NOTHING, db_column='ProductID')  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=128, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='Url', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    serialno = models.CharField(db_column='SerialNo', max_length=128, blank=True, null=True)  # Field name made lowercase.
    weight = models.DecimalField(db_column='Weight', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    height = models.DecimalField(db_column='Height', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    width = models.DecimalField(db_column='Width', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lenght = models.DecimalField(db_column='Lenght', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ProductDetails'


class Status(models.Model):
    statusid = models.AutoField(db_column='StatusID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=48)  # Field name made lowercase.
    color = models.CharField(db_column='Color', max_length=32)  # Field name made lowercase.
    userid = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Status'


class Warehouse(models.Model):
    warehouseid = models.AutoField(db_column='WarehouseID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=48)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    active = models.BooleanField(db_column='Active')  # Field name made lowercase.
    userid = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created')  # Field name made lowercase.
    in_field = models.BooleanField(db_column='In')  # Field name made lowercase. Field renamed because it was a Python reserved word.
    out = models.BooleanField(db_column='Out')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Warehouse'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
