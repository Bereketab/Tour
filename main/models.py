# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class EthFnf2020(models.Model):
    id = models.BigIntegerField(primary_key=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    gridcode = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ETH_FNF2020'


class EthAdm0(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    id_0 = models.BigIntegerField(blank=True, null=True)
    iso = models.CharField(max_length=3, blank=True, null=True)
    name_0 = models.CharField(max_length=75, blank=True, null=True)
    objectid_1 = models.BigIntegerField(blank=True, null=True)
    iso3 = models.CharField(max_length=5, blank=True, null=True)
    name_engli = models.CharField(max_length=50, blank=True, null=True)
    name_iso = models.CharField(max_length=54, blank=True, null=True)
    name_fao = models.CharField(max_length=50, blank=True, null=True)
    name_local = models.CharField(max_length=54, blank=True, null=True)
    name_obsol = models.CharField(max_length=150, blank=True, null=True)
    name_varia = models.CharField(max_length=160, blank=True, null=True)
    name_nonla = models.CharField(max_length=50, blank=True, null=True)
    name_frenc = models.CharField(max_length=50, blank=True, null=True)
    name_spani = models.CharField(max_length=50, blank=True, null=True)
    name_russi = models.CharField(max_length=50, blank=True, null=True)
    name_arabi = models.CharField(max_length=50, blank=True, null=True)
    name_chine = models.CharField(max_length=50, blank=True, null=True)
    waspartof = models.CharField(max_length=100, blank=True, null=True)
    contains = models.CharField(max_length=50, blank=True, null=True)
    sovereign = models.CharField(max_length=40, blank=True, null=True)
    iso2 = models.CharField(max_length=4, blank=True, null=True)
    www = models.CharField(max_length=2, blank=True, null=True)
    fips = models.CharField(max_length=6, blank=True, null=True)
    ison = models.FloatField(blank=True, null=True)
    validfr = models.CharField(max_length=12, blank=True, null=True)
    validto = models.CharField(max_length=10, blank=True, null=True)
    pop2000 = models.FloatField(blank=True, null=True)
    sqkm = models.FloatField(blank=True, null=True)
    popsqkm = models.FloatField(blank=True, null=True)
    unregion1 = models.CharField(max_length=254, blank=True, null=True)
    unregion2 = models.CharField(max_length=254, blank=True, null=True)
    developing = models.FloatField(blank=True, null=True)
    cis = models.FloatField(blank=True, null=True)
    transition = models.FloatField(blank=True, null=True)
    oecd = models.FloatField(blank=True, null=True)
    wbregion = models.CharField(max_length=254, blank=True, null=True)
    wbincome = models.CharField(max_length=254, blank=True, null=True)
    wbdebt = models.CharField(max_length=254, blank=True, null=True)
    wbother = models.CharField(max_length=254, blank=True, null=True)
    ceeac = models.FloatField(blank=True, null=True)
    cemac = models.FloatField(blank=True, null=True)
    ceplg = models.FloatField(blank=True, null=True)
    comesa = models.FloatField(blank=True, null=True)
    eac = models.FloatField(blank=True, null=True)
    ecowas = models.FloatField(blank=True, null=True)
    igad = models.FloatField(blank=True, null=True)
    ioc = models.FloatField(blank=True, null=True)
    mru = models.FloatField(blank=True, null=True)
    sacu = models.FloatField(blank=True, null=True)
    uemoa = models.FloatField(blank=True, null=True)
    uma = models.FloatField(blank=True, null=True)
    palop = models.FloatField(blank=True, null=True)
    parta = models.FloatField(blank=True, null=True)
    cacm = models.FloatField(blank=True, null=True)
    eurasec = models.FloatField(blank=True, null=True)
    agadir = models.FloatField(blank=True, null=True)
    saarc = models.FloatField(blank=True, null=True)
    asean = models.FloatField(blank=True, null=True)
    nafta = models.FloatField(blank=True, null=True)
    gcc = models.FloatField(blank=True, null=True)
    csn = models.FloatField(blank=True, null=True)
    caricom = models.FloatField(blank=True, null=True)
    eu = models.FloatField(blank=True, null=True)
    can = models.FloatField(blank=True, null=True)
    acp = models.FloatField(blank=True, null=True)
    landlocked = models.FloatField(blank=True, null=True)
    aosis = models.FloatField(blank=True, null=True)
    sids = models.FloatField(blank=True, null=True)
    islands = models.FloatField(blank=True, null=True)
    ldc = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ETH_adm0'


class EthAdm1(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    id_0 = models.BigIntegerField(blank=True, null=True)
    iso = models.CharField(max_length=3, blank=True, null=True)
    name_0 = models.CharField(max_length=75, blank=True, null=True)
    id_1 = models.BigIntegerField(blank=True, null=True)
    name_1 = models.CharField(max_length=75, blank=True, null=True)
    type_1 = models.CharField(max_length=50, blank=True, null=True)
    engtype_1 = models.CharField(max_length=50, blank=True, null=True)
    nl_name_1 = models.CharField(max_length=50, blank=True, null=True)
    varname_1 = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ETH_adm1'


class EthAdm2(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    id_0 = models.BigIntegerField(blank=True, null=True)
    iso = models.CharField(max_length=3, blank=True, null=True)
    name_0 = models.CharField(max_length=75, blank=True, null=True)
    id_1 = models.BigIntegerField(blank=True, null=True)
    name_1 = models.CharField(max_length=75, blank=True, null=True)
    id_2 = models.BigIntegerField(blank=True, null=True)
    name_2 = models.CharField(max_length=75, blank=True, null=True)
    type_2 = models.CharField(max_length=50, blank=True, null=True)
    engtype_2 = models.CharField(max_length=50, blank=True, null=True)
    nl_name_2 = models.CharField(max_length=75, blank=True, null=True)
    varname_2 = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ETH_adm2'


class EthAdm3(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    id_0 = models.BigIntegerField(blank=True, null=True)
    iso = models.CharField(max_length=3, blank=True, null=True)
    name_0 = models.CharField(max_length=75, blank=True, null=True)
    id_1 = models.BigIntegerField(blank=True, null=True)
    name_1 = models.CharField(max_length=75, blank=True, null=True)
    id_2 = models.BigIntegerField(blank=True, null=True)
    name_2 = models.CharField(max_length=75, blank=True, null=True)
    id_3 = models.BigIntegerField(blank=True, null=True)
    name_3 = models.CharField(max_length=75, blank=True, null=True)
    type_3 = models.CharField(max_length=50, blank=True, null=True)
    engtype_3 = models.CharField(max_length=50, blank=True, null=True)
    nl_name_3 = models.CharField(max_length=75, blank=True, null=True)
    varname_3 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ETH_adm3'


class AccountsAdminuser(models.Model):
    user = models.OneToOneField('AccountsUser', models.DO_NOTHING, primary_key=True)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'accounts_adminuser'


class AccountsClientuser(models.Model):
    user = models.OneToOneField('AccountsUser', models.DO_NOTHING, primary_key=True)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    location = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'accounts_clientuser'


class AccountsUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    is_admin = models.BooleanField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'accounts_user'


class AccountsUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AccountsUser, models.DO_NOTHING)
    group = models.ForeignKey('AuthGroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'accounts_user_groups'
        unique_together = (('user', 'group'),)


class AccountsUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AccountsUser, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'accounts_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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


class Destinations(models.Model):
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    objectid = models.IntegerField(db_column='OBJECTID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    datetimes = models.DateTimeField(db_column='DateTimeS', blank=True, null=True)  # Field name made lowercase.
    elevation = models.FloatField(db_column='Elevation', blank=True, null=True)  # Field name made lowercase.
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    full_name = models.CharField(db_column='Full_Name', blank=True, null=True)  # Field name made lowercase.
    short_name = models.CharField(db_column='Short_Name', blank=True, null=True)  # Field name made lowercase.
    zone = models.CharField(db_column='Zone', blank=True, null=True)  # Field name made lowercase.
    wereda = models.CharField(db_column='Wereda', blank=True, null=True)  # Field name made lowercase.
    kebele = models.CharField(db_column='Kebele', blank=True, null=True)  # Field name made lowercase.
    locality_n = models.CharField(db_column='Locality_N', blank=True, null=True)  # Field name made lowercase.
    organizati = models.CharField(db_column='Organizati', blank=True, null=True)  # Field name made lowercase.
    destinatio = models.CharField(db_column='Destinatio', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    area_sqkm = models.CharField(db_column='Area_sqkm', blank=True, null=True)  # Field name made lowercase.
    yearly_est = models.CharField(db_column='Yearly_Est', blank=True, null=True)  # Field name made lowercase.
    unesco_reg = models.CharField(db_column='UNESCO_Reg', blank=True, null=True)  # Field name made lowercase.
    descriptio = models.TextField(db_column='Descriptio', blank=True, null=True)  # Field name made lowercase.
    photo_no = models.CharField(db_column='Photo_No', blank=True, null=True)  # Field name made lowercase.
    photo_loca = models.CharField(db_column='Photo_Loca', blank=True, null=True)  # Field name made lowercase.
    site_des_a = models.CharField(db_column='Site_Des_A', blank=True, null=True)  # Field name made lowercase.
    amharic = models.TextField(db_column='Amharic', blank=True, null=True)  # Field name made lowercase.
    english = models.CharField(db_column='English', blank=True, null=True)  # Field name made lowercase.
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(db_column='Y', blank=True, null=True)  # Field name made lowercase.
    image1 = models.FileField(blank=True, null=True)  # This field type is a guess.
    image2 = models.FileField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'destinations'
    
    def __str__(self):
        return self.full_name



class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AccountsUser, models.DO_NOTHING)

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
    id = models.BigAutoField(primary_key=True)
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


class Services(models.Model):
    id = models.CharField(primary_key=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    objectid = models.IntegerField(blank=True, null=True)
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    z = models.IntegerField(blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    full_name = models.CharField(blank=True, null=True)
    short_name = models.CharField(blank=True, null=True)
    zone = models.CharField(blank=True, null=True)
    wereda = models.CharField(blank=True, null=True)
    kebele = models.CharField(blank=True, null=True)
    phone_line = models.CharField(blank=True, null=True)
    email = models.CharField(blank=True, null=True)
    website = models.CharField(blank=True, null=True)
    service_ty = models.CharField(blank=True, null=True)
    owner_name = models.CharField(blank=True, null=True)
    moto = models.CharField(blank=True, null=True)
    

    class Meta:
        managed = False
        db_table = 'services'
    def __str__(self):
        return self.full_name


class SpatialRefSys(models.Model):
    srid = models.IntegerField(primary_key=True)
    auth_name = models.CharField(max_length=256, blank=True, null=True)
    auth_srid = models.IntegerField(blank=True, null=True)
    srtext = models.CharField(max_length=2048, blank=True, null=True)
    proj4text = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spatial_ref_sys'


class TE(models.Model):
    docs = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_e'
