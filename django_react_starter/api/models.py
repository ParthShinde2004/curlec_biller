# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
"""
The models are from the tables in the Curlec database (check settings.py for database info).
The models that are currently comments are not being used feel free to delete them or uncomment them
if you use it (remember to make migrations).
"""

from django.db import models


# class Acl(models.Model):
#     uid = models.CharField(primary_key=True, max_length=32)
#     name = models.CharField(unique=True, max_length=50)

#     class Meta:
#         managed = False
#         db_table = 'acl'


# class AclInfo(models.Model):
#     acl_uid = models.OneToOneField(
#         Acl, models.DO_NOTHING, db_column='acl_uid', primary_key=True)
#     principal_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='principal_uid')
#     # Field renamed because it ended with '_'.
#     use_field = models.SmallIntegerField(db_column='use_')
#     see = models.SmallIntegerField()
#     chg = models.SmallIntegerField()
#     # Field renamed because it was a Python reserved word.
#     del_field = models.SmallIntegerField(db_column='del')
#     gac = models.SmallIntegerField()
#     see_cnt = models.SmallIntegerField()
#     chg_cnt = models.SmallIntegerField()
#     del_cnt = models.SmallIntegerField()
#     dl_cnt = models.SmallIntegerField()

#     class Meta:
#         managed = False
#         db_table = 'acl_info'
#         unique_together = (('acl_uid', 'principal_uid'),)


# class ActionEvent(models.Model):
#     uid = models.CharField(primary_key=True, max_length=32)
#     activity_uid = models.ForeignKey(
#         'Activity', models.DO_NOTHING, db_column='activity_uid', blank=True, null=True)
#     activity_instance_uid = models.ForeignKey(
#         'ActivityInstance', models.DO_NOTHING, db_column='activity_instance_uid', blank=True, null=True)
#     action_uid = models.CharField(max_length=32, blank=True, null=True)
#     action_name = models.CharField(max_length=50, blank=True, null=True)
#     action_type = models.CharField(max_length=50, blank=True, null=True)
#     state = models.SmallIntegerField(blank=True, null=True)
#     event = models.CharField(max_length=12, blank=True, null=True)
#     event_date = models.DateTimeField(blank=True, null=True)
#     actor = models.CharField(max_length=50, blank=True, null=True)
#     estimated_cost = models.IntegerField(blank=True, null=True)
#     actual_cost = models.IntegerField(blank=True, null=True)
#     estimated_duration = models.BigIntegerField(blank=True, null=True)
#     actual_duration = models.BigIntegerField(blank=True, null=True)
#     milestone = models.CharField(max_length=50, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'action_event'


# class Activity(models.Model):
#     uid = models.CharField(primary_key=True, max_length=32)
#     name = models.CharField(max_length=50)
#     version = models.IntegerField()
#     activity_graph = models.TextField(blank=True, null=True)
#     description = models.CharField(max_length=255, blank=True, null=True)
#     is_sub = models.SmallIntegerField()

#     class Meta:
#         managed = False
#         db_table = 'activity'


# class ActivityAcl(models.Model):
#     activity_uid = models.OneToOneField(
#         Activity, models.DO_NOTHING, db_column='activity_uid', primary_key=True)
#     acl_uid = models.CharField(max_length=32, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'activity_acl'


# class ActivityInstance(models.Model):
#     uid = models.CharField(primary_key=True, max_length=32)
#     activity_uid = models.ForeignKey(
#         Activity, models.DO_NOTHING, db_column='activity_uid', blank=True, null=True)
#     root_token_uid = models.CharField(max_length=32, blank=True, null=True)
#     launched_by = models.CharField(max_length=50, blank=True, null=True)
#     launched_when = models.DateTimeField(blank=True, null=True)
#     completed = models.SmallIntegerField(blank=True, null=True)
#     completed_when = models.DateTimeField(blank=True, null=True)
#     aborted = models.SmallIntegerField(blank=True, null=True)
#     aborted_when = models.DateTimeField(blank=True, null=True)
#     aborted_by = models.CharField(max_length=50, blank=True, null=True)
#     name = models.CharField(max_length=150, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'activity_instance'


# class AltContainerContainee(models.Model):
#     alt_container_uid = models.CharField(primary_key=True, max_length=65)
#     containee_uid = models.CharField(max_length=65)

#     class Meta:
#         managed = False
#         db_table = 'alt_container_containee'
#         unique_together = (('alt_container_uid', 'containee_uid'),)


# class Annotation(models.Model):
#     uid = models.CharField(primary_key=True, max_length=32)
#     content_uid = models.CharField(max_length=65)
#     creator = models.CharField(max_length=255)
#     annotation_content = models.TextField(blank=True, null=True)
#     date_created = models.DateTimeField(blank=True, null=True)
#     date_last_modified = models.DateTimeField(blank=True, null=True)
#     acl_uid = models.ForeignKey(
#         Acl, models.DO_NOTHING, db_column='acl_uid', blank=True, null=True)
#     creator_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='creator_uid', blank=True, null=True)
#     accesstype = models.SmallIntegerField()

#     class Meta:
#         managed = False
#         db_table = 'annotation'


# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=150)

#     class Meta:
#         managed = False
#         db_table = 'auth_group'


# class AuthGroupPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)


# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)


# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.BooleanField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.BooleanField()
#     is_active = models.BooleanField()
#     date_joined = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'auth_user'


# class AuthUserGroups(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)


# class AuthUserUserPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)


class Bank(models.Model):
    code = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    display_name = models.CharField(max_length=255, blank=True, null=True)
    is_allowed_direct_debit = models.BooleanField()
    bank_email = models.TextField(blank=True, null=True)
    position_order = models.IntegerField()
    logo_bank_file = models.CharField(max_length=255, blank=True, null=True)
    swift_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "bank"


# class BatchUploadJob(models.Model):
#     uid = models.CharField(primary_key=True, max_length=32)
#     batch_id = models.CharField(max_length=255)
#     date_created = models.DateTimeField()
#     date_started = models.DateTimeField(blank=True, null=True)
#     date_completed = models.DateTimeField(blank=True, null=True)
#     status = models.IntegerField()
#     priority = models.IntegerField(blank=True, null=True)
#     execution_logs = models.TextField(blank=True, null=True)
#     creator_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='creator_uid')
#     object_name = models.CharField(max_length=50)
#     object_type = models.IntegerField()
#     reader_type = models.IntegerField()
#     filename = models.CharField(max_length=100, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'batch_upload_job'


class CalculationRule(models.Model):
    merchant_id = models.IntegerField(primary_key=True)
    company_name = models.CharField(max_length=50, blank=True, null=True)
    calculation_rule_creditcard = models.CharField(max_length=50, blank=True, null=True)
    calculation_rule_casa = models.CharField(max_length=50, blank=True, null=True)
    calculation_rule_instant_pay = models.CharField(
        max_length=50, blank=True, null=True
    )
    calculation_rule_setup_fees = models.CharField(max_length=50, blank=True, null=True)
    is_live = models.BooleanField()
    calculation_rule_minimum_fee = models.CharField(
        max_length=50, blank=True, null=True
    )
    calculation_rule_credit_card_fee = models.CharField(
        max_length=50, blank=True, null=True
    )
    calculation_rule_mandate_fee = models.CharField(
        max_length=250, blank=True, null=True
    )
    calculation_rule_cc_discount = models.CharField(
        max_length=10, blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "calculation_rule"


# class Classification(models.Model):
#     uid = models.CharField(primary_key=True, max_length=32)
#     title = models.CharField(max_length=255, blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     notes = models.TextField(blank=True, null=True)
#     number = models.CharField(max_length=20, blank=True, null=True)
#     number_pattern = models.CharField(max_length=20, blank=True, null=True)
#     next_child_classification_number = models.IntegerField(
#         blank=True, null=True)
#     next_child_record_number = models.IntegerField(blank=True, null=True)
#     init_child_classification_number = models.IntegerField(
#         blank=True, null=True)
#     child_classification_number_increment = models.IntegerField()
#     init_child_record_number = models.IntegerField(blank=True, null=True)
#     child_record_number_increment = models.IntegerField()
#     retention_schedule_uid = models.ForeignKey(
#         'RetentionSchedule', models.DO_NOTHING, db_column='retention_schedule_uid', blank=True, null=True)
#     is_top_level = models.SmallIntegerField(blank=True, null=True)
#     parent_uid = models.ForeignKey(
#         'self', models.DO_NOTHING, db_column='parent_uid', blank=True, null=True)
#     full_number = models.CharField(
#         unique=True, max_length=255, blank=True, null=True)
#     child_classification_number_pattern = models.CharField(
#         max_length=20, blank=True, null=True)
#     child_record_number_pattern = models.CharField(
#         max_length=20, blank=True, null=True)
#     current_classification_year = models.IntegerField()
#     current_record_year = models.IntegerField()
#     reset_child_classification_number_at_year_end = models.SmallIntegerField()
#     reset_child_record_number_at_year_end = models.SmallIntegerField()
#     acl_uid = models.CharField(max_length=32, blank=True, null=True)
#     default_acl_uid = models.CharField(max_length=32, blank=True, null=True)
#     uncompressed_number = models.CharField(
#         max_length=20, blank=True, null=True)
#     uncompressed_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     default_security_level_uid = models.ForeignKey(
#         'SecurityLevel', models.DO_NOTHING, db_column='default_security_level_uid', blank=True, null=True)
#     can_have_child_records = models.SmallIntegerField()
#     cumulative_child_uids = models.TextField(blank=True, null=True)
#     date_created = models.DateTimeField(blank=True, null=True)
#     active_from = models.DateTimeField(blank=True, null=True)
#     active_to = models.DateTimeField(blank=True, null=True)
#     default_record_class = models.IntegerField()
#     is_combined_title_inherits_from_parent = models.SmallIntegerField()
#     is_inherit_retention_schedule_from_parent = models.SmallIntegerField()
#     is_auto_update_security_level = models.SmallIntegerField()
#     is_auto_update_security_level_on_particular_date = models.SmallIntegerField()
#     security_level_trigger_date = models.DateTimeField(blank=True, null=True)
#     is_update_security_level_on_triggered_event = models.SmallIntegerField()
#     security_level_triggered_event = models.IntegerField(blank=True, null=True)
#     security_level_triggered_event_type = models.IntegerField(
#         blank=True, null=True)
#     security_level_triggered_event_duration = models.IntegerField(
#         blank=True, null=True)
#     security_level_triggered_event_property = models.CharField(
#         max_length=32, blank=True, null=True)
#     auto_update_security_level_id = models.CharField(
#         max_length=32, blank=True, null=True)
#     creator_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='creator_uid', blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'classification'


# class ClassificationRel(models.Model):
#     from_classification_uid = models.CharField(primary_key=True, max_length=65)
#     to_classification_uid = models.CharField(max_length=65)
#     classification_rel_uid = models.CharField(max_length=5)

#     class Meta:
#         managed = False
#         db_table = 'classification_rel'
#         unique_together = (('from_classification_uid',
#                            'to_classification_uid', 'classification_rel_uid'),)


# class ClassificationRelType(models.Model):
#     uid = models.CharField(primary_key=True, max_length=5)
#     rel_name = models.CharField(max_length=50)

#     class Meta:
#         managed = False
#         db_table = 'classification_rel_type'


# class CollectionDaily(models.Model):
#     id = models.IntegerField(primary_key=True)
#     merchant = models.ForeignKey('Merchant', models.DO_NOTHING)
#     amount_success = models.DecimalField(
#         max_digits=20, decimal_places=2, blank=True, null=True)
#     no_success = models.IntegerField(blank=True, null=True)
#     amount_pending = models.DecimalField(
#         max_digits=20, decimal_places=2, blank=True, null=True)
#     no_pending = models.IntegerField(blank=True, null=True)
#     amount_rejected = models.DecimalField(
#         max_digits=20, decimal_places=2, blank=True, null=True)
#     no_rejected = models.IntegerField(blank=True, null=True)
#     date_collection = models.DateField(blank=True, null=True)
#     amount_estimate = models.DecimalField(
#         max_digits=20, decimal_places=2, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'collection_daily'


# class CollectionDisplaySetting(models.Model):
#     merchant_id = models.IntegerField(primary_key=True)
#     collection_batch = models.BooleanField(blank=True, null=True)
#     collection_bank_name = models.BooleanField(blank=True, null=True)
#     collection_purpose = models.BooleanField(blank=True, null=True)
#     collection_amount = models.BooleanField(blank=True, null=True)
#     collection_package = models.BooleanField(blank=True, null=True)
#     collection_details = models.BooleanField(blank=True, null=True)
#     collection_link_id = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'collection_display_setting'


# class CollectionGraphSetting(models.Model):
#     id = models.IntegerField(primary_key=True)
#     month_start = models.IntegerField(blank=True, null=True)
#     year_start = models.IntegerField(blank=True, null=True)
#     mandate_target_jan = models.DecimalField(
#         max_digits=20, decimal_places=2, blank=True, null=True)
#     mandate_target_feb = models.DecimalField(
#         max_digits=20, decimal_places=2, blank=True, null=True)
#     mandate_target_mac = models.DecimalField(
#         max_digits=20, decimal_places=2, blank=True, null=True)
#     mandate_target_apr = models.DecimalField(
#         max_digits=20, decimal_places=2, blank=True, null=True)
#     mandate_target_may = models.DecimalField(
#         max_digits=20, decimal_places=2, blank=True, null=True)
#     mandate_target_june = models.DecimalField(
#         max_digits=20, decimal_places=2, blank=True, null=True)
#     mandate_target_july = models.DecimalField(
#         max_digits=20, decimal_places=2, blank=True, null=True)
#     mandate_target_aug = models.DecimalField(
#         max_digits=20, decimal_places=2, blank=True, null=True)
#     mandate_target_sept = models.DecimalField(
#         max_digits=20, decimal_places=2, blank=True, null=True)
#     mandate_target_oct = models.DecimalField(
#         max_digits=20, decimal_places=2, blank=True, null=True)
#     mandate_target_nov = models.DecimalField(
#         max_digits=20, decimal_places=2, blank=True, null=True)
#     mandate_target_dec = models.DecimalField(
#         max_digits=20, decimal_places=2, blank=True, null=True)
#     instant_target_jan = models.DecimalField(
#         max_digits=20, decimal_places=2, blank=True, null=True)
#     instant_target_feb = models.DecimalField(
#         max_digits=20, decimal_places=2, blank=True, null=True)
#     instant_target_mac = models.DecimalField(
#         max_digits=20, decimal_places=2, blank=True, null=True)
#     instant_target_apr = models.DecimalField(
#         max_digits=20, decimal_places=2, blank=True, null=True)
#     instant_target_may = models.DecimalField(
#         max_digits=20, decimal_places=2, blank=True, null=True)
#     instant_target_june = models.DecimalField(
#         max_digits=20, decimal_places=2, blank=True, null=True)
#     instant_target_july = models.DecimalField(
#         max_digits=20, decimal_places=2, blank=True, null=True)
#     instant_target_aug = models.DecimalField(
#         max_digits=20, decimal_places=2, blank=True, null=True)
#     instant_target_sept = models.DecimalField(
#         max_digits=20, decimal_places=2, blank=True, null=True)
#     instant_target_oct = models.DecimalField(
#         max_digits=20, decimal_places=2, blank=True, null=True)
#     instant_target_nov = models.DecimalField(
#         max_digits=20, decimal_places=2, blank=True, null=True)
#     instant_target_dec = models.DecimalField(
#         max_digits=20, decimal_places=2, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'collection_graph_setting'


# class CollectionJobMerchantLock(models.Model):
#     merchant = models.OneToOneField(
#         'Merchant', models.DO_NOTHING, primary_key=True)

#     class Meta:
#         managed = False
#         db_table = 'collection_job_merchant_lock'


# class CollectionOverallMerchant(models.Model):
#     id = models.IntegerField(primary_key=True)
#     merchant = models.ForeignKey(
#         'Merchant', models.DO_NOTHING, blank=True, null=True)
#     total_success = models.DecimalField(
#         max_digits=20, decimal_places=2, blank=True, null=True)
#     total_number_success = models.IntegerField()
#     total_pending = models.DecimalField(
#         max_digits=20, decimal_places=2, blank=True, null=True)
#     total_number_pending = models.IntegerField()
#     total_rejected = models.DecimalField(
#         max_digits=20, decimal_places=2, blank=True, null=True)
#     total_number_rejected = models.IntegerField()
#     instant_pay_success = models.DecimalField(
#         max_digits=20, decimal_places=2, blank=True, null=True)
#     no_ip_success = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'collection_overall_merchant'


# class CommunicationHistory(models.Model):
#     event_timestamp = models.DateTimeField()
#     node_uid = models.ForeignKey(
#         'RecordNode', models.DO_NOTHING, db_column='node_uid')
#     node_record_number = models.CharField(max_length=50, blank=True, null=True)
#     node_title = models.CharField(max_length=255)
#     principal_uid = models.CharField(max_length=32)
#     principal_name = models.CharField(max_length=255)
#     ip_address = models.CharField(max_length=45, blank=True, null=True)
#     to_address = models.TextField(blank=True, null=True)
#     cc_address = models.TextField(blank=True, null=True)
#     from_address = models.CharField(max_length=255, blank=True, null=True)
#     bcc_address = models.TextField(blank=True, null=True)
#     subject = models.TextField(blank=True, null=True)
#     body = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'communication_history'


# class ContainerContainee(models.Model):
#     container_uid = models.CharField(primary_key=True, max_length=65)
#     containee_uid = models.CharField(unique=True, max_length=65)
#     enclosure_number = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'container_containee'
#         unique_together = (('container_uid', 'containee_uid'),)


# class Content(models.Model):
#     uid = models.CharField(primary_key=True, max_length=32)
#     node_uid = models.CharField(max_length=65)
#     version = models.IntegerField()
#     filename = models.CharField(max_length=255)
#     filesize = models.BigIntegerField()
#     date_last_modified = models.DateTimeField(blank=True, null=True)
#     date_created = models.DateTimeField(blank=True, null=True)
#     store_uid = models.ForeignKey(
#         'Store', models.DO_NOTHING, db_column='store_uid')
#     mimetype = models.CharField(max_length=255, blank=True, null=True)
#     encryption = models.SmallIntegerField()
#     encryption_password = models.CharField(
#         max_length=255, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'content'
#         unique_together = (('node_uid', 'version'),)


# class CreditCardToken(models.Model):
#     credit_card_token = models.CharField(primary_key=True, max_length=255)
#     card_issuer = models.CharField(max_length=255, blank=True, null=True)
#     card_expiry = models.CharField(max_length=4, blank=True, null=True)
#     card_brand = models.CharField(max_length=15, blank=True, null=True)
#     card_funding_method = models.CharField(max_length=6, blank=True, null=True)
#     card_number = models.CharField(max_length=20, blank=True, null=True)
#     card_scheme = models.CharField(max_length=15, blank=True, null=True)
#     merchant_id = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'credit_card_token'


# class Currency(models.Model):
#     currency_code = models.IntegerField(primary_key=True)
#     currency = models.CharField(max_length=3, blank=True, null=True)
#     currency_name = models.CharField(max_length=255, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'currency'


class Customer(models.Model):
    id_type = models.IntegerField(blank=True, null=True)
    id_value = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    principal_uid = models.CharField(max_length=255, blank=True, null=True)
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = "customer"


class CustomerBankAccount(models.Model):
    account_number = models.CharField(max_length=255, blank=True, null=True)
    bank = models.ForeignKey(Bank, models.DO_NOTHING, blank=True, null=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "customer_bank_account"


class CustomerBankAccounts(models.Model):
    customer = models.ForeignKey(Customer, models.DO_NOTHING)
    bank_accounts = models.OneToOneField(CustomerBankAccount, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "customer_bank_accounts"


# class DatabaseSchema(models.Model):
#     version = models.CharField(max_length=50)

#     class Meta:
#         managed = False
#         db_table = 'database_schema'


# class DigitalSignature(models.Model):
#     uid = models.CharField(primary_key=True, max_length=32)
#     node_uid = models.CharField(max_length=65)
#     signature = models.BinaryField(blank=True, null=True)
#     certificate = models.BinaryField(blank=True, null=True)
#     date_signed = models.DateTimeField(blank=True, null=True)
#     signer = models.CharField(max_length=255, blank=True, null=True)
#     acl_uid = models.CharField(max_length=32, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'digital_signature'


# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.SmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey(
#         'DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'


# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)


# class DjangoMigrations(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_migrations'


# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_session'


# class EbnQueue(models.Model):
#     uid = models.CharField(primary_key=True, max_length=32)
#     date_added_to_queue = models.DateTimeField(blank=True, null=True)
#     subject = models.CharField(max_length=255, blank=True, null=True)
#     message = models.TextField(blank=True, null=True)
#     send_as_bcc = models.SmallIntegerField()
#     recipients = models.TextField(blank=True, null=True)
#     reply_to = models.CharField(max_length=255, blank=True, null=True)
#     method = models.SmallIntegerField()
#     sent = models.SmallIntegerField()
#     date_sent = models.DateTimeField(blank=True, null=True)
#     urgent = models.SmallIntegerField()
#     no_of_retries = models.SmallIntegerField()
#     cc = models.TextField(blank=True, null=True)
#     full_name = models.TextField(blank=True, null=True)
#     can_send_calendar_email = models.SmallIntegerField()
#     node_uid = models.CharField(max_length=255, blank=True, null=True)
#     can_attach_email_content = models.SmallIntegerField()

#     class Meta:
#         managed = False
#         db_table = 'ebn_queue'


# class EmailClient(models.Model):
#     email_header = models.CharField(primary_key=True, max_length=255)
#     cataloged = models.SmallIntegerField()

#     class Meta:
#         managed = False
#         db_table = 'email_client'


# class EmailLink(models.Model):
#     uid = models.CharField(primary_key=True, max_length=32)
#     acl_uid = models.CharField(max_length=32, blank=True, null=True)
#     link_id = models.CharField(max_length=32, blank=True, null=True)
#     node_id = models.CharField(max_length=65)
#     is_used = models.SmallIntegerField()

#     class Meta:
#         managed = False
#         db_table = 'email_link'


# class EmailTemplate(models.Model):
#     uid = models.CharField(primary_key=True, max_length=32)
#     name = models.CharField(max_length=100)
#     description = models.CharField(max_length=255, blank=True, null=True)
#     acl_uid = models.CharField(max_length=32, blank=True, null=True)
#     sl_create_evt = models.CharField(max_length=255, blank=True, null=True)
#     sl_change_evt = models.CharField(max_length=255, blank=True, null=True)
#     sl_delete_evt = models.CharField(max_length=255, blank=True, null=True)
#     sl_sched_evt = models.CharField(max_length=255, blank=True, null=True)
#     msg_create_evt = models.TextField(blank=True, null=True)
#     msg_change_evt = models.TextField(blank=True, null=True)
#     msg_delete_evt = models.TextField(blank=True, null=True)
#     msg_sched_evt = models.TextField(blank=True, null=True)
#     is_calendar_update_email = models.SmallIntegerField()
#     is_calendar_create_email = models.SmallIntegerField()
#     is_calendar_delete_email = models.SmallIntegerField()
#     is_update_email_content = models.SmallIntegerField()
#     is_create_email_content = models.SmallIntegerField()
#     is_delete_email_content = models.SmallIntegerField()

#     class Meta:
#         managed = False
#         db_table = 'email_template'


# class Employee(models.Model):
#     id = models.IntegerField(primary_key=True)
#     manager = models.ForeignKey(
#         'self', models.DO_NOTHING, blank=True, null=True)
#     merchant = models.ForeignKey(
#         'Merchant', models.DO_NOTHING, blank=True, null=True)
#     name = models.CharField(max_length=255, blank=True, null=True)
#     principal_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='principal_uid', blank=True, null=True)
#     special_permission = models.BooleanField(blank=True, null=True)
#     enable_view_all_collection = models.BooleanField(blank=True, null=True)
#     impersonator = models.BooleanField(blank=True, null=True)
#     tfa_is_setup = models.BooleanField(blank=True, null=True)
#     tfa_secret = models.CharField(max_length=255, blank=True, null=True)
#     super_user = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'employee'


# class EscalationInstance(models.Model):
#     uid = models.CharField(primary_key=True, max_length=32)
#     task_instance_uid = models.ForeignKey(
#         'TaskInstance', models.DO_NOTHING, db_column='task_instance_uid', blank=True, null=True)
#     expiry_date = models.DateTimeField(blank=True, null=True)
#     target_actor = models.CharField(max_length=50, blank=True, null=True)
#     target_group = models.CharField(max_length=50, blank=True, null=True)
#     date_escalated = models.DateTimeField(blank=True, null=True)
#     on_escalate = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'escalation_instance'


# class EsignTask(models.Model):
#     uid = models.CharField(primary_key=True, max_length=32)
#     esign_wflow_uid = models.ForeignKey(
#         'EsignWflow', models.DO_NOTHING, db_column='esign_wflow_uid')
#     signatory_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='signatory_uid', blank=True, null=True)
#     signatory_name = models.CharField(max_length=255)
#     signatory_email = models.CharField(max_length=255)
#     start_ts = models.DateTimeField(blank=True, null=True)
#     end_ts = models.DateTimeField(blank=True, null=True)
#     status = models.SmallIntegerField()
#     seq_number = models.IntegerField()
#     esign = models.BinaryField(blank=True, null=True)
#     rejection_reason = models.TextField(blank=True, null=True)
#     visual_signature = models.BinaryField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'esign_task'
#         unique_together = (('esign_wflow_uid', 'seq_number'),)


# class EsignWflow(models.Model):
#     uid = models.CharField(primary_key=True, max_length=32)
#     node_uid = models.ForeignKey(
#         'RecordNode', models.DO_NOTHING, db_column='node_uid')
#     message = models.TextField(blank=True, null=True)
#     status = models.SmallIntegerField()
#     esign_type = models.SmallIntegerField()
#     initiator_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='initiator_uid')
#     abortion_reason = models.TextField(blank=True, null=True)
#     esign = models.BinaryField(blank=True, null=True)
#     start_ts = models.DateTimeField(blank=True, null=True)
#     end_ts = models.DateTimeField(blank=True, null=True)
#     bank_type = models.SmallIntegerField()
#     use_guard_time = models.SmallIntegerField()

#     class Meta:
#         managed = False
#         db_table = 'esign_wflow'


# class EvtBasedNotification(models.Model):
#     uid = models.CharField(primary_key=True, max_length=32)
#     name = models.CharField(max_length=50)
#     description = models.CharField(max_length=255, blank=True, null=True)
#     acl_uid = models.CharField(max_length=32, blank=True, null=True)
#     active_from = models.DateTimeField(blank=True, null=True)
#     active_to = models.DateTimeField(blank=True, null=True)
#     suspend = models.SmallIntegerField()
#     nodetype_uid = models.ForeignKey(
#         'Nodetype', models.DO_NOTHING, db_column='nodetype_uid')
#     use_node_filter_script = models.SmallIntegerField()
#     node_filter_script = models.TextField(blank=True, null=True)
#     notify_on_create_event = models.SmallIntegerField()
#     notify_on_change_event = models.SmallIntegerField()
#     notify_on_delete_event = models.SmallIntegerField()
#     urgent = models.SmallIntegerField()
#     send_as_bcc = models.SmallIntegerField()
#     email_template_uid = models.ForeignKey(
#         EmailTemplate, models.DO_NOTHING, db_column='email_template_uid', blank=True, null=True)
#     recipients_email = models.TextField(blank=True, null=True)
#     include_assignee = models.SmallIntegerField()
#     include_home = models.SmallIntegerField()
#     include_owner = models.SmallIntegerField()
#     include_members_of_group = models.SmallIntegerField()
#     group_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='group_uid', blank=True, null=True)
#     include_principals_from_property = models.SmallIntegerField()
#     property_uid = models.ForeignKey(
#         'Property', models.DO_NOTHING, db_column='property_uid', blank=True, null=True)
#     sender_email = models.CharField(max_length=255, blank=True, null=True)
#     cc_email = models.TextField(blank=True, null=True)
#     include_principals_from_propertycc = models.SmallIntegerField()
#     propertycc_uid = models.CharField(max_length=32, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'evt_based_notification'


# class ExportJob(models.Model):
#     uid = models.CharField(primary_key=True, max_length=32)
#     date_created = models.DateTimeField()
#     date_started = models.DateTimeField(blank=True, null=True)
#     date_completed = models.DateTimeField(blank=True, null=True)
#     date_expired = models.DateTimeField(blank=True, null=True)
#     status = models.IntegerField()
#     email = models.CharField(max_length=255)
#     object_uids = models.TextField(blank=True, null=True)
#     object_type = models.CharField(max_length=100)
#     impersonator_username = models.CharField(max_length=50)
#     preferences = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'export_job'


# class Favourites(models.Model):
#     uid = models.CharField(primary_key=True, max_length=32)
#     favouriteschildname = models.CharField(max_length=50)
#     principal_uid = models.CharField(max_length=32, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'favourites'


# class FileProcessing(models.Model):
#     type = models.CharField(max_length=30, blank=True, null=True)
#     bank_code = models.CharField(max_length=10, blank=True, null=True)
#     date_upload = models.DateTimeField(blank=True, null=True)
#     date_processed = models.DateTimeField(blank=True, null=True)
#     filename = models.CharField(max_length=100, blank=True, null=True)
#     status = models.CharField(max_length=10, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'file_processing'


# class Ftextindex(models.Model):
#     uid = models.CharField(primary_key=True, max_length=32)
#     insertion_timestamp = models.DateTimeField()
#     nodetype_id = models.CharField(max_length=32)
#     node_id = models.CharField(max_length=65)
#     index_code = models.SmallIntegerField()
#     target = models.CharField(max_length=1, blank=True, null=True)
#     completion_status = models.CharField(max_length=1, blank=True, null=True)
#     exception = models.CharField(max_length=255, blank=True, null=True)
#     index_timestamp = models.DateTimeField(blank=True, null=True)
#     completion_timestamp = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'ftextindex'


# class Gadget(models.Model):
#     uid = models.CharField(primary_key=True, max_length=32)
#     acl_uid = models.CharField(max_length=32, blank=True, null=True)
#     title = models.CharField(max_length=50)
#     col_maximized = models.CharField(max_length=200, blank=True, null=True)
#     col_detail = models.CharField(max_length=200, blank=True, null=True)
#     col_report_type = models.CharField(max_length=200, blank=True, null=True)
#     col_parameter = models.CharField(max_length=200, blank=True, null=True)
#     col_padding = models.CharField(max_length=200, blank=True, null=True)
#     html = models.CharField(max_length=500, blank=True, null=True)
#     icon = models.CharField(max_length=50)
#     url_link = models.CharField(max_length=500, blank=True, null=True)
#     style = models.CharField(max_length=200, blank=True, null=True)
#     is_auto_refresh = models.SmallIntegerField()
#     is_auto_scroll = models.SmallIntegerField()
#     gadget_type = models.SmallIntegerField()
#     height = models.SmallIntegerField()
#     auto_refresh_interval = models.SmallIntegerField()
#     col_width = models.DecimalField(max_digits=5, decimal_places=2)
#     col_type = models.SmallIntegerField()

#     class Meta:
#         managed = False
#         db_table = 'gadget'


# class Hold(models.Model):
#     uid = models.CharField(primary_key=True, max_length=32)
#     name = models.CharField(max_length=50)
#     acl_uid = models.ForeignKey(
#         Acl, models.DO_NOTHING, db_column='acl_uid', blank=True, null=True)
#     description = models.CharField(max_length=255, blank=True, null=True)
#     active_from = models.DateTimeField(blank=True, null=True)
#     active_to = models.DateTimeField(blank=True, null=True)
#     contact_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='contact_uid', blank=True, null=True)
#     only_prevent_disposition_changes = models.SmallIntegerField(
#         blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'hold'


# class HoldNode(models.Model):
#     hold_uid = models.OneToOneField(
#         Hold, models.DO_NOTHING, db_column='hold_uid', primary_key=True)
#     node_uid = models.CharField(max_length=65)

#     class Meta:
#         managed = False
#         db_table = 'hold_node'
#         unique_together = (('hold_uid', 'node_uid'),)


# class HolidayCalendar(models.Model):
#     uid = models.CharField(primary_key=True, max_length=32)
#     holiday_name = models.TextField(blank=True, null=True)
#     holiday_description = models.TextField(blank=True, null=True)
#     holiday_end_date = models.DateField(blank=True, null=True)
#     holiday_start_date = models.DateField(blank=True, null=True)
#     principal_uid = models.CharField(max_length=32, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'holiday_calendar'


# class JobQueue(models.Model):
#     job_type = models.CharField(max_length=255)
#     job_method = models.CharField(max_length=255)
#     status = models.CharField(max_length=255)
#     date_started = models.DateTimeField(blank=True, null=True)
#     date_created = models.DateTimeField(blank=True, null=True)
#     date_finished = models.DateTimeField(blank=True, null=True)
#     job_content = models.TextField(blank=True, null=True)
#     job_result = models.TextField(blank=True, null=True)
#     merchant = models.ForeignKey('Merchant', models.DO_NOTHING)
#     call_back_url = models.CharField(max_length=255, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'job_queue'


# class LoginFail(models.Model):
#     username = models.CharField(max_length=50)
#     login_fail_timestamp = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'login_fail'


# class LoginPolicy(models.Model):
#     uid = models.CharField(primary_key=True, max_length=32)
#     attributes = models.TextField(blank=True, null=True)
#     is_on = models.SmallIntegerField()

#     class Meta:
#         managed = False
#         db_table = 'login_policy'


# class Lookupitem(models.Model):
#     uid = models.CharField(primary_key=True, max_length=32)
#     lookupset_uid = models.ForeignKey(
#         'Lookupset', models.DO_NOTHING, db_column='lookupset_uid')
#     code = models.CharField(max_length=20)
#     val = models.CharField(max_length=100)
#     description = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'lookupitem'
#         unique_together = (('lookupset_uid', 'code'),)


# class Lookupset(models.Model):
#     uid = models.CharField(primary_key=True, max_length=32)
#     name = models.CharField(unique=True, max_length=255)
#     description = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'lookupset'


class Mandate(models.Model):
    id = models.IntegerField(primary_key=True)
    business_model = models.IntegerField(blank=True, null=True)
    date_created = models.DateTimeField()
    purpose_of_payment = models.CharField(max_length=255, blank=True, null=True)
    reference_number = models.CharField(max_length=255, blank=True, null=True)
    effective_date = models.DateTimeField(blank=True, null=True)
    expiry_date = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    buyer = models.ForeignKey(
        "MandateParty", models.DO_NOTHING, blank=True, null=True, related_name="buyer"
    )
    employee_id = models.IntegerField(blank=True, null=True)
    merchant = models.ForeignKey(
        "MandateParty",
        models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="merchant",
    )
    batch_id = models.CharField(max_length=255, blank=True, null=True)
    is_paper_mandate = models.BooleanField(blank=True, null=True)
    pre_approved = models.BooleanField(blank=True, null=True)
    cc_email = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "mandate"


class MandateCollection(models.Model):
    id = models.IntegerField(primary_key=True)
    amount_original = models.DecimalField(
        max_digits=19, decimal_places=2, blank=True, null=True
    )
    amount_collection = models.DecimalField(
        max_digits=19, decimal_places=2, blank=True, null=True
    )
    collection_date = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    batch_id = models.CharField(max_length=225, blank=True, null=True)
    transaction_id = models.CharField(max_length=50, blank=True, null=True)
    mandate_reference_no = models.CharField(max_length=255, blank=True, null=True)
    email_reminder = models.IntegerField(blank=True, null=True)
    merchant_id = models.IntegerField(blank=True, null=True)
    response_date = models.DateTimeField(blank=True, null=True)
    response_batch = models.CharField(max_length=255, blank=True, null=True)
    number_retry = models.IntegerField(blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    mode_created = models.IntegerField(blank=True, null=True)
    payment_method = models.IntegerField(blank=True, null=True)
    cc_authorisation_code = models.CharField(max_length=100, blank=True, null=True)
    cc_transaction_id = models.CharField(max_length=255, blank=True, null=True)
    retry_count = models.IntegerField(blank=True, null=True)
    retry_max = models.IntegerField(blank=True, null=True)
    retry_triggered = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "mandate_collection"


class MandateCollectionBatch(models.Model):
    batch_id = models.CharField(primary_key=True, max_length=255)
    date_created = models.DateTimeField(blank=True, null=True)
    merchant_id = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    file_location = models.CharField(max_length=1000, blank=True, null=True)
    collection_date = models.DateTimeField(blank=True, null=True)
    is_auto_collection = models.BooleanField(blank=True, null=True)
    payment_method = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "mandate_collection_batch"


class MandateCollectionBatchCollections(models.Model):
    mandate_collection_batch_batch = models.ForeignKey(
        MandateCollectionBatch, models.DO_NOTHING, blank=True, null=True
    )
    collections = models.OneToOneField(MandateCollection, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "mandate_collection_batch_collections"


class MandateCollectionItem(models.Model):
    item = models.CharField(max_length=255, blank=True, null=True)
    amount = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    collection = models.ForeignKey(
        MandateCollection, models.DO_NOTHING, blank=True, null=True
    )
    description = models.CharField(max_length=255, blank=True, null=True)
    customer_uid = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "mandate_collection_item"


class MandateCollectionItems(models.Model):
    mandate_collection = models.ForeignKey(MandateCollection, models.DO_NOTHING)
    items = models.ForeignKey(MandateCollectionItem, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "mandate_collection_items"


class MandateDetails(models.Model):
    details_id = models.AutoField(primary_key=True)
    details_number = models.CharField(max_length=255, blank=True, null=True)
    details_description = models.CharField(max_length=255, blank=True, null=True)
    details_amount = models.DecimalField(
        max_digits=16, decimal_places=2, blank=True, null=True
    )
    details_created = models.DateTimeField(blank=True, null=True)
    details_change_by = models.CharField(max_length=255, blank=True, null=True)
    details_mandate_id = models.IntegerField(blank=True, null=True)
    details_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "mandate_details"


class MandateInstantPay(models.Model):
    order_no = models.CharField(max_length=50)
    date_created = models.DateTimeField()
    merchant = models.ForeignKey("Merchant", models.DO_NOTHING)
    description = models.CharField(max_length=225, blank=True, null=True)
    amount = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True
    )
    status = models.IntegerField(blank=True, null=True)
    fpx_transaction_id = models.CharField(max_length=255, blank=True, null=True)
    effective_date = models.DateTimeField(blank=True, null=True)
    buyer_id = models.IntegerField(blank=True, null=True)
    employee_id = models.IntegerField(blank=True, null=True)
    mandate_id = models.IntegerField(blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    check_status_count = models.IntegerField(blank=True, null=True)
    fpx_transaction_date = models.DateTimeField(blank=True, null=True)
    node_id = models.CharField(max_length=255, blank=True, null=True)
    fpx_buyer_name = models.CharField(max_length=255, blank=True, null=True)
    bank = models.ForeignKey(Bank, models.DO_NOTHING, blank=True, null=True)
    business_model = models.IntegerField(blank=True, null=True)
    creation_mode = models.IntegerField(blank=True, null=True)
    merchant_url = models.CharField(max_length=255, blank=True, null=True)
    merchant_callback_url = models.CharField(max_length=255, blank=True, null=True)
    ip_phone_number = models.CharField(max_length=255, blank=True, null=True)
    ip_property_one = models.TextField(blank=True, null=True)
    ip_property_two = models.TextField(blank=True, null=True)
    attached_file_location = models.CharField(max_length=255, blank=True, null=True)
    payment_method = models.IntegerField(blank=True, null=True)
    cc_card_number = models.CharField(max_length=20, blank=True, null=True)
    cc_funding_method = models.CharField(max_length=6, blank=True, null=True)
    cc_issuer = models.CharField(max_length=255, blank=True, null=True)
    ac_direct = models.IntegerField(blank=True, null=True)
    ac_indirect = models.IntegerField(blank=True, null=True)
    cc_email = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "mandate_instant_pay"


class MandateInstantPayTermsConditions(models.Model):
    mandate_instant_pay = models.ForeignKey(
        MandateInstantPay, models.DO_NOTHING, blank=True, null=True
    )
    terms_conditions_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "mandate_instant_pay_terms_conditions"


class MandateOrder(models.Model):
    merchant_id = models.IntegerField(blank=True, null=True)
    transaction = models.ForeignKey(
        "MandateTransaction", models.DO_NOTHING, blank=True, null=True
    )
    collection_id = models.IntegerField(blank=True, null=True)
    order_amount = models.DecimalField(
        max_digits=16, decimal_places=2, blank=True, null=True
    )
    date_created = models.DateTimeField(blank=True, null=True)
    collection_date = models.DateField(blank=True, null=True)
    collection_triggered = models.BooleanField(blank=True, null=True)
    collection_status = models.IntegerField(blank=True, null=True)
    collection_retry = models.IntegerField(blank=True, null=True)
    collection_cancel = models.BooleanField(blank=True, null=True)
    date_cancel = models.DateTimeField(blank=True, null=True)
    order_retry = models.BooleanField(blank=True, null=True)
    creation_method = models.IntegerField(blank=True, null=True)
    order_date = models.DateTimeField(blank=True, null=True)
    collection_max_retry = models.IntegerField(blank=True, null=True)
    reference_id = models.CharField(max_length=255, blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    collection_disabled = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "mandate_order"


class MandateParty(models.Model):
    email_address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "mandate_party"


class MandatePayOnBehalf(models.Model):
    account_code = models.CharField(primary_key=True, max_length=255)
    mandate = models.ForeignKey(Mandate, models.DO_NOTHING)
    merchant = models.ForeignKey("Merchant", models.DO_NOTHING)
    mandate_details = models.OneToOneField(
        MandateDetails, models.DO_NOTHING, blank=True, null=True
    )
    date_created = models.DateTimeField(blank=True, null=True)
    date_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "mandate_pay_on_behalf"
        unique_together = (("account_code", "merchant"),)


class MandateRules(models.Model):
    mandate = models.ForeignKey(Mandate, models.DO_NOTHING)
    agree = models.BooleanField()
    amount = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True
    )
    date_period = models.DateTimeField(blank=True, null=True)
    amount_enable = models.BooleanField(blank=True, null=True)
    date_enable = models.BooleanField(blank=True, null=True)
    period = models.IntegerField(blank=True, null=True)
    period_option = models.IntegerField(blank=True, null=True)
    auto_expiry = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "mandate_rules"


class MandateTransaction(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    amount = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    date_created = models.DateTimeField()
    fpx_transaction_id = models.CharField(max_length=255, blank=True, null=True)
    frequency = models.IntegerField(blank=True, null=True)
    maximum_frequency = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    bank = models.ForeignKey(Bank, models.DO_NOTHING, blank=True, null=True)
    mandate = models.ForeignKey(Mandate, models.DO_NOTHING, blank=True, null=True)
    node_id = models.CharField(max_length=255, blank=True, null=True)
    terminate_reason = models.CharField(max_length=255, blank=True, null=True)
    principal_uid = models.ForeignKey(
        "Principal", models.DO_NOTHING, db_column="principal_uid", blank=True, null=True
    )
    reference_number = models.CharField(max_length=255, blank=True, null=True)
    customer_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    id_type = models.IntegerField(blank=True, null=True)
    id_value = models.CharField(max_length=255, blank=True, null=True)
    effective_date = models.DateTimeField(blank=True, null=True)
    expiry_date = models.DateTimeField(blank=True, null=True)
    purpose = models.CharField(max_length=255, blank=True, null=True)
    link_id = models.CharField(max_length=255, blank=True, null=True)
    check_status_count = models.IntegerField(blank=True, null=True)
    fpx_transaction_date = models.DateTimeField(blank=True, null=True)
    creation_mode = models.IntegerField(blank=True, null=True)
    fpx_buyer_name = models.CharField(max_length=255, blank=True, null=True)
    last_collection_date = models.DateTimeField(blank=True, null=True)
    default_collection_amount = models.DecimalField(
        max_digits=16, decimal_places=2, blank=True, null=True
    )
    additional_field_one = models.CharField(max_length=255, blank=True, null=True)
    additional_field_two = models.CharField(max_length=255, blank=True, null=True)
    attached_file_location = models.CharField(max_length=255, blank=True, null=True)
    merchant_url = models.CharField(max_length=255, blank=True, null=True)
    merchant_callback_url = models.TextField(blank=True, null=True)
    package_id = models.IntegerField(blank=True, null=True)
    allow_order = models.BooleanField(blank=True, null=True)
    order_triggered = models.IntegerField(blank=True, null=True)
    terminated_date = models.DateTimeField(blank=True, null=True)
    order_cancel_date = models.DateTimeField(blank=True, null=True)
    order_auto_cancel = models.BooleanField(blank=True, null=True)
    collection_date = models.CharField(max_length=255, blank=True, null=True)
    initial_collection_amount = models.DecimalField(
        max_digits=16, decimal_places=2, blank=True, null=True
    )
    initial_collection_opt = models.IntegerField(blank=True, null=True)
    start_collection_date = models.DateTimeField(blank=True, null=True)
    end_collection_date = models.DateTimeField(blank=True, null=True)
    payment_method = models.IntegerField(blank=True, null=True)
    cc_token = models.CharField(max_length=255, blank=True, null=True)
    terminate_email = models.CharField(max_length=255, blank=True, null=True)
    collection_count = models.IntegerField(blank=True, null=True)
    collection_auto_retry = models.IntegerField(blank=True, null=True)
    collection_retry_remark = models.TextField(blank=True, null=True)
    collection_remark = models.TextField(blank=True, null=True)
    additional_field_three = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "mandate_transaction"


class MandateTransactionCollections(models.Model):
    mandate_transaction = models.ForeignKey(
        MandateTransaction, models.DO_NOTHING, blank=True, null=True
    )
    collections = models.OneToOneField(MandateCollection, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "mandate_transaction_collections"


class MandateTransactionEnrp(models.Model):
    transaction = models.ForeignKey(MandateTransaction, models.DO_NOTHING)
    batch_id = models.CharField(max_length=50, blank=True, null=True)
    account_holder_name = models.CharField(max_length=225, blank=True, null=True)
    account_no = models.CharField(max_length=50, blank=True, null=True)
    fpx_approval_status = models.IntegerField(blank=True, null=True)
    record_number = models.CharField(max_length=225, blank=True, null=True)
    mandate_reference_number = models.CharField(max_length=255, blank=True, null=True)
    response_date = models.DateTimeField(blank=True, null=True)
    enrp_mandate_condition = models.IntegerField()
    is_credit_card = models.BooleanField(blank=True, null=True)
    meps_bank_code = models.CharField(max_length=255, blank=True, null=True)
    fpx_bank_code = models.CharField(max_length=10, blank=True, null=True)
    allow_auto_collection = models.IntegerField()
    date_deleted = models.DateTimeField(blank=True, null=True)
    encryption_key = models.CharField(max_length=255, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "mandate_transaction_enrp"


class MandateTransactionTermsConditions(models.Model):
    mandate_transaction = models.ForeignKey(
        MandateTransaction, models.DO_NOTHING, blank=True, null=True
    )
    terms_conditions_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "mandate_transaction_terms_conditions"


class MandateTransactions(models.Model):
    mandate = models.ForeignKey(Mandate, models.DO_NOTHING)
    transactions = models.OneToOneField(MandateTransaction, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "mandate_transactions"


class Merchant(models.Model):
    company_name = models.CharField(max_length=255, blank=True, null=True)
    company_registration_number = models.CharField(
        max_length=255, blank=True, null=True
    )
    logo_file_location = models.CharField(max_length=255, blank=True, null=True)
    seller_id = models.CharField(max_length=255, blank=True, null=True)
    id = models.IntegerField(primary_key=True)
    show_effective_date = models.BooleanField()
    show_expiry_date = models.BooleanField()
    show_max_frequency = models.BooleanField()
    default_max_frequency = models.IntegerField()
    b2c_display_value = models.CharField(max_length=100)
    b2b_display_value = models.CharField(max_length=100)
    default_check = models.CharField(max_length=4)
    b2c_min_amount = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True
    )
    b2c_max_amount = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True
    )
    b2b1_min_amount = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True
    )
    b2b1_max_amount = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True
    )
    link_id_display_value = models.CharField(max_length=255, blank=True, null=True)
    show_link_id = models.BooleanField(blank=True, null=True)
    reset_mandate_number_at_year_end = models.BooleanField(blank=True, null=True)
    next_mandate_number = models.IntegerField(blank=True, null=True)
    mandate_number_pattern = models.CharField(max_length=50, blank=True, null=True)
    init_mandate_number = models.IntegerField(blank=True, null=True)
    number_pattern_increment = models.IntegerField(blank=True, null=True)
    current_mandate_year = models.IntegerField(blank=True, null=True)
    instant_pay_order_no_pattern = models.CharField(
        max_length=50, blank=True, null=True
    )
    instant_pay_nextval = models.IntegerField(blank=True, null=True)
    instant_pay_init_number = models.IntegerField(blank=True, null=True)
    instant_pay_reset_no_year_end = models.BooleanField(blank=True, null=True)
    instant_pay_current_year = models.IntegerField(blank=True, null=True)
    instant_pay_number_increment = models.IntegerField(blank=True, null=True)
    amount_drop_list = models.BooleanField(blank=True, null=True)
    instant_pay_amount_drop_list = models.BooleanField(blank=True, null=True)
    instant_pay_min_amount = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True
    )
    instant_pay_max_amount = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True
    )
    set_default_rules = models.BooleanField(blank=True, null=True)
    default_rules_amount = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True
    )
    default_contract_date = models.DateTimeField(blank=True, null=True)
    default_mandate_limit = models.IntegerField()
    default_instant_limit = models.IntegerField()
    mandate_ref_no = models.BooleanField(blank=True, null=True)
    mandate_effective_date = models.BooleanField(blank=True, null=True)
    mandate_amount = models.BooleanField(blank=True, null=True)
    mandate_frequency = models.BooleanField(blank=True, null=True)
    mandate_customer_name = models.BooleanField(blank=True, null=True)
    mandate_customer_id = models.BooleanField(blank=True, null=True)
    mandate_person_in_charge = models.BooleanField(blank=True, null=True)
    mandate_status = models.BooleanField(blank=True, null=True)
    admin_land_page = models.IntegerField(blank=True, null=True)
    manager_land_page = models.IntegerField(blank=True, null=True)
    sales_land_page = models.IntegerField(blank=True, null=True)
    view_only_land_page = models.IntegerField(blank=True, null=True)
    cust_land_page = models.IntegerField(blank=True, null=True)
    short_name = models.CharField(max_length=50, blank=True, null=True)
    mandate_date_created = models.BooleanField(blank=True, null=True)
    mandate_transaction_date = models.BooleanField(blank=True, null=True)
    direct_debit_id = models.CharField(max_length=10, blank=True, null=True)
    enable_customer_edit = models.BooleanField(blank=True, null=True)
    set_service = models.BooleanField(blank=True, null=True)
    default_merchant_url = models.CharField(max_length=255, blank=True, null=True)
    default_merchant_called_back_url = models.CharField(
        max_length=255, blank=True, null=True
    )
    init_mandate_ref = models.IntegerField()
    mandate_ref_pattern = models.CharField(max_length=50)
    mandate_ref_next = models.IntegerField(blank=True, null=True)
    mandate_reference_auto = models.BooleanField()
    enrp_notification = models.BooleanField()
    enrp_reminder = models.IntegerField(blank=True, null=True)
    enrp_support = models.BooleanField(blank=True, null=True)
    enrp_merchant = models.BooleanField(blank=True, null=True)
    enrp_bank = models.BooleanField(blank=True, null=True)
    enrp_bank_email = models.TextField(blank=True, null=True)
    enrp_others = models.BooleanField(blank=True, null=True)
    enrp_others_email = models.TextField(blank=True, null=True)
    enable_collection_items = models.BooleanField(blank=True, null=True)
    enrp_merchant_email = models.TextField(blank=True, null=True)
    enrp_checking_from = models.DateTimeField(blank=True, null=True)
    res_notification = models.BooleanField(blank=True, null=True)
    res_interval_day = models.IntegerField(blank=True, null=True)
    res_support = models.BooleanField(blank=True, null=True)
    res_bank = models.BooleanField(blank=True, null=True)
    res_merchant = models.BooleanField(blank=True, null=True)
    res_others = models.BooleanField(blank=True, null=True)
    res_bank_email = models.TextField(blank=True, null=True)
    res_merchant_email = models.TextField(blank=True, null=True)
    res_others_email = models.TextField(blank=True, null=True)
    res_check_from = models.DateTimeField(blank=True, null=True)
    enable_ref1 = models.BooleanField(blank=True, null=True)
    enable_view_all = models.BooleanField(blank=True, null=True)
    enable_num_of_retry = models.BooleanField(blank=True, null=True)
    default_num_of_retry = models.IntegerField(blank=True, null=True)
    enable_auto_collection = models.BooleanField(blank=True, null=True)
    enable_merchant_callback = models.BooleanField(blank=True, null=True)
    b2b_duplicate_reference = models.IntegerField()
    term_condition_mandate = models.TextField(blank=True, null=True)
    term_condition_instant = models.TextField(blank=True, null=True)
    mandate_term_location = models.CharField(max_length=255, blank=True, null=True)
    instant_term_location = models.CharField(max_length=255, blank=True, null=True)
    merchant_password_strength = models.IntegerField(blank=True, null=True)
    b2b1_instant_pay_min_amount = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True
    )
    b2b1_instant_pay_max_amount = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True
    )
    enable_enrp = models.BooleanField(blank=True, null=True)
    mandate_form_dynamic = models.BooleanField()
    default_rules_amount_enable = models.BooleanField(blank=True, null=True)
    default_contract_date_enable = models.BooleanField(blank=True, null=True)
    auto_expiry_date = models.BooleanField(blank=True, null=True)
    merchant_email = models.CharField(max_length=255, blank=True, null=True)
    email_sender = models.CharField(max_length=255, blank=True, null=True)
    cft_failed_notification = models.BooleanField(blank=True, null=True)
    cft_failed_support = models.BooleanField(blank=True, null=True)
    cft_failed_bank = models.BooleanField(blank=True, null=True)
    cft_failed_merchant = models.BooleanField(blank=True, null=True)
    cft_failed_others = models.BooleanField(blank=True, null=True)
    cft_failed_bank_email = models.TextField(blank=True, null=True)
    cft_failed_merchant_email = models.TextField(blank=True, null=True)
    cft_failed_others_email = models.TextField(blank=True, null=True)
    set_secret = models.BooleanField(blank=True, null=True)
    secret_key = models.CharField(max_length=255, blank=True, null=True)
    default_collection_called_back_url = models.CharField(
        max_length=255, blank=True, null=True
    )
    enable_collection_called_back = models.BooleanField(blank=True, null=True)
    service_amount_readonly = models.BooleanField(blank=True, null=True)
    service_description_readonly = models.BooleanField(blank=True, null=True)
    mandate_expiry_notification = models.BooleanField(blank=True, null=True)
    mandate_expiry_support = models.BooleanField(blank=True, null=True)
    mandate_expiry_merchant = models.BooleanField(blank=True, null=True)
    mandate_expiry_others = models.BooleanField(blank=True, null=True)
    mandate_expiry_merchant_email = models.TextField(blank=True, null=True)
    mandate_expiry_others_email = models.TextField(blank=True, null=True)
    mandate_expiry_interval = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True
    )
    secondary_company_name = models.CharField(max_length=255, blank=True, null=True)
    enable_whats_app = models.BooleanField(blank=True, null=True)
    enable_autosend_receipt_collection = models.BooleanField(blank=True, null=True)
    phone_no = models.CharField(max_length=255, blank=True, null=True)
    company_address = models.TextField(blank=True, null=True)
    show_collection_amount = models.BooleanField(blank=True, null=True)
    ip_order_num = models.BooleanField(blank=True, null=True)
    ip_seller_exchanger_order_num = models.BooleanField(blank=True, null=True)
    ip_email = models.BooleanField(blank=True, null=True)
    ip_buyer_name = models.BooleanField(blank=True, null=True)
    ip_description = models.BooleanField(blank=True, null=True)
    ip_transaction_date = models.BooleanField(blank=True, null=True)
    ip_amount = models.BooleanField(blank=True, null=True)
    ip_mandate = models.BooleanField(blank=True, null=True)
    ip_status = models.BooleanField(blank=True, null=True)
    ip_link_id = models.BooleanField(blank=True, null=True)
    allow_instant_pay = models.BooleanField(blank=True, null=True)
    enable_merchant_package = models.BooleanField(blank=True, null=True)
    enable_merchant_package_display = models.BooleanField(blank=True, null=True)
    merchant_package_display_type = models.IntegerField(blank=True, null=True)
    property_one = models.BooleanField(blank=True, null=True)
    property_two = models.BooleanField(blank=True, null=True)
    merchant_package_display_type_layout = models.IntegerField(blank=True, null=True)
    ip_phone_number = models.BooleanField(blank=True, null=True)
    ip_property_one = models.BooleanField(blank=True, null=True)
    ip_property_two = models.BooleanField(blank=True, null=True)
    allow_details = models.BooleanField(blank=True, null=True)
    enable_view_all_collection = models.BooleanField(blank=True, null=True)
    collection_auto_retry = models.BooleanField(blank=True, null=True)
    collection_num_auto_retry = models.IntegerField(blank=True, null=True)
    auto_generate_cft_after_enrp = models.BooleanField(blank=True, null=True)
    hide_parameter = models.BooleanField(blank=True, null=True)
    masterdetails_total_validate = models.BooleanField(blank=True, null=True)
    fpx_seller_id = models.CharField(max_length=255, blank=True, null=True)
    enable_mandate_order = models.BooleanField(blank=True, null=True)
    instant_pay_form_dynamic = models.BooleanField()
    allow_details_ip = models.BooleanField(blank=True, null=True)
    masterdetails_amount_validate_ip = models.BooleanField(blank=True, null=True)
    enable_bank_with_logo = models.BooleanField(blank=True, null=True)
    enable_major_bank_order = models.BooleanField(blank=True, null=True)
    retry_next_option = models.IntegerField(blank=True, null=True)
    disable_collection_after_retry = models.BooleanField(blank=True, null=True)
    enable_mandate_order_schedule = models.BooleanField(blank=True, null=True)
    enable_enrp_callback = models.BooleanField(blank=True, null=True)
    enrp_callback_url = models.CharField(max_length=255, blank=True, null=True)
    merchant_website = models.CharField(max_length=255, blank=True, null=True)
    encryption_key = models.CharField(max_length=255, blank=True, null=True)
    default_rules_period_option = models.IntegerField(blank=True, null=True)
    default_rules_period = models.IntegerField(blank=True, null=True)
    ip_payment_method = models.BooleanField(blank=True, null=True)
    xero_data = models.TextField(blank=True, null=True)
    enable_xero = models.BooleanField(blank=True, null=True)
    max_collection_item = models.IntegerField()
    mandate_collection_date = models.BooleanField(blank=True, null=True)
    view_downpayment_amount = models.BooleanField(blank=True, null=True)
    view_downpayment_option = models.BooleanField(blank=True, null=True)
    merchant_status = models.CharField(max_length=50, blank=True, null=True)
    enable_paper_mandate = models.BooleanField(blank=True, null=True)
    enable_payonbehalf = models.BooleanField(blank=True, null=True)
    include_non_working_days = models.BooleanField(blank=True, null=True)
    use_ref_num_as_seller_order_no = models.BooleanField(blank=True, null=True)
    xero_payment_account = models.TextField(blank=True, null=True)
    enable_2c2p = models.BooleanField(blank=True, null=True)
    enable_fpx = models.BooleanField(blank=True, null=True)
    cc_email = models.TextField(blank=True, null=True)
    send_sms_notif = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "merchant"


# class MerchantAmountList(models.Model):
#     merchant = models.ForeignKey(Merchant, models.DO_NOTHING)
#     amount_list = models.DecimalField(
#         max_digits=65535, decimal_places=65535, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'merchant_amount_list'


# class MerchantAutoCollectionJob(models.Model):
#     merchant_id = models.IntegerField()
#     date_started = models.DateTimeField(blank=True, null=True)
#     date_ended = models.DateTimeField(blank=True, null=True)
#     type = models.IntegerField(blank=True, null=True)
#     result = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'merchant_auto_collection_job'


# class MerchantAutoCollectionOrderSettings(models.Model):
#     merchant_id = models.IntegerField(primary_key=True)
#     upload_enable = models.BooleanField(blank=True, null=True)
#     reminder_enable = models.BooleanField(blank=True, null=True)
#     reminder_option = models.IntegerField(blank=True, null=True)
#     reminder_day = models.IntegerField(blank=True, null=True)
#     daily_amount_option = models.IntegerField(blank=True, null=True)
#     daily_amount_value = models.DecimalField(
#         max_digits=16, decimal_places=2, blank=True, null=True)
#     weekly_schedule_day = models.IntegerField(blank=True, null=True)
#     weekly_enable_rules = models.BooleanField(blank=True, null=True)
#     weekly_effective_option = models.IntegerField(blank=True, null=True)
#     weekly_effective_day = models.IntegerField(blank=True, null=True)
#     weekly_amount_option = models.IntegerField(blank=True, null=True)
#     weekly_amount_value = models.DecimalField(
#         max_digits=16, decimal_places=2, blank=True, null=True)
#     monthly_schedule_date = models.IntegerField(blank=True, null=True)
#     monthly_enable_rules = models.BooleanField(blank=True, null=True)
#     monthly_effective_option = models.IntegerField(blank=True, null=True)
#     monthly_effective_day = models.IntegerField(blank=True, null=True)
#     monthly_effective_on_28 = models.BooleanField(blank=True, null=True)
#     monthly_amount_option = models.IntegerField(blank=True, null=True)
#     monthly_amount_value = models.DecimalField(
#         max_digits=16, decimal_places=2, blank=True, null=True)
#     yearly_schedule_date = models.CharField(
#         max_length=255, blank=True, null=True)
#     yearly_enable_rules = models.BooleanField(blank=True, null=True)
#     yearly_effective_option = models.IntegerField(blank=True, null=True)
#     yearly_effective_day = models.IntegerField(blank=True, null=True)
#     yearly_amount_option = models.IntegerField(blank=True, null=True)
#     yearly_amount_value = models.DecimalField(
#         max_digits=16, decimal_places=2, blank=True, null=True)
#     biweekly_schedule_date = models.IntegerField(blank=True, null=True)
#     biweekly_amount_option = models.IntegerField(blank=True, null=True)
#     biweekly_amount_value = models.DecimalField(
#         max_digits=16, decimal_places=2, blank=True, null=True)
#     biweekly_enable_rules = models.BooleanField(blank=True, null=True)
#     biweekly_effective_option = models.IntegerField(blank=True, null=True)
#     biweekly_effective_day = models.IntegerField(blank=True, null=True)
#     quarterly_schedule_date = models.IntegerField(blank=True, null=True)
#     quarterly_amount_option = models.IntegerField(blank=True, null=True)
#     quarterly_amount_value = models.DecimalField(
#         max_digits=16, decimal_places=2, blank=True, null=True)
#     quarterly_enable_rules = models.BooleanField(blank=True, null=True)
#     quarterly_effective_option = models.IntegerField(blank=True, null=True)
#     quarterly_effective_day = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'merchant_auto_collection_order_settings'


# class MerchantAutoCollectionSettings(models.Model):
#     merchant_id = models.IntegerField(primary_key=True)
#     daily_schedule_time = models.DecimalField(
#         max_digits=4, decimal_places=2, blank=True, null=True)
#     daily_amount_option = models.IntegerField(blank=True, null=True)
#     daily_amount_value = models.DecimalField(
#         max_digits=16, decimal_places=2, blank=True, null=True)
#     daily_reminder_enable = models.BooleanField(blank=True, null=True)
#     daily_reminder_option = models.IntegerField(blank=True, null=True)
#     daily_reminder_day = models.IntegerField(blank=True, null=True)
#     daily_upload = models.BooleanField(blank=True, null=True)
#     daily_enable_rules = models.BooleanField(blank=True, null=True)
#     daily_num_retry = models.IntegerField(blank=True, null=True)
#     daily_effective_option = models.IntegerField(blank=True, null=True)
#     daily_effective_day = models.IntegerField(blank=True, null=True)
#     weekly_schedule_day = models.IntegerField(blank=True, null=True)
#     weekly_schedule_time = models.DecimalField(
#         max_digits=4, decimal_places=2, blank=True, null=True)
#     weekly_amount_option = models.IntegerField(blank=True, null=True)
#     weekly_amount_value = models.DecimalField(
#         max_digits=16, decimal_places=2, blank=True, null=True)
#     weekly_reminder_enable = models.BooleanField(blank=True, null=True)
#     weekly_reminder_option = models.IntegerField(blank=True, null=True)
#     weekly_reminder_day = models.IntegerField(blank=True, null=True)
#     weekly_upload = models.BooleanField(blank=True, null=True)
#     weekly_enable_rules = models.BooleanField(blank=True, null=True)
#     weekly_num_retry = models.IntegerField(blank=True, null=True)
#     weekly_effective_option = models.IntegerField(blank=True, null=True)
#     weekly_effective_day = models.IntegerField(blank=True, null=True)
#     monthly_schedule_date = models.IntegerField(blank=True, null=True)
#     monthly_schedule_time = models.DecimalField(
#         max_digits=4, decimal_places=2, blank=True, null=True)
#     monthly_amount_option = models.IntegerField(blank=True, null=True)
#     monthly_amount_value = models.DecimalField(
#         max_digits=16, decimal_places=2, blank=True, null=True)
#     monthly_reminder_enable = models.BooleanField(blank=True, null=True)
#     monthly_reminder_option = models.IntegerField(blank=True, null=True)
#     monthly_reminder_day = models.IntegerField(blank=True, null=True)
#     monthly_upload = models.BooleanField(blank=True, null=True)
#     monthly_enable_rules = models.BooleanField(blank=True, null=True)
#     monthly_num_retry = models.IntegerField(blank=True, null=True)
#     monthly_effective_option = models.IntegerField(blank=True, null=True)
#     monthly_effective_day = models.IntegerField(blank=True, null=True)
#     yearly_schedule_date = models.CharField(
#         max_length=255, blank=True, null=True)
#     yearly_schedule_time = models.DecimalField(
#         max_digits=4, decimal_places=2, blank=True, null=True)
#     yearly_amount_option = models.IntegerField(blank=True, null=True)
#     yearly_amount_value = models.DecimalField(
#         max_digits=16, decimal_places=2, blank=True, null=True)
#     yearly_reminder_enable = models.BooleanField(blank=True, null=True)
#     yearly_reminder_option = models.IntegerField(blank=True, null=True)
#     yearly_reminder_day = models.IntegerField(blank=True, null=True)
#     yearly_upload = models.BooleanField(blank=True, null=True)
#     yearly_enable_rules = models.BooleanField(blank=True, null=True)
#     yearly_num_retry = models.IntegerField(blank=True, null=True)
#     yearly_effective_option = models.IntegerField(blank=True, null=True)
#     yearly_effective_day = models.IntegerField(blank=True, null=True)
#     daily_schedule_start = models.DateTimeField(blank=True, null=True)
#     daily_schedule_opt = models.IntegerField(blank=True, null=True)
#     daily_schedule_end = models.DateTimeField(blank=True, null=True)
#     weekly_schedule_start = models.DateTimeField(blank=True, null=True)
#     weekly_schedule_opt = models.IntegerField(blank=True, null=True)
#     weekly_schedule_end = models.DateTimeField(blank=True, null=True)
#     monthly_schedule_start = models.DateTimeField(blank=True, null=True)
#     monthly_schedule_opt = models.IntegerField(blank=True, null=True)
#     monthly_schedule_end = models.DateTimeField(blank=True, null=True)
#     yearly_schedule_start = models.DateTimeField(blank=True, null=True)
#     yearly_schedule_opt = models.IntegerField(blank=True, null=True)
#     yearly_schedule_end = models.DateTimeField(blank=True, null=True)
#     yearly_schedule_option = models.IntegerField(blank=True, null=True)
#     monthly_effective_on_28 = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'merchant_auto_collection_settings'


class MerchantBankAccount(models.Model):
    account_number = models.CharField(max_length=255, blank=True, null=True)
    seller_id = models.CharField(max_length=255, blank=True, null=True)
    bank = models.ForeignKey(Bank, models.DO_NOTHING, blank=True, null=True)
    collection_manual_update = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "merchant_bank_account"


# class MerchantCallbackQueue(models.Model):
#     uid = models.CharField(primary_key=True, max_length=32)
#     date_added_to_queue = models.DateTimeField(blank=True, null=True)
#     reference_id = models.CharField(max_length=50, blank=True, null=True)
#     transaction_type = models.IntegerField(blank=True, null=True)
#     transaction_date = models.DateTimeField(blank=True, null=True)
#     status = models.IntegerField(blank=True, null=True)
#     target_url = models.CharField(max_length=255, blank=True, null=True)
#     max_retry = models.IntegerField(blank=True, null=True)
#     count_retry = models.IntegerField(blank=True, null=True)
#     response_code = models.IntegerField(blank=True, null=True)
#     response_text = models.TextField(blank=True, null=True)
#     response_date = models.DateTimeField(blank=True, null=True)
#     merchant_id = models.IntegerField(blank=True, null=True)
#     error_message = models.TextField(blank=True, null=True)
#     reference_num = models.CharField(max_length=50, blank=True, null=True)
#     batch_id = models.CharField(max_length=255, blank=True, null=True)
#     payout_payee = models.CharField(max_length=255, blank=True, null=True)
#     payout_amount = models.DecimalField(
#         max_digits=19, decimal_places=2, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'merchant_callback_queue'


# class MerchantChecksum(models.Model):
#     merchant_id = models.IntegerField(primary_key=True)
#     apply_checksum = models.BooleanField(blank=True, null=True)
#     private_key = models.TextField(blank=True, null=True)
#     public_key = models.TextField(blank=True, null=True)
#     password_key = models.CharField(max_length=255, blank=True, null=True)
#     apply_rsa = models.BooleanField(blank=True, null=True)
#     key_encrypt = models.CharField(max_length=255, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'merchant_checksum'


# class MerchantCreditCard(models.Model):
#     uid = models.AutoField(primary_key=True)
#     merchant_id = models.IntegerField(blank=True, null=True)
#     cc_uname_ip = models.CharField(max_length=255, blank=True, null=True)
#     cc_upass_ip = models.CharField(max_length=255, blank=True, null=True)
#     cc_uname = models.CharField(max_length=255, blank=True, null=True)
#     cc_upass = models.CharField(max_length=255, blank=True, null=True)
#     cc_allow = models.BooleanField(blank=True, null=True)
#     cc_allow_ip = models.BooleanField(blank=True, null=True)
#     cc_merchant_name = models.CharField(max_length=255, blank=True, null=True)
#     cc_address_line1 = models.CharField(max_length=150, blank=True, null=True)
#     cc_address_line2 = models.CharField(max_length=150, blank=True, null=True)
#     cc_merchant_name_ip = models.CharField(
#         max_length=255, blank=True, null=True)
#     cc_enable = models.BooleanField(blank=True, null=True)
#     cc_payment_site = models.IntegerField(blank=True, null=True)
#     transaction_source = models.CharField(
#         max_length=255, blank=True, null=True)
#     cc_otp_visa = models.BooleanField(blank=True, null=True)
#     cc_otp_mastercard = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'merchant_credit_card'


# class MerchantEmailServer(models.Model):
#     merchant_id = models.IntegerField(primary_key=True)
#     email_host = models.CharField(max_length=255, blank=True, null=True)
#     email_port = models.IntegerField(blank=True, null=True)
#     email_username = models.CharField(max_length=255, blank=True, null=True)
#     email_password = models.CharField(max_length=255, blank=True, null=True)
#     email_relay = models.BooleanField(blank=True, null=True)
#     via_api = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'merchant_email_server'


# class MerchantEmailSettings(models.Model):
#     id = models.IntegerField(primary_key=True)
#     signup = models.BooleanField(blank=True, null=True)
#     new_customer = models.BooleanField(blank=True, null=True)
#     user_reg = models.BooleanField(blank=True, null=True)
#     mandate_auth_req = models.BooleanField(blank=True, null=True)
#     mandate_cancel = models.BooleanField(blank=True, null=True)
#     mandate_modified = models.BooleanField(blank=True, null=True)
#     mandate_mod_rules = models.BooleanField(blank=True, null=True)
#     mandate_pending_auth = models.BooleanField(blank=True, null=True)
#     mandate_rejected = models.BooleanField(blank=True, null=True)
#     mandate_succ_terminate = models.BooleanField(blank=True, null=True)
#     mandate_succ_auth = models.BooleanField(blank=True, null=True)
#     mandate_term_req = models.BooleanField(blank=True, null=True)
#     mandate_pending_b2b = models.BooleanField(blank=True, null=True)
#     ip_approved = models.BooleanField(blank=True, null=True)
#     ip_cancelled = models.BooleanField(blank=True, null=True)
#     ip_new = models.BooleanField(blank=True, null=True)
#     ip_pending_auth = models.BooleanField(blank=True, null=True)
#     ip_rejected = models.BooleanField(blank=True, null=True)
#     use_default_template = models.BooleanField(blank=True, null=True)
#     service_request_auth = models.BooleanField(blank=True, null=True)
#     service_ip_new = models.BooleanField(blank=True, null=True)
#     merchant_auth_req = models.BooleanField(blank=True, null=True)
#     merchant_cancel = models.BooleanField(blank=True, null=True)
#     merchant_modified = models.BooleanField(blank=True, null=True)
#     merchant_pending_auth = models.BooleanField(blank=True, null=True)
#     merchant_rejected = models.BooleanField(blank=True, null=True)
#     merchant_succ_terminate = models.BooleanField(blank=True, null=True)
#     merchant_succ_auth = models.BooleanField(blank=True, null=True)
#     merchant_terminate_req = models.BooleanField(blank=True, null=True)
#     merchant_pending_b2b = models.BooleanField(blank=True, null=True)
#     merchant_ip_approved = models.BooleanField(blank=True, null=True)
#     merchant_ip_cancelled = models.BooleanField(blank=True, null=True)
#     merchant_ip_new = models.BooleanField(blank=True, null=True)
#     merchant_ip_pending_auth = models.BooleanField(blank=True, null=True)
#     merchant_ip_rejected = models.BooleanField(blank=True, null=True)
#     collection_receipt = models.BooleanField(blank=True, null=True)
#     service_mandate_success = models.BooleanField(blank=True, null=True)
#     service_ip_success = models.BooleanField(blank=True, null=True)
#     collection_insufficient_fund = models.BooleanField(blank=True, null=True)
#     new_payout_batch = models.BooleanField(blank=True, null=True)
#     payout_batch_approved = models.BooleanField(blank=True, null=True)
#     payout_batch_rejected = models.BooleanField(blank=True, null=True)
#     payout_batch_transferred = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'merchant_email_settings'


# class MerchantForm(models.Model):
#     merchant = models.ForeignKey(Merchant, models.DO_NOTHING)
#     property_key = models.CharField(max_length=255)
#     property_name = models.CharField(max_length=255)
#     property_group = models.CharField(max_length=255, blank=True, null=True)
#     is_mandatory = models.BooleanField(blank=True, null=True)
#     is_hidden = models.BooleanField(blank=True, null=True)
#     is_readonly = models.BooleanField(blank=True, null=True)
#     property_order = models.IntegerField(blank=True, null=True)
#     default_value = models.CharField(max_length=255, blank=True, null=True)
#     max_length = models.IntegerField(blank=True, null=True)
#     min_value = models.IntegerField(blank=True, null=True)
#     max_value = models.IntegerField(blank=True, null=True)
#     min_decimal = models.DecimalField(
#         max_digits=31, decimal_places=2, blank=True, null=True)
#     max_decimal = models.DecimalField(
#         max_digits=31, decimal_places=2, blank=True, null=True)
#     property_type = models.IntegerField(blank=True, null=True)
#     form_type = models.IntegerField(blank=True, null=True)
#     uid = models.IntegerField(primary_key=True)
#     default_order = models.IntegerField(blank=True, null=True)
#     property_alias = models.CharField(max_length=255, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'merchant_form'


# class MerchantInstantPayAmountList(models.Model):
#     merchant = models.ForeignKey(Merchant, models.DO_NOTHING)
#     instant_pay_amount_list = models.DecimalField(
#         max_digits=65535, decimal_places=65535, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'merchant_instant_pay_amount_list'


class MerchantMerchantBankAccounts(models.Model):
    merchant = models.ForeignKey(Merchant, models.DO_NOTHING)
    merchant_bank_accounts = models.OneToOneField(
        MerchantBankAccount, models.DO_NOTHING
    )

    class Meta:
        managed = False
        db_table = "merchant_merchant_bank_accounts"


# class MerchantOnestopPayment(models.Model):
#     merchant_id = models.IntegerField(primary_key=True)
#     merchant_id_2c2p = models.CharField(max_length=100, blank=True, null=True)
#     secret_key_2c2p = models.CharField(max_length=255, blank=True, null=True)
#     country = models.CharField(max_length=100, blank=True, null=True)
#     currency_code = models.CharField(max_length=3, blank=True, null=True)
#     enable_2c2p = models.BooleanField(blank=True, null=True)
#     currency_code2 = models.CharField(max_length=3, blank=True, null=True)
#     merchant_prefix = models.CharField(max_length=5, blank=True, null=True)
#     request3ds = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'merchant_onestop_payment'


# class MerchantPackageInstallment(models.Model):
#     package = models.ForeignKey('MerchantPackageSettings', models.DO_NOTHING)
#     start_period = models.IntegerField(blank=True, null=True)
#     end_period = models.IntegerField(blank=True, null=True)
#     amount = models.DecimalField(
#         max_digits=16, decimal_places=2, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'merchant_package_installment'


# class MerchantPackageSettings(models.Model):
#     id = models.IntegerField(primary_key=True)
#     merchant_id = models.IntegerField(blank=True, null=True)
#     label = models.CharField(max_length=255, blank=True, null=True)
#     enable_amount = models.BooleanField(blank=True, null=True)
#     amount = models.DecimalField(
#         max_digits=19, decimal_places=2, blank=True, null=True)
#     enable_period = models.BooleanField(blank=True, null=True)
#     period = models.IntegerField(blank=True, null=True)
#     period_option = models.IntegerField(blank=True, null=True)
#     auto_expired = models.BooleanField(blank=True, null=True)
#     change_terms_condition = models.BooleanField(blank=True, null=True)
#     terms_condition_text = models.TextField(blank=True, null=True)
#     include = models.BooleanField(blank=True, null=True)
#     enable_max_amount = models.BooleanField(blank=True, null=True)
#     enable_frequency = models.BooleanField(blank=True, null=True)
#     frequency = models.IntegerField(blank=True, null=True)
#     enable_max_frequency = models.BooleanField(blank=True, null=True)
#     max_frequency = models.IntegerField(blank=True, null=True)
#     enable_purpose_of_payment = models.BooleanField(blank=True, null=True)
#     purpose_of_payment = models.CharField(
#         max_length=255, blank=True, null=True)
#     enable_expired_after = models.BooleanField(blank=True, null=True)
#     expired_days = models.IntegerField(blank=True, null=True)
#     position = models.IntegerField(blank=True, null=True)
#     taxable = models.BooleanField(blank=True, null=True)
#     tax_percentage = models.DecimalField(
#         max_digits=16, decimal_places=5, blank=True, null=True)
#     max_amount = models.DecimalField(
#         max_digits=16, decimal_places=2, blank=True, null=True)
#     enable_installment = models.BooleanField(blank=True, null=True)
#     installment_count = models.IntegerField(blank=True, null=True)
#     enable_start_collect_opt = models.BooleanField(blank=True, null=True)
#     start_collect_opt = models.IntegerField(blank=True, null=True)
#     enable_downpayment = models.BooleanField(blank=True, null=True)
#     downpayment_amount = models.DecimalField(
#         max_digits=16, decimal_places=2, blank=True, null=True)
#     downpayment_option = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'merchant_package_settings'


# class MerchantPayout(models.Model):
#     merchant_id = models.IntegerField(primary_key=True)
#     payout_enable = models.BooleanField(blank=True, null=True)
#     rhb_corporate_id = models.CharField(max_length=6, blank=True, null=True)
#     payment_callback_url = models.CharField(
#         max_length=255, blank=True, null=True)
#     rhb_subsidiary_id = models.CharField(max_length=10, blank=True, null=True)
#     debiting_method = models.CharField(max_length=1, blank=True, null=True)
#     telegram_chat_id = models.BigIntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'merchant_payout'


# class MerchantPayoutBankAccount(models.Model):
#     account_number = models.CharField(max_length=255, blank=True, null=True)
#     bank_swift_code = models.CharField(max_length=255, blank=True, null=True)
#     is_default = models.BooleanField(blank=True, null=True)
#     merchant = models.ForeignKey(Merchant, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'merchant_payout_bank_account'


# class MerchantPoweredbyTag(models.Model):
#     merchant_id = models.IntegerField(primary_key=True)
#     poweredby_tag = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'merchant_poweredby_tag'


# class MerchantPurposeOfPayments(models.Model):
#     merchant = models.ForeignKey(Merchant, models.DO_NOTHING)
#     purpose_of_payments = models.CharField(
#         max_length=255, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'merchant_purpose_of_payments'


# class MerchantSelectedFrequencies(models.Model):
#     merchant = models.ForeignKey(Merchant, models.DO_NOTHING)
#     selected_frequencies = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'merchant_selected_frequencies'


# class MerchantSelectedIdType(models.Model):
#     merchant = models.ForeignKey(Merchant, models.DO_NOTHING)
#     selected_id_type = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'merchant_selected_id_type'


# class MerchantTermsConditions(models.Model):
#     merchant = models.ForeignKey(Merchant, models.DO_NOTHING)
#     terms_conditions_text = models.TextField(blank=True, null=True)
#     mandatory = models.BooleanField(blank=True, null=True)
#     type = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'merchant_terms_conditions'


# class MerchantTwoFactorAuth(models.Model):
#     merchant = models.OneToOneField(
#         Merchant, models.DO_NOTHING, primary_key=True)
#     two_factor_auth_enable = models.BooleanField(blank=True, null=True)
#     two_factor_auth_is_setup = models.BooleanField(blank=True, null=True)
#     tfa_secret = models.CharField(max_length=255, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'merchant_two_factor_auth'


# class NodeEvent(models.Model):
#     event_timestamp = models.DateTimeField()
#     event_type = models.CharField(max_length=100)
#     node_uid = models.CharField(max_length=65)
#     node_record_number = models.CharField(max_length=50, blank=True, null=True)
#     node_title = models.CharField(max_length=255)
#     principal_uid = models.CharField(max_length=32)
#     principal_name = models.CharField(max_length=255)
#     details = models.TextField(blank=True, null=True)
#     ipaddress = models.CharField(max_length=45, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'node_event'


# class NodeLock(models.Model):
#     node_uid = models.CharField(primary_key=True, max_length=65)
#     locked_by = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='locked_by')

#     class Meta:
#         managed = False
#         db_table = 'node_lock'


# class NodeRefs(models.Model):
#     property_uid = models.OneToOneField(
#         'Property', models.DO_NOTHING, db_column='property_uid', primary_key=True)
#     from_node_uid = models.CharField(max_length=65)
#     to_node_uid = models.CharField(max_length=65)

#     class Meta:
#         managed = False
#         db_table = 'node_refs'
#         unique_together = (('property_uid', 'from_node_uid', 'to_node_uid'),)


# class NodeRel(models.Model):
#     from_node_uid = models.CharField(primary_key=True, max_length=65)
#     to_node_uid = models.CharField(max_length=65)
#     rel_uid = models.ForeignKey(
#         'NodeRelType', models.DO_NOTHING, db_column='rel_uid')

#     class Meta:
#         managed = False
#         db_table = 'node_rel'
#         unique_together = (('from_node_uid', 'to_node_uid', 'rel_uid'),)


# class NodeRelType(models.Model):
#     uid = models.CharField(primary_key=True, max_length=5)
#     rel_name = models.CharField(unique=True, max_length=50)

#     class Meta:
#         managed = False
#         db_table = 'node_rel_type'


# class Nodetype(models.Model):
#     uid = models.CharField(primary_key=True, max_length=32)
#     name = models.CharField(unique=True, max_length=50)
#     description = models.CharField(max_length=255, blank=True, null=True)
#     store_uid = models.ForeignKey(
#         'Store', models.DO_NOTHING, db_column='store_uid', blank=True, null=True)
#     acl_uid = models.ForeignKey(
#         Acl, models.DO_NOTHING, db_column='acl_uid', blank=True, null=True)
#     apply_node_acl_filter = models.SmallIntegerField()
#     apply_nodetype_default_acl_filter = models.SmallIntegerField()
#     apply_owner_filter = models.SmallIntegerField()
#     apply_classification_default_acl_filter = models.SmallIntegerField()
#     apply_container_based_filter = models.SmallIntegerField()
#     is_container = models.SmallIntegerField()
#     level = models.SmallIntegerField()
#     record_numbering_method = models.SmallIntegerField(blank=True, null=True)
#     enclosure_number_prefix = models.CharField(
#         max_length=3, blank=True, null=True)
#     enclosure_number_suffix = models.CharField(
#         max_length=3, blank=True, null=True)
#     current_record_year = models.IntegerField(blank=True, null=True)
#     reset_record_number_at_year_end = models.SmallIntegerField()
#     next_record_number = models.IntegerField(blank=True, null=True)
#     record_number_pattern = models.CharField(
#         max_length=50, blank=True, null=True)
#     init_record_number = models.IntegerField(blank=True, null=True)
#     number_pattern_increment = models.IntegerField()
#     enclosure_number_max_digits = models.IntegerField()
#     default_acl_uid = models.CharField(max_length=32, blank=True, null=True)
#     default_security_level_uid = models.CharField(
#         max_length=32, blank=True, null=True)
#     default_retention_schedule_uid = models.ForeignKey(
#         'RetentionSchedule', models.DO_NOTHING, db_column='default_retention_schedule_uid', blank=True, null=True)
#     is_metadata_text_indexed = models.SmallIntegerField()
#     is_content_text_indexed = models.SmallIntegerField()
#     titling_method = models.SmallIntegerField()
#     can_attach_content = models.SmallIntegerField()
#     content_mandatory = models.SmallIntegerField()
#     is_shreddable = models.SmallIntegerField()
#     autoexec_script = models.TextField(blank=True, null=True)
#     titlealias = models.CharField(max_length=255, blank=True, null=True)
#     icon = models.BinaryField(blank=True, null=True)
#     description_alias = models.CharField(max_length=255, blank=True, null=True)
#     notes_alias = models.CharField(max_length=255, blank=True, null=True)
#     record_number_alias = models.CharField(
#         max_length=255, blank=True, null=True)
#     barcode_alias = models.CharField(max_length=255, blank=True, null=True)
#     container_alias = models.CharField(max_length=255, blank=True, null=True)
#     external_barcode_alias = models.CharField(
#         max_length=255, blank=True, null=True)
#     enclosure_number_alias = models.CharField(
#         max_length=255, blank=True, null=True)
#     classification_alias = models.CharField(
#         max_length=255, blank=True, null=True)
#     secondary_classification_alias = models.CharField(
#         max_length=255, blank=True, null=True)
#     tertiary_classification_alias = models.CharField(
#         max_length=255, blank=True, null=True)
#     date_registered_alias = models.CharField(
#         max_length=255, blank=True, null=True)
#     creator_name_alias = models.CharField(
#         max_length=255, blank=True, null=True)
#     creator_username_alias = models.CharField(
#         max_length=255, blank=True, null=True)
#     master_alias = models.CharField(max_length=255, blank=True, null=True)
#     date_of_last_enclosure_alias = models.CharField(
#         max_length=255, blank=True, null=True)
#     date_enclosed_alias = models.CharField(
#         max_length=255, blank=True, null=True)
#     date_finalized_alias = models.CharField(
#         max_length=255, blank=True, null=True)
#     assignee_alias = models.CharField(max_length=255, blank=True, null=True)
#     home_alias = models.CharField(max_length=255, blank=True, null=True)
#     owner_alias = models.CharField(max_length=255, blank=True, null=True)
#     disposition_status_alias = models.CharField(
#         max_length=255, blank=True, null=True)
#     external_uid_alias = models.CharField(
#         max_length=255, blank=True, null=True)
#     integrity_check_alias = models.CharField(
#         max_length=255, blank=True, null=True)
#     finalized_alias = models.CharField(max_length=255, blank=True, null=True)
#     is_hybrid_alias = models.CharField(max_length=255, blank=True, null=True)
#     retention_schedule_alias = models.CharField(
#         max_length=255, blank=True, null=True)
#     security_level_alias = models.CharField(
#         max_length=255, blank=True, null=True)
#     date_last_modified_alias = models.CharField(
#         max_length=255, blank=True, null=True)
#     date_last_modified_of_contents_alias = models.CharField(
#         max_length=255, blank=True, null=True)
#     client_alias = models.CharField(max_length=255, blank=True, null=True)
#     combined_title_alias = models.CharField(
#         max_length=255, blank=True, null=True)
#     mime_type_alias = models.CharField(max_length=255, blank=True, null=True)
#     date_closed_alias = models.CharField(max_length=255, blank=True, null=True)
#     num_digits_enclosure_number = models.SmallIntegerField()
#     apply_autoexec_scripting = models.SmallIntegerField()
#     uncompressed_record_number_alias = models.CharField(
#         max_length=255, blank=True, null=True)
#     opened_temporarily_alias = models.CharField(
#         max_length=255, blank=True, null=True)
#     date_created_alias = models.CharField(
#         max_length=255, blank=True, null=True)
#     author_alias = models.CharField(max_length=255, blank=True, null=True)
#     batch_id_alias = models.CharField(max_length=255, blank=True, null=True)
#     date_archived_alias = models.CharField(
#         max_length=255, blank=True, null=True)
#     date_made_inactive_alias = models.CharField(
#         max_length=255, blank=True, null=True)
#     apply_content_template = models.SmallIntegerField()
#     content_template_node_uid = models.ForeignKey(
#         'RecordNode', models.DO_NOTHING, db_column='content_template_node_uid', blank=True, null=True)
#     copy_content_template_on_create = models.SmallIntegerField()
#     copy_content_template_on_update = models.SmallIntegerField()
#     content_template_on_update_behaviour = models.SmallIntegerField()
#     launch_activity_on_node_create = models.SmallIntegerField()
#     activity_name = models.CharField(max_length=50, blank=True, null=True)
#     apply_content_conversion = models.SmallIntegerField()
#     conversion_format = models.CharField(max_length=10, blank=True, null=True)
#     default_auto_finalize = models.SmallIntegerField()
#     record_class_alias = models.CharField(
#         max_length=255, blank=True, null=True)
#     default_record_class = models.IntegerField()
#     is_voluming_enabled = models.SmallIntegerField()
#     is_auto_close_volume = models.SmallIntegerField()
#     is_close_volume_after_exceed_max_content = models.SmallIntegerField()
#     is_close_volume_on_particular_date = models.SmallIntegerField()
#     is_close_volume_on_triggered_event = models.SmallIntegerField()
#     is_auto_open_volume_after_exceed_max_content = models.SmallIntegerField()
#     is_auto_open_volume_on_particular_date = models.SmallIntegerField()
#     is_auto_open_volume_on_triggered_event = models.SmallIntegerField()
#     volume_max_content = models.IntegerField(blank=True, null=True)
#     volume_closing_date = models.DateTimeField(blank=True, null=True)
#     volume_triggered_event = models.IntegerField(blank=True, null=True)
#     volume_triggered_event_type = models.IntegerField(blank=True, null=True)
#     volume_triggered_event_duration = models.IntegerField(
#         blank=True, null=True)
#     volume_separator = models.CharField(max_length=5, blank=True, null=True)
#     num_of_digits_for_volume_number = models.IntegerField()
#     volume_triggered_event_property_uid = models.CharField(
#         max_length=32, blank=True, null=True)
#     record_event_setting = models.IntegerField()
#     is_auto_update_security_level = models.SmallIntegerField()
#     is_auto_update_security_level_on_particular_date = models.SmallIntegerField()
#     security_level_trigger_date = models.DateTimeField(blank=True, null=True)
#     is_update_security_level_on_triggered_event = models.SmallIntegerField()
#     security_level_triggered_event = models.IntegerField(blank=True, null=True)
#     security_level_triggered_event_type = models.IntegerField(
#         blank=True, null=True)
#     security_level_triggered_event_duration = models.IntegerField(
#         blank=True, null=True)
#     security_level_triggered_event_property = models.CharField(
#         max_length=32, blank=True, null=True)
#     auto_update_security_level_id = models.CharField(
#         max_length=32, blank=True, null=True)
#     hybrid_remarks_alias = models.CharField(
#         max_length=255, blank=True, null=True)
#     is_declassify_alias = models.TextField(blank=True, null=True)
#     enforce_single_creation_in_a_workflow = models.SmallIntegerField()
#     check_in_as_new_version = models.SmallIntegerField()
#     check_in_as_override_previous_content = models.SmallIntegerField()
#     is_imported = models.SmallIntegerField()
#     can_show_tab = models.SmallIntegerField()
#     can_show_alt_container = models.SmallIntegerField()
#     can_show_rel_record = models.SmallIntegerField()
#     can_show_retention = models.SmallIntegerField()
#     can_transfer_metadata = models.SmallIntegerField()

#     class Meta:
#         managed = False
#         db_table = 'nodetype'


# class NodetypeAttribute(models.Model):
#     nodetype_uid = models.OneToOneField(
#         Nodetype, models.DO_NOTHING, db_column='nodetype_uid', primary_key=True)
#     attribute_no = models.SmallIntegerField()
#     group_name = models.CharField(max_length=50, blank=True, null=True)
#     # Field renamed because it started with '_'.
#     field_order = models.IntegerField(
#         db_column='_order', blank=True, null=True)
#     is_readonly = models.SmallIntegerField()

#     class Meta:
#         managed = False
#         db_table = 'nodetype_attribute'
#         unique_together = (('nodetype_uid', 'attribute_no'),
#                            ('nodetype_uid', 'attribute_no', 'group_name'),)


# class NodetypeB7Bc8B7449614D159Ce0869306F04D36(models.Model):
#     uid = models.CharField(primary_key=True, max_length=65)
#     acl_uid = models.ForeignKey(
#         Acl, models.DO_NOTHING, db_column='acl_uid', blank=True, null=True)
#     owner_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='owner_uid', blank=True, null=True)
#     classification_uid = models.ForeignKey(
#         Classification, models.DO_NOTHING, db_column='classification_uid', blank=True, null=True)
#     secondary_classification_uid = models.CharField(
#         max_length=32, blank=True, null=True)
#     tertiary_classification_uid = models.CharField(
#         max_length=32, blank=True, null=True)
#     record_number = models.CharField(max_length=100, blank=True, null=True)
#     retention_schedule_uid = models.ForeignKey(
#         'RetentionSchedule', models.DO_NOTHING, db_column='retention_schedule_uid', blank=True, null=True)
#     hold_uid = models.ForeignKey(
#         Hold, models.DO_NOTHING, db_column='hold_uid', blank=True, null=True)
#     disposition_status = models.IntegerField(blank=True, null=True)
#     title = models.CharField(max_length=255, blank=True, null=True)
#     combined_title = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     date_registered = models.DateTimeField(blank=True, null=True)
#     creator_name = models.CharField(max_length=255, blank=True, null=True)
#     creator_username = models.CharField(max_length=255, blank=True, null=True)
#     notes = models.TextField(blank=True, null=True)
#     home_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='home_uid', blank=True, null=True)
#     assignee_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='assignee_uid', blank=True, null=True)
#     is_finalized = models.SmallIntegerField(blank=True, null=True)
#     is_hybrid = models.SmallIntegerField(blank=True, null=True)
#     date_finalized = models.DateTimeField(blank=True, null=True)
#     barcode = models.CharField(max_length=50, blank=True, null=True)
#     external_barcode = models.CharField(max_length=50, blank=True, null=True)
#     external_uid = models.CharField(max_length=50, blank=True, null=True)
#     integrity_check = models.TextField(blank=True, null=True)
#     security_level_uid = models.ForeignKey(
#         'SecurityLevel', models.DO_NOTHING, db_column='security_level_uid', blank=True, null=True)
#     date_last_modified = models.DateTimeField(blank=True, null=True)
#     date_last_modified_of_contents = models.DateTimeField(
#         blank=True, null=True)
#     client_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='client_uid', blank=True, null=True)
#     date_closed = models.DateTimeField(blank=True, null=True)
#     next_enclosure_number = models.IntegerField()
#     enclosure_number_increment = models.IntegerField()
#     uncompressed_record_number = models.CharField(
#         max_length=100, blank=True, null=True)
#     security_based_on_container = models.SmallIntegerField(
#         blank=True, null=True)
#     bypass_referenced_acls = models.SmallIntegerField(blank=True, null=True)
#     opened_temporarily = models.SmallIntegerField(blank=True, null=True)
#     date_created = models.DateTimeField(blank=True, null=True)
#     author = models.CharField(max_length=255, blank=True, null=True)
#     batch_id = models.CharField(max_length=40, blank=True, null=True)
#     date_archived = models.DateTimeField(blank=True, null=True)
#     date_made_inactive = models.DateTimeField(blank=True, null=True)
#     date_of_last_enclosure = models.DateTimeField(blank=True, null=True)
#     date_enclosed = models.DateTimeField(blank=True, null=True)
#     record_class = models.IntegerField()
#     container_record_number = models.CharField(
#         max_length=50, blank=True, null=True)
#     classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     secondary_classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     tertiary_classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     assignee_name = models.CharField(max_length=255, blank=True, null=True)
#     home_name = models.CharField(max_length=255, blank=True, null=True)
#     owner_name = models.CharField(max_length=255, blank=True, null=True)
#     retention_schedule_number = models.CharField(
#         max_length=100, blank=True, null=True)
#     security_level_number = models.SmallIntegerField(blank=True, null=True)
#     client_name = models.CharField(max_length=255, blank=True, null=True)
#     is_container_removed_on_ret_trig = models.SmallIntegerField(
#         blank=True, null=True)
#     is_set_home_on_container_ret_trig = models.SmallIntegerField(
#         blank=True, null=True)
#     retention_schedule_new_home = models.CharField(
#         max_length=32, blank=True, null=True)
#     is_misfiled = models.SmallIntegerField(blank=True, null=True)
#     master_uid = models.CharField(max_length=65, blank=True, null=True)
#     hybrid_remarks = models.TextField(blank=True, null=True)
#     date_last_modified_of_security_level = models.DateTimeField(
#         blank=True, null=True)
#     is_declassify = models.SmallIntegerField(blank=True, null=True)
#     is_imported = models.SmallIntegerField(blank=True, null=True)
#     enforce_single_creation_in_a_workflow = models.SmallIntegerField()
#     check_in_as_new_version = models.SmallIntegerField()
#     check_in_as_override_previous_content = models.SmallIntegerField()
#     is_declassify_alias = models.TextField(blank=True, null=True)
#     is_auto_update_security_level = models.SmallIntegerField()
#     is_auto_update_security_level_on_particular_date = models.SmallIntegerField()
#     security_level_trigger_date = models.DateTimeField(blank=True, null=True)
#     is_update_security_level_on_triggered_event = models.SmallIntegerField()
#     security_level_triggered_event = models.IntegerField(blank=True, null=True)
#     security_level_triggered_event_type = models.IntegerField(
#         blank=True, null=True)
#     security_level_triggered_event_duration = models.IntegerField(
#         blank=True, null=True)
#     security_level_triggered_event_property = models.CharField(
#         max_length=32, blank=True, null=True)
#     auto_update_security_level_id = models.CharField(
#         max_length=32, blank=True, null=True)
#     afd1329c2de2421bbbe5a48f65b56818 = models.CharField(
#         max_length=255, blank=True, null=True)
#     b5fb184441d941d6936f00708785f3f3 = models.CharField(
#         max_length=10, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'nodetype_b7bc8b7449614d159ce0869306f04d36'


# class NodetypeBa1E2021Ffdc497Ba7F8347Aff83E150(models.Model):
#     uid = models.CharField(primary_key=True, max_length=65)
#     acl_uid = models.ForeignKey(
#         Acl, models.DO_NOTHING, db_column='acl_uid', blank=True, null=True)
#     owner_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='owner_uid', blank=True, null=True)
#     classification_uid = models.ForeignKey(
#         Classification, models.DO_NOTHING, db_column='classification_uid', blank=True, null=True)
#     secondary_classification_uid = models.CharField(
#         max_length=32, blank=True, null=True)
#     tertiary_classification_uid = models.CharField(
#         max_length=32, blank=True, null=True)
#     record_number = models.CharField(max_length=100, blank=True, null=True)
#     retention_schedule_uid = models.ForeignKey(
#         'RetentionSchedule', models.DO_NOTHING, db_column='retention_schedule_uid', blank=True, null=True)
#     hold_uid = models.ForeignKey(
#         Hold, models.DO_NOTHING, db_column='hold_uid', blank=True, null=True)
#     disposition_status = models.IntegerField(blank=True, null=True)
#     title = models.CharField(max_length=255, blank=True, null=True)
#     combined_title = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     date_registered = models.DateTimeField(blank=True, null=True)
#     creator_name = models.CharField(max_length=255, blank=True, null=True)
#     creator_username = models.CharField(max_length=255, blank=True, null=True)
#     notes = models.TextField(blank=True, null=True)
#     home_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='home_uid', blank=True, null=True)
#     assignee_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='assignee_uid', blank=True, null=True)
#     is_finalized = models.SmallIntegerField(blank=True, null=True)
#     is_hybrid = models.SmallIntegerField(blank=True, null=True)
#     date_finalized = models.DateTimeField(blank=True, null=True)
#     barcode = models.CharField(max_length=50, blank=True, null=True)
#     external_barcode = models.CharField(max_length=50, blank=True, null=True)
#     external_uid = models.CharField(max_length=50, blank=True, null=True)
#     integrity_check = models.TextField(blank=True, null=True)
#     security_level_uid = models.ForeignKey(
#         'SecurityLevel', models.DO_NOTHING, db_column='security_level_uid', blank=True, null=True)
#     date_last_modified = models.DateTimeField(blank=True, null=True)
#     date_last_modified_of_contents = models.DateTimeField(
#         blank=True, null=True)
#     client_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='client_uid', blank=True, null=True)
#     date_closed = models.DateTimeField(blank=True, null=True)
#     next_enclosure_number = models.IntegerField()
#     enclosure_number_increment = models.IntegerField()
#     uncompressed_record_number = models.CharField(
#         max_length=100, blank=True, null=True)
#     security_based_on_container = models.SmallIntegerField(
#         blank=True, null=True)
#     bypass_referenced_acls = models.SmallIntegerField(blank=True, null=True)
#     opened_temporarily = models.SmallIntegerField(blank=True, null=True)
#     date_created = models.DateTimeField(blank=True, null=True)
#     author = models.CharField(max_length=255, blank=True, null=True)
#     batch_id = models.CharField(max_length=40, blank=True, null=True)
#     date_archived = models.DateTimeField(blank=True, null=True)
#     date_made_inactive = models.DateTimeField(blank=True, null=True)
#     date_of_last_enclosure = models.DateTimeField(blank=True, null=True)
#     date_enclosed = models.DateTimeField(blank=True, null=True)
#     record_class = models.IntegerField()
#     container_record_number = models.CharField(
#         max_length=50, blank=True, null=True)
#     classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     secondary_classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     tertiary_classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     assignee_name = models.CharField(max_length=255, blank=True, null=True)
#     home_name = models.CharField(max_length=255, blank=True, null=True)
#     owner_name = models.CharField(max_length=255, blank=True, null=True)
#     retention_schedule_number = models.CharField(
#         max_length=100, blank=True, null=True)
#     security_level_number = models.SmallIntegerField(blank=True, null=True)
#     client_name = models.CharField(max_length=255, blank=True, null=True)
#     is_container_removed_on_ret_trig = models.SmallIntegerField(
#         blank=True, null=True)
#     is_set_home_on_container_ret_trig = models.SmallIntegerField(
#         blank=True, null=True)
#     retention_schedule_new_home = models.CharField(
#         max_length=32, blank=True, null=True)
#     is_misfiled = models.SmallIntegerField(blank=True, null=True)
#     master_uid = models.CharField(max_length=65, blank=True, null=True)
#     hybrid_remarks = models.TextField(blank=True, null=True)
#     date_last_modified_of_security_level = models.DateTimeField(
#         blank=True, null=True)
#     is_declassify = models.SmallIntegerField(blank=True, null=True)
#     is_imported = models.SmallIntegerField(blank=True, null=True)
#     enforce_single_creation_in_a_workflow = models.SmallIntegerField()
#     check_in_as_new_version = models.SmallIntegerField()
#     check_in_as_override_previous_content = models.SmallIntegerField()
#     is_declassify_alias = models.TextField(blank=True, null=True)
#     is_auto_update_security_level = models.SmallIntegerField()
#     is_auto_update_security_level_on_particular_date = models.SmallIntegerField()
#     security_level_trigger_date = models.DateTimeField(blank=True, null=True)
#     is_update_security_level_on_triggered_event = models.SmallIntegerField()
#     security_level_triggered_event = models.IntegerField(blank=True, null=True)
#     security_level_triggered_event_type = models.IntegerField(
#         blank=True, null=True)
#     security_level_triggered_event_duration = models.IntegerField(
#         blank=True, null=True)
#     security_level_triggered_event_property = models.CharField(
#         max_length=32, blank=True, null=True)
#     auto_update_security_level_id = models.CharField(
#         max_length=32, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'nodetype_ba1e2021ffdc497ba7f8347aff83e150'


# class NodetypeC22816Ad803C47Ed83400Bc787D06Ed4(models.Model):
#     uid = models.CharField(primary_key=True, max_length=65)
#     acl_uid = models.ForeignKey(
#         Acl, models.DO_NOTHING, db_column='acl_uid', blank=True, null=True)
#     owner_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='owner_uid', blank=True, null=True)
#     classification_uid = models.ForeignKey(
#         Classification, models.DO_NOTHING, db_column='classification_uid', blank=True, null=True)
#     secondary_classification_uid = models.CharField(
#         max_length=32, blank=True, null=True)
#     tertiary_classification_uid = models.CharField(
#         max_length=32, blank=True, null=True)
#     record_number = models.CharField(max_length=100, blank=True, null=True)
#     retention_schedule_uid = models.ForeignKey(
#         'RetentionSchedule', models.DO_NOTHING, db_column='retention_schedule_uid', blank=True, null=True)
#     hold_uid = models.ForeignKey(
#         Hold, models.DO_NOTHING, db_column='hold_uid', blank=True, null=True)
#     disposition_status = models.IntegerField(blank=True, null=True)
#     title = models.CharField(max_length=255, blank=True, null=True)
#     combined_title = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     date_registered = models.DateTimeField(blank=True, null=True)
#     creator_name = models.CharField(max_length=255, blank=True, null=True)
#     creator_username = models.CharField(max_length=255, blank=True, null=True)
#     notes = models.TextField(blank=True, null=True)
#     home_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='home_uid', blank=True, null=True)
#     assignee_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='assignee_uid', blank=True, null=True)
#     is_finalized = models.SmallIntegerField(blank=True, null=True)
#     is_hybrid = models.SmallIntegerField(blank=True, null=True)
#     date_finalized = models.DateTimeField(blank=True, null=True)
#     barcode = models.CharField(max_length=50, blank=True, null=True)
#     external_barcode = models.CharField(max_length=50, blank=True, null=True)
#     external_uid = models.CharField(max_length=50, blank=True, null=True)
#     integrity_check = models.TextField(blank=True, null=True)
#     security_level_uid = models.ForeignKey(
#         'SecurityLevel', models.DO_NOTHING, db_column='security_level_uid', blank=True, null=True)
#     date_last_modified = models.DateTimeField(blank=True, null=True)
#     date_last_modified_of_contents = models.DateTimeField(
#         blank=True, null=True)
#     client_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='client_uid', blank=True, null=True)
#     date_closed = models.DateTimeField(blank=True, null=True)
#     next_enclosure_number = models.IntegerField()
#     enclosure_number_increment = models.IntegerField()
#     uncompressed_record_number = models.CharField(
#         max_length=100, blank=True, null=True)
#     security_based_on_container = models.SmallIntegerField(
#         blank=True, null=True)
#     bypass_referenced_acls = models.SmallIntegerField(blank=True, null=True)
#     opened_temporarily = models.SmallIntegerField(blank=True, null=True)
#     date_created = models.DateTimeField(blank=True, null=True)
#     author = models.CharField(max_length=255, blank=True, null=True)
#     batch_id = models.CharField(max_length=40, blank=True, null=True)
#     date_archived = models.DateTimeField(blank=True, null=True)
#     date_made_inactive = models.DateTimeField(blank=True, null=True)
#     date_of_last_enclosure = models.DateTimeField(blank=True, null=True)
#     date_enclosed = models.DateTimeField(blank=True, null=True)
#     record_class = models.IntegerField()
#     container_record_number = models.CharField(
#         max_length=50, blank=True, null=True)
#     classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     secondary_classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     tertiary_classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     assignee_name = models.CharField(max_length=255, blank=True, null=True)
#     home_name = models.CharField(max_length=255, blank=True, null=True)
#     owner_name = models.CharField(max_length=255, blank=True, null=True)
#     retention_schedule_number = models.CharField(
#         max_length=100, blank=True, null=True)
#     security_level_number = models.SmallIntegerField(blank=True, null=True)
#     client_name = models.CharField(max_length=255, blank=True, null=True)
#     is_container_removed_on_ret_trig = models.SmallIntegerField(
#         blank=True, null=True)
#     is_set_home_on_container_ret_trig = models.SmallIntegerField(
#         blank=True, null=True)
#     retention_schedule_new_home = models.CharField(
#         max_length=32, blank=True, null=True)
#     is_misfiled = models.SmallIntegerField(blank=True, null=True)
#     master_uid = models.CharField(max_length=65, blank=True, null=True)
#     hybrid_remarks = models.TextField(blank=True, null=True)
#     date_last_modified_of_security_level = models.DateTimeField(
#         blank=True, null=True)
#     is_declassify = models.SmallIntegerField(blank=True, null=True)
#     is_imported = models.SmallIntegerField(blank=True, null=True)
#     enforce_single_creation_in_a_workflow = models.SmallIntegerField()
#     check_in_as_new_version = models.SmallIntegerField()
#     check_in_as_override_previous_content = models.SmallIntegerField()
#     is_declassify_alias = models.TextField(blank=True, null=True)
#     is_auto_update_security_level = models.SmallIntegerField()
#     is_auto_update_security_level_on_particular_date = models.SmallIntegerField()
#     security_level_trigger_date = models.DateTimeField(blank=True, null=True)
#     is_update_security_level_on_triggered_event = models.SmallIntegerField()
#     security_level_triggered_event = models.IntegerField(blank=True, null=True)
#     security_level_triggered_event_type = models.IntegerField(
#         blank=True, null=True)
#     security_level_triggered_event_duration = models.IntegerField(
#         blank=True, null=True)
#     security_level_triggered_event_property = models.CharField(
#         max_length=32, blank=True, null=True)
#     auto_update_security_level_id = models.CharField(
#         max_length=32, blank=True, null=True)
#     ha41c373c2f0413cb1458bb886048bb2 = models.CharField(
#         max_length=255, blank=True, null=True)
#     f0970f3862f941338e162f34b75e6831 = models.CharField(
#         max_length=20, blank=True, null=True)
#     f362b3fe8c934881b0a3ee7e829df929 = models.TextField(blank=True, null=True)
#     f3e001ad12ef439b9b7c3d67a6239f10 = models.TextField(blank=True, null=True)
#     d2800efb0ed84f738f8dff1b9be7860e = models.CharField(
#         max_length=15, blank=True, null=True)
#     f8fef67bb03c47faa48061fcd1c2f038 = models.CharField(
#         max_length=15, blank=True, null=True)
#     a219cee40a3f4ae9be8f695763b78d33 = models.CharField(
#         max_length=255, blank=True, null=True)
#     d6376ccdb85c43af8260fb05786d731a = models.CharField(
#         max_length=255, blank=True, null=True)
#     bf65f9219f944e47b00873d7bec3343c = models.CharField(
#         max_length=15, blank=True, null=True)
#     gf1f763b063149df8529223e8b37a24b = models.CharField(
#         max_length=15, blank=True, null=True)
#     ec690c2952ef478ebcc6f25afbc367f2 = models.CharField(
#         max_length=255, blank=True, null=True)
#     d5858a70d49d4cf2b0d009ffac1c2f01 = models.CharField(
#         max_length=32, blank=True, null=True)
#     j1a034132d74409fa321444e8b7ff4b2 = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='j1a034132d74409fa321444e8b7ff4b2', blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'nodetype_c22816ad803c47ed83400bc787d06ed4'


# class NodetypeC408Fbc0Ea084Ec19B7Ee3F4D94E7711(models.Model):
#     uid = models.CharField(primary_key=True, max_length=65)
#     acl_uid = models.ForeignKey(
#         Acl, models.DO_NOTHING, db_column='acl_uid', blank=True, null=True)
#     owner_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='owner_uid', blank=True, null=True)
#     classification_uid = models.ForeignKey(
#         Classification, models.DO_NOTHING, db_column='classification_uid', blank=True, null=True)
#     secondary_classification_uid = models.CharField(
#         max_length=32, blank=True, null=True)
#     tertiary_classification_uid = models.CharField(
#         max_length=32, blank=True, null=True)
#     record_number = models.CharField(max_length=100, blank=True, null=True)
#     retention_schedule_uid = models.ForeignKey(
#         'RetentionSchedule', models.DO_NOTHING, db_column='retention_schedule_uid', blank=True, null=True)
#     hold_uid = models.ForeignKey(
#         Hold, models.DO_NOTHING, db_column='hold_uid', blank=True, null=True)
#     disposition_status = models.IntegerField(blank=True, null=True)
#     title = models.CharField(max_length=255, blank=True, null=True)
#     combined_title = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     date_registered = models.DateTimeField(blank=True, null=True)
#     creator_name = models.CharField(max_length=255, blank=True, null=True)
#     creator_username = models.CharField(max_length=255, blank=True, null=True)
#     notes = models.TextField(blank=True, null=True)
#     home_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='home_uid', blank=True, null=True)
#     assignee_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='assignee_uid', blank=True, null=True)
#     is_finalized = models.SmallIntegerField(blank=True, null=True)
#     is_hybrid = models.SmallIntegerField(blank=True, null=True)
#     date_finalized = models.DateTimeField(blank=True, null=True)
#     barcode = models.CharField(max_length=50, blank=True, null=True)
#     external_barcode = models.CharField(max_length=50, blank=True, null=True)
#     external_uid = models.CharField(max_length=50, blank=True, null=True)
#     integrity_check = models.TextField(blank=True, null=True)
#     security_level_uid = models.ForeignKey(
#         'SecurityLevel', models.DO_NOTHING, db_column='security_level_uid', blank=True, null=True)
#     date_last_modified = models.DateTimeField(blank=True, null=True)
#     date_last_modified_of_contents = models.DateTimeField(
#         blank=True, null=True)
#     client_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='client_uid', blank=True, null=True)
#     date_closed = models.DateTimeField(blank=True, null=True)
#     next_enclosure_number = models.IntegerField()
#     enclosure_number_increment = models.IntegerField()
#     uncompressed_record_number = models.CharField(
#         max_length=100, blank=True, null=True)
#     security_based_on_container = models.SmallIntegerField(
#         blank=True, null=True)
#     bypass_referenced_acls = models.SmallIntegerField(blank=True, null=True)
#     opened_temporarily = models.SmallIntegerField(blank=True, null=True)
#     date_created = models.DateTimeField(blank=True, null=True)
#     author = models.CharField(max_length=255, blank=True, null=True)
#     batch_id = models.CharField(max_length=40, blank=True, null=True)
#     date_archived = models.DateTimeField(blank=True, null=True)
#     date_made_inactive = models.DateTimeField(blank=True, null=True)
#     date_of_last_enclosure = models.DateTimeField(blank=True, null=True)
#     date_enclosed = models.DateTimeField(blank=True, null=True)
#     record_class = models.IntegerField()
#     container_record_number = models.CharField(
#         max_length=50, blank=True, null=True)
#     classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     secondary_classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     tertiary_classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     assignee_name = models.CharField(max_length=255, blank=True, null=True)
#     home_name = models.CharField(max_length=255, blank=True, null=True)
#     owner_name = models.CharField(max_length=255, blank=True, null=True)
#     retention_schedule_number = models.CharField(
#         max_length=100, blank=True, null=True)
#     security_level_number = models.SmallIntegerField(blank=True, null=True)
#     client_name = models.CharField(max_length=255, blank=True, null=True)
#     is_container_removed_on_ret_trig = models.SmallIntegerField(
#         blank=True, null=True)
#     is_set_home_on_container_ret_trig = models.SmallIntegerField(
#         blank=True, null=True)
#     retention_schedule_new_home = models.CharField(
#         max_length=32, blank=True, null=True)
#     is_misfiled = models.SmallIntegerField(blank=True, null=True)
#     master_uid = models.CharField(max_length=65, blank=True, null=True)
#     hybrid_remarks = models.TextField(blank=True, null=True)
#     date_last_modified_of_security_level = models.DateTimeField(
#         blank=True, null=True)
#     is_declassify = models.SmallIntegerField(blank=True, null=True)
#     is_imported = models.SmallIntegerField(blank=True, null=True)
#     enforce_single_creation_in_a_workflow = models.SmallIntegerField()
#     check_in_as_new_version = models.SmallIntegerField()
#     check_in_as_override_previous_content = models.SmallIntegerField()
#     is_declassify_alias = models.TextField(blank=True, null=True)
#     is_auto_update_security_level = models.SmallIntegerField()
#     is_auto_update_security_level_on_particular_date = models.SmallIntegerField()
#     security_level_trigger_date = models.DateTimeField(blank=True, null=True)
#     is_update_security_level_on_triggered_event = models.SmallIntegerField()
#     security_level_triggered_event = models.IntegerField(blank=True, null=True)
#     security_level_triggered_event_type = models.IntegerField(
#         blank=True, null=True)
#     security_level_triggered_event_duration = models.IntegerField(
#         blank=True, null=True)
#     security_level_triggered_event_property = models.CharField(
#         max_length=32, blank=True, null=True)
#     auto_update_security_level_id = models.CharField(
#         max_length=32, blank=True, null=True)
#     c1fb9f1f82af496cbbfd8f387aefab42 = models.CharField(
#         max_length=20, blank=True, null=True)
#     fdc659695c944890b9c1720de461db2e = models.ForeignKey(
#         'RecordNode', models.DO_NOTHING, db_column='fdc659695c944890b9c1720de461db2e', blank=True, null=True)
#     cead45cc70f2415ca1054f2853a8a100 = models.CharField(
#         max_length=20, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'nodetype_c408fbc0ea084ec19b7ee3f4d94e7711'


# class NodetypeCf35C509E3E846F2A5C7A2Fdba57Cb34(models.Model):
#     uid = models.CharField(primary_key=True, max_length=65)
#     acl_uid = models.ForeignKey(
#         Acl, models.DO_NOTHING, db_column='acl_uid', blank=True, null=True)
#     owner_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='owner_uid', blank=True, null=True)
#     classification_uid = models.ForeignKey(
#         Classification, models.DO_NOTHING, db_column='classification_uid', blank=True, null=True)
#     secondary_classification_uid = models.CharField(
#         max_length=32, blank=True, null=True)
#     tertiary_classification_uid = models.CharField(
#         max_length=32, blank=True, null=True)
#     record_number = models.CharField(max_length=100, blank=True, null=True)
#     retention_schedule_uid = models.ForeignKey(
#         'RetentionSchedule', models.DO_NOTHING, db_column='retention_schedule_uid', blank=True, null=True)
#     hold_uid = models.ForeignKey(
#         Hold, models.DO_NOTHING, db_column='hold_uid', blank=True, null=True)
#     disposition_status = models.IntegerField(blank=True, null=True)
#     title = models.CharField(max_length=255, blank=True, null=True)
#     combined_title = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     date_registered = models.DateTimeField(blank=True, null=True)
#     creator_name = models.CharField(max_length=255, blank=True, null=True)
#     creator_username = models.CharField(max_length=255, blank=True, null=True)
#     notes = models.TextField(blank=True, null=True)
#     home_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='home_uid', blank=True, null=True)
#     assignee_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='assignee_uid', blank=True, null=True)
#     is_finalized = models.SmallIntegerField(blank=True, null=True)
#     is_hybrid = models.SmallIntegerField(blank=True, null=True)
#     date_finalized = models.DateTimeField(blank=True, null=True)
#     barcode = models.CharField(max_length=50, blank=True, null=True)
#     external_barcode = models.CharField(max_length=50, blank=True, null=True)
#     external_uid = models.CharField(max_length=50, blank=True, null=True)
#     integrity_check = models.TextField(blank=True, null=True)
#     security_level_uid = models.ForeignKey(
#         'SecurityLevel', models.DO_NOTHING, db_column='security_level_uid', blank=True, null=True)
#     date_last_modified = models.DateTimeField(blank=True, null=True)
#     date_last_modified_of_contents = models.DateTimeField(
#         blank=True, null=True)
#     client_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='client_uid', blank=True, null=True)
#     date_closed = models.DateTimeField(blank=True, null=True)
#     next_enclosure_number = models.IntegerField()
#     enclosure_number_increment = models.IntegerField()
#     uncompressed_record_number = models.CharField(
#         max_length=100, blank=True, null=True)
#     security_based_on_container = models.SmallIntegerField(
#         blank=True, null=True)
#     bypass_referenced_acls = models.SmallIntegerField(blank=True, null=True)
#     opened_temporarily = models.SmallIntegerField(blank=True, null=True)
#     date_created = models.DateTimeField(blank=True, null=True)
#     author = models.CharField(max_length=255, blank=True, null=True)
#     batch_id = models.CharField(max_length=255, blank=True, null=True)
#     date_archived = models.DateTimeField(blank=True, null=True)
#     date_made_inactive = models.DateTimeField(blank=True, null=True)
#     date_of_last_enclosure = models.DateTimeField(blank=True, null=True)
#     date_enclosed = models.DateTimeField(blank=True, null=True)
#     record_class = models.IntegerField()
#     container_record_number = models.CharField(
#         max_length=50, blank=True, null=True)
#     classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     secondary_classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     tertiary_classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     assignee_name = models.CharField(max_length=255, blank=True, null=True)
#     home_name = models.CharField(max_length=255, blank=True, null=True)
#     owner_name = models.CharField(max_length=255, blank=True, null=True)
#     retention_schedule_number = models.CharField(
#         max_length=100, blank=True, null=True)
#     security_level_number = models.SmallIntegerField(blank=True, null=True)
#     client_name = models.CharField(max_length=255, blank=True, null=True)
#     is_container_removed_on_ret_trig = models.SmallIntegerField(
#         blank=True, null=True)
#     is_set_home_on_container_ret_trig = models.SmallIntegerField(
#         blank=True, null=True)
#     retention_schedule_new_home = models.CharField(
#         max_length=32, blank=True, null=True)
#     is_misfiled = models.SmallIntegerField(blank=True, null=True)
#     master_uid = models.CharField(max_length=65, blank=True, null=True)
#     hybrid_remarks = models.TextField(blank=True, null=True)
#     date_last_modified_of_security_level = models.DateTimeField(
#         blank=True, null=True)
#     is_declassify = models.SmallIntegerField(blank=True, null=True)
#     is_imported = models.SmallIntegerField(blank=True, null=True)
#     enforce_single_creation_in_a_workflow = models.SmallIntegerField()
#     check_in_as_new_version = models.SmallIntegerField()
#     check_in_as_override_previous_content = models.SmallIntegerField()
#     is_declassify_alias = models.TextField(blank=True, null=True)
#     is_auto_update_security_level = models.SmallIntegerField()
#     is_auto_update_security_level_on_particular_date = models.SmallIntegerField()
#     security_level_trigger_date = models.DateTimeField(blank=True, null=True)
#     is_update_security_level_on_triggered_event = models.SmallIntegerField()
#     security_level_triggered_event = models.IntegerField(blank=True, null=True)
#     security_level_triggered_event_type = models.IntegerField(
#         blank=True, null=True)
#     security_level_triggered_event_duration = models.IntegerField(
#         blank=True, null=True)
#     security_level_triggered_event_property = models.CharField(
#         max_length=32, blank=True, null=True)
#     auto_update_security_level_id = models.CharField(
#         max_length=32, blank=True, null=True)
#     c1fb9f1f82af496cbbfd8f387aefab42 = models.CharField(
#         max_length=20, blank=True, null=True)
#     mdd00000000000000000000000msn001 = models.CharField(
#         max_length=100, blank=True, null=True)
#     mdd000000000000000000000002ncn01 = models.CharField(
#         max_length=255, blank=True, null=True)
#     mdd00000000000000000000000mea001 = models.TextField(blank=True, null=True)
#     a0000000000000000000000000000003 = models.CharField(
#         max_length=255, blank=True, null=True)
#     mdd00000000000000000000000uas001 = models.SmallIntegerField(
#         blank=True, null=True)
#     fc3b7ba10a1441c8ae2f6884869bd95f = models.CharField(
#         max_length=100, blank=True, null=True)
#     mdd00000000000000000000000arfs01 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000desc01 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000encr01 = models.CharField(
#         max_length=255, blank=True, null=True)
#     mdd00000000000000000000000eesk01 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000ccur01 = models.CharField(
#         max_length=255, blank=True, null=True)
#     mdd00000000000000000000000mcur01 = models.CharField(
#         max_length=255, blank=True, null=True)
#     mdd00000000000000000000000murl01 = models.CharField(
#         max_length=255, blank=True, null=True)
#     mdd00000000000000000000000tctm01 = models.TextField(blank=True, null=True)
#     mdd00000000000000000000000tcti01 = models.TextField(blank=True, null=True)
#     mdd00000000000000000000000mrnp01 = models.CharField(
#         max_length=100, blank=True, null=True)
#     j8e43ac4e85940c6a15e4c35f0a5a7e5 = models.CharField(
#         max_length=20, blank=True, null=True)
#     mdd00000000000000000000000auic01 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000addi01 = models.TextField(blank=True, null=True)
#     mdd00000000000000000000000addm01 = models.TextField(blank=True, null=True)
#     mdd00000000000000000000000aenc01 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000aexr01 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000bxai01 = models.CharField(
#         max_length=100, blank=True, null=True)
#     mdd00000000000000000000000bxam01 = models.CharField(
#         max_length=100, blank=True, null=True)
#     mdd00000000000000000000000bnam01 = models.CharField(
#         max_length=100, blank=True, null=True)
#     mdd00000000000000000000000bnai01 = models.CharField(
#         max_length=100, blank=True, null=True)
#     mdd00000000000000000000000cxai01 = models.CharField(
#         max_length=100, blank=True, null=True)
#     mdd00000000000000000000000cxam01 = models.CharField(
#         max_length=100, blank=True, null=True)
#     mdd00000000000000000000000cnai01 = models.CharField(
#         max_length=100, blank=True, null=True)
#     mdd00000000000000000000000cnam01 = models.CharField(
#         max_length=100, blank=True, null=True)
#     mdd00000000000000000000000dram01 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000dyfm01 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000eaci01 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd0000000000000000000000000001p = models.CharField(
#         max_length=100, blank=True, null=True)
#     mdd00000000000000000000000enri01 = models.CharField(
#         max_length=100, blank=True, null=True)
#     mdd00000000000000000000000encf01 = models.DateTimeField(
#         blank=True, null=True)
#     mdd00000000000000000000000frqs01 = models.TextField(blank=True, null=True)
#     mdd00000000000000000000000idts01 = models.TextField(blank=True, null=True)
#     mdd00000000000000000000000minr01 = models.CharField(
#         max_length=255, blank=True, null=True)
#     mdd00000000000000000000000nor001 = models.CharField(
#         max_length=100, blank=True, null=True)
#     mdd00000000000000000000000pwst01 = models.CharField(
#         max_length=100, blank=True, null=True)
#     mdd00000000000000000000000purs01 = models.TextField(blank=True, null=True)
#     mdd00000000000000000000000senn01 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000agmr01 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000ctp001 = models.TextField(blank=True, null=True)
#     mdd00000000000000000000000dps001 = models.TextField(blank=True, null=True)
#     mdd00000000000000000000000aip001 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000awa001 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000ipds01 = models.TextField(blank=True, null=True)
#     mdd00000000000000000000000emna01 = models.CharField(
#         max_length=255, blank=True, null=True)
#     mdd00000000000000000000000tcfi01 = models.CharField(
#         max_length=255, blank=True, null=True)
#     mdd00000000000000000000000tcfm01 = models.CharField(
#         max_length=255, blank=True, null=True)
#     mdd00000000000000000000000cnce01 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000cure01 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000mmare1 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000cmare1 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000cifae1 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000cifce1 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000cifne1 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000cifpae = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000cifre1 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000cmce01 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000cmme01 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000cmmre1 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000cmpabe = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000cmpae1 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000cmre01 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000cmsae1 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000cmste1 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000cmtre1 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000mmce01 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000mmpabe = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000mmpae1 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000mmsae1 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000mmste1 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000mmtre1 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000mifne1 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000mifre1 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000mifae1 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000mifce1 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000mifpae = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000smifn1 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000smra01 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000mxid01 = models.CharField(
#         max_length=255, blank=True, null=True)
#     mdd00000000000000000000000mxme01 = models.TextField(blank=True, null=True)
#     mdd00000000000000000000000mxmen1 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000mxn001 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000mxoe01 = models.TextField(blank=True, null=True)
#     mdd00000000000000000000000mxoen1 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000mxsen1 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000rebe01 = models.TextField(blank=True, null=True)
#     mdd00000000000000000000000reben1 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000recf01 = models.DateTimeField(
#         blank=True, null=True)
#     mdd00000000000000000000000reme01 = models.TextField(blank=True, null=True)
#     mdd00000000000000000000000remen1 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000reoe01 = models.TextField(blank=True, null=True)
#     mdd00000000000000000000000reoen1 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000resen1 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000reri01 = models.CharField(
#         max_length=255, blank=True, null=True)
#     mdd00000000000000000000000sren01 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000ense01 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000enoen1 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000enoe01 = models.TextField(blank=True, null=True)
#     mdd00000000000000000000000enmen1 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000enme01 = models.TextField(blank=True, null=True)
#     mdd00000000000000000000pkgen0001 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000pkgensmf1 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000pkgsd0001 = models.CharField(
#         max_length=100, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'nodetype_cf35c509e3e846f2a5c7a2fdba57cb34'


# class NodetypeD91D5170Deb3497Dbedce5912A3Aa016(models.Model):
#     uid = models.CharField(primary_key=True, max_length=65)
#     acl_uid = models.ForeignKey(
#         Acl, models.DO_NOTHING, db_column='acl_uid', blank=True, null=True)
#     owner_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='owner_uid', blank=True, null=True)
#     classification_uid = models.ForeignKey(
#         Classification, models.DO_NOTHING, db_column='classification_uid', blank=True, null=True)
#     secondary_classification_uid = models.CharField(
#         max_length=32, blank=True, null=True)
#     tertiary_classification_uid = models.CharField(
#         max_length=32, blank=True, null=True)
#     record_number = models.CharField(max_length=100, blank=True, null=True)
#     retention_schedule_uid = models.ForeignKey(
#         'RetentionSchedule', models.DO_NOTHING, db_column='retention_schedule_uid', blank=True, null=True)
#     hold_uid = models.ForeignKey(
#         Hold, models.DO_NOTHING, db_column='hold_uid', blank=True, null=True)
#     disposition_status = models.IntegerField(blank=True, null=True)
#     title = models.CharField(max_length=255, blank=True, null=True)
#     combined_title = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     date_registered = models.DateTimeField(blank=True, null=True)
#     creator_name = models.CharField(max_length=255, blank=True, null=True)
#     creator_username = models.CharField(max_length=255, blank=True, null=True)
#     notes = models.TextField(blank=True, null=True)
#     home_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='home_uid', blank=True, null=True)
#     assignee_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='assignee_uid', blank=True, null=True)
#     is_finalized = models.SmallIntegerField(blank=True, null=True)
#     is_hybrid = models.SmallIntegerField(blank=True, null=True)
#     date_finalized = models.DateTimeField(blank=True, null=True)
#     barcode = models.CharField(max_length=50, blank=True, null=True)
#     external_barcode = models.CharField(max_length=50, blank=True, null=True)
#     external_uid = models.CharField(max_length=50, blank=True, null=True)
#     integrity_check = models.TextField(blank=True, null=True)
#     security_level_uid = models.ForeignKey(
#         'SecurityLevel', models.DO_NOTHING, db_column='security_level_uid', blank=True, null=True)
#     date_last_modified = models.DateTimeField(blank=True, null=True)
#     date_last_modified_of_contents = models.DateTimeField(
#         blank=True, null=True)
#     client_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='client_uid', blank=True, null=True)
#     date_closed = models.DateTimeField(blank=True, null=True)
#     next_enclosure_number = models.IntegerField()
#     enclosure_number_increment = models.IntegerField()
#     uncompressed_record_number = models.CharField(
#         max_length=100, blank=True, null=True)
#     security_based_on_container = models.SmallIntegerField(
#         blank=True, null=True)
#     bypass_referenced_acls = models.SmallIntegerField(blank=True, null=True)
#     opened_temporarily = models.SmallIntegerField(blank=True, null=True)
#     date_created = models.DateTimeField(blank=True, null=True)
#     author = models.CharField(max_length=255, blank=True, null=True)
#     batch_id = models.CharField(max_length=255, blank=True, null=True)
#     date_archived = models.DateTimeField(blank=True, null=True)
#     date_made_inactive = models.DateTimeField(blank=True, null=True)
#     date_of_last_enclosure = models.DateTimeField(blank=True, null=True)
#     date_enclosed = models.DateTimeField(blank=True, null=True)
#     record_class = models.IntegerField()
#     container_record_number = models.CharField(
#         max_length=50, blank=True, null=True)
#     classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     secondary_classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     tertiary_classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     assignee_name = models.CharField(max_length=255, blank=True, null=True)
#     home_name = models.CharField(max_length=255, blank=True, null=True)
#     owner_name = models.CharField(max_length=255, blank=True, null=True)
#     retention_schedule_number = models.CharField(
#         max_length=100, blank=True, null=True)
#     security_level_number = models.SmallIntegerField(blank=True, null=True)
#     client_name = models.CharField(max_length=255, blank=True, null=True)
#     is_container_removed_on_ret_trig = models.SmallIntegerField(
#         blank=True, null=True)
#     is_set_home_on_container_ret_trig = models.SmallIntegerField(
#         blank=True, null=True)
#     retention_schedule_new_home = models.CharField(
#         max_length=32, blank=True, null=True)
#     is_misfiled = models.SmallIntegerField(blank=True, null=True)
#     master_uid = models.CharField(max_length=65, blank=True, null=True)
#     hybrid_remarks = models.TextField(blank=True, null=True)
#     date_last_modified_of_security_level = models.DateTimeField(
#         blank=True, null=True)
#     is_declassify = models.SmallIntegerField(blank=True, null=True)
#     is_imported = models.SmallIntegerField(blank=True, null=True)
#     enforce_single_creation_in_a_workflow = models.SmallIntegerField()
#     check_in_as_new_version = models.SmallIntegerField()
#     check_in_as_override_previous_content = models.SmallIntegerField()
#     is_declassify_alias = models.TextField(blank=True, null=True)
#     is_auto_update_security_level = models.SmallIntegerField()
#     is_auto_update_security_level_on_particular_date = models.SmallIntegerField()
#     security_level_trigger_date = models.DateTimeField(blank=True, null=True)
#     is_update_security_level_on_triggered_event = models.SmallIntegerField()
#     security_level_triggered_event = models.IntegerField(blank=True, null=True)
#     security_level_triggered_event_type = models.IntegerField(
#         blank=True, null=True)
#     security_level_triggered_event_duration = models.IntegerField(
#         blank=True, null=True)
#     security_level_triggered_event_property = models.CharField(
#         max_length=32, blank=True, null=True)
#     auto_update_security_level_id = models.CharField(
#         max_length=32, blank=True, null=True)
#     gf15d57f6c1a44bbad05ed181c0ea8c0 = models.SmallIntegerField(
#         blank=True, null=True)
#     fba294aecf6447c7af2ae54034f99a72 = models.SmallIntegerField(
#         blank=True, null=True)
#     d67b9c82758f4b219c6159fe5a61e7fe = models.SmallIntegerField(
#         blank=True, null=True)
#     a0c09a79df314650b3f110d8accd0cb4 = models.SmallIntegerField(
#         blank=True, null=True)
#     fbbe2417e42e476da35e543ee89b2ff4 = models.CharField(
#         max_length=100, blank=True, null=True)
#     ad313e7ce9b64ada9a03991b44c08d62 = models.CharField(
#         max_length=100, blank=True, null=True)
#     mdd00000000000000000000000dcao01 = models.CharField(
#         max_length=255, blank=True, null=True)
#     mdd00000000000000000000000dcav01 = models.CharField(
#         max_length=255, blank=True, null=True)
#     mdd00000000000000000000000wscd01 = models.CharField(
#         max_length=100, blank=True, null=True)
#     mdd00000000000000000000000wcao01 = models.CharField(
#         max_length=255, blank=True, null=True)
#     mdd00000000000000000000000wcav01 = models.CharField(
#         max_length=100, blank=True, null=True)
#     mdd00000000000000000000000wecmed = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000wmeo01 = models.CharField(
#         max_length=255, blank=True, null=True)
#     mdd00000000000000000000000wmed01 = models.CharField(
#         max_length=100, blank=True, null=True)
#     h51fbfcd1fd04540adc7c35bb032ae63 = models.CharField(
#         max_length=100, blank=True, null=True)
#     jc99056960324f48bcf7176c3cf82ea8 = models.CharField(
#         max_length=100, blank=True, null=True)
#     b6e7bb7619e843fb9f09f4c083185e37 = models.CharField(
#         max_length=100, blank=True, null=True)
#     de2d79cdb02044c796cac6c874f68dcc = models.SmallIntegerField(
#         blank=True, null=True)
#     d38e937c9d39427dbf4acf2d10d0d431 = models.CharField(
#         max_length=100, blank=True, null=True)
#     g85531ef3f764bd6b0e7f9e37f2b2be9 = models.CharField(
#         max_length=100, blank=True, null=True)
#     mdd00000000000000000000000mso001 = models.CharField(
#         max_length=255, blank=True, null=True)
#     mdd00000000000000000000000mcao01 = models.CharField(
#         max_length=255, blank=True, null=True)
#     mdd00000000000000000000000mcav01 = models.CharField(
#         max_length=100, blank=True, null=True)
#     mdd00000000000000000000000mecmed = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000mmeo01 = models.CharField(
#         max_length=255, blank=True, null=True)
#     mdd00000000000000000000000mmed01 = models.CharField(
#         max_length=100, blank=True, null=True)
#     mdd00000000000000000000000mc2801 = models.SmallIntegerField(
#         blank=True, null=True)
#     jf2731c2763341f8860b49a8a4317fe8 = models.CharField(
#         max_length=100, blank=True, null=True)
#     c5db7ce6e4f6498f81335548430f9aaf = models.CharField(
#         max_length=100, blank=True, null=True)
#     c01f68f39e284e6eb60597d8d08b61a4 = models.CharField(
#         max_length=100, blank=True, null=True)
#     je348d0baaa549a9b91c764a1801f799 = models.SmallIntegerField(
#         blank=True, null=True)
#     j83e72ca7d4e464088ca8ff00c2c5da9 = models.CharField(
#         max_length=100, blank=True, null=True)
#     f0c2f14c76354c4cbf8f8055f657f439 = models.CharField(
#         max_length=100, blank=True, null=True)
#     mdd00000000000000000000000yscd01 = models.CharField(
#         max_length=255, blank=True, null=True)
#     mdd00000000000000000000000ycao01 = models.CharField(
#         max_length=255, blank=True, null=True)
#     mdd00000000000000000000000ycav01 = models.CharField(
#         max_length=100, blank=True, null=True)
#     mdd00000000000000000000000yecoed = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000ymeop1 = models.CharField(
#         max_length=255, blank=True, null=True)
#     mdd00000000000000000000000ymed01 = models.CharField(
#         max_length=100, blank=True, null=True)
#     mdd00000000000000000000000enamc1 = models.SmallIntegerField(
#         blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'nodetype_d91d5170deb3497dbedce5912a3aa016'


# class NodetypeDc8E3Bc6F41F4F15Aa445184108A680A(models.Model):
#     uid = models.CharField(primary_key=True, max_length=65)
#     acl_uid = models.ForeignKey(
#         Acl, models.DO_NOTHING, db_column='acl_uid', blank=True, null=True)
#     owner_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='owner_uid', blank=True, null=True)
#     classification_uid = models.ForeignKey(
#         Classification, models.DO_NOTHING, db_column='classification_uid', blank=True, null=True)
#     secondary_classification_uid = models.CharField(
#         max_length=32, blank=True, null=True)
#     tertiary_classification_uid = models.CharField(
#         max_length=32, blank=True, null=True)
#     record_number = models.CharField(max_length=100, blank=True, null=True)
#     retention_schedule_uid = models.ForeignKey(
#         'RetentionSchedule', models.DO_NOTHING, db_column='retention_schedule_uid', blank=True, null=True)
#     hold_uid = models.ForeignKey(
#         Hold, models.DO_NOTHING, db_column='hold_uid', blank=True, null=True)
#     disposition_status = models.IntegerField(blank=True, null=True)
#     title = models.CharField(max_length=255, blank=True, null=True)
#     combined_title = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     date_registered = models.DateTimeField(blank=True, null=True)
#     creator_name = models.CharField(max_length=255, blank=True, null=True)
#     creator_username = models.CharField(max_length=255, blank=True, null=True)
#     notes = models.TextField(blank=True, null=True)
#     home_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='home_uid', blank=True, null=True)
#     assignee_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='assignee_uid', blank=True, null=True)
#     is_finalized = models.SmallIntegerField(blank=True, null=True)
#     is_hybrid = models.SmallIntegerField(blank=True, null=True)
#     date_finalized = models.DateTimeField(blank=True, null=True)
#     barcode = models.CharField(max_length=50, blank=True, null=True)
#     external_barcode = models.CharField(max_length=50, blank=True, null=True)
#     external_uid = models.CharField(max_length=50, blank=True, null=True)
#     integrity_check = models.TextField(blank=True, null=True)
#     security_level_uid = models.ForeignKey(
#         'SecurityLevel', models.DO_NOTHING, db_column='security_level_uid', blank=True, null=True)
#     date_last_modified = models.DateTimeField(blank=True, null=True)
#     date_last_modified_of_contents = models.DateTimeField(
#         blank=True, null=True)
#     client_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='client_uid', blank=True, null=True)
#     date_closed = models.DateTimeField(blank=True, null=True)
#     next_enclosure_number = models.IntegerField()
#     enclosure_number_increment = models.IntegerField()
#     uncompressed_record_number = models.CharField(
#         max_length=100, blank=True, null=True)
#     security_based_on_container = models.SmallIntegerField(
#         blank=True, null=True)
#     bypass_referenced_acls = models.SmallIntegerField(blank=True, null=True)
#     opened_temporarily = models.SmallIntegerField(blank=True, null=True)
#     date_created = models.DateTimeField(blank=True, null=True)
#     author = models.CharField(max_length=255, blank=True, null=True)
#     batch_id = models.CharField(max_length=40, blank=True, null=True)
#     date_archived = models.DateTimeField(blank=True, null=True)
#     date_made_inactive = models.DateTimeField(blank=True, null=True)
#     date_of_last_enclosure = models.DateTimeField(blank=True, null=True)
#     date_enclosed = models.DateTimeField(blank=True, null=True)
#     record_class = models.IntegerField()
#     container_record_number = models.CharField(
#         max_length=50, blank=True, null=True)
#     classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     secondary_classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     tertiary_classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     assignee_name = models.CharField(max_length=255, blank=True, null=True)
#     home_name = models.CharField(max_length=255, blank=True, null=True)
#     owner_name = models.CharField(max_length=255, blank=True, null=True)
#     retention_schedule_number = models.CharField(
#         max_length=100, blank=True, null=True)
#     security_level_number = models.SmallIntegerField(blank=True, null=True)
#     client_name = models.CharField(max_length=255, blank=True, null=True)
#     is_container_removed_on_ret_trig = models.SmallIntegerField(
#         blank=True, null=True)
#     is_set_home_on_container_ret_trig = models.SmallIntegerField(
#         blank=True, null=True)
#     retention_schedule_new_home = models.CharField(
#         max_length=32, blank=True, null=True)
#     is_misfiled = models.SmallIntegerField(blank=True, null=True)
#     master_uid = models.CharField(max_length=65, blank=True, null=True)
#     hybrid_remarks = models.TextField(blank=True, null=True)
#     date_last_modified_of_security_level = models.DateTimeField(
#         blank=True, null=True)
#     is_declassify = models.SmallIntegerField(blank=True, null=True)
#     is_imported = models.SmallIntegerField(blank=True, null=True)
#     enforce_single_creation_in_a_workflow = models.SmallIntegerField()
#     check_in_as_new_version = models.SmallIntegerField()
#     check_in_as_override_previous_content = models.SmallIntegerField()
#     is_declassify_alias = models.TextField(blank=True, null=True)
#     is_auto_update_security_level = models.SmallIntegerField()
#     is_auto_update_security_level_on_particular_date = models.SmallIntegerField()
#     security_level_trigger_date = models.DateTimeField(blank=True, null=True)
#     is_update_security_level_on_triggered_event = models.SmallIntegerField()
#     security_level_triggered_event = models.IntegerField(blank=True, null=True)
#     security_level_triggered_event_type = models.IntegerField(
#         blank=True, null=True)
#     security_level_triggered_event_duration = models.IntegerField(
#         blank=True, null=True)
#     security_level_triggered_event_property = models.CharField(
#         max_length=32, blank=True, null=True)
#     auto_update_security_level_id = models.CharField(
#         max_length=32, blank=True, null=True)
#     j72d25f47afb42ea84fd364233a29430 = models.CharField(
#         max_length=50, blank=True, null=True)
#     a4d54a1736fa45e796aa89ff04b83f55 = models.CharField(
#         max_length=255, blank=True, null=True)
#     ibdaf89d09234fef9826c0f2a81ef088 = models.CharField(
#         max_length=255, blank=True, null=True)
#     f5da945a323c4488b407142013d47646 = models.CharField(
#         max_length=15, blank=True, null=True)
#     ac587b9bdb0545d9a4bb872848b12755 = models.CharField(
#         max_length=100, blank=True, null=True)
#     c7b15198b7a844d2bbe56fa6116f9018 = models.CharField(
#         max_length=50, blank=True, null=True)
#     b1b99355d0834804a01b7a69fc2421bd = models.DecimalField(
#         max_digits=16, decimal_places=2, blank=True, null=True)
#     f9ce8fde98e547699ff79602b2dce34f = models.DateTimeField(
#         blank=True, null=True)
#     hea71551e76346ad8f8e87f13911c1b3 = models.CharField(
#         max_length=100, blank=True, null=True)
#     afd1329c2de2421bbbe5a48f65b56818 = models.CharField(
#         max_length=255, blank=True, null=True)
#     c1fb9f1f82af496cbbfd8f387aefab42 = models.CharField(
#         max_length=20, blank=True, null=True)
#     ha41c373c2f0413cb1458bb886048bb2 = models.CharField(
#         max_length=255, blank=True, null=True)
#     f0970f3862f941338e162f34b75e6831 = models.CharField(
#         max_length=50, blank=True, null=True)
#     h7f705c3a23b48a897df194cb6aa373f = models.CharField(
#         max_length=100, blank=True, null=True)
#     ba832c949a544def959b33f23ebd6404 = models.CharField(
#         max_length=4, blank=True, null=True)
#     d17a4a24785a4faba79f0a6135ca214c = models.CharField(
#         max_length=255, blank=True, null=True)
#     h3ff7814caaf4664a54a4d0cb2748ea4 = models.CharField(
#         max_length=50, blank=True, null=True)
#     ac88f80ecee245b0821768d6493db2c2 = models.DateTimeField(
#         blank=True, null=True)
#     b7aadfe282354bff9f5d437ab9e52511 = models.CharField(
#         max_length=255, blank=True, null=True)
#     d10e16c77b0f4a7987f65e710a629f02 = models.CharField(
#         max_length=255, blank=True, null=True)
#     f218857ed07c448dbfe8f03332b144f9 = models.CharField(
#         max_length=50, blank=True, null=True)
#     ie250b9283204d01ade2f7a0136a8ead = models.DateTimeField(
#         blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'nodetype_dc8e3bc6f41f4f15aa445184108a680a'


# class NodetypeE3Cfb64D11D24A9B955Bf1Dbf93724Ba(models.Model):
#     uid = models.CharField(primary_key=True, max_length=65)
#     acl_uid = models.ForeignKey(
#         Acl, models.DO_NOTHING, db_column='acl_uid', blank=True, null=True)
#     owner_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='owner_uid', blank=True, null=True)
#     classification_uid = models.ForeignKey(
#         Classification, models.DO_NOTHING, db_column='classification_uid', blank=True, null=True)
#     secondary_classification_uid = models.CharField(
#         max_length=32, blank=True, null=True)
#     tertiary_classification_uid = models.CharField(
#         max_length=32, blank=True, null=True)
#     record_number = models.CharField(max_length=100, blank=True, null=True)
#     retention_schedule_uid = models.ForeignKey(
#         'RetentionSchedule', models.DO_NOTHING, db_column='retention_schedule_uid', blank=True, null=True)
#     hold_uid = models.ForeignKey(
#         Hold, models.DO_NOTHING, db_column='hold_uid', blank=True, null=True)
#     disposition_status = models.IntegerField(blank=True, null=True)
#     title = models.CharField(max_length=255, blank=True, null=True)
#     combined_title = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     date_registered = models.DateTimeField(blank=True, null=True)
#     creator_name = models.CharField(max_length=255, blank=True, null=True)
#     creator_username = models.CharField(max_length=255, blank=True, null=True)
#     notes = models.TextField(blank=True, null=True)
#     home_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='home_uid', blank=True, null=True)
#     assignee_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='assignee_uid', blank=True, null=True)
#     is_finalized = models.SmallIntegerField(blank=True, null=True)
#     is_hybrid = models.SmallIntegerField(blank=True, null=True)
#     date_finalized = models.DateTimeField(blank=True, null=True)
#     barcode = models.CharField(max_length=50, blank=True, null=True)
#     external_barcode = models.CharField(max_length=50, blank=True, null=True)
#     external_uid = models.CharField(max_length=50, blank=True, null=True)
#     integrity_check = models.TextField(blank=True, null=True)
#     security_level_uid = models.ForeignKey(
#         'SecurityLevel', models.DO_NOTHING, db_column='security_level_uid', blank=True, null=True)
#     date_last_modified = models.DateTimeField(blank=True, null=True)
#     date_last_modified_of_contents = models.DateTimeField(
#         blank=True, null=True)
#     client_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='client_uid', blank=True, null=True)
#     date_closed = models.DateTimeField(blank=True, null=True)
#     next_enclosure_number = models.IntegerField()
#     enclosure_number_increment = models.IntegerField()
#     uncompressed_record_number = models.CharField(
#         max_length=100, blank=True, null=True)
#     security_based_on_container = models.SmallIntegerField(
#         blank=True, null=True)
#     bypass_referenced_acls = models.SmallIntegerField(blank=True, null=True)
#     opened_temporarily = models.SmallIntegerField(blank=True, null=True)
#     date_created = models.DateTimeField(blank=True, null=True)
#     author = models.CharField(max_length=255, blank=True, null=True)
#     batch_id = models.CharField(max_length=255, blank=True, null=True)
#     date_archived = models.DateTimeField(blank=True, null=True)
#     date_made_inactive = models.DateTimeField(blank=True, null=True)
#     date_of_last_enclosure = models.DateTimeField(blank=True, null=True)
#     date_enclosed = models.DateTimeField(blank=True, null=True)
#     record_class = models.IntegerField()
#     container_record_number = models.CharField(
#         max_length=50, blank=True, null=True)
#     classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     secondary_classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     tertiary_classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     assignee_name = models.CharField(max_length=255, blank=True, null=True)
#     home_name = models.CharField(max_length=255, blank=True, null=True)
#     owner_name = models.CharField(max_length=255, blank=True, null=True)
#     retention_schedule_number = models.CharField(
#         max_length=100, blank=True, null=True)
#     security_level_number = models.SmallIntegerField(blank=True, null=True)
#     client_name = models.CharField(max_length=255, blank=True, null=True)
#     is_container_removed_on_ret_trig = models.SmallIntegerField(
#         blank=True, null=True)
#     is_set_home_on_container_ret_trig = models.SmallIntegerField(
#         blank=True, null=True)
#     retention_schedule_new_home = models.CharField(
#         max_length=32, blank=True, null=True)
#     is_misfiled = models.SmallIntegerField(blank=True, null=True)
#     master_uid = models.CharField(max_length=65, blank=True, null=True)
#     hybrid_remarks = models.TextField(blank=True, null=True)
#     date_last_modified_of_security_level = models.DateTimeField(
#         blank=True, null=True)
#     is_declassify = models.SmallIntegerField(blank=True, null=True)
#     is_imported = models.SmallIntegerField(blank=True, null=True)
#     enforce_single_creation_in_a_workflow = models.SmallIntegerField()
#     check_in_as_new_version = models.SmallIntegerField()
#     check_in_as_override_previous_content = models.SmallIntegerField()
#     is_declassify_alias = models.TextField(blank=True, null=True)
#     is_auto_update_security_level = models.SmallIntegerField()
#     is_auto_update_security_level_on_particular_date = models.SmallIntegerField()
#     security_level_trigger_date = models.DateTimeField(blank=True, null=True)
#     is_update_security_level_on_triggered_event = models.SmallIntegerField()
#     security_level_triggered_event = models.IntegerField(blank=True, null=True)
#     security_level_triggered_event_type = models.IntegerField(
#         blank=True, null=True)
#     security_level_triggered_event_duration = models.IntegerField(
#         blank=True, null=True)
#     security_level_triggered_event_property = models.CharField(
#         max_length=32, blank=True, null=True)
#     auto_update_security_level_id = models.CharField(
#         max_length=32, blank=True, null=True)
#     fc3b7ba10a1441c8ae2f6884869bd95f = models.CharField(
#         max_length=100, blank=True, null=True)
#     f1cc064c505249df913a9cb83068cc03 = models.CharField(
#         max_length=255, blank=True, null=True)
#     b68d1d522f604375b9b48f486e596760 = models.CharField(
#         max_length=255, blank=True, null=True)
#     cc9520041083491abe5f65256ed5ea91 = models.CharField(
#         max_length=255, blank=True, null=True)
#     f06b48e8bdc94cbfbbc6ffebfd276d94 = models.CharField(
#         max_length=255, blank=True, null=True)
#     ibdaf89d09234fef9826c0f2a81ef088 = models.CharField(
#         max_length=255, blank=True, null=True)
#     a4d54a1736fa45e796aa89ff04b83f55 = models.CharField(
#         max_length=255, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'nodetype_e3cfb64d11d24a9b955bf1dbf93724ba'


# class NodetypeE5777068Dbf64A4D9Abbc21797C8Bae2(models.Model):
#     uid = models.CharField(primary_key=True, max_length=65)
#     acl_uid = models.ForeignKey(
#         Acl, models.DO_NOTHING, db_column='acl_uid', blank=True, null=True)
#     owner_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='owner_uid', blank=True, null=True)
#     classification_uid = models.ForeignKey(
#         Classification, models.DO_NOTHING, db_column='classification_uid', blank=True, null=True)
#     secondary_classification_uid = models.CharField(
#         max_length=32, blank=True, null=True)
#     tertiary_classification_uid = models.CharField(
#         max_length=32, blank=True, null=True)
#     record_number = models.CharField(max_length=100, blank=True, null=True)
#     retention_schedule_uid = models.ForeignKey(
#         'RetentionSchedule', models.DO_NOTHING, db_column='retention_schedule_uid', blank=True, null=True)
#     hold_uid = models.ForeignKey(
#         Hold, models.DO_NOTHING, db_column='hold_uid', blank=True, null=True)
#     disposition_status = models.IntegerField(blank=True, null=True)
#     title = models.CharField(max_length=255, blank=True, null=True)
#     combined_title = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     date_registered = models.DateTimeField(blank=True, null=True)
#     creator_name = models.CharField(max_length=255, blank=True, null=True)
#     creator_username = models.CharField(max_length=255, blank=True, null=True)
#     notes = models.TextField(blank=True, null=True)
#     home_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='home_uid', blank=True, null=True)
#     assignee_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='assignee_uid', blank=True, null=True)
#     is_finalized = models.SmallIntegerField(blank=True, null=True)
#     is_hybrid = models.SmallIntegerField(blank=True, null=True)
#     date_finalized = models.DateTimeField(blank=True, null=True)
#     barcode = models.CharField(max_length=50, blank=True, null=True)
#     external_barcode = models.CharField(max_length=50, blank=True, null=True)
#     external_uid = models.CharField(max_length=50, blank=True, null=True)
#     integrity_check = models.TextField(blank=True, null=True)
#     security_level_uid = models.ForeignKey(
#         'SecurityLevel', models.DO_NOTHING, db_column='security_level_uid', blank=True, null=True)
#     date_last_modified = models.DateTimeField(blank=True, null=True)
#     date_last_modified_of_contents = models.DateTimeField(
#         blank=True, null=True)
#     client_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='client_uid', blank=True, null=True)
#     date_closed = models.DateTimeField(blank=True, null=True)
#     next_enclosure_number = models.IntegerField()
#     enclosure_number_increment = models.IntegerField()
#     uncompressed_record_number = models.CharField(
#         max_length=100, blank=True, null=True)
#     security_based_on_container = models.SmallIntegerField(
#         blank=True, null=True)
#     bypass_referenced_acls = models.SmallIntegerField(blank=True, null=True)
#     opened_temporarily = models.SmallIntegerField(blank=True, null=True)
#     date_created = models.DateTimeField(blank=True, null=True)
#     author = models.CharField(max_length=255, blank=True, null=True)
#     batch_id = models.CharField(max_length=255, blank=True, null=True)
#     date_archived = models.DateTimeField(blank=True, null=True)
#     date_made_inactive = models.DateTimeField(blank=True, null=True)
#     date_of_last_enclosure = models.DateTimeField(blank=True, null=True)
#     date_enclosed = models.DateTimeField(blank=True, null=True)
#     record_class = models.IntegerField()
#     container_record_number = models.CharField(
#         max_length=50, blank=True, null=True)
#     classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     secondary_classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     tertiary_classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     assignee_name = models.CharField(max_length=255, blank=True, null=True)
#     home_name = models.CharField(max_length=255, blank=True, null=True)
#     owner_name = models.CharField(max_length=255, blank=True, null=True)
#     retention_schedule_number = models.CharField(
#         max_length=100, blank=True, null=True)
#     security_level_number = models.SmallIntegerField(blank=True, null=True)
#     client_name = models.CharField(max_length=255, blank=True, null=True)
#     is_container_removed_on_ret_trig = models.SmallIntegerField(
#         blank=True, null=True)
#     is_set_home_on_container_ret_trig = models.SmallIntegerField(
#         blank=True, null=True)
#     retention_schedule_new_home = models.CharField(
#         max_length=32, blank=True, null=True)
#     is_misfiled = models.SmallIntegerField(blank=True, null=True)
#     master_uid = models.CharField(max_length=65, blank=True, null=True)
#     hybrid_remarks = models.TextField(blank=True, null=True)
#     date_last_modified_of_security_level = models.DateTimeField(
#         blank=True, null=True)
#     is_declassify = models.SmallIntegerField(blank=True, null=True)
#     is_imported = models.SmallIntegerField(blank=True, null=True)
#     enforce_single_creation_in_a_workflow = models.SmallIntegerField()
#     check_in_as_new_version = models.SmallIntegerField()
#     check_in_as_override_previous_content = models.SmallIntegerField()
#     is_declassify_alias = models.TextField(blank=True, null=True)
#     is_auto_update_security_level = models.SmallIntegerField()
#     is_auto_update_security_level_on_particular_date = models.SmallIntegerField()
#     security_level_trigger_date = models.DateTimeField(blank=True, null=True)
#     is_update_security_level_on_triggered_event = models.SmallIntegerField()
#     security_level_triggered_event = models.IntegerField(blank=True, null=True)
#     security_level_triggered_event_type = models.IntegerField(
#         blank=True, null=True)
#     security_level_triggered_event_duration = models.IntegerField(
#         blank=True, null=True)
#     security_level_triggered_event_property = models.CharField(
#         max_length=32, blank=True, null=True)
#     auto_update_security_level_id = models.CharField(
#         max_length=32, blank=True, null=True)
#     mdd00000000000000000000pkgacxd01 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000pkgctctx1 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000pkgenca01 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000pkgendpb1 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000pkgiipl01 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000pkglb0001 = models.CharField(
#         max_length=255, blank=True, null=True)
#     mdd00000000000000000000pkgpe0001 = models.CharField(
#         max_length=100, blank=True, null=True)
#     mdd00000000000000000000pkgpeop01 = models.CharField(
#         max_length=100, blank=True, null=True)
#     mdd00000000000000000000pkgsdf001 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000pkgsdpop1 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000pkgsxdad1 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000pkgsxf001 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000pkgcamt01 = models.CharField(
#         max_length=100, blank=True, null=True)
#     mdd00000000000000000000pkgnday01 = models.CharField(
#         max_length=100, blank=True, null=True)
#     mdd00000000000000000000pkgxfreq1 = models.CharField(
#         max_length=100, blank=True, null=True)
#     mdd00000000000000000000000tctm01 = models.TextField(blank=True, null=True)
#     mdd00000000000000000000pkgcaaxta = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000pkgpopymt = models.CharField(
#         max_length=255, blank=True, null=True)
#     mdd00000000000000000000pkgen0001 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000pkgensmf1 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000pkgsd0001 = models.CharField(
#         max_length=100, blank=True, null=True)
#     mdd00000000000000000000pkgfreq01 = models.CharField(
#         max_length=255, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'nodetype_e5777068dbf64a4d9abbc21797c8bae2'


# class NodetypeE98Ff175F08F44B4B5C60D859C469C6B(models.Model):
#     uid = models.CharField(primary_key=True, max_length=65)
#     acl_uid = models.ForeignKey(
#         Acl, models.DO_NOTHING, db_column='acl_uid', blank=True, null=True)
#     owner_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='owner_uid', blank=True, null=True)
#     classification_uid = models.ForeignKey(
#         Classification, models.DO_NOTHING, db_column='classification_uid', blank=True, null=True)
#     secondary_classification_uid = models.CharField(
#         max_length=32, blank=True, null=True)
#     tertiary_classification_uid = models.CharField(
#         max_length=32, blank=True, null=True)
#     record_number = models.CharField(max_length=100, blank=True, null=True)
#     retention_schedule_uid = models.ForeignKey(
#         'RetentionSchedule', models.DO_NOTHING, db_column='retention_schedule_uid', blank=True, null=True)
#     hold_uid = models.ForeignKey(
#         Hold, models.DO_NOTHING, db_column='hold_uid', blank=True, null=True)
#     disposition_status = models.IntegerField(blank=True, null=True)
#     title = models.CharField(max_length=255, blank=True, null=True)
#     combined_title = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     date_registered = models.DateTimeField(blank=True, null=True)
#     creator_name = models.CharField(max_length=255, blank=True, null=True)
#     creator_username = models.CharField(max_length=255, blank=True, null=True)
#     notes = models.TextField(blank=True, null=True)
#     home_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='home_uid', blank=True, null=True)
#     assignee_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='assignee_uid', blank=True, null=True)
#     is_finalized = models.SmallIntegerField(blank=True, null=True)
#     is_hybrid = models.SmallIntegerField(blank=True, null=True)
#     date_finalized = models.DateTimeField(blank=True, null=True)
#     barcode = models.CharField(max_length=50, blank=True, null=True)
#     external_barcode = models.CharField(max_length=50, blank=True, null=True)
#     external_uid = models.CharField(max_length=50, blank=True, null=True)
#     integrity_check = models.TextField(blank=True, null=True)
#     security_level_uid = models.ForeignKey(
#         'SecurityLevel', models.DO_NOTHING, db_column='security_level_uid', blank=True, null=True)
#     date_last_modified = models.DateTimeField(blank=True, null=True)
#     date_last_modified_of_contents = models.DateTimeField(
#         blank=True, null=True)
#     client_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='client_uid', blank=True, null=True)
#     date_closed = models.DateTimeField(blank=True, null=True)
#     next_enclosure_number = models.IntegerField()
#     enclosure_number_increment = models.IntegerField()
#     uncompressed_record_number = models.CharField(
#         max_length=100, blank=True, null=True)
#     security_based_on_container = models.SmallIntegerField(
#         blank=True, null=True)
#     bypass_referenced_acls = models.SmallIntegerField(blank=True, null=True)
#     opened_temporarily = models.SmallIntegerField(blank=True, null=True)
#     date_created = models.DateTimeField(blank=True, null=True)
#     author = models.CharField(max_length=255, blank=True, null=True)
#     batch_id = models.CharField(max_length=255, blank=True, null=True)
#     date_archived = models.DateTimeField(blank=True, null=True)
#     date_made_inactive = models.DateTimeField(blank=True, null=True)
#     date_of_last_enclosure = models.DateTimeField(blank=True, null=True)
#     date_enclosed = models.DateTimeField(blank=True, null=True)
#     record_class = models.IntegerField()
#     container_record_number = models.CharField(
#         max_length=50, blank=True, null=True)
#     classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     secondary_classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     tertiary_classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     assignee_name = models.CharField(max_length=255, blank=True, null=True)
#     home_name = models.CharField(max_length=255, blank=True, null=True)
#     owner_name = models.CharField(max_length=255, blank=True, null=True)
#     retention_schedule_number = models.CharField(
#         max_length=100, blank=True, null=True)
#     security_level_number = models.SmallIntegerField(blank=True, null=True)
#     client_name = models.CharField(max_length=255, blank=True, null=True)
#     is_container_removed_on_ret_trig = models.SmallIntegerField(
#         blank=True, null=True)
#     is_set_home_on_container_ret_trig = models.SmallIntegerField(
#         blank=True, null=True)
#     retention_schedule_new_home = models.CharField(
#         max_length=32, blank=True, null=True)
#     is_misfiled = models.SmallIntegerField(blank=True, null=True)
#     master_uid = models.CharField(max_length=65, blank=True, null=True)
#     hybrid_remarks = models.TextField(blank=True, null=True)
#     date_last_modified_of_security_level = models.DateTimeField(
#         blank=True, null=True)
#     is_declassify = models.SmallIntegerField(blank=True, null=True)
#     is_imported = models.SmallIntegerField(blank=True, null=True)
#     enforce_single_creation_in_a_workflow = models.SmallIntegerField()
#     check_in_as_new_version = models.SmallIntegerField()
#     check_in_as_override_previous_content = models.SmallIntegerField()
#     is_declassify_alias = models.TextField(blank=True, null=True)
#     is_auto_update_security_level = models.SmallIntegerField()
#     is_auto_update_security_level_on_particular_date = models.SmallIntegerField()
#     security_level_trigger_date = models.DateTimeField(blank=True, null=True)
#     is_update_security_level_on_triggered_event = models.SmallIntegerField()
#     security_level_triggered_event = models.IntegerField(blank=True, null=True)
#     security_level_triggered_event_type = models.IntegerField(
#         blank=True, null=True)
#     security_level_triggered_event_duration = models.IntegerField(
#         blank=True, null=True)
#     security_level_triggered_event_property = models.CharField(
#         max_length=32, blank=True, null=True)
#     auto_update_security_level_id = models.CharField(
#         max_length=32, blank=True, null=True)
#     mdd0000000000000000000000000001p = models.CharField(
#         max_length=100, blank=True, null=True)
#     mdd00000000000000000000000txid01 = models.CharField(
#         max_length=255, blank=True, null=True)
#     mdd00000000000000000000000ene001 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000auc001 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000emna01 = models.CharField(
#         max_length=255, blank=True, null=True)
#     j72d25f47afb42ea84fd364233a29430 = models.CharField(
#         max_length=50, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'nodetype_e98ff175f08f44b4b5c60d859c469c6b'


# class NodetypeEb50047853D6486B8C7F78Ad91D4F454(models.Model):
#     uid = models.CharField(primary_key=True, max_length=65)
#     acl_uid = models.ForeignKey(
#         Acl, models.DO_NOTHING, db_column='acl_uid', blank=True, null=True)
#     owner_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='owner_uid', blank=True, null=True)
#     classification_uid = models.ForeignKey(
#         Classification, models.DO_NOTHING, db_column='classification_uid', blank=True, null=True)
#     secondary_classification_uid = models.CharField(
#         max_length=32, blank=True, null=True)
#     tertiary_classification_uid = models.CharField(
#         max_length=32, blank=True, null=True)
#     record_number = models.CharField(max_length=100, blank=True, null=True)
#     retention_schedule_uid = models.ForeignKey(
#         'RetentionSchedule', models.DO_NOTHING, db_column='retention_schedule_uid', blank=True, null=True)
#     hold_uid = models.ForeignKey(
#         Hold, models.DO_NOTHING, db_column='hold_uid', blank=True, null=True)
#     disposition_status = models.IntegerField(blank=True, null=True)
#     title = models.CharField(max_length=255, blank=True, null=True)
#     combined_title = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     date_registered = models.DateTimeField(blank=True, null=True)
#     creator_name = models.CharField(max_length=255, blank=True, null=True)
#     creator_username = models.CharField(max_length=255, blank=True, null=True)
#     notes = models.TextField(blank=True, null=True)
#     home_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='home_uid', blank=True, null=True)
#     assignee_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='assignee_uid', blank=True, null=True)
#     is_finalized = models.SmallIntegerField(blank=True, null=True)
#     is_hybrid = models.SmallIntegerField(blank=True, null=True)
#     date_finalized = models.DateTimeField(blank=True, null=True)
#     barcode = models.CharField(max_length=50, blank=True, null=True)
#     external_barcode = models.CharField(max_length=50, blank=True, null=True)
#     external_uid = models.CharField(max_length=50, blank=True, null=True)
#     integrity_check = models.TextField(blank=True, null=True)
#     security_level_uid = models.ForeignKey(
#         'SecurityLevel', models.DO_NOTHING, db_column='security_level_uid', blank=True, null=True)
#     date_last_modified = models.DateTimeField(blank=True, null=True)
#     date_last_modified_of_contents = models.DateTimeField(
#         blank=True, null=True)
#     client_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='client_uid', blank=True, null=True)
#     date_closed = models.DateTimeField(blank=True, null=True)
#     next_enclosure_number = models.IntegerField()
#     enclosure_number_increment = models.IntegerField()
#     uncompressed_record_number = models.CharField(
#         max_length=100, blank=True, null=True)
#     security_based_on_container = models.SmallIntegerField(
#         blank=True, null=True)
#     bypass_referenced_acls = models.SmallIntegerField(blank=True, null=True)
#     opened_temporarily = models.SmallIntegerField(blank=True, null=True)
#     date_created = models.DateTimeField(blank=True, null=True)
#     author = models.CharField(max_length=255, blank=True, null=True)
#     batch_id = models.CharField(max_length=40, blank=True, null=True)
#     date_archived = models.DateTimeField(blank=True, null=True)
#     date_made_inactive = models.DateTimeField(blank=True, null=True)
#     date_of_last_enclosure = models.DateTimeField(blank=True, null=True)
#     date_enclosed = models.DateTimeField(blank=True, null=True)
#     record_class = models.IntegerField()
#     container_record_number = models.CharField(
#         max_length=50, blank=True, null=True)
#     classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     secondary_classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     tertiary_classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     assignee_name = models.CharField(max_length=255, blank=True, null=True)
#     home_name = models.CharField(max_length=255, blank=True, null=True)
#     owner_name = models.CharField(max_length=255, blank=True, null=True)
#     retention_schedule_number = models.CharField(
#         max_length=100, blank=True, null=True)
#     security_level_number = models.SmallIntegerField(blank=True, null=True)
#     client_name = models.CharField(max_length=255, blank=True, null=True)
#     is_container_removed_on_ret_trig = models.SmallIntegerField(
#         blank=True, null=True)
#     is_set_home_on_container_ret_trig = models.SmallIntegerField(
#         blank=True, null=True)
#     retention_schedule_new_home = models.CharField(
#         max_length=32, blank=True, null=True)
#     is_misfiled = models.SmallIntegerField(blank=True, null=True)
#     master_uid = models.CharField(max_length=65, blank=True, null=True)
#     hybrid_remarks = models.TextField(blank=True, null=True)
#     date_last_modified_of_security_level = models.DateTimeField(
#         blank=True, null=True)
#     is_declassify = models.SmallIntegerField(blank=True, null=True)
#     is_imported = models.SmallIntegerField(blank=True, null=True)
#     enforce_single_creation_in_a_workflow = models.SmallIntegerField()
#     check_in_as_new_version = models.SmallIntegerField()
#     check_in_as_override_previous_content = models.SmallIntegerField()
#     is_declassify_alias = models.TextField(blank=True, null=True)
#     is_auto_update_security_level = models.SmallIntegerField()
#     is_auto_update_security_level_on_particular_date = models.SmallIntegerField()
#     security_level_trigger_date = models.DateTimeField(blank=True, null=True)
#     is_update_security_level_on_triggered_event = models.SmallIntegerField()
#     security_level_triggered_event = models.IntegerField(blank=True, null=True)
#     security_level_triggered_event_type = models.IntegerField(
#         blank=True, null=True)
#     security_level_triggered_event_duration = models.IntegerField(
#         blank=True, null=True)
#     security_level_triggered_event_property = models.CharField(
#         max_length=32, blank=True, null=True)
#     auto_update_security_level_id = models.CharField(
#         max_length=32, blank=True, null=True)
#     fdc659695c944890b9c1720de461db2e = models.ForeignKey(
#         'RecordNode', models.DO_NOTHING, db_column='fdc659695c944890b9c1720de461db2e', blank=True, null=True)
#     j8e43ac4e85940c6a15e4c35f0a5a7e5 = models.CharField(
#         max_length=20, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'nodetype_eb50047853d6486b8c7f78ad91d4f454'


# class NodetypeEcbfc51142D84Ef68C62847B60924F7A(models.Model):
#     uid = models.CharField(primary_key=True, max_length=65)
#     acl_uid = models.ForeignKey(
#         Acl, models.DO_NOTHING, db_column='acl_uid', blank=True, null=True)
#     owner_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='owner_uid', blank=True, null=True)
#     classification_uid = models.ForeignKey(
#         Classification, models.DO_NOTHING, db_column='classification_uid', blank=True, null=True)
#     secondary_classification_uid = models.CharField(
#         max_length=32, blank=True, null=True)
#     tertiary_classification_uid = models.CharField(
#         max_length=32, blank=True, null=True)
#     record_number = models.CharField(max_length=100, blank=True, null=True)
#     retention_schedule_uid = models.ForeignKey(
#         'RetentionSchedule', models.DO_NOTHING, db_column='retention_schedule_uid', blank=True, null=True)
#     hold_uid = models.ForeignKey(
#         Hold, models.DO_NOTHING, db_column='hold_uid', blank=True, null=True)
#     disposition_status = models.IntegerField(blank=True, null=True)
#     title = models.CharField(max_length=255, blank=True, null=True)
#     combined_title = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     date_registered = models.DateTimeField(blank=True, null=True)
#     creator_name = models.CharField(max_length=255, blank=True, null=True)
#     creator_username = models.CharField(max_length=255, blank=True, null=True)
#     notes = models.TextField(blank=True, null=True)
#     home_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='home_uid', blank=True, null=True)
#     assignee_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='assignee_uid', blank=True, null=True)
#     is_finalized = models.SmallIntegerField(blank=True, null=True)
#     is_hybrid = models.SmallIntegerField(blank=True, null=True)
#     date_finalized = models.DateTimeField(blank=True, null=True)
#     barcode = models.CharField(max_length=50, blank=True, null=True)
#     external_barcode = models.CharField(max_length=50, blank=True, null=True)
#     external_uid = models.CharField(max_length=50, blank=True, null=True)
#     integrity_check = models.TextField(blank=True, null=True)
#     security_level_uid = models.ForeignKey(
#         'SecurityLevel', models.DO_NOTHING, db_column='security_level_uid', blank=True, null=True)
#     date_last_modified = models.DateTimeField(blank=True, null=True)
#     date_last_modified_of_contents = models.DateTimeField(
#         blank=True, null=True)
#     client_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='client_uid', blank=True, null=True)
#     date_closed = models.DateTimeField(blank=True, null=True)
#     next_enclosure_number = models.IntegerField()
#     enclosure_number_increment = models.IntegerField()
#     uncompressed_record_number = models.CharField(
#         max_length=100, blank=True, null=True)
#     security_based_on_container = models.SmallIntegerField(
#         blank=True, null=True)
#     bypass_referenced_acls = models.SmallIntegerField(blank=True, null=True)
#     opened_temporarily = models.SmallIntegerField(blank=True, null=True)
#     date_created = models.DateTimeField(blank=True, null=True)
#     author = models.CharField(max_length=255, blank=True, null=True)
#     batch_id = models.CharField(max_length=255, blank=True, null=True)
#     date_archived = models.DateTimeField(blank=True, null=True)
#     date_made_inactive = models.DateTimeField(blank=True, null=True)
#     date_of_last_enclosure = models.DateTimeField(blank=True, null=True)
#     date_enclosed = models.DateTimeField(blank=True, null=True)
#     record_class = models.IntegerField()
#     container_record_number = models.CharField(
#         max_length=50, blank=True, null=True)
#     classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     secondary_classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     tertiary_classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     assignee_name = models.CharField(max_length=255, blank=True, null=True)
#     home_name = models.CharField(max_length=255, blank=True, null=True)
#     owner_name = models.CharField(max_length=255, blank=True, null=True)
#     retention_schedule_number = models.CharField(
#         max_length=100, blank=True, null=True)
#     security_level_number = models.SmallIntegerField(blank=True, null=True)
#     client_name = models.CharField(max_length=255, blank=True, null=True)
#     is_container_removed_on_ret_trig = models.SmallIntegerField(
#         blank=True, null=True)
#     is_set_home_on_container_ret_trig = models.SmallIntegerField(
#         blank=True, null=True)
#     retention_schedule_new_home = models.CharField(
#         max_length=32, blank=True, null=True)
#     is_misfiled = models.SmallIntegerField(blank=True, null=True)
#     master_uid = models.CharField(max_length=65, blank=True, null=True)
#     hybrid_remarks = models.TextField(blank=True, null=True)
#     date_last_modified_of_security_level = models.DateTimeField(
#         blank=True, null=True)
#     is_declassify = models.SmallIntegerField(blank=True, null=True)
#     is_imported = models.SmallIntegerField(blank=True, null=True)
#     enforce_single_creation_in_a_workflow = models.SmallIntegerField()
#     check_in_as_new_version = models.SmallIntegerField()
#     check_in_as_override_previous_content = models.SmallIntegerField()
#     is_declassify_alias = models.TextField(blank=True, null=True)
#     is_auto_update_security_level = models.SmallIntegerField()
#     is_auto_update_security_level_on_particular_date = models.SmallIntegerField()
#     security_level_trigger_date = models.DateTimeField(blank=True, null=True)
#     is_update_security_level_on_triggered_event = models.SmallIntegerField()
#     security_level_triggered_event = models.IntegerField(blank=True, null=True)
#     security_level_triggered_event_type = models.IntegerField(
#         blank=True, null=True)
#     security_level_triggered_event_duration = models.IntegerField(
#         blank=True, null=True)
#     security_level_triggered_event_property = models.CharField(
#         max_length=32, blank=True, null=True)
#     auto_update_security_level_id = models.CharField(
#         max_length=32, blank=True, null=True)
#     f2c1c29f2bd94c03ada72e22647cea82 = models.CharField(
#         max_length=255, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'nodetype_ecbfc51142d84ef68c62847b60924f7a'


# class NodetypeF0000000000000000000000000000000(models.Model):
#     uid = models.CharField(primary_key=True, max_length=65)
#     acl_uid = models.ForeignKey(
#         Acl, models.DO_NOTHING, db_column='acl_uid', blank=True, null=True)
#     owner_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='owner_uid', blank=True, null=True)
#     classification_uid = models.ForeignKey(
#         Classification, models.DO_NOTHING, db_column='classification_uid', blank=True, null=True)
#     record_number = models.CharField(max_length=50, blank=True, null=True)
#     retention_schedule_uid = models.ForeignKey(
#         'RetentionSchedule', models.DO_NOTHING, db_column='retention_schedule_uid', blank=True, null=True)
#     disposition_status = models.IntegerField(blank=True, null=True)
#     title = models.CharField(max_length=255, blank=True, null=True)
#     combined_title = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     date_registered = models.DateTimeField(blank=True, null=True)
#     creator_name = models.CharField(max_length=255, blank=True, null=True)
#     creator_username = models.CharField(max_length=255, blank=True, null=True)
#     date_of_last_enclosure = models.DateTimeField(blank=True, null=True)
#     date_enclosed = models.DateTimeField(blank=True, null=True)
#     notes = models.TextField(blank=True, null=True)
#     home_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='home_uid', blank=True, null=True)
#     assignee_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='assignee_uid', blank=True, null=True)
#     is_finalized = models.SmallIntegerField(blank=True, null=True)
#     is_hybrid = models.SmallIntegerField(blank=True, null=True)
#     hybrid_remarks = models.TextField(blank=True, null=True)
#     date_last_modified_of_security_level = models.DateTimeField(
#         blank=True, null=True)
#     date_finalized = models.DateTimeField(blank=True, null=True)
#     barcode = models.CharField(max_length=50, blank=True, null=True)
#     external_barcode = models.CharField(max_length=50, blank=True, null=True)
#     external_uid = models.CharField(max_length=50, blank=True, null=True)
#     integrity_check = models.TextField(blank=True, null=True)
#     security_level_uid = models.ForeignKey(
#         'SecurityLevel', models.DO_NOTHING, db_column='security_level_uid', blank=True, null=True)
#     date_last_modified = models.DateTimeField(blank=True, null=True)
#     date_last_modified_of_contents = models.DateTimeField(
#         blank=True, null=True)
#     client_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='client_uid', blank=True, null=True)
#     date_closed = models.DateTimeField(blank=True, null=True)
#     next_enclosure_number = models.IntegerField()
#     enclosure_number_increment = models.IntegerField()
#     uncompressed_record_number = models.CharField(
#         max_length=50, blank=True, null=True)
#     security_based_on_container = models.SmallIntegerField(
#         blank=True, null=True)
#     bypass_referenced_acls = models.SmallIntegerField(blank=True, null=True)
#     opened_temporarily = models.SmallIntegerField(blank=True, null=True)
#     date_created = models.DateTimeField(blank=True, null=True)
#     author = models.CharField(max_length=255, blank=True, null=True)
#     date_archived = models.DateTimeField(blank=True, null=True)
#     date_made_inactive = models.DateTimeField(blank=True, null=True)
#     record_class = models.IntegerField()
#     container_record_number = models.CharField(
#         max_length=50, blank=True, null=True)
#     classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     assignee_name = models.CharField(max_length=255, blank=True, null=True)
#     home_name = models.CharField(max_length=255, blank=True, null=True)
#     owner_name = models.CharField(max_length=255, blank=True, null=True)
#     retention_schedule_number = models.CharField(
#         max_length=100, blank=True, null=True)
#     security_level_number = models.SmallIntegerField(blank=True, null=True)
#     client_name = models.CharField(max_length=255, blank=True, null=True)
#     batch_id = models.CharField(max_length=255, blank=True, null=True)
#     secondary_classification_uid = models.CharField(
#         max_length=32, blank=True, null=True)
#     tertiary_classification_uid = models.CharField(
#         max_length=32, blank=True, null=True)
#     secondary_classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     tertiary_classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     is_container_removed_on_ret_trig = models.SmallIntegerField(
#         blank=True, null=True)
#     is_set_home_on_container_ret_trig = models.SmallIntegerField(
#         blank=True, null=True)
#     retention_schedule_new_home = models.CharField(
#         max_length=32, blank=True, null=True)
#     hold_uid = models.ForeignKey(
#         Hold, models.DO_NOTHING, db_column='hold_uid', blank=True, null=True)
#     is_misfiled = models.SmallIntegerField(blank=True, null=True)
#     is_declassify = models.SmallIntegerField(blank=True, null=True)
#     is_auto_update_security_level = models.SmallIntegerField()
#     is_auto_update_security_level_on_particular_date = models.SmallIntegerField()
#     security_level_trigger_date = models.DateTimeField(blank=True, null=True)
#     is_update_security_level_on_triggered_event = models.SmallIntegerField()
#     security_level_triggered_event = models.IntegerField(blank=True, null=True)
#     security_level_triggered_event_type = models.IntegerField(
#         blank=True, null=True)
#     security_level_triggered_event_duration = models.IntegerField(
#         blank=True, null=True)
#     security_level_triggered_event_property = models.CharField(
#         max_length=32, blank=True, null=True)
#     auto_update_security_level_id = models.CharField(
#         max_length=32, blank=True, null=True)
#     enforce_single_creation_in_a_workflow = models.SmallIntegerField()
#     check_in_as_new_version = models.SmallIntegerField()
#     check_in_as_override_previous_content = models.SmallIntegerField()
#     is_declassify_alias = models.TextField(blank=True, null=True)
#     is_imported = models.SmallIntegerField(blank=True, null=True)
#     a0000000000000000000000000000000 = models.CharField(
#         max_length=65, blank=True, null=True)
#     master_uid = models.CharField(max_length=65, blank=True, null=True)
#     a0000000000000000000000000000013 = models.CharField(
#         max_length=65, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'nodetype_f0000000000000000000000000000000'


# class NodetypeF0000000000000000000000000000001(models.Model):
#     uid = models.CharField(primary_key=True, max_length=65)
#     acl_uid = models.ForeignKey(
#         Acl, models.DO_NOTHING, db_column='acl_uid', blank=True, null=True)
#     owner_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='owner_uid', blank=True, null=True)
#     classification_uid = models.ForeignKey(
#         Classification, models.DO_NOTHING, db_column='classification_uid', blank=True, null=True)
#     record_number = models.CharField(max_length=50, blank=True, null=True)
#     retention_schedule_uid = models.ForeignKey(
#         'RetentionSchedule', models.DO_NOTHING, db_column='retention_schedule_uid', blank=True, null=True)
#     disposition_status = models.IntegerField(blank=True, null=True)
#     title = models.CharField(max_length=255, blank=True, null=True)
#     combined_title = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     date_registered = models.DateTimeField(blank=True, null=True)
#     creator_name = models.CharField(max_length=255, blank=True, null=True)
#     creator_username = models.CharField(max_length=255, blank=True, null=True)
#     date_of_last_enclosure = models.DateTimeField(blank=True, null=True)
#     date_enclosed = models.DateTimeField(blank=True, null=True)
#     notes = models.TextField(blank=True, null=True)
#     home_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='home_uid', blank=True, null=True)
#     assignee_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='assignee_uid', blank=True, null=True)
#     is_finalized = models.SmallIntegerField(blank=True, null=True)
#     is_hybrid = models.SmallIntegerField(blank=True, null=True)
#     hybrid_remarks = models.TextField(blank=True, null=True)
#     date_last_modified_of_security_level = models.DateTimeField(
#         blank=True, null=True)
#     date_finalized = models.DateTimeField(blank=True, null=True)
#     barcode = models.CharField(max_length=50, blank=True, null=True)
#     external_barcode = models.CharField(max_length=50, blank=True, null=True)
#     external_uid = models.CharField(max_length=50, blank=True, null=True)
#     integrity_check = models.TextField(blank=True, null=True)
#     security_level_uid = models.ForeignKey(
#         'SecurityLevel', models.DO_NOTHING, db_column='security_level_uid', blank=True, null=True)
#     date_last_modified = models.DateTimeField(blank=True, null=True)
#     date_last_modified_of_contents = models.DateTimeField(
#         blank=True, null=True)
#     client_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='client_uid', blank=True, null=True)
#     date_closed = models.DateTimeField(blank=True, null=True)
#     next_enclosure_number = models.IntegerField()
#     enclosure_number_increment = models.IntegerField()
#     uncompressed_record_number = models.CharField(
#         max_length=50, blank=True, null=True)
#     security_based_on_container = models.SmallIntegerField(
#         blank=True, null=True)
#     bypass_referenced_acls = models.SmallIntegerField(blank=True, null=True)
#     opened_temporarily = models.SmallIntegerField(blank=True, null=True)
#     date_created = models.DateTimeField(blank=True, null=True)
#     author = models.CharField(max_length=255, blank=True, null=True)
#     date_archived = models.DateTimeField(blank=True, null=True)
#     date_made_inactive = models.DateTimeField(blank=True, null=True)
#     record_class = models.IntegerField()
#     container_record_number = models.CharField(
#         max_length=50, blank=True, null=True)
#     classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     assignee_name = models.CharField(max_length=255, blank=True, null=True)
#     home_name = models.CharField(max_length=255, blank=True, null=True)
#     owner_name = models.CharField(max_length=255, blank=True, null=True)
#     retention_schedule_number = models.CharField(
#         max_length=100, blank=True, null=True)
#     security_level_number = models.SmallIntegerField(blank=True, null=True)
#     client_name = models.CharField(max_length=255, blank=True, null=True)
#     batch_id = models.CharField(max_length=255, blank=True, null=True)
#     secondary_classification_uid = models.CharField(
#         max_length=32, blank=True, null=True)
#     tertiary_classification_uid = models.CharField(
#         max_length=32, blank=True, null=True)
#     secondary_classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     tertiary_classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     is_container_removed_on_ret_trig = models.SmallIntegerField(
#         blank=True, null=True)
#     is_set_home_on_container_ret_trig = models.SmallIntegerField(
#         blank=True, null=True)
#     retention_schedule_new_home = models.CharField(
#         max_length=32, blank=True, null=True)
#     hold_uid = models.ForeignKey(
#         Hold, models.DO_NOTHING, db_column='hold_uid', blank=True, null=True)
#     is_misfiled = models.SmallIntegerField(blank=True, null=True)
#     is_declassify = models.SmallIntegerField(blank=True, null=True)
#     is_auto_update_security_level = models.SmallIntegerField()
#     is_auto_update_security_level_on_particular_date = models.SmallIntegerField()
#     security_level_trigger_date = models.DateTimeField(blank=True, null=True)
#     is_update_security_level_on_triggered_event = models.SmallIntegerField()
#     security_level_triggered_event = models.IntegerField(blank=True, null=True)
#     security_level_triggered_event_type = models.IntegerField(
#         blank=True, null=True)
#     security_level_triggered_event_duration = models.IntegerField(
#         blank=True, null=True)
#     security_level_triggered_event_property = models.CharField(
#         max_length=32, blank=True, null=True)
#     auto_update_security_level_id = models.CharField(
#         max_length=32, blank=True, null=True)
#     enforce_single_creation_in_a_workflow = models.SmallIntegerField()
#     check_in_as_new_version = models.SmallIntegerField()
#     check_in_as_override_previous_content = models.SmallIntegerField()
#     is_declassify_alias = models.TextField(blank=True, null=True)
#     is_imported = models.SmallIntegerField(blank=True, null=True)
#     a0000000000000000000000000000001 = models.BinaryField(
#         blank=True, null=True)
#     master_uid = models.CharField(max_length=65, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'nodetype_f0000000000000000000000000000001'


# class NodetypeF0000000000000000000000000000002(models.Model):
#     uid = models.CharField(primary_key=True, max_length=65)
#     acl_uid = models.ForeignKey(
#         Acl, models.DO_NOTHING, db_column='acl_uid', blank=True, null=True)
#     owner_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='owner_uid', blank=True, null=True)
#     classification_uid = models.ForeignKey(
#         Classification, models.DO_NOTHING, db_column='classification_uid', blank=True, null=True)
#     record_number = models.CharField(max_length=50, blank=True, null=True)
#     retention_schedule_uid = models.ForeignKey(
#         'RetentionSchedule', models.DO_NOTHING, db_column='retention_schedule_uid', blank=True, null=True)
#     disposition_status = models.IntegerField(blank=True, null=True)
#     title = models.CharField(max_length=255, blank=True, null=True)
#     combined_title = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     date_registered = models.DateTimeField(blank=True, null=True)
#     creator_name = models.CharField(max_length=255, blank=True, null=True)
#     creator_username = models.CharField(max_length=255, blank=True, null=True)
#     date_of_last_enclosure = models.DateTimeField(blank=True, null=True)
#     date_enclosed = models.DateTimeField(blank=True, null=True)
#     notes = models.TextField(blank=True, null=True)
#     home_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='home_uid', blank=True, null=True)
#     assignee_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='assignee_uid', blank=True, null=True)
#     is_finalized = models.SmallIntegerField(blank=True, null=True)
#     is_hybrid = models.SmallIntegerField(blank=True, null=True)
#     hybrid_remarks = models.TextField(blank=True, null=True)
#     date_last_modified_of_security_level = models.DateTimeField(
#         blank=True, null=True)
#     date_finalized = models.DateTimeField(blank=True, null=True)
#     barcode = models.CharField(max_length=50, blank=True, null=True)
#     external_barcode = models.CharField(max_length=50, blank=True, null=True)
#     external_uid = models.CharField(max_length=50, blank=True, null=True)
#     integrity_check = models.TextField(blank=True, null=True)
#     security_level_uid = models.ForeignKey(
#         'SecurityLevel', models.DO_NOTHING, db_column='security_level_uid', blank=True, null=True)
#     date_last_modified = models.DateTimeField(blank=True, null=True)
#     date_last_modified_of_contents = models.DateTimeField(
#         blank=True, null=True)
#     client_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='client_uid', blank=True, null=True)
#     date_closed = models.DateTimeField(blank=True, null=True)
#     next_enclosure_number = models.IntegerField()
#     enclosure_number_increment = models.IntegerField()
#     uncompressed_record_number = models.CharField(
#         max_length=50, blank=True, null=True)
#     security_based_on_container = models.SmallIntegerField(
#         blank=True, null=True)
#     bypass_referenced_acls = models.SmallIntegerField(blank=True, null=True)
#     opened_temporarily = models.SmallIntegerField(blank=True, null=True)
#     date_created = models.DateTimeField(blank=True, null=True)
#     author = models.CharField(max_length=255, blank=True, null=True)
#     date_archived = models.DateTimeField(blank=True, null=True)
#     date_made_inactive = models.DateTimeField(blank=True, null=True)
#     record_class = models.IntegerField()
#     container_record_number = models.CharField(
#         max_length=50, blank=True, null=True)
#     classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     assignee_name = models.CharField(max_length=255, blank=True, null=True)
#     home_name = models.CharField(max_length=255, blank=True, null=True)
#     owner_name = models.CharField(max_length=255, blank=True, null=True)
#     retention_schedule_number = models.CharField(
#         max_length=100, blank=True, null=True)
#     security_level_number = models.SmallIntegerField(blank=True, null=True)
#     client_name = models.CharField(max_length=255, blank=True, null=True)
#     batch_id = models.CharField(max_length=255, blank=True, null=True)
#     secondary_classification_uid = models.CharField(
#         max_length=32, blank=True, null=True)
#     tertiary_classification_uid = models.CharField(
#         max_length=32, blank=True, null=True)
#     secondary_classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     tertiary_classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     is_container_removed_on_ret_trig = models.SmallIntegerField(
#         blank=True, null=True)
#     is_set_home_on_container_ret_trig = models.SmallIntegerField(
#         blank=True, null=True)
#     retention_schedule_new_home = models.CharField(
#         max_length=32, blank=True, null=True)
#     hold_uid = models.ForeignKey(
#         Hold, models.DO_NOTHING, db_column='hold_uid', blank=True, null=True)
#     is_misfiled = models.SmallIntegerField(blank=True, null=True)
#     is_declassify = models.SmallIntegerField(blank=True, null=True)
#     is_auto_update_security_level = models.SmallIntegerField()
#     is_auto_update_security_level_on_particular_date = models.SmallIntegerField()
#     security_level_trigger_date = models.DateTimeField(blank=True, null=True)
#     is_update_security_level_on_triggered_event = models.SmallIntegerField()
#     security_level_triggered_event = models.IntegerField(blank=True, null=True)
#     security_level_triggered_event_type = models.IntegerField(
#         blank=True, null=True)
#     security_level_triggered_event_duration = models.IntegerField(
#         blank=True, null=True)
#     security_level_triggered_event_property = models.CharField(
#         max_length=32, blank=True, null=True)
#     auto_update_security_level_id = models.CharField(
#         max_length=32, blank=True, null=True)
#     enforce_single_creation_in_a_workflow = models.SmallIntegerField()
#     check_in_as_new_version = models.SmallIntegerField()
#     check_in_as_override_previous_content = models.SmallIntegerField()
#     is_declassify_alias = models.TextField(blank=True, null=True)
#     is_imported = models.SmallIntegerField(blank=True, null=True)
#     a0000000000000000000000000000002 = models.CharField(
#         max_length=255, blank=True, null=True)
#     a0000000000000000000000000000003 = models.CharField(
#         max_length=255, blank=True, null=True)
#     a0000000000000000000000000000004 = models.TextField(blank=True, null=True)
#     a0000000000000000000000000000005 = models.TextField(blank=True, null=True)
#     a0000000000000000000000000000006 = models.TextField(blank=True, null=True)
#     a0000000000000000000000000000007 = models.CharField(
#         max_length=255, blank=True, null=True)
#     a0000000000000000000000000000009 = models.DateTimeField(
#         blank=True, null=True)
#     a0000000000000000000000000000010 = models.DateTimeField(
#         blank=True, null=True)
#     master_uid = models.CharField(max_length=65, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'nodetype_f0000000000000000000000000000002'


# class NodetypeF0000000000000000000000000000003(models.Model):
#     uid = models.CharField(primary_key=True, max_length=65)
#     acl_uid = models.ForeignKey(
#         Acl, models.DO_NOTHING, db_column='acl_uid', blank=True, null=True)
#     owner_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='owner_uid', blank=True, null=True)
#     classification_uid = models.ForeignKey(
#         Classification, models.DO_NOTHING, db_column='classification_uid', blank=True, null=True)
#     record_number = models.CharField(max_length=50, blank=True, null=True)
#     retention_schedule_uid = models.ForeignKey(
#         'RetentionSchedule', models.DO_NOTHING, db_column='retention_schedule_uid', blank=True, null=True)
#     disposition_status = models.IntegerField(blank=True, null=True)
#     title = models.CharField(max_length=255, blank=True, null=True)
#     combined_title = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     date_registered = models.DateTimeField(blank=True, null=True)
#     creator_name = models.CharField(max_length=255, blank=True, null=True)
#     creator_username = models.CharField(max_length=255, blank=True, null=True)
#     date_of_last_enclosure = models.DateTimeField(blank=True, null=True)
#     date_enclosed = models.DateTimeField(blank=True, null=True)
#     notes = models.TextField(blank=True, null=True)
#     home_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='home_uid', blank=True, null=True)
#     assignee_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='assignee_uid', blank=True, null=True)
#     is_finalized = models.SmallIntegerField(blank=True, null=True)
#     is_hybrid = models.SmallIntegerField(blank=True, null=True)
#     hybrid_remarks = models.TextField(blank=True, null=True)
#     date_last_modified_of_security_level = models.DateTimeField(
#         blank=True, null=True)
#     date_finalized = models.DateTimeField(blank=True, null=True)
#     barcode = models.CharField(max_length=50, blank=True, null=True)
#     external_barcode = models.CharField(max_length=50, blank=True, null=True)
#     external_uid = models.CharField(max_length=50, blank=True, null=True)
#     integrity_check = models.TextField(blank=True, null=True)
#     security_level_uid = models.ForeignKey(
#         'SecurityLevel', models.DO_NOTHING, db_column='security_level_uid', blank=True, null=True)
#     date_last_modified = models.DateTimeField(blank=True, null=True)
#     date_last_modified_of_contents = models.DateTimeField(
#         blank=True, null=True)
#     client_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='client_uid', blank=True, null=True)
#     date_closed = models.DateTimeField(blank=True, null=True)
#     next_enclosure_number = models.IntegerField()
#     enclosure_number_increment = models.IntegerField()
#     uncompressed_record_number = models.CharField(
#         max_length=50, blank=True, null=True)
#     security_based_on_container = models.SmallIntegerField(
#         blank=True, null=True)
#     bypass_referenced_acls = models.SmallIntegerField(blank=True, null=True)
#     opened_temporarily = models.SmallIntegerField(blank=True, null=True)
#     date_created = models.DateTimeField(blank=True, null=True)
#     author = models.CharField(max_length=255, blank=True, null=True)
#     date_archived = models.DateTimeField(blank=True, null=True)
#     date_made_inactive = models.DateTimeField(blank=True, null=True)
#     record_class = models.IntegerField()
#     container_record_number = models.CharField(
#         max_length=50, blank=True, null=True)
#     classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     assignee_name = models.CharField(max_length=255, blank=True, null=True)
#     home_name = models.CharField(max_length=255, blank=True, null=True)
#     owner_name = models.CharField(max_length=255, blank=True, null=True)
#     retention_schedule_number = models.CharField(
#         max_length=100, blank=True, null=True)
#     security_level_number = models.SmallIntegerField(blank=True, null=True)
#     client_name = models.CharField(max_length=255, blank=True, null=True)
#     batch_id = models.CharField(max_length=255, blank=True, null=True)
#     secondary_classification_uid = models.CharField(
#         max_length=32, blank=True, null=True)
#     tertiary_classification_uid = models.CharField(
#         max_length=32, blank=True, null=True)
#     secondary_classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     tertiary_classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     is_container_removed_on_ret_trig = models.SmallIntegerField(
#         blank=True, null=True)
#     is_set_home_on_container_ret_trig = models.SmallIntegerField(
#         blank=True, null=True)
#     retention_schedule_new_home = models.CharField(
#         max_length=32, blank=True, null=True)
#     hold_uid = models.ForeignKey(
#         Hold, models.DO_NOTHING, db_column='hold_uid', blank=True, null=True)
#     is_misfiled = models.SmallIntegerField(blank=True, null=True)
#     is_declassify = models.SmallIntegerField(blank=True, null=True)
#     is_auto_update_security_level = models.SmallIntegerField()
#     is_auto_update_security_level_on_particular_date = models.SmallIntegerField()
#     security_level_trigger_date = models.DateTimeField(blank=True, null=True)
#     is_update_security_level_on_triggered_event = models.SmallIntegerField()
#     security_level_triggered_event = models.IntegerField(blank=True, null=True)
#     security_level_triggered_event_type = models.IntegerField(
#         blank=True, null=True)
#     security_level_triggered_event_duration = models.IntegerField(
#         blank=True, null=True)
#     security_level_triggered_event_property = models.CharField(
#         max_length=32, blank=True, null=True)
#     auto_update_security_level_id = models.CharField(
#         max_length=32, blank=True, null=True)
#     enforce_single_creation_in_a_workflow = models.SmallIntegerField()
#     check_in_as_new_version = models.SmallIntegerField()
#     check_in_as_override_previous_content = models.SmallIntegerField()
#     is_declassify_alias = models.TextField(blank=True, null=True)
#     is_imported = models.SmallIntegerField(blank=True, null=True)
#     a0000000000000000000000000000008 = models.CharField(
#         max_length=100, blank=True, null=True)
#     master_uid = models.CharField(max_length=65, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'nodetype_f0000000000000000000000000000003'


# class NodetypeF0000000000000000000000000000004(models.Model):
#     uid = models.CharField(primary_key=True, max_length=65)
#     acl_uid = models.ForeignKey(
#         Acl, models.DO_NOTHING, db_column='acl_uid', blank=True, null=True)
#     owner_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='owner_uid', blank=True, null=True)
#     classification_uid = models.ForeignKey(
#         Classification, models.DO_NOTHING, db_column='classification_uid', blank=True, null=True)
#     record_number = models.CharField(max_length=50, blank=True, null=True)
#     retention_schedule_uid = models.ForeignKey(
#         'RetentionSchedule', models.DO_NOTHING, db_column='retention_schedule_uid', blank=True, null=True)
#     disposition_status = models.IntegerField(blank=True, null=True)
#     title = models.CharField(max_length=255, blank=True, null=True)
#     combined_title = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     date_registered = models.DateTimeField(blank=True, null=True)
#     creator_name = models.CharField(max_length=255, blank=True, null=True)
#     creator_username = models.CharField(max_length=255, blank=True, null=True)
#     date_of_last_enclosure = models.DateTimeField(blank=True, null=True)
#     date_enclosed = models.DateTimeField(blank=True, null=True)
#     notes = models.TextField(blank=True, null=True)
#     home_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='home_uid', blank=True, null=True)
#     assignee_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='assignee_uid', blank=True, null=True)
#     is_finalized = models.SmallIntegerField(blank=True, null=True)
#     is_hybrid = models.SmallIntegerField(blank=True, null=True)
#     hybrid_remarks = models.TextField(blank=True, null=True)
#     date_last_modified_of_security_level = models.DateTimeField(
#         blank=True, null=True)
#     date_finalized = models.DateTimeField(blank=True, null=True)
#     barcode = models.CharField(max_length=50, blank=True, null=True)
#     external_barcode = models.CharField(max_length=50, blank=True, null=True)
#     external_uid = models.CharField(max_length=50, blank=True, null=True)
#     integrity_check = models.TextField(blank=True, null=True)
#     security_level_uid = models.ForeignKey(
#         'SecurityLevel', models.DO_NOTHING, db_column='security_level_uid', blank=True, null=True)
#     date_last_modified = models.DateTimeField(blank=True, null=True)
#     date_last_modified_of_contents = models.DateTimeField(
#         blank=True, null=True)
#     client_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='client_uid', blank=True, null=True)
#     date_closed = models.DateTimeField(blank=True, null=True)
#     next_enclosure_number = models.IntegerField()
#     enclosure_number_increment = models.IntegerField()
#     uncompressed_record_number = models.CharField(
#         max_length=50, blank=True, null=True)
#     security_based_on_container = models.SmallIntegerField(
#         blank=True, null=True)
#     bypass_referenced_acls = models.SmallIntegerField(blank=True, null=True)
#     opened_temporarily = models.SmallIntegerField(blank=True, null=True)
#     date_created = models.DateTimeField(blank=True, null=True)
#     author = models.CharField(max_length=255, blank=True, null=True)
#     date_archived = models.DateTimeField(blank=True, null=True)
#     date_made_inactive = models.DateTimeField(blank=True, null=True)
#     record_class = models.IntegerField()
#     container_record_number = models.CharField(
#         max_length=50, blank=True, null=True)
#     classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     assignee_name = models.CharField(max_length=255, blank=True, null=True)
#     home_name = models.CharField(max_length=255, blank=True, null=True)
#     owner_name = models.CharField(max_length=255, blank=True, null=True)
#     retention_schedule_number = models.CharField(
#         max_length=100, blank=True, null=True)
#     security_level_number = models.SmallIntegerField(blank=True, null=True)
#     client_name = models.CharField(max_length=255, blank=True, null=True)
#     batch_id = models.CharField(max_length=255, blank=True, null=True)
#     secondary_classification_uid = models.CharField(
#         max_length=32, blank=True, null=True)
#     tertiary_classification_uid = models.CharField(
#         max_length=32, blank=True, null=True)
#     secondary_classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     tertiary_classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     is_container_removed_on_ret_trig = models.SmallIntegerField(
#         blank=True, null=True)
#     is_set_home_on_container_ret_trig = models.SmallIntegerField(
#         blank=True, null=True)
#     retention_schedule_new_home = models.CharField(
#         max_length=32, blank=True, null=True)
#     hold_uid = models.ForeignKey(
#         Hold, models.DO_NOTHING, db_column='hold_uid', blank=True, null=True)
#     is_misfiled = models.SmallIntegerField(blank=True, null=True)
#     is_declassify = models.SmallIntegerField(blank=True, null=True)
#     is_auto_update_security_level = models.SmallIntegerField()
#     is_auto_update_security_level_on_particular_date = models.SmallIntegerField()
#     security_level_trigger_date = models.DateTimeField(blank=True, null=True)
#     is_update_security_level_on_triggered_event = models.SmallIntegerField()
#     security_level_triggered_event = models.IntegerField(blank=True, null=True)
#     security_level_triggered_event_type = models.IntegerField(
#         blank=True, null=True)
#     security_level_triggered_event_duration = models.IntegerField(
#         blank=True, null=True)
#     security_level_triggered_event_property = models.CharField(
#         max_length=32, blank=True, null=True)
#     auto_update_security_level_id = models.CharField(
#         max_length=32, blank=True, null=True)
#     enforce_single_creation_in_a_workflow = models.SmallIntegerField()
#     check_in_as_new_version = models.SmallIntegerField()
#     check_in_as_override_previous_content = models.SmallIntegerField()
#     is_declassify_alias = models.TextField(blank=True, null=True)
#     is_imported = models.SmallIntegerField(blank=True, null=True)
#     master_uid = models.CharField(max_length=65, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'nodetype_f0000000000000000000000000000004'


# class NodetypeF0000000000000000000000000000005(models.Model):
#     uid = models.CharField(primary_key=True, max_length=65)
#     acl_uid = models.ForeignKey(
#         Acl, models.DO_NOTHING, db_column='acl_uid', blank=True, null=True)
#     owner_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='owner_uid', blank=True, null=True)
#     classification_uid = models.ForeignKey(
#         Classification, models.DO_NOTHING, db_column='classification_uid', blank=True, null=True)
#     record_number = models.CharField(max_length=50, blank=True, null=True)
#     retention_schedule_uid = models.ForeignKey(
#         'RetentionSchedule', models.DO_NOTHING, db_column='retention_schedule_uid', blank=True, null=True)
#     disposition_status = models.IntegerField(blank=True, null=True)
#     title = models.CharField(max_length=255, blank=True, null=True)
#     combined_title = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     date_registered = models.DateTimeField(blank=True, null=True)
#     creator_name = models.CharField(max_length=255, blank=True, null=True)
#     creator_username = models.CharField(max_length=255, blank=True, null=True)
#     date_of_last_enclosure = models.DateTimeField(blank=True, null=True)
#     date_enclosed = models.DateTimeField(blank=True, null=True)
#     notes = models.TextField(blank=True, null=True)
#     home_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='home_uid', blank=True, null=True)
#     assignee_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='assignee_uid', blank=True, null=True)
#     is_finalized = models.SmallIntegerField(blank=True, null=True)
#     is_hybrid = models.SmallIntegerField(blank=True, null=True)
#     hybrid_remarks = models.TextField(blank=True, null=True)
#     date_last_modified_of_security_level = models.DateTimeField(
#         blank=True, null=True)
#     date_finalized = models.DateTimeField(blank=True, null=True)
#     barcode = models.CharField(max_length=50, blank=True, null=True)
#     external_barcode = models.CharField(max_length=50, blank=True, null=True)
#     external_uid = models.CharField(max_length=50, blank=True, null=True)
#     integrity_check = models.TextField(blank=True, null=True)
#     security_level_uid = models.ForeignKey(
#         'SecurityLevel', models.DO_NOTHING, db_column='security_level_uid', blank=True, null=True)
#     date_last_modified = models.DateTimeField(blank=True, null=True)
#     date_last_modified_of_contents = models.DateTimeField(
#         blank=True, null=True)
#     client_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='client_uid', blank=True, null=True)
#     date_closed = models.DateTimeField(blank=True, null=True)
#     next_enclosure_number = models.IntegerField()
#     enclosure_number_increment = models.IntegerField()
#     uncompressed_record_number = models.CharField(
#         max_length=50, blank=True, null=True)
#     security_based_on_container = models.SmallIntegerField(
#         blank=True, null=True)
#     bypass_referenced_acls = models.SmallIntegerField(blank=True, null=True)
#     opened_temporarily = models.SmallIntegerField(blank=True, null=True)
#     date_created = models.DateTimeField(blank=True, null=True)
#     author = models.CharField(max_length=255, blank=True, null=True)
#     date_archived = models.DateTimeField(blank=True, null=True)
#     date_made_inactive = models.DateTimeField(blank=True, null=True)
#     record_class = models.IntegerField()
#     container_record_number = models.CharField(
#         max_length=50, blank=True, null=True)
#     classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     assignee_name = models.CharField(max_length=255, blank=True, null=True)
#     home_name = models.CharField(max_length=255, blank=True, null=True)
#     owner_name = models.CharField(max_length=255, blank=True, null=True)
#     retention_schedule_number = models.CharField(
#         max_length=100, blank=True, null=True)
#     security_level_number = models.SmallIntegerField(blank=True, null=True)
#     client_name = models.CharField(max_length=255, blank=True, null=True)
#     batch_id = models.CharField(max_length=255, blank=True, null=True)
#     secondary_classification_uid = models.CharField(
#         max_length=32, blank=True, null=True)
#     tertiary_classification_uid = models.CharField(
#         max_length=32, blank=True, null=True)
#     secondary_classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     tertiary_classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     is_container_removed_on_ret_trig = models.SmallIntegerField(
#         blank=True, null=True)
#     is_set_home_on_container_ret_trig = models.SmallIntegerField(
#         blank=True, null=True)
#     retention_schedule_new_home = models.CharField(
#         max_length=32, blank=True, null=True)
#     hold_uid = models.ForeignKey(
#         Hold, models.DO_NOTHING, db_column='hold_uid', blank=True, null=True)
#     is_misfiled = models.SmallIntegerField(blank=True, null=True)
#     is_declassify = models.SmallIntegerField(blank=True, null=True)
#     is_auto_update_security_level = models.SmallIntegerField()
#     is_auto_update_security_level_on_particular_date = models.SmallIntegerField()
#     security_level_trigger_date = models.DateTimeField(blank=True, null=True)
#     is_update_security_level_on_triggered_event = models.SmallIntegerField()
#     security_level_triggered_event = models.IntegerField(blank=True, null=True)
#     security_level_triggered_event_type = models.IntegerField(
#         blank=True, null=True)
#     security_level_triggered_event_duration = models.IntegerField(
#         blank=True, null=True)
#     security_level_triggered_event_property = models.CharField(
#         max_length=32, blank=True, null=True)
#     auto_update_security_level_id = models.CharField(
#         max_length=32, blank=True, null=True)
#     enforce_single_creation_in_a_workflow = models.SmallIntegerField()
#     check_in_as_new_version = models.SmallIntegerField()
#     check_in_as_override_previous_content = models.SmallIntegerField()
#     is_declassify_alias = models.TextField(blank=True, null=True)
#     is_imported = models.SmallIntegerField(blank=True, null=True)
#     a0000000000000000000000000000002 = models.CharField(
#         max_length=255, blank=True, null=True)
#     a0000000000000000000000000000003 = models.CharField(
#         max_length=255, blank=True, null=True)
#     a0000000000000000000000000000004 = models.TextField(blank=True, null=True)
#     a0000000000000000000000000000005 = models.TextField(blank=True, null=True)
#     a0000000000000000000000000000006 = models.TextField(blank=True, null=True)
#     a0000000000000000000000000000007 = models.CharField(
#         max_length=255, blank=True, null=True)
#     a0000000000000000000000000000011 = models.TextField(blank=True, null=True)
#     a0000000000000000000000000000012 = models.CharField(
#         max_length=32, blank=True, null=True)
#     master_uid = models.CharField(max_length=65, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'nodetype_f0000000000000000000000000000005'


# class NodetypeF0000000000000000000000000000006(models.Model):
#     uid = models.CharField(primary_key=True, max_length=65)
#     acl_uid = models.ForeignKey(
#         Acl, models.DO_NOTHING, db_column='acl_uid', blank=True, null=True)
#     owner_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='owner_uid', blank=True, null=True)
#     classification_uid = models.ForeignKey(
#         Classification, models.DO_NOTHING, db_column='classification_uid', blank=True, null=True)
#     record_number = models.CharField(max_length=50, blank=True, null=True)
#     retention_schedule_uid = models.ForeignKey(
#         'RetentionSchedule', models.DO_NOTHING, db_column='retention_schedule_uid', blank=True, null=True)
#     disposition_status = models.IntegerField(blank=True, null=True)
#     title = models.CharField(max_length=255, blank=True, null=True)
#     combined_title = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     date_registered = models.DateTimeField(blank=True, null=True)
#     creator_name = models.CharField(max_length=255, blank=True, null=True)
#     creator_username = models.CharField(max_length=255, blank=True, null=True)
#     date_of_last_enclosure = models.DateTimeField(blank=True, null=True)
#     date_enclosed = models.DateTimeField(blank=True, null=True)
#     notes = models.TextField(blank=True, null=True)
#     home_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='home_uid', blank=True, null=True)
#     assignee_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='assignee_uid', blank=True, null=True)
#     is_finalized = models.SmallIntegerField(blank=True, null=True)
#     is_hybrid = models.SmallIntegerField(blank=True, null=True)
#     hybrid_remarks = models.TextField(blank=True, null=True)
#     date_last_modified_of_security_level = models.DateTimeField(
#         blank=True, null=True)
#     date_finalized = models.DateTimeField(blank=True, null=True)
#     barcode = models.CharField(max_length=50, blank=True, null=True)
#     external_barcode = models.CharField(max_length=50, blank=True, null=True)
#     external_uid = models.CharField(max_length=50, blank=True, null=True)
#     integrity_check = models.TextField(blank=True, null=True)
#     security_level_uid = models.ForeignKey(
#         'SecurityLevel', models.DO_NOTHING, db_column='security_level_uid', blank=True, null=True)
#     date_last_modified = models.DateTimeField(blank=True, null=True)
#     date_last_modified_of_contents = models.DateTimeField(
#         blank=True, null=True)
#     client_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='client_uid', blank=True, null=True)
#     date_closed = models.DateTimeField(blank=True, null=True)
#     next_enclosure_number = models.IntegerField()
#     enclosure_number_increment = models.IntegerField()
#     uncompressed_record_number = models.CharField(
#         max_length=50, blank=True, null=True)
#     security_based_on_container = models.SmallIntegerField(
#         blank=True, null=True)
#     bypass_referenced_acls = models.SmallIntegerField(blank=True, null=True)
#     opened_temporarily = models.SmallIntegerField(blank=True, null=True)
#     date_created = models.DateTimeField(blank=True, null=True)
#     author = models.CharField(max_length=255, blank=True, null=True)
#     date_archived = models.DateTimeField(blank=True, null=True)
#     date_made_inactive = models.DateTimeField(blank=True, null=True)
#     record_class = models.IntegerField()
#     container_record_number = models.CharField(
#         max_length=50, blank=True, null=True)
#     classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     assignee_name = models.CharField(max_length=255, blank=True, null=True)
#     home_name = models.CharField(max_length=255, blank=True, null=True)
#     owner_name = models.CharField(max_length=255, blank=True, null=True)
#     retention_schedule_number = models.CharField(
#         max_length=100, blank=True, null=True)
#     security_level_number = models.SmallIntegerField(blank=True, null=True)
#     client_name = models.CharField(max_length=255, blank=True, null=True)
#     batch_id = models.CharField(max_length=255, blank=True, null=True)
#     secondary_classification_uid = models.CharField(
#         max_length=32, blank=True, null=True)
#     tertiary_classification_uid = models.CharField(
#         max_length=32, blank=True, null=True)
#     secondary_classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     tertiary_classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     is_container_removed_on_ret_trig = models.SmallIntegerField(
#         blank=True, null=True)
#     is_set_home_on_container_ret_trig = models.SmallIntegerField(
#         blank=True, null=True)
#     retention_schedule_new_home = models.CharField(
#         max_length=32, blank=True, null=True)
#     hold_uid = models.ForeignKey(
#         Hold, models.DO_NOTHING, db_column='hold_uid', blank=True, null=True)
#     is_misfiled = models.SmallIntegerField(blank=True, null=True)
#     is_declassify = models.SmallIntegerField(blank=True, null=True)
#     is_auto_update_security_level = models.SmallIntegerField()
#     is_auto_update_security_level_on_particular_date = models.SmallIntegerField()
#     security_level_trigger_date = models.DateTimeField(blank=True, null=True)
#     is_update_security_level_on_triggered_event = models.SmallIntegerField()
#     security_level_triggered_event = models.IntegerField(blank=True, null=True)
#     security_level_triggered_event_type = models.IntegerField(
#         blank=True, null=True)
#     security_level_triggered_event_duration = models.IntegerField(
#         blank=True, null=True)
#     security_level_triggered_event_property = models.CharField(
#         max_length=32, blank=True, null=True)
#     auto_update_security_level_id = models.CharField(
#         max_length=32, blank=True, null=True)
#     enforce_single_creation_in_a_workflow = models.SmallIntegerField()
#     check_in_as_new_version = models.SmallIntegerField()
#     check_in_as_override_previous_content = models.SmallIntegerField()
#     is_declassify_alias = models.TextField(blank=True, null=True)
#     is_imported = models.SmallIntegerField(blank=True, null=True)
#     master_uid = models.CharField(max_length=65, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'nodetype_f0000000000000000000000000000006'


# class NodetypeF0000000000000000000000000000007(models.Model):
#     uid = models.CharField(primary_key=True, max_length=65)
#     acl_uid = models.ForeignKey(
#         Acl, models.DO_NOTHING, db_column='acl_uid', blank=True, null=True)
#     owner_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='owner_uid', blank=True, null=True)
#     classification_uid = models.ForeignKey(
#         Classification, models.DO_NOTHING, db_column='classification_uid', blank=True, null=True)
#     record_number = models.CharField(max_length=50, blank=True, null=True)
#     retention_schedule_uid = models.ForeignKey(
#         'RetentionSchedule', models.DO_NOTHING, db_column='retention_schedule_uid', blank=True, null=True)
#     disposition_status = models.IntegerField(blank=True, null=True)
#     title = models.CharField(max_length=255, blank=True, null=True)
#     combined_title = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     date_registered = models.DateTimeField(blank=True, null=True)
#     creator_name = models.CharField(max_length=255, blank=True, null=True)
#     creator_username = models.CharField(max_length=255, blank=True, null=True)
#     date_of_last_enclosure = models.DateTimeField(blank=True, null=True)
#     date_enclosed = models.DateTimeField(blank=True, null=True)
#     notes = models.TextField(blank=True, null=True)
#     home_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='home_uid', blank=True, null=True)
#     assignee_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='assignee_uid', blank=True, null=True)
#     is_finalized = models.SmallIntegerField(blank=True, null=True)
#     is_hybrid = models.SmallIntegerField(blank=True, null=True)
#     hybrid_remarks = models.TextField(blank=True, null=True)
#     date_last_modified_of_security_level = models.DateTimeField(
#         blank=True, null=True)
#     date_finalized = models.DateTimeField(blank=True, null=True)
#     barcode = models.CharField(max_length=50, blank=True, null=True)
#     external_barcode = models.CharField(max_length=50, blank=True, null=True)
#     external_uid = models.CharField(max_length=50, blank=True, null=True)
#     integrity_check = models.TextField(blank=True, null=True)
#     security_level_uid = models.ForeignKey(
#         'SecurityLevel', models.DO_NOTHING, db_column='security_level_uid', blank=True, null=True)
#     date_last_modified = models.DateTimeField(blank=True, null=True)
#     date_last_modified_of_contents = models.DateTimeField(
#         blank=True, null=True)
#     client_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='client_uid', blank=True, null=True)
#     date_closed = models.DateTimeField(blank=True, null=True)
#     next_enclosure_number = models.IntegerField()
#     enclosure_number_increment = models.IntegerField()
#     uncompressed_record_number = models.CharField(
#         max_length=50, blank=True, null=True)
#     security_based_on_container = models.SmallIntegerField(
#         blank=True, null=True)
#     bypass_referenced_acls = models.SmallIntegerField(blank=True, null=True)
#     opened_temporarily = models.SmallIntegerField(blank=True, null=True)
#     date_created = models.DateTimeField(blank=True, null=True)
#     author = models.CharField(max_length=255, blank=True, null=True)
#     date_archived = models.DateTimeField(blank=True, null=True)
#     date_made_inactive = models.DateTimeField(blank=True, null=True)
#     record_class = models.IntegerField()
#     container_record_number = models.CharField(
#         max_length=50, blank=True, null=True)
#     classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     assignee_name = models.CharField(max_length=255, blank=True, null=True)
#     home_name = models.CharField(max_length=255, blank=True, null=True)
#     owner_name = models.CharField(max_length=255, blank=True, null=True)
#     retention_schedule_number = models.CharField(
#         max_length=100, blank=True, null=True)
#     security_level_number = models.SmallIntegerField(blank=True, null=True)
#     client_name = models.CharField(max_length=255, blank=True, null=True)
#     batch_id = models.CharField(max_length=255, blank=True, null=True)
#     secondary_classification_uid = models.CharField(
#         max_length=32, blank=True, null=True)
#     tertiary_classification_uid = models.CharField(
#         max_length=32, blank=True, null=True)
#     secondary_classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     tertiary_classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     is_container_removed_on_ret_trig = models.SmallIntegerField(
#         blank=True, null=True)
#     is_set_home_on_container_ret_trig = models.SmallIntegerField(
#         blank=True, null=True)
#     retention_schedule_new_home = models.CharField(
#         max_length=32, blank=True, null=True)
#     hold_uid = models.ForeignKey(
#         Hold, models.DO_NOTHING, db_column='hold_uid', blank=True, null=True)
#     is_misfiled = models.SmallIntegerField(blank=True, null=True)
#     is_declassify = models.SmallIntegerField(blank=True, null=True)
#     is_auto_update_security_level = models.SmallIntegerField()
#     is_auto_update_security_level_on_particular_date = models.SmallIntegerField()
#     security_level_trigger_date = models.DateTimeField(blank=True, null=True)
#     is_update_security_level_on_triggered_event = models.SmallIntegerField()
#     security_level_triggered_event = models.IntegerField(blank=True, null=True)
#     security_level_triggered_event_type = models.IntegerField(
#         blank=True, null=True)
#     security_level_triggered_event_duration = models.IntegerField(
#         blank=True, null=True)
#     security_level_triggered_event_property = models.CharField(
#         max_length=32, blank=True, null=True)
#     auto_update_security_level_id = models.CharField(
#         max_length=32, blank=True, null=True)
#     enforce_single_creation_in_a_workflow = models.SmallIntegerField()
#     check_in_as_new_version = models.SmallIntegerField()
#     check_in_as_override_previous_content = models.SmallIntegerField()
#     is_declassify_alias = models.TextField(blank=True, null=True)
#     is_imported = models.SmallIntegerField(blank=True, null=True)
#     a0000000000000000000000000000000 = models.CharField(
#         max_length=65, blank=True, null=True)
#     a0000000000000000000000000000014 = models.CharField(
#         max_length=255, blank=True, null=True)
#     a0000000000000000000000000000013 = models.CharField(
#         max_length=65, blank=True, null=True)
#     master_uid = models.CharField(max_length=65, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'nodetype_f0000000000000000000000000000007'


# class NodetypeF1605B990313411Da01Ab6F97945Dccd(models.Model):
#     uid = models.CharField(primary_key=True, max_length=65)
#     acl_uid = models.ForeignKey(
#         Acl, models.DO_NOTHING, db_column='acl_uid', blank=True, null=True)
#     owner_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='owner_uid', blank=True, null=True)
#     classification_uid = models.ForeignKey(
#         Classification, models.DO_NOTHING, db_column='classification_uid', blank=True, null=True)
#     secondary_classification_uid = models.CharField(
#         max_length=32, blank=True, null=True)
#     tertiary_classification_uid = models.CharField(
#         max_length=32, blank=True, null=True)
#     record_number = models.CharField(max_length=100, blank=True, null=True)
#     retention_schedule_uid = models.ForeignKey(
#         'RetentionSchedule', models.DO_NOTHING, db_column='retention_schedule_uid', blank=True, null=True)
#     hold_uid = models.ForeignKey(
#         Hold, models.DO_NOTHING, db_column='hold_uid', blank=True, null=True)
#     disposition_status = models.IntegerField(blank=True, null=True)
#     title = models.CharField(max_length=255, blank=True, null=True)
#     combined_title = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     date_registered = models.DateTimeField(blank=True, null=True)
#     creator_name = models.CharField(max_length=255, blank=True, null=True)
#     creator_username = models.CharField(max_length=255, blank=True, null=True)
#     notes = models.TextField(blank=True, null=True)
#     home_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='home_uid', blank=True, null=True)
#     assignee_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='assignee_uid', blank=True, null=True)
#     is_finalized = models.SmallIntegerField(blank=True, null=True)
#     is_hybrid = models.SmallIntegerField(blank=True, null=True)
#     date_finalized = models.DateTimeField(blank=True, null=True)
#     barcode = models.CharField(max_length=50, blank=True, null=True)
#     external_barcode = models.CharField(max_length=50, blank=True, null=True)
#     external_uid = models.CharField(max_length=50, blank=True, null=True)
#     integrity_check = models.TextField(blank=True, null=True)
#     security_level_uid = models.ForeignKey(
#         'SecurityLevel', models.DO_NOTHING, db_column='security_level_uid', blank=True, null=True)
#     date_last_modified = models.DateTimeField(blank=True, null=True)
#     date_last_modified_of_contents = models.DateTimeField(
#         blank=True, null=True)
#     client_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='client_uid', blank=True, null=True)
#     date_closed = models.DateTimeField(blank=True, null=True)
#     next_enclosure_number = models.IntegerField()
#     enclosure_number_increment = models.IntegerField()
#     uncompressed_record_number = models.CharField(
#         max_length=100, blank=True, null=True)
#     security_based_on_container = models.SmallIntegerField(
#         blank=True, null=True)
#     bypass_referenced_acls = models.SmallIntegerField(blank=True, null=True)
#     opened_temporarily = models.SmallIntegerField(blank=True, null=True)
#     date_created = models.DateTimeField(blank=True, null=True)
#     author = models.CharField(max_length=255, blank=True, null=True)
#     batch_id = models.CharField(max_length=255, blank=True, null=True)
#     date_archived = models.DateTimeField(blank=True, null=True)
#     date_made_inactive = models.DateTimeField(blank=True, null=True)
#     date_of_last_enclosure = models.DateTimeField(blank=True, null=True)
#     date_enclosed = models.DateTimeField(blank=True, null=True)
#     record_class = models.IntegerField()
#     container_record_number = models.CharField(
#         max_length=50, blank=True, null=True)
#     classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     secondary_classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     tertiary_classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     assignee_name = models.CharField(max_length=255, blank=True, null=True)
#     home_name = models.CharField(max_length=255, blank=True, null=True)
#     owner_name = models.CharField(max_length=255, blank=True, null=True)
#     retention_schedule_number = models.CharField(
#         max_length=100, blank=True, null=True)
#     security_level_number = models.SmallIntegerField(blank=True, null=True)
#     client_name = models.CharField(max_length=255, blank=True, null=True)
#     is_container_removed_on_ret_trig = models.SmallIntegerField(
#         blank=True, null=True)
#     is_set_home_on_container_ret_trig = models.SmallIntegerField(
#         blank=True, null=True)
#     retention_schedule_new_home = models.CharField(
#         max_length=32, blank=True, null=True)
#     is_misfiled = models.SmallIntegerField(blank=True, null=True)
#     master_uid = models.CharField(max_length=65, blank=True, null=True)
#     hybrid_remarks = models.TextField(blank=True, null=True)
#     date_last_modified_of_security_level = models.DateTimeField(
#         blank=True, null=True)
#     is_declassify = models.SmallIntegerField(blank=True, null=True)
#     is_imported = models.SmallIntegerField(blank=True, null=True)
#     enforce_single_creation_in_a_workflow = models.SmallIntegerField()
#     check_in_as_new_version = models.SmallIntegerField()
#     check_in_as_override_previous_content = models.SmallIntegerField()
#     is_declassify_alias = models.TextField(blank=True, null=True)
#     is_auto_update_security_level = models.SmallIntegerField()
#     is_auto_update_security_level_on_particular_date = models.SmallIntegerField()
#     security_level_trigger_date = models.DateTimeField(blank=True, null=True)
#     is_update_security_level_on_triggered_event = models.SmallIntegerField()
#     security_level_triggered_event = models.IntegerField(blank=True, null=True)
#     security_level_triggered_event_type = models.IntegerField(
#         blank=True, null=True)
#     security_level_triggered_event_duration = models.IntegerField(
#         blank=True, null=True)
#     security_level_triggered_event_property = models.CharField(
#         max_length=32, blank=True, null=True)
#     auto_update_security_level_id = models.CharField(
#         max_length=32, blank=True, null=True)
#     f9ce8fde98e547699ff79602b2dce34f = models.DateTimeField(
#         blank=True, null=True)
#     ibdaf89d09234fef9826c0f2a81ef088 = models.CharField(
#         max_length=255, blank=True, null=True)
#     i9a97f4ee4f34ba4a645d2b783963bba = models.DecimalField(
#         max_digits=16, decimal_places=2, blank=True, null=True)
#     a4d54a1736fa45e796aa89ff04b83f55 = models.CharField(
#         max_length=255, blank=True, null=True)
#     h7f705c3a23b48a897df194cb6aa373f = models.CharField(
#         max_length=100, blank=True, null=True)
#     j72d25f47afb42ea84fd364233a29430 = models.CharField(
#         max_length=50, blank=True, null=True)
#     c1fb9f1f82af496cbbfd8f387aefab42 = models.CharField(
#         max_length=20, blank=True, null=True)
#     ha41c373c2f0413cb1458bb886048bb2 = models.CharField(
#         max_length=255, blank=True, null=True)
#     f0970f3862f941338e162f34b75e6831 = models.CharField(
#         max_length=20, blank=True, null=True)
#     ba832c949a544def959b33f23ebd6404 = models.CharField(
#         max_length=4, blank=True, null=True)
#     d17a4a24785a4faba79f0a6135ca214c = models.CharField(
#         max_length=255, blank=True, null=True)
#     a9c7182451794f839e10323104d8231f = models.CharField(
#         max_length=255, blank=True, null=True)
#     h3ff7814caaf4664a54a4d0cb2748ea4 = models.CharField(
#         max_length=50, blank=True, null=True)
#     ic51998ca67846f18d5149a399635e39 = models.CharField(
#         max_length=255, blank=True, null=True)
#     ac88f80ecee245b0821768d6493db2c2 = models.DateTimeField(
#         blank=True, null=True)
#     b7aadfe282354bff9f5d437ab9e52511 = models.CharField(
#         max_length=255, blank=True, null=True)
#     f2c1c29f2bd94c03ada72e22647cea82 = models.CharField(
#         max_length=255, blank=True, null=True)
#     afd1329c2de2421bbbe5a48f65b56818 = models.CharField(
#         max_length=255, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'nodetype_f1605b990313411da01ab6f97945dccd'


# class NodetypeF2Bfeb5852264C5Aa67F53F96Ac28D39(models.Model):
#     uid = models.CharField(primary_key=True, max_length=65)
#     acl_uid = models.ForeignKey(
#         Acl, models.DO_NOTHING, db_column='acl_uid', blank=True, null=True)
#     owner_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='owner_uid', blank=True, null=True)
#     classification_uid = models.ForeignKey(
#         Classification, models.DO_NOTHING, db_column='classification_uid', blank=True, null=True)
#     secondary_classification_uid = models.CharField(
#         max_length=32, blank=True, null=True)
#     tertiary_classification_uid = models.CharField(
#         max_length=32, blank=True, null=True)
#     record_number = models.CharField(max_length=100, blank=True, null=True)
#     retention_schedule_uid = models.ForeignKey(
#         'RetentionSchedule', models.DO_NOTHING, db_column='retention_schedule_uid', blank=True, null=True)
#     hold_uid = models.ForeignKey(
#         Hold, models.DO_NOTHING, db_column='hold_uid', blank=True, null=True)
#     disposition_status = models.IntegerField(blank=True, null=True)
#     title = models.CharField(max_length=255, blank=True, null=True)
#     combined_title = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     date_registered = models.DateTimeField(blank=True, null=True)
#     creator_name = models.CharField(max_length=255, blank=True, null=True)
#     creator_username = models.CharField(max_length=255, blank=True, null=True)
#     notes = models.TextField(blank=True, null=True)
#     home_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='home_uid', blank=True, null=True)
#     assignee_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='assignee_uid', blank=True, null=True)
#     is_finalized = models.SmallIntegerField(blank=True, null=True)
#     is_hybrid = models.SmallIntegerField(blank=True, null=True)
#     date_finalized = models.DateTimeField(blank=True, null=True)
#     barcode = models.CharField(max_length=50, blank=True, null=True)
#     external_barcode = models.CharField(max_length=50, blank=True, null=True)
#     external_uid = models.CharField(max_length=50, blank=True, null=True)
#     integrity_check = models.TextField(blank=True, null=True)
#     security_level_uid = models.ForeignKey(
#         'SecurityLevel', models.DO_NOTHING, db_column='security_level_uid', blank=True, null=True)
#     date_last_modified = models.DateTimeField(blank=True, null=True)
#     date_last_modified_of_contents = models.DateTimeField(
#         blank=True, null=True)
#     client_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='client_uid', blank=True, null=True)
#     date_closed = models.DateTimeField(blank=True, null=True)
#     next_enclosure_number = models.IntegerField()
#     enclosure_number_increment = models.IntegerField()
#     uncompressed_record_number = models.CharField(
#         max_length=100, blank=True, null=True)
#     security_based_on_container = models.SmallIntegerField(
#         blank=True, null=True)
#     bypass_referenced_acls = models.SmallIntegerField(blank=True, null=True)
#     opened_temporarily = models.SmallIntegerField(blank=True, null=True)
#     date_created = models.DateTimeField(blank=True, null=True)
#     author = models.CharField(max_length=255, blank=True, null=True)
#     batch_id = models.CharField(max_length=40, blank=True, null=True)
#     date_archived = models.DateTimeField(blank=True, null=True)
#     date_made_inactive = models.DateTimeField(blank=True, null=True)
#     date_of_last_enclosure = models.DateTimeField(blank=True, null=True)
#     date_enclosed = models.DateTimeField(blank=True, null=True)
#     record_class = models.IntegerField()
#     container_record_number = models.CharField(
#         max_length=50, blank=True, null=True)
#     classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     secondary_classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     tertiary_classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     assignee_name = models.CharField(max_length=255, blank=True, null=True)
#     home_name = models.CharField(max_length=255, blank=True, null=True)
#     owner_name = models.CharField(max_length=255, blank=True, null=True)
#     retention_schedule_number = models.CharField(
#         max_length=100, blank=True, null=True)
#     security_level_number = models.SmallIntegerField(blank=True, null=True)
#     client_name = models.CharField(max_length=255, blank=True, null=True)
#     is_container_removed_on_ret_trig = models.SmallIntegerField(
#         blank=True, null=True)
#     is_set_home_on_container_ret_trig = models.SmallIntegerField(
#         blank=True, null=True)
#     retention_schedule_new_home = models.CharField(
#         max_length=32, blank=True, null=True)
#     is_misfiled = models.SmallIntegerField(blank=True, null=True)
#     master_uid = models.CharField(max_length=65, blank=True, null=True)
#     hybrid_remarks = models.TextField(blank=True, null=True)
#     date_last_modified_of_security_level = models.DateTimeField(
#         blank=True, null=True)
#     is_declassify = models.SmallIntegerField(blank=True, null=True)
#     is_imported = models.SmallIntegerField(blank=True, null=True)
#     enforce_single_creation_in_a_workflow = models.SmallIntegerField()
#     check_in_as_new_version = models.SmallIntegerField()
#     check_in_as_override_previous_content = models.SmallIntegerField()
#     is_declassify_alias = models.TextField(blank=True, null=True)
#     is_auto_update_security_level = models.SmallIntegerField()
#     is_auto_update_security_level_on_particular_date = models.SmallIntegerField()
#     security_level_trigger_date = models.DateTimeField(blank=True, null=True)
#     is_update_security_level_on_triggered_event = models.SmallIntegerField()
#     security_level_triggered_event = models.IntegerField(blank=True, null=True)
#     security_level_triggered_event_type = models.IntegerField(
#         blank=True, null=True)
#     security_level_triggered_event_duration = models.IntegerField(
#         blank=True, null=True)
#     security_level_triggered_event_property = models.CharField(
#         max_length=32, blank=True, null=True)
#     auto_update_security_level_id = models.CharField(
#         max_length=32, blank=True, null=True)
#     ae6c83a22dd849ebba2cfddb45a32a47 = models.CharField(
#         max_length=100, blank=True, null=True)
#     h763e35b6288452895b143ec4bad9d02 = models.CharField(
#         max_length=255, blank=True, null=True)
#     ac587b9bdb0545d9a4bb872848b12755 = models.CharField(
#         max_length=100, blank=True, null=True)
#     c7b15198b7a844d2bbe56fa6116f9018 = models.CharField(
#         max_length=15, blank=True, null=True)
#     ibdaf89d09234fef9826c0f2a81ef088 = models.CharField(
#         max_length=255, blank=True, null=True)
#     e12bc6ec5ab144aab50b592c046de9f5 = models.TextField(blank=True, null=True)
#     f5da945a323c4488b407142013d47646 = models.CharField(
#         max_length=15, blank=True, null=True)
#     he2bb392ca384d81a11181cdea5a9006 = models.CharField(
#         max_length=32, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'nodetype_f2bfeb5852264c5aa67f53f96ac28d39'


# class NodetypeFd5Cb124De3F463Fac3F308181Eeb551(models.Model):
#     uid = models.CharField(primary_key=True, max_length=65)
#     acl_uid = models.ForeignKey(
#         Acl, models.DO_NOTHING, db_column='acl_uid', blank=True, null=True)
#     owner_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='owner_uid', blank=True, null=True)
#     classification_uid = models.ForeignKey(
#         Classification, models.DO_NOTHING, db_column='classification_uid', blank=True, null=True)
#     secondary_classification_uid = models.CharField(
#         max_length=32, blank=True, null=True)
#     tertiary_classification_uid = models.CharField(
#         max_length=32, blank=True, null=True)
#     record_number = models.CharField(max_length=100, blank=True, null=True)
#     retention_schedule_uid = models.ForeignKey(
#         'RetentionSchedule', models.DO_NOTHING, db_column='retention_schedule_uid', blank=True, null=True)
#     hold_uid = models.ForeignKey(
#         Hold, models.DO_NOTHING, db_column='hold_uid', blank=True, null=True)
#     disposition_status = models.IntegerField(blank=True, null=True)
#     title = models.CharField(max_length=255, blank=True, null=True)
#     combined_title = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     date_registered = models.DateTimeField(blank=True, null=True)
#     creator_name = models.CharField(max_length=255, blank=True, null=True)
#     creator_username = models.CharField(max_length=255, blank=True, null=True)
#     notes = models.TextField(blank=True, null=True)
#     home_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='home_uid', blank=True, null=True)
#     assignee_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='assignee_uid', blank=True, null=True)
#     is_finalized = models.SmallIntegerField(blank=True, null=True)
#     is_hybrid = models.SmallIntegerField(blank=True, null=True)
#     date_finalized = models.DateTimeField(blank=True, null=True)
#     barcode = models.CharField(max_length=50, blank=True, null=True)
#     external_barcode = models.CharField(max_length=50, blank=True, null=True)
#     external_uid = models.CharField(max_length=50, blank=True, null=True)
#     integrity_check = models.TextField(blank=True, null=True)
#     security_level_uid = models.ForeignKey(
#         'SecurityLevel', models.DO_NOTHING, db_column='security_level_uid', blank=True, null=True)
#     date_last_modified = models.DateTimeField(blank=True, null=True)
#     date_last_modified_of_contents = models.DateTimeField(
#         blank=True, null=True)
#     client_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='client_uid', blank=True, null=True)
#     date_closed = models.DateTimeField(blank=True, null=True)
#     next_enclosure_number = models.IntegerField()
#     enclosure_number_increment = models.IntegerField()
#     uncompressed_record_number = models.CharField(
#         max_length=100, blank=True, null=True)
#     security_based_on_container = models.SmallIntegerField(
#         blank=True, null=True)
#     bypass_referenced_acls = models.SmallIntegerField(blank=True, null=True)
#     opened_temporarily = models.SmallIntegerField(blank=True, null=True)
#     date_created = models.DateTimeField(blank=True, null=True)
#     author = models.CharField(max_length=255, blank=True, null=True)
#     batch_id = models.CharField(max_length=255, blank=True, null=True)
#     date_archived = models.DateTimeField(blank=True, null=True)
#     date_made_inactive = models.DateTimeField(blank=True, null=True)
#     date_of_last_enclosure = models.DateTimeField(blank=True, null=True)
#     date_enclosed = models.DateTimeField(blank=True, null=True)
#     record_class = models.IntegerField()
#     container_record_number = models.CharField(
#         max_length=50, blank=True, null=True)
#     classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     secondary_classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     tertiary_classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     assignee_name = models.CharField(max_length=255, blank=True, null=True)
#     home_name = models.CharField(max_length=255, blank=True, null=True)
#     owner_name = models.CharField(max_length=255, blank=True, null=True)
#     retention_schedule_number = models.CharField(
#         max_length=100, blank=True, null=True)
#     security_level_number = models.SmallIntegerField(blank=True, null=True)
#     client_name = models.CharField(max_length=255, blank=True, null=True)
#     is_container_removed_on_ret_trig = models.SmallIntegerField(
#         blank=True, null=True)
#     is_set_home_on_container_ret_trig = models.SmallIntegerField(
#         blank=True, null=True)
#     retention_schedule_new_home = models.CharField(
#         max_length=32, blank=True, null=True)
#     is_misfiled = models.SmallIntegerField(blank=True, null=True)
#     master_uid = models.CharField(max_length=65, blank=True, null=True)
#     hybrid_remarks = models.TextField(blank=True, null=True)
#     date_last_modified_of_security_level = models.DateTimeField(
#         blank=True, null=True)
#     is_declassify = models.SmallIntegerField(blank=True, null=True)
#     is_imported = models.SmallIntegerField(blank=True, null=True)
#     enforce_single_creation_in_a_workflow = models.SmallIntegerField()
#     check_in_as_new_version = models.SmallIntegerField()
#     check_in_as_override_previous_content = models.SmallIntegerField()
#     is_declassify_alias = models.TextField(blank=True, null=True)
#     is_auto_update_security_level = models.SmallIntegerField()
#     is_auto_update_security_level_on_particular_date = models.SmallIntegerField()
#     security_level_trigger_date = models.DateTimeField(blank=True, null=True)
#     is_update_security_level_on_triggered_event = models.SmallIntegerField()
#     security_level_triggered_event = models.IntegerField(blank=True, null=True)
#     security_level_triggered_event_type = models.IntegerField(
#         blank=True, null=True)
#     security_level_triggered_event_duration = models.IntegerField(
#         blank=True, null=True)
#     security_level_triggered_event_property = models.CharField(
#         max_length=32, blank=True, null=True)
#     auto_update_security_level_id = models.CharField(
#         max_length=32, blank=True, null=True)
#     mdd00000000000000000000000dsd001 = models.DateTimeField(
#         blank=True, null=True)
#     mdd00000000000000000000000dst001 = models.CharField(
#         max_length=255, blank=True, null=True)
#     mdd00000000000000000000000dso001 = models.CharField(
#         max_length=100, blank=True, null=True)
#     mdd00000000000000000000000dcao01 = models.CharField(
#         max_length=255, blank=True, null=True)
#     mdd00000000000000000000000dubog1 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000ded001 = models.DateTimeField(
#         blank=True, null=True)
#     mdd00000000000000000000000dserog = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000dnor01 = models.CharField(
#         max_length=255, blank=True, null=True)
#     mdd00000000000000000000000dero01 = models.CharField(
#         max_length=255, blank=True, null=True)
#     mdd00000000000000000000000dcav01 = models.CharField(
#         max_length=255, blank=True, null=True)
#     mdd00000000000000000000000drd001 = models.CharField(
#         max_length=255, blank=True, null=True)
#     mdd00000000000000000000000wnor01 = models.CharField(
#         max_length=100, blank=True, null=True)
#     mdd00000000000000000000000wmed01 = models.CharField(
#         max_length=100, blank=True, null=True)
#     mdd00000000000000000000000wmeo01 = models.CharField(
#         max_length=255, blank=True, null=True)
#     mdd00000000000000000000000wecmed = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000wrd001 = models.CharField(
#         max_length=100, blank=True, null=True)
#     mdd00000000000000000000000wero01 = models.CharField(
#         max_length=255, blank=True, null=True)
#     mdd00000000000000000000000wserog = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000wubog1 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000wcav01 = models.CharField(
#         max_length=100, blank=True, null=True)
#     mdd00000000000000000000000wcao01 = models.CharField(
#         max_length=255, blank=True, null=True)
#     mdd00000000000000000000000wed001 = models.DateTimeField(
#         blank=True, null=True)
#     mdd00000000000000000000000wso001 = models.CharField(
#         max_length=100, blank=True, null=True)
#     mdd00000000000000000000000wsd001 = models.DateTimeField(
#         blank=True, null=True)
#     mdd00000000000000000000000wst001 = models.CharField(
#         max_length=100, blank=True, null=True)
#     mdd00000000000000000000000wscd01 = models.CharField(
#         max_length=100, blank=True, null=True)
#     mdd00000000000000000000000mso001 = models.CharField(
#         max_length=255, blank=True, null=True)
#     mdd00000000000000000000000mst001 = models.CharField(
#         max_length=100, blank=True, null=True)
#     mdd00000000000000000000000msd001 = models.DateTimeField(
#         blank=True, null=True)
#     mdd00000000000000000000000msop01 = models.CharField(
#         max_length=100, blank=True, null=True)
#     mdd00000000000000000000000med001 = models.DateTimeField(
#         blank=True, null=True)
#     mdd00000000000000000000000mcao01 = models.CharField(
#         max_length=255, blank=True, null=True)
#     mdd00000000000000000000000mcav01 = models.CharField(
#         max_length=100, blank=True, null=True)
#     mdd00000000000000000000000mubog1 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000mserog = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000mero01 = models.CharField(
#         max_length=255, blank=True, null=True)
#     mdd00000000000000000000000mrd001 = models.CharField(
#         max_length=100, blank=True, null=True)
#     mdd00000000000000000000000mecmed = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000mmeo01 = models.CharField(
#         max_length=255, blank=True, null=True)
#     mdd00000000000000000000000mmed01 = models.CharField(
#         max_length=100, blank=True, null=True)
#     mdd00000000000000000000000mc2801 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000mnor01 = models.CharField(
#         max_length=100, blank=True, null=True)
#     mdd00000000000000000000000yubog1 = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000ycao01 = models.CharField(
#         max_length=255, blank=True, null=True)
#     mdd00000000000000000000000ycav01 = models.CharField(
#         max_length=100, blank=True, null=True)
#     mdd00000000000000000000000yed001 = models.DateTimeField(
#         blank=True, null=True)
#     mdd00000000000000000000000yscd01 = models.CharField(
#         max_length=255, blank=True, null=True)
#     mdd00000000000000000000000ysdop1 = models.CharField(
#         max_length=100, blank=True, null=True)
#     mdd00000000000000000000000yso001 = models.CharField(
#         max_length=255, blank=True, null=True)
#     mdd00000000000000000000000yst001 = models.CharField(
#         max_length=100, blank=True, null=True)
#     mdd00000000000000000000000yserog = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000ysd001 = models.DateTimeField(
#         blank=True, null=True)
#     mdd00000000000000000000000yrop01 = models.CharField(
#         max_length=255, blank=True, null=True)
#     mdd00000000000000000000000yrd001 = models.CharField(
#         max_length=100, blank=True, null=True)
#     mdd00000000000000000000000yecoed = models.SmallIntegerField(
#         blank=True, null=True)
#     mdd00000000000000000000000ymeop1 = models.CharField(
#         max_length=255, blank=True, null=True)
#     mdd00000000000000000000000ymed01 = models.CharField(
#         max_length=100, blank=True, null=True)
#     mdd00000000000000000000000ynor01 = models.CharField(
#         max_length=100, blank=True, null=True)
#     mdd00000000000000000000000enamc1 = models.SmallIntegerField(
#         blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'nodetype_fd5cb124de3f463fac3f308181eeb551'


# class NodetypeI00C1Aaa03044852A17746Bf95B806Bd(models.Model):
#     uid = models.CharField(primary_key=True, max_length=65)
#     acl_uid = models.ForeignKey(
#         Acl, models.DO_NOTHING, db_column='acl_uid', blank=True, null=True)
#     owner_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='owner_uid', blank=True, null=True)
#     classification_uid = models.ForeignKey(
#         Classification, models.DO_NOTHING, db_column='classification_uid', blank=True, null=True)
#     secondary_classification_uid = models.CharField(
#         max_length=32, blank=True, null=True)
#     tertiary_classification_uid = models.CharField(
#         max_length=32, blank=True, null=True)
#     record_number = models.CharField(max_length=100, blank=True, null=True)
#     retention_schedule_uid = models.ForeignKey(
#         'RetentionSchedule', models.DO_NOTHING, db_column='retention_schedule_uid', blank=True, null=True)
#     hold_uid = models.ForeignKey(
#         Hold, models.DO_NOTHING, db_column='hold_uid', blank=True, null=True)
#     disposition_status = models.IntegerField(blank=True, null=True)
#     title = models.CharField(max_length=255, blank=True, null=True)
#     combined_title = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     date_registered = models.DateTimeField(blank=True, null=True)
#     creator_name = models.CharField(max_length=255, blank=True, null=True)
#     creator_username = models.CharField(max_length=255, blank=True, null=True)
#     notes = models.TextField(blank=True, null=True)
#     home_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='home_uid', blank=True, null=True)
#     assignee_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='assignee_uid', blank=True, null=True)
#     is_finalized = models.SmallIntegerField(blank=True, null=True)
#     is_hybrid = models.SmallIntegerField(blank=True, null=True)
#     date_finalized = models.DateTimeField(blank=True, null=True)
#     barcode = models.CharField(max_length=50, blank=True, null=True)
#     external_barcode = models.CharField(max_length=50, blank=True, null=True)
#     external_uid = models.CharField(max_length=50, blank=True, null=True)
#     integrity_check = models.TextField(blank=True, null=True)
#     security_level_uid = models.ForeignKey(
#         'SecurityLevel', models.DO_NOTHING, db_column='security_level_uid', blank=True, null=True)
#     date_last_modified = models.DateTimeField(blank=True, null=True)
#     date_last_modified_of_contents = models.DateTimeField(
#         blank=True, null=True)
#     client_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='client_uid', blank=True, null=True)
#     date_closed = models.DateTimeField(blank=True, null=True)
#     next_enclosure_number = models.IntegerField()
#     enclosure_number_increment = models.IntegerField()
#     uncompressed_record_number = models.CharField(
#         max_length=100, blank=True, null=True)
#     security_based_on_container = models.SmallIntegerField(
#         blank=True, null=True)
#     bypass_referenced_acls = models.SmallIntegerField(blank=True, null=True)
#     opened_temporarily = models.SmallIntegerField(blank=True, null=True)
#     date_created = models.DateTimeField(blank=True, null=True)
#     author = models.CharField(max_length=255, blank=True, null=True)
#     batch_id = models.CharField(max_length=40, blank=True, null=True)
#     date_archived = models.DateTimeField(blank=True, null=True)
#     date_made_inactive = models.DateTimeField(blank=True, null=True)
#     date_of_last_enclosure = models.DateTimeField(blank=True, null=True)
#     date_enclosed = models.DateTimeField(blank=True, null=True)
#     record_class = models.IntegerField()
#     container_record_number = models.CharField(
#         max_length=50, blank=True, null=True)
#     classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     secondary_classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     tertiary_classification_full_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     assignee_name = models.CharField(max_length=255, blank=True, null=True)
#     home_name = models.CharField(max_length=255, blank=True, null=True)
#     owner_name = models.CharField(max_length=255, blank=True, null=True)
#     retention_schedule_number = models.CharField(
#         max_length=100, blank=True, null=True)
#     security_level_number = models.SmallIntegerField(blank=True, null=True)
#     client_name = models.CharField(max_length=255, blank=True, null=True)
#     is_container_removed_on_ret_trig = models.SmallIntegerField(
#         blank=True, null=True)
#     is_set_home_on_container_ret_trig = models.SmallIntegerField(
#         blank=True, null=True)
#     retention_schedule_new_home = models.CharField(
#         max_length=32, blank=True, null=True)
#     is_misfiled = models.SmallIntegerField(blank=True, null=True)
#     master_uid = models.CharField(max_length=65, blank=True, null=True)
#     hybrid_remarks = models.TextField(blank=True, null=True)
#     date_last_modified_of_security_level = models.DateTimeField(
#         blank=True, null=True)
#     is_declassify = models.SmallIntegerField(blank=True, null=True)
#     is_imported = models.SmallIntegerField(blank=True, null=True)
#     enforce_single_creation_in_a_workflow = models.SmallIntegerField()
#     check_in_as_new_version = models.SmallIntegerField()
#     check_in_as_override_previous_content = models.SmallIntegerField()
#     is_declassify_alias = models.TextField(blank=True, null=True)
#     is_auto_update_security_level = models.SmallIntegerField()
#     is_auto_update_security_level_on_particular_date = models.SmallIntegerField()
#     security_level_trigger_date = models.DateTimeField(blank=True, null=True)
#     is_update_security_level_on_triggered_event = models.SmallIntegerField()
#     security_level_triggered_event = models.IntegerField(blank=True, null=True)
#     security_level_triggered_event_type = models.IntegerField(
#         blank=True, null=True)
#     security_level_triggered_event_duration = models.IntegerField(
#         blank=True, null=True)
#     security_level_triggered_event_property = models.CharField(
#         max_length=32, blank=True, null=True)
#     auto_update_security_level_id = models.CharField(
#         max_length=32, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'nodetype_i00c1aaa03044852a17746bf95b806bd'


# class NodetypeProperty(models.Model):
#     nodetype_uid = models.OneToOneField(
#         Nodetype, models.DO_NOTHING, db_column='nodetype_uid', primary_key=True)
#     property_uid = models.ForeignKey(
#         'Property', models.DO_NOTHING, db_column='property_uid')
#     alias = models.CharField(max_length=255)
#     is_mandatory = models.SmallIntegerField()
#     is_readonly = models.SmallIntegerField()
#     property_group_name = models.CharField(
#         max_length=50, blank=True, null=True)
#     property_order = models.IntegerField(blank=True, null=True)
#     default_value = models.TextField(blank=True, null=True)
#     issortable = models.SmallIntegerField()

#     class Meta:
#         managed = False
#         db_table = 'nodetype_property'
#         unique_together = (('nodetype_uid', 'property_uid'),)


# class ObjectEvent(models.Model):
#     event_timestamp = models.DateTimeField()
#     event_type = models.CharField(max_length=100)
#     object_uid = models.CharField(max_length=32)
#     object_type = models.IntegerField()
#     object_name = models.CharField(max_length=255)
#     principal_uid = models.CharField(max_length=32)
#     principal_name = models.CharField(max_length=255)
#     details = models.TextField()
#     ipaddress = models.CharField(max_length=45, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'object_event'


# class Part(models.Model):
#     uid = models.CharField(primary_key=True, max_length=32)
#     content_uid = models.ForeignKey(
#         Content, models.DO_NOTHING, db_column='content_uid')
#     part_no = models.IntegerField()
#     part_type = models.CharField(max_length=25, blank=True, null=True)
#     filename = models.CharField(max_length=255)
#     filesize = models.BigIntegerField()
#     date_last_modified = models.DateTimeField(blank=True, null=True)
#     date_created = models.DateTimeField(blank=True, null=True)
#     store_uid = models.CharField(max_length=32)
#     mimetype = models.CharField(max_length=255, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'part'


# class PaswEvents(models.Model):
#     uid = models.CharField(primary_key=True, max_length=32)
#     principal_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='principal_uid', blank=True, null=True)
#     changed_by = models.CharField(max_length=32, blank=True, null=True)
#     password = models.CharField(max_length=255, blank=True, null=True)
#     date_modified = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'pasw_events'


# class Payee(models.Model):
#     name = models.CharField(max_length=255, blank=True, null=True)
#     recipient_reference = models.CharField(
#         max_length=255, blank=True, null=True)
#     internal_reference = models.CharField(
#         max_length=255, blank=True, null=True)
#     id_type = models.IntegerField(blank=True, null=True)
#     id_value = models.CharField(max_length=255, blank=True, null=True)
#     email_address = models.CharField(max_length=255, blank=True, null=True)
#     phone_number = models.CharField(max_length=255, blank=True, null=True)
#     payment_details = models.CharField(max_length=255, blank=True, null=True)
#     status = models.IntegerField(blank=True, null=True)
#     merchant = models.ForeignKey(
#         Merchant, models.DO_NOTHING, blank=True, null=True)
#     date_created = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'payee'
#         unique_together = (('name', 'merchant'),)


# class PayeeBank(models.Model):
#     swift_code = models.CharField(primary_key=True, max_length=255)
#     name = models.CharField(max_length=255, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'payee_bank'


# class PayeeBankAccount(models.Model):
#     bank_swift_code = models.ForeignKey(
#         PayeeBank, models.DO_NOTHING, db_column='bank_swift_code', blank=True, null=True)
#     account_holder_name = models.CharField(
#         max_length=96, blank=True, null=True)
#     bank_account_number = models.CharField(
#         max_length=255, blank=True, null=True)
#     payee_id = models.IntegerField(blank=True, null=True)
#     id_type = models.IntegerField(blank=True, null=True)
#     id_value = models.CharField(max_length=255, blank=True, null=True)
#     is_active = models.BooleanField(blank=True, null=True)
#     payment_method = models.IntegerField(blank=True, null=True)
#     account_type = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'payee_bank_account'


# class PayoutPayment(models.Model):
#     recipient_reference = models.CharField(
#         max_length=255, blank=True, null=True)
#     internal_reference = models.CharField(
#         max_length=255, blank=True, null=True)
#     amount = models.DecimalField(
#         max_digits=19, decimal_places=2, blank=True, null=True)
#     payment_details = models.CharField(max_length=255, blank=True, null=True)
#     payment_date = models.DateTimeField(blank=True, null=True)
#     status = models.IntegerField(blank=True, null=True)
#     batch = models.ForeignKey('PayoutPaymentBatch',
#                               models.DO_NOTHING, blank=True, null=True)
#     payee = models.ForeignKey(Payee, models.DO_NOTHING, blank=True, null=True)
#     date_created = models.DateTimeField(blank=True, null=True)
#     response_date = models.DateTimeField(blank=True, null=True)
#     status_reason = models.CharField(max_length=255, blank=True, null=True)
#     response_batch = models.CharField(max_length=225, blank=True, null=True)
#     payee_bank_account = models.ForeignKey(
#         PayeeBankAccount, models.DO_NOTHING, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'payout_payment'


# class PayoutPaymentBatch(models.Model):
#     batch_id = models.CharField(primary_key=True, max_length=255)
#     payment_date = models.DateTimeField(blank=True, null=True)
#     status = models.IntegerField(blank=True, null=True)
#     merchant = models.ForeignKey(
#         Merchant, models.DO_NOTHING, blank=True, null=True)
#     date_created = models.DateTimeField(blank=True, null=True)
#     file_location = models.CharField(max_length=1000, blank=True, null=True)
#     maker = models.ForeignKey(
#         Employee, models.DO_NOTHING, blank=True, null=True)
#     checker = models.ForeignKey(
#         Employee, models.DO_NOTHING, blank=True, null=True)
#     status_reason = models.CharField(max_length=255, blank=True, null=True)
#     debiting_method = models.CharField(max_length=1, blank=True, null=True)
#     purpose = models.IntegerField(blank=True, null=True)
#     payment_method = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'payout_payment_batch'


# class Pin(models.Model):
#     uid = models.CharField(primary_key=True, max_length=32)
#     acl_uid = models.ForeignKey(
#         Acl, models.DO_NOTHING, db_column='acl_uid', blank=True, null=True)
#     node_uid = models.ForeignKey(
#         'RecordNode', models.DO_NOTHING, db_column='node_uid')
#     expiry_date = models.DateTimeField()
#     is_used = models.SmallIntegerField()
#     use_only_once = models.SmallIntegerField()
#     password = models.CharField(max_length=50, blank=True, null=True)
#     recipient_email = models.CharField(max_length=255)
#     shared_by_uid = models.ForeignKey(
#         'Principal', models.DO_NOTHING, db_column='shared_by_uid')
#     password_retry_count = models.SmallIntegerField()
#     history = models.TextField(blank=True, null=True)
#     subject = models.CharField(max_length=255, blank=True, null=True)
#     message = models.TextField(blank=True, null=True)
#     pin_disable = models.SmallIntegerField()
#     email_cc = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'pin'


class Principal(models.Model):
    uid = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(max_length=255)
    extid = models.CharField(unique=True, max_length=50, blank=True, null=True)
    username = models.CharField(unique=True, max_length=50, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    isgroup = models.SmallIntegerField()
    acl_uid = models.CharField(max_length=32, blank=True, null=True)
    security_level_uid = models.CharField(max_length=32, blank=True, null=True)
    isinternal = models.SmallIntegerField()
    issuspended = models.SmallIntegerField()
    gender = models.SmallIntegerField()
    email = models.CharField(max_length=255, blank=True, null=True)
    profile_uid = models.ForeignKey(
        "Profile", models.DO_NOTHING, db_column="profile_uid", blank=True, null=True
    )
    canlogin = models.SmallIntegerField()
    active_from = models.DateTimeField(blank=True, null=True)
    active_to = models.DateTimeField(blank=True, null=True)
    date_registered = models.DateTimeField(blank=True, null=True)
    barcode = models.CharField(unique=True, max_length=50, blank=True, null=True)
    external_barcode = models.CharField(
        unique=True, max_length=50, blank=True, null=True
    )
    ptype = models.SmallIntegerField()
    date_last_modified_of_password = models.DateTimeField(blank=True, null=True)
    loginmessage = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    ic_passport_no = models.CharField(max_length=32, blank=True, null=True)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    nationality = models.CharField(max_length=50, blank=True, null=True)
    business_occupation = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    mobile_phone = models.CharField(max_length=20, blank=True, null=True)
    af7c0ba6be8a452194d3e040048463d6 = models.CharField(
        max_length=100, blank=True, null=True
    )
    jc2300d55f3547e3a495f6332e259604 = models.CharField(
        max_length=100, blank=True, null=True
    )
    mdd0000000000000000000000000001p = models.CharField(
        max_length=100, blank=True, null=True
    )
    fc3b7ba10a1441c8ae2f6884869bd95f = models.CharField(
        max_length=100, blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "principal"


# class PrincipalDefaultOrganization(models.Model):
#     principal_uid = models.OneToOneField(
#         Principal, models.DO_NOTHING, db_column='principal_uid', primary_key=True)
#     default_org_uid = models.ForeignKey(
#         Principal, models.DO_NOTHING, db_column='default_org_uid')

#     class Meta:
#         managed = False
#         db_table = 'principal_default_organization'


# class PrincipalDefaultPosition(models.Model):
#     principal_uid = models.OneToOneField(
#         Principal, models.DO_NOTHING, db_column='principal_uid', primary_key=True)
#     default_position_uid = models.ForeignKey(
#         Principal, models.DO_NOTHING, db_column='default_position_uid')

#     class Meta:
#         managed = False
#         db_table = 'principal_default_position'


# class PrincipalGadgetLayout(models.Model):
#     uid = models.CharField(primary_key=True, max_length=32)
#     acl_uid = models.CharField(max_length=32, blank=True, null=True)
#     principal = models.ForeignKey(Principal, models.DO_NOTHING)
#     gadgetid = models.ForeignKey(
#         Gadget, models.DO_NOTHING, db_column='gadgetid')
#     sort_order = models.SmallIntegerField()

#     class Meta:
#         managed = False
#         db_table = 'principal_gadget_layout'


# class PrincipalGroup(models.Model):
#     principal_uid = models.OneToOneField(
#         Principal, models.DO_NOTHING, db_column='principal_uid', primary_key=True)
#     group_uid = models.ForeignKey(
#         Principal, models.DO_NOTHING, db_column='group_uid')

#     class Meta:
#         managed = False
#         db_table = 'principal_group'
#         unique_together = (('principal_uid', 'group_uid'),)


# class PrincipalRefs(models.Model):
#     property_uid = models.OneToOneField(
#         'Property', models.DO_NOTHING, db_column='property_uid', primary_key=True)
#     from_node_uid = models.CharField(max_length=65)
#     to_principal_uid = models.CharField(max_length=32)

#     class Meta:
#         managed = False
#         db_table = 'principal_refs'
#         unique_together = (
#             ('property_uid', 'from_node_uid', 'to_principal_uid'),)


class Profile(models.Model):
    uid = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(unique=True, max_length=50)
    p1000 = models.SmallIntegerField()
    p1 = models.SmallIntegerField()
    p11 = models.SmallIntegerField()
    p21 = models.SmallIntegerField()
    p41 = models.SmallIntegerField()
    p42 = models.SmallIntegerField()
    p51 = models.SmallIntegerField()
    p52 = models.SmallIntegerField()
    p53 = models.SmallIntegerField()
    p54 = models.SmallIntegerField()
    p61 = models.SmallIntegerField()
    p71 = models.SmallIntegerField()
    p81 = models.SmallIntegerField()
    p91 = models.SmallIntegerField()
    p92 = models.SmallIntegerField()
    p93 = models.SmallIntegerField()
    p94 = models.SmallIntegerField()
    p95 = models.SmallIntegerField()
    p100 = models.SmallIntegerField()
    p101 = models.SmallIntegerField()
    p102 = models.SmallIntegerField()
    p103 = models.SmallIntegerField()
    p111 = models.SmallIntegerField()
    p112 = models.SmallIntegerField()
    p121 = models.SmallIntegerField()
    p122 = models.SmallIntegerField()
    p123 = models.SmallIntegerField()
    p2001 = models.SmallIntegerField()
    p2002 = models.SmallIntegerField()
    p2003 = models.SmallIntegerField()
    p2005 = models.SmallIntegerField()
    p2006 = models.SmallIntegerField()
    p2007 = models.SmallIntegerField()
    p2008 = models.SmallIntegerField()
    p2009 = models.SmallIntegerField()
    p2010 = models.SmallIntegerField()
    p2011 = models.SmallIntegerField()
    p2012 = models.SmallIntegerField()
    p2013 = models.SmallIntegerField()
    p2014 = models.SmallIntegerField()
    p2015 = models.SmallIntegerField()
    p2016 = models.SmallIntegerField()
    p2017 = models.SmallIntegerField()
    p2018 = models.SmallIntegerField()
    p2019 = models.SmallIntegerField()
    p2020 = models.SmallIntegerField()
    p2021 = models.SmallIntegerField()
    p2022 = models.SmallIntegerField()
    p2023 = models.SmallIntegerField()
    p2024 = models.SmallIntegerField()
    p2025 = models.SmallIntegerField()
    p2026 = models.SmallIntegerField()
    p2027 = models.SmallIntegerField()
    p2028 = models.SmallIntegerField()
    p2029 = models.SmallIntegerField()
    p3000 = models.SmallIntegerField()
    p4000 = models.SmallIntegerField()
    p5000 = models.SmallIntegerField()
    p6000 = models.SmallIntegerField()
    p6001 = models.SmallIntegerField()
    p7000 = models.SmallIntegerField()
    p8000 = models.SmallIntegerField()
    p8001 = models.SmallIntegerField()
    p9000 = models.SmallIntegerField()
    p10000 = models.SmallIntegerField()
    p11000 = models.SmallIntegerField()
    p12000 = models.SmallIntegerField()
    p13000 = models.SmallIntegerField()
    p14000 = models.SmallIntegerField()
    p15000 = models.SmallIntegerField()
    p16000 = models.SmallIntegerField()
    p17000 = models.SmallIntegerField()
    p18000 = models.SmallIntegerField()
    p19000 = models.SmallIntegerField()
    p20000 = models.SmallIntegerField()
    p21000 = models.SmallIntegerField()
    p22000 = models.SmallIntegerField()
    p23000 = models.SmallIntegerField()
    p25000 = models.SmallIntegerField()
    p26000 = models.SmallIntegerField()
    p27000 = models.SmallIntegerField()
    p28000 = models.SmallIntegerField()
    p29000 = models.SmallIntegerField()
    p30000 = models.SmallIntegerField()
    p31000 = models.SmallIntegerField()
    p40000 = models.SmallIntegerField()
    p41000 = models.SmallIntegerField()
    p42000 = models.SmallIntegerField()
    p43000 = models.SmallIntegerField()
    p44000 = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = "profile"


# class ProfileGadgetLayout(models.Model):
#     uid = models.CharField(primary_key=True, max_length=32)
#     acl_uid = models.CharField(max_length=32, blank=True, null=True)
#     profile = models.ForeignKey(Profile, models.DO_NOTHING)
#     gadgetid = models.ForeignKey(
#         Gadget, models.DO_NOTHING, db_column='gadgetid')
#     sort_order = models.SmallIntegerField()

#     class Meta:
#         managed = False
#         db_table = 'profile_gadget_layout'


# class Property(models.Model):
#     uid = models.CharField(primary_key=True, max_length=32)
#     name = models.CharField(unique=True, max_length=255)
#     property_type = models.IntegerField()
#     length = models.IntegerField()
#     decimals = models.IntegerField()
#     refnodetypeid = models.ForeignKey(
#         Nodetype, models.DO_NOTHING, db_column='refnodetypeid', blank=True, null=True)
#     refmultivalue = models.SmallIntegerField(blank=True, null=True)
#     acl_uid = models.CharField(max_length=32, blank=True, null=True)
#     semantics = models.SmallIntegerField(blank=True, null=True)
#     maskre = models.CharField(max_length=255, blank=True, null=True)
#     min_date_value = models.DateTimeField(blank=True, null=True)
#     max_date_value = models.DateTimeField(blank=True, null=True)
#     min_int_value = models.IntegerField(blank=True, null=True)
#     max_int_value = models.IntegerField(blank=True, null=True)
#     min_decimal_value = models.DecimalField(
#         max_digits=31, decimal_places=5, blank=True, null=True)
#     max_decimal_value = models.DecimalField(
#         max_digits=31, decimal_places=5, blank=True, null=True)
#     groups_only = models.SmallIntegerField(blank=True, null=True)
#     non_groups_only = models.SmallIntegerField(blank=True, null=True)
#     must_be_member_of = models.ForeignKey(
#         Principal, models.DO_NOTHING, db_column='must_be_member_of', blank=True, null=True)
#     must_be_container = models.SmallIntegerField(blank=True, null=True)
#     lookupset_uid = models.ForeignKey(
#         Lookupset, models.DO_NOTHING, db_column='lookupset_uid', blank=True, null=True)
#     using_lookupset = models.SmallIntegerField()
#     allow_non_matching_values = models.SmallIntegerField()
#     apply_to_principal = models.SmallIntegerField()

#     class Meta:
#         managed = False
#         db_table = 'property'


# class PropertyGroup(models.Model):
#     nodetype_uid = models.OneToOneField(
#         Nodetype, models.DO_NOTHING, db_column='nodetype_uid', primary_key=True)
#     name = models.CharField(max_length=50)
#     group_order = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'property_group'
#         unique_together = (('nodetype_uid', 'name'), ('nodetype_uid',
#                            'name'), ('nodetype_uid', 'group_order'),)


# class RecentContainer(models.Model):
#     uid = models.CharField(primary_key=True, max_length=32)
#     node_uid = models.CharField(max_length=65)
#     action_timestamp = models.DateTimeField()
#     actor_uid = models.ForeignKey(
#         Principal, models.DO_NOTHING, db_column='actor_uid')
#     container_level = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'recent_container'
#         unique_together = (('actor_uid', 'node_uid'),)


# class RecordNode(models.Model):
#     record_number = models.CharField(primary_key=True, max_length=50)
#     node_uid = models.CharField(unique=True, max_length=65)

#     class Meta:
#         managed = False
#         db_table = 'record_node'


# class RecordRequest(models.Model):
#     uid = models.CharField(primary_key=True, max_length=32)
#     node_uid = models.ForeignKey(
#         RecordNode, models.DO_NOTHING, db_column='node_uid')
#     request_by_uid = models.CharField(max_length=32)
#     date_needed = models.DateTimeField()
#     requested_period = models.IntegerField(blank=True, null=True)
#     date_request = models.DateTimeField()
#     request_status = models.IntegerField()
#     notes = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'record_request'


# class Rendition(models.Model):
#     uid = models.CharField(primary_key=True, max_length=32)
#     external_id = models.CharField(max_length=255, blank=True, null=True)
#     content_uid = models.ForeignKey(
#         Content, models.DO_NOTHING, db_column='content_uid')
#     filename = models.CharField(max_length=255)
#     filesize = models.BigIntegerField()
#     date_last_modified = models.DateTimeField(blank=True, null=True)
#     date_created = models.DateTimeField(blank=True, null=True)
#     store_uid = models.CharField(max_length=32)
#     mimetype = models.CharField(max_length=255, blank=True, null=True)
#     encryption = models.SmallIntegerField()
#     encryption_password = models.CharField(
#         max_length=255, blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     rendition_type = models.SmallIntegerField()

#     class Meta:
#         managed = False
#         db_table = 'rendition'


# class RetentionSchedule(models.Model):
#     uid = models.CharField(primary_key=True, max_length=32)
#     title = models.CharField(max_length=255, blank=True, null=True)
#     notes = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     number = models.CharField(
#         unique=True, max_length=100, blank=True, null=True)
#     acl_uid = models.CharField(max_length=32, blank=True, null=True)
#     date_created = models.DateTimeField(blank=True, null=True)
#     parent_uid = models.ForeignKey(
#         'self', models.DO_NOTHING, db_column='parent_uid', blank=True, null=True)
#     is_inherit_triggers_from_parent = models.SmallIntegerField()
#     ui_configs = models.TextField(blank=True, null=True)
#     active_from = models.DateTimeField(blank=True, null=True)
#     active_to = models.DateTimeField(blank=True, null=True)
#     creator_uid = models.ForeignKey(
#         Principal, models.DO_NOTHING, db_column='creator_uid', blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'retention_schedule'


# class RetentionTrigger(models.Model):
#     uid = models.CharField(primary_key=True, max_length=32)
#     retention_schedule_uid = models.ForeignKey(
#         RetentionSchedule, models.DO_NOTHING, db_column='retention_schedule_uid')
#     disposal_action = models.SmallIntegerField(blank=True, null=True)
#     trigger_type = models.SmallIntegerField()
#     duration_years = models.IntegerField(blank=True, null=True)
#     duration_months = models.IntegerField(blank=True, null=True)
#     duration_days = models.IntegerField(blank=True, null=True)
#     fixed_date = models.DateTimeField(blank=True, null=True)
#     property_uid = models.ForeignKey(
#         Property, models.DO_NOTHING, db_column='property_uid', blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'retention_trigger'


# class SavedSearch(models.Model):
#     uid = models.CharField(primary_key=True, max_length=32)
#     name = models.CharField(unique=True, max_length=255)
#     description = models.CharField(max_length=255, blank=True, null=True)
#     query_json = models.TextField()
#     owner_uid = models.CharField(max_length=32, blank=True, null=True)
#     acl_uid = models.CharField(max_length=32, blank=True, null=True)
#     formatted_col = models.TextField(blank=True, null=True)
#     formatted_col_width = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'saved_search'


# class SbnQueue(models.Model):
#     uid = models.CharField(primary_key=True, max_length=32)
#     date_added_to_queue = models.DateTimeField(blank=True, null=True)
#     subject = models.CharField(max_length=255, blank=True, null=True)
#     message = models.TextField(blank=True, null=True)
#     send_as_bcc = models.SmallIntegerField()
#     recipients = models.TextField(blank=True, null=True)
#     reply_to = models.CharField(max_length=255, blank=True, null=True)
#     method = models.SmallIntegerField()
#     sent = models.SmallIntegerField()
#     date_sent = models.DateTimeField(blank=True, null=True)
#     urgent = models.SmallIntegerField()
#     no_of_retries = models.SmallIntegerField()
#     cc = models.TextField(blank=True, null=True)
#     node_uid = models.CharField(max_length=65, blank=True, null=True)
#     email_template_uid = models.CharField(max_length=65, blank=True, null=True)
#     mdd_reference = models.CharField(max_length=50, blank=True, null=True)
#     mdd_status = models.IntegerField(blank=True, null=True)
#     mdd_type = models.IntegerField(blank=True, null=True)
#     mdd_merchant_id = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'sbn_queue'
#         unique_together = (('mdd_reference', 'mdd_status', 'mdd_type'),)


# class SchedBasedNotification(models.Model):
#     uid = models.CharField(primary_key=True, max_length=32)
#     name = models.CharField(max_length=100)
#     description = models.CharField(max_length=255, blank=True, null=True)
#     acl_uid = models.CharField(max_length=32, blank=True, null=True)
#     active_from = models.DateTimeField(blank=True, null=True)
#     active_to = models.DateTimeField(blank=True, null=True)
#     suspend = models.SmallIntegerField()
#     saved_search_uid = models.ForeignKey(
#         SavedSearch, models.DO_NOTHING, db_column='saved_search_uid')
#     urgent = models.SmallIntegerField()
#     send_as_bcc = models.SmallIntegerField()
#     email_per_search_result = models.SmallIntegerField()
#     email_template_uid = models.ForeignKey(
#         EmailTemplate, models.DO_NOTHING, db_column='email_template_uid', blank=True, null=True)
#     recipients_email = models.TextField(blank=True, null=True)
#     include_assignee = models.SmallIntegerField()
#     include_home = models.SmallIntegerField()
#     include_owner = models.SmallIntegerField()
#     include_members_of_group = models.SmallIntegerField()
#     group_uid = models.ForeignKey(
#         Principal, models.DO_NOTHING, db_column='group_uid', blank=True, null=True)
#     include_principals_from_property = models.SmallIntegerField()
#     property_uid = models.CharField(max_length=32, blank=True, null=True)
#     sender_email = models.CharField(max_length=255, blank=True, null=True)
#     schedule_type = models.SmallIntegerField()
#     days_of_week = models.CharField(max_length=7)
#     days_of_month = models.CharField(max_length=31)
#     yearly_month_1 = models.SmallIntegerField(blank=True, null=True)
#     yearly_month_2 = models.SmallIntegerField(blank=True, null=True)
#     yearly_month_3 = models.SmallIntegerField(blank=True, null=True)
#     yearly_month_4 = models.SmallIntegerField(blank=True, null=True)
#     yearly_day_1 = models.SmallIntegerField(blank=True, null=True)
#     yearly_day_2 = models.SmallIntegerField(blank=True, null=True)
#     yearly_day_3 = models.SmallIntegerField(blank=True, null=True)
#     yearly_day_4 = models.SmallIntegerField(blank=True, null=True)
#     cc_email = models.TextField(blank=True, null=True)
#     include_principals_from_propertycc = models.SmallIntegerField()
#     propertycc_uid = models.CharField(max_length=32, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'sched_based_notification'


# class SecurityLevel(models.Model):
#     uid = models.CharField(primary_key=True, max_length=32)
#     name = models.CharField(unique=True, max_length=50)
#     level = models.SmallIntegerField()
#     acl_uid = models.CharField(max_length=32, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'security_level'


# class Session(models.Model):
#     uid = models.CharField(primary_key=True, max_length=32)
#     is_open = models.SmallIntegerField()
#     username = models.CharField(max_length=50)
#     is_impersonation = models.SmallIntegerField()
#     impersonator = models.CharField(max_length=20, blank=True, null=True)
#     login_timestamp = models.DateTimeField(blank=True, null=True)
#     logout_timestamp = models.DateTimeField(blank=True, null=True)
#     principal_uid = models.CharField(max_length=32, blank=True, null=True)
#     impersonator_uid = models.CharField(max_length=32, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'session'


# class SmsNotification(models.Model):
#     uid = models.UUIDField(primary_key=True)
#     # This field type is a guess.
#     data_info = models.TextField(blank=True, null=True)
#     sms_message = models.TextField(blank=True, null=True)
#     phone_number = models.CharField(max_length=255, blank=True, null=True)
#     sms_type = models.CharField(max_length=255, blank=True, null=True)
#     merchant_id = models.IntegerField(blank=True, null=True)
#     date_created = models.DateField(blank=True, null=True)
#     date_sent = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'sms_notification'


# class SmsQueue(models.Model):
#     date_added_to_queue = models.DateTimeField(blank=True, null=True)
#     message = models.TextField(blank=True, null=True)
#     contact_number = models.CharField(max_length=20, blank=True, null=True)
#     date_sent = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'sms_queue'


# class StatusCollection(models.Model):
#     type = models.CharField(max_length=20, blank=True, null=True)
#     db_code = models.SmallIntegerField(blank=True, null=True)
#     status = models.CharField(max_length=100, blank=True, null=True)
#     status_desc = models.CharField(max_length=100, blank=True, null=True)
#     response_code = models.CharField(max_length=10, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'status_collection'


# class Store(models.Model):
#     uid = models.CharField(primary_key=True, max_length=32)
#     name = models.CharField(unique=True, max_length=50)
#     store_type = models.CharField(max_length=3)
#     uri = models.CharField(max_length=255)
#     acl_uid = models.CharField(max_length=32, blank=True, null=True)
#     readonly = models.SmallIntegerField()
#     encryption = models.SmallIntegerField()

#     class Meta:
#         managed = False
#         db_table = 'store'


# class TaskInstance(models.Model):
#     uid = models.CharField(primary_key=True, max_length=32)
#     activity_instance_uid = models.CharField(
#         max_length=32, blank=True, null=True)
#     activity_uid = models.ForeignKey(
#         Activity, models.DO_NOTHING, db_column='activity_uid', blank=True, null=True)
#     token_uid = models.CharField(max_length=32, blank=True, null=True)
#     date_entered = models.DateTimeField(blank=True, null=True)
#     task_uid = models.CharField(max_length=32, blank=True, null=True)
#     swimlane = models.CharField(max_length=50, blank=True, null=True)
#     date_started = models.DateTimeField(blank=True, null=True)
#     date_completed = models.DateTimeField(blank=True, null=True)
#     actor = models.CharField(max_length=50, blank=True, null=True)
#     # Field renamed because it ended with '_'.
#     group_field = models.CharField(
#         db_column='group_', max_length=50, blank=True, null=True)
#     actual_cost = models.IntegerField(blank=True, null=True)
#     # Field renamed because it ended with '_'.
#     variables_field = models.TextField(
#         db_column='variables_', blank=True, null=True)
#     initiating_rec = models.CharField(max_length=65, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'task_instance'


# class TaskLastActor(models.Model):
#     task_uid = models.CharField(max_length=32, blank=True, null=True)
#     last_actor = models.CharField(max_length=50, blank=True, null=True)
#     ts = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'task_last_actor'


# class TmpTable(models.Model):
#     uid = models.CharField(max_length=50, blank=True, null=True)
#     recordtypename = models.CharField(max_length=50, blank=True, null=True)
#     noofrecords = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'tmp_table'


# class ToDo(models.Model):
#     uid = models.CharField(primary_key=True, max_length=32)
#     node_uid = models.CharField(max_length=65)
#     owner_uid = models.CharField(max_length=32)
#     assignee_uid = models.CharField(max_length=32)
#     start_date = models.DateTimeField()
#     due_date = models.DateTimeField()
#     subject = models.CharField(max_length=255, blank=True, null=True)
#     parent_uid = models.CharField(max_length=32, blank=True, null=True)
#     instruction = models.TextField(blank=True, null=True)
#     is_important = models.SmallIntegerField()
#     is_missed = models.SmallIntegerField()
#     is_completed = models.SmallIntegerField()
#     date_completed = models.DateTimeField(blank=True, null=True)
#     is_reassigned = models.SmallIntegerField()
#     date_reassignment = models.DateTimeField(blank=True, null=True)
#     es_duration = models.SmallIntegerField()
#     ac_duration = models.SmallIntegerField()
#     acl_uid = models.CharField(max_length=32, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'to_do'


# class ToDoCc(models.Model):
#     td_cc_uid = models.CharField(max_length=32)
#     principal_uid = models.CharField(max_length=32)

#     class Meta:
#         managed = False
#         db_table = 'to_do_cc'


# class Token(models.Model):
#     uid = models.CharField(primary_key=True, max_length=32)
#     activity_instance_uid = models.CharField(
#         max_length=32, blank=True, null=True)
#     # Field renamed because it ended with '_'.
#     variables_field = models.TextField(
#         db_column='variables_', blank=True, null=True)
#     parent_token_uid = models.ForeignKey(
#         'self', models.DO_NOTHING, db_column='parent_token_uid', blank=True, null=True)
#     current_activity_uid = models.ForeignKey(
#         Activity, models.DO_NOTHING, db_column='current_activity_uid', blank=True, null=True)
#     current_action_uid = models.CharField(max_length=32, blank=True, null=True)
#     current_actor = models.CharField(max_length=50, blank=True, null=True)
#     current_group = models.CharField(max_length=50, blank=True, null=True)
#     state = models.SmallIntegerField(blank=True, null=True)
#     completed_actions = models.TextField(blank=True, null=True)
#     date_entered = models.DateTimeField(blank=True, null=True)
#     date_started = models.DateTimeField(blank=True, null=True)
#     date_executed = models.DateTimeField(blank=True, null=True)
#     date_completed = models.DateTimeField(blank=True, null=True)
#     date_exited = models.DateTimeField(blank=True, null=True)
#     date_aborted = models.DateTimeField(blank=True, null=True)
#     sibling_size = models.IntegerField(blank=True, null=True)
#     actual_cost = models.IntegerField(blank=True, null=True)
#     activity_date_started = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'token'


# class UserPreferences(models.Model):
#     principal_uid = models.OneToOneField(
#         Principal, models.DO_NOTHING, db_column='principal_uid', primary_key=True)
#     pref_1 = models.TextField(blank=True, null=True)
#     pref_2 = models.TextField(blank=True, null=True)
#     pref_3 = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'user_preferences'


# class UserVerificationToken(models.Model):
#     token = models.CharField(max_length=255)
#     principal_uid = models.CharField(max_length=255)
#     expiry_date = models.DateTimeField(blank=True, null=True)
#     is_confirm = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'user_verification_token'


# class VisualSignature(models.Model):
#     uid = models.CharField(primary_key=True, max_length=32)
#     principal_uid = models.ForeignKey(
#         Principal, models.DO_NOTHING, db_column='principal_uid')
#     signature = models.BinaryField()
#     signature_timestamp = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'visual_signature'


# class WaitInstance(models.Model):
#     uid = models.CharField(primary_key=True, max_length=32)
#     token_uid = models.CharField(max_length=32, blank=True, null=True)
#     activity_uid = models.ForeignKey(
#         Activity, models.DO_NOTHING, db_column='activity_uid', blank=True, null=True)
#     activity_instance_uid = models.CharField(
#         max_length=32, blank=True, null=True)
#     wait_uid = models.CharField(max_length=32, blank=True, null=True)
#     fixed_date = models.DateTimeField(blank=True, null=True)
#     use_dynamic_date = models.IntegerField(blank=True, null=True)
#     dynamic_date = models.TextField(blank=True, null=True)
#     lead_time = models.IntegerField(blank=True, null=True)
#     on_evaluate = models.TextField(blank=True, null=True)
#     date_started = models.DateTimeField(blank=True, null=True)
#     date_completed = models.DateTimeField(blank=True, null=True)
#     state = models.SmallIntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'wait_instance'
