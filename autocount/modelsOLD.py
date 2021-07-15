# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Adj(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', unique=True, max_length=20)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    remark1 = models.CharField(db_column='Remark1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark2 = models.CharField(db_column='Remark2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark3 = models.CharField(db_column='Remark3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark4 = models.CharField(db_column='Remark4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    printcount = models.SmallIntegerField(db_column='PrintCount')  # Field name made lowercase.
    cancelled = models.CharField(db_column='Cancelled', max_length=1)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    createduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    externallink = models.TextField(db_column='ExternalLink', blank=True, null=True)  # Field name made lowercase.
    refdocno = models.CharField(db_column='RefDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    cansync = models.CharField(db_column='CanSync', max_length=1)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.

    class Meta:
 
        db_table = 'ADJ'


class Adjdtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    numbering = models.CharField(db_column='Numbering', max_length=6, blank=True, null=True)  # Field name made lowercase.
    itemcode = models.ForeignKey('Itemuom', models.DO_NOTHING, db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    location = models.ForeignKey('Location', models.DO_NOTHING, db_column='Location', blank=True, null=True)  # Field name made lowercase.
    batchno = models.ForeignKey('Itembatch', models.DO_NOTHING, db_column='BatchNo', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    furtherdescription = models.TextField(db_column='FurtherDescription', blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey('Dept', models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    uom = models.ForeignKey('Itemuom', models.DO_NOTHING, db_column='UOM', blank=True, null=True)  # Field name made lowercase.
    unitcost = models.DecimalField(db_column='UnitCost', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    printout = models.CharField(db_column='PrintOut', max_length=1)  # Field name made lowercase.
    serialnolist = models.TextField(db_column='SerialNoList', blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.

    class Meta:
 
        db_table = 'ADJDTL'


class Aorprocessing(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    fromdtlkey = models.BigIntegerField(db_column='FromDtlKey', blank=True, null=True)  # Field name made lowercase.
    fromdockey = models.BigIntegerField(db_column='FromDocKey', blank=True, null=True)  # Field name made lowercase.
    aodockey = models.BigIntegerField(db_column='AODocKey', blank=True, null=True)  # Field name made lowercase.
    aodocno = models.CharField(db_column='AODocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    aodtlkey = models.BigIntegerField(db_column='AODtlKey', blank=True, null=True)  # Field name made lowercase.
    itemcode = models.ForeignKey('Item', models.DO_NOTHING, db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    furtherdescription = models.TextField(db_column='FurtherDescription', blank=True, null=True)  # Field name made lowercase.
    estimateddeliverydate = models.CharField(db_column='EstimatedDeliveryDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    location = models.ForeignKey('Location', models.DO_NOTHING, db_column='Location', blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey('Dept', models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    requestqty = models.DecimalField(db_column='RequestQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    createduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    fromdoctype = models.CharField(db_column='FromDocType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
    deliverydate = models.DateTimeField(db_column='DeliveryDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'AORProcessing'


class Apcn(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', unique=True, max_length=20)  # Field name made lowercase.
    creditorcode = models.ForeignKey('Branch', models.DO_NOTHING, db_column='CreditorCode')  # Field name made lowercase.
    journaltype = models.ForeignKey('Journal', models.DO_NOTHING, db_column='JournalType')  # Field name made lowercase.
    cntype = models.ForeignKey('Cntype', models.DO_NOTHING, db_column='CNType', blank=True, null=True)  # Field name made lowercase.
    ref = models.CharField(db_column='Ref', max_length=40, blank=True, null=True)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=80, blank=True, null=True)  # Field name made lowercase.
    currencycode = models.ForeignKey('Currency', models.DO_NOTHING, db_column='CurrencyCode')  # Field name made lowercase.
    currencyrate = models.DecimalField(db_column='CurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtotal = models.DecimalField(db_column='LocalTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtax = models.DecimalField(db_column='LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nettotal = models.DecimalField(db_column='NetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localnettotal = models.DecimalField(db_column='LocalNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    knockoffamt = models.DecimalField(db_column='KnockOffAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    refundamt = models.DecimalField(db_column='RefundAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cancelled = models.CharField(db_column='Cancelled', max_length=1)  # Field name made lowercase.
    isjournal = models.CharField(db_column='IsJournal', max_length=1)  # Field name made lowercase.
    jekey = models.BigIntegerField(db_column='JEKey', blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    externallink = models.TextField(db_column='ExternalLink', blank=True, null=True)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    createduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    sourcetype = models.CharField(db_column='SourceType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    sourcekey = models.BigIntegerField(db_column='SourceKey', blank=True, null=True)  # Field name made lowercase.
    revaluerate = models.DecimalField(db_column='RevalueRate', max_digits=19, decimal_places=12, blank=True, null=True)  # Field name made lowercase.
    totalrevaluegainloss = models.DecimalField(db_column='TotalRevalueGainLoss', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    refno2 = models.CharField(db_column='RefNo2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    extax = models.DecimalField(db_column='ExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localextax = models.DecimalField(db_column='LocalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    total2 = models.DecimalField(db_column='Total2', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtotal2 = models.DecimalField(db_column='LocalTotal2', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    branchcode = models.ForeignKey('Branch', models.DO_NOTHING, db_column='BranchCode', blank=True, null=True)  # Field name made lowercase.
    suppliercnno = models.CharField(db_column='SupplierCNNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    totaxcurrencyrate = models.DecimalField(db_column='ToTaxCurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    taxdocno = models.CharField(db_column='TaxDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    supplierinvoiceno = models.CharField(db_column='SupplierInvoiceNo', max_length=40, blank=True, null=True)  # Field name made lowercase.
    reason = models.CharField(db_column='Reason', max_length=80, blank=True, null=True)  # Field name made lowercase.
    inclusivetax = models.CharField(db_column='InclusiveTax', max_length=1)  # Field name made lowercase.
    taxableamt = models.DecimalField(db_column='TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    gltrxid = models.BigIntegerField(db_column='GLTrxID', blank=True, null=True)  # Field name made lowercase.
    taxdate = models.DateTimeField(db_column='TaxDate', blank=True, null=True)  # Field name made lowercase.
    roundingmethod = models.IntegerField(db_column='RoundingMethod')  # Field name made lowercase.
    localtaxableamt = models.DecimalField(db_column='LocalTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytax = models.DecimalField(db_column='TaxCurrencyTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxableamt = models.DecimalField(db_column='TaxCurrencyTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    docdate2 = models.DateTimeField(db_column='DocDate2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'APCN'


class Apcndtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey', blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    accno = models.ForeignKey('Glmast', models.DO_NOTHING, db_column='AccNo', blank=True, null=True)  # Field name made lowercase.
    toaccountrate = models.DecimalField(db_column='ToAccountRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey('Dept', models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='TaxType', blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtax = models.DecimalField(db_column='LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    netamount = models.DecimalField(db_column='NetAmount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localnetamount = models.DecimalField(db_column='LocalNetAmount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unappliedamount = models.DecimalField(db_column='UnappliedAmount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localunappliedamount = models.DecimalField(db_column='LocalUnappliedAmount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    knockoffamount = models.DecimalField(db_column='KnockOffAmount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxableamt = models.DecimalField(db_column='TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localsubtotal = models.DecimalField(db_column='LocalSubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxpermitno = models.CharField(db_column='TaxPermitNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    taxadjustment = models.DecimalField(db_column='TaxAdjustment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sourcedtlkey = models.BigIntegerField(db_column='SourceDtlKey', blank=True, null=True)  # Field name made lowercase.
    taxrate = models.DecimalField(db_column='TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    localtaxadjustment = models.DecimalField(db_column='LocalTaxAdjustment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sourcedtltype = models.CharField(db_column='SourceDtlType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    localtaxableamt = models.DecimalField(db_column='LocalTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytax = models.DecimalField(db_column='TaxCurrencyTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxableamt = models.DecimalField(db_column='TaxCurrencyTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    supplypurchase = models.CharField(db_column='SupplyPurchase', max_length=1)  # Field name made lowercase.
    tariffcode = models.ForeignKey('Tariff', models.DO_NOTHING, db_column='TariffCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'APCNDTL'


class Apcnknockoff(models.Model):
    knockoffkey = models.BigIntegerField(db_column='KnockOffKey', primary_key=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    knockoffdoctype = models.CharField(db_column='KnockOffDocType', max_length=2)  # Field name made lowercase.
    knockoffdockey = models.BigIntegerField(db_column='KnockOffDocKey')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    gainlossdate = models.DateTimeField(db_column='GainLossDate')  # Field name made lowercase.
    revalue = models.CharField(db_column='Revalue', max_length=1, blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey('Dept', models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    useprojdept = models.CharField(db_column='UseProjDept', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fcrevaluekey = models.BigIntegerField(db_column='FCRevalueKey', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'APCNKnockOff'


class Apcnknockoffdetail(models.Model):
    knockoffkey = models.BigIntegerField(db_column='KnockOffKey', primary_key=True)  # Field name made lowercase.
    knockoffdtlkey = models.BigIntegerField(db_column='KnockOffDtlKey')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localcnamt = models.DecimalField(db_column='LocalCNAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localinvoiceamt = models.DecimalField(db_column='LocalInvoiceAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'APCNKnockOffDetail'
        unique_together = (('knockoffkey', 'knockoffdtlkey'),)


class Apcontraknockoff(models.Model):
    knockoffkey = models.BigIntegerField(db_column='KnockOffKey', primary_key=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    knockoffdoctype = models.CharField(db_column='KnockOffDocType', max_length=2)  # Field name made lowercase.
    knockoffdockey = models.BigIntegerField(db_column='KnockOffDocKey')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    gainlossdate = models.DateTimeField(db_column='GainLossDate')  # Field name made lowercase.
    revalue = models.CharField(db_column='Revalue', max_length=1, blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey('Dept', models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    useprojdept = models.CharField(db_column='UseProjDept', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fcrevaluekey = models.BigIntegerField(db_column='FCRevalueKey', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'APContraKnockOff'


class Apcontraknockoffdetail(models.Model):
    knockoffkey = models.BigIntegerField(db_column='KnockOffKey', primary_key=True)  # Field name made lowercase.
    knockoffdtlkey = models.BigIntegerField(db_column='KnockOffDtlKey')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localcontraamt = models.DecimalField(db_column='LocalContraAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localinvoiceamt = models.DecimalField(db_column='LocalInvoiceAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'APContraKnockOffDetail'
        unique_together = (('knockoffkey', 'knockoffdtlkey'),)


class Apdn(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', unique=True, max_length=20)  # Field name made lowercase.
    creditorcode = models.ForeignKey('Branch', models.DO_NOTHING, db_column='CreditorCode')  # Field name made lowercase.
    journaltype = models.ForeignKey('Journal', models.DO_NOTHING, db_column='JournalType')  # Field name made lowercase.
    dntype = models.ForeignKey('Dntype', models.DO_NOTHING, db_column='DNType', blank=True, null=True)  # Field name made lowercase.
    ref = models.CharField(db_column='Ref', max_length=40, blank=True, null=True)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    displayterm = models.ForeignKey('Terms', models.DO_NOTHING, db_column='DisplayTerm')  # Field name made lowercase.
    duedate = models.DateTimeField(db_column='DueDate')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=80, blank=True, null=True)  # Field name made lowercase.
    purchaseagent = models.ForeignKey('Purchaseagent', models.DO_NOTHING, db_column='PurchaseAgent', blank=True, null=True)  # Field name made lowercase.
    currencycode = models.ForeignKey('Currency', models.DO_NOTHING, db_column='CurrencyCode')  # Field name made lowercase.
    currencyrate = models.DecimalField(db_column='CurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtotal = models.DecimalField(db_column='LocalTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtax = models.DecimalField(db_column='LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nettotal = models.DecimalField(db_column='NetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localnettotal = models.DecimalField(db_column='LocalNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    paymentamt = models.DecimalField(db_column='PaymentAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localpaymentamt = models.DecimalField(db_column='LocalPaymentAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    outstanding = models.DecimalField(db_column='Outstanding', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cancelled = models.CharField(db_column='Cancelled', max_length=1)  # Field name made lowercase.
    isjournal = models.CharField(db_column='IsJournal', max_length=1)  # Field name made lowercase.
    jekey = models.BigIntegerField(db_column='JEKey', blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    externallink = models.TextField(db_column='ExternalLink', blank=True, null=True)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    createduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    sourcetype = models.CharField(db_column='SourceType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    sourcekey = models.BigIntegerField(db_column='SourceKey', blank=True, null=True)  # Field name made lowercase.
    forecastduedate = models.DateTimeField(db_column='ForecastDueDate', blank=True, null=True)  # Field name made lowercase.
    revaluerate = models.DecimalField(db_column='RevalueRate', max_digits=19, decimal_places=12, blank=True, null=True)  # Field name made lowercase.
    totalrevaluegainloss = models.DecimalField(db_column='TotalRevalueGainLoss', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    refno2 = models.CharField(db_column='RefNo2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    agingdate = models.DateTimeField(db_column='AgingDate', blank=True, null=True)  # Field name made lowercase.
    extax = models.DecimalField(db_column='ExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localextax = models.DecimalField(db_column='LocalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    total2 = models.DecimalField(db_column='Total2', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtotal2 = models.DecimalField(db_column='LocalTotal2', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    branchcode = models.ForeignKey('Branch', models.DO_NOTHING, db_column='BranchCode', blank=True, null=True)  # Field name made lowercase.
    supplierdnno = models.CharField(db_column='SupplierDNNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    totaxcurrencyrate = models.DecimalField(db_column='ToTaxCurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    taxdocno = models.CharField(db_column='TaxDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    supplierinvoiceno = models.CharField(db_column='SupplierInvoiceNo', max_length=40, blank=True, null=True)  # Field name made lowercase.
    reason = models.CharField(db_column='Reason', max_length=80, blank=True, null=True)  # Field name made lowercase.
    inclusivetax = models.CharField(db_column='InclusiveTax', max_length=1)  # Field name made lowercase.
    taxableamt = models.DecimalField(db_column='TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    gltrxid = models.BigIntegerField(db_column='GLTrxID', blank=True, null=True)  # Field name made lowercase.
    taxdate = models.DateTimeField(db_column='TaxDate', blank=True, null=True)  # Field name made lowercase.
    roundingmethod = models.IntegerField(db_column='RoundingMethod')  # Field name made lowercase.
    localtaxableamt = models.DecimalField(db_column='LocalTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytax = models.DecimalField(db_column='TaxCurrencyTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxableamt = models.DecimalField(db_column='TaxCurrencyTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    docdate2 = models.DateTimeField(db_column='DocDate2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'APDN'


class Apdndtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey', blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    accno = models.ForeignKey('Glmast', models.DO_NOTHING, db_column='AccNo', blank=True, null=True)  # Field name made lowercase.
    toaccountrate = models.DecimalField(db_column='ToAccountRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey('Dept', models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='TaxType', blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtax = models.DecimalField(db_column='LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    netamount = models.DecimalField(db_column='NetAmount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localnetamount = models.DecimalField(db_column='LocalNetAmount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    knockoffamount = models.DecimalField(db_column='KnockOffAmount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxableamt = models.DecimalField(db_column='TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localsubtotal = models.DecimalField(db_column='LocalSubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxpermitno = models.CharField(db_column='TaxPermitNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    taxadjustment = models.DecimalField(db_column='TaxAdjustment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sourcedtlkey = models.BigIntegerField(db_column='SourceDtlKey', blank=True, null=True)  # Field name made lowercase.
    taxrate = models.DecimalField(db_column='TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    localtaxadjustment = models.DecimalField(db_column='LocalTaxAdjustment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sourcedtltype = models.CharField(db_column='SourceDtlType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    localtaxableamt = models.DecimalField(db_column='LocalTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytax = models.DecimalField(db_column='TaxCurrencyTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxableamt = models.DecimalField(db_column='TaxCurrencyTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    supplypurchase = models.CharField(db_column='SupplyPurchase', max_length=1)  # Field name made lowercase.
    tariffcode = models.ForeignKey('Tariff', models.DO_NOTHING, db_column='TariffCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'APDNDTL'


class Apdeposit(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', unique=True, max_length=20)  # Field name made lowercase.
    creditorcode = models.ForeignKey('Glmast', models.DO_NOTHING, db_column='CreditorCode', blank=True, null=True)  # Field name made lowercase.
    creditorname = models.CharField(db_column='CreditorName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    invaddr1 = models.CharField(db_column='InvAddr1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr2 = models.CharField(db_column='InvAddr2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr3 = models.CharField(db_column='InvAddr3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr4 = models.CharField(db_column='InvAddr4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    phone1 = models.CharField(db_column='Phone1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    fax1 = models.CharField(db_column='Fax1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    attention = models.CharField(db_column='Attention', max_length=40, blank=True, null=True)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=40, blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey('Dept', models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    depositpaymentmethod = models.ForeignKey('Paymentmethod', models.DO_NOTHING, db_column='DepositPaymentMethod')  # Field name made lowercase.
    currencycode = models.ForeignKey('Currency', models.DO_NOTHING, db_column='CurrencyCode')  # Field name made lowercase.
    todepositrate = models.DecimalField(db_column='ToDepositRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    tohomerate = models.DecimalField(db_column='ToHomeRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    paymentamt = models.DecimalField(db_column='PaymentAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    transferedamt = models.DecimalField(db_column='TransferedAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cbkey = models.BigIntegerField(db_column='CBKey', blank=True, null=True)  # Field name made lowercase.
    hasforfeit = models.CharField(db_column='HasForfeit', max_length=1)  # Field name made lowercase.
    forfeiteddate = models.DateTimeField(db_column='ForfeitedDate', blank=True, null=True)  # Field name made lowercase.
    forfeitedamt = models.DecimalField(db_column='ForfeitedAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    forfeitedaccno = models.ForeignKey('Glmast', models.DO_NOTHING, db_column='ForfeitedAccNo', blank=True, null=True)  # Field name made lowercase.
    hasrefund = models.CharField(db_column='HasRefund', max_length=1)  # Field name made lowercase.
    refunddate = models.DateTimeField(db_column='RefundDate', blank=True, null=True)  # Field name made lowercase.
    refunddocno = models.CharField(db_column='RefundDocNo', max_length=20)  # Field name made lowercase.
    refundname = models.CharField(db_column='RefundName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    refundamt = models.DecimalField(db_column='RefundAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    refundcbkey = models.BigIntegerField(db_column='RefundCBKey', blank=True, null=True)  # Field name made lowercase.
    outstanding = models.DecimalField(db_column='Outstanding', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    printcount = models.SmallIntegerField(db_column='PrintCount')  # Field name made lowercase.
    cancelled = models.CharField(db_column='Cancelled', max_length=1)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    externallink = models.TextField(db_column='ExternalLink', blank=True, null=True)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    createduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    sourcetype = models.CharField(db_column='SourceType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    sourcekey = models.BigIntegerField(db_column='SourceKey', blank=True, null=True)  # Field name made lowercase.
    gltrxid = models.BigIntegerField(db_column='GLTrxID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'APDeposit'


class Apdepositdtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    paymentmethod = models.ForeignKey('Paymentmethod', models.DO_NOTHING, db_column='PaymentMethod')  # Field name made lowercase.
    paymentby = models.CharField(db_column='PaymentBy', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tobankrate = models.DecimalField(db_column='ToBankRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    chequeno = models.CharField(db_column='ChequeNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    floatday = models.SmallIntegerField(db_column='FloatDay', blank=True, null=True)  # Field name made lowercase.
    bankcharge = models.DecimalField(db_column='BankCharge', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    paymentamt = models.DecimalField(db_column='PaymentAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    isrchq = models.CharField(db_column='IsRCHQ', max_length=1)  # Field name made lowercase.
    rchqdate = models.DateTimeField(db_column='RCHQDate', blank=True, null=True)  # Field name made lowercase.
    bankchargedtlkey = models.BigIntegerField(db_column='BankChargeDtlKey', blank=True, null=True)  # Field name made lowercase.
    bankchargeprojno = models.ForeignKey('Project', models.DO_NOTHING, db_column='BankChargeProjNo', blank=True, null=True)  # Field name made lowercase.
    bankchargedeptno = models.ForeignKey('Dept', models.DO_NOTHING, db_column='BankChargeDeptNo', blank=True, null=True)  # Field name made lowercase.
    bankchargetaxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='BankChargeTaxType', blank=True, null=True)  # Field name made lowercase.
    bankchargetaxrate = models.DecimalField(db_column='BankChargeTaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    bankchargetax = models.DecimalField(db_column='BankChargeTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    bankchargetaxrefno = models.CharField(db_column='BankChargeTaxRefNo', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'APDepositDTL'


class Apinvoice(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', unique=True, max_length=20)  # Field name made lowercase.
    creditorcode = models.ForeignKey('Branch', models.DO_NOTHING, db_column='CreditorCode')  # Field name made lowercase.
    journaltype = models.ForeignKey('Journal', models.DO_NOTHING, db_column='JournalType')  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    displayterm = models.ForeignKey('Terms', models.DO_NOTHING, db_column='DisplayTerm')  # Field name made lowercase.
    duedate = models.DateTimeField(db_column='DueDate')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=80, blank=True, null=True)  # Field name made lowercase.
    purchaseagent = models.ForeignKey('Purchaseagent', models.DO_NOTHING, db_column='PurchaseAgent', blank=True, null=True)  # Field name made lowercase.
    currencycode = models.ForeignKey('Currency', models.DO_NOTHING, db_column='CurrencyCode')  # Field name made lowercase.
    currencyrate = models.DecimalField(db_column='CurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtotal = models.DecimalField(db_column='LocalTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtax = models.DecimalField(db_column='LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nettotal = models.DecimalField(db_column='NetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localnettotal = models.DecimalField(db_column='LocalNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    paymentamt = models.DecimalField(db_column='PaymentAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localpaymentamt = models.DecimalField(db_column='LocalPaymentAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    outstanding = models.DecimalField(db_column='Outstanding', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cancelled = models.CharField(db_column='Cancelled', max_length=1)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    externallink = models.TextField(db_column='ExternalLink', blank=True, null=True)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    createduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    sourcetype = models.CharField(db_column='SourceType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    sourcekey = models.BigIntegerField(db_column='SourceKey', blank=True, null=True)  # Field name made lowercase.
    forecastduedate = models.DateTimeField(db_column='ForecastDueDate', blank=True, null=True)  # Field name made lowercase.
    revaluerate = models.DecimalField(db_column='RevalueRate', max_digits=19, decimal_places=12, blank=True, null=True)  # Field name made lowercase.
    totalrevaluegainloss = models.DecimalField(db_column='TotalRevalueGainLoss', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    refno2 = models.CharField(db_column='RefNo2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    agingdate = models.DateTimeField(db_column='AgingDate', blank=True, null=True)  # Field name made lowercase.
    extax = models.DecimalField(db_column='ExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localextax = models.DecimalField(db_column='LocalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    total2 = models.DecimalField(db_column='Total2', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtotal2 = models.DecimalField(db_column='LocalTotal2', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    branchcode = models.ForeignKey('Branch', models.DO_NOTHING, db_column='BranchCode', blank=True, null=True)  # Field name made lowercase.
    supplierinvoiceno = models.CharField(db_column='SupplierInvoiceNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    totaxcurrencyrate = models.DecimalField(db_column='ToTaxCurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    taxdocno = models.CharField(db_column='TaxDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    inclusivetax = models.CharField(db_column='InclusiveTax', max_length=1)  # Field name made lowercase.
    taxableamt = models.DecimalField(db_column='TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    gltrxid = models.BigIntegerField(db_column='GLTrxID', blank=True, null=True)  # Field name made lowercase.
    referatmsjedockey = models.BigIntegerField(db_column='ReferATMSJEDocKey', blank=True, null=True)  # Field name made lowercase.
    referatmsjedocno = models.CharField(db_column='ReferATMSJEDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    referatmsjeisnontaxablesupply = models.CharField(db_column='ReferATMSJEIsNonTaxableSupply', max_length=1, blank=True, null=True)  # Field name made lowercase.
    taxdate = models.DateTimeField(db_column='TaxDate', blank=True, null=True)  # Field name made lowercase.
    roundingmethod = models.IntegerField(db_column='RoundingMethod')  # Field name made lowercase.
    localtaxableamt = models.DecimalField(db_column='LocalTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytax = models.DecimalField(db_column='TaxCurrencyTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxableamt = models.DecimalField(db_column='TaxCurrencyTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    docdate2 = models.DateTimeField(db_column='DocDate2', blank=True, null=True)  # Field name made lowercase.
    referisjeispayment = models.CharField(db_column='ReferISJEIsPayment', max_length=1, blank=True, null=True)  # Field name made lowercase.
    referisjedockey = models.BigIntegerField(db_column='ReferISJEDocKey', blank=True, null=True)  # Field name made lowercase.
    referisjedocno = models.CharField(db_column='ReferISJEDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    referisjeisnontaxablesupply = models.CharField(db_column='ReferISJEIsNonTaxableSupply', max_length=1, blank=True, null=True)  # Field name made lowercase.
    refercajeispayment = models.CharField(db_column='ReferCAJEIsPayment', max_length=1, blank=True, null=True)  # Field name made lowercase.
    refercajedockey = models.BigIntegerField(db_column='ReferCAJEDocKey', blank=True, null=True)  # Field name made lowercase.
    refercajedocno = models.CharField(db_column='ReferCAJEDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    refersstisjedockey = models.BigIntegerField(db_column='ReferSSTISJEDocKey', blank=True, null=True)  # Field name made lowercase.
    refersstisjedocno = models.CharField(db_column='ReferSSTISJEDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    refersstsdjedockey = models.BigIntegerField(db_column='ReferSSTSDJEDocKey', blank=True, null=True)  # Field name made lowercase.
    refersstsdjedocno = models.CharField(db_column='ReferSSTSDJEDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'APInvoice'


class Apinvoicedtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey', blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    accno = models.ForeignKey('Glmast', models.DO_NOTHING, db_column='AccNo', blank=True, null=True)  # Field name made lowercase.
    toaccountrate = models.DecimalField(db_column='ToAccountRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey('Dept', models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='TaxType', blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtax = models.DecimalField(db_column='LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    netamount = models.DecimalField(db_column='NetAmount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localnetamount = models.DecimalField(db_column='LocalNetAmount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    knockoffamount = models.DecimalField(db_column='KnockOffAmount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxableamt = models.DecimalField(db_column='TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localsubtotal = models.DecimalField(db_column='LocalSubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxpermitno = models.CharField(db_column='TaxPermitNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    taxadjustment = models.DecimalField(db_column='TaxAdjustment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sourcedtlkey = models.BigIntegerField(db_column='SourceDtlKey', blank=True, null=True)  # Field name made lowercase.
    taxrate = models.DecimalField(db_column='TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    localtaxadjustment = models.DecimalField(db_column='LocalTaxAdjustment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sourcedtltype = models.CharField(db_column='SourceDtlType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    localtaxableamt = models.DecimalField(db_column='LocalTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytax = models.DecimalField(db_column='TaxCurrencyTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxableamt = models.DecimalField(db_column='TaxCurrencyTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tariffcode = models.ForeignKey('Tariff', models.DO_NOTHING, db_column='TariffCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'APInvoiceDTL'


class Appayment(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', unique=True, max_length=20)  # Field name made lowercase.
    creditorcode = models.ForeignKey('Branch', models.DO_NOTHING, db_column='CreditorCode')  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=80, blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey('Dept', models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    currencycode = models.ForeignKey('Currency', models.DO_NOTHING, db_column='CurrencyCode')  # Field name made lowercase.
    tocreditorrate = models.DecimalField(db_column='ToCreditorRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    tohomerate = models.DecimalField(db_column='ToHomeRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    paymentamt = models.DecimalField(db_column='PaymentAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localpaymentamt = models.DecimalField(db_column='LocalPaymentAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    knockoffamt = models.DecimalField(db_column='KnockOffAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localunappliedamount = models.DecimalField(db_column='LocalUnappliedAmount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    refundamt = models.DecimalField(db_column='RefundAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cbkey = models.BigIntegerField(db_column='CBKey', blank=True, null=True)  # Field name made lowercase.
    cancelled = models.CharField(db_column='Cancelled', max_length=1)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    externallink = models.TextField(db_column='ExternalLink', blank=True, null=True)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    createduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    sourcetype = models.CharField(db_column='SourceType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    sourcekey = models.BigIntegerField(db_column='SourceKey', blank=True, null=True)  # Field name made lowercase.
    revaluerate = models.DecimalField(db_column='RevalueRate', max_digits=19, decimal_places=12, blank=True, null=True)  # Field name made lowercase.
    totalrevaluegainloss = models.DecimalField(db_column='TotalRevalueGainLoss', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    handoverdate = models.DateTimeField(db_column='HandOverDate', blank=True, null=True)  # Field name made lowercase.
    refercndockey = models.BigIntegerField(db_column='ReferCNDocKey', blank=True, null=True)  # Field name made lowercase.
    refercndocdate = models.DateTimeField(db_column='ReferCNDocDate', blank=True, null=True)  # Field name made lowercase.
    refercndocno = models.CharField(db_column='ReferCNDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    branchcode = models.ForeignKey('Branch', models.DO_NOTHING, db_column='BranchCode', blank=True, null=True)  # Field name made lowercase.
    docno2 = models.CharField(db_column='DocNo2', max_length=25, blank=True, null=True)  # Field name made lowercase.
    gltrxid = models.BigIntegerField(db_column='GLTrxID', blank=True, null=True)  # Field name made lowercase.
    referisjedockey = models.BigIntegerField(db_column='ReferISJEDocKey', blank=True, null=True)  # Field name made lowercase.
    referisjedocno = models.CharField(db_column='ReferISJEDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    referisjeisnontaxablesupply = models.CharField(db_column='ReferISJEIsNonTaxableSupply', max_length=1, blank=True, null=True)  # Field name made lowercase.
    refercnreason = models.CharField(db_column='ReferCNReason', max_length=80, blank=True, null=True)  # Field name made lowercase.
    refercajedockey = models.BigIntegerField(db_column='ReferCAJEDocKey', blank=True, null=True)  # Field name made lowercase.
    refercajedocno = models.CharField(db_column='ReferCAJEDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'APPayment'


class Appaymentdtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    paymentmethod = models.ForeignKey('Paymentmethod', models.DO_NOTHING, db_column='PaymentMethod')  # Field name made lowercase.
    paymentby = models.CharField(db_column='PaymentBy', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tobankrate = models.DecimalField(db_column='ToBankRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    chequeno = models.CharField(db_column='ChequeNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    floatday = models.SmallIntegerField(db_column='FloatDay', blank=True, null=True)  # Field name made lowercase.
    bankcharge = models.DecimalField(db_column='BankCharge', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    paymentamt = models.DecimalField(db_column='PaymentAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    creditorpaymentamt = models.DecimalField(db_column='CreditorPaymentAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    isrchq = models.CharField(db_column='IsRCHQ', max_length=1)  # Field name made lowercase.
    rchqdate = models.DateTimeField(db_column='RCHQDate', blank=True, null=True)  # Field name made lowercase.
    depositdockey = models.BigIntegerField(db_column='DepositDocKey', blank=True, null=True)  # Field name made lowercase.
    bankchargedtlkey = models.BigIntegerField(db_column='BankChargeDtlKey', blank=True, null=True)  # Field name made lowercase.
    localpaymentamt = models.DecimalField(db_column='LocalPaymentAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    withholdingtax = models.DecimalField(db_column='WithholdingTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    bankchargeprojno = models.ForeignKey('Project', models.DO_NOTHING, db_column='BankChargeProjNo', blank=True, null=True)  # Field name made lowercase.
    bankchargedeptno = models.ForeignKey('Dept', models.DO_NOTHING, db_column='BankChargeDeptNo', blank=True, null=True)  # Field name made lowercase.
    bankchargetaxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='BankChargeTaxType', blank=True, null=True)  # Field name made lowercase.
    bankchargetaxrate = models.DecimalField(db_column='BankChargeTaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    bankchargetax = models.DecimalField(db_column='BankChargeTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    bankchargetaxrefno = models.CharField(db_column='BankChargeTaxRefNo', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'APPaymentDTL'


class Appaymentknockoff(models.Model):
    knockoffkey = models.BigIntegerField(db_column='KnockOffKey', primary_key=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    knockoffdoctype = models.CharField(db_column='KnockOffDocType', max_length=2)  # Field name made lowercase.
    knockoffdockey = models.BigIntegerField(db_column='KnockOffDocKey')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    gainlossdate = models.DateTimeField(db_column='GainLossDate')  # Field name made lowercase.
    revalue = models.CharField(db_column='Revalue', max_length=1, blank=True, null=True)  # Field name made lowercase.
    discountamt = models.DecimalField(db_column='DiscountAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey('Dept', models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    useprojdept = models.CharField(db_column='UseProjDept', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fcrevaluekey = models.BigIntegerField(db_column='FCRevalueKey', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'APPaymentKnockOff'


class Appaymentknockoffdetail(models.Model):
    knockoffkey = models.BigIntegerField(db_column='KnockOffKey', primary_key=True)  # Field name made lowercase.
    knockoffdtlkey = models.BigIntegerField(db_column='KnockOffDtlKey')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localpaymentamt = models.DecimalField(db_column='LocalPaymentAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localinvoiceamt = models.DecimalField(db_column='LocalInvoiceAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'APPaymentKnockOffDetail'
        unique_together = (('knockoffkey', 'knockoffdtlkey'),)


class Aprefund(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', unique=True, max_length=20)  # Field name made lowercase.
    creditorcode = models.ForeignKey('Branch', models.DO_NOTHING, db_column='CreditorCode')  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=80, blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey('Dept', models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    currencycode = models.ForeignKey('Currency', models.DO_NOTHING, db_column='CurrencyCode')  # Field name made lowercase.
    tocreditorrate = models.DecimalField(db_column='ToCreditorRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    tohomerate = models.DecimalField(db_column='ToHomeRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    paymentamt = models.DecimalField(db_column='PaymentAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localpaymentamt = models.DecimalField(db_column='LocalPaymentAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    knockoffamt = models.DecimalField(db_column='KnockOffAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cbkey = models.BigIntegerField(db_column='CBKey', blank=True, null=True)  # Field name made lowercase.
    cancelled = models.CharField(db_column='Cancelled', max_length=1)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    externallink = models.TextField(db_column='ExternalLink', blank=True, null=True)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    createduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    sourcetype = models.CharField(db_column='SourceType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    sourcekey = models.BigIntegerField(db_column='SourceKey', blank=True, null=True)  # Field name made lowercase.
    revaluerate = models.DecimalField(db_column='RevalueRate', max_digits=19, decimal_places=12, blank=True, null=True)  # Field name made lowercase.
    handoverdate = models.DateTimeField(db_column='HandOverDate', blank=True, null=True)  # Field name made lowercase.
    branchcode = models.ForeignKey('Branch', models.DO_NOTHING, db_column='BranchCode', blank=True, null=True)  # Field name made lowercase.
    docno2 = models.CharField(db_column='DocNo2', max_length=25, blank=True, null=True)  # Field name made lowercase.
    gltrxid = models.BigIntegerField(db_column='GLTrxID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'APRefund'


class Aprefunddtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    paymentmethod = models.ForeignKey('Paymentmethod', models.DO_NOTHING, db_column='PaymentMethod')  # Field name made lowercase.
    paymentby = models.CharField(db_column='PaymentBy', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tobankrate = models.DecimalField(db_column='ToBankRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    chequeno = models.CharField(db_column='ChequeNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    floatday = models.SmallIntegerField(db_column='FloatDay', blank=True, null=True)  # Field name made lowercase.
    bankcharge = models.DecimalField(db_column='BankCharge', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    paymentamt = models.DecimalField(db_column='PaymentAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    creditorpaymentamt = models.DecimalField(db_column='CreditorPaymentAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    isrchq = models.CharField(db_column='IsRCHQ', max_length=1)  # Field name made lowercase.
    rchqdate = models.DateTimeField(db_column='RCHQDate', blank=True, null=True)  # Field name made lowercase.
    bankchargedtlkey = models.BigIntegerField(db_column='BankChargeDtlKey', blank=True, null=True)  # Field name made lowercase.
    localpaymentamt = models.DecimalField(db_column='LocalPaymentAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    withholdingtax = models.DecimalField(db_column='WithholdingTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    bankchargeprojno = models.ForeignKey('Project', models.DO_NOTHING, db_column='BankChargeProjNo', blank=True, null=True)  # Field name made lowercase.
    bankchargedeptno = models.ForeignKey('Dept', models.DO_NOTHING, db_column='BankChargeDeptNo', blank=True, null=True)  # Field name made lowercase.
    bankchargetaxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='BankChargeTaxType', blank=True, null=True)  # Field name made lowercase.
    bankchargetaxrate = models.DecimalField(db_column='BankChargeTaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    bankchargetax = models.DecimalField(db_column='BankChargeTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    bankchargetaxrefno = models.CharField(db_column='BankChargeTaxRefNo', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'APRefundDTL'


class Aprefunddepositdtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    paymentmethod = models.ForeignKey('Paymentmethod', models.DO_NOTHING, db_column='PaymentMethod')  # Field name made lowercase.
    paymentby = models.CharField(db_column='PaymentBy', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tobankrate = models.DecimalField(db_column='ToBankRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    chequeno = models.CharField(db_column='ChequeNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    floatday = models.SmallIntegerField(db_column='FloatDay', blank=True, null=True)  # Field name made lowercase.
    bankcharge = models.DecimalField(db_column='BankCharge', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    paymentamt = models.DecimalField(db_column='PaymentAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    isrchq = models.CharField(db_column='IsRCHQ', max_length=1)  # Field name made lowercase.
    rchqdate = models.DateTimeField(db_column='RCHQDate', blank=True, null=True)  # Field name made lowercase.
    bankchargedtlkey = models.BigIntegerField(db_column='BankChargeDtlKey', blank=True, null=True)  # Field name made lowercase.
    bankchargeprojno = models.ForeignKey('Project', models.DO_NOTHING, db_column='BankChargeProjNo', blank=True, null=True)  # Field name made lowercase.
    bankchargedeptno = models.ForeignKey('Dept', models.DO_NOTHING, db_column='BankChargeDeptNo', blank=True, null=True)  # Field name made lowercase.
    bankchargetaxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='BankChargeTaxType', blank=True, null=True)  # Field name made lowercase.
    bankchargetaxrate = models.DecimalField(db_column='BankChargeTaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    bankchargetax = models.DecimalField(db_column='BankChargeTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    bankchargetaxrefno = models.CharField(db_column='BankChargeTaxRefNo', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'APRefundDepositDTL'


class Aprefundknockoff(models.Model):
    knockoffkey = models.BigIntegerField(db_column='KnockOffKey', primary_key=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    knockoffdoctype = models.CharField(db_column='KnockOffDocType', max_length=2)  # Field name made lowercase.
    knockoffdockey = models.BigIntegerField(db_column='KnockOffDocKey')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    gainlossdate = models.DateTimeField(db_column='GainLossDate')  # Field name made lowercase.
    revalue = models.CharField(db_column='Revalue', max_length=1, blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey('Dept', models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    useprojdept = models.CharField(db_column='UseProjDept', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fcrevaluekey = models.BigIntegerField(db_column='FCRevalueKey', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'APRefundKnockOff'


class Aprefundknockoffdetail(models.Model):
    knockoffkey = models.BigIntegerField(db_column='KnockOffKey', primary_key=True)  # Field name made lowercase.
    knockoffdtlkey = models.BigIntegerField(db_column='KnockOffDtlKey')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localrefundamt = models.DecimalField(db_column='LocalRefundAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localpaymentamt = models.DecimalField(db_column='LocalPaymentAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'APRefundKnockOffDetail'
        unique_together = (('knockoffkey', 'knockoffdtlkey'),)


class Arapbaddebt(models.Model):
    doctype = models.CharField(db_column='DocType', primary_key=True, max_length=2)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    jedockey = models.BigIntegerField(db_column='JEDocKey', blank=True, null=True)  # Field name made lowercase.
    jedocdate = models.DateTimeField(db_column='JEDocDate', blank=True, null=True)  # Field name made lowercase.
    bdcndockey = models.BigIntegerField(db_column='BDCNDocKey', blank=True, null=True)  # Field name made lowercase.
    bdcndocdate = models.DateTimeField(db_column='BDCNDocDate', blank=True, null=True)  # Field name made lowercase.
    bdwithbdrcndockey = models.BigIntegerField(db_column='BDWithBDRCNDocKey', blank=True, null=True)  # Field name made lowercase.
    bdwithbdrcndocdate = models.DateTimeField(db_column='BDWithBDRCNDocDate', blank=True, null=True)  # Field name made lowercase.
    baddebttype = models.IntegerField(db_column='BadDebtType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'ARAPBadDebt'
        unique_together = (('doctype', 'dockey'),)


class Arapbaddebtrecovery(models.Model):
    doctype = models.OneToOneField(Arapbaddebt, models.DO_NOTHING, db_column='DocType', primary_key=True)  # Field name made lowercase.
    dockey = models.ForeignKey(Arapbaddebt, models.DO_NOTHING, db_column='DocKey')  # Field name made lowercase.
    paymentdoctype = models.CharField(db_column='PaymentDocType', max_length=2)  # Field name made lowercase.
    paymentdockey = models.BigIntegerField(db_column='PaymentDocKey')  # Field name made lowercase.
    jedockey = models.BigIntegerField(db_column='JEDocKey', blank=True, null=True)  # Field name made lowercase.
    jedrdtlkey = models.BigIntegerField(db_column='JEDRDtlKey', blank=True, null=True)  # Field name made lowercase.
    jecrdtlkey = models.BigIntegerField(db_column='JECRDtlKey', blank=True, null=True)  # Field name made lowercase.
    jedocdate = models.DateTimeField(db_column='JEDocDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'ARAPBadDebtRecovery'
        unique_together = (('doctype', 'dockey', 'paymentdoctype', 'paymentdockey'),)


class Arapcontra(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', unique=True, max_length=20)  # Field name made lowercase.
    debtorcode = models.ForeignKey('Branch', models.DO_NOTHING, db_column='DebtorCode')  # Field name made lowercase.
    creditorcode = models.ForeignKey('Branch', models.DO_NOTHING, db_column='CreditorCode')  # Field name made lowercase.
    tempaccno = models.ForeignKey('Glmast', models.DO_NOTHING, db_column='TempAccNo')  # Field name made lowercase.
    journaltype = models.ForeignKey('Journal', models.DO_NOTHING, db_column='JournalType')  # Field name made lowercase.
    ref = models.CharField(db_column='Ref', max_length=40, blank=True, null=True)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=80, blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey('Dept', models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    currencycode = models.ForeignKey('Currency', models.DO_NOTHING, db_column='CurrencyCode')  # Field name made lowercase.
    currencyrate = models.DecimalField(db_column='CurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    nettotal = models.DecimalField(db_column='NetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    arlocalnettotal = models.DecimalField(db_column='ARLocalNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    aplocalnettotal = models.DecimalField(db_column='APLocalNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    arknockoffamt = models.DecimalField(db_column='ARKnockOffAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    apknockoffamt = models.DecimalField(db_column='APKnockOffAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cancelled = models.CharField(db_column='Cancelled', max_length=1)  # Field name made lowercase.
    jekey = models.BigIntegerField(db_column='JEKey', blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    externallink = models.TextField(db_column='ExternalLink', blank=True, null=True)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    createduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    sourcetype = models.CharField(db_column='SourceType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    sourcekey = models.BigIntegerField(db_column='SourceKey', blank=True, null=True)  # Field name made lowercase.
    revaluerate = models.DecimalField(db_column='RevalueRate', max_digits=19, decimal_places=12, blank=True, null=True)  # Field name made lowercase.
    refno2 = models.CharField(db_column='RefNo2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    debtorbranchcode = models.ForeignKey('Branch', models.DO_NOTHING, db_column='DebtorBranchCode', blank=True, null=True)  # Field name made lowercase.
    creditorbranchcode = models.ForeignKey('Branch', models.DO_NOTHING, db_column='CreditorBranchCode', blank=True, null=True)  # Field name made lowercase.
    gltrxid = models.BigIntegerField(db_column='GLTrxID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'ARAPContra'


class Arcn(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', unique=True, max_length=20)  # Field name made lowercase.
    debtorcode = models.ForeignKey('Branch', models.DO_NOTHING, db_column='DebtorCode')  # Field name made lowercase.
    journaltype = models.ForeignKey('Journal', models.DO_NOTHING, db_column='JournalType')  # Field name made lowercase.
    cntype = models.ForeignKey('Cntype', models.DO_NOTHING, db_column='CNType', blank=True, null=True)  # Field name made lowercase.
    ref = models.CharField(db_column='Ref', max_length=40, blank=True, null=True)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=80, blank=True, null=True)  # Field name made lowercase.
    currencycode = models.ForeignKey('Currency', models.DO_NOTHING, db_column='CurrencyCode')  # Field name made lowercase.
    currencyrate = models.DecimalField(db_column='CurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtotal = models.DecimalField(db_column='LocalTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtax = models.DecimalField(db_column='LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nettotal = models.DecimalField(db_column='NetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localnettotal = models.DecimalField(db_column='LocalNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    knockoffamt = models.DecimalField(db_column='KnockOffAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    refundamt = models.DecimalField(db_column='RefundAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cancelled = models.CharField(db_column='Cancelled', max_length=1)  # Field name made lowercase.
    isjournal = models.CharField(db_column='IsJournal', max_length=1)  # Field name made lowercase.
    jekey = models.BigIntegerField(db_column='JEKey', blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    externallink = models.TextField(db_column='ExternalLink', blank=True, null=True)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    createduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    sourcetype = models.CharField(db_column='SourceType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    sourcekey = models.BigIntegerField(db_column='SourceKey', blank=True, null=True)  # Field name made lowercase.
    revaluerate = models.DecimalField(db_column='RevalueRate', max_digits=19, decimal_places=12, blank=True, null=True)  # Field name made lowercase.
    totalrevaluegainloss = models.DecimalField(db_column='TotalRevalueGainLoss', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    refno2 = models.CharField(db_column='RefNo2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    extax = models.DecimalField(db_column='ExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localextax = models.DecimalField(db_column='LocalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    total2 = models.DecimalField(db_column='Total2', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtotal2 = models.DecimalField(db_column='LocalTotal2', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    branchcode = models.ForeignKey('Branch', models.DO_NOTHING, db_column='BranchCode', blank=True, null=True)  # Field name made lowercase.
    totaxcurrencyrate = models.DecimalField(db_column='ToTaxCurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    taxdocno = models.CharField(db_column='TaxDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ourinvoiceno = models.CharField(db_column='OurInvoiceNo', max_length=40, blank=True, null=True)  # Field name made lowercase.
    reason = models.CharField(db_column='Reason', max_length=80, blank=True, null=True)  # Field name made lowercase.
    inclusivetax = models.CharField(db_column='InclusiveTax', max_length=1)  # Field name made lowercase.
    taxableamt = models.DecimalField(db_column='TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    gltrxid = models.BigIntegerField(db_column='GLTrxID', blank=True, null=True)  # Field name made lowercase.
    gstjedockey = models.BigIntegerField(db_column='GSTJEDocKey', blank=True, null=True)  # Field name made lowercase.
    taxdate = models.DateTimeField(db_column='TaxDate', blank=True, null=True)  # Field name made lowercase.
    roundingmethod = models.IntegerField(db_column='RoundingMethod')  # Field name made lowercase.
    localtaxableamt = models.DecimalField(db_column='LocalTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytax = models.DecimalField(db_column='TaxCurrencyTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxableamt = models.DecimalField(db_column='TaxCurrencyTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sstjedockey = models.BigIntegerField(db_column='SSTJEDocKey', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'ARCN'


class Arcndtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey', blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    accno = models.ForeignKey('Glmast', models.DO_NOTHING, db_column='AccNo', blank=True, null=True)  # Field name made lowercase.
    toaccountrate = models.DecimalField(db_column='ToAccountRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey('Dept', models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='TaxType', blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtax = models.DecimalField(db_column='LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    netamount = models.DecimalField(db_column='NetAmount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localnetamount = models.DecimalField(db_column='LocalNetAmount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unappliedamount = models.DecimalField(db_column='UnappliedAmount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localunappliedamount = models.DecimalField(db_column='LocalUnappliedAmount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    knockoffamount = models.DecimalField(db_column='KnockOffAmount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxableamt = models.DecimalField(db_column='TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localsubtotal = models.DecimalField(db_column='LocalSubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxadjustment = models.DecimalField(db_column='TaxAdjustment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxexportcountry = models.CharField(db_column='TaxExportCountry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sourcedtlkey = models.BigIntegerField(db_column='SourceDtlKey', blank=True, null=True)  # Field name made lowercase.
    taxrate = models.DecimalField(db_column='TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    localtaxadjustment = models.DecimalField(db_column='LocalTaxAdjustment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sourcedtltype = models.CharField(db_column='SourceDtlType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    localtaxableamt = models.DecimalField(db_column='LocalTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytax = models.DecimalField(db_column='TaxCurrencyTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxableamt = models.DecimalField(db_column='TaxCurrencyTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    supplypurchase = models.CharField(db_column='SupplyPurchase', max_length=1)  # Field name made lowercase.
    taxpermitno = models.CharField(db_column='TaxPermitNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tariffcode = models.ForeignKey('Tariff', models.DO_NOTHING, db_column='TariffCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'ARCNDTL'


class Arcnknockoff(models.Model):
    knockoffkey = models.BigIntegerField(db_column='KnockOffKey', primary_key=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    knockoffdoctype = models.CharField(db_column='KnockOffDocType', max_length=2)  # Field name made lowercase.
    knockoffdockey = models.BigIntegerField(db_column='KnockOffDocKey')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    gainlossdate = models.DateTimeField(db_column='GainLossDate')  # Field name made lowercase.
    revalue = models.CharField(db_column='Revalue', max_length=1, blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey('Dept', models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    useprojdept = models.CharField(db_column='UseProjDept', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fcrevaluekey = models.BigIntegerField(db_column='FCRevalueKey', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'ARCNKnockOff'


class Arcnknockoffdetail(models.Model):
    knockoffkey = models.BigIntegerField(db_column='KnockOffKey', primary_key=True)  # Field name made lowercase.
    knockoffdtlkey = models.BigIntegerField(db_column='KnockOffDtlKey')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localcnamt = models.DecimalField(db_column='LocalCNAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localinvoiceamt = models.DecimalField(db_column='LocalInvoiceAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'ARCNKnockOffDetail'
        unique_together = (('knockoffkey', 'knockoffdtlkey'),)


class Arcontraknockoff(models.Model):
    knockoffkey = models.BigIntegerField(db_column='KnockOffKey', primary_key=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    knockoffdoctype = models.CharField(db_column='KnockOffDocType', max_length=2)  # Field name made lowercase.
    knockoffdockey = models.BigIntegerField(db_column='KnockOffDocKey')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    gainlossdate = models.DateTimeField(db_column='GainLossDate')  # Field name made lowercase.
    revalue = models.CharField(db_column='Revalue', max_length=1, blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey('Dept', models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    useprojdept = models.CharField(db_column='UseProjDept', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fcrevaluekey = models.BigIntegerField(db_column='FCRevalueKey', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'ARContraKnockOff'


class Arcontraknockoffdetail(models.Model):
    knockoffkey = models.BigIntegerField(db_column='KnockOffKey', primary_key=True)  # Field name made lowercase.
    knockoffdtlkey = models.BigIntegerField(db_column='KnockOffDtlKey')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localcontraamt = models.DecimalField(db_column='LocalContraAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localinvoiceamt = models.DecimalField(db_column='LocalInvoiceAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'ARContraKnockOffDetail'
        unique_together = (('knockoffkey', 'knockoffdtlkey'),)


class Ardn(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', unique=True, max_length=20)  # Field name made lowercase.
    debtorcode = models.ForeignKey('Branch', models.DO_NOTHING, db_column='DebtorCode')  # Field name made lowercase.
    journaltype = models.ForeignKey('Journal', models.DO_NOTHING, db_column='JournalType')  # Field name made lowercase.
    dntype = models.ForeignKey('Dntype', models.DO_NOTHING, db_column='DNType', blank=True, null=True)  # Field name made lowercase.
    ref = models.CharField(db_column='Ref', max_length=40, blank=True, null=True)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    displayterm = models.ForeignKey('Terms', models.DO_NOTHING, db_column='DisplayTerm')  # Field name made lowercase.
    duedate = models.DateTimeField(db_column='DueDate')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=80, blank=True, null=True)  # Field name made lowercase.
    salesagent = models.ForeignKey('Salesagent', models.DO_NOTHING, db_column='SalesAgent', blank=True, null=True)  # Field name made lowercase.
    currencycode = models.ForeignKey('Currency', models.DO_NOTHING, db_column='CurrencyCode')  # Field name made lowercase.
    currencyrate = models.DecimalField(db_column='CurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtotal = models.DecimalField(db_column='LocalTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtax = models.DecimalField(db_column='LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nettotal = models.DecimalField(db_column='NetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localnettotal = models.DecimalField(db_column='LocalNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    paymentamt = models.DecimalField(db_column='PaymentAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localpaymentamt = models.DecimalField(db_column='LocalPaymentAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    outstanding = models.DecimalField(db_column='Outstanding', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cancelled = models.CharField(db_column='Cancelled', max_length=1)  # Field name made lowercase.
    isjournal = models.CharField(db_column='IsJournal', max_length=1)  # Field name made lowercase.
    jekey = models.BigIntegerField(db_column='JEKey', blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    externallink = models.TextField(db_column='ExternalLink', blank=True, null=True)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    createduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    sourcetype = models.CharField(db_column='SourceType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    sourcekey = models.BigIntegerField(db_column='SourceKey', blank=True, null=True)  # Field name made lowercase.
    forecastduedate = models.DateTimeField(db_column='ForecastDueDate', blank=True, null=True)  # Field name made lowercase.
    revaluerate = models.DecimalField(db_column='RevalueRate', max_digits=19, decimal_places=12, blank=True, null=True)  # Field name made lowercase.
    totalrevaluegainloss = models.DecimalField(db_column='TotalRevalueGainLoss', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    refno2 = models.CharField(db_column='RefNo2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    agingdate = models.DateTimeField(db_column='AgingDate', blank=True, null=True)  # Field name made lowercase.
    extax = models.DecimalField(db_column='ExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localextax = models.DecimalField(db_column='LocalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    total2 = models.DecimalField(db_column='Total2', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtotal2 = models.DecimalField(db_column='LocalTotal2', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    branchcode = models.ForeignKey('Branch', models.DO_NOTHING, db_column='BranchCode', blank=True, null=True)  # Field name made lowercase.
    totaxcurrencyrate = models.DecimalField(db_column='ToTaxCurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    taxdocno = models.CharField(db_column='TaxDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ourinvoiceno = models.CharField(db_column='OurInvoiceNo', max_length=40, blank=True, null=True)  # Field name made lowercase.
    reason = models.CharField(db_column='Reason', max_length=80, blank=True, null=True)  # Field name made lowercase.
    inclusivetax = models.CharField(db_column='InclusiveTax', max_length=1)  # Field name made lowercase.
    taxableamt = models.DecimalField(db_column='TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    gltrxid = models.BigIntegerField(db_column='GLTrxID', blank=True, null=True)  # Field name made lowercase.
    taxdate = models.DateTimeField(db_column='TaxDate', blank=True, null=True)  # Field name made lowercase.
    roundingmethod = models.IntegerField(db_column='RoundingMethod')  # Field name made lowercase.
    localtaxableamt = models.DecimalField(db_column='LocalTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytax = models.DecimalField(db_column='TaxCurrencyTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxableamt = models.DecimalField(db_column='TaxCurrencyTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'ARDN'


class Ardndtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey', blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    accno = models.ForeignKey('Glmast', models.DO_NOTHING, db_column='AccNo', blank=True, null=True)  # Field name made lowercase.
    toaccountrate = models.DecimalField(db_column='ToAccountRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey('Dept', models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='TaxType', blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtax = models.DecimalField(db_column='LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    netamount = models.DecimalField(db_column='NetAmount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localnetamount = models.DecimalField(db_column='LocalNetAmount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    knockoffamount = models.DecimalField(db_column='KnockOffAmount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxableamt = models.DecimalField(db_column='TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localsubtotal = models.DecimalField(db_column='LocalSubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxadjustment = models.DecimalField(db_column='TaxAdjustment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxexportcountry = models.CharField(db_column='TaxExportCountry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sourcedtlkey = models.BigIntegerField(db_column='SourceDtlKey', blank=True, null=True)  # Field name made lowercase.
    taxrate = models.DecimalField(db_column='TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    localtaxadjustment = models.DecimalField(db_column='LocalTaxAdjustment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sourcedtltype = models.CharField(db_column='SourceDtlType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    localtaxableamt = models.DecimalField(db_column='LocalTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytax = models.DecimalField(db_column='TaxCurrencyTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxableamt = models.DecimalField(db_column='TaxCurrencyTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    supplypurchase = models.CharField(db_column='SupplyPurchase', max_length=1)  # Field name made lowercase.
    taxpermitno = models.CharField(db_column='TaxPermitNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tariffcode = models.ForeignKey('Tariff', models.DO_NOTHING, db_column='TariffCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'ARDNDTL'


class Ardeposit(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', unique=True, max_length=20)  # Field name made lowercase.
    debtorcode = models.ForeignKey('Glmast', models.DO_NOTHING, db_column='DebtorCode', blank=True, null=True)  # Field name made lowercase.
    debtorname = models.CharField(db_column='DebtorName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    invaddr1 = models.CharField(db_column='InvAddr1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr2 = models.CharField(db_column='InvAddr2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr3 = models.CharField(db_column='InvAddr3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr4 = models.CharField(db_column='InvAddr4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    phone1 = models.CharField(db_column='Phone1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    fax1 = models.CharField(db_column='Fax1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    attention = models.CharField(db_column='Attention', max_length=40, blank=True, null=True)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=40, blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey('Dept', models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    depositpaymentmethod = models.ForeignKey('Paymentmethod', models.DO_NOTHING, db_column='DepositPaymentMethod')  # Field name made lowercase.
    currencycode = models.ForeignKey('Currency', models.DO_NOTHING, db_column='CurrencyCode')  # Field name made lowercase.
    todepositrate = models.DecimalField(db_column='ToDepositRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    tohomerate = models.DecimalField(db_column='ToHomeRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    paymentamt = models.DecimalField(db_column='PaymentAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    transferedamt = models.DecimalField(db_column='TransferedAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cbkey = models.BigIntegerField(db_column='CBKey', blank=True, null=True)  # Field name made lowercase.
    hasforfeit = models.CharField(db_column='HasForfeit', max_length=1)  # Field name made lowercase.
    forfeiteddate = models.DateTimeField(db_column='ForfeitedDate', blank=True, null=True)  # Field name made lowercase.
    forfeitedamt = models.DecimalField(db_column='ForfeitedAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    forfeitedaccno = models.ForeignKey('Glmast', models.DO_NOTHING, db_column='ForfeitedAccNo', blank=True, null=True)  # Field name made lowercase.
    hasrefund = models.CharField(db_column='HasRefund', max_length=1)  # Field name made lowercase.
    refunddate = models.DateTimeField(db_column='RefundDate', blank=True, null=True)  # Field name made lowercase.
    refunddocno = models.CharField(db_column='RefundDocNo', max_length=20)  # Field name made lowercase.
    refundname = models.CharField(db_column='RefundName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    refundamt = models.DecimalField(db_column='RefundAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    refundcbkey = models.BigIntegerField(db_column='RefundCBKey', blank=True, null=True)  # Field name made lowercase.
    printcount = models.SmallIntegerField(db_column='PrintCount')  # Field name made lowercase.
    cancelled = models.CharField(db_column='Cancelled', max_length=1)  # Field name made lowercase.
    outstanding = models.DecimalField(db_column='Outstanding', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    externallink = models.TextField(db_column='ExternalLink', blank=True, null=True)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    createduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    sourcetype = models.CharField(db_column='SourceType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    sourcekey = models.BigIntegerField(db_column='SourceKey', blank=True, null=True)  # Field name made lowercase.
    gltrxid = models.BigIntegerField(db_column='GLTrxID', blank=True, null=True)  # Field name made lowercase.
    gstjedockey = models.BigIntegerField(db_column='GSTJEDocKey', blank=True, null=True)  # Field name made lowercase.
    issecuritydeposit = models.CharField(db_column='IsSecurityDeposit', max_length=1)  # Field name made lowercase.
    sstjedockey = models.BigIntegerField(db_column='SSTJEDocKey', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'ARDeposit'


class Ardepositdtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    paymentmethod = models.ForeignKey('Paymentmethod', models.DO_NOTHING, db_column='PaymentMethod')  # Field name made lowercase.
    paymentby = models.CharField(db_column='PaymentBy', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tobankrate = models.DecimalField(db_column='ToBankRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    chequeno = models.CharField(db_column='ChequeNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    floatday = models.SmallIntegerField(db_column='FloatDay', blank=True, null=True)  # Field name made lowercase.
    bankcharge = models.DecimalField(db_column='BankCharge', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    paymentamt = models.DecimalField(db_column='PaymentAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    isrchq = models.CharField(db_column='IsRCHQ', max_length=1)  # Field name made lowercase.
    rchqdate = models.DateTimeField(db_column='RCHQDate', blank=True, null=True)  # Field name made lowercase.
    bankchargedtlkey = models.BigIntegerField(db_column='BankChargeDtlKey', blank=True, null=True)  # Field name made lowercase.
    bankchargeprojno = models.ForeignKey('Project', models.DO_NOTHING, db_column='BankChargeProjNo', blank=True, null=True)  # Field name made lowercase.
    bankchargedeptno = models.ForeignKey('Dept', models.DO_NOTHING, db_column='BankChargeDeptNo', blank=True, null=True)  # Field name made lowercase.
    bankchargetaxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='BankChargeTaxType', blank=True, null=True)  # Field name made lowercase.
    bankchargetaxrate = models.DecimalField(db_column='BankChargeTaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    bankchargetax = models.DecimalField(db_column='BankChargeTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    bankchargetaxrefno = models.CharField(db_column='BankChargeTaxRefNo', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'ARDepositDTL'


class Arinvoice(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', unique=True, max_length=20)  # Field name made lowercase.
    debtorcode = models.ForeignKey('Branch', models.DO_NOTHING, db_column='DebtorCode')  # Field name made lowercase.
    journaltype = models.ForeignKey('Journal', models.DO_NOTHING, db_column='JournalType')  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    displayterm = models.ForeignKey('Terms', models.DO_NOTHING, db_column='DisplayTerm')  # Field name made lowercase.
    duedate = models.DateTimeField(db_column='DueDate')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=80, blank=True, null=True)  # Field name made lowercase.
    salesagent = models.ForeignKey('Salesagent', models.DO_NOTHING, db_column='SalesAgent', blank=True, null=True)  # Field name made lowercase.
    currencycode = models.ForeignKey('Currency', models.DO_NOTHING, db_column='CurrencyCode')  # Field name made lowercase.
    currencyrate = models.DecimalField(db_column='CurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtotal = models.DecimalField(db_column='LocalTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtax = models.DecimalField(db_column='LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nettotal = models.DecimalField(db_column='NetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localnettotal = models.DecimalField(db_column='LocalNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    paymentamt = models.DecimalField(db_column='PaymentAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localpaymentamt = models.DecimalField(db_column='LocalPaymentAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    outstanding = models.DecimalField(db_column='Outstanding', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cancelled = models.CharField(db_column='Cancelled', max_length=1)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    externallink = models.TextField(db_column='ExternalLink', blank=True, null=True)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    createduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    sourcetype = models.CharField(db_column='SourceType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    sourcekey = models.BigIntegerField(db_column='SourceKey', blank=True, null=True)  # Field name made lowercase.
    forecastduedate = models.DateTimeField(db_column='ForecastDueDate', blank=True, null=True)  # Field name made lowercase.
    revaluerate = models.DecimalField(db_column='RevalueRate', max_digits=19, decimal_places=12, blank=True, null=True)  # Field name made lowercase.
    totalrevaluegainloss = models.DecimalField(db_column='TotalRevalueGainLoss', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    refno2 = models.CharField(db_column='RefNo2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    agingdate = models.DateTimeField(db_column='AgingDate', blank=True, null=True)  # Field name made lowercase.
    extax = models.DecimalField(db_column='ExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localextax = models.DecimalField(db_column='LocalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    total2 = models.DecimalField(db_column='Total2', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtotal2 = models.DecimalField(db_column='LocalTotal2', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    branchcode = models.ForeignKey('Branch', models.DO_NOTHING, db_column='BranchCode', blank=True, null=True)  # Field name made lowercase.
    totaxcurrencyrate = models.DecimalField(db_column='ToTaxCurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    taxdocno = models.CharField(db_column='TaxDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    inclusivetax = models.CharField(db_column='InclusiveTax', max_length=1)  # Field name made lowercase.
    taxableamt = models.DecimalField(db_column='TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    gltrxid = models.BigIntegerField(db_column='GLTrxID', blank=True, null=True)  # Field name made lowercase.
    taxdate = models.DateTimeField(db_column='TaxDate', blank=True, null=True)  # Field name made lowercase.
    roundingmethod = models.IntegerField(db_column='RoundingMethod')  # Field name made lowercase.
    localtaxableamt = models.DecimalField(db_column='LocalTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytax = models.DecimalField(db_column='TaxCurrencyTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxableamt = models.DecimalField(db_column='TaxCurrencyTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'ARInvoice'


class Arinvoicedtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey', blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    accno = models.ForeignKey('Glmast', models.DO_NOTHING, db_column='AccNo', blank=True, null=True)  # Field name made lowercase.
    toaccountrate = models.DecimalField(db_column='ToAccountRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey('Dept', models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='TaxType', blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtax = models.DecimalField(db_column='LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    netamount = models.DecimalField(db_column='NetAmount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localnetamount = models.DecimalField(db_column='LocalNetAmount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    knockoffamount = models.DecimalField(db_column='KnockOffAmount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxableamt = models.DecimalField(db_column='TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localsubtotal = models.DecimalField(db_column='LocalSubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxadjustment = models.DecimalField(db_column='TaxAdjustment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxexportcountry = models.CharField(db_column='TaxExportCountry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sourcedtlkey = models.BigIntegerField(db_column='SourceDtlKey', blank=True, null=True)  # Field name made lowercase.
    taxrate = models.DecimalField(db_column='TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    localtaxadjustment = models.DecimalField(db_column='LocalTaxAdjustment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sourcedtltype = models.CharField(db_column='SourceDtlType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    localtaxableamt = models.DecimalField(db_column='LocalTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytax = models.DecimalField(db_column='TaxCurrencyTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxableamt = models.DecimalField(db_column='TaxCurrencyTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxpermitno = models.CharField(db_column='TaxPermitNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tariffcode = models.ForeignKey('Tariff', models.DO_NOTHING, db_column='TariffCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'ARInvoiceDTL'


class Arpayment(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', unique=True, max_length=20)  # Field name made lowercase.
    debtorcode = models.ForeignKey('Branch', models.DO_NOTHING, db_column='DebtorCode')  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=80, blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey('Dept', models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    currencycode = models.ForeignKey('Currency', models.DO_NOTHING, db_column='CurrencyCode')  # Field name made lowercase.
    todebtorrate = models.DecimalField(db_column='ToDebtorRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    tohomerate = models.DecimalField(db_column='ToHomeRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    paymentamt = models.DecimalField(db_column='PaymentAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localpaymentamt = models.DecimalField(db_column='LocalPaymentAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    knockoffamt = models.DecimalField(db_column='KnockOffAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localunappliedamount = models.DecimalField(db_column='LocalUnappliedAmount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    refundamt = models.DecimalField(db_column='RefundAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cbkey = models.BigIntegerField(db_column='CBKey', blank=True, null=True)  # Field name made lowercase.
    cancelled = models.CharField(db_column='Cancelled', max_length=1)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    externallink = models.TextField(db_column='ExternalLink', blank=True, null=True)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    createduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    sourcetype = models.CharField(db_column='SourceType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    sourcekey = models.BigIntegerField(db_column='SourceKey', blank=True, null=True)  # Field name made lowercase.
    revaluerate = models.DecimalField(db_column='RevalueRate', max_digits=19, decimal_places=12, blank=True, null=True)  # Field name made lowercase.
    totalrevaluegainloss = models.DecimalField(db_column='TotalRevalueGainLoss', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    handoverdate = models.DateTimeField(db_column='HandOverDate', blank=True, null=True)  # Field name made lowercase.
    refercndockey = models.BigIntegerField(db_column='ReferCNDocKey', blank=True, null=True)  # Field name made lowercase.
    refercndocdate = models.DateTimeField(db_column='ReferCNDocDate', blank=True, null=True)  # Field name made lowercase.
    refercndocno = models.CharField(db_column='ReferCNDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    branchcode = models.ForeignKey('Branch', models.DO_NOTHING, db_column='BranchCode', blank=True, null=True)  # Field name made lowercase.
    docno2 = models.CharField(db_column='DocNo2', max_length=25, blank=True, null=True)  # Field name made lowercase.
    gltrxid = models.BigIntegerField(db_column='GLTrxID', blank=True, null=True)  # Field name made lowercase.
    gstjedockey = models.BigIntegerField(db_column='GSTJEDocKey', blank=True, null=True)  # Field name made lowercase.
    refercnreason = models.CharField(db_column='ReferCNReason', max_length=80, blank=True, null=True)  # Field name made lowercase.
    sstjedockey = models.BigIntegerField(db_column='SSTJEDocKey', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'ARPayment'


class Arpaymentdtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    paymentmethod = models.ForeignKey('Paymentmethod', models.DO_NOTHING, db_column='PaymentMethod')  # Field name made lowercase.
    paymentby = models.CharField(db_column='PaymentBy', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tobankrate = models.DecimalField(db_column='ToBankRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    chequeno = models.CharField(db_column='ChequeNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    floatday = models.SmallIntegerField(db_column='FloatDay', blank=True, null=True)  # Field name made lowercase.
    bankcharge = models.DecimalField(db_column='BankCharge', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    paymentamt = models.DecimalField(db_column='PaymentAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    debtorpaymentamt = models.DecimalField(db_column='DebtorPaymentAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    isrchq = models.CharField(db_column='IsRCHQ', max_length=1)  # Field name made lowercase.
    rchqdate = models.DateTimeField(db_column='RCHQDate', blank=True, null=True)  # Field name made lowercase.
    depositdockey = models.BigIntegerField(db_column='DepositDocKey', blank=True, null=True)  # Field name made lowercase.
    bankchargedtlkey = models.BigIntegerField(db_column='BankChargeDtlKey', blank=True, null=True)  # Field name made lowercase.
    localpaymentamt = models.DecimalField(db_column='LocalPaymentAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    withholdingtax = models.DecimalField(db_column='WithholdingTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    bankchargeprojno = models.ForeignKey('Project', models.DO_NOTHING, db_column='BankChargeProjNo', blank=True, null=True)  # Field name made lowercase.
    bankchargedeptno = models.ForeignKey('Dept', models.DO_NOTHING, db_column='BankChargeDeptNo', blank=True, null=True)  # Field name made lowercase.
    bankchargetaxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='BankChargeTaxType', blank=True, null=True)  # Field name made lowercase.
    bankchargetaxrate = models.DecimalField(db_column='BankChargeTaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    bankchargetax = models.DecimalField(db_column='BankChargeTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    bankchargetaxrefno = models.CharField(db_column='BankChargeTaxRefNo', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'ARPaymentDTL'


class Arpaymentknockoff(models.Model):
    knockoffkey = models.BigIntegerField(db_column='KnockOffKey', primary_key=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    knockoffdoctype = models.CharField(db_column='KnockOffDocType', max_length=2)  # Field name made lowercase.
    knockoffdockey = models.BigIntegerField(db_column='KnockOffDocKey')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    gainlossdate = models.DateTimeField(db_column='GainLossDate')  # Field name made lowercase.
    revalue = models.CharField(db_column='Revalue', max_length=1, blank=True, null=True)  # Field name made lowercase.
    discountamt = models.DecimalField(db_column='DiscountAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey('Dept', models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    useprojdept = models.CharField(db_column='UseProjDept', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fcrevaluekey = models.BigIntegerField(db_column='FCRevalueKey', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'ARPaymentKnockOff'


class Arpaymentknockoffdetail(models.Model):
    knockoffkey = models.BigIntegerField(db_column='KnockOffKey', primary_key=True)  # Field name made lowercase.
    knockoffdtlkey = models.BigIntegerField(db_column='KnockOffDtlKey')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localpaymentamt = models.DecimalField(db_column='LocalPaymentAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localinvoiceamt = models.DecimalField(db_column='LocalInvoiceAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'ARPaymentKnockOffDetail'
        unique_together = (('knockoffkey', 'knockoffdtlkey'),)


class Arrefund(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', unique=True, max_length=20)  # Field name made lowercase.
    debtorcode = models.ForeignKey('Branch', models.DO_NOTHING, db_column='DebtorCode')  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=80, blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey('Dept', models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    currencycode = models.ForeignKey('Currency', models.DO_NOTHING, db_column='CurrencyCode')  # Field name made lowercase.
    todebtorrate = models.DecimalField(db_column='ToDebtorRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    tohomerate = models.DecimalField(db_column='ToHomeRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    paymentamt = models.DecimalField(db_column='PaymentAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localpaymentamt = models.DecimalField(db_column='LocalPaymentAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    knockoffamt = models.DecimalField(db_column='KnockOffAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cbkey = models.BigIntegerField(db_column='CBKey', blank=True, null=True)  # Field name made lowercase.
    cancelled = models.CharField(db_column='Cancelled', max_length=1)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    externallink = models.TextField(db_column='ExternalLink', blank=True, null=True)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    createduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    sourcetype = models.CharField(db_column='SourceType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    sourcekey = models.BigIntegerField(db_column='SourceKey', blank=True, null=True)  # Field name made lowercase.
    revaluerate = models.DecimalField(db_column='RevalueRate', max_digits=19, decimal_places=12, blank=True, null=True)  # Field name made lowercase.
    handoverdate = models.DateTimeField(db_column='HandOverDate', blank=True, null=True)  # Field name made lowercase.
    branchcode = models.ForeignKey('Branch', models.DO_NOTHING, db_column='BranchCode', blank=True, null=True)  # Field name made lowercase.
    docno2 = models.CharField(db_column='DocNo2', max_length=25, blank=True, null=True)  # Field name made lowercase.
    gltrxid = models.BigIntegerField(db_column='GLTrxID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'ARRefund'


class Arrefunddtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    paymentmethod = models.ForeignKey('Paymentmethod', models.DO_NOTHING, db_column='PaymentMethod')  # Field name made lowercase.
    paymentby = models.CharField(db_column='PaymentBy', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tobankrate = models.DecimalField(db_column='ToBankRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    chequeno = models.CharField(db_column='ChequeNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    floatday = models.SmallIntegerField(db_column='FloatDay', blank=True, null=True)  # Field name made lowercase.
    bankcharge = models.DecimalField(db_column='BankCharge', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    paymentamt = models.DecimalField(db_column='PaymentAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    debtorpaymentamt = models.DecimalField(db_column='DebtorPaymentAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    isrchq = models.CharField(db_column='IsRCHQ', max_length=1)  # Field name made lowercase.
    rchqdate = models.DateTimeField(db_column='RCHQDate', blank=True, null=True)  # Field name made lowercase.
    bankchargedtlkey = models.BigIntegerField(db_column='BankChargeDtlKey', blank=True, null=True)  # Field name made lowercase.
    localpaymentamt = models.DecimalField(db_column='LocalPaymentAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    withholdingtax = models.DecimalField(db_column='WithholdingTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    bankchargeprojno = models.ForeignKey('Project', models.DO_NOTHING, db_column='BankChargeProjNo', blank=True, null=True)  # Field name made lowercase.
    bankchargedeptno = models.ForeignKey('Dept', models.DO_NOTHING, db_column='BankChargeDeptNo', blank=True, null=True)  # Field name made lowercase.
    bankchargetaxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='BankChargeTaxType', blank=True, null=True)  # Field name made lowercase.
    bankchargetaxrate = models.DecimalField(db_column='BankChargeTaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    bankchargetax = models.DecimalField(db_column='BankChargeTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    bankchargetaxrefno = models.CharField(db_column='BankChargeTaxRefNo', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'ARRefundDTL'


class Arrefunddepositdtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    paymentmethod = models.ForeignKey('Paymentmethod', models.DO_NOTHING, db_column='PaymentMethod')  # Field name made lowercase.
    paymentby = models.CharField(db_column='PaymentBy', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tobankrate = models.DecimalField(db_column='ToBankRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    chequeno = models.CharField(db_column='ChequeNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    floatday = models.SmallIntegerField(db_column='FloatDay', blank=True, null=True)  # Field name made lowercase.
    bankcharge = models.DecimalField(db_column='BankCharge', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    paymentamt = models.DecimalField(db_column='PaymentAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    isrchq = models.CharField(db_column='IsRCHQ', max_length=1)  # Field name made lowercase.
    rchqdate = models.DateTimeField(db_column='RCHQDate', blank=True, null=True)  # Field name made lowercase.
    bankchargedtlkey = models.BigIntegerField(db_column='BankChargeDtlKey', blank=True, null=True)  # Field name made lowercase.
    bankchargeprojno = models.ForeignKey('Project', models.DO_NOTHING, db_column='BankChargeProjNo', blank=True, null=True)  # Field name made lowercase.
    bankchargedeptno = models.ForeignKey('Dept', models.DO_NOTHING, db_column='BankChargeDeptNo', blank=True, null=True)  # Field name made lowercase.
    bankchargetaxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='BankChargeTaxType', blank=True, null=True)  # Field name made lowercase.
    bankchargetaxrate = models.DecimalField(db_column='BankChargeTaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    bankchargetax = models.DecimalField(db_column='BankChargeTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    bankchargetaxrefno = models.CharField(db_column='BankChargeTaxRefNo', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'ARRefundDepositDTL'


class Arrefundknockoff(models.Model):
    knockoffkey = models.BigIntegerField(db_column='KnockOffKey', primary_key=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    knockoffdoctype = models.CharField(db_column='KnockOffDocType', max_length=2)  # Field name made lowercase.
    knockoffdockey = models.BigIntegerField(db_column='KnockOffDocKey')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    gainlossdate = models.DateTimeField(db_column='GainLossDate')  # Field name made lowercase.
    revalue = models.CharField(db_column='Revalue', max_length=1, blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey('Dept', models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    useprojdept = models.CharField(db_column='UseProjDept', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fcrevaluekey = models.BigIntegerField(db_column='FCRevalueKey', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'ARRefundKnockOff'


class Arrefundknockoffdetail(models.Model):
    knockoffkey = models.BigIntegerField(db_column='KnockOffKey', primary_key=True)  # Field name made lowercase.
    knockoffdtlkey = models.BigIntegerField(db_column='KnockOffDtlKey')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localrefundamt = models.DecimalField(db_column='LocalRefundAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localpaymentamt = models.DecimalField(db_column='LocalPaymentAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'ARRefundKnockOffDetail'
        unique_together = (('knockoffkey', 'knockoffdtlkey'),)


class Asm(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', unique=True, max_length=20)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    itemcode = models.ForeignKey('Itembatch', models.DO_NOTHING, db_column='ItemCode')  # Field name made lowercase.
    location = models.ForeignKey('Location', models.DO_NOTHING, db_column='Location')  # Field name made lowercase.
    batchno = models.ForeignKey('Itembatch', models.DO_NOTHING, db_column='BatchNo', blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey('Dept', models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    assemblycost = models.DecimalField(db_column='AssemblyCost', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nettotal = models.DecimalField(db_column='NetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    remark1 = models.CharField(db_column='Remark1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark2 = models.CharField(db_column='Remark2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark3 = models.CharField(db_column='Remark3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark4 = models.CharField(db_column='Remark4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    printcount = models.SmallIntegerField(db_column='PrintCount', blank=True, null=True)  # Field name made lowercase.
    cancelled = models.CharField(db_column='Cancelled', max_length=1)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    createduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    externallink = models.TextField(db_column='ExternalLink', blank=True, null=True)  # Field name made lowercase.
    refdocno = models.CharField(db_column='RefDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    cansync = models.CharField(db_column='CanSync', max_length=1, blank=True, null=True)  # Field name made lowercase.
    serialnolist = models.TextField(db_column='SerialNoList', blank=True, null=True)  # Field name made lowercase.
    fromasmorderdockey = models.BigIntegerField(db_column='FromASMOrderDocKey', blank=True, null=True)  # Field name made lowercase.
    dismantled = models.CharField(db_column='Dismantled', max_length=1)  # Field name made lowercase.
    ismultilevel = models.CharField(db_column='IsMultilevel', max_length=1, blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.

    class Meta:
 
        db_table = 'ASM'


class Asmbomoptional(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey', blank=True, null=True)  # Field name made lowercase.
    bomoptionalkey = models.BigIntegerField(db_column='BOMOptionalKey', blank=True, null=True)  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=25, decimal_places=8)  # Field name made lowercase.

    class Meta:
 
        db_table = 'ASMBOMOptional'


class Asmdtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey', blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    numbering = models.CharField(db_column='Numbering', max_length=6, blank=True, null=True)  # Field name made lowercase.
    itemcode = models.ForeignKey('Itembatch', models.DO_NOTHING, db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    location = models.ForeignKey('Location', models.DO_NOTHING, db_column='Location', blank=True, null=True)  # Field name made lowercase.
    batchno = models.ForeignKey('Itembatch', models.DO_NOTHING, db_column='BatchNo', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    furtherdescription = models.TextField(db_column='FurtherDescription', blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey('Dept', models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    itemcost = models.DecimalField(db_column='ItemCost', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    overheadcost = models.DecimalField(db_column='OverHeadCost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    subtotalcost = models.DecimalField(db_column='SubTotalCost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=40, blank=True, null=True)  # Field name made lowercase.
    printout = models.CharField(db_column='PrintOut', max_length=1)  # Field name made lowercase.
    serialnolist = models.TextField(db_column='SerialNoList', blank=True, null=True)  # Field name made lowercase.
    fromasmorderdtlkey = models.BigIntegerField(db_column='FromASMOrderDtlKey', blank=True, null=True)  # Field name made lowercase.
    dismantledqty = models.DecimalField(db_column='DismantledQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    parentdtlkey = models.BigIntegerField(db_column='ParentDtlKey', blank=True, null=True)  # Field name made lowercase.
    isbomitem = models.CharField(db_column='IsBOMItem', max_length=1, blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.
    orderqty = models.DecimalField(db_column='OrderQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'ASMDTL'


class Asmorder(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', unique=True, max_length=20)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    itemcode = models.ForeignKey('Itembatch', models.DO_NOTHING, db_column='ItemCode')  # Field name made lowercase.
    location = models.ForeignKey('Location', models.DO_NOTHING, db_column='Location')  # Field name made lowercase.
    batchno = models.ForeignKey('Itembatch', models.DO_NOTHING, db_column='BatchNo', blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey('Dept', models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    transferedqty = models.DecimalField(db_column='TransferedQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    assemblycost = models.DecimalField(db_column='AssemblyCost', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nettotal = models.DecimalField(db_column='NetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    fromdoctype = models.CharField(db_column='FromDocType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    fromdocdtlkey = models.BigIntegerField(db_column='FromDocDtlKey', blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    remark1 = models.CharField(db_column='Remark1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark2 = models.CharField(db_column='Remark2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark3 = models.CharField(db_column='Remark3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark4 = models.CharField(db_column='Remark4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    printcount = models.SmallIntegerField(db_column='PrintCount', blank=True, null=True)  # Field name made lowercase.
    cancelled = models.CharField(db_column='Cancelled', max_length=1)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    createduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    externallink = models.TextField(db_column='ExternalLink', blank=True, null=True)  # Field name made lowercase.
    refdocno = models.CharField(db_column='RefDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    cansync = models.CharField(db_column='CanSync', max_length=1, blank=True, null=True)  # Field name made lowercase.
    totalassemblyrequestqty = models.DecimalField(db_column='TotalAssemblyRequestQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    assemblystatus = models.SmallIntegerField(db_column='AssemblyStatus', blank=True, null=True)  # Field name made lowercase.
    lastaopmodified = models.DateTimeField(db_column='LastAOPModified', blank=True, null=True)  # Field name made lowercase.
    lastaopmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastAOPModifiedUserID', blank=True, null=True)  # Field name made lowercase.
    expectedcompleteddate = models.CharField(db_column='ExpectedCompletedDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ismultilevel = models.CharField(db_column='IsMultilevel', max_length=1, blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.

    class Meta:
 
        db_table = 'ASMOrder'


class Asmorderdtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey', blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    numbering = models.CharField(db_column='Numbering', max_length=6, blank=True, null=True)  # Field name made lowercase.
    itemcode = models.ForeignKey('Itembatch', models.DO_NOTHING, db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    location = models.ForeignKey('Location', models.DO_NOTHING, db_column='Location', blank=True, null=True)  # Field name made lowercase.
    batchno = models.ForeignKey('Itembatch', models.DO_NOTHING, db_column='BatchNo', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    furtherdescription = models.TextField(db_column='FurtherDescription', blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey('Dept', models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    transferedqty = models.DecimalField(db_column='TransferedQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    itemcost = models.DecimalField(db_column='ItemCost', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    overheadcost = models.DecimalField(db_column='OverHeadCost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    subtotalcost = models.DecimalField(db_column='SubTotalCost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=40, blank=True, null=True)  # Field name made lowercase.
    printout = models.CharField(db_column='PrintOut', max_length=1)  # Field name made lowercase.
    stockreceived = models.CharField(db_column='StockReceived', max_length=1)  # Field name made lowercase.
    totalpurchaserequestqty = models.DecimalField(db_column='TotalPurchaseRequestQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    totalassemblyorderrequestqty = models.DecimalField(db_column='TotalAssemblyOrderRequestQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    purchasestatus = models.SmallIntegerField(db_column='PurchaseStatus', blank=True, null=True)  # Field name made lowercase.
    assemblyorderstatus = models.SmallIntegerField(db_column='AssemblyOrderStatus', blank=True, null=True)  # Field name made lowercase.
    lastprmodified = models.DateTimeField(db_column='LastPRModified', blank=True, null=True)  # Field name made lowercase.
    lastprmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastPRModifiedUserID', blank=True, null=True)  # Field name made lowercase.
    lastaorpmodified = models.DateTimeField(db_column='LastAORPModified', blank=True, null=True)  # Field name made lowercase.
    lastaorpmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastAORPModifiedUserID', blank=True, null=True)  # Field name made lowercase.
    parentdtlkey = models.BigIntegerField(db_column='ParentDtlKey', blank=True, null=True)  # Field name made lowercase.
    isbomitem = models.CharField(db_column='IsBOMItem', max_length=1, blank=True, null=True)  # Field name made lowercase.
    transferpoqty = models.DecimalField(db_column='TransferPOQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.

    class Meta:
 
        db_table = 'ASMOrderDTL'


class Accgroup(models.Model):
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    acctype = models.OneToOneField('Acctype', models.DO_NOTHING, db_column='AccType', primary_key=True)  # Field name made lowercase.
    normalbalance = models.CharField(db_column='NormalBalance', max_length=1)  # Field name made lowercase.
    group = models.CharField(db_column='Group', max_length=2)  # Field name made lowercase.
    level = models.IntegerField(db_column='Level')  # Field name made lowercase.

    class Meta:
 
        db_table = 'AccGroup'


class Accperiod(models.Model):
    periodno = models.IntegerField(db_column='PeriodNo', primary_key=True)  # Field name made lowercase.
    lock = models.CharField(db_column='Lock', max_length=1)  # Field name made lowercase.

    class Meta:
 
        db_table = 'AccPeriod'


class Acctype(models.Model):
    acctype = models.CharField(db_column='AccType', primary_key=True, max_length=2)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=40, blank=True, null=True)  # Field name made lowercase.
    desc2 = models.CharField(db_column='Desc2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    isbstype = models.CharField(db_column='IsBSType', max_length=1)  # Field name made lowercase.
    issystemtype = models.CharField(db_column='IsSystemType', max_length=1)  # Field name made lowercase.

    class Meta:
 
        db_table = 'AccType'


class Accessright(models.Model):
    cmdid = models.CharField(db_column='CmdID', primary_key=True, max_length=60)  # Field name made lowercase.
    userid = models.CharField(db_column='UserID', max_length=10)  # Field name made lowercase.

    class Meta:
 
        db_table = 'AccessRight'
        unique_together = (('cmdid', 'userid'),)


class Accountant(models.Model):
    accountantid = models.CharField(db_column='AccountantID', primary_key=True, max_length=80)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    schedulerdata = models.BinaryField(db_column='SchedulerData', blank=True, null=True)  # Field name made lowercase.
    isactive = models.CharField(db_column='IsActive', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'Accountant'


class Activity(models.Model):
    activitykey = models.BigAutoField(db_column='ActivityKey', primary_key=True)  # Field name made lowercase.
    activitydatetime = models.DateTimeField(db_column='ActivityDateTime')  # Field name made lowercase.
    eventkey = models.BigIntegerField(db_column='EventKey', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    computername = models.CharField(db_column='ComputerName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    doctype = models.CharField(db_column='DocType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    detail = models.TextField(db_column='Detail', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'Activity'


class Address(models.Model):
    name = models.CharField(db_column='Name', primary_key=True, max_length=40)  # Field name made lowercase.
    address1 = models.CharField(db_column='Address1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    address2 = models.CharField(db_column='Address2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    address3 = models.CharField(db_column='Address3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    address4 = models.CharField(db_column='Address4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    postcode = models.CharField(db_column='PostCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    contact = models.CharField(db_column='Contact', max_length=40, blank=True, null=True)  # Field name made lowercase.
    phone1 = models.CharField(db_column='Phone1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    phone2 = models.CharField(db_column='Phone2', max_length=25, blank=True, null=True)  # Field name made lowercase.
    fax1 = models.CharField(db_column='Fax1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    fax2 = models.CharField(db_column='Fax2', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'Address'


class Area(models.Model):
    areacode = models.CharField(db_column='AreaCode', primary_key=True, max_length=12)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=40, blank=True, null=True)  # Field name made lowercase.
    desc2 = models.CharField(db_column='Desc2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.

    class Meta:
 
        db_table = 'Area'


class Asmrprocessing(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    aodockey = models.BigIntegerField(db_column='AODocKey')  # Field name made lowercase.
    asmdockey = models.BigIntegerField(db_column='ASMDocKey', blank=True, null=True)  # Field name made lowercase.
    asmdocno = models.CharField(db_column='ASMDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    itemcode = models.ForeignKey('Item', models.DO_NOTHING, db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    location = models.ForeignKey('Location', models.DO_NOTHING, db_column='Location', blank=True, null=True)  # Field name made lowercase.
    batchno = models.CharField(db_column='BatchNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey('Dept', models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    requestqty = models.DecimalField(db_column='RequestQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    createduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'AsmRProcessing'


class Assetdisposal(models.Model):
    disposalkey = models.BigAutoField(db_column='DisposalKey', primary_key=True)  # Field name made lowercase.
    fixedassetaccno = models.ForeignKey('Glmast', models.DO_NOTHING, db_column='FixedAssetAccNo')  # Field name made lowercase.
    transdate = models.DateTimeField(db_column='TransDate')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=80, blank=True, null=True)  # Field name made lowercase.
    disposalvalue = models.DecimalField(db_column='DisposalValue', max_digits=19, decimal_places=2)  # Field name made lowercase.
    currencyrate = models.DecimalField(db_column='CurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    localdisposalvalue = models.DecimalField(db_column='LocalDisposalValue', max_digits=19, decimal_places=2)  # Field name made lowercase.

    class Meta:
 
        db_table = 'AssetDisposal'


class Assetlink(models.Model):
    assetaccno = models.OneToOneField('Glmast', models.DO_NOTHING, db_column='AssetAccNo', primary_key=True)  # Field name made lowercase.
    assetdeprnaccno = models.ForeignKey('Glmast', models.DO_NOTHING, db_column='AssetDeprnAccNo')  # Field name made lowercase.

    class Meta:
 
        db_table = 'AssetLink'
        unique_together = (('assetaccno', 'assetdeprnaccno'),)


class Autoprice(models.Model):
    autopricekey = models.AutoField(db_column='AutoPriceKey', primary_key=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    autopricetype = models.CharField(db_column='AutoPriceType', max_length=10)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=60)  # Field name made lowercase.
    forsale = models.CharField(db_column='ForSale', max_length=1)  # Field name made lowercase.
    enable = models.CharField(db_column='Enable', max_length=1)  # Field name made lowercase.

    class Meta:
 
        db_table = 'AutoPrice'


class Bomoptional(models.Model):
    bomoptionalkey = models.BigIntegerField(db_column='BOMOptionalKey', primary_key=True)  # Field name made lowercase.
    bomoptionalcode = models.CharField(db_column='BOMOptionalCode', max_length=30)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    desc2 = models.CharField(db_column='Desc2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    isactive = models.CharField(db_column='IsActive', max_length=1)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.

    class Meta:
 
        db_table = 'BOMOptional'


class Bomoptionaldtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    bomoptionalkey = models.BigIntegerField(db_column='BOMOptionalKey')  # Field name made lowercase.
    subitemcode = models.ForeignKey('Item', models.DO_NOTHING, db_column='SubItemCode')  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=25, decimal_places=8)  # Field name made lowercase.
    overheadcost = models.DecimalField(db_column='OverheadCost', max_digits=25, decimal_places=8)  # Field name made lowercase.

    class Meta:
 
        db_table = 'BOMOptionalDTL'


class Bomoptionallink(models.Model):
    bomoptionallinkkey = models.BigIntegerField(db_column='BOMOptionalLinkKey', primary_key=True)  # Field name made lowercase.
    bomoptionalkey = models.BigIntegerField(db_column='BOMOptionalKey')  # Field name made lowercase.
    bomitemcode = models.ForeignKey('Item', models.DO_NOTHING, db_column='BOMItemCode')  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=25, decimal_places=8)  # Field name made lowercase.

    class Meta:
 
        db_table = 'BOMOptionalLink'


class Bsformat(models.Model):
    autokey = models.AutoField(db_column='AutoKey', primary_key=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    rowtype = models.CharField(db_column='RowType', max_length=1)  # Field name made lowercase.
    acctype = models.ForeignKey(Acctype, models.DO_NOTHING, db_column='AccType', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    creditaspositive = models.CharField(db_column='CreditAsPositive', max_length=1)  # Field name made lowercase.

    class Meta:
 
        db_table = 'BSFormat'


class Bankrecon(models.Model):
    accno = models.OneToOneField('Glmast', models.DO_NOTHING, db_column='AccNo', primary_key=True)  # Field name made lowercase.
    bankstatementdate = models.DateTimeField(db_column='BankStatementDate')  # Field name made lowercase.
    actualbankstatementbalance = models.DecimalField(db_column='ActualBankStatementBalance', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'BankRecon'
        unique_together = (('accno', 'bankstatementdate'),)


class Bankslip(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', max_length=20)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    bankaccno = models.CharField(db_column='BankAccNo', max_length=12)  # Field name made lowercase.

    class Meta:
 
        db_table = 'BankSlip'


class Banktrans(models.Model):
    banktranskey = models.BigAutoField(db_column='BankTransKey', primary_key=True)  # Field name made lowercase.
    sourcetype = models.CharField(db_column='SourceType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    sourcekey = models.BigIntegerField(db_column='SourceKey', blank=True, null=True)  # Field name made lowercase.
    dtlkey = models.BigIntegerField(db_column='DtlKey', blank=True, null=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', max_length=20)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    accno = models.ForeignKey(Bankrecon, models.DO_NOTHING, db_column='AccNo')  # Field name made lowercase.
    chequeno = models.CharField(db_column='ChequeNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    floatday = models.SmallIntegerField(db_column='FloatDay', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    paymentamt = models.DecimalField(db_column='PaymentAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    bankstatementdate = models.ForeignKey(Bankrecon, models.DO_NOTHING, db_column='BankStatementDate', blank=True, null=True)  # Field name made lowercase.
    bankreconstatus = models.SmallIntegerField(db_column='BankReconStatus', blank=True, null=True)  # Field name made lowercase.
    bankslipdockey = models.BigIntegerField(db_column='BankSlipDocKey', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'BankTrans'


class Bonuspointadj(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', max_length=20)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    remark1 = models.CharField(db_column='Remark1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark2 = models.CharField(db_column='Remark2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark3 = models.CharField(db_column='Remark3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark4 = models.CharField(db_column='Remark4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    printcount = models.SmallIntegerField(db_column='PrintCount')  # Field name made lowercase.
    cancelled = models.CharField(db_column='Cancelled', max_length=1)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    createduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    externallink = models.TextField(db_column='ExternalLink', blank=True, null=True)  # Field name made lowercase.
    refdocno = models.CharField(db_column='RefDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    cansync = models.CharField(db_column='CanSync', max_length=1)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.

    class Meta:
 
        db_table = 'BonusPointADJ'


class Bonuspointadjdtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    memberno = models.ForeignKey('Member', models.DO_NOTHING, db_column='MemberNo', blank=True, null=True)  # Field name made lowercase.
    point = models.DecimalField(db_column='Point', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    printout = models.CharField(db_column='PrintOut', max_length=1)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.

    class Meta:
 
        db_table = 'BonusPointADJDTL'


class Bonuspointredemption(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    memberno = models.ForeignKey('Member', models.DO_NOTHING, db_column='MemberNo', blank=True, null=True)  # Field name made lowercase.
    debtorcode = models.ForeignKey('Glmast', models.DO_NOTHING, db_column='DebtorCode', blank=True, null=True)  # Field name made lowercase.
    totalpointredeem = models.DecimalField(db_column='TotalPointRedeem', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=40, blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    posttostock = models.CharField(db_column='PostToStock', max_length=1)  # Field name made lowercase.
    referdockey = models.BigIntegerField(db_column='ReferDocKey', blank=True, null=True)  # Field name made lowercase.
    printcount = models.SmallIntegerField(db_column='PrintCount')  # Field name made lowercase.
    cancelled = models.CharField(db_column='Cancelled', max_length=1)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    createduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    cansync = models.CharField(db_column='CanSync', max_length=1)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.

    class Meta:
 
        db_table = 'BonusPointRedemption'


class Bonuspointredemptiondtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    dockey = models.ForeignKey(Bonuspointredemption, models.DO_NOTHING, db_column='DocKey')  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    itemcode = models.ForeignKey('Itemuom', models.DO_NOTHING, db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    location = models.ForeignKey('Location', models.DO_NOTHING, db_column='Location', blank=True, null=True)  # Field name made lowercase.
    batchno = models.ForeignKey('Itembatch', models.DO_NOTHING, db_column='BatchNo', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    furtherdescription = models.TextField(db_column='FurtherDescription', blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey('Dept', models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    uom = models.ForeignKey('Itemuom', models.DO_NOTHING, db_column='UOM', blank=True, null=True)  # Field name made lowercase.
    qty = models.BigIntegerField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    smallestqty = models.DecimalField(db_column='SmallestQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    unitpoint = models.DecimalField(db_column='UnitPoint', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    posttostockdate = models.DateTimeField(db_column='PostToStockDate', blank=True, null=True)  # Field name made lowercase.
    printout = models.CharField(db_column='PrintOut', max_length=1)  # Field name made lowercase.

    class Meta:
 
        db_table = 'BonusPointRedemptionDTL'


class Branch(models.Model):
    accno = models.OneToOneField('Glmast', models.DO_NOTHING, db_column='AccNo', primary_key=True)  # Field name made lowercase.
    branchcode = models.CharField(db_column='BranchCode', max_length=20)  # Field name made lowercase.
    branchname = models.CharField(db_column='BranchName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    address1 = models.CharField(db_column='Address1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    address2 = models.CharField(db_column='Address2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    address3 = models.CharField(db_column='Address3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    address4 = models.CharField(db_column='Address4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    postcode = models.CharField(db_column='PostCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    contact = models.CharField(db_column='Contact', max_length=40, blank=True, null=True)  # Field name made lowercase.
    phone1 = models.CharField(db_column='Phone1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    phone2 = models.CharField(db_column='Phone2', max_length=25, blank=True, null=True)  # Field name made lowercase.
    fax1 = models.CharField(db_column='Fax1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    fax2 = models.CharField(db_column='Fax2', max_length=25, blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    areacode = models.ForeignKey(Area, models.DO_NOTHING, db_column='AreaCode', blank=True, null=True)  # Field name made lowercase.
    salesagent = models.ForeignKey('Salesagent', models.DO_NOTHING, db_column='SalesAgent', blank=True, null=True)  # Field name made lowercase.
    purchaseagent = models.ForeignKey('Purchaseagent', models.DO_NOTHING, db_column='PurchaseAgent', blank=True, null=True)  # Field name made lowercase.
    emailaddress = models.CharField(db_column='EmailAddress', max_length=80, blank=True, null=True)  # Field name made lowercase.
    isactive = models.CharField(db_column='IsActive', max_length=1)  # Field name made lowercase.

    class Meta:
 
        db_table = 'Branch'
        unique_together = (('accno', 'branchcode'),)


class Budget(models.Model):
    budgetkey = models.IntegerField(db_column='BudgetKey', primary_key=True)  # Field name made lowercase.
    budgetname = models.CharField(db_column='BudgetName', max_length=20)  # Field name made lowercase.

    class Meta:
 
        db_table = 'Budget'


class Budgetpbalance(models.Model):
    budgetkey = models.IntegerField(db_column='BudgetKey')  # Field name made lowercase.
    periodno = models.IntegerField(db_column='PeriodNo')  # Field name made lowercase.
    accno = models.ForeignKey('Glmast', models.DO_NOTHING, db_column='AccNO')  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey('Dept', models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'BudgetPBalance'


class Cb(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', unique=True, max_length=20)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    doctype = models.CharField(db_column='DocType', max_length=2)  # Field name made lowercase.
    dealwith = models.CharField(db_column='DealWith', max_length=80, blank=True, null=True)  # Field name made lowercase.
    currencycode = models.ForeignKey('Currency', models.DO_NOTHING, db_column='CurrencyCode')  # Field name made lowercase.
    currencyrate = models.DecimalField(db_column='CurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    totalpayment = models.DecimalField(db_column='TotalPayment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtotal = models.DecimalField(db_column='LocalTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtax = models.DecimalField(db_column='LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nettotal = models.DecimalField(db_column='NetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localnettotal = models.DecimalField(db_column='LocalNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    printcount = models.SmallIntegerField(db_column='PrintCount')  # Field name made lowercase.
    cancelled = models.CharField(db_column='Cancelled', max_length=1)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    externallink = models.TextField(db_column='ExternalLink', blank=True, null=True)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    createduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    sourcetype = models.CharField(db_column='SourceType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    sourcekey = models.BigIntegerField(db_column='SourceKey', blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    postdetaildesc = models.CharField(db_column='PostDetailDesc', max_length=1, blank=True, null=True)  # Field name made lowercase.
    handoverdate = models.DateTimeField(db_column='HandOverDate', blank=True, null=True)  # Field name made lowercase.
    extax = models.DecimalField(db_column='ExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localextax = models.DecimalField(db_column='LocalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    docno2 = models.CharField(db_column='DocNo2', max_length=25, blank=True, null=True)  # Field name made lowercase.
    totaxcurrencyrate = models.DecimalField(db_column='ToTaxCurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=80, blank=True, null=True)  # Field name made lowercase.
    inclusivetax = models.CharField(db_column='InclusiveTax', max_length=1)  # Field name made lowercase.
    totalextax = models.DecimalField(db_column='TotalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtotalextax = models.DecimalField(db_column='LocalTotalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxableamt = models.DecimalField(db_column='TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    gltrxid = models.BigIntegerField(db_column='GLTrxID', blank=True, null=True)  # Field name made lowercase.
    taxdate = models.DateTimeField(db_column='TaxDate', blank=True, null=True)  # Field name made lowercase.
    roundingmethod = models.IntegerField(db_column='RoundingMethod')  # Field name made lowercase.
    localtaxableamt = models.DecimalField(db_column='LocalTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytax = models.DecimalField(db_column='TaxCurrencyTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxableamt = models.DecimalField(db_column='TaxCurrencyTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    rchqtaxtranskeymap = models.BinaryField(db_column='RCHQTaxTransKeymap', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'CB'


class Cbdtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    accno = models.ForeignKey('Glmast', models.DO_NOTHING, db_column='AccNo', blank=True, null=True)  # Field name made lowercase.
    toaccountrate = models.DecimalField(db_column='ToAccountRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey('Dept', models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='TaxType', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    furtherdescription = models.TextField(db_column='FurtherDescription', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localamount = models.DecimalField(db_column='LocalAmount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    rchqamount = models.DecimalField(db_column='RCHQAmount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    salesagent = models.ForeignKey('Salesagent', models.DO_NOTHING, db_column='SalesAgent', blank=True, null=True)  # Field name made lowercase.
    taxableamt = models.DecimalField(db_column='TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtax = models.DecimalField(db_column='LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxpermitno = models.CharField(db_column='TaxPermitNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    taxadjustment = models.DecimalField(db_column='TaxAdjustment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxexportcountry = models.CharField(db_column='TaxExportCountry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    taxrefno = models.CharField(db_column='TaxRefNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    taxrate = models.DecimalField(db_column='TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    taxbrno = models.CharField(db_column='TaxBRNo', max_length=25, blank=True, null=True)  # Field name made lowercase.
    taxbname = models.CharField(db_column='TaxBName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    localtaxadjustment = models.DecimalField(db_column='LocalTaxAdjustment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxregisterno = models.CharField(db_column='TaxRegisterNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    taxbilldate = models.DateTimeField(db_column='TaxBillDate', blank=True, null=True)  # Field name made lowercase.
    localtaxableamt = models.DecimalField(db_column='LocalTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytax = models.DecimalField(db_column='TaxCurrencyTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxableamt = models.DecimalField(db_column='TaxCurrencyTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    inclusivetax = models.CharField(db_column='InclusiveTax', max_length=1)  # Field name made lowercase.
    amountextax = models.DecimalField(db_column='AmountExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localamountextax = models.DecimalField(db_column='LocalAmountExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    amountwithtax = models.DecimalField(db_column='AmountWithTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localamountwithtax = models.DecimalField(db_column='LocalAmountWithTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    negativekopayment = models.CharField(db_column='NegativeKOPayment', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tariffcode = models.ForeignKey('Tariff', models.DO_NOTHING, db_column='TariffCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'CBDTL'


class Cbigdtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    cbdtlkey = models.BigIntegerField(db_column='CBDtlKey')  # Field name made lowercase.
    taxableamt = models.DecimalField(db_column='TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxtype = models.CharField(db_column='TaxType', max_length=14, blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtax = models.DecimalField(db_column='LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxpermitno = models.CharField(db_column='TaxPermitNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    taxrate = models.DecimalField(db_column='TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    currencyrate = models.DecimalField(db_column='CurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    taxadjustment = models.DecimalField(db_column='TaxAdjustment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtaxadjustment = models.DecimalField(db_column='LocalTaxAdjustment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtaxableamt = models.DecimalField(db_column='LocalTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytax = models.DecimalField(db_column='TaxCurrencyTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxableamt = models.DecimalField(db_column='TaxCurrencyTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sourcedtlkey = models.BigIntegerField(db_column='SourceDtlKey')  # Field name made lowercase.
    sourcetype = models.CharField(db_column='SourceType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    sourcedtltype = models.CharField(db_column='SourceDtlType', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'CBIGDTL'
        unique_together = (('sourcetype', 'sourcedtlkey', 'sourcedtltype'),)


class Cbpaymentdtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    paymentmethod = models.ForeignKey('Paymentmethod', models.DO_NOTHING, db_column='PaymentMethod')  # Field name made lowercase.
    paymentby = models.CharField(db_column='PaymentBy', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tobankrate = models.DecimalField(db_column='ToBankRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    chequeno = models.CharField(db_column='ChequeNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    floatday = models.SmallIntegerField(db_column='FloatDay', blank=True, null=True)  # Field name made lowercase.
    bankcharge = models.DecimalField(db_column='BankCharge', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    paymentamt = models.DecimalField(db_column='PaymentAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    isrchq = models.CharField(db_column='IsRCHQ', max_length=1)  # Field name made lowercase.
    rchqdate = models.DateTimeField(db_column='RCHQDate', blank=True, null=True)  # Field name made lowercase.
    bankchargedtlkey = models.BigIntegerField(db_column='BankChargeDtlKey', blank=True, null=True)  # Field name made lowercase.
    withholdingtax = models.DecimalField(db_column='WithholdingTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    bankchargeprojno = models.CharField(db_column='BankChargeProjNo', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bankchargedeptno = models.CharField(db_column='BankChargeDeptNo', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bankchargetaxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='BankChargeTaxType', blank=True, null=True)  # Field name made lowercase.
    bankchargetaxrate = models.DecimalField(db_column='BankChargeTaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    bankchargetax = models.DecimalField(db_column='BankChargeTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    bankchargetaxrefno = models.CharField(db_column='BankChargeTaxRefNo', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'CBPaymentDTL'


class Cn(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', unique=True, max_length=20)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    debtorcode = models.ForeignKey(Branch, models.DO_NOTHING, db_column='DebtorCode')  # Field name made lowercase.
    debtorname = models.CharField(db_column='DebtorName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cntype = models.ForeignKey('Cntype', models.DO_NOTHING, db_column='CNType', blank=True, null=True)  # Field name made lowercase.
    ref = models.CharField(db_column='Ref', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ourinvoiceno = models.CharField(db_column='OurInvoiceNo', max_length=40, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=80, blank=True, null=True)  # Field name made lowercase.
    displayterm = models.ForeignKey('Terms', models.DO_NOTHING, db_column='DisplayTerm')  # Field name made lowercase.
    salesagent = models.ForeignKey('Salesagent', models.DO_NOTHING, db_column='SalesAgent', blank=True, null=True)  # Field name made lowercase.
    invaddr1 = models.CharField(db_column='InvAddr1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr2 = models.CharField(db_column='InvAddr2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr3 = models.CharField(db_column='InvAddr3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr4 = models.CharField(db_column='InvAddr4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    phone1 = models.CharField(db_column='Phone1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    fax1 = models.CharField(db_column='Fax1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    attention = models.CharField(db_column='Attention', max_length=40, blank=True, null=True)  # Field name made lowercase.
    branchcode = models.ForeignKey(Branch, models.DO_NOTHING, db_column='BranchCode', blank=True, null=True)  # Field name made lowercase.
    deliveraddr1 = models.CharField(db_column='DeliverAddr1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliveraddr2 = models.CharField(db_column='DeliverAddr2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliveraddr3 = models.CharField(db_column='DeliverAddr3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliveraddr4 = models.CharField(db_column='DeliverAddr4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliverphone1 = models.CharField(db_column='DeliverPhone1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    deliverfax1 = models.CharField(db_column='DeliverFax1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    delivercontact = models.CharField(db_column='DeliverContact', max_length=40, blank=True, null=True)  # Field name made lowercase.
    salesexemptionno = models.CharField(db_column='SalesExemptionNo', max_length=60, blank=True, null=True)  # Field name made lowercase.
    salesexemptionexpirydate = models.DateTimeField(db_column='SalesExemptionExpiryDate', blank=True, null=True)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1param = models.DecimalField(db_column='Footer1Param', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1amt = models.DecimalField(db_column='Footer1Amt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1localamt = models.DecimalField(db_column='Footer1LocalAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='Footer1TaxType', blank=True, null=True)  # Field name made lowercase.
    footer2param = models.DecimalField(db_column='Footer2Param', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2amt = models.DecimalField(db_column='Footer2Amt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2localamt = models.DecimalField(db_column='Footer2LocalAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='Footer2TaxType', blank=True, null=True)  # Field name made lowercase.
    footer3param = models.DecimalField(db_column='Footer3Param', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3amt = models.DecimalField(db_column='Footer3Amt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3localamt = models.DecimalField(db_column='Footer3LocalAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='Footer3TaxType', blank=True, null=True)  # Field name made lowercase.
    currencycode = models.ForeignKey('Currency', models.DO_NOTHING, db_column='CurrencyCode')  # Field name made lowercase.
    currencyrate = models.DecimalField(db_column='CurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    nettotal = models.DecimalField(db_column='NetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localnettotal = models.DecimalField(db_column='LocalNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    analysisnettotal = models.DecimalField(db_column='AnalysisNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localanalysisnettotal = models.DecimalField(db_column='LocalAnalysisNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtotalcost = models.DecimalField(db_column='LocalTotalCost', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtax = models.DecimalField(db_column='LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    totalbonuspoint = models.DecimalField(db_column='TotalBonusPoint', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    posttostock = models.CharField(db_column='PostToStock', max_length=1)  # Field name made lowercase.
    posttogl = models.CharField(db_column='PostToGL', max_length=1)  # Field name made lowercase.
    referdockey = models.BigIntegerField(db_column='ReferDocKey', blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    remark1 = models.CharField(db_column='Remark1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark2 = models.CharField(db_column='Remark2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark3 = models.CharField(db_column='Remark3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark4 = models.CharField(db_column='Remark4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    printcount = models.SmallIntegerField(db_column='PrintCount')  # Field name made lowercase.
    cancelled = models.CharField(db_column='Cancelled', max_length=1)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    createduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    externallink = models.TextField(db_column='ExternalLink', blank=True, null=True)  # Field name made lowercase.
    refdocno = models.CharField(db_column='RefDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cansync = models.CharField(db_column='CanSync', max_length=1)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    memberno = models.ForeignKey('Member', models.DO_NOTHING, db_column='MemberNo', blank=True, null=True)  # Field name made lowercase.
    refno2 = models.CharField(db_column='RefNo2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    saleslocation = models.ForeignKey('Location', models.DO_NOTHING, db_column='SalesLocation', blank=True, null=True)  # Field name made lowercase.
    footer1tax = models.DecimalField(db_column='Footer1Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1localtax = models.DecimalField(db_column='Footer1LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2tax = models.DecimalField(db_column='Footer2Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2localtax = models.DecimalField(db_column='Footer2LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3tax = models.DecimalField(db_column='Footer3Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3localtax = models.DecimalField(db_column='Footer3LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    extax = models.DecimalField(db_column='ExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localextax = models.DecimalField(db_column='LocalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    yourpono = models.CharField(db_column='YourPONo', max_length=25, blank=True, null=True)  # Field name made lowercase.
    yourpodate = models.DateTimeField(db_column='YourPODate', blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.
    totaxcurrencyrate = models.DecimalField(db_column='ToTaxCurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    calcdiscountonunitprice = models.CharField(db_column='CalcDiscountOnUnitPrice', max_length=1, blank=True, null=True)  # Field name made lowercase.
    taxdocno = models.CharField(db_column='TaxDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    totalextax = models.DecimalField(db_column='TotalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxableamt = models.DecimalField(db_column='TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    reason = models.CharField(db_column='Reason', max_length=80, blank=True, null=True)  # Field name made lowercase.
    inclusivetax = models.CharField(db_column='InclusiveTax', max_length=1)  # Field name made lowercase.
    footer1taxrate = models.DecimalField(db_column='Footer1TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    footer2taxrate = models.DecimalField(db_column='Footer2TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    footer3taxrate = models.DecimalField(db_column='Footer3TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    taxdate = models.DateTimeField(db_column='TaxDate', blank=True, null=True)  # Field name made lowercase.
    isroundadj = models.CharField(db_column='IsRoundAdj', max_length=1)  # Field name made lowercase.
    roundadj = models.DecimalField(db_column='RoundAdj', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    finaltotal = models.DecimalField(db_column='FinalTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    roundingmethod = models.IntegerField(db_column='RoundingMethod')  # Field name made lowercase.
    localtaxableamt = models.DecimalField(db_column='LocalTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytax = models.DecimalField(db_column='TaxCurrencyTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxableamt = models.DecimalField(db_column='TaxCurrencyTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'CN'


class Cndtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    focdtlkey = models.BigIntegerField(db_column='FOCDtlKey', blank=True, null=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    indent = models.SmallIntegerField(db_column='Indent', blank=True, null=True)  # Field name made lowercase.
    fontstyle = models.ForeignKey('Fontstyle', models.DO_NOTHING, db_column='FontStyle', blank=True, null=True)  # Field name made lowercase.
    mainitem = models.CharField(db_column='MainItem', max_length=1)  # Field name made lowercase.
    numbering = models.CharField(db_column='Numbering', max_length=6, blank=True, null=True)  # Field name made lowercase.
    itemcode = models.ForeignKey('Itemuom', models.DO_NOTHING, db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    location = models.ForeignKey('Location', models.DO_NOTHING, db_column='Location', blank=True, null=True)  # Field name made lowercase.
    batchno = models.ForeignKey('Itembatch', models.DO_NOTHING, db_column='BatchNo', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    furtherdescription = models.TextField(db_column='FurtherDescription', blank=True, null=True)  # Field name made lowercase.
    posttostockdate = models.DateTimeField(db_column='PostToStockDate', blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey('Dept', models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    uom = models.ForeignKey('Itemuom', models.DO_NOTHING, db_column='UOM', blank=True, null=True)  # Field name made lowercase.
    useruom = models.CharField(db_column='UserUOM', max_length=8, blank=True, null=True)  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    smallestqty = models.DecimalField(db_column='SmallestQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    focqty = models.DecimalField(db_column='FOCQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    smallestunitprice = models.DecimalField(db_column='SmallestUnitPrice', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    unitcost = models.DecimalField(db_column='UnitCost', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    focunitcost = models.DecimalField(db_column='FOCUnitCost', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    discount = models.CharField(db_column='Discount', max_length=20, blank=True, null=True)  # Field name made lowercase.
    discountamt = models.DecimalField(db_column='DiscountAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='TaxType', blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localsubtotal = models.DecimalField(db_column='LocalSubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    bonuspoint = models.DecimalField(db_column='BonusPoint', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    printout = models.CharField(db_column='PrintOut', max_length=1)  # Field name made lowercase.
    dtltype = models.CharField(db_column='DtlType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    calcbypercent = models.DecimalField(db_column='CalcByPercent', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    addtosubtotal = models.CharField(db_column='AddToSubTotal', max_length=1)  # Field name made lowercase.
    fromdoctype = models.CharField(db_column='FromDocType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    fromdocno = models.CharField(db_column='FromDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fromdocdtlkey = models.BigIntegerField(db_column='FromDocDtlKey', blank=True, null=True)  # Field name made lowercase.
    accno = models.ForeignKey('Glmast', models.DO_NOTHING, db_column='AccNo', blank=True, null=True)  # Field name made lowercase.
    fulltransferoption = models.CharField(db_column='FullTransferOption', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fulltransferfromdoclist = models.TextField(db_column='FullTransferFromDocList', blank=True, null=True)  # Field name made lowercase.
    serialnolist = models.TextField(db_column='SerialNoList', blank=True, null=True)  # Field name made lowercase.
    packagedockey = models.BigIntegerField(db_column='PackageDocKey', blank=True, null=True)  # Field name made lowercase.
    parentdtlkey = models.BigIntegerField(db_column='ParentDtlKey', blank=True, null=True)  # Field name made lowercase.
    subqty = models.DecimalField(db_column='SubQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    iscalcbonuspoint = models.CharField(db_column='IsCalcBonusPoint', max_length=1, blank=True, null=True)  # Field name made lowercase.
    subtotalextax = models.DecimalField(db_column='SubTotalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtax = models.DecimalField(db_column='LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    yourpono = models.CharField(db_column='YourPONo', max_length=25, blank=True, null=True)  # Field name made lowercase.
    yourpodate = models.DateTimeField(db_column='YourPODate', blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.
    ruleno = models.BigIntegerField(db_column='RuleNo', blank=True, null=True)  # Field name made lowercase.
    goodsreturn = models.CharField(db_column='GoodsReturn', max_length=1, blank=True, null=True)  # Field name made lowercase.
    taxableamt = models.DecimalField(db_column='TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxadjustment = models.DecimalField(db_column='TaxAdjustment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxexportcountry = models.CharField(db_column='TaxExportCountry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    localsubtotalextax = models.DecimalField(db_column='LocalSubTotalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    extradiscountamt = models.DecimalField(db_column='ExtraDiscountAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxrate = models.DecimalField(db_column='TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    localtaxadjustment = models.DecimalField(db_column='LocalTaxAdjustment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtaxableamt = models.DecimalField(db_column='LocalTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytax = models.DecimalField(db_column='TaxCurrencyTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxableamt = models.DecimalField(db_column='TaxCurrencyTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxpermitno = models.CharField(db_column='TaxPermitNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    supplypurchase = models.CharField(db_column='SupplyPurchase', max_length=1, blank=True, null=True)  # Field name made lowercase.
    salesexemptionno = models.CharField(db_column='SalesExemptionNo', max_length=60, blank=True, null=True)  # Field name made lowercase.
    tariffcode = models.ForeignKey('Tariff', models.DO_NOTHING, db_column='TariffCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'CNDTL'


class Cntype(models.Model):
    cntype = models.CharField(db_column='CNType', primary_key=True, max_length=12)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=40, blank=True, null=True)  # Field name made lowercase.
    desc2 = models.CharField(db_column='Desc2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    isactive = models.CharField(db_column='IsActive', max_length=1)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.

    class Meta:
 
        db_table = 'CNType'


class Cp(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', unique=True, max_length=20)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    creditorcode = models.ForeignKey(Branch, models.DO_NOTHING, db_column='CreditorCode', blank=True, null=True)  # Field name made lowercase.
    creditorname = models.CharField(db_column='CreditorName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ref = models.CharField(db_column='Ref', max_length=40, blank=True, null=True)  # Field name made lowercase.
    supplierdono = models.CharField(db_column='SupplierDONo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    supplierinvoiceno = models.CharField(db_column='SupplierInvoiceNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=80, blank=True, null=True)  # Field name made lowercase.
    displayterm = models.ForeignKey('Terms', models.DO_NOTHING, db_column='DisplayTerm')  # Field name made lowercase.
    purchaseagent = models.ForeignKey('Purchaseagent', models.DO_NOTHING, db_column='PurchaseAgent', blank=True, null=True)  # Field name made lowercase.
    invaddr1 = models.CharField(db_column='InvAddr1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr2 = models.CharField(db_column='InvAddr2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr3 = models.CharField(db_column='InvAddr3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr4 = models.CharField(db_column='InvAddr4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    phone1 = models.CharField(db_column='Phone1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    fax1 = models.CharField(db_column='Fax1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    attention = models.CharField(db_column='Attention', max_length=40, blank=True, null=True)  # Field name made lowercase.
    branchcode = models.ForeignKey(Branch, models.DO_NOTHING, db_column='BranchCode', blank=True, null=True)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1param = models.DecimalField(db_column='Footer1Param', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1amt = models.DecimalField(db_column='Footer1Amt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1localamt = models.DecimalField(db_column='Footer1LocalAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='Footer1TaxType', blank=True, null=True)  # Field name made lowercase.
    footer2param = models.DecimalField(db_column='Footer2Param', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2amt = models.DecimalField(db_column='Footer2Amt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2localamt = models.DecimalField(db_column='Footer2LocalAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='Footer2TaxType', blank=True, null=True)  # Field name made lowercase.
    footer3param = models.DecimalField(db_column='Footer3Param', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3amt = models.DecimalField(db_column='Footer3Amt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3localamt = models.DecimalField(db_column='Footer3LocalAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='Footer3TaxType', blank=True, null=True)  # Field name made lowercase.
    currencycode = models.ForeignKey('Currency', models.DO_NOTHING, db_column='CurrencyCode')  # Field name made lowercase.
    currencyrate = models.DecimalField(db_column='CurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    nettotal = models.DecimalField(db_column='NetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localnettotal = models.DecimalField(db_column='LocalNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtax = models.DecimalField(db_column='LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    foreigncharges = models.DecimalField(db_column='ForeignCharges', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localcharges = models.DecimalField(db_column='LocalCharges', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    landedcostmethod = models.CharField(db_column='LandedCostMethod', max_length=1, blank=True, null=True)  # Field name made lowercase.
    posttostock = models.CharField(db_column='PostToStock', max_length=1)  # Field name made lowercase.
    posttogl = models.CharField(db_column='PostToGL', max_length=1)  # Field name made lowercase.
    referdockey = models.BigIntegerField(db_column='ReferDocKey', blank=True, null=True)  # Field name made lowercase.
    referpaymentdockey = models.BigIntegerField(db_column='ReferPaymentDocKey', blank=True, null=True)  # Field name made lowercase.
    transferable = models.CharField(db_column='Transferable', max_length=1)  # Field name made lowercase.
    todoctype = models.CharField(db_column='ToDocType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    todockey = models.BigIntegerField(db_column='ToDocKey', blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    remark1 = models.CharField(db_column='Remark1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark2 = models.CharField(db_column='Remark2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark3 = models.CharField(db_column='Remark3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark4 = models.CharField(db_column='Remark4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    printcount = models.SmallIntegerField(db_column='PrintCount')  # Field name made lowercase.
    cancelled = models.CharField(db_column='Cancelled', max_length=1)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    createduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    externallink = models.TextField(db_column='ExternalLink', blank=True, null=True)  # Field name made lowercase.
    refdocno = models.CharField(db_column='RefDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    csgndockey = models.BigIntegerField(db_column='CSGNDocKey', blank=True, null=True)  # Field name made lowercase.
    cansync = models.CharField(db_column='CanSync', max_length=1)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    todtlkey = models.BigIntegerField(db_column='ToDtlKey', blank=True, null=True)  # Field name made lowercase.
    fulltransferoption = models.CharField(db_column='FullTransferOption', max_length=1, blank=True, null=True)  # Field name made lowercase.
    shipvia = models.ForeignKey('Shippingmethod', models.DO_NOTHING, db_column='ShipVia', blank=True, null=True)  # Field name made lowercase.
    shipinfo = models.CharField(db_column='ShipInfo', max_length=40, blank=True, null=True)  # Field name made lowercase.
    refno2 = models.CharField(db_column='RefNo2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    purchaselocation = models.ForeignKey('Location', models.DO_NOTHING, db_column='PurchaseLocation', blank=True, null=True)  # Field name made lowercase.
    footer1tax = models.DecimalField(db_column='Footer1Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1localtax = models.DecimalField(db_column='Footer1LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2tax = models.DecimalField(db_column='Footer2Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2localtax = models.DecimalField(db_column='Footer2LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3tax = models.DecimalField(db_column='Footer3Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3localtax = models.DecimalField(db_column='Footer3LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    extax = models.DecimalField(db_column='ExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localextax = models.DecimalField(db_column='LocalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    paymentmode = models.SmallIntegerField(db_column='PaymentMode', blank=True, null=True)  # Field name made lowercase.
    cashpayment = models.DecimalField(db_column='CashPayment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ccapprovalcode = models.CharField(db_column='CCApprovalCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    analysisnettotal = models.DecimalField(db_column='AnalysisNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localanalysisnettotal = models.DecimalField(db_column='LocalAnalysisNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.
    totaxcurrencyrate = models.DecimalField(db_column='ToTaxCurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    calcdiscountonunitprice = models.CharField(db_column='CalcDiscountOnUnitPrice', max_length=1, blank=True, null=True)  # Field name made lowercase.
    taxdocno = models.CharField(db_column='TaxDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    totalextax = models.DecimalField(db_column='TotalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxableamt = models.DecimalField(db_column='TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    inclusivetax = models.CharField(db_column='InclusiveTax', max_length=1)  # Field name made lowercase.
    footer1taxrate = models.DecimalField(db_column='Footer1TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    footer2taxrate = models.DecimalField(db_column='Footer2TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    footer3taxrate = models.DecimalField(db_column='Footer3TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    taxdate = models.DateTimeField(db_column='TaxDate', blank=True, null=True)  # Field name made lowercase.
    isroundadj = models.CharField(db_column='IsRoundAdj', max_length=1)  # Field name made lowercase.
    roundadj = models.DecimalField(db_column='RoundAdj', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    finaltotal = models.DecimalField(db_column='FinalTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    selfbilledapprovalno = models.CharField(db_column='SelfBilledApprovalNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    roundingmethod = models.IntegerField(db_column='RoundingMethod')  # Field name made lowercase.
    localtaxableamt = models.DecimalField(db_column='LocalTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytax = models.DecimalField(db_column='TaxCurrencyTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxableamt = models.DecimalField(db_column='TaxCurrencyTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    docdate2 = models.DateTimeField(db_column='DocDate2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'CP'


class Cpdtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    focdtlkey = models.BigIntegerField(db_column='FOCDtlKey', blank=True, null=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    indent = models.SmallIntegerField(db_column='Indent', blank=True, null=True)  # Field name made lowercase.
    fontstyle = models.ForeignKey('Fontstyle', models.DO_NOTHING, db_column='FontStyle', blank=True, null=True)  # Field name made lowercase.
    mainitem = models.CharField(db_column='MainItem', max_length=1)  # Field name made lowercase.
    numbering = models.CharField(db_column='Numbering', max_length=6, blank=True, null=True)  # Field name made lowercase.
    itemcode = models.ForeignKey('Itemuom', models.DO_NOTHING, db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    location = models.ForeignKey('Location', models.DO_NOTHING, db_column='Location', blank=True, null=True)  # Field name made lowercase.
    batchno = models.ForeignKey('Itembatch', models.DO_NOTHING, db_column='BatchNo', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    furtherdescription = models.TextField(db_column='FurtherDescription', blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey('Dept', models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    ourpono = models.CharField(db_column='OurPONo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ourpodate = models.DateTimeField(db_column='OurPODate', blank=True, null=True)  # Field name made lowercase.
    posttostockdate = models.DateTimeField(db_column='PostToStockDate', blank=True, null=True)  # Field name made lowercase.
    uom = models.ForeignKey('Itemuom', models.DO_NOTHING, db_column='UOM', blank=True, null=True)  # Field name made lowercase.
    useruom = models.CharField(db_column='UserUOM', max_length=8, blank=True, null=True)  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    smallestqty = models.DecimalField(db_column='SmallestQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    transferedqty = models.DecimalField(db_column='TransferedQty', max_digits=25, decimal_places=8)  # Field name made lowercase.
    focqty = models.DecimalField(db_column='FOCQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    foctransferedqty = models.DecimalField(db_column='FOCTransferedQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    smallestunitprice = models.DecimalField(db_column='SmallestUnitPrice', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    discount = models.CharField(db_column='Discount', max_length=20, blank=True, null=True)  # Field name made lowercase.
    discountamt = models.DecimalField(db_column='DiscountAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='TaxType', blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localsubtotal = models.DecimalField(db_column='LocalSubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    transferable = models.CharField(db_column='Transferable', max_length=1)  # Field name made lowercase.
    printout = models.CharField(db_column='PrintOut', max_length=1)  # Field name made lowercase.
    dtltype = models.CharField(db_column='DtlType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    calcbypercent = models.DecimalField(db_column='CalcByPercent', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    addtosubtotal = models.CharField(db_column='AddToSubTotal', max_length=1)  # Field name made lowercase.
    fromdoctype = models.CharField(db_column='FromDocType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    fromdocno = models.CharField(db_column='FromDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fromdocdtlkey = models.BigIntegerField(db_column='FromDocDtlKey', blank=True, null=True)  # Field name made lowercase.
    fulltransferoption = models.CharField(db_column='FullTransferOption', max_length=1, blank=True, null=True)  # Field name made lowercase.
    foreigncharges = models.DecimalField(db_column='ForeignCharges', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    localcharges = models.DecimalField(db_column='LocalCharges', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    duty = models.DecimalField(db_column='Duty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    forconsignment = models.CharField(db_column='ForConsignment', max_length=1)  # Field name made lowercase.
    accno = models.ForeignKey('Glmast', models.DO_NOTHING, db_column='AccNo', blank=True, null=True)  # Field name made lowercase.
    fulltransferfromdoclist = models.TextField(db_column='FullTransferFromDocList', blank=True, null=True)  # Field name made lowercase.
    serialnolist = models.TextField(db_column='SerialNoList', blank=True, null=True)  # Field name made lowercase.
    estimateddeliverydate = models.CharField(db_column='EstimatedDeliveryDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    packagedockey = models.BigIntegerField(db_column='PackageDocKey', blank=True, null=True)  # Field name made lowercase.
    parentdtlkey = models.BigIntegerField(db_column='ParentDtlKey', blank=True, null=True)  # Field name made lowercase.
    subqty = models.DecimalField(db_column='SubQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    subtotalextax = models.DecimalField(db_column='SubTotalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtax = models.DecimalField(db_column='LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.
    deliverydate = models.DateTimeField(db_column='DeliveryDate', blank=True, null=True)  # Field name made lowercase.
    cnamt = models.DecimalField(db_column='CNAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxpermitno = models.CharField(db_column='TaxPermitNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    taxableamt = models.DecimalField(db_column='TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxadjustment = models.DecimalField(db_column='TaxAdjustment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localsubtotalextax = models.DecimalField(db_column='LocalSubTotalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    extradiscountamt = models.DecimalField(db_column='ExtraDiscountAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxrate = models.DecimalField(db_column='TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    localtaxadjustment = models.DecimalField(db_column='LocalTaxAdjustment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtaxableamt = models.DecimalField(db_column='LocalTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytax = models.DecimalField(db_column='TaxCurrencyTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxableamt = models.DecimalField(db_column='TaxCurrencyTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    salesexemptionno = models.CharField(db_column='SalesExemptionNo', max_length=60, blank=True, null=True)  # Field name made lowercase.
    tariffcode = models.ForeignKey('Tariff', models.DO_NOTHING, db_column='TariffCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'CPDTL'


class Cs(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', unique=True, max_length=20)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    debtorcode = models.ForeignKey(Branch, models.DO_NOTHING, db_column='DebtorCode')  # Field name made lowercase.
    debtorname = models.CharField(db_column='DebtorName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ref = models.CharField(db_column='Ref', max_length=40, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=80, blank=True, null=True)  # Field name made lowercase.
    displayterm = models.ForeignKey('Terms', models.DO_NOTHING, db_column='DisplayTerm')  # Field name made lowercase.
    salesagent = models.ForeignKey('Salesagent', models.DO_NOTHING, db_column='SalesAgent', blank=True, null=True)  # Field name made lowercase.
    invaddr1 = models.CharField(db_column='InvAddr1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr2 = models.CharField(db_column='InvAddr2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr3 = models.CharField(db_column='InvAddr3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr4 = models.CharField(db_column='InvAddr4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    phone1 = models.CharField(db_column='Phone1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    fax1 = models.CharField(db_column='Fax1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    attention = models.CharField(db_column='Attention', max_length=40, blank=True, null=True)  # Field name made lowercase.
    branchcode = models.ForeignKey(Branch, models.DO_NOTHING, db_column='BranchCode', blank=True, null=True)  # Field name made lowercase.
    deliveraddr1 = models.CharField(db_column='DeliverAddr1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliveraddr2 = models.CharField(db_column='DeliverAddr2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliveraddr3 = models.CharField(db_column='DeliverAddr3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliveraddr4 = models.CharField(db_column='DeliverAddr4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliverphone1 = models.CharField(db_column='DeliverPhone1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    deliverfax1 = models.CharField(db_column='DeliverFax1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    delivercontact = models.CharField(db_column='DeliverContact', max_length=40, blank=True, null=True)  # Field name made lowercase.
    salesexemptionno = models.CharField(db_column='SalesExemptionNo', max_length=60, blank=True, null=True)  # Field name made lowercase.
    salesexemptionexpirydate = models.DateTimeField(db_column='SalesExemptionExpiryDate', blank=True, null=True)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1param = models.DecimalField(db_column='Footer1Param', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1amt = models.DecimalField(db_column='Footer1Amt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1localamt = models.DecimalField(db_column='Footer1LocalAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='Footer1TaxType', blank=True, null=True)  # Field name made lowercase.
    footer2param = models.DecimalField(db_column='Footer2Param', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2amt = models.DecimalField(db_column='Footer2Amt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2localamt = models.DecimalField(db_column='Footer2LocalAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='Footer2TaxType', blank=True, null=True)  # Field name made lowercase.
    footer3param = models.DecimalField(db_column='Footer3Param', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3amt = models.DecimalField(db_column='Footer3Amt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3localamt = models.DecimalField(db_column='Footer3LocalAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='Footer3TaxType', blank=True, null=True)  # Field name made lowercase.
    currencycode = models.ForeignKey('Currency', models.DO_NOTHING, db_column='CurrencyCode')  # Field name made lowercase.
    currencyrate = models.DecimalField(db_column='CurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    nettotal = models.DecimalField(db_column='NetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localnettotal = models.DecimalField(db_column='LocalNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    analysisnettotal = models.DecimalField(db_column='AnalysisNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localanalysisnettotal = models.DecimalField(db_column='LocalAnalysisNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtotalcost = models.DecimalField(db_column='LocalTotalCost', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtax = models.DecimalField(db_column='LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    totalbonuspoint = models.DecimalField(db_column='TotalBonusPoint', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    posttostock = models.CharField(db_column='PostToStock', max_length=1)  # Field name made lowercase.
    posttogl = models.CharField(db_column='PostToGL', max_length=1)  # Field name made lowercase.
    referdockey = models.BigIntegerField(db_column='ReferDocKey', blank=True, null=True)  # Field name made lowercase.
    referpaymentdockey = models.BigIntegerField(db_column='ReferPaymentDocKey', blank=True, null=True)  # Field name made lowercase.
    transferable = models.CharField(db_column='Transferable', max_length=1)  # Field name made lowercase.
    todoctype = models.CharField(db_column='ToDocType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    todockey = models.BigIntegerField(db_column='ToDocKey', blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    remark1 = models.CharField(db_column='Remark1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark2 = models.CharField(db_column='Remark2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark3 = models.CharField(db_column='Remark3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark4 = models.CharField(db_column='Remark4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    printcount = models.SmallIntegerField(db_column='PrintCount')  # Field name made lowercase.
    cancelled = models.CharField(db_column='Cancelled', max_length=1)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    createduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    externallink = models.TextField(db_column='ExternalLink', blank=True, null=True)  # Field name made lowercase.
    refdocno = models.CharField(db_column='RefDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    csgndockey = models.BigIntegerField(db_column='CSGNDocKey', blank=True, null=True)  # Field name made lowercase.
    cansync = models.CharField(db_column='CanSync', max_length=1)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    memberno = models.ForeignKey('Member', models.DO_NOTHING, db_column='MemberNo', blank=True, null=True)  # Field name made lowercase.
    todtlkey = models.BigIntegerField(db_column='ToDtlKey', blank=True, null=True)  # Field name made lowercase.
    fulltransferoption = models.CharField(db_column='FullTransferOption', max_length=1, blank=True, null=True)  # Field name made lowercase.
    shipvia = models.ForeignKey('Shippingmethod', models.DO_NOTHING, db_column='ShipVia', blank=True, null=True)  # Field name made lowercase.
    shipinfo = models.CharField(db_column='ShipInfo', max_length=40, blank=True, null=True)  # Field name made lowercase.
    reallocatepurchasebyproject = models.CharField(db_column='ReallocatePurchaseByProject', max_length=1)  # Field name made lowercase.
    reallocatepurchasebyprojectjedockey = models.BigIntegerField(db_column='ReallocatePurchaseByProjectJEDocKey', blank=True, null=True)  # Field name made lowercase.
    refno2 = models.CharField(db_column='RefNo2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    paymentmode = models.SmallIntegerField(db_column='PaymentMode', blank=True, null=True)  # Field name made lowercase.
    cashpayment = models.DecimalField(db_column='CashPayment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ccapprovalcode = models.CharField(db_column='CCApprovalCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    saleslocation = models.ForeignKey('Location', models.DO_NOTHING, db_column='SalesLocation', blank=True, null=True)  # Field name made lowercase.
    footer1tax = models.DecimalField(db_column='Footer1Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1localtax = models.DecimalField(db_column='Footer1LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2tax = models.DecimalField(db_column='Footer2Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2localtax = models.DecimalField(db_column='Footer2LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3tax = models.DecimalField(db_column='Footer3Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3localtax = models.DecimalField(db_column='Footer3LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    extax = models.DecimalField(db_column='ExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localextax = models.DecimalField(db_column='LocalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    yourpono = models.CharField(db_column='YourPONo', max_length=25, blank=True, null=True)  # Field name made lowercase.
    yourpodate = models.DateTimeField(db_column='YourPODate', blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.
    reallocatepurchasebyprojectno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ReallocatePurchaseByProjectNo', blank=True, null=True)  # Field name made lowercase.
    totaxcurrencyrate = models.DecimalField(db_column='ToTaxCurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    roundadj = models.DecimalField(db_column='RoundAdj', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    finaltotal = models.DecimalField(db_column='FinalTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    calcdiscountonunitprice = models.CharField(db_column='CalcDiscountOnUnitPrice', max_length=1, blank=True, null=True)  # Field name made lowercase.
    taxdocno = models.CharField(db_column='TaxDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    totalextax = models.DecimalField(db_column='TotalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxableamt = models.DecimalField(db_column='TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    inclusivetax = models.CharField(db_column='InclusiveTax', max_length=1)  # Field name made lowercase.
    footer1taxrate = models.DecimalField(db_column='Footer1TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    footer2taxrate = models.DecimalField(db_column='Footer2TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    footer3taxrate = models.DecimalField(db_column='Footer3TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    taxdate = models.DateTimeField(db_column='TaxDate', blank=True, null=True)  # Field name made lowercase.
    isroundadj = models.CharField(db_column='IsRoundAdj', max_length=1)  # Field name made lowercase.
    roundingmethod = models.IntegerField(db_column='RoundingMethod')  # Field name made lowercase.
    localtaxableamt = models.DecimalField(db_column='LocalTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytax = models.DecimalField(db_column='TaxCurrencyTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxableamt = models.DecimalField(db_column='TaxCurrencyTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'CS'


class Csdtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    focdtlkey = models.BigIntegerField(db_column='FOCDtlKey', blank=True, null=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    indent = models.SmallIntegerField(db_column='Indent', blank=True, null=True)  # Field name made lowercase.
    fontstyle = models.ForeignKey('Fontstyle', models.DO_NOTHING, db_column='FontStyle', blank=True, null=True)  # Field name made lowercase.
    mainitem = models.CharField(db_column='MainItem', max_length=1)  # Field name made lowercase.
    numbering = models.CharField(db_column='Numbering', max_length=6, blank=True, null=True)  # Field name made lowercase.
    itemcode = models.ForeignKey('Itemuom', models.DO_NOTHING, db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    location = models.ForeignKey('Location', models.DO_NOTHING, db_column='Location', blank=True, null=True)  # Field name made lowercase.
    batchno = models.ForeignKey('Itembatch', models.DO_NOTHING, db_column='BatchNo', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    furtherdescription = models.TextField(db_column='FurtherDescription', blank=True, null=True)  # Field name made lowercase.
    yourpono = models.CharField(db_column='YourPONo', max_length=25, blank=True, null=True)  # Field name made lowercase.
    yourpodate = models.DateTimeField(db_column='YourPODate', blank=True, null=True)  # Field name made lowercase.
    posttostockdate = models.DateTimeField(db_column='PostToStockDate', blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey('Dept', models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    uom = models.ForeignKey('Itemuom', models.DO_NOTHING, db_column='UOM', blank=True, null=True)  # Field name made lowercase.
    useruom = models.CharField(db_column='UserUOM', max_length=8, blank=True, null=True)  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    smallestqty = models.DecimalField(db_column='SmallestQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    transferedqty = models.DecimalField(db_column='TransferedQty', max_digits=25, decimal_places=8)  # Field name made lowercase.
    focqty = models.DecimalField(db_column='FOCQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    foctransferedqty = models.DecimalField(db_column='FOCTransferedQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    smallestunitprice = models.DecimalField(db_column='SmallestUnitPrice', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    discount = models.CharField(db_column='Discount', max_length=20, blank=True, null=True)  # Field name made lowercase.
    discountamt = models.DecimalField(db_column='DiscountAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='TaxType', blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localsubtotal = models.DecimalField(db_column='LocalSubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtotalcost = models.DecimalField(db_column='LocalTotalCost', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    localfoctotalcost = models.DecimalField(db_column='LocalFOCTotalCost', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    bonuspoint = models.DecimalField(db_column='BonusPoint', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    transferable = models.CharField(db_column='Transferable', max_length=1)  # Field name made lowercase.
    printout = models.CharField(db_column='PrintOut', max_length=1)  # Field name made lowercase.
    dtltype = models.CharField(db_column='DtlType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    calcbypercent = models.DecimalField(db_column='CalcByPercent', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    addtosubtotal = models.CharField(db_column='AddToSubTotal', max_length=1)  # Field name made lowercase.
    fromdoctype = models.CharField(db_column='FromDocType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    fromdocno = models.CharField(db_column='FromDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fromdocdtlkey = models.BigIntegerField(db_column='FromDocDtlKey', blank=True, null=True)  # Field name made lowercase.
    forconsignment = models.CharField(db_column='ForConsignment', max_length=1)  # Field name made lowercase.
    accno = models.ForeignKey('Glmast', models.DO_NOTHING, db_column='AccNo', blank=True, null=True)  # Field name made lowercase.
    fulltransferoption = models.CharField(db_column='FullTransferOption', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fulltransferfromdoclist = models.TextField(db_column='FullTransferFromDocList', blank=True, null=True)  # Field name made lowercase.
    ourdono = models.CharField(db_column='OurDONo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ourdodate = models.DateTimeField(db_column='OurDODate', blank=True, null=True)  # Field name made lowercase.
    serialnolist = models.TextField(db_column='SerialNoList', blank=True, null=True)  # Field name made lowercase.
    estimateddeliverydate = models.CharField(db_column='EstimatedDeliveryDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    packagedockey = models.BigIntegerField(db_column='PackageDocKey', blank=True, null=True)  # Field name made lowercase.
    parentdtlkey = models.BigIntegerField(db_column='ParentDtlKey', blank=True, null=True)  # Field name made lowercase.
    subqty = models.DecimalField(db_column='SubQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    iscalcbonuspoint = models.CharField(db_column='IsCalcBonusPoint', max_length=1, blank=True, null=True)  # Field name made lowercase.
    subtotalextax = models.DecimalField(db_column='SubTotalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtax = models.DecimalField(db_column='LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.
    ruleno = models.BigIntegerField(db_column='RuleNo', blank=True, null=True)  # Field name made lowercase.
    deliverydate = models.DateTimeField(db_column='DeliveryDate', blank=True, null=True)  # Field name made lowercase.
    taxableamt = models.DecimalField(db_column='TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxadjustment = models.DecimalField(db_column='TaxAdjustment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxexportcountry = models.CharField(db_column='TaxExportCountry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    localsubtotalextax = models.DecimalField(db_column='LocalSubTotalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    extradiscountamt = models.DecimalField(db_column='ExtraDiscountAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxrate = models.DecimalField(db_column='TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    localtaxadjustment = models.DecimalField(db_column='LocalTaxAdjustment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtaxableamt = models.DecimalField(db_column='LocalTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytax = models.DecimalField(db_column='TaxCurrencyTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxableamt = models.DecimalField(db_column='TaxCurrencyTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxpermitno = models.CharField(db_column='TaxPermitNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    salesexemptionno = models.CharField(db_column='SalesExemptionNo', max_length=60, blank=True, null=True)  # Field name made lowercase.
    tariffcode = models.ForeignKey('Tariff', models.DO_NOTHING, db_column='TariffCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'CSDTL'


class Csgn(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', unique=True, max_length=20)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    debtorcode = models.ForeignKey(Branch, models.DO_NOTHING, db_column='DebtorCode')  # Field name made lowercase.
    debtorname = models.CharField(db_column='DebtorName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ref = models.CharField(db_column='Ref', max_length=40, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=60, blank=True, null=True)  # Field name made lowercase.
    salesagent = models.ForeignKey('Salesagent', models.DO_NOTHING, db_column='SalesAgent', blank=True, null=True)  # Field name made lowercase.
    invaddr1 = models.CharField(db_column='InvAddr1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr2 = models.CharField(db_column='InvAddr2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr3 = models.CharField(db_column='InvAddr3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr4 = models.CharField(db_column='InvAddr4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    phone1 = models.CharField(db_column='Phone1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    fax1 = models.CharField(db_column='Fax1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    attention = models.CharField(db_column='Attention', max_length=40, blank=True, null=True)  # Field name made lowercase.
    branchcode = models.ForeignKey(Branch, models.DO_NOTHING, db_column='BranchCode', blank=True, null=True)  # Field name made lowercase.
    deliveraddr1 = models.CharField(db_column='DeliverAddr1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliveraddr2 = models.CharField(db_column='DeliverAddr2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliveraddr3 = models.CharField(db_column='DeliverAddr3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliveraddr4 = models.CharField(db_column='DeliverAddr4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliverphone1 = models.CharField(db_column='DeliverPhone1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    deliverfax1 = models.CharField(db_column='DeliverFax1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    delivercontact = models.CharField(db_column='DeliverContact', max_length=40, blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    remark1 = models.CharField(db_column='Remark1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark2 = models.CharField(db_column='Remark2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark3 = models.CharField(db_column='Remark3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark4 = models.CharField(db_column='Remark4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    printcount = models.SmallIntegerField(db_column='PrintCount')  # Field name made lowercase.
    cancelled = models.CharField(db_column='Cancelled', max_length=1)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    createduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    externallink = models.TextField(db_column='ExternalLink', blank=True, null=True)  # Field name made lowercase.
    refdocno = models.CharField(db_column='RefDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    cansync = models.CharField(db_column='CanSync', max_length=1)  # Field name made lowercase.
    sourcetype = models.CharField(db_column='SourceType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    sourcekey = models.BigIntegerField(db_column='SourceKey', blank=True, null=True)  # Field name made lowercase.
    shipvia = models.ForeignKey('Shippingmethod', models.DO_NOTHING, db_column='ShipVia', blank=True, null=True)  # Field name made lowercase.
    shipinfo = models.CharField(db_column='ShipInfo', max_length=40, blank=True, null=True)  # Field name made lowercase.
    saleslocation = models.ForeignKey('Location', models.DO_NOTHING, db_column='SalesLocation', blank=True, null=True)  # Field name made lowercase.
    nettotal = models.DecimalField(db_column='NetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    referadjdockey = models.BigIntegerField(db_column='ReferAdjDocKey', blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.

    class Meta:
 
        db_table = 'CSGN'


class Csgndtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    itemcode = models.ForeignKey('Itemuom', models.DO_NOTHING, db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    uom = models.ForeignKey('Itemuom', models.DO_NOTHING, db_column='UOM', blank=True, null=True)  # Field name made lowercase.
    location = models.ForeignKey('Location', models.DO_NOTHING, db_column='Location', blank=True, null=True)  # Field name made lowercase.
    batchno = models.ForeignKey('Itembatch', models.DO_NOTHING, db_column='BatchNo', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
    furtherdescription = models.TextField(db_column='FurtherDescription', blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey('Dept', models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    serialnolist = models.TextField(db_column='SerialNoList', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    discount = models.CharField(db_column='Discount', max_length=20, blank=True, null=True)  # Field name made lowercase.
    discountamt = models.DecimalField(db_column='DiscountAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lost = models.CharField(db_column='Lost', max_length=1, blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.

    class Meta:
 
        db_table = 'CSGNDTL'


class Csgnitembalqty(models.Model):
    accno = models.ForeignKey(Branch, models.DO_NOTHING, db_column='AccNo')  # Field name made lowercase.
    itemcode = models.ForeignKey('Itemuom', models.DO_NOTHING, db_column='ItemCode')  # Field name made lowercase.
    uom = models.ForeignKey('Itemuom', models.DO_NOTHING, db_column='UOM')  # Field name made lowercase.
    location = models.ForeignKey('Location', models.DO_NOTHING, db_column='Location')  # Field name made lowercase.
    branchcode = models.ForeignKey(Branch, models.DO_NOTHING, db_column='BranchCode', blank=True, null=True)  # Field name made lowercase.
    batchno = models.ForeignKey('Itembatch', models.DO_NOTHING, db_column='BatchNo', blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey('Dept', models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    balqty = models.DecimalField(db_column='BalQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'CSGNItemBalQty'


class Csgnxfer(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', unique=True, max_length=20)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    fromdebtorcode = models.ForeignKey(Branch, models.DO_NOTHING, db_column='FromDebtorCode')  # Field name made lowercase.
    fromdebtorname = models.CharField(db_column='FromDebtorName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    frombranchcode = models.ForeignKey(Branch, models.DO_NOTHING, db_column='FromBranchCode', blank=True, null=True)  # Field name made lowercase.
    todebtorcode = models.ForeignKey(Branch, models.DO_NOTHING, db_column='ToDebtorCode')  # Field name made lowercase.
    todebtorname = models.CharField(db_column='ToDebtorName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tobranchcode = models.ForeignKey(Branch, models.DO_NOTHING, db_column='ToBranchCode', blank=True, null=True)  # Field name made lowercase.
    ref = models.CharField(db_column='Ref', max_length=40, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=40, blank=True, null=True)  # Field name made lowercase.
    salesagent = models.ForeignKey('Salesagent', models.DO_NOTHING, db_column='SalesAgent', blank=True, null=True)  # Field name made lowercase.
    toinvaddr1 = models.CharField(db_column='ToInvAddr1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    toinvaddr2 = models.CharField(db_column='ToInvAddr2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    toinvaddr3 = models.CharField(db_column='ToInvAddr3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    toinvaddr4 = models.CharField(db_column='ToInvAddr4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tophone1 = models.CharField(db_column='ToPhone1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    tofax1 = models.CharField(db_column='ToFax1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    toattention = models.CharField(db_column='ToAttention', max_length=40, blank=True, null=True)  # Field name made lowercase.
    todeliveraddr1 = models.CharField(db_column='ToDeliverAddr1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    todeliveraddr2 = models.CharField(db_column='ToDeliverAddr2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    todeliveraddr3 = models.CharField(db_column='ToDeliverAddr3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    todeliveraddr4 = models.CharField(db_column='ToDeliverAddr4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    todeliverphone1 = models.CharField(db_column='ToDeliverPhone1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    todeliverfax1 = models.CharField(db_column='ToDeliverFax1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    todelivercontact = models.CharField(db_column='ToDeliverContact', max_length=40, blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    remark1 = models.CharField(db_column='Remark1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark2 = models.CharField(db_column='Remark2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark3 = models.CharField(db_column='Remark3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark4 = models.CharField(db_column='Remark4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    printcount = models.SmallIntegerField(db_column='PrintCount')  # Field name made lowercase.
    cancelled = models.CharField(db_column='Cancelled', max_length=1)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    createduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    externallink = models.TextField(db_column='ExternalLink', blank=True, null=True)  # Field name made lowercase.
    refdocno = models.CharField(db_column='RefDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    cansync = models.CharField(db_column='CanSync', max_length=1)  # Field name made lowercase.

    class Meta:
 
        db_table = 'CSGNXFER'


class Csgnxferdtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    itemcode = models.ForeignKey('Itemuom', models.DO_NOTHING, db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    uom = models.ForeignKey('Itemuom', models.DO_NOTHING, db_column='UOM', blank=True, null=True)  # Field name made lowercase.
    location = models.ForeignKey('Location', models.DO_NOTHING, db_column='Location', blank=True, null=True)  # Field name made lowercase.
    batchno = models.ForeignKey('Itembatch', models.DO_NOTHING, db_column='BatchNo', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
    furtherdescription = models.TextField(db_column='FurtherDescription', blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey('Dept', models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'CSGNXFERDTL'


class Currency(models.Model):
    currencycode = models.CharField(db_column='CurrencyCode', primary_key=True, max_length=5)  # Field name made lowercase.
    currencyword = models.CharField(db_column='CurrencyWord', max_length=40, blank=True, null=True)  # Field name made lowercase.
    currencyword2 = models.CharField(db_column='CurrencyWord2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    currencysymbol = models.CharField(db_column='CurrencySymbol', max_length=6, blank=True, null=True)  # Field name made lowercase.
    bankbuyrate = models.DecimalField(db_column='BankBuyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    banksellrate = models.DecimalField(db_column='BankSellRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    fcgainaccount = models.ForeignKey('Glmast', models.DO_NOTHING, db_column='FCGainAccount', blank=True, null=True)  # Field name made lowercase.
    fclossaccount = models.ForeignKey('Glmast', models.DO_NOTHING, db_column='FCLossAccount', blank=True, null=True)  # Field name made lowercase.
    gainlossjournaltype = models.ForeignKey('Journal', models.DO_NOTHING, db_column='GainLossJournalType', blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.

    class Meta:
 
        db_table = 'CURRENCY'


class Cashflowforecast(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    section = models.CharField(db_column='Section', max_length=20)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate')  # Field name made lowercase.
    frequency = models.CharField(db_column='Frequency', max_length=12)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=2)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'CashFlowForecast'


class Changecount(models.Model):
    tablename = models.CharField(db_column='TableName', primary_key=True, max_length=40)  # Field name made lowercase.
    counter = models.IntegerField(db_column='Counter')  # Field name made lowercase.

    class Meta:
 
        db_table = 'ChangeCount'


class Columnlock(models.Model):
    doctype = models.CharField(db_column='DocType', primary_key=True, max_length=2)  # Field name made lowercase.
    dtltype = models.CharField(db_column='DtlType', max_length=1)  # Field name made lowercase.
    indent = models.CharField(db_column='Indent', max_length=1)  # Field name made lowercase.
    fontstyle = models.CharField(db_column='FontStyle', max_length=1)  # Field name made lowercase.
    mainitem = models.CharField(db_column='MainItem', max_length=1)  # Field name made lowercase.
    numbering = models.CharField(db_column='Numbering', max_length=1)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=1)  # Field name made lowercase.
    batchno = models.CharField(db_column='BatchNo', max_length=1)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=1)  # Field name made lowercase.
    furtherdescription = models.CharField(db_column='FurtherDescription', max_length=1)  # Field name made lowercase.
    yourpono = models.CharField(db_column='YourPONo', max_length=1)  # Field name made lowercase.
    yourpodate = models.CharField(db_column='YourPODate', max_length=1)  # Field name made lowercase.
    yourdono = models.CharField(db_column='YourDONo', max_length=1)  # Field name made lowercase.
    yourdodate = models.CharField(db_column='YourDODate', max_length=1)  # Field name made lowercase.
    ourpono = models.CharField(db_column='OurPONo', max_length=1)  # Field name made lowercase.
    ourpodate = models.CharField(db_column='OurPODate', max_length=1)  # Field name made lowercase.
    deliverydate = models.CharField(db_column='DeliveryDate', max_length=1)  # Field name made lowercase.
    posttostockdate = models.CharField(db_column='PostToStockDate', max_length=1)  # Field name made lowercase.
    projno = models.CharField(db_column='ProjNo', max_length=1)  # Field name made lowercase.
    deptno = models.CharField(db_column='DeptNo', max_length=1)  # Field name made lowercase.
    qty = models.CharField(db_column='Qty', max_length=1)  # Field name made lowercase.
    focqty = models.CharField(db_column='FOCQty', max_length=1)  # Field name made lowercase.
    unitprice = models.CharField(db_column='UnitPrice', max_length=1)  # Field name made lowercase.
    discount = models.CharField(db_column='Discount', max_length=1)  # Field name made lowercase.
    taxtype = models.CharField(db_column='TaxType', max_length=1)  # Field name made lowercase.
    tax = models.CharField(db_column='Tax', max_length=1)  # Field name made lowercase.
    subtotal = models.CharField(db_column='SubTotal', max_length=1)  # Field name made lowercase.
    bonuspoint = models.CharField(db_column='BonusPoint', max_length=1)  # Field name made lowercase.
    printout = models.CharField(db_column='PrintOut', max_length=1)  # Field name made lowercase.
    forconsignment = models.CharField(db_column='ForConsignment', max_length=1)  # Field name made lowercase.
    accno = models.CharField(db_column='AccNo', max_length=1)  # Field name made lowercase.
    foreigncharges = models.CharField(db_column='ForeignCharges', max_length=1)  # Field name made lowercase.
    localcharges = models.CharField(db_column='LocalCharges', max_length=1)  # Field name made lowercase.
    duty = models.CharField(db_column='Duty', max_length=1)  # Field name made lowercase.
    estimateddeliverydate = models.CharField(db_column='EstimatedDeliveryDate', max_length=1)  # Field name made lowercase.
    taxrate = models.CharField(db_column='TaxRate', max_length=1)  # Field name made lowercase.

    class Meta:
 
        db_table = 'ColumnLock'
        unique_together = (('doctype', 'dtltype'),)


class Comment(models.Model):
    commentkey = models.BigAutoField(db_column='CommentKey', primary_key=True)  # Field name made lowercase.
    commenttype = models.SmallIntegerField(db_column='CommentType')  # Field name made lowercase.
    commentdatetime = models.DateTimeField(db_column='CommentDateTime')  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    doctype = models.CharField(db_column='DocType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'Comment'


class Commission(models.Model):
    salesagent = models.OneToOneField('Salesagent', models.DO_NOTHING, db_column='SalesAgent', primary_key=True)  # Field name made lowercase.
    withinday = models.SmallIntegerField(db_column='WithinDay')  # Field name made lowercase.
    percentage = models.DecimalField(db_column='Percentage', max_digits=18, decimal_places=6)  # Field name made lowercase.

    class Meta:
 
        db_table = 'Commission'
        unique_together = (('salesagent', 'withinday'),)


class Contact(models.Model):
    accno = models.OneToOneField('Glmast', models.DO_NOTHING, db_column='AccNo', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=40)  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=30, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=40, blank=True, null=True)  # Field name made lowercase.
    mobilephone = models.CharField(db_column='MobilePhone', max_length=25, blank=True, null=True)  # Field name made lowercase.
    directphone = models.CharField(db_column='DirectPhone', max_length=25, blank=True, null=True)  # Field name made lowercase.
    directfax = models.CharField(db_column='DirectFax', max_length=25, blank=True, null=True)  # Field name made lowercase.
    emailaddress = models.CharField(db_column='EmailAddress', max_length=80, blank=True, null=True)  # Field name made lowercase.
    imaddress = models.CharField(db_column='IMAddress', max_length=40, blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    openingbonuspoint = models.IntegerField(db_column='OpeningBonusPoint', blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    includeincontactinfo = models.CharField(db_column='IncludeInContactInfo', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'Contact'
        unique_together = (('accno', 'name'),)


class Creditcard(models.Model):
    name = models.CharField(db_column='Name', primary_key=True, max_length=8)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bankaccount = models.ForeignKey('Glmast', models.DO_NOTHING, db_column='BankAccount')  # Field name made lowercase.
    amount1 = models.DecimalField(db_column='Amount1', max_digits=19, decimal_places=2)  # Field name made lowercase.
    amount2 = models.DecimalField(db_column='Amount2', max_digits=19, decimal_places=2)  # Field name made lowercase.
    rate1 = models.DecimalField(db_column='Rate1', max_digits=18, decimal_places=6)  # Field name made lowercase.
    amount3 = models.DecimalField(db_column='Amount3', max_digits=19, decimal_places=2)  # Field name made lowercase.
    amount4 = models.DecimalField(db_column='Amount4', max_digits=19, decimal_places=2)  # Field name made lowercase.
    rate2 = models.DecimalField(db_column='Rate2', max_digits=18, decimal_places=6)  # Field name made lowercase.
    chargecustomer = models.CharField(db_column='ChargeCustomer', max_length=1)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.

    class Meta:
 
        db_table = 'CreditCard'


class Creditcontrolsync(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', max_length=50)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    accno = models.ForeignKey('Glmast', models.DO_NOTHING, db_column='AccNo')  # Field name made lowercase.
    companyname = models.CharField(db_column='CompanyName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    creditlimit = models.DecimalField(db_column='CreditLimit', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    overduelimit = models.DecimalField(db_column='OverdueLimit', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    currentcredit = models.DecimalField(db_column='CurrentCredit', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    currentoverdue = models.DecimalField(db_column='CurrentOverdue', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    overduedetail = models.TextField(db_column='OverdueDetail', blank=True, null=True)  # Field name made lowercase.
    action = models.CharField(db_column='Action', max_length=1, blank=True, null=True)  # Field name made lowercase.
    computername = models.CharField(db_column='ComputerName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    requestdatetime = models.DateTimeField(db_column='RequestDateTime', blank=True, null=True)  # Field name made lowercase.
    createduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='CreatedUserID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'CreditControlSync'


class Creditor(models.Model):
    accno = models.OneToOneField('Glmast', models.DO_NOTHING, db_column='AccNo', primary_key=True)  # Field name made lowercase.
    companyname = models.CharField(db_column='CompanyName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    desc2 = models.CharField(db_column='Desc2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    registerno = models.CharField(db_column='RegisterNo', max_length=25, blank=True, null=True)  # Field name made lowercase.
    address1 = models.CharField(db_column='Address1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    address2 = models.CharField(db_column='Address2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    address3 = models.CharField(db_column='Address3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    address4 = models.CharField(db_column='Address4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    postcode = models.CharField(db_column='PostCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    deliveraddr1 = models.CharField(db_column='DeliverAddr1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliveraddr2 = models.CharField(db_column='DeliverAddr2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliveraddr3 = models.CharField(db_column='DeliverAddr3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliveraddr4 = models.CharField(db_column='DeliverAddr4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliverpostcode = models.CharField(db_column='DeliverPostCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    attention = models.CharField(db_column='Attention', max_length=40, blank=True, null=True)  # Field name made lowercase.
    phone1 = models.CharField(db_column='Phone1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    phone2 = models.CharField(db_column='Phone2', max_length=25, blank=True, null=True)  # Field name made lowercase.
    fax1 = models.CharField(db_column='Fax1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    fax2 = models.CharField(db_column='Fax2', max_length=25, blank=True, null=True)  # Field name made lowercase.
    areacode = models.ForeignKey(Area, models.DO_NOTHING, db_column='AreaCode', blank=True, null=True)  # Field name made lowercase.
    purchaseagent = models.ForeignKey('Purchaseagent', models.DO_NOTHING, db_column='PurchaseAgent', blank=True, null=True)  # Field name made lowercase.
    creditortype = models.ForeignKey('Creditortype', models.DO_NOTHING, db_column='CreditorType', blank=True, null=True)  # Field name made lowercase.
    natureofbusiness = models.CharField(db_column='NatureOfBusiness', max_length=40, blank=True, null=True)  # Field name made lowercase.
    weburl = models.CharField(db_column='WebURL', max_length=80, blank=True, null=True)  # Field name made lowercase.
    emailaddress = models.CharField(db_column='EmailAddress', max_length=80, blank=True, null=True)  # Field name made lowercase.
    displayterm = models.ForeignKey('Terms', models.DO_NOTHING, db_column='DisplayTerm')  # Field name made lowercase.
    creditlimit = models.DecimalField(db_column='CreditLimit', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    agingon = models.CharField(db_column='AgingOn', max_length=1, blank=True, null=True)  # Field name made lowercase.
    statementtype = models.CharField(db_column='StatementType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    currencycode = models.ForeignKey(Currency, models.DO_NOTHING, db_column='CurrencyCode')  # Field name made lowercase.
    allowexceedcreditlimit = models.CharField(db_column='AllowExceedCreditLimit', max_length=1)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    exemptno = models.CharField(db_column='ExemptNo', max_length=60, blank=True, null=True)  # Field name made lowercase.
    expirydate = models.DateTimeField(db_column='ExpiryDate', blank=True, null=True)  # Field name made lowercase.
    pricecategory = models.ForeignKey('Pricecategory', models.DO_NOTHING, db_column='PriceCategory', blank=True, null=True)  # Field name made lowercase.
    taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='TaxType', blank=True, null=True)  # Field name made lowercase.
    discountpercent = models.DecimalField(db_column='DiscountPercent', max_digits=18, decimal_places=6)  # Field name made lowercase.
    detaildiscount = models.CharField(db_column='DetailDiscount', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    createduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    overduelimit = models.DecimalField(db_column='OverdueLimit', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    poblockstatus = models.SmallIntegerField(db_column='POBlockStatus', blank=True, null=True)  # Field name made lowercase.
    gnblockstatus = models.SmallIntegerField(db_column='GNBlockStatus', blank=True, null=True)  # Field name made lowercase.
    piblockstatus = models.SmallIntegerField(db_column='PIBlockStatus', blank=True, null=True)  # Field name made lowercase.
    cpblockstatus = models.SmallIntegerField(db_column='CPBlockStatus', blank=True, null=True)  # Field name made lowercase.
    poblockmessage = models.CharField(db_column='POBlockMessage', max_length=40, blank=True, null=True)  # Field name made lowercase.
    gnblockmessage = models.CharField(db_column='GNBlockMessage', max_length=40, blank=True, null=True)  # Field name made lowercase.
    piblockmessage = models.CharField(db_column='PIBlockMessage', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cpblockmessage = models.CharField(db_column='CPBlockMessage', max_length=40, blank=True, null=True)  # Field name made lowercase.
    externallink = models.TextField(db_column='ExternalLink', blank=True, null=True)  # Field name made lowercase.
    isgroupcompany = models.CharField(db_column='IsGroupCompany', max_length=1)  # Field name made lowercase.
    isactive = models.CharField(db_column='IsActive', max_length=1)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    contactinfo = models.TextField(db_column='ContactInfo', blank=True, null=True)  # Field name made lowercase.
    accountgroup = models.CharField(db_column='AccountGroup', max_length=12, blank=True, null=True)  # Field name made lowercase.
    markupratio = models.DecimalField(db_column='MarkupRatio', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    taxregisterno = models.CharField(db_column='TaxRegisterNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    calcdiscountonunitprice = models.CharField(db_column='CalcDiscountOnUnitPrice', max_length=1, blank=True, null=True)  # Field name made lowercase.
    gststatusverifieddate = models.DateTimeField(db_column='GSTStatusVerifiedDate', blank=True, null=True)  # Field name made lowercase.
    inclusivetax = models.CharField(db_column='InclusiveTax', max_length=1)  # Field name made lowercase.
    selfbilledapprovalno = models.CharField(db_column='SelfBilledApprovalNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    roundingmethod = models.IntegerField(db_column='RoundingMethod')  # Field name made lowercase.
    receiptwithholdingtaxcode = models.CharField(db_column='ReceiptWithholdingTaxCode', max_length=14, blank=True, null=True)  # Field name made lowercase.
    paymentwithholdingtaxcode = models.CharField(db_column='PaymentWithholdingTaxCode', max_length=14, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'Creditor'


class Creditortype(models.Model):
    creditortype = models.CharField(db_column='CreditorType', primary_key=True, max_length=20)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=40, blank=True, null=True)  # Field name made lowercase.
    desc2 = models.CharField(db_column='Desc2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    isactive = models.CharField(db_column='IsActive', max_length=1)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.

    class Meta:
 
        db_table = 'CreditorType'


class Criteria(models.Model):
    criterianame = models.CharField(db_column='CriteriaName', primary_key=True, max_length=80)  # Field name made lowercase.
    criteriatype = models.CharField(db_column='CriteriaType', max_length=8)  # Field name made lowercase.
    data = models.BinaryField(db_column='Data', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'Criteria'
        unique_together = (('criterianame', 'criteriatype'),)


class Currrate(models.Model):
    currencycode = models.OneToOneField(Currency, models.DO_NOTHING, db_column='CurrencyCode', primary_key=True)  # Field name made lowercase.
    fromdate = models.DateTimeField(db_column='FromDate')  # Field name made lowercase.
    todate = models.DateTimeField(db_column='ToDate')  # Field name made lowercase.
    bankbuyrate = models.DecimalField(db_column='BankBuyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    banksellrate = models.DecimalField(db_column='BankSellRate', max_digits=19, decimal_places=12)  # Field name made lowercase.

    class Meta:
 
        db_table = 'CurrRate'
        unique_together = (('currencycode', 'fromdate', 'todate'),)


class Dn(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', unique=True, max_length=20)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    debtorcode = models.ForeignKey(Branch, models.DO_NOTHING, db_column='DebtorCode')  # Field name made lowercase.
    debtorname = models.CharField(db_column='DebtorName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dntype = models.ForeignKey('Dntype', models.DO_NOTHING, db_column='DNType', blank=True, null=True)  # Field name made lowercase.
    ref = models.CharField(db_column='Ref', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ourinvoiceno = models.CharField(db_column='OurInvoiceNo', max_length=40, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=80, blank=True, null=True)  # Field name made lowercase.
    displayterm = models.ForeignKey('Terms', models.DO_NOTHING, db_column='DisplayTerm')  # Field name made lowercase.
    salesagent = models.ForeignKey('Salesagent', models.DO_NOTHING, db_column='SalesAgent', blank=True, null=True)  # Field name made lowercase.
    invaddr1 = models.CharField(db_column='InvAddr1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr2 = models.CharField(db_column='InvAddr2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr3 = models.CharField(db_column='InvAddr3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr4 = models.CharField(db_column='InvAddr4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    phone1 = models.CharField(db_column='Phone1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    fax1 = models.CharField(db_column='Fax1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    attention = models.CharField(db_column='Attention', max_length=40, blank=True, null=True)  # Field name made lowercase.
    branchcode = models.ForeignKey(Branch, models.DO_NOTHING, db_column='BranchCode', blank=True, null=True)  # Field name made lowercase.
    deliveraddr1 = models.CharField(db_column='DeliverAddr1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliveraddr2 = models.CharField(db_column='DeliverAddr2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliveraddr3 = models.CharField(db_column='DeliverAddr3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliveraddr4 = models.CharField(db_column='DeliverAddr4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliverphone1 = models.CharField(db_column='DeliverPhone1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    deliverfax1 = models.CharField(db_column='DeliverFax1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    delivercontact = models.CharField(db_column='DeliverContact', max_length=40, blank=True, null=True)  # Field name made lowercase.
    salesexemptionno = models.CharField(db_column='SalesExemptionNo', max_length=60, blank=True, null=True)  # Field name made lowercase.
    salesexemptionexpirydate = models.DateTimeField(db_column='SalesExemptionExpiryDate', blank=True, null=True)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1param = models.DecimalField(db_column='Footer1Param', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1amt = models.DecimalField(db_column='Footer1Amt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1localamt = models.DecimalField(db_column='Footer1LocalAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='Footer1TaxType', blank=True, null=True)  # Field name made lowercase.
    footer2param = models.DecimalField(db_column='Footer2Param', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2amt = models.DecimalField(db_column='Footer2Amt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2localamt = models.DecimalField(db_column='Footer2LocalAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='Footer2TaxType', blank=True, null=True)  # Field name made lowercase.
    footer3param = models.DecimalField(db_column='Footer3Param', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3amt = models.DecimalField(db_column='Footer3Amt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3localamt = models.DecimalField(db_column='Footer3LocalAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='Footer3TaxType', blank=True, null=True)  # Field name made lowercase.
    currencycode = models.ForeignKey(Currency, models.DO_NOTHING, db_column='CurrencyCode')  # Field name made lowercase.
    currencyrate = models.DecimalField(db_column='CurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    nettotal = models.DecimalField(db_column='NetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localnettotal = models.DecimalField(db_column='LocalNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    analysisnettotal = models.DecimalField(db_column='AnalysisNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localanalysisnettotal = models.DecimalField(db_column='LocalAnalysisNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtotalcost = models.DecimalField(db_column='LocalTotalCost', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtax = models.DecimalField(db_column='LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    totalbonuspoint = models.DecimalField(db_column='TotalBonusPoint', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    posttostock = models.CharField(db_column='PostToStock', max_length=1)  # Field name made lowercase.
    posttogl = models.CharField(db_column='PostToGL', max_length=1)  # Field name made lowercase.
    referdockey = models.BigIntegerField(db_column='ReferDocKey', blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    remark1 = models.CharField(db_column='Remark1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark2 = models.CharField(db_column='Remark2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark3 = models.CharField(db_column='Remark3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark4 = models.CharField(db_column='Remark4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    printcount = models.SmallIntegerField(db_column='PrintCount')  # Field name made lowercase.
    cancelled = models.CharField(db_column='Cancelled', max_length=1)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    createduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    externallink = models.TextField(db_column='ExternalLink', blank=True, null=True)  # Field name made lowercase.
    refdocno = models.CharField(db_column='RefDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cansync = models.CharField(db_column='CanSync', max_length=1)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    memberno = models.ForeignKey('Member', models.DO_NOTHING, db_column='MemberNo', blank=True, null=True)  # Field name made lowercase.
    reallocatepurchasebyproject = models.CharField(db_column='ReallocatePurchaseByProject', max_length=1)  # Field name made lowercase.
    reallocatepurchasebyprojectjedockey = models.BigIntegerField(db_column='ReallocatePurchaseByProjectJEDocKey', blank=True, null=True)  # Field name made lowercase.
    refno2 = models.CharField(db_column='RefNo2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    saleslocation = models.ForeignKey('Location', models.DO_NOTHING, db_column='SalesLocation', blank=True, null=True)  # Field name made lowercase.
    footer1tax = models.DecimalField(db_column='Footer1Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1localtax = models.DecimalField(db_column='Footer1LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2tax = models.DecimalField(db_column='Footer2Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2localtax = models.DecimalField(db_column='Footer2LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3tax = models.DecimalField(db_column='Footer3Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3localtax = models.DecimalField(db_column='Footer3LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    extax = models.DecimalField(db_column='ExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localextax = models.DecimalField(db_column='LocalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    yourpono = models.CharField(db_column='YourPONo', max_length=25, blank=True, null=True)  # Field name made lowercase.
    yourpodate = models.DateTimeField(db_column='YourPODate', blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.
    reallocatepurchasebyprojectno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ReallocatePurchaseByProjectNo', blank=True, null=True)  # Field name made lowercase.
    totaxcurrencyrate = models.DecimalField(db_column='ToTaxCurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    calcdiscountonunitprice = models.CharField(db_column='CalcDiscountOnUnitPrice', max_length=1, blank=True, null=True)  # Field name made lowercase.
    taxdocno = models.CharField(db_column='TaxDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    totalextax = models.DecimalField(db_column='TotalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxableamt = models.DecimalField(db_column='TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    reason = models.CharField(db_column='Reason', max_length=80, blank=True, null=True)  # Field name made lowercase.
    inclusivetax = models.CharField(db_column='InclusiveTax', max_length=1)  # Field name made lowercase.
    footer1taxrate = models.DecimalField(db_column='Footer1TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    footer2taxrate = models.DecimalField(db_column='Footer2TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    footer3taxrate = models.DecimalField(db_column='Footer3TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    taxdate = models.DateTimeField(db_column='TaxDate', blank=True, null=True)  # Field name made lowercase.
    roundingmethod = models.IntegerField(db_column='RoundingMethod')  # Field name made lowercase.
    localtaxableamt = models.DecimalField(db_column='LocalTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytax = models.DecimalField(db_column='TaxCurrencyTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxableamt = models.DecimalField(db_column='TaxCurrencyTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'DN'


class Dndtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    focdtlkey = models.BigIntegerField(db_column='FOCDtlKey', blank=True, null=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    indent = models.SmallIntegerField(db_column='Indent', blank=True, null=True)  # Field name made lowercase.
    fontstyle = models.ForeignKey('Fontstyle', models.DO_NOTHING, db_column='FontStyle', blank=True, null=True)  # Field name made lowercase.
    mainitem = models.CharField(db_column='MainItem', max_length=1)  # Field name made lowercase.
    numbering = models.CharField(db_column='Numbering', max_length=6, blank=True, null=True)  # Field name made lowercase.
    itemcode = models.ForeignKey('Itemuom', models.DO_NOTHING, db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    location = models.ForeignKey('Location', models.DO_NOTHING, db_column='Location', blank=True, null=True)  # Field name made lowercase.
    batchno = models.ForeignKey('Itembatch', models.DO_NOTHING, db_column='BatchNo', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    furtherdescription = models.TextField(db_column='FurtherDescription', blank=True, null=True)  # Field name made lowercase.
    posttostockdate = models.DateTimeField(db_column='PostToStockDate', blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey('Dept', models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    uom = models.ForeignKey('Itemuom', models.DO_NOTHING, db_column='UOM', blank=True, null=True)  # Field name made lowercase.
    useruom = models.CharField(db_column='UserUOM', max_length=8, blank=True, null=True)  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    smallestqty = models.DecimalField(db_column='SmallestQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    focqty = models.DecimalField(db_column='FOCQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    smallestunitprice = models.DecimalField(db_column='SmallestUnitPrice', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    discount = models.CharField(db_column='Discount', max_length=20, blank=True, null=True)  # Field name made lowercase.
    discountamt = models.DecimalField(db_column='DiscountAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='TaxType', blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localsubtotal = models.DecimalField(db_column='LocalSubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtotalcost = models.DecimalField(db_column='LocalTotalCost', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    localfoctotalcost = models.DecimalField(db_column='LocalFOCTotalCost', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    bonuspoint = models.DecimalField(db_column='BonusPoint', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    printout = models.CharField(db_column='PrintOut', max_length=1)  # Field name made lowercase.
    dtltype = models.CharField(db_column='DtlType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    calcbypercent = models.DecimalField(db_column='CalcByPercent', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    addtosubtotal = models.CharField(db_column='AddToSubTotal', max_length=1)  # Field name made lowercase.
    accno = models.ForeignKey('Glmast', models.DO_NOTHING, db_column='AccNo', blank=True, null=True)  # Field name made lowercase.
    serialnolist = models.TextField(db_column='SerialNoList', blank=True, null=True)  # Field name made lowercase.
    packagedockey = models.BigIntegerField(db_column='PackageDocKey', blank=True, null=True)  # Field name made lowercase.
    parentdtlkey = models.BigIntegerField(db_column='ParentDtlKey', blank=True, null=True)  # Field name made lowercase.
    subqty = models.DecimalField(db_column='SubQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    iscalcbonuspoint = models.CharField(db_column='IsCalcBonusPoint', max_length=1, blank=True, null=True)  # Field name made lowercase.
    subtotalextax = models.DecimalField(db_column='SubTotalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtax = models.DecimalField(db_column='LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    yourpono = models.CharField(db_column='YourPONo', max_length=25, blank=True, null=True)  # Field name made lowercase.
    yourpodate = models.DateTimeField(db_column='YourPODate', blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.
    ruleno = models.BigIntegerField(db_column='RuleNo', blank=True, null=True)  # Field name made lowercase.
    taxableamt = models.DecimalField(db_column='TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxadjustment = models.DecimalField(db_column='TaxAdjustment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxexportcountry = models.CharField(db_column='TaxExportCountry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    localsubtotalextax = models.DecimalField(db_column='LocalSubTotalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    extradiscountamt = models.DecimalField(db_column='ExtraDiscountAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxrate = models.DecimalField(db_column='TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    localtaxadjustment = models.DecimalField(db_column='LocalTaxAdjustment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtaxableamt = models.DecimalField(db_column='LocalTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytax = models.DecimalField(db_column='TaxCurrencyTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxableamt = models.DecimalField(db_column='TaxCurrencyTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxpermitno = models.CharField(db_column='TaxPermitNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    supplypurchase = models.CharField(db_column='SupplyPurchase', max_length=1, blank=True, null=True)  # Field name made lowercase.
    salesexemptionno = models.CharField(db_column='SalesExemptionNo', max_length=60, blank=True, null=True)  # Field name made lowercase.
    tariffcode = models.ForeignKey('Tariff', models.DO_NOTHING, db_column='TariffCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'DNDTL'


class Dntype(models.Model):
    dntype = models.CharField(db_column='DNType', primary_key=True, max_length=12)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=40, blank=True, null=True)  # Field name made lowercase.
    desc2 = models.CharField(db_column='Desc2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    isactive = models.CharField(db_column='IsActive', max_length=1)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.

    class Meta:
 
        db_table = 'DNType'


class Do(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', unique=True, max_length=20)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    debtorcode = models.ForeignKey(Branch, models.DO_NOTHING, db_column='DebtorCode')  # Field name made lowercase.
    debtorname = models.CharField(db_column='DebtorName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ref = models.CharField(db_column='Ref', max_length=40, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=80, blank=True, null=True)  # Field name made lowercase.
    displayterm = models.ForeignKey('Terms', models.DO_NOTHING, db_column='DisplayTerm')  # Field name made lowercase.
    salesagent = models.ForeignKey('Salesagent', models.DO_NOTHING, db_column='SalesAgent', blank=True, null=True)  # Field name made lowercase.
    invaddr1 = models.CharField(db_column='InvAddr1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr2 = models.CharField(db_column='InvAddr2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr3 = models.CharField(db_column='InvAddr3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr4 = models.CharField(db_column='InvAddr4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    phone1 = models.CharField(db_column='Phone1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    fax1 = models.CharField(db_column='Fax1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    attention = models.CharField(db_column='Attention', max_length=40, blank=True, null=True)  # Field name made lowercase.
    branchcode = models.ForeignKey(Branch, models.DO_NOTHING, db_column='BranchCode', blank=True, null=True)  # Field name made lowercase.
    deliveraddr1 = models.CharField(db_column='DeliverAddr1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliveraddr2 = models.CharField(db_column='DeliverAddr2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliveraddr3 = models.CharField(db_column='DeliverAddr3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliveraddr4 = models.CharField(db_column='DeliverAddr4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliverphone1 = models.CharField(db_column='DeliverPhone1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    deliverfax1 = models.CharField(db_column='DeliverFax1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    delivercontact = models.CharField(db_column='DeliverContact', max_length=40, blank=True, null=True)  # Field name made lowercase.
    salesexemptionno = models.CharField(db_column='SalesExemptionNo', max_length=60, blank=True, null=True)  # Field name made lowercase.
    salesexemptionexpirydate = models.DateTimeField(db_column='SalesExemptionExpiryDate', blank=True, null=True)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1param = models.DecimalField(db_column='Footer1Param', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1amt = models.DecimalField(db_column='Footer1Amt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1localamt = models.DecimalField(db_column='Footer1LocalAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='Footer1TaxType', blank=True, null=True)  # Field name made lowercase.
    footer2param = models.DecimalField(db_column='Footer2Param', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2amt = models.DecimalField(db_column='Footer2Amt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2localamt = models.DecimalField(db_column='Footer2LocalAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='Footer2TaxType', blank=True, null=True)  # Field name made lowercase.
    footer3param = models.DecimalField(db_column='Footer3Param', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3amt = models.DecimalField(db_column='Footer3Amt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3localamt = models.DecimalField(db_column='Footer3LocalAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='Footer3TaxType', blank=True, null=True)  # Field name made lowercase.
    currencycode = models.ForeignKey(Currency, models.DO_NOTHING, db_column='CurrencyCode')  # Field name made lowercase.
    currencyrate = models.DecimalField(db_column='CurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    nettotal = models.DecimalField(db_column='NetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localnettotal = models.DecimalField(db_column='LocalNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    analysisnettotal = models.DecimalField(db_column='AnalysisNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localanalysisnettotal = models.DecimalField(db_column='LocalAnalysisNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtotalcost = models.DecimalField(db_column='LocalTotalCost', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtax = models.DecimalField(db_column='LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    posttostock = models.CharField(db_column='PostToStock', max_length=1)  # Field name made lowercase.
    transferable = models.CharField(db_column='Transferable', max_length=1)  # Field name made lowercase.
    todoctype = models.CharField(db_column='ToDocType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    todockey = models.BigIntegerField(db_column='ToDocKey', blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    remark1 = models.CharField(db_column='Remark1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark2 = models.CharField(db_column='Remark2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark3 = models.CharField(db_column='Remark3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark4 = models.CharField(db_column='Remark4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    printcount = models.SmallIntegerField(db_column='PrintCount')  # Field name made lowercase.
    cancelled = models.CharField(db_column='Cancelled', max_length=1)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    createduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    externallink = models.TextField(db_column='ExternalLink', blank=True, null=True)  # Field name made lowercase.
    refdocno = models.CharField(db_column='RefDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cansync = models.CharField(db_column='CanSync', max_length=1)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    todtlkey = models.BigIntegerField(db_column='ToDtlKey', blank=True, null=True)  # Field name made lowercase.
    fulltransferoption = models.CharField(db_column='FullTransferOption', max_length=1, blank=True, null=True)  # Field name made lowercase.
    shipvia = models.ForeignKey('Shippingmethod', models.DO_NOTHING, db_column='ShipVia', blank=True, null=True)  # Field name made lowercase.
    shipinfo = models.CharField(db_column='ShipInfo', max_length=40, blank=True, null=True)  # Field name made lowercase.
    saleslocation = models.ForeignKey('Location', models.DO_NOTHING, db_column='SalesLocation', blank=True, null=True)  # Field name made lowercase.
    footer1tax = models.DecimalField(db_column='Footer1Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1localtax = models.DecimalField(db_column='Footer1LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2tax = models.DecimalField(db_column='Footer2Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2localtax = models.DecimalField(db_column='Footer2LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3tax = models.DecimalField(db_column='Footer3Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3localtax = models.DecimalField(db_column='Footer3LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    extax = models.DecimalField(db_column='ExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localextax = models.DecimalField(db_column='LocalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    yourpono = models.CharField(db_column='YourPONo', max_length=25, blank=True, null=True)  # Field name made lowercase.
    yourpodate = models.DateTimeField(db_column='YourPODate', blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.
    totaxcurrencyrate = models.DecimalField(db_column='ToTaxCurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    calcdiscountonunitprice = models.CharField(db_column='CalcDiscountOnUnitPrice', max_length=1, blank=True, null=True)  # Field name made lowercase.
    totalextax = models.DecimalField(db_column='TotalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxableamt = models.DecimalField(db_column='TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    inclusivetax = models.CharField(db_column='InclusiveTax', max_length=1)  # Field name made lowercase.
    gstjedockey = models.BigIntegerField(db_column='GSTJEDocKey', blank=True, null=True)  # Field name made lowercase.
    footer1taxrate = models.DecimalField(db_column='Footer1TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    footer2taxrate = models.DecimalField(db_column='Footer2TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    footer3taxrate = models.DecimalField(db_column='Footer3TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    roundingmethod = models.IntegerField(db_column='RoundingMethod')  # Field name made lowercase.
    localtaxableamt = models.DecimalField(db_column='LocalTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytax = models.DecimalField(db_column='TaxCurrencyTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxableamt = models.DecimalField(db_column='TaxCurrencyTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'DO'


class Dodtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    focdtlkey = models.BigIntegerField(db_column='FOCDtlKey', blank=True, null=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    indent = models.SmallIntegerField(db_column='Indent', blank=True, null=True)  # Field name made lowercase.
    fontstyle = models.ForeignKey('Fontstyle', models.DO_NOTHING, db_column='FontStyle', blank=True, null=True)  # Field name made lowercase.
    mainitem = models.CharField(db_column='MainItem', max_length=1)  # Field name made lowercase.
    numbering = models.CharField(db_column='Numbering', max_length=6, blank=True, null=True)  # Field name made lowercase.
    itemcode = models.ForeignKey('Itemuom', models.DO_NOTHING, db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    location = models.ForeignKey('Location', models.DO_NOTHING, db_column='Location', blank=True, null=True)  # Field name made lowercase.
    batchno = models.ForeignKey('Itembatch', models.DO_NOTHING, db_column='BatchNo', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    furtherdescription = models.TextField(db_column='FurtherDescription', blank=True, null=True)  # Field name made lowercase.
    yourpono = models.CharField(db_column='YourPONo', max_length=25, blank=True, null=True)  # Field name made lowercase.
    yourpodate = models.DateTimeField(db_column='YourPODate', blank=True, null=True)  # Field name made lowercase.
    posttostockdate = models.DateTimeField(db_column='PostToStockDate', blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey('Dept', models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    uom = models.ForeignKey('Itemuom', models.DO_NOTHING, db_column='UOM', blank=True, null=True)  # Field name made lowercase.
    useruom = models.CharField(db_column='UserUOM', max_length=8, blank=True, null=True)  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    smallestqty = models.DecimalField(db_column='SmallestQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    transferedqty = models.DecimalField(db_column='TransferedQty', max_digits=25, decimal_places=8)  # Field name made lowercase.
    focqty = models.DecimalField(db_column='FOCQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    foctransferedqty = models.DecimalField(db_column='FOCTransferedQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    smallestunitprice = models.DecimalField(db_column='SmallestUnitPrice', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    discount = models.CharField(db_column='Discount', max_length=20, blank=True, null=True)  # Field name made lowercase.
    discountamt = models.DecimalField(db_column='DiscountAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='TaxType', blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localsubtotal = models.DecimalField(db_column='LocalSubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtotalcost = models.DecimalField(db_column='LocalTotalCost', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    localfoctotalcost = models.DecimalField(db_column='LocalFOCTotalCost', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    transferable = models.CharField(db_column='Transferable', max_length=1)  # Field name made lowercase.
    printout = models.CharField(db_column='PrintOut', max_length=1)  # Field name made lowercase.
    dtltype = models.CharField(db_column='DtlType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    calcbypercent = models.DecimalField(db_column='CalcByPercent', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    addtosubtotal = models.CharField(db_column='AddToSubTotal', max_length=1)  # Field name made lowercase.
    fromdoctype = models.CharField(db_column='FromDocType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    fromdocno = models.CharField(db_column='FromDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fromdocdtlkey = models.BigIntegerField(db_column='FromDocDtlKey', blank=True, null=True)  # Field name made lowercase.
    fulltransferoption = models.CharField(db_column='FullTransferOption', max_length=1, blank=True, null=True)  # Field name made lowercase.
    isvaluetransfereditem = models.CharField(db_column='IsValueTransferedItem', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fulltransferfromdoclist = models.TextField(db_column='FullTransferFromDocList', blank=True, null=True)  # Field name made lowercase.
    serialnolist = models.TextField(db_column='SerialNoList', blank=True, null=True)  # Field name made lowercase.
    estimateddeliverydate = models.CharField(db_column='EstimatedDeliveryDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    packagedockey = models.BigIntegerField(db_column='PackageDocKey', blank=True, null=True)  # Field name made lowercase.
    parentdtlkey = models.BigIntegerField(db_column='ParentDtlKey', blank=True, null=True)  # Field name made lowercase.
    subqty = models.DecimalField(db_column='SubQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    subtotalextax = models.DecimalField(db_column='SubTotalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtax = models.DecimalField(db_column='LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.
    ruleno = models.BigIntegerField(db_column='RuleNo', blank=True, null=True)  # Field name made lowercase.
    deliverydate = models.DateTimeField(db_column='DeliveryDate', blank=True, null=True)  # Field name made lowercase.
    taxableamt = models.DecimalField(db_column='TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxadjustment = models.DecimalField(db_column='TaxAdjustment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localsubtotalextax = models.DecimalField(db_column='LocalSubTotalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    extradiscountamt = models.DecimalField(db_column='ExtraDiscountAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxrate = models.DecimalField(db_column='TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    localtaxadjustment = models.DecimalField(db_column='LocalTaxAdjustment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    accno = models.ForeignKey('Glmast', models.DO_NOTHING, db_column='AccNo', blank=True, null=True)  # Field name made lowercase.
    localtaxableamt = models.DecimalField(db_column='LocalTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytax = models.DecimalField(db_column='TaxCurrencyTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxableamt = models.DecimalField(db_column='TaxCurrencyTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    salesexemptionno = models.CharField(db_column='SalesExemptionNo', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'DODTL'


class Dr(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', unique=True, max_length=20)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    debtorcode = models.ForeignKey(Branch, models.DO_NOTHING, db_column='DebtorCode')  # Field name made lowercase.
    debtorname = models.CharField(db_column='DebtorName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ref = models.CharField(db_column='Ref', max_length=40, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=80, blank=True, null=True)  # Field name made lowercase.
    displayterm = models.ForeignKey('Terms', models.DO_NOTHING, db_column='DisplayTerm')  # Field name made lowercase.
    salesagent = models.ForeignKey('Salesagent', models.DO_NOTHING, db_column='SalesAgent', blank=True, null=True)  # Field name made lowercase.
    invaddr1 = models.CharField(db_column='InvAddr1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr2 = models.CharField(db_column='InvAddr2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr3 = models.CharField(db_column='InvAddr3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr4 = models.CharField(db_column='InvAddr4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    phone1 = models.CharField(db_column='Phone1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    fax1 = models.CharField(db_column='Fax1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    attention = models.CharField(db_column='Attention', max_length=40, blank=True, null=True)  # Field name made lowercase.
    branchcode = models.ForeignKey(Branch, models.DO_NOTHING, db_column='BranchCode', blank=True, null=True)  # Field name made lowercase.
    deliveraddr1 = models.CharField(db_column='DeliverAddr1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliveraddr2 = models.CharField(db_column='DeliverAddr2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliveraddr3 = models.CharField(db_column='DeliverAddr3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliveraddr4 = models.CharField(db_column='DeliverAddr4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliverphone1 = models.CharField(db_column='DeliverPhone1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    deliverfax1 = models.CharField(db_column='DeliverFax1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    delivercontact = models.CharField(db_column='DeliverContact', max_length=40, blank=True, null=True)  # Field name made lowercase.
    salesexemptionno = models.CharField(db_column='SalesExemptionNo', max_length=60, blank=True, null=True)  # Field name made lowercase.
    salesexemptionexpirydate = models.DateTimeField(db_column='SalesExemptionExpiryDate', blank=True, null=True)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1param = models.DecimalField(db_column='Footer1Param', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1amt = models.DecimalField(db_column='Footer1Amt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1localamt = models.DecimalField(db_column='Footer1LocalAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='Footer1TaxType', blank=True, null=True)  # Field name made lowercase.
    footer2param = models.DecimalField(db_column='Footer2Param', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2amt = models.DecimalField(db_column='Footer2Amt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2localamt = models.DecimalField(db_column='Footer2LocalAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='Footer2TaxType', blank=True, null=True)  # Field name made lowercase.
    footer3param = models.DecimalField(db_column='Footer3Param', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3amt = models.DecimalField(db_column='Footer3Amt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3localamt = models.DecimalField(db_column='Footer3LocalAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='Footer3TaxType', blank=True, null=True)  # Field name made lowercase.
    currencycode = models.ForeignKey(Currency, models.DO_NOTHING, db_column='CurrencyCode')  # Field name made lowercase.
    currencyrate = models.DecimalField(db_column='CurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    nettotal = models.DecimalField(db_column='NetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localnettotal = models.DecimalField(db_column='LocalNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    analysisnettotal = models.DecimalField(db_column='AnalysisNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localanalysisnettotal = models.DecimalField(db_column='LocalAnalysisNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtotalcost = models.DecimalField(db_column='LocalTotalCost', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtax = models.DecimalField(db_column='LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    posttostock = models.CharField(db_column='PostToStock', max_length=1)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    remark1 = models.CharField(db_column='Remark1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark2 = models.CharField(db_column='Remark2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark3 = models.CharField(db_column='Remark3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark4 = models.CharField(db_column='Remark4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    printcount = models.SmallIntegerField(db_column='PrintCount')  # Field name made lowercase.
    cancelled = models.CharField(db_column='Cancelled', max_length=1)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    createduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    externallink = models.TextField(db_column='ExternalLink', blank=True, null=True)  # Field name made lowercase.
    refdocno = models.CharField(db_column='RefDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cansync = models.CharField(db_column='CanSync', max_length=1)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    saleslocation = models.ForeignKey('Location', models.DO_NOTHING, db_column='SalesLocation', blank=True, null=True)  # Field name made lowercase.
    footer1tax = models.DecimalField(db_column='Footer1Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1localtax = models.DecimalField(db_column='Footer1LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2tax = models.DecimalField(db_column='Footer2Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2localtax = models.DecimalField(db_column='Footer2LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3tax = models.DecimalField(db_column='Footer3Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3localtax = models.DecimalField(db_column='Footer3LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    extax = models.DecimalField(db_column='ExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localextax = models.DecimalField(db_column='LocalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    yourpono = models.CharField(db_column='YourPONo', max_length=25, blank=True, null=True)  # Field name made lowercase.
    yourpodate = models.DateTimeField(db_column='YourPODate', blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.
    totaxcurrencyrate = models.DecimalField(db_column='ToTaxCurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    calcdiscountonunitprice = models.CharField(db_column='CalcDiscountOnUnitPrice', max_length=1, blank=True, null=True)  # Field name made lowercase.
    totalextax = models.DecimalField(db_column='TotalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxableamt = models.DecimalField(db_column='TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    inclusivetax = models.CharField(db_column='InclusiveTax', max_length=1)  # Field name made lowercase.
    footer1taxrate = models.DecimalField(db_column='Footer1TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    footer2taxrate = models.DecimalField(db_column='Footer2TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    footer3taxrate = models.DecimalField(db_column='Footer3TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    roundingmethod = models.IntegerField(db_column='RoundingMethod')  # Field name made lowercase.
    localtaxableamt = models.DecimalField(db_column='LocalTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytax = models.DecimalField(db_column='TaxCurrencyTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxableamt = models.DecimalField(db_column='TaxCurrencyTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'DR'


class Drdtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    focdtlkey = models.BigIntegerField(db_column='FOCDtlKey', blank=True, null=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    indent = models.SmallIntegerField(db_column='Indent', blank=True, null=True)  # Field name made lowercase.
    fontstyle = models.ForeignKey('Fontstyle', models.DO_NOTHING, db_column='FontStyle', blank=True, null=True)  # Field name made lowercase.
    mainitem = models.CharField(db_column='MainItem', max_length=1)  # Field name made lowercase.
    numbering = models.CharField(db_column='Numbering', max_length=6, blank=True, null=True)  # Field name made lowercase.
    itemcode = models.ForeignKey('Itemuom', models.DO_NOTHING, db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    location = models.ForeignKey('Location', models.DO_NOTHING, db_column='Location', blank=True, null=True)  # Field name made lowercase.
    batchno = models.ForeignKey('Itembatch', models.DO_NOTHING, db_column='BatchNo', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    furtherdescription = models.TextField(db_column='FurtherDescription', blank=True, null=True)  # Field name made lowercase.
    yourpono = models.CharField(db_column='YourPONo', max_length=25, blank=True, null=True)  # Field name made lowercase.
    yourpodate = models.DateTimeField(db_column='YourPODate', blank=True, null=True)  # Field name made lowercase.
    posttostockdate = models.DateTimeField(db_column='PostToStockDate', blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey('Dept', models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    uom = models.ForeignKey('Itemuom', models.DO_NOTHING, db_column='UOM', blank=True, null=True)  # Field name made lowercase.
    useruom = models.CharField(db_column='UserUOM', max_length=8, blank=True, null=True)  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    smallestqty = models.DecimalField(db_column='SmallestQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    focqty = models.DecimalField(db_column='FOCQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    smallestunitprice = models.DecimalField(db_column='SmallestUnitPrice', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    discount = models.CharField(db_column='Discount', max_length=20, blank=True, null=True)  # Field name made lowercase.
    discountamt = models.DecimalField(db_column='DiscountAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='TaxType', blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localsubtotal = models.DecimalField(db_column='LocalSubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtotalcost = models.DecimalField(db_column='LocalTotalCost', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    localfoctotalcost = models.DecimalField(db_column='LocalFOCTotalCost', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    printout = models.CharField(db_column='PrintOut', max_length=1)  # Field name made lowercase.
    dtltype = models.CharField(db_column='DtlType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    calcbypercent = models.DecimalField(db_column='CalcByPercent', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    addtosubtotal = models.CharField(db_column='AddToSubTotal', max_length=1)  # Field name made lowercase.
    fromdoctype = models.CharField(db_column='FromDocType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    fromdocno = models.CharField(db_column='FromDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fromdocdtlkey = models.BigIntegerField(db_column='FromDocDtlKey', blank=True, null=True)  # Field name made lowercase.
    fulltransferoption = models.CharField(db_column='FullTransferOption', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fulltransferfromdoclist = models.TextField(db_column='FullTransferFromDocList', blank=True, null=True)  # Field name made lowercase.
    serialnolist = models.TextField(db_column='SerialNoList', blank=True, null=True)  # Field name made lowercase.
    estimateddeliverydate = models.CharField(db_column='EstimatedDeliveryDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    packagedockey = models.BigIntegerField(db_column='PackageDocKey', blank=True, null=True)  # Field name made lowercase.
    parentdtlkey = models.BigIntegerField(db_column='ParentDtlKey', blank=True, null=True)  # Field name made lowercase.
    subqty = models.DecimalField(db_column='SubQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    subtotalextax = models.DecimalField(db_column='SubTotalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtax = models.DecimalField(db_column='LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.
    ruleno = models.BigIntegerField(db_column='RuleNo', blank=True, null=True)  # Field name made lowercase.
    deliverydate = models.DateTimeField(db_column='DeliveryDate', blank=True, null=True)  # Field name made lowercase.
    taxableamt = models.DecimalField(db_column='TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxadjustment = models.DecimalField(db_column='TaxAdjustment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localsubtotalextax = models.DecimalField(db_column='LocalSubTotalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    extradiscountamt = models.DecimalField(db_column='ExtraDiscountAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxrate = models.DecimalField(db_column='TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    localtaxadjustment = models.DecimalField(db_column='LocalTaxAdjustment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtaxableamt = models.DecimalField(db_column='LocalTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytax = models.DecimalField(db_column='TaxCurrencyTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxableamt = models.DecimalField(db_column='TaxCurrencyTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    salesexemptionno = models.CharField(db_column='SalesExemptionNo', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'DRDTL'


class Drprocessing(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    sodtlkey = models.BigIntegerField(db_column='SODtlKey')  # Field name made lowercase.
    sodockey = models.BigIntegerField(db_column='SODocKey')  # Field name made lowercase.
    itemcode = models.ForeignKey('Itemuom', models.DO_NOTHING, db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    furtherdescription = models.TextField(db_column='FurtherDescription', blank=True, null=True)  # Field name made lowercase.
    estimateddeliverydate = models.CharField(db_column='EstimatedDeliveryDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    location = models.ForeignKey('Location', models.DO_NOTHING, db_column='Location', blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey('Dept', models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    debtorcode = models.ForeignKey('Glmast', models.DO_NOTHING, db_column='DebtorCode', blank=True, null=True)  # Field name made lowercase.
    deliveryqty = models.DecimalField(db_column='DeliveryQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    deliveryuom = models.ForeignKey('Itemuom', models.DO_NOTHING, db_column='DeliveryUOM', blank=True, null=True)  # Field name made lowercase.
    deliveryrate = models.DecimalField(db_column='DeliveryRate', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    discount = models.CharField(db_column='Discount', max_length=12, blank=True, null=True)  # Field name made lowercase.
    taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='TaxType', blank=True, null=True)  # Field name made lowercase.
    createduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
    isallowopedit = models.CharField(db_column='IsAllowOPEdit', max_length=1, blank=True, null=True)  # Field name made lowercase.
    deliverydate = models.DateTimeField(db_column='DeliveryDate', blank=True, null=True)  # Field name made lowercase.
    taxrate = models.DecimalField(db_column='TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'DRProcessing'


class Drprocessingdo(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    drpkey = models.BigIntegerField(db_column='DRPKey')  # Field name made lowercase.
    sodtlkey = models.BigIntegerField(db_column='SODtlKey')  # Field name made lowercase.
    sodockey = models.BigIntegerField(db_column='SODocKey')  # Field name made lowercase.
    dodockey = models.BigIntegerField(db_column='DODocKey', blank=True, null=True)  # Field name made lowercase.
    dodocno = models.CharField(db_column='DODocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dodtlkey = models.BigIntegerField(db_column='DODtlKey', blank=True, null=True)  # Field name made lowercase.
    itemcode = models.ForeignKey('Itemuom', models.DO_NOTHING, db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    deliveryqty = models.DecimalField(db_column='DeliveryQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    deliveryuom = models.ForeignKey('Itemuom', models.DO_NOTHING, db_column='DeliveryUOM', blank=True, null=True)  # Field name made lowercase.
    deliveryrate = models.DecimalField(db_column='DeliveryRate', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    kiv = models.CharField(db_column='KIV', max_length=1)  # Field name made lowercase.
    createduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.

    class Meta:
 
        db_table = 'DRProcessingDO'


class Debtor(models.Model):
    accno = models.OneToOneField('Glmast', models.DO_NOTHING, db_column='AccNo', primary_key=True)  # Field name made lowercase.
    companyname = models.CharField(db_column='CompanyName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    desc2 = models.CharField(db_column='Desc2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    registerno = models.CharField(db_column='RegisterNo', max_length=25, blank=True, null=True)  # Field name made lowercase.
    address1 = models.CharField(db_column='Address1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    address2 = models.CharField(db_column='Address2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    address3 = models.CharField(db_column='Address3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    address4 = models.CharField(db_column='Address4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    postcode = models.CharField(db_column='PostCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    deliveraddr1 = models.CharField(db_column='DeliverAddr1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliveraddr2 = models.CharField(db_column='DeliverAddr2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliveraddr3 = models.CharField(db_column='DeliverAddr3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliveraddr4 = models.CharField(db_column='DeliverAddr4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliverpostcode = models.CharField(db_column='DeliverPostCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    attention = models.CharField(db_column='Attention', max_length=40, blank=True, null=True)  # Field name made lowercase.
    phone1 = models.CharField(db_column='Phone1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    phone2 = models.CharField(db_column='Phone2', max_length=25, blank=True, null=True)  # Field name made lowercase.
    fax1 = models.CharField(db_column='Fax1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    fax2 = models.CharField(db_column='Fax2', max_length=25, blank=True, null=True)  # Field name made lowercase.
    areacode = models.ForeignKey(Area, models.DO_NOTHING, db_column='AreaCode', blank=True, null=True)  # Field name made lowercase.
    salesagent = models.ForeignKey('Salesagent', models.DO_NOTHING, db_column='SalesAgent', blank=True, null=True)  # Field name made lowercase.
    debtortype = models.ForeignKey('Debtortype', models.DO_NOTHING, db_column='DebtorType', blank=True, null=True)  # Field name made lowercase.
    natureofbusiness = models.CharField(db_column='NatureOfBusiness', max_length=40, blank=True, null=True)  # Field name made lowercase.
    weburl = models.CharField(db_column='WebURL', max_length=80, blank=True, null=True)  # Field name made lowercase.
    emailaddress = models.CharField(db_column='EmailAddress', max_length=80, blank=True, null=True)  # Field name made lowercase.
    displayterm = models.ForeignKey('Terms', models.DO_NOTHING, db_column='DisplayTerm')  # Field name made lowercase.
    creditlimit = models.DecimalField(db_column='CreditLimit', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    agingon = models.CharField(db_column='AgingOn', max_length=1, blank=True, null=True)  # Field name made lowercase.
    statementtype = models.CharField(db_column='StatementType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    currencycode = models.ForeignKey(Currency, models.DO_NOTHING, db_column='CurrencyCode')  # Field name made lowercase.
    allowexceedcreditlimit = models.CharField(db_column='AllowExceedCreditLimit', max_length=1)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    exemptno = models.CharField(db_column='ExemptNo', max_length=60, blank=True, null=True)  # Field name made lowercase.
    expirydate = models.DateTimeField(db_column='ExpiryDate', blank=True, null=True)  # Field name made lowercase.
    pricecategory = models.ForeignKey('Pricecategory', models.DO_NOTHING, db_column='PriceCategory', blank=True, null=True)  # Field name made lowercase.
    taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='TaxType', blank=True, null=True)  # Field name made lowercase.
    discountpercent = models.DecimalField(db_column='DiscountPercent', max_digits=18, decimal_places=6)  # Field name made lowercase.
    detaildiscount = models.CharField(db_column='DetailDiscount', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    createduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    overduelimit = models.DecimalField(db_column='OverdueLimit', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    hasbonuspoint = models.CharField(db_column='HasBonusPoint', max_length=1)  # Field name made lowercase.
    openingbonuspoint = models.DecimalField(db_column='OpeningBonusPoint', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    qtblockstatus = models.SmallIntegerField(db_column='QTBlockStatus', blank=True, null=True)  # Field name made lowercase.
    soblockstatus = models.SmallIntegerField(db_column='SOBlockStatus', blank=True, null=True)  # Field name made lowercase.
    doblockstatus = models.SmallIntegerField(db_column='DOBlockStatus', blank=True, null=True)  # Field name made lowercase.
    ivblockstatus = models.SmallIntegerField(db_column='IVBlockStatus', blank=True, null=True)  # Field name made lowercase.
    csblockstatus = models.SmallIntegerField(db_column='CSBlockStatus', blank=True, null=True)  # Field name made lowercase.
    qtblockmessage = models.CharField(db_column='QTBlockMessage', max_length=40, blank=True, null=True)  # Field name made lowercase.
    soblockmessage = models.CharField(db_column='SOBlockMessage', max_length=40, blank=True, null=True)  # Field name made lowercase.
    doblockmessage = models.CharField(db_column='DOBlockMessage', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ivblockmessage = models.CharField(db_column='IVBlockMessage', max_length=40, blank=True, null=True)  # Field name made lowercase.
    csblockmessage = models.CharField(db_column='CSBlockMessage', max_length=40, blank=True, null=True)  # Field name made lowercase.
    externallink = models.TextField(db_column='ExternalLink', blank=True, null=True)  # Field name made lowercase.
    isgroupcompany = models.CharField(db_column='IsGroupCompany', max_length=1)  # Field name made lowercase.
    isactive = models.CharField(db_column='IsActive', max_length=1)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    contactinfo = models.TextField(db_column='ContactInfo', blank=True, null=True)  # Field name made lowercase.
    accountgroup = models.CharField(db_column='AccountGroup', max_length=12, blank=True, null=True)  # Field name made lowercase.
    markupratio = models.DecimalField(db_column='MarkupRatio', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    taxregisterno = models.CharField(db_column='TaxRegisterNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    calcdiscountonunitprice = models.CharField(db_column='CalcDiscountOnUnitPrice', max_length=1, blank=True, null=True)  # Field name made lowercase.
    gststatusverifieddate = models.DateTimeField(db_column='GSTStatusVerifiedDate', blank=True, null=True)  # Field name made lowercase.
    inclusivetax = models.CharField(db_column='InclusiveTax', max_length=1)  # Field name made lowercase.
    roundingmethod = models.IntegerField(db_column='RoundingMethod')  # Field name made lowercase.
    istaxregistered = models.CharField(db_column='IsTaxRegistered', max_length=1, blank=True, null=True)  # Field name made lowercase.
    receiptwithholdingtaxcode = models.CharField(db_column='ReceiptWithholdingTaxCode', max_length=14, blank=True, null=True)  # Field name made lowercase.
    paymentwithholdingtaxcode = models.CharField(db_column='PaymentWithholdingTaxCode', max_length=14, blank=True, null=True)  # Field name made lowercase.
    servicetaxregisterno = models.CharField(db_column='ServiceTaxRegisterNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    selfbilledapprovalno = models.CharField(db_column='SelfBilledApprovalNo', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'Debtor'


class Debtortype(models.Model):
    debtortype = models.CharField(db_column='DebtorType', primary_key=True, max_length=20)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=40, blank=True, null=True)  # Field name made lowercase.
    desc2 = models.CharField(db_column='Desc2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    isactive = models.CharField(db_column='IsActive', max_length=1)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.

    class Meta:
 
        db_table = 'DebtorType'


class Defaultreport(models.Model):
    reporttype = models.CharField(db_column='ReportType', primary_key=True, max_length=60)  # Field name made lowercase.
    reportname = models.CharField(db_column='ReportName', max_length=100)  # Field name made lowercase.

    class Meta:
 
        db_table = 'DefaultReport'


class Dept(models.Model):
    deptno = models.CharField(db_column='DeptNo', primary_key=True, max_length=10)  # Field name made lowercase.
    parentdeptno = models.ForeignKey('self', models.DO_NOTHING, db_column='ParentDeptNo', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=40, blank=True, null=True)  # Field name made lowercase.
    desc2 = models.CharField(db_column='Desc2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    isactive = models.CharField(db_column='IsActive', max_length=1)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.

    class Meta:
 
        db_table = 'Dept'


class Docnoformat(models.Model):
    name = models.CharField(db_column='Name', primary_key=True, max_length=20)  # Field name made lowercase.
    doctype = models.CharField(db_column='DocType', max_length=2)  # Field name made lowercase.
    nextnumber = models.IntegerField(db_column='NextNumber')  # Field name made lowercase.
    format = models.CharField(db_column='Format', max_length=30)  # Field name made lowercase.
    sample = models.CharField(db_column='Sample', max_length=20)  # Field name made lowercase.
    isdefault = models.CharField(db_column='IsDefault', max_length=1)  # Field name made lowercase.
    onemonthoneset = models.CharField(db_column='OneMonthOneSet', max_length=1)  # Field name made lowercase.
    maxnumber = models.IntegerField(db_column='MaxNumber', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'DocNoFormat'


class Docnoformataccno(models.Model):
    name = models.OneToOneField(Docnoformat, models.DO_NOTHING, db_column='Name', primary_key=True)  # Field name made lowercase.
    accno = models.ForeignKey('Glmast', models.DO_NOTHING, db_column='AccNo')  # Field name made lowercase.

    class Meta:
 
        db_table = 'DocNoFormatAccNo'
        unique_together = (('name', 'accno'),)


class Docnoformatusers(models.Model):
    name = models.OneToOneField(Docnoformat, models.DO_NOTHING, db_column='Name', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.

    class Meta:
 
        db_table = 'DocNoFormatUsers'
        unique_together = (('name', 'userid'),)


class Docnoformatyearlynumber(models.Model):
    name = models.CharField(db_column='Name', primary_key=True, max_length=20)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    m1nextnumber = models.IntegerField(db_column='M1NextNumber')  # Field name made lowercase.
    m2nextnumber = models.IntegerField(db_column='M2NextNumber')  # Field name made lowercase.
    m3nextnumber = models.IntegerField(db_column='M3NextNumber')  # Field name made lowercase.
    m4nextnumber = models.IntegerField(db_column='M4NextNumber')  # Field name made lowercase.
    m5nextnumber = models.IntegerField(db_column='M5NextNumber')  # Field name made lowercase.
    m6nextnumber = models.IntegerField(db_column='M6NextNumber')  # Field name made lowercase.
    m7nextnumber = models.IntegerField(db_column='M7NextNumber')  # Field name made lowercase.
    m8nextnumber = models.IntegerField(db_column='M8NextNumber')  # Field name made lowercase.
    m9nextnumber = models.IntegerField(db_column='M9NextNumber')  # Field name made lowercase.
    m10nextnumber = models.IntegerField(db_column='M10NextNumber')  # Field name made lowercase.
    m11nextnumber = models.IntegerField(db_column='M11NextNumber')  # Field name made lowercase.
    m12nextnumber = models.IntegerField(db_column='M12NextNumber')  # Field name made lowercase.

    class Meta:
 
        db_table = 'DocNoFormatYearlyNumber'
        unique_together = (('name', 'year'),)


class Docreportsetting(models.Model):
    doctype = models.CharField(db_column='DocType', primary_key=True, max_length=2)  # Field name made lowercase.
    data = models.BinaryField(db_column='Data', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'DocReportSetting'


class Eventlog(models.Model):
    eventkey = models.BigAutoField(db_column='EventKey', primary_key=True)  # Field name made lowercase.
    eventdatetime = models.DateTimeField(db_column='EventDateTime')  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    computername = models.CharField(db_column='ComputerName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    doctype = models.CharField(db_column='DocType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey', blank=True, null=True)  # Field name made lowercase.
    eventtype = models.SmallIntegerField(db_column='EventType')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50, blank=True, null=True)  # Field name made lowercase.
    eventmessage = models.TextField(db_column='EventMessage', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'EventLog'


class Expenses(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    accno = models.ForeignKey('Glmast', models.DO_NOTHING, db_column='AccNo')  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate')  # Field name made lowercase.
    frequency = models.CharField(db_column='Frequency', max_length=12)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=2)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'Expenses'


class Fcrevalue(models.Model):
    fcrevaluekey = models.BigIntegerField(db_column='FCRevalueKey', primary_key=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', max_length=20)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    unrealizedgainaccount = models.ForeignKey('Glmast', models.DO_NOTHING, db_column='UnrealizedGainAccount')  # Field name made lowercase.
    unrealizedlossaccount = models.ForeignKey('Glmast', models.DO_NOTHING, db_column='UnrealizedLossAccount')  # Field name made lowercase.
    gainlossjournaltype = models.ForeignKey('Journal', models.DO_NOTHING, db_column='GainLossJournalType')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    totalgainloss = models.DecimalField(db_column='TotalGainLoss', max_digits=19, decimal_places=2)  # Field name made lowercase.
    jekey = models.BigIntegerField(db_column='JEKey', blank=True, null=True)  # Field name made lowercase.
    printcount = models.SmallIntegerField(db_column='PrintCount', blank=True, null=True)  # Field name made lowercase.
    refcount = models.BigIntegerField(db_column='RefCount')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    createduserid = models.CharField(db_column='CreatedUserID', max_length=10)  # Field name made lowercase.
    usesinglegainlossaccount = models.CharField(db_column='UseSingleGainLossAccount', max_length=1)  # Field name made lowercase.
    gltrxid = models.BigIntegerField(db_column='GLTrxID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'FCRevalue'


class Fcrevaluedocument(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    fcrevaluekey = models.BigIntegerField(db_column='FCRevalueKey')  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=2)  # Field name made lowercase.
    doctype = models.CharField(db_column='DocType', max_length=2)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', max_length=20)  # Field name made lowercase.
    accno = models.ForeignKey('Glmast', models.DO_NOTHING, db_column='AccNo')  # Field name made lowercase.
    companyname = models.CharField(db_column='CompanyName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    currencycode = models.ForeignKey(Currency, models.DO_NOTHING, db_column='CurrencyCode')  # Field name made lowercase.
    revaluerate = models.DecimalField(db_column='RevalueRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    currencyrate = models.DecimalField(db_column='CurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    outstanding = models.DecimalField(db_column='Outstanding', max_digits=19, decimal_places=2)  # Field name made lowercase.
    gainloss = models.DecimalField(db_column='GainLoss', max_digits=19, decimal_places=2)  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey(Dept, models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'FCRevalueDocument'


class Fcrevalueglaccount(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    fcrevaluekey = models.BigIntegerField(db_column='FCRevalueKey')  # Field name made lowercase.
    accno = models.ForeignKey('Glmast', models.DO_NOTHING, db_column='AccNo')  # Field name made lowercase.
    revaluerate = models.DecimalField(db_column='RevalueRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    balance = models.DecimalField(db_column='Balance', max_digits=19, decimal_places=2)  # Field name made lowercase.
    newhomebalance = models.DecimalField(db_column='NewHomeBalance', max_digits=19, decimal_places=2)  # Field name made lowercase.
    homebalance = models.DecimalField(db_column='HomeBalance', max_digits=19, decimal_places=2)  # Field name made lowercase.
    gainloss = models.DecimalField(db_column='GainLoss', max_digits=19, decimal_places=2)  # Field name made lowercase.

    class Meta:
 
        db_table = 'FCRevalueGLAccount'


class Fcrevaluelock(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    fcrevaluekey = models.BigIntegerField(db_column='FCRevalueKey')  # Field name made lowercase.
    objtype = models.CharField(db_column='ObjType', max_length=2)  # Field name made lowercase.
    objkey = models.BigIntegerField(db_column='ObjKey')  # Field name made lowercase.
    prevrevalue = models.CharField(db_column='PrevRevalue', max_length=1, blank=True, null=True)  # Field name made lowercase.
    prevrevaluerate = models.DecimalField(db_column='PrevRevalueRate', max_digits=19, decimal_places=12, blank=True, null=True)  # Field name made lowercase.
    revaluerate = models.DecimalField(db_column='RevalueRate', max_digits=19, decimal_places=12, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'FCRevalueLock'


class Fcrevaluerate(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    fcrevaluekey = models.BigIntegerField(db_column='FCRevalueKey')  # Field name made lowercase.
    currencycode = models.ForeignKey(Currency, models.DO_NOTHING, db_column='CurrencyCode')  # Field name made lowercase.
    bankbuyrate = models.DecimalField(db_column='BankBuyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    unrealizedgainaccount = models.CharField(db_column='UnrealizedGainAccount', max_length=12, blank=True, null=True)  # Field name made lowercase.
    unrealizedlossaccount = models.CharField(db_column='UnrealizedLossAccount', max_length=12, blank=True, null=True)  # Field name made lowercase.
    banksellrate = models.DecimalField(db_column='BankSellRate', max_digits=19, decimal_places=12)  # Field name made lowercase.

    class Meta:
 
        db_table = 'FCRevalueRate'


class Fifocost(models.Model):
    fifocostkey = models.BigAutoField(db_column='FIFOCostKey', primary_key=True)  # Field name made lowercase.
    stockdtlkey = models.BigIntegerField(db_column='StockDTLKey')  # Field name made lowercase.
    seq = models.SmallIntegerField(db_column='Seq')  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=25, decimal_places=8)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=25, decimal_places=8)  # Field name made lowercase.

    class Meta:
 
        db_table = 'FIFOCost'


class Frcustomtext(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=20)  # Field name made lowercase.
    text1 = models.CharField(db_column='Text1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    text2 = models.CharField(db_column='Text2', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'FRCustomText'


class Fiscalyear(models.Model):
    fiscalyearname = models.CharField(db_column='FiscalYearName', primary_key=True, max_length=20)  # Field name made lowercase.
    fromdate = models.DateTimeField(db_column='FromDate')  # Field name made lowercase.
    todate = models.DateTimeField(db_column='ToDate')  # Field name made lowercase.
    isactive = models.CharField(db_column='IsActive', max_length=1)  # Field name made lowercase.

    class Meta:
 
        db_table = 'FiscalYear'


class Fontstyle(models.Model):
    fontstyle = models.CharField(db_column='FontStyle', primary_key=True, max_length=8)  # Field name made lowercase.
    fontname = models.CharField(db_column='FontName', max_length=40)  # Field name made lowercase.
    fontsize = models.DecimalField(db_column='FontSize', max_digits=6, decimal_places=2)  # Field name made lowercase.
    fontcolor = models.IntegerField(db_column='FontColor')  # Field name made lowercase.
    bold = models.CharField(db_column='Bold', max_length=1)  # Field name made lowercase.
    italic = models.CharField(db_column='Italic', max_length=1)  # Field name made lowercase.
    underline = models.CharField(db_column='Underline', max_length=1)  # Field name made lowercase.
    indent = models.SmallIntegerField(db_column='Indent', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'FontStyle'


class Footer(models.Model):
    footername = models.CharField(db_column='FooterName', primary_key=True, max_length=20)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=40, blank=True, null=True)  # Field name made lowercase.
    addtonettotal = models.CharField(db_column='AddToNetTotal', max_length=1)  # Field name made lowercase.
    addtoanalysisnettotal = models.CharField(db_column='AddToAnalysisNetTotal', max_length=1)  # Field name made lowercase.
    formula = models.TextField(db_column='Formula', blank=True, null=True)  # Field name made lowercase.
    posttogl = models.CharField(db_column='PostToGL', max_length=1)  # Field name made lowercase.
    accno = models.ForeignKey('Glmast', models.DO_NOTHING, db_column='AccNo', blank=True, null=True)  # Field name made lowercase.
    enable = models.CharField(db_column='Enable', max_length=1)  # Field name made lowercase.
    taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='TaxType', blank=True, null=True)  # Field name made lowercase.
    paramcaption = models.CharField(db_column='ParamCaption', max_length=40, blank=True, null=True)  # Field name made lowercase.
    paramvisible = models.CharField(db_column='ParamVisible', max_length=1)  # Field name made lowercase.
    paramdecimal = models.SmallIntegerField(db_column='ParamDecimal')  # Field name made lowercase.
    paramdefaultvalue = models.DecimalField(db_column='ParamDefaultValue', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    paramfrompercent = models.CharField(db_column='ParamFromPercent', max_length=1)  # Field name made lowercase.
    iscalcbonuspoint = models.CharField(db_column='IsCalcBonusPoint', max_length=1, blank=True, null=True)  # Field name made lowercase.
    addtocalculateextradiscountamount = models.CharField(db_column='AddToCalculateExtraDiscountAmount', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'Footer'


class Gldtl(models.Model):
    gldtlkey = models.BigAutoField(db_column='GLDtlKey', primary_key=True)  # Field name made lowercase.
    accno = models.ForeignKey('Glmast', models.DO_NOTHING, db_column='AccNo')  # Field name made lowercase.
    deaccno = models.ForeignKey('Glmast', models.DO_NOTHING, db_column='DEAccNo', blank=True, null=True)  # Field name made lowercase.
    journaltype = models.ForeignKey('Journal', models.DO_NOTHING, db_column='JournalType')  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey(Dept, models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    currencycode = models.ForeignKey(Currency, models.DO_NOTHING, db_column='CurrencyCode')  # Field name made lowercase.
    currencyrate = models.DecimalField(db_column='CurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    tohomerate = models.DecimalField(db_column='ToHomeRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    orgdr = models.DecimalField(db_column='OrgDR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    orgcr = models.DecimalField(db_column='OrgCR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    dr = models.DecimalField(db_column='DR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cr = models.DecimalField(db_column='CR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    homedr = models.DecimalField(db_column='HomeDR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    homecr = models.DecimalField(db_column='HomeCR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    transdate = models.DateTimeField(db_column='TransDate')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    refno1 = models.CharField(db_column='RefNo1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    refno2 = models.CharField(db_column='RefNo2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dekey = models.BigIntegerField(db_column='DEKey', blank=True, null=True)  # Field name made lowercase.
    userid = models.CharField(db_column='UserID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sourcetype = models.CharField(db_column='SourceType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    sourcekey = models.BigIntegerField(db_column='SourceKey', blank=True, null=True)  # Field name made lowercase.
    taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='TaxType', blank=True, null=True)  # Field name made lowercase.
    gltrxid = models.BigIntegerField(db_column='GLTrxID', blank=True, null=True)  # Field name made lowercase.
    sourcedtlkey = models.BigIntegerField(db_column='SourceDtlKey', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'GLDTL'


class Glmast(models.Model):
    accno = models.CharField(db_column='AccNo', primary_key=True, max_length=12)  # Field name made lowercase.
    parentaccno = models.CharField(db_column='ParentAccNo', max_length=12, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    desc2 = models.CharField(db_column='Desc2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    acctype = models.ForeignKey(Acctype, models.DO_NOTHING, db_column='AccType')  # Field name made lowercase.
    specialacctype = models.CharField(db_column='SpecialAccType', max_length=3, blank=True, null=True)  # Field name made lowercase.
    currencycode = models.ForeignKey(Currency, models.DO_NOTHING, db_column='CurrencyCode')  # Field name made lowercase.
    cashflowcategory = models.CharField(db_column='CashFlowCategory', max_length=1, blank=True, null=True)  # Field name made lowercase.
    msiccode = models.CharField(db_column='MSICCode', max_length=5, blank=True, null=True)  # Field name made lowercase.
    inputtaxtype = models.CharField(db_column='InputTaxType', max_length=14, blank=True, null=True)  # Field name made lowercase.
    outputtaxtype = models.CharField(db_column='OutputTaxType', max_length=14, blank=True, null=True)  # Field name made lowercase.
    tariffcode = models.ForeignKey('Tariff', models.DO_NOTHING, db_column='TariffCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'GLMast'


class Gltrxidtrash(models.Model):
    gltrxid = models.BigIntegerField(db_column='GLTrxID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    doctype = models.CharField(db_column='DocType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey', blank=True, null=True)  # Field name made lowercase.
    sourcedata = models.BinaryField(db_column='SourceData', blank=True, null=True)  # Field name made lowercase.
    compressed = models.CharField(db_column='Compressed', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'GLTrxIDTrash'


class Gr(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', unique=True, max_length=20)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    creditorcode = models.ForeignKey(Branch, models.DO_NOTHING, db_column='CreditorCode', blank=True, null=True)  # Field name made lowercase.
    creditorname = models.CharField(db_column='CreditorName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ref = models.CharField(db_column='Ref', max_length=40, blank=True, null=True)  # Field name made lowercase.
    supplierdono = models.CharField(db_column='SupplierDONo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=80, blank=True, null=True)  # Field name made lowercase.
    displayterm = models.ForeignKey('Terms', models.DO_NOTHING, db_column='DisplayTerm')  # Field name made lowercase.
    purchaseagent = models.ForeignKey('Purchaseagent', models.DO_NOTHING, db_column='PurchaseAgent', blank=True, null=True)  # Field name made lowercase.
    invaddr1 = models.CharField(db_column='InvAddr1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr2 = models.CharField(db_column='InvAddr2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr3 = models.CharField(db_column='InvAddr3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr4 = models.CharField(db_column='InvAddr4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    phone1 = models.CharField(db_column='Phone1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    fax1 = models.CharField(db_column='Fax1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    attention = models.CharField(db_column='Attention', max_length=40, blank=True, null=True)  # Field name made lowercase.
    branchcode = models.ForeignKey(Branch, models.DO_NOTHING, db_column='BranchCode', blank=True, null=True)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1param = models.DecimalField(db_column='Footer1Param', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1amt = models.DecimalField(db_column='Footer1Amt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1localamt = models.DecimalField(db_column='Footer1LocalAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='Footer1TaxType', blank=True, null=True)  # Field name made lowercase.
    footer2param = models.DecimalField(db_column='Footer2Param', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2amt = models.DecimalField(db_column='Footer2Amt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2localamt = models.DecimalField(db_column='Footer2LocalAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='Footer2TaxType', blank=True, null=True)  # Field name made lowercase.
    footer3param = models.DecimalField(db_column='Footer3Param', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3amt = models.DecimalField(db_column='Footer3Amt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3localamt = models.DecimalField(db_column='Footer3LocalAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='Footer3TaxType', blank=True, null=True)  # Field name made lowercase.
    currencycode = models.ForeignKey(Currency, models.DO_NOTHING, db_column='CurrencyCode')  # Field name made lowercase.
    currencyrate = models.DecimalField(db_column='CurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    nettotal = models.DecimalField(db_column='NetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localnettotal = models.DecimalField(db_column='LocalNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtax = models.DecimalField(db_column='LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    foreigncharges = models.DecimalField(db_column='ForeignCharges', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localcharges = models.DecimalField(db_column='LocalCharges', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    landedcostmethod = models.CharField(db_column='LandedCostMethod', max_length=1, blank=True, null=True)  # Field name made lowercase.
    posttostock = models.CharField(db_column='PostToStock', max_length=1)  # Field name made lowercase.
    transferable = models.CharField(db_column='Transferable', max_length=1)  # Field name made lowercase.
    todoctype = models.CharField(db_column='ToDocType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    todockey = models.BigIntegerField(db_column='ToDocKey', blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    remark1 = models.CharField(db_column='Remark1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark2 = models.CharField(db_column='Remark2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark3 = models.CharField(db_column='Remark3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark4 = models.CharField(db_column='Remark4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    printcount = models.SmallIntegerField(db_column='PrintCount')  # Field name made lowercase.
    cancelled = models.CharField(db_column='Cancelled', max_length=1)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    createduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    externallink = models.TextField(db_column='ExternalLink', blank=True, null=True)  # Field name made lowercase.
    refdocno = models.CharField(db_column='RefDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cansync = models.CharField(db_column='CanSync', max_length=1)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    todtlkey = models.BigIntegerField(db_column='ToDtlKey', blank=True, null=True)  # Field name made lowercase.
    fulltransferoption = models.CharField(db_column='FullTransferOption', max_length=1, blank=True, null=True)  # Field name made lowercase.
    shipvia = models.ForeignKey('Shippingmethod', models.DO_NOTHING, db_column='ShipVia', blank=True, null=True)  # Field name made lowercase.
    shipinfo = models.CharField(db_column='ShipInfo', max_length=40, blank=True, null=True)  # Field name made lowercase.
    purchaselocation = models.ForeignKey('Location', models.DO_NOTHING, db_column='PurchaseLocation', blank=True, null=True)  # Field name made lowercase.
    footer1tax = models.DecimalField(db_column='Footer1Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1localtax = models.DecimalField(db_column='Footer1LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2tax = models.DecimalField(db_column='Footer2Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2localtax = models.DecimalField(db_column='Footer2LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3tax = models.DecimalField(db_column='Footer3Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3localtax = models.DecimalField(db_column='Footer3LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    extax = models.DecimalField(db_column='ExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localextax = models.DecimalField(db_column='LocalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    analysisnettotal = models.DecimalField(db_column='AnalysisNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localanalysisnettotal = models.DecimalField(db_column='LocalAnalysisNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.
    totaxcurrencyrate = models.DecimalField(db_column='ToTaxCurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    calcdiscountonunitprice = models.CharField(db_column='CalcDiscountOnUnitPrice', max_length=1, blank=True, null=True)  # Field name made lowercase.
    totalextax = models.DecimalField(db_column='TotalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxableamt = models.DecimalField(db_column='TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    inclusivetax = models.CharField(db_column='InclusiveTax', max_length=1)  # Field name made lowercase.
    footer1taxrate = models.DecimalField(db_column='Footer1TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    footer2taxrate = models.DecimalField(db_column='Footer2TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    footer3taxrate = models.DecimalField(db_column='Footer3TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    roundingmethod = models.IntegerField(db_column='RoundingMethod')  # Field name made lowercase.
    localtaxableamt = models.DecimalField(db_column='LocalTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytax = models.DecimalField(db_column='TaxCurrencyTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxableamt = models.DecimalField(db_column='TaxCurrencyTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'GR'


class Grdtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    focdtlkey = models.BigIntegerField(db_column='FOCDtlKey', blank=True, null=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    indent = models.SmallIntegerField(db_column='Indent', blank=True, null=True)  # Field name made lowercase.
    fontstyle = models.ForeignKey(Fontstyle, models.DO_NOTHING, db_column='FontStyle', blank=True, null=True)  # Field name made lowercase.
    mainitem = models.CharField(db_column='MainItem', max_length=1)  # Field name made lowercase.
    numbering = models.CharField(db_column='Numbering', max_length=6, blank=True, null=True)  # Field name made lowercase.
    itemcode = models.ForeignKey('Itemuom', models.DO_NOTHING, db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    location = models.ForeignKey('Location', models.DO_NOTHING, db_column='Location', blank=True, null=True)  # Field name made lowercase.
    batchno = models.ForeignKey('Itembatch', models.DO_NOTHING, db_column='BatchNo', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    furtherdescription = models.TextField(db_column='FurtherDescription', blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey(Dept, models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    ourpono = models.CharField(db_column='OurPONo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ourpodate = models.DateTimeField(db_column='OurPODate', blank=True, null=True)  # Field name made lowercase.
    posttostockdate = models.DateTimeField(db_column='PostToStockDate', blank=True, null=True)  # Field name made lowercase.
    uom = models.ForeignKey('Itemuom', models.DO_NOTHING, db_column='UOM', blank=True, null=True)  # Field name made lowercase.
    useruom = models.CharField(db_column='UserUOM', max_length=8, blank=True, null=True)  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    smallestqty = models.DecimalField(db_column='SmallestQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    transferedqty = models.DecimalField(db_column='TransferedQty', max_digits=25, decimal_places=8)  # Field name made lowercase.
    focqty = models.DecimalField(db_column='FOCQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    foctransferedqty = models.DecimalField(db_column='FOCTransferedQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    smallestunitprice = models.DecimalField(db_column='SmallestUnitPrice', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    discount = models.CharField(db_column='Discount', max_length=20, blank=True, null=True)  # Field name made lowercase.
    discountamt = models.DecimalField(db_column='DiscountAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='TaxType', blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localsubtotal = models.DecimalField(db_column='LocalSubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    transferable = models.CharField(db_column='Transferable', max_length=1)  # Field name made lowercase.
    printout = models.CharField(db_column='PrintOut', max_length=1)  # Field name made lowercase.
    dtltype = models.CharField(db_column='DtlType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    calcbypercent = models.DecimalField(db_column='CalcByPercent', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    addtosubtotal = models.CharField(db_column='AddToSubTotal', max_length=1)  # Field name made lowercase.
    fromdoctype = models.CharField(db_column='FromDocType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    fromdocno = models.CharField(db_column='FromDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fromdocdtlkey = models.BigIntegerField(db_column='FromDocDtlKey', blank=True, null=True)  # Field name made lowercase.
    fulltransferoption = models.CharField(db_column='FullTransferOption', max_length=1, blank=True, null=True)  # Field name made lowercase.
    foreigncharges = models.DecimalField(db_column='ForeignCharges', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    localcharges = models.DecimalField(db_column='LocalCharges', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    duty = models.DecimalField(db_column='Duty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    fulltransferfromdoclist = models.TextField(db_column='FullTransferFromDocList', blank=True, null=True)  # Field name made lowercase.
    serialnolist = models.TextField(db_column='SerialNoList', blank=True, null=True)  # Field name made lowercase.
    estimateddeliverydate = models.CharField(db_column='EstimatedDeliveryDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    packagedockey = models.BigIntegerField(db_column='PackageDocKey', blank=True, null=True)  # Field name made lowercase.
    parentdtlkey = models.BigIntegerField(db_column='ParentDtlKey', blank=True, null=True)  # Field name made lowercase.
    subqty = models.DecimalField(db_column='SubQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    subtotalextax = models.DecimalField(db_column='SubTotalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtax = models.DecimalField(db_column='LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.
    deliverydate = models.DateTimeField(db_column='DeliveryDate', blank=True, null=True)  # Field name made lowercase.
    cnamt = models.DecimalField(db_column='CNAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxableamt = models.DecimalField(db_column='TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxadjustment = models.DecimalField(db_column='TaxAdjustment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localsubtotalextax = models.DecimalField(db_column='LocalSubTotalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    extradiscountamt = models.DecimalField(db_column='ExtraDiscountAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxrate = models.DecimalField(db_column='TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    localtaxadjustment = models.DecimalField(db_column='LocalTaxAdjustment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtaxableamt = models.DecimalField(db_column='LocalTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytax = models.DecimalField(db_column='TaxCurrencyTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxableamt = models.DecimalField(db_column='TaxCurrencyTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    salesexemptionno = models.CharField(db_column='SalesExemptionNo', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'GRDTL'


class Gstcapitalgoods(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    capitalcode = models.CharField(db_column='CapitalCode', unique=True, max_length=50)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=200, blank=True, null=True)  # Field name made lowercase.
    furtherdescription = models.TextField(db_column='FurtherDescription', blank=True, null=True)  # Field name made lowercase.
    commencedate = models.DateTimeField(db_column='CommenceDate')  # Field name made lowercase.
    disposaldate = models.DateTimeField(db_column='DisposalDate', blank=True, null=True)  # Field name made lowercase.
    islost = models.CharField(db_column='IsLost', max_length=1)  # Field name made lowercase.
    documentlink = models.TextField(db_column='DocumentLink', blank=True, null=True)  # Field name made lowercase.
    numofinterval = models.IntegerField(db_column='NumOfInterval')  # Field name made lowercase.
    totalamount = models.DecimalField(db_column='TotalAmount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    totaltax = models.DecimalField(db_column='TotalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'GSTCapitalGoods'


class Gstcapitalgoodsdtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    dockey = models.ForeignKey(Gstcapitalgoods, models.DO_NOTHING, db_column='DocKey')  # Field name made lowercase.
    parentdtlkey = models.BigIntegerField(db_column='ParentDtlKey', blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=200, blank=True, null=True)  # Field name made lowercase.
    furtherdescription = models.TextField(db_column='FurtherDescription', blank=True, null=True)  # Field name made lowercase.
    incurreddate = models.DateTimeField(db_column='IncurredDate')  # Field name made lowercase.
    disposaldate = models.DateTimeField(db_column='DisposalDate', blank=True, null=True)  # Field name made lowercase.
    islost = models.CharField(db_column='IsLost', max_length=1)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'GSTCapitalGoodsDTL'


class Gstcapitalgoodsschedule(models.Model):
    dockey = models.OneToOneField(Gstcapitalgoods, models.DO_NOTHING, db_column='DocKey', primary_key=True)  # Field name made lowercase.
    dtlkey = models.BigIntegerField(db_column='DtlKey')  # Field name made lowercase.
    gstseq = models.IntegerField(db_column='GSTSeq')  # Field name made lowercase.
    interval = models.IntegerField(db_column='Interval')  # Field name made lowercase.
    fromdate = models.DateTimeField(db_column='FromDate')  # Field name made lowercase.
    todate = models.DateTimeField(db_column='ToDate')  # Field name made lowercase.
    retax = models.DecimalField(db_column='RETax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    irrate = models.DecimalField(db_column='IRRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    retaxclaim = models.DecimalField(db_column='RETaxClaim', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    jeadjdockey = models.BigIntegerField(db_column='JEAdjDocKey', blank=True, null=True)  # Field name made lowercase.
    irratecalccontent = models.TextField(db_column='IRRateCalcContent', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'GSTCapitalGoodsSchedule'
        unique_together = (('dockey', 'dtlkey', 'gstseq', 'interval'),)


class Gstcapitalgoodsscheduleadj(models.Model):
    dockey = models.OneToOneField(Gstcapitalgoods, models.DO_NOTHING, db_column='DocKey', primary_key=True)  # Field name made lowercase.
    dtlkey = models.BigIntegerField(db_column='DtlKey')  # Field name made lowercase.
    gstseq = models.IntegerField(db_column='GSTSeq')  # Field name made lowercase.
    interval = models.IntegerField(db_column='Interval')  # Field name made lowercase.
    intervaladj = models.IntegerField(db_column='IntervalAdj')  # Field name made lowercase.
    cgarate = models.DecimalField(db_column='CGARate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    cgaamount = models.DecimalField(db_column='CGAAmount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cgaratecalccontent = models.TextField(db_column='CGARateCalcContent', blank=True, null=True)  # Field name made lowercase.
    cgaamountcalccontent = models.TextField(db_column='CGAAmountCalcContent', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'GSTCapitalGoodsScheduleAdj'
        unique_together = (('dockey', 'dtlkey', 'gstseq', 'interval', 'intervaladj'),)


class Gstpartialexemption(models.Model):
    fromdate = models.DateTimeField(db_column='FromDate', primary_key=True)  # Field name made lowercase.
    todate = models.DateTimeField(db_column='ToDate')  # Field name made lowercase.
    gstseq = models.IntegerField(db_column='GSTSeq')  # Field name made lowercase.
    isremainperiod = models.CharField(db_column='IsRemainPeriod', max_length=1)  # Field name made lowercase.
    ttaxableamt = models.DecimalField(db_column='TTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    etaxableamt = models.DecimalField(db_column='ETaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    o1taxableamt = models.DecimalField(db_column='O1TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    o2taxableamt = models.DecimalField(db_column='O2TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    r1_o1taxableamt = models.DecimalField(db_column='R1_O1TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    r1_o2taxableamt = models.DecimalField(db_column='R1_O2TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    r2taxableamt = models.DecimalField(db_column='R2TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    r3taxableamt = models.DecimalField(db_column='R3TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    r4taxableamt = models.DecimalField(db_column='R4TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    r5taxableamt = models.DecimalField(db_column='R5TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    estax = models.DecimalField(db_column='ESTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    retax = models.DecimalField(db_column='RETax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    isdeminimis = models.CharField(db_column='IsDeMinimis', max_length=1, blank=True, null=True)  # Field name made lowercase.
    irrate = models.DecimalField(db_column='IRRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    estaxclaim = models.DecimalField(db_column='ESTaxClaim', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    retaxclaim = models.DecimalField(db_column='RETaxClaim', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    estaxclaimperiodadj = models.DecimalField(db_column='ESTaxClaimPeriodAdj', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    retaxclaimperiodadj = models.DecimalField(db_column='RETaxClaimPeriodAdj', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    jeperioddockey = models.BigIntegerField(db_column='JEPeriodDocKey', blank=True, null=True)  # Field name made lowercase.
    jeperiodadjdockey = models.BigIntegerField(db_column='JEPeriodAdjDocKey', blank=True, null=True)  # Field name made lowercase.
    jeannualadjdockey = models.BigIntegerField(db_column='JEAnnualAdjDocKey', blank=True, null=True)  # Field name made lowercase.
    isdeminimiscalccontent = models.TextField(db_column='IsDeMinimisCalcContent', blank=True, null=True)  # Field name made lowercase.
    irratecalccontent = models.TextField(db_column='IRRateCalcContent', blank=True, null=True)  # Field name made lowercase.
    processjeperiodadj = models.CharField(db_column='ProcessJEPeriodAdj', max_length=1, blank=True, null=True)  # Field name made lowercase.
    jeannualadjdockey2 = models.BigIntegerField(db_column='JEAnnualAdjDocKey2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'GSTPartialExemption'
        unique_together = (('fromdate', 'todate', 'gstseq'),)


class Gstprocessor(models.Model):
    gstkey = models.BigAutoField(db_column='GSTKey', primary_key=True)  # Field name made lowercase.
    fromdate = models.DateTimeField(db_column='FromDate')  # Field name made lowercase.
    todate = models.DateTimeField(db_column='ToDate')  # Field name made lowercase.
    duration = models.SmallIntegerField(db_column='Duration')  # Field name made lowercase.
    submitted = models.CharField(db_column='Submitted', max_length=1)  # Field name made lowercase.
    taxdatareport = models.BinaryField(db_column='TaxDataReport', blank=True, null=True)  # Field name made lowercase.
    jedockey = models.BigIntegerField(db_column='JEDocKey', blank=True, null=True)  # Field name made lowercase.
    carryforwardrefundgst = models.CharField(db_column='CarryForwardRefundGST', max_length=1, blank=True, null=True)  # Field name made lowercase.
    authorizername = models.CharField(db_column='AuthorizerName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    newicno = models.CharField(db_column='NewICNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    oldicno = models.CharField(db_column='OldICNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    passportno = models.CharField(db_column='PassportNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nationality = models.CharField(db_column='Nationality', max_length=40, blank=True, null=True)  # Field name made lowercase.
    compressed = models.CharField(db_column='Compressed', max_length=1)  # Field name made lowercase.
    parentgstkey = models.BigIntegerField(db_column='ParentGSTKey', blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq', blank=True, null=True)  # Field name made lowercase.
    ispartialexemption = models.CharField(db_column='IsPartialExemption', max_length=1, blank=True, null=True)  # Field name made lowercase.
    iscapitalgoodsadj = models.CharField(db_column='IsCapitalGoodsAdj', max_length=1, blank=True, null=True)  # Field name made lowercase.
    productversion = models.CharField(db_column='ProductVersion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    gafversion = models.CharField(db_column='GAFVersion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    gstversion = models.IntegerField(db_column='GSTVersion')  # Field name made lowercase.
    isfinalgstreturn = models.CharField(db_column='IsFinalGSTReturn', max_length=1, blank=True, null=True)  # Field name made lowercase.
    jefixedassetandstockvaluedockey = models.BigIntegerField(db_column='JEFixedAssetAndStockValueDocKey', blank=True, null=True)  # Field name made lowercase.
    cimbstatuscode = models.CharField(db_column='CIMBStatusCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cimbstatusdesc = models.CharField(db_column='CIMBStatusDesc', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cimbrefno = models.CharField(db_column='CIMBRefNo', max_length=32, blank=True, null=True)  # Field name made lowercase.
    cimbmediano = models.CharField(db_column='CIMBMediaNo', max_length=15, blank=True, null=True)  # Field name made lowercase.
    cbkey = models.BigIntegerField(db_column='CBKey', blank=True, null=True)  # Field name made lowercase.
    jegainlossdockey = models.BigIntegerField(db_column='JEGainLossDocKey', blank=True, null=True)  # Field name made lowercase.
    declarationdate = models.DateTimeField(db_column='DeclarationDate', blank=True, null=True)  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp', blank=True, null=True)  # Field name made lowercase.
    createduserid = models.CharField(db_column='CreatedUserID', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'GSTProcessor'


class Gstsetting(models.Model):
    gstname = models.CharField(db_column='GSTName', primary_key=True, max_length=100)  # Field name made lowercase.
    gstvalue = models.CharField(db_column='GSTValue', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'GSTSetting'


class Gt(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', unique=True, max_length=20)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    creditorcode = models.ForeignKey(Branch, models.DO_NOTHING, db_column='CreditorCode', blank=True, null=True)  # Field name made lowercase.
    creditorname = models.CharField(db_column='CreditorName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ref = models.CharField(db_column='Ref', max_length=40, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=80, blank=True, null=True)  # Field name made lowercase.
    displayterm = models.ForeignKey('Terms', models.DO_NOTHING, db_column='DisplayTerm')  # Field name made lowercase.
    purchaseagent = models.ForeignKey('Purchaseagent', models.DO_NOTHING, db_column='PurchaseAgent', blank=True, null=True)  # Field name made lowercase.
    invaddr1 = models.CharField(db_column='InvAddr1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr2 = models.CharField(db_column='InvAddr2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr3 = models.CharField(db_column='InvAddr3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr4 = models.CharField(db_column='InvAddr4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    phone1 = models.CharField(db_column='Phone1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    fax1 = models.CharField(db_column='Fax1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    attention = models.CharField(db_column='Attention', max_length=40, blank=True, null=True)  # Field name made lowercase.
    branchcode = models.ForeignKey(Branch, models.DO_NOTHING, db_column='BranchCode', blank=True, null=True)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1param = models.DecimalField(db_column='Footer1Param', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1amt = models.DecimalField(db_column='Footer1Amt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1localamt = models.DecimalField(db_column='Footer1LocalAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='Footer1TaxType', blank=True, null=True)  # Field name made lowercase.
    footer2param = models.DecimalField(db_column='Footer2Param', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2amt = models.DecimalField(db_column='Footer2Amt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2localamt = models.DecimalField(db_column='Footer2LocalAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='Footer2TaxType', blank=True, null=True)  # Field name made lowercase.
    footer3param = models.DecimalField(db_column='Footer3Param', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3amt = models.DecimalField(db_column='Footer3Amt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3localamt = models.DecimalField(db_column='Footer3LocalAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='Footer3TaxType', blank=True, null=True)  # Field name made lowercase.
    currencycode = models.ForeignKey(Currency, models.DO_NOTHING, db_column='CurrencyCode')  # Field name made lowercase.
    currencyrate = models.DecimalField(db_column='CurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    nettotal = models.DecimalField(db_column='NetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localnettotal = models.DecimalField(db_column='LocalNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtax = models.DecimalField(db_column='LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    posttostock = models.CharField(db_column='PostToStock', max_length=1)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    remark1 = models.CharField(db_column='Remark1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark2 = models.CharField(db_column='Remark2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark3 = models.CharField(db_column='Remark3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark4 = models.CharField(db_column='Remark4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    printcount = models.SmallIntegerField(db_column='PrintCount')  # Field name made lowercase.
    cancelled = models.CharField(db_column='Cancelled', max_length=1)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    createduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    externallink = models.TextField(db_column='ExternalLink', blank=True, null=True)  # Field name made lowercase.
    refdocno = models.CharField(db_column='RefDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cansync = models.CharField(db_column='CanSync', max_length=1)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    purchaselocation = models.ForeignKey('Location', models.DO_NOTHING, db_column='PurchaseLocation', blank=True, null=True)  # Field name made lowercase.
    footer1tax = models.DecimalField(db_column='Footer1Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1localtax = models.DecimalField(db_column='Footer1LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2tax = models.DecimalField(db_column='Footer2Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2localtax = models.DecimalField(db_column='Footer2LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3tax = models.DecimalField(db_column='Footer3Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3localtax = models.DecimalField(db_column='Footer3LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    extax = models.DecimalField(db_column='ExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localextax = models.DecimalField(db_column='LocalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    analysisnettotal = models.DecimalField(db_column='AnalysisNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localanalysisnettotal = models.DecimalField(db_column='LocalAnalysisNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.
    totaxcurrencyrate = models.DecimalField(db_column='ToTaxCurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    calcdiscountonunitprice = models.CharField(db_column='CalcDiscountOnUnitPrice', max_length=1, blank=True, null=True)  # Field name made lowercase.
    totalextax = models.DecimalField(db_column='TotalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxableamt = models.DecimalField(db_column='TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    inclusivetax = models.CharField(db_column='InclusiveTax', max_length=1)  # Field name made lowercase.
    footer1taxrate = models.DecimalField(db_column='Footer1TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    footer2taxrate = models.DecimalField(db_column='Footer2TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    footer3taxrate = models.DecimalField(db_column='Footer3TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    roundingmethod = models.IntegerField(db_column='RoundingMethod')  # Field name made lowercase.
    localtaxableamt = models.DecimalField(db_column='LocalTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytax = models.DecimalField(db_column='TaxCurrencyTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxableamt = models.DecimalField(db_column='TaxCurrencyTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'GT'


class Gtdtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    focdtlkey = models.BigIntegerField(db_column='FOCDtlKey', blank=True, null=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    indent = models.SmallIntegerField(db_column='Indent', blank=True, null=True)  # Field name made lowercase.
    fontstyle = models.ForeignKey(Fontstyle, models.DO_NOTHING, db_column='FontStyle', blank=True, null=True)  # Field name made lowercase.
    mainitem = models.CharField(db_column='MainItem', max_length=1)  # Field name made lowercase.
    numbering = models.CharField(db_column='Numbering', max_length=6, blank=True, null=True)  # Field name made lowercase.
    itemcode = models.ForeignKey('Itemuom', models.DO_NOTHING, db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    location = models.ForeignKey('Location', models.DO_NOTHING, db_column='Location', blank=True, null=True)  # Field name made lowercase.
    batchno = models.ForeignKey('Itembatch', models.DO_NOTHING, db_column='BatchNo', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    furtherdescription = models.TextField(db_column='FurtherDescription', blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey(Dept, models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    ourpono = models.CharField(db_column='OurPONo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ourpodate = models.DateTimeField(db_column='OurPODate', blank=True, null=True)  # Field name made lowercase.
    posttostockdate = models.DateTimeField(db_column='PostToStockDate', blank=True, null=True)  # Field name made lowercase.
    uom = models.ForeignKey('Itemuom', models.DO_NOTHING, db_column='UOM', blank=True, null=True)  # Field name made lowercase.
    useruom = models.CharField(db_column='UserUOM', max_length=8, blank=True, null=True)  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    smallestqty = models.DecimalField(db_column='SmallestQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    focqty = models.DecimalField(db_column='FOCQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    smallestunitprice = models.DecimalField(db_column='SmallestUnitPrice', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    discount = models.CharField(db_column='Discount', max_length=20, blank=True, null=True)  # Field name made lowercase.
    discountamt = models.DecimalField(db_column='DiscountAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='TaxType', blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localsubtotal = models.DecimalField(db_column='LocalSubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    printout = models.CharField(db_column='PrintOut', max_length=1)  # Field name made lowercase.
    dtltype = models.CharField(db_column='DtlType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    calcbypercent = models.DecimalField(db_column='CalcByPercent', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    addtosubtotal = models.CharField(db_column='AddToSubTotal', max_length=1)  # Field name made lowercase.
    fromdoctype = models.CharField(db_column='FromDocType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    fromdocno = models.CharField(db_column='FromDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fromdocdtlkey = models.BigIntegerField(db_column='FromDocDtlKey', blank=True, null=True)  # Field name made lowercase.
    fulltransferoption = models.CharField(db_column='FullTransferOption', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fulltransferfromdoclist = models.TextField(db_column='FullTransferFromDocList', blank=True, null=True)  # Field name made lowercase.
    serialnolist = models.TextField(db_column='SerialNoList', blank=True, null=True)  # Field name made lowercase.
    estimateddeliverydate = models.CharField(db_column='EstimatedDeliveryDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    packagedockey = models.BigIntegerField(db_column='PackageDocKey', blank=True, null=True)  # Field name made lowercase.
    parentdtlkey = models.BigIntegerField(db_column='ParentDtlKey', blank=True, null=True)  # Field name made lowercase.
    subqty = models.DecimalField(db_column='SubQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    subtotalextax = models.DecimalField(db_column='SubTotalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtax = models.DecimalField(db_column='LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.
    deliverydate = models.DateTimeField(db_column='DeliveryDate', blank=True, null=True)  # Field name made lowercase.
    taxableamt = models.DecimalField(db_column='TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxadjustment = models.DecimalField(db_column='TaxAdjustment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localsubtotalextax = models.DecimalField(db_column='LocalSubTotalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    extradiscountamt = models.DecimalField(db_column='ExtraDiscountAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxrate = models.DecimalField(db_column='TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    localtaxadjustment = models.DecimalField(db_column='LocalTaxAdjustment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtaxableamt = models.DecimalField(db_column='LocalTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytax = models.DecimalField(db_column='TaxCurrencyTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxableamt = models.DecimalField(db_column='TaxCurrencyTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    salesexemptionno = models.CharField(db_column='SalesExemptionNo', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'GTDTL'


class Giftrule(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', unique=True, max_length=20)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    icno = models.CharField(db_column='ICNo', max_length=25, blank=True, null=True)  # Field name made lowercase.
    address1 = models.CharField(db_column='Address1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    address2 = models.CharField(db_column='Address2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    address3 = models.CharField(db_column='Address3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    address4 = models.CharField(db_column='Address4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=25, blank=True, null=True)  # Field name made lowercase.
    emailaddress = models.CharField(db_column='EmailAddress', max_length=80, blank=True, null=True)  # Field name made lowercase.
    giftdescription = models.CharField(db_column='GiftDescription', max_length=100, blank=True, null=True)  # Field name made lowercase.
    gifttotalamount = models.DecimalField(db_column='GiftTotalAmount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    createduserid = models.CharField(db_column='CreatedUserID', max_length=10)  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.CharField(db_column='LastModifiedUserID', max_length=10)  # Field name made lowercase.
    jedockey = models.BigIntegerField(db_column='JEDocKey', blank=True, null=True)  # Field name made lowercase.
    taxcurrencygifttotalamount = models.DecimalField(db_column='TaxCurrencyGiftTotalAmount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    currencycode = models.CharField(db_column='CurrencyCode', max_length=5)  # Field name made lowercase.
    totaxcurrencyrate = models.DecimalField(db_column='ToTaxCurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    currencyrate = models.DecimalField(db_column='CurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.

    class Meta:
 
        db_table = 'GiftRule'


class Globalpricechange(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200, blank=True, null=True)  # Field name made lowercase.
    changedatetime = models.DateTimeField(db_column='ChangeDateTime', blank=True, null=True)  # Field name made lowercase.
    criteria = models.TextField(db_column='Criteria', blank=True, null=True)  # Field name made lowercase.
    data = models.TextField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    updated = models.CharField(db_column='Updated', max_length=1, blank=True, null=True)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.CharField(db_column='LastModifiedUserID', max_length=10)  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    createduserid = models.CharField(db_column='CreatedUserID', max_length=10)  # Field name made lowercase.

    class Meta:
 
        db_table = 'GlobalPriceChange'


class Gridlistingfilter(models.Model):
    filtername = models.CharField(db_column='FilterName', primary_key=True, max_length=40)  # Field name made lowercase.
    template = models.TextField(db_column='Template', blank=True, null=True)  # Field name made lowercase.
    isdefault = models.CharField(db_column='IsDefault', max_length=1)  # Field name made lowercase.

    class Meta:
 
        db_table = 'GridListingFilter'


class Gridlistingfilterusers(models.Model):
    filtername = models.CharField(db_column='FilterName', primary_key=True, max_length=40)  # Field name made lowercase.
    userid = models.CharField(db_column='UserID', max_length=10)  # Field name made lowercase.

    class Meta:
 
        db_table = 'GridListingFilterUsers'
        unique_together = (('filtername', 'userid'),)


class Iphist(models.Model):
    ipkey = models.BigAutoField(db_column='IPKey', primary_key=True)  # Field name made lowercase.
    dtlkey = models.BigIntegerField(db_column='DtlKey', blank=True, null=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey', blank=True, null=True)  # Field name made lowercase.
    doctype = models.CharField(db_column='DocType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    accno = models.ForeignKey(Branch, models.DO_NOTHING, db_column='AccNo', blank=True, null=True)  # Field name made lowercase.
    branchcode = models.ForeignKey(Branch, models.DO_NOTHING, db_column='BranchCode', blank=True, null=True)  # Field name made lowercase.
    itemcode = models.ForeignKey('Itemuom', models.DO_NOTHING, db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', max_length=20)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    location = models.ForeignKey('Location', models.DO_NOTHING, db_column='Location', blank=True, null=True)  # Field name made lowercase.
    agent = models.CharField(db_column='Agent', max_length=12, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    furtherdescription = models.TextField(db_column='FurtherDescription', blank=True, null=True)  # Field name made lowercase.
    batchno = models.ForeignKey('Itembatch', models.DO_NOTHING, db_column='BatchNo', blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey(Dept, models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    uom = models.ForeignKey('Itemuom', models.DO_NOTHING, db_column='UOM', blank=True, null=True)  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    smallestqty = models.DecimalField(db_column='SmallestQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    focqty = models.DecimalField(db_column='FOCQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    discount = models.CharField(db_column='Discount', max_length=20, blank=True, null=True)  # Field name made lowercase.
    taxtype = models.CharField(db_column='TaxType', max_length=14, blank=True, null=True)  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    currencyrate = models.DecimalField(db_column='CurrencyRate', max_digits=19, decimal_places=12, blank=True, null=True)  # Field name made lowercase.
    cancelled = models.CharField(db_column='Cancelled', max_length=1)  # Field name made lowercase.
    transfered = models.CharField(db_column='Transfered', max_length=1, blank=True, null=True)  # Field name made lowercase.
    packagedockey = models.BigIntegerField(db_column='PackageDocKey', blank=True, null=True)  # Field name made lowercase.
    parentdtlkey = models.BigIntegerField(db_column='ParentDtlKey', blank=True, null=True)  # Field name made lowercase.
    memberno = models.CharField(db_column='MemberNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.
    taxrate = models.DecimalField(db_column='TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'IPHIST'


class Iss(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', unique=True, max_length=20)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    remark1 = models.CharField(db_column='Remark1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark2 = models.CharField(db_column='Remark2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark3 = models.CharField(db_column='Remark3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark4 = models.CharField(db_column='Remark4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    printcount = models.SmallIntegerField(db_column='PrintCount')  # Field name made lowercase.
    cancelled = models.CharField(db_column='Cancelled', max_length=1)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    createduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    externallink = models.TextField(db_column='ExternalLink', blank=True, null=True)  # Field name made lowercase.
    refdocno = models.CharField(db_column='RefDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    cansync = models.CharField(db_column='CanSync', max_length=1)  # Field name made lowercase.
    reallocatepurchasebyproject = models.CharField(db_column='ReallocatePurchaseByProject', max_length=1)  # Field name made lowercase.
    reallocatepurchasebyprojectjedockey = models.BigIntegerField(db_column='ReallocatePurchaseByProjectJEDocKey', blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.
    reallocatepurchasebyprojectno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ReallocatePurchaseByProjectNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'ISS'


class Issdtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    numbering = models.CharField(db_column='Numbering', max_length=6, blank=True, null=True)  # Field name made lowercase.
    itemcode = models.ForeignKey('Itemuom', models.DO_NOTHING, db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    location = models.ForeignKey('Location', models.DO_NOTHING, db_column='Location', blank=True, null=True)  # Field name made lowercase.
    batchno = models.ForeignKey('Itembatch', models.DO_NOTHING, db_column='BatchNo', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    furtherdescription = models.TextField(db_column='FurtherDescription', blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey(Dept, models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    uom = models.ForeignKey('Itemuom', models.DO_NOTHING, db_column='UOM', blank=True, null=True)  # Field name made lowercase.
    unitcost = models.DecimalField(db_column='UnitCost', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    printout = models.CharField(db_column='PrintOut', max_length=1)  # Field name made lowercase.
    serialnolist = models.TextField(db_column='SerialNoList', blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.

    class Meta:
 
        db_table = 'ISSDTL'


class Iv(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', unique=True, max_length=20)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    debtorcode = models.ForeignKey(Branch, models.DO_NOTHING, db_column='DebtorCode')  # Field name made lowercase.
    debtorname = models.CharField(db_column='DebtorName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ref = models.CharField(db_column='Ref', max_length=40, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=80, blank=True, null=True)  # Field name made lowercase.
    displayterm = models.ForeignKey('Terms', models.DO_NOTHING, db_column='DisplayTerm')  # Field name made lowercase.
    salesagent = models.ForeignKey('Salesagent', models.DO_NOTHING, db_column='SalesAgent', blank=True, null=True)  # Field name made lowercase.
    invaddr1 = models.CharField(db_column='InvAddr1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr2 = models.CharField(db_column='InvAddr2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr3 = models.CharField(db_column='InvAddr3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr4 = models.CharField(db_column='InvAddr4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    phone1 = models.CharField(db_column='Phone1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    fax1 = models.CharField(db_column='Fax1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    attention = models.CharField(db_column='Attention', max_length=40, blank=True, null=True)  # Field name made lowercase.
    branchcode = models.ForeignKey(Branch, models.DO_NOTHING, db_column='BranchCode', blank=True, null=True)  # Field name made lowercase.
    deliveraddr1 = models.CharField(db_column='DeliverAddr1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliveraddr2 = models.CharField(db_column='DeliverAddr2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliveraddr3 = models.CharField(db_column='DeliverAddr3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliveraddr4 = models.CharField(db_column='DeliverAddr4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliverphone1 = models.CharField(db_column='DeliverPhone1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    deliverfax1 = models.CharField(db_column='DeliverFax1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    delivercontact = models.CharField(db_column='DeliverContact', max_length=40, blank=True, null=True)  # Field name made lowercase.
    salesexemptionno = models.CharField(db_column='SalesExemptionNo', max_length=60, blank=True, null=True)  # Field name made lowercase.
    salesexemptionexpirydate = models.DateTimeField(db_column='SalesExemptionExpiryDate', blank=True, null=True)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1param = models.DecimalField(db_column='Footer1Param', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1amt = models.DecimalField(db_column='Footer1Amt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1localamt = models.DecimalField(db_column='Footer1LocalAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='Footer1TaxType', blank=True, null=True)  # Field name made lowercase.
    footer2param = models.DecimalField(db_column='Footer2Param', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2amt = models.DecimalField(db_column='Footer2Amt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2localamt = models.DecimalField(db_column='Footer2LocalAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='Footer2TaxType', blank=True, null=True)  # Field name made lowercase.
    footer3param = models.DecimalField(db_column='Footer3Param', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3amt = models.DecimalField(db_column='Footer3Amt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3localamt = models.DecimalField(db_column='Footer3LocalAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='Footer3TaxType', blank=True, null=True)  # Field name made lowercase.
    currencycode = models.ForeignKey(Currency, models.DO_NOTHING, db_column='CurrencyCode')  # Field name made lowercase.
    currencyrate = models.DecimalField(db_column='CurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    nettotal = models.DecimalField(db_column='NetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localnettotal = models.DecimalField(db_column='LocalNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    analysisnettotal = models.DecimalField(db_column='AnalysisNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localanalysisnettotal = models.DecimalField(db_column='LocalAnalysisNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtotalcost = models.DecimalField(db_column='LocalTotalCost', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtax = models.DecimalField(db_column='LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    totalbonuspoint = models.DecimalField(db_column='TotalBonusPoint', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    posttostock = models.CharField(db_column='PostToStock', max_length=1)  # Field name made lowercase.
    posttogl = models.CharField(db_column='PostToGL', max_length=1)  # Field name made lowercase.
    referdockey = models.BigIntegerField(db_column='ReferDocKey', blank=True, null=True)  # Field name made lowercase.
    referpaymentdockey = models.BigIntegerField(db_column='ReferPaymentDocKey', blank=True, null=True)  # Field name made lowercase.
    transferable = models.CharField(db_column='Transferable', max_length=1)  # Field name made lowercase.
    todoctype = models.CharField(db_column='ToDocType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    todockey = models.BigIntegerField(db_column='ToDocKey', blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    remark1 = models.CharField(db_column='Remark1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark2 = models.CharField(db_column='Remark2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark3 = models.CharField(db_column='Remark3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark4 = models.CharField(db_column='Remark4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    printcount = models.SmallIntegerField(db_column='PrintCount')  # Field name made lowercase.
    cancelled = models.CharField(db_column='Cancelled', max_length=1)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    createduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    externallink = models.TextField(db_column='ExternalLink', blank=True, null=True)  # Field name made lowercase.
    refdocno = models.CharField(db_column='RefDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    csgndockey = models.BigIntegerField(db_column='CSGNDocKey', blank=True, null=True)  # Field name made lowercase.
    cansync = models.CharField(db_column='CanSync', max_length=1)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    memberno = models.ForeignKey('Member', models.DO_NOTHING, db_column='MemberNo', blank=True, null=True)  # Field name made lowercase.
    todtlkey = models.BigIntegerField(db_column='ToDtlKey', blank=True, null=True)  # Field name made lowercase.
    fulltransferoption = models.CharField(db_column='FullTransferOption', max_length=1, blank=True, null=True)  # Field name made lowercase.
    shipvia = models.ForeignKey('Shippingmethod', models.DO_NOTHING, db_column='ShipVia', blank=True, null=True)  # Field name made lowercase.
    shipinfo = models.CharField(db_column='ShipInfo', max_length=40, blank=True, null=True)  # Field name made lowercase.
    reallocatepurchasebyproject = models.CharField(db_column='ReallocatePurchaseByProject', max_length=1)  # Field name made lowercase.
    reallocatepurchasebyprojectjedockey = models.BigIntegerField(db_column='ReallocatePurchaseByProjectJEDocKey', blank=True, null=True)  # Field name made lowercase.
    refno2 = models.CharField(db_column='RefNo2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    saleslocation = models.ForeignKey('Location', models.DO_NOTHING, db_column='SalesLocation', blank=True, null=True)  # Field name made lowercase.
    footer1tax = models.DecimalField(db_column='Footer1Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1localtax = models.DecimalField(db_column='Footer1LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2tax = models.DecimalField(db_column='Footer2Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2localtax = models.DecimalField(db_column='Footer2LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3tax = models.DecimalField(db_column='Footer3Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3localtax = models.DecimalField(db_column='Footer3LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    extax = models.DecimalField(db_column='ExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localextax = models.DecimalField(db_column='LocalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    yourpono = models.CharField(db_column='YourPONo', max_length=25, blank=True, null=True)  # Field name made lowercase.
    yourpodate = models.DateTimeField(db_column='YourPODate', blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.
    reallocatepurchasebyprojectno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ReallocatePurchaseByProjectNo', blank=True, null=True)  # Field name made lowercase.
    totaxcurrencyrate = models.DecimalField(db_column='ToTaxCurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    roundadj = models.DecimalField(db_column='RoundAdj', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    finaltotal = models.DecimalField(db_column='FinalTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    calcdiscountonunitprice = models.CharField(db_column='CalcDiscountOnUnitPrice', max_length=1, blank=True, null=True)  # Field name made lowercase.
    taxdocno = models.CharField(db_column='TaxDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    totalextax = models.DecimalField(db_column='TotalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxableamt = models.DecimalField(db_column='TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    inclusivetax = models.CharField(db_column='InclusiveTax', max_length=1)  # Field name made lowercase.
    footer1taxrate = models.DecimalField(db_column='Footer1TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    footer2taxrate = models.DecimalField(db_column='Footer2TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    footer3taxrate = models.DecimalField(db_column='Footer3TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    taxdate = models.DateTimeField(db_column='TaxDate', blank=True, null=True)  # Field name made lowercase.
    isroundadj = models.CharField(db_column='IsRoundAdj', max_length=1)  # Field name made lowercase.
    roundingmethod = models.IntegerField(db_column='RoundingMethod')  # Field name made lowercase.
    localtaxableamt = models.DecimalField(db_column='LocalTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytax = models.DecimalField(db_column='TaxCurrencyTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxableamt = models.DecimalField(db_column='TaxCurrencyTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'IV'


class Ivdtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    focdtlkey = models.BigIntegerField(db_column='FOCDtlKey', blank=True, null=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    indent = models.SmallIntegerField(db_column='Indent', blank=True, null=True)  # Field name made lowercase.
    fontstyle = models.ForeignKey(Fontstyle, models.DO_NOTHING, db_column='FontStyle', blank=True, null=True)  # Field name made lowercase.
    mainitem = models.CharField(db_column='MainItem', max_length=1)  # Field name made lowercase.
    numbering = models.CharField(db_column='Numbering', max_length=6, blank=True, null=True)  # Field name made lowercase.
    itemcode = models.ForeignKey('Itemuom', models.DO_NOTHING, db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    location = models.ForeignKey('Location', models.DO_NOTHING, db_column='Location', blank=True, null=True)  # Field name made lowercase.
    batchno = models.ForeignKey('Itembatch', models.DO_NOTHING, db_column='BatchNo', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    furtherdescription = models.TextField(db_column='FurtherDescription', blank=True, null=True)  # Field name made lowercase.
    yourpono = models.CharField(db_column='YourPONo', max_length=25, blank=True, null=True)  # Field name made lowercase.
    yourpodate = models.DateTimeField(db_column='YourPODate', blank=True, null=True)  # Field name made lowercase.
    posttostockdate = models.DateTimeField(db_column='PostToStockDate', blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey(Dept, models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    uom = models.ForeignKey('Itemuom', models.DO_NOTHING, db_column='UOM', blank=True, null=True)  # Field name made lowercase.
    useruom = models.CharField(db_column='UserUOM', max_length=8, blank=True, null=True)  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    smallestqty = models.DecimalField(db_column='SmallestQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    transferedqty = models.DecimalField(db_column='TransferedQty', max_digits=25, decimal_places=8)  # Field name made lowercase.
    focqty = models.DecimalField(db_column='FOCQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    foctransferedqty = models.DecimalField(db_column='FOCTransferedQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    smallestunitprice = models.DecimalField(db_column='SmallestUnitPrice', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    discount = models.CharField(db_column='Discount', max_length=20, blank=True, null=True)  # Field name made lowercase.
    discountamt = models.DecimalField(db_column='DiscountAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='TaxType', blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localsubtotal = models.DecimalField(db_column='LocalSubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtotalcost = models.DecimalField(db_column='LocalTotalCost', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    localfoctotalcost = models.DecimalField(db_column='LocalFOCTotalCost', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    bonuspoint = models.DecimalField(db_column='BonusPoint', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    transferable = models.CharField(db_column='Transferable', max_length=1)  # Field name made lowercase.
    printout = models.CharField(db_column='PrintOut', max_length=1)  # Field name made lowercase.
    dtltype = models.CharField(db_column='DtlType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    calcbypercent = models.DecimalField(db_column='CalcByPercent', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    addtosubtotal = models.CharField(db_column='AddToSubTotal', max_length=1)  # Field name made lowercase.
    fromdoctype = models.CharField(db_column='FromDocType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    fromdocno = models.CharField(db_column='FromDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fromdocdtlkey = models.BigIntegerField(db_column='FromDocDtlKey', blank=True, null=True)  # Field name made lowercase.
    valuexfersodockey = models.BigIntegerField(db_column='ValueXferSODocKey', blank=True, null=True)  # Field name made lowercase.
    forconsignment = models.CharField(db_column='ForConsignment', max_length=1)  # Field name made lowercase.
    accno = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='AccNo', blank=True, null=True)  # Field name made lowercase.
    fulltransferoption = models.CharField(db_column='FullTransferOption', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fulltransferfromdoclist = models.TextField(db_column='FullTransferFromDocList', blank=True, null=True)  # Field name made lowercase.
    ourdono = models.CharField(db_column='OurDONo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ourdodate = models.DateTimeField(db_column='OurDODate', blank=True, null=True)  # Field name made lowercase.
    serialnolist = models.TextField(db_column='SerialNoList', blank=True, null=True)  # Field name made lowercase.
    estimateddeliverydate = models.CharField(db_column='EstimatedDeliveryDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    packagedockey = models.BigIntegerField(db_column='PackageDocKey', blank=True, null=True)  # Field name made lowercase.
    parentdtlkey = models.BigIntegerField(db_column='ParentDtlKey', blank=True, null=True)  # Field name made lowercase.
    subqty = models.DecimalField(db_column='SubQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    iscalcbonuspoint = models.CharField(db_column='IsCalcBonusPoint', max_length=1, blank=True, null=True)  # Field name made lowercase.
    subtotalextax = models.DecimalField(db_column='SubTotalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtax = models.DecimalField(db_column='LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.
    ruleno = models.BigIntegerField(db_column='RuleNo', blank=True, null=True)  # Field name made lowercase.
    deliverydate = models.DateTimeField(db_column='DeliveryDate', blank=True, null=True)  # Field name made lowercase.
    taxableamt = models.DecimalField(db_column='TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxadjustment = models.DecimalField(db_column='TaxAdjustment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxexportcountry = models.CharField(db_column='TaxExportCountry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    localsubtotalextax = models.DecimalField(db_column='LocalSubTotalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    extradiscountamt = models.DecimalField(db_column='ExtraDiscountAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxrate = models.DecimalField(db_column='TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    localtaxadjustment = models.DecimalField(db_column='LocalTaxAdjustment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtaxableamt = models.DecimalField(db_column='LocalTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytax = models.DecimalField(db_column='TaxCurrencyTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxableamt = models.DecimalField(db_column='TaxCurrencyTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxpermitno = models.CharField(db_column='TaxPermitNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    salesexemptionno = models.CharField(db_column='SalesExemptionNo', max_length=60, blank=True, null=True)  # Field name made lowercase.
    tariffcode = models.ForeignKey('Tariff', models.DO_NOTHING, db_column='TariffCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'IVDTL'


class Item(models.Model):
    itemgroup = models.ForeignKey(Itemgroup, models.DO_NOTHING, db_column='ItemGroup', blank=True, null=True)  # Field name made lowercase.
    itemtype = models.ForeignKey('Itemtype', models.DO_NOTHING, db_column='ItemType', blank=True, null=True)  # Field name made lowercase.
    taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='Taxtype', blank=True, null=True)  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    createduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    itembrand = models.ForeignKey('Itembrand', models.DO_NOTHING, db_column='ItemBrand', blank=True, null=True)  # Field name made lowercase.
    itemmodel = models.ForeignKey('Itemmodel', models.DO_NOTHING, db_column='ItemModel', blank=True, null=True)  # Field name made lowercase.
    purchasetaxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='PurchaseTaxType', blank=True, null=True)  # Field name made lowercase.
    tariffcode = models.ForeignKey('Tariff', models.DO_NOTHING, db_column='TariffCode', blank=True, null=True)  # Field name made lowercase.

    itemcode = models.CharField(db_column='ItemCode', primary_key=True, max_length=30)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    desc2 = models.CharField(db_column='Desc2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    furtherdescription = models.TextField(db_column='FurtherDescription', blank=True, null=True)  # Field name made lowercase.
    assemblycost = models.DecimalField(db_column='AssemblyCost', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    leadtime = models.CharField(db_column='LeadTime', max_length=40, blank=True, null=True)  # Field name made lowercase.
    stockcontrol = models.CharField(db_column='StockControl', max_length=1)  # Field name made lowercase.
    hasserialno = models.CharField(db_column='HasSerialNo', max_length=1)  # Field name made lowercase.
    hasbatchno = models.CharField(db_column='HasBatchNo', max_length=1)  # Field name made lowercase.
    dutyrate = models.DecimalField(db_column='DutyRate', max_digits=18, decimal_places=6)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    imagefilename = models.CharField(db_column='ImageFileName', max_length=120, blank=True, null=True)  # Field name made lowercase.
    costingmethod = models.SmallIntegerField(db_column='CostingMethod')  # Field name made lowercase.
    salesuom = models.CharField(db_column='SalesUOM', max_length=8)  # Field name made lowercase.
    purchaseuom = models.CharField(db_column='PurchaseUOM', max_length=8)  # Field name made lowercase.
    reportuom = models.CharField(db_column='ReportUOM', max_length=8)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    isactive = models.CharField(db_column='IsActive', max_length=1)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    snformatname = models.CharField(db_column='SNFormatName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    iscalcbonuspoint = models.CharField(db_column='IsCalcBonusPoint', max_length=1, blank=True, null=True)  # Field name made lowercase.
    markupratio = models.DecimalField(db_column='MarkupRatio', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    haspromoter = models.CharField(db_column='HasPromoter', max_length=1)  # Field name made lowercase.
    globalcode = models.CharField(db_column='GlobalCode', max_length=30, blank=True, null=True)  # Field name made lowercase.
    leadtimeday = models.IntegerField(db_column='LeadTimeDay', blank=True, null=True)  # Field name made lowercase.
    externallink = models.TextField(db_column='ExternalLink', blank=True, null=True)  # Field name made lowercase.
    discontinued = models.CharField(db_column='Discontinued', max_length=1)  # Field name made lowercase.
    autouomconversion = models.CharField(db_column='AutoUOMConversion', max_length=1, blank=True, null=True)  # Field name made lowercase.
    baseuom = models.CharField(db_column='BaseUOM', max_length=8)  # Field name made lowercase.
    backordercontrol = models.CharField(db_column='BackOrderControl', max_length=1)  # Field name made lowercase.

    class Meta:
 
        db_table = 'Item'


class Itembom(models.Model):
    itembomkey = models.BigAutoField(db_column='ItemBOMKey', primary_key=True)  # Field name made lowercase.
    itemcode = models.ForeignKey(Item, models.DO_NOTHING, db_column='ItemCode')  # Field name made lowercase.
    subitemcode = models.ForeignKey(Item, models.DO_NOTHING, db_column='SubItemCode')  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=25, decimal_places=8)  # Field name made lowercase.
    overheadcost = models.DecimalField(db_column='OverheadCost', max_digits=25, decimal_places=8)  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.

    class Meta:
 
        db_table = 'ItemBOM'


class Itembalqty(models.Model):
    itemcode = models.OneToOneField('Itemuom', models.DO_NOTHING, db_column='ItemCode', primary_key=True)  # Field name made lowercase.
    uom = models.ForeignKey('Itemuom', models.DO_NOTHING, db_column='UOM')  # Field name made lowercase.
    location = models.ForeignKey('Location', models.DO_NOTHING, db_column='Location')  # Field name made lowercase.
    balqty = models.DecimalField(db_column='BalQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'ItemBalQty'
        unique_together = (('itemcode', 'uom', 'location'),)


class Itembatch(models.Model):
    itemcode = models.CharField(db_column='ItemCode', primary_key=True, max_length=30)  # Field name made lowercase.
    batchno = models.CharField(db_column='BatchNo', max_length=20)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=40, blank=True, null=True)  # Field name made lowercase.
    manufactureddate = models.DateTimeField(db_column='ManufacturedDate', blank=True, null=True)  # Field name made lowercase.
    expirydate = models.DateTimeField(db_column='ExpiryDate', blank=True, null=True)  # Field name made lowercase.
    lastsaledate = models.DateTimeField(db_column='LastSaleDate', blank=True, null=True)  # Field name made lowercase.
    balqty = models.DecimalField(db_column='BalQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'ItemBatch'
        unique_together = (('itemcode', 'batchno'),)


class Itembatchbalqty(models.Model):
    itemcode = models.OneToOneField('Itemuom', models.DO_NOTHING, db_column='ItemCode', primary_key=True)  # Field name made lowercase.
    uom = models.ForeignKey('Itemuom', models.DO_NOTHING, db_column='UOM')  # Field name made lowercase.
    location = models.ForeignKey('Location', models.DO_NOTHING, db_column='Location')  # Field name made lowercase.
    batchno = models.CharField(db_column='BatchNo', max_length=20)  # Field name made lowercase.
    balqty = models.DecimalField(db_column='BalQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    mostrecentlycost = models.DecimalField(db_column='MostRecentlyCost', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'ItemBatchBalQty'
        unique_together = (('itemcode', 'uom', 'location', 'batchno'),)


class Itembrand(models.Model):
    itembrand = models.CharField(db_column='ItemBrand', primary_key=True, max_length=20)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=40, blank=True, null=True)  # Field name made lowercase.
    desc2 = models.CharField(db_column='Desc2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    markupratio = models.DecimalField(db_column='MarkupRatio', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'ItemBrand'


class Itemcostchangehistory(models.Model):
    hkey = models.BigAutoField(db_column='HKey', primary_key=True)  # Field name made lowercase.
    itemcode = models.ForeignKey('Itemuom', models.DO_NOTHING, db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    uom = models.ForeignKey('Itemuom', models.DO_NOTHING, db_column='UOM', blank=True, null=True)  # Field name made lowercase.
    changetime = models.DateTimeField(db_column='ChangeTime')  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'ItemCostChangeHistory'


class Itemcosthistory(models.Model):
    hkey = models.AutoField(db_column='HKey', primary_key=True)  # Field name made lowercase.
    itemcode = models.ForeignKey('Itemuom', models.DO_NOTHING, db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    uom = models.ForeignKey('Itemuom', models.DO_NOTHING, db_column='UOM', blank=True, null=True)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    dtlkey = models.BigIntegerField(db_column='DtlKey')  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    doctype = models.CharField(db_column='DocType', max_length=2)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', max_length=20)  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp', blank=True, null=True)  # Field name made lowercase.
    createduserid = models.CharField(db_column='CreatedUserID', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'ItemCostHistory'


class Itemcurrencyprice(models.Model):
    itemcode = models.OneToOneField('Itemuom', models.DO_NOTHING, db_column='ItemCode', primary_key=True)  # Field name made lowercase.
    uom = models.ForeignKey('Itemuom', models.DO_NOTHING, db_column='UOM')  # Field name made lowercase.
    currencycode = models.ForeignKey(Currency, models.DO_NOTHING, db_column='CurrencyCode')  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.

    class Meta:
 
        db_table = 'ItemCurrencyPrice'
        unique_together = (('itemcode', 'uom', 'currencycode'),)


class Itemgroup(models.Model):
    itemgroup = models.CharField(db_column='ItemGroup', primary_key=True, max_length=8)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=40, blank=True, null=True)  # Field name made lowercase.
    desc2 = models.CharField(db_column='Desc2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    salescode = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='SalesCode', blank=True, null=True)  # Field name made lowercase.
    cashsalescode = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='CashSalesCode', blank=True, null=True)  # Field name made lowercase.
    salesreturncode = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='SalesReturnCode', blank=True, null=True)  # Field name made lowercase.
    salesdiscountcode = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='SalesDiscountCode', blank=True, null=True)  # Field name made lowercase.
    purchasediscountcode = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='PurchaseDiscountCode', blank=True, null=True)  # Field name made lowercase.
    purchasecode = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='PurchaseCode', blank=True, null=True)  # Field name made lowercase.
    purchasereturncode = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='PurchaseReturnCode', blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    shortcode = models.CharField(db_column='ShortCode', max_length=8, blank=True, null=True)  # Field name made lowercase.
    markupratio = models.DecimalField(db_column='MarkupRatio', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    balancestockcode = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='BalanceStockCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'ItemGroup'


class Itemlocationprice(models.Model):
    itemcode = models.OneToOneField('Itemuom', models.DO_NOTHING, db_column='ItemCode', primary_key=True)  # Field name made lowercase.
    uom = models.ForeignKey('Itemuom', models.DO_NOTHING, db_column='UOM')  # Field name made lowercase.
    location = models.ForeignKey('Location', models.DO_NOTHING, db_column='Location')  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    minqty = models.DecimalField(db_column='MinQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    maxqty = models.DecimalField(db_column='MaxQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    normallevel = models.DecimalField(db_column='NormalLevel', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    reolevel = models.DecimalField(db_column='ReOLevel', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    reoqty = models.DecimalField(db_column='ReOQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'ItemLocationPrice'
        unique_together = (('itemcode', 'uom', 'location'),)


class Itemmodel(models.Model):
    itemmodel = models.CharField(db_column='ItemModel', primary_key=True, max_length=20)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=40, blank=True, null=True)  # Field name made lowercase.
    desc2 = models.CharField(db_column='Desc2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    markupratio = models.DecimalField(db_column='MarkupRatio', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'ItemModel'


class Itemopening(models.Model):
    itemopeningkey = models.BigIntegerField(db_column='ItemOpeningKey', primary_key=True)  # Field name made lowercase.
    itemcode = models.ForeignKey('Itemuom', models.DO_NOTHING, db_column='ItemCode')  # Field name made lowercase.
    uom = models.ForeignKey('Itemuom', models.DO_NOTHING, db_column='UOM')  # Field name made lowercase.
    location = models.ForeignKey('Location', models.DO_NOTHING, db_column='Location')  # Field name made lowercase.
    batchno = models.ForeignKey(Itembatch, models.DO_NOTHING, db_column='BatchNo', blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=25, decimal_places=8)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=25, decimal_places=8)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey(Dept, models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.

    class Meta:
 
        db_table = 'ItemOpening'


class Itemprice(models.Model):
    itempricekey = models.BigIntegerField(db_column='ItemPriceKey', primary_key=True)  # Field name made lowercase.
    itemcode = models.ForeignKey('Itemuom', models.DO_NOTHING, db_column='ItemCode')  # Field name made lowercase.
    uom = models.ForeignKey('Itemuom', models.DO_NOTHING, db_column='UOM')  # Field name made lowercase.
    pricecategory = models.ForeignKey('Pricecategory', models.DO_NOTHING, db_column='PriceCategory', blank=True, null=True)  # Field name made lowercase.
    accno = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='AccNo', blank=True, null=True)  # Field name made lowercase.
    suppcustitemcode = models.CharField(db_column='SuppCustItemCode', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ref = models.CharField(db_column='Ref', max_length=80, blank=True, null=True)  # Field name made lowercase.
    usefixedprice = models.CharField(db_column='UseFixedPrice', max_length=1)  # Field name made lowercase.
    fixedprice = models.DecimalField(db_column='FixedPrice', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    fixeddetaildiscount = models.CharField(db_column='FixedDetailDiscount', max_length=20, blank=True, null=True)  # Field name made lowercase.
    qty1 = models.DecimalField(db_column='Qty1', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    price1 = models.DecimalField(db_column='Price1', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    detaildiscount1 = models.CharField(db_column='DetailDiscount1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    qty2 = models.DecimalField(db_column='Qty2', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    price2 = models.DecimalField(db_column='Price2', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    detaildiscount2 = models.CharField(db_column='DetailDiscount2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    qty3 = models.DecimalField(db_column='Qty3', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    price3 = models.DecimalField(db_column='Price3', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    detaildiscount3 = models.CharField(db_column='DetailDiscount3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    qty4 = models.DecimalField(db_column='Qty4', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    price4 = models.DecimalField(db_column='Price4', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    detaildiscount4 = models.CharField(db_column='DetailDiscount4', max_length=20, blank=True, null=True)  # Field name made lowercase.
    foclevel = models.DecimalField(db_column='FOCLevel', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    focqty = models.DecimalField(db_column='FOCQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    bonuspointqty = models.DecimalField(db_column='BonusPointQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    bonuspoint = models.DecimalField(db_column='BonusPoint', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.

    class Meta:
 
        db_table = 'ItemPrice'


class Itempricechangehistory(models.Model):
    hkey = models.BigAutoField(db_column='HKey', primary_key=True)  # Field name made lowercase.
    itemcode = models.ForeignKey('Itemuom', models.DO_NOTHING, db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    uom = models.ForeignKey('Itemuom', models.DO_NOTHING, db_column='UOM', blank=True, null=True)  # Field name made lowercase.
    changetime = models.DateTimeField(db_column='ChangeTime')  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'ItemPriceChangeHistory'


class Itemreplacement(models.Model):
    itemcode = models.OneToOneField(Item, models.DO_NOTHING, db_column='ItemCode', primary_key=True)  # Field name made lowercase.
    replacementitemcode = models.ForeignKey(Item, models.DO_NOTHING, db_column='ReplacementItemCode')  # Field name made lowercase.
    replacementdegree = models.DecimalField(db_column='ReplacementDegree', max_digits=18, decimal_places=6)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'ItemReplacement'
        unique_together = (('itemcode', 'replacementitemcode'),)


class Itemserialno(models.Model):
    serialnumber = models.CharField(db_column='SerialNumber', primary_key=True, max_length=40)  # Field name made lowercase.
    itemcode = models.ForeignKey(Itembatch, models.DO_NOTHING, db_column='ItemCode')  # Field name made lowercase.
    batchno = models.ForeignKey(Itembatch, models.DO_NOTHING, db_column='BatchNo', blank=True, null=True)  # Field name made lowercase.
    manufactureddate = models.DateTimeField(db_column='ManufacturedDate', blank=True, null=True)  # Field name made lowercase.
    expirydate = models.DateTimeField(db_column='ExpiryDate', blank=True, null=True)  # Field name made lowercase.
    lastsalesdate = models.DateTimeField(db_column='LastSalesDate', blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=20, blank=True, null=True)  # Field name made lowercase.
    qty = models.IntegerField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    csgnqty = models.IntegerField(db_column='CSGNQty', blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'ItemSerialNo'
        unique_together = (('serialnumber', 'itemcode', 'itemcode'),)


class Itemserialnodtl(models.Model):
    serialnumber = models.CharField(db_column='SerialNumber', primary_key=True, max_length=40)  # Field name made lowercase.
    itemcode = models.ForeignKey(Item, models.DO_NOTHING, db_column='ItemCode')  # Field name made lowercase.
    location = models.ForeignKey('Location', models.DO_NOTHING, db_column='Location')  # Field name made lowercase.
    qty = models.IntegerField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    csgnqty = models.IntegerField(db_column='CSGNQty', blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'ItemSerialNoDtl'
        unique_together = (('serialnumber', 'itemcode', 'location'),)


class Itemsubcode(models.Model):
    itemcode = models.OneToOneField(Item, models.DO_NOTHING, db_column='ItemCode', primary_key=True)  # Field name made lowercase.
    subcode = models.CharField(db_column='SubCode', max_length=30)  # Field name made lowercase.

    class Meta:
 
        db_table = 'ItemSubCode'
        unique_together = (('itemcode', 'subcode'),)


class Itemtype(models.Model):
    itemtype = models.CharField(db_column='ItemType', primary_key=True, max_length=12)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=40, blank=True, null=True)  # Field name made lowercase.
    desc2 = models.CharField(db_column='Desc2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    shortcode = models.CharField(db_column='ShortCode', max_length=8, blank=True, null=True)  # Field name made lowercase.
    markupratio = models.DecimalField(db_column='MarkupRatio', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'ItemType'


class Itemuom(models.Model):
    itemcode = models.CharField(db_column='ItemCode', primary_key=True, max_length=30)  # Field name made lowercase.
    uom = models.CharField(db_column='UOM', max_length=8)  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=25, decimal_places=8)  # Field name made lowercase.
    shelf = models.CharField(db_column='Shelf', max_length=20, blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    realcost = models.DecimalField(db_column='RealCost', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    mostrecentlycost = models.DecimalField(db_column='MostRecentlyCost', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    minsaleprice = models.DecimalField(db_column='MinSalePrice', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    maxsaleprice = models.DecimalField(db_column='MaxSalePrice', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    minpurchaseprice = models.DecimalField(db_column='MinPurchasePrice', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    maxpurchaseprice = models.DecimalField(db_column='MaxPurchasePrice', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    balqty = models.DecimalField(db_column='BalQty', max_digits=25, decimal_places=8)  # Field name made lowercase.
    minqty = models.DecimalField(db_column='MinQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    maxqty = models.DecimalField(db_column='MaxQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    normallevel = models.DecimalField(db_column='NormalLevel', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    reolevel = models.DecimalField(db_column='ReOLevel', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    reoqty = models.DecimalField(db_column='ReOQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    foclevel = models.DecimalField(db_column='FOCLevel', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    focqty = models.DecimalField(db_column='FOCQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    bonuspointqty = models.DecimalField(db_column='BonusPointQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    bonuspoint = models.DecimalField(db_column='BonusPoint', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    weight = models.DecimalField(db_column='Weight', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    weightuom = models.CharField(db_column='WeightUOM', max_length=8, blank=True, null=True)  # Field name made lowercase.
    volume = models.DecimalField(db_column='Volume', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    volumeuom = models.CharField(db_column='VolumeUOM', max_length=8, blank=True, null=True)  # Field name made lowercase.
    barcode = models.CharField(db_column='BarCode', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    redeembonuspoint = models.DecimalField(db_column='RedeemBonusPoint', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    csgnqty = models.DecimalField(db_column='CSGNQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    price2 = models.DecimalField(db_column='Price2', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'ItemUOM'
        unique_together = (('itemcode', 'uom'),)


class Je(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', unique=True, max_length=20)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    journaltype = models.ForeignKey('Journal', models.DO_NOTHING, db_column='JournalType')  # Field name made lowercase.
    currencycode = models.ForeignKey(Currency, models.DO_NOTHING, db_column='CurrencyCode')  # Field name made lowercase.
    currencyrate = models.DecimalField(db_column='CurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    totaldr = models.DecimalField(db_column='TotalDR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    totalcr = models.DecimalField(db_column='TotalCR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    externallink = models.TextField(db_column='ExternalLink', blank=True, null=True)  # Field name made lowercase.
    cancelled = models.CharField(db_column='Cancelled', max_length=1)  # Field name made lowercase.
    printcount = models.SmallIntegerField(db_column='PrintCount')  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    createduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    sourcetype = models.CharField(db_column='SourceType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    sourcekey = models.BigIntegerField(db_column='SourceKey', blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    postdetaildesc = models.CharField(db_column='PostDetailDesc', max_length=1, blank=True, null=True)  # Field name made lowercase.
    docno2 = models.CharField(db_column='DocNo2', max_length=25, blank=True, null=True)  # Field name made lowercase.
    taxabledr = models.DecimalField(db_column='TaxableDR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxablecr = models.DecimalField(db_column='TaxableCR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxdr = models.DecimalField(db_column='TaxDR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcr = models.DecimalField(db_column='TaxCR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    extaxdr = models.DecimalField(db_column='ExTaxDR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    extaxcr = models.DecimalField(db_column='ExTaxCR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nettotaldr = models.DecimalField(db_column='NetTotalDR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nettotalcr = models.DecimalField(db_column='NetTotalCR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtotaldr = models.DecimalField(db_column='LocalTotalDR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtotalcr = models.DecimalField(db_column='LocalTotalCR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtaxabledr = models.DecimalField(db_column='LocalTaxableDR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtaxablecr = models.DecimalField(db_column='LocalTaxableCR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtaxdr = models.DecimalField(db_column='LocalTaxDR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtaxcr = models.DecimalField(db_column='LocalTaxCR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localextaxdr = models.DecimalField(db_column='LocalExTaxDR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localextaxcr = models.DecimalField(db_column='LocalExTaxCR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localnettotaldr = models.DecimalField(db_column='LocalNetTotalDR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localnettotalcr = models.DecimalField(db_column='LocalNetTotalCR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    totaxcurrencyrate = models.DecimalField(db_column='ToTaxCurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    inclusivetax = models.CharField(db_column='InclusiveTax', max_length=1)  # Field name made lowercase.
    totaldrextax = models.DecimalField(db_column='TotalDRExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    totalcrextax = models.DecimalField(db_column='TotalCRExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtotaldrextax = models.DecimalField(db_column='LocalTotalDRExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtotalcrextax = models.DecimalField(db_column='LocalTotalCRExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    gltrxid = models.BigIntegerField(db_column='GLTrxID', blank=True, null=True)  # Field name made lowercase.
    taxdate = models.DateTimeField(db_column='TaxDate', blank=True, null=True)  # Field name made lowercase.
    roundingmethod = models.IntegerField(db_column='RoundingMethod')  # Field name made lowercase.
    taxcurrencytaxdr = models.DecimalField(db_column='TaxCurrencyTaxDR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxcr = models.DecimalField(db_column='TaxCurrencyTaxCR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxabledr = models.DecimalField(db_column='TaxCurrencyTaxableDR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxablecr = models.DecimalField(db_column='TaxCurrencyTaxableCR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'JE'


class Jedtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    accno = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='AccNo', blank=True, null=True)  # Field name made lowercase.
    toaccountrate = models.DecimalField(db_column='ToAccountRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey(Dept, models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    furtherdescription = models.TextField(db_column='FurtherDescription', blank=True, null=True)  # Field name made lowercase.
    dr = models.DecimalField(db_column='DR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cr = models.DecimalField(db_column='CR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='TaxType', blank=True, null=True)  # Field name made lowercase.
    supplypurchase = models.CharField(db_column='SupplyPurchase', max_length=1)  # Field name made lowercase.
    taxdr = models.DecimalField(db_column='TaxDR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcr = models.DecimalField(db_column='TaxCR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    totaldr = models.DecimalField(db_column='TotalDR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    totalcr = models.DecimalField(db_column='TotalCR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    salesagent = models.ForeignKey('Salesagent', models.DO_NOTHING, db_column='SalesAgent', blank=True, null=True)  # Field name made lowercase.
    taxabledr = models.DecimalField(db_column='TaxableDR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxablecr = models.DecimalField(db_column='TaxableCR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    refno2 = models.CharField(db_column='RefNo2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    taxpermitno = models.CharField(db_column='TaxPermitNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    taxadjustment = models.DecimalField(db_column='TaxAdjustment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxexportcountry = models.CharField(db_column='TaxExportCountry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    taxbrno = models.CharField(db_column='TaxBRNo', max_length=25, blank=True, null=True)  # Field name made lowercase.
    taxbname = models.CharField(db_column='TaxBName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    taxrefno = models.CharField(db_column='TaxRefNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    taxrate = models.DecimalField(db_column='TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    localtaxadjustment = models.DecimalField(db_column='LocalTaxAdjustment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxregisterno = models.CharField(db_column='TaxRegisterNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    taxbilldate = models.DateTimeField(db_column='TaxBillDate', blank=True, null=True)  # Field name made lowercase.
    localtaxabledr = models.DecimalField(db_column='LocalTaxableDR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtaxablecr = models.DecimalField(db_column='LocalTaxableCR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtaxdr = models.DecimalField(db_column='LocalTaxDR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtaxcr = models.DecimalField(db_column='LocalTaxCR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxdr = models.DecimalField(db_column='TaxCurrencyTaxDR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxcr = models.DecimalField(db_column='TaxCurrencyTaxCR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxabledr = models.DecimalField(db_column='TaxCurrencyTaxableDR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxablecr = models.DecimalField(db_column='TaxCurrencyTaxableCR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    inclusivetax = models.CharField(db_column='InclusiveTax', max_length=1)  # Field name made lowercase.
    tariffcode = models.ForeignKey('Tariff', models.DO_NOTHING, db_column='TariffCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'JEDTL'


class Journal(models.Model):
    journaltype = models.CharField(db_column='JournalType', primary_key=True, max_length=10)  # Field name made lowercase.
    entrytype = models.CharField(db_column='EntryType', max_length=1)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=40, blank=True, null=True)  # Field name made lowercase.
    desc2 = models.CharField(db_column='Desc2', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'Journal'


class Layout(models.Model):
    title = models.CharField(db_column='Title', primary_key=True, max_length=60)  # Field name made lowercase.
    formname = models.CharField(db_column='FormName', max_length=60, blank=True, null=True)  # Field name made lowercase.
    componentname = models.CharField(db_column='ComponentName', max_length=60, blank=True, null=True)  # Field name made lowercase.
    template = models.TextField(db_column='Template', blank=True, null=True)  # Field name made lowercase.
    isdefault = models.CharField(db_column='IsDefault', max_length=1)  # Field name made lowercase.
    lastupdate = models.BigIntegerField(db_column='LastUpdate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'Layout'


class Layoutusers(models.Model):
    title = models.CharField(db_column='Title', primary_key=True, max_length=60)  # Field name made lowercase.
    userid = models.CharField(db_column='UserID', max_length=10)  # Field name made lowercase.

    class Meta:
 
        db_table = 'LayoutUsers'
        unique_together = (('title', 'userid'),)


class Location(models.Model):
    location = models.CharField(db_column='Location', primary_key=True, max_length=8)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=80, blank=True, null=True)  # Field name made lowercase.
    desc2 = models.CharField(db_column='Desc2', max_length=80, blank=True, null=True)  # Field name made lowercase.
    address1 = models.CharField(db_column='Address1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    address2 = models.CharField(db_column='Address2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    address3 = models.CharField(db_column='Address3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    address4 = models.CharField(db_column='Address4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    postcode = models.CharField(db_column='PostCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    phone1 = models.CharField(db_column='Phone1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    phone2 = models.CharField(db_column='Phone2', max_length=25, blank=True, null=True)  # Field name made lowercase.
    fax1 = models.CharField(db_column='Fax1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    fax2 = models.CharField(db_column='Fax2', max_length=25, blank=True, null=True)  # Field name made lowercase.
    contact = models.CharField(db_column='Contact', max_length=40, blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    isactive = models.CharField(db_column='IsActive', max_length=1)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    areacode = models.ForeignKey(Area, models.DO_NOTHING, db_column='AreaCode', blank=True, null=True)  # Field name made lowercase.
    cashpaymentmethod = models.ForeignKey('Paymentmethod', models.DO_NOTHING, db_column='CashPaymentMethod', blank=True, null=True)  # Field name made lowercase.
    debitcardpaymentmethod = models.ForeignKey('Paymentmethod', models.DO_NOTHING, db_column='DebitCardPaymentMethod', blank=True, null=True)  # Field name made lowercase.
    voucherpaymentmethod = models.ForeignKey('Paymentmethod', models.DO_NOTHING, db_column='VoucherPaymentMethod', blank=True, null=True)  # Field name made lowercase.
    chequepaymentmethod = models.ForeignKey('Paymentmethod', models.DO_NOTHING, db_column='ChequePaymentMethod', blank=True, null=True)  # Field name made lowercase.
    pointpaymentmethod = models.ForeignKey('Paymentmethod', models.DO_NOTHING, db_column='PointPaymentMethod', blank=True, null=True)  # Field name made lowercase.
    roundingaccno = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='RoundingAccNo', blank=True, null=True)  # Field name made lowercase.
    depositaccno = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='DepositAccNo', blank=True, null=True)  # Field name made lowercase.
    forfeitedaccno = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='ForfeitedAccNo', blank=True, null=True)  # Field name made lowercase.
    creditcardchargesaccno = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='CreditCardChargesAccNo', blank=True, null=True)  # Field name made lowercase.
    pointpaymentaccno = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='PointPaymentAccNo', blank=True, null=True)  # Field name made lowercase.
    servicechargeaccno = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='ServiceChargeAccNo', blank=True, null=True)  # Field name made lowercase.
    voucherforfeitedaccno = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='VoucherForfeitedAccNo', blank=True, null=True)  # Field name made lowercase.
    alipaypaymentmethod = models.ForeignKey('Paymentmethod', models.DO_NOTHING, db_column='AlipayPaymentMethod', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'Location'


class Mru(models.Model):
    mrukey = models.IntegerField(db_column='MRUKey', primary_key=True)  # Field name made lowercase.
    userid = models.CharField(db_column='UserID', max_length=10)  # Field name made lowercase.
    mruitems = models.TextField(db_column='MRUItems', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'MRU'
        unique_together = (('mrukey', 'userid'),)


class Member(models.Model):
    memberno = models.CharField(db_column='MemberNo', primary_key=True, max_length=20)  # Field name made lowercase.
    membertype = models.ForeignKey('Membertype', models.DO_NOTHING, db_column='MemberType')  # Field name made lowercase.
    id = models.CharField(db_column='ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    address1 = models.CharField(db_column='Address1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    address2 = models.CharField(db_column='Address2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    address3 = models.CharField(db_column='Address3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    address4 = models.CharField(db_column='Address4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    postcode = models.CharField(db_column='PostCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    areacode = models.ForeignKey(Area, models.DO_NOTHING, db_column='AreaCode', blank=True, null=True)  # Field name made lowercase.
    individual = models.CharField(db_column='Individual', max_length=1)  # Field name made lowercase.
    race = models.ForeignKey('Race', models.DO_NOTHING, db_column='Race', blank=True, null=True)  # Field name made lowercase.
    dob = models.DateTimeField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    debtorcode = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='DebtorCode', blank=True, null=True)  # Field name made lowercase.
    companyname = models.CharField(db_column='CompanyName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=30, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=40, blank=True, null=True)  # Field name made lowercase.
    mobilephone = models.CharField(db_column='MobilePhone', max_length=25, blank=True, null=True)  # Field name made lowercase.
    directphone = models.CharField(db_column='DirectPhone', max_length=25, blank=True, null=True)  # Field name made lowercase.
    directfax = models.CharField(db_column='DirectFax', max_length=25, blank=True, null=True)  # Field name made lowercase.
    emailaddress = models.CharField(db_column='EmailAddress', max_length=80, blank=True, null=True)  # Field name made lowercase.
    imaddress = models.CharField(db_column='IMAddress', max_length=40, blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    openingpoints = models.DecimalField(db_column='OpeningPoints', max_digits=19, decimal_places=2)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=1, blank=True, null=True)  # Field name made lowercase.
    registerdate = models.DateTimeField(db_column='RegisterDate', blank=True, null=True)  # Field name made lowercase.
    expirydate = models.DateTimeField(db_column='ExpiryDate', blank=True, null=True)  # Field name made lowercase.
    isactive = models.CharField(db_column='IsActive', max_length=1)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    createduserid = models.CharField(db_column='CreatedUserID', max_length=10)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.CharField(db_column='LastModifiedUserID', max_length=10)  # Field name made lowercase.
    photo = models.BinaryField(db_column='Photo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'Member'


class Membertype(models.Model):
    membertype = models.CharField(db_column='MemberType', primary_key=True, max_length=20)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=80, blank=True, null=True)  # Field name made lowercase.
    level = models.SmallIntegerField(db_column='Level')  # Field name made lowercase.

    class Meta:
 
        db_table = 'MemberType'


class Netusers(models.Model):
    sessionkey = models.BigAutoField(db_column='SessionKey', primary_key=True)  # Field name made lowercase.
    lastcheckdatetime = models.DateTimeField(db_column='LastCheckDateTime')  # Field name made lowercase.
    logintime = models.DateTimeField(db_column='LoginTime')  # Field name made lowercase.
    isinternetuser = models.CharField(db_column='IsInternetUser', max_length=1)  # Field name made lowercase.
    userid = models.CharField(db_column='UserID', max_length=10)  # Field name made lowercase.
    computername = models.CharField(db_column='ComputerName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'NetUsers'


class Notifallowusers(models.Model):
    notificationkey = models.BigIntegerField(db_column='NotificationKey', primary_key=True)  # Field name made lowercase.
    userid = models.CharField(db_column='UserID', max_length=10)  # Field name made lowercase.

    class Meta:
 
        db_table = 'NotifAllowUsers'
        unique_together = (('notificationkey', 'userid'),)


class Notifreadusers(models.Model):
    notificationkey = models.BigIntegerField(db_column='NotificationKey', primary_key=True)  # Field name made lowercase.
    userid = models.CharField(db_column='UserID', max_length=10)  # Field name made lowercase.

    class Meta:
 
        db_table = 'NotifReadUsers'
        unique_together = (('notificationkey', 'userid'),)


class Notification(models.Model):
    notificationkey = models.BigIntegerField(db_column='NotificationKey', primary_key=True)  # Field name made lowercase.
    header = models.TextField(db_column='Header', blank=True, null=True)  # Field name made lowercase.
    detail = models.TextField(db_column='Detail', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=40, blank=True, null=True)  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.

    class Meta:
 
        db_table = 'Notification'


class Obdtl(models.Model):
    obdtlkey = models.BigAutoField(db_column='OBDtlKey', primary_key=True)  # Field name made lowercase.
    periodno = models.IntegerField(db_column='PeriodNo')  # Field name made lowercase.
    accno = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='AccNo')  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey(Dept, models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    homeamount = models.DecimalField(db_column='HomeAmount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sourcetype = models.CharField(db_column='SourceType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    sourcekey = models.BigIntegerField(db_column='SourceKey', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'OBDTL'


class Obalance(models.Model):
    periodno = models.IntegerField(db_column='PeriodNo')  # Field name made lowercase.
    accno = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='AccNo')  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey(Dept, models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    dr = models.DecimalField(db_column='DR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cr = models.DecimalField(db_column='CR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    homedr = models.DecimalField(db_column='HomeDR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    homecr = models.DecimalField(db_column='HomeCR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'OBalance'


class Objecteventlog(models.Model):
    eventkey = models.BigIntegerField(db_column='EventKey', primary_key=True)  # Field name made lowercase.
    occurtime = models.DateTimeField(db_column='OccurTime')  # Field name made lowercase.
    eventtype = models.CharField(db_column='EventType', max_length=1)  # Field name made lowercase.
    userid = models.CharField(db_column='UserID', max_length=10)  # Field name made lowercase.
    objtype = models.CharField(db_column='ObjType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    objkey = models.BigIntegerField(db_column='ObjKey', blank=True, null=True)  # Field name made lowercase.
    objcode = models.CharField(db_column='ObjCode', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'ObjectEventLog'


class Pbalance(models.Model):
    periodno = models.IntegerField(db_column='PeriodNo')  # Field name made lowercase.
    accno = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='AccNo')  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey(Dept, models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    dr = models.DecimalField(db_column='DR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cr = models.DecimalField(db_column='CR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    homedr = models.DecimalField(db_column='HomeDR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    homecr = models.DecimalField(db_column='HomeCR', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'PBalance'


class Pi(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', unique=True, max_length=20)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    creditorcode = models.ForeignKey(Branch, models.DO_NOTHING, db_column='CreditorCode', blank=True, null=True)  # Field name made lowercase.
    creditorname = models.CharField(db_column='CreditorName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ref = models.CharField(db_column='Ref', max_length=40, blank=True, null=True)  # Field name made lowercase.
    supplierdono = models.CharField(db_column='SupplierDONo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    supplierinvoiceno = models.CharField(db_column='SupplierInvoiceNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=80, blank=True, null=True)  # Field name made lowercase.
    displayterm = models.ForeignKey('Terms', models.DO_NOTHING, db_column='DisplayTerm')  # Field name made lowercase.
    purchaseagent = models.ForeignKey('Purchaseagent', models.DO_NOTHING, db_column='PurchaseAgent', blank=True, null=True)  # Field name made lowercase.
    invaddr1 = models.CharField(db_column='InvAddr1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr2 = models.CharField(db_column='InvAddr2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr3 = models.CharField(db_column='InvAddr3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr4 = models.CharField(db_column='InvAddr4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    phone1 = models.CharField(db_column='Phone1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    fax1 = models.CharField(db_column='Fax1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    attention = models.CharField(db_column='Attention', max_length=40, blank=True, null=True)  # Field name made lowercase.
    branchcode = models.ForeignKey(Branch, models.DO_NOTHING, db_column='BranchCode', blank=True, null=True)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1param = models.DecimalField(db_column='Footer1Param', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1amt = models.DecimalField(db_column='Footer1Amt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1localamt = models.DecimalField(db_column='Footer1LocalAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='Footer1TaxType', blank=True, null=True)  # Field name made lowercase.
    footer2param = models.DecimalField(db_column='Footer2Param', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2amt = models.DecimalField(db_column='Footer2Amt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2localamt = models.DecimalField(db_column='Footer2LocalAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='Footer2TaxType', blank=True, null=True)  # Field name made lowercase.
    footer3param = models.DecimalField(db_column='Footer3Param', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3amt = models.DecimalField(db_column='Footer3Amt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3localamt = models.DecimalField(db_column='Footer3LocalAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='Footer3TaxType', blank=True, null=True)  # Field name made lowercase.
    currencycode = models.ForeignKey(Currency, models.DO_NOTHING, db_column='CurrencyCode')  # Field name made lowercase.
    currencyrate = models.DecimalField(db_column='CurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    nettotal = models.DecimalField(db_column='NetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localnettotal = models.DecimalField(db_column='LocalNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtax = models.DecimalField(db_column='LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    foreigncharges = models.DecimalField(db_column='ForeignCharges', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localcharges = models.DecimalField(db_column='LocalCharges', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    landedcostmethod = models.CharField(db_column='LandedCostMethod', max_length=1, blank=True, null=True)  # Field name made lowercase.
    posttostock = models.CharField(db_column='PostToStock', max_length=1)  # Field name made lowercase.
    posttogl = models.CharField(db_column='PostToGL', max_length=1)  # Field name made lowercase.
    referdockey = models.BigIntegerField(db_column='ReferDocKey', blank=True, null=True)  # Field name made lowercase.
    referpaymentdockey = models.BigIntegerField(db_column='ReferPaymentDocKey', blank=True, null=True)  # Field name made lowercase.
    transferable = models.CharField(db_column='Transferable', max_length=1)  # Field name made lowercase.
    todoctype = models.CharField(db_column='ToDocType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    todockey = models.BigIntegerField(db_column='ToDocKey', blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    remark1 = models.CharField(db_column='Remark1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark2 = models.CharField(db_column='Remark2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark3 = models.CharField(db_column='Remark3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark4 = models.CharField(db_column='Remark4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    printcount = models.SmallIntegerField(db_column='PrintCount')  # Field name made lowercase.
    cancelled = models.CharField(db_column='Cancelled', max_length=1)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    createduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    externallink = models.TextField(db_column='ExternalLink', blank=True, null=True)  # Field name made lowercase.
    refdocno = models.CharField(db_column='RefDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    csgndockey = models.BigIntegerField(db_column='CSGNDocKey', blank=True, null=True)  # Field name made lowercase.
    cansync = models.CharField(db_column='CanSync', max_length=1)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    todtlkey = models.BigIntegerField(db_column='ToDtlKey', blank=True, null=True)  # Field name made lowercase.
    fulltransferoption = models.CharField(db_column='FullTransferOption', max_length=1, blank=True, null=True)  # Field name made lowercase.
    shipvia = models.ForeignKey('Shippingmethod', models.DO_NOTHING, db_column='ShipVia', blank=True, null=True)  # Field name made lowercase.
    shipinfo = models.CharField(db_column='ShipInfo', max_length=40, blank=True, null=True)  # Field name made lowercase.
    refno2 = models.CharField(db_column='RefNo2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    purchaselocation = models.ForeignKey(Location, models.DO_NOTHING, db_column='PurchaseLocation', blank=True, null=True)  # Field name made lowercase.
    footer1tax = models.DecimalField(db_column='Footer1Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1localtax = models.DecimalField(db_column='Footer1LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2tax = models.DecimalField(db_column='Footer2Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2localtax = models.DecimalField(db_column='Footer2LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3tax = models.DecimalField(db_column='Footer3Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3localtax = models.DecimalField(db_column='Footer3LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    extax = models.DecimalField(db_column='ExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localextax = models.DecimalField(db_column='LocalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    analysisnettotal = models.DecimalField(db_column='AnalysisNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localanalysisnettotal = models.DecimalField(db_column='LocalAnalysisNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.
    totaxcurrencyrate = models.DecimalField(db_column='ToTaxCurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    calcdiscountonunitprice = models.CharField(db_column='CalcDiscountOnUnitPrice', max_length=1, blank=True, null=True)  # Field name made lowercase.
    taxdocno = models.CharField(db_column='TaxDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    totalextax = models.DecimalField(db_column='TotalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxableamt = models.DecimalField(db_column='TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    inclusivetax = models.CharField(db_column='InclusiveTax', max_length=1)  # Field name made lowercase.
    footer1taxrate = models.DecimalField(db_column='Footer1TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    footer2taxrate = models.DecimalField(db_column='Footer2TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    footer3taxrate = models.DecimalField(db_column='Footer3TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    taxdate = models.DateTimeField(db_column='TaxDate', blank=True, null=True)  # Field name made lowercase.
    isroundadj = models.CharField(db_column='IsRoundAdj', max_length=1)  # Field name made lowercase.
    roundadj = models.DecimalField(db_column='RoundAdj', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    finaltotal = models.DecimalField(db_column='FinalTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    selfbilledapprovalno = models.CharField(db_column='SelfBilledApprovalNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    roundingmethod = models.IntegerField(db_column='RoundingMethod')  # Field name made lowercase.
    localtaxableamt = models.DecimalField(db_column='LocalTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytax = models.DecimalField(db_column='TaxCurrencyTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxableamt = models.DecimalField(db_column='TaxCurrencyTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    docdate2 = models.DateTimeField(db_column='DocDate2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'PI'


class Pidtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    focdtlkey = models.BigIntegerField(db_column='FOCDtlKey', blank=True, null=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    indent = models.SmallIntegerField(db_column='Indent', blank=True, null=True)  # Field name made lowercase.
    fontstyle = models.ForeignKey(Fontstyle, models.DO_NOTHING, db_column='FontStyle', blank=True, null=True)  # Field name made lowercase.
    mainitem = models.CharField(db_column='MainItem', max_length=1)  # Field name made lowercase.
    numbering = models.CharField(db_column='Numbering', max_length=6, blank=True, null=True)  # Field name made lowercase.
    itemcode = models.ForeignKey(Itemuom, models.DO_NOTHING, db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    location = models.ForeignKey(Location, models.DO_NOTHING, db_column='Location', blank=True, null=True)  # Field name made lowercase.
    batchno = models.ForeignKey(Itembatch, models.DO_NOTHING, db_column='BatchNo', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    furtherdescription = models.TextField(db_column='FurtherDescription', blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey(Dept, models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    ourpono = models.CharField(db_column='OurPONo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ourpodate = models.DateTimeField(db_column='OurPODate', blank=True, null=True)  # Field name made lowercase.
    posttostockdate = models.DateTimeField(db_column='PostToStockDate', blank=True, null=True)  # Field name made lowercase.
    uom = models.ForeignKey(Itemuom, models.DO_NOTHING, db_column='UOM', blank=True, null=True)  # Field name made lowercase.
    useruom = models.CharField(db_column='UserUOM', max_length=8, blank=True, null=True)  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    smallestqty = models.DecimalField(db_column='SmallestQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    transferedqty = models.DecimalField(db_column='TransferedQty', max_digits=25, decimal_places=8)  # Field name made lowercase.
    focqty = models.DecimalField(db_column='FOCQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    foctransferedqty = models.DecimalField(db_column='FOCTransferedQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    smallestunitprice = models.DecimalField(db_column='SmallestUnitPrice', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    discount = models.CharField(db_column='Discount', max_length=20, blank=True, null=True)  # Field name made lowercase.
    discountamt = models.DecimalField(db_column='DiscountAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='TaxType', blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localsubtotal = models.DecimalField(db_column='LocalSubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    transferable = models.CharField(db_column='Transferable', max_length=1)  # Field name made lowercase.
    printout = models.CharField(db_column='PrintOut', max_length=1)  # Field name made lowercase.
    dtltype = models.CharField(db_column='DtlType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    calcbypercent = models.DecimalField(db_column='CalcByPercent', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    addtosubtotal = models.CharField(db_column='AddToSubTotal', max_length=1)  # Field name made lowercase.
    fromdoctype = models.CharField(db_column='FromDocType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    fromdocno = models.CharField(db_column='FromDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fromdocdtlkey = models.BigIntegerField(db_column='FromDocDtlKey', blank=True, null=True)  # Field name made lowercase.
    fulltransferoption = models.CharField(db_column='FullTransferOption', max_length=1, blank=True, null=True)  # Field name made lowercase.
    foreigncharges = models.DecimalField(db_column='ForeignCharges', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    localcharges = models.DecimalField(db_column='LocalCharges', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    duty = models.DecimalField(db_column='Duty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    forconsignment = models.CharField(db_column='ForConsignment', max_length=1)  # Field name made lowercase.
    accno = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='AccNo', blank=True, null=True)  # Field name made lowercase.
    fulltransferfromdoclist = models.TextField(db_column='FullTransferFromDocList', blank=True, null=True)  # Field name made lowercase.
    serialnolist = models.TextField(db_column='SerialNoList', blank=True, null=True)  # Field name made lowercase.
    estimateddeliverydate = models.CharField(db_column='EstimatedDeliveryDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    packagedockey = models.BigIntegerField(db_column='PackageDocKey', blank=True, null=True)  # Field name made lowercase.
    parentdtlkey = models.BigIntegerField(db_column='ParentDtlKey', blank=True, null=True)  # Field name made lowercase.
    subqty = models.DecimalField(db_column='SubQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    subtotalextax = models.DecimalField(db_column='SubTotalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtax = models.DecimalField(db_column='LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.
    deliverydate = models.DateTimeField(db_column='DeliveryDate', blank=True, null=True)  # Field name made lowercase.
    cnamt = models.DecimalField(db_column='CNAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxpermitno = models.CharField(db_column='TaxPermitNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    taxableamt = models.DecimalField(db_column='TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxadjustment = models.DecimalField(db_column='TaxAdjustment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localsubtotalextax = models.DecimalField(db_column='LocalSubTotalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    extradiscountamt = models.DecimalField(db_column='ExtraDiscountAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxrate = models.DecimalField(db_column='TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    localtaxadjustment = models.DecimalField(db_column='LocalTaxAdjustment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtaxableamt = models.DecimalField(db_column='LocalTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytax = models.DecimalField(db_column='TaxCurrencyTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxableamt = models.DecimalField(db_column='TaxCurrencyTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    salesexemptionno = models.CharField(db_column='SalesExemptionNo', max_length=60, blank=True, null=True)  # Field name made lowercase.
    tariffcode = models.ForeignKey('Tariff', models.DO_NOTHING, db_column='TariffCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'PIDTL'


class Plformat(models.Model):
    autokey = models.AutoField(db_column='AutoKey', primary_key=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    rowtype = models.CharField(db_column='RowType', max_length=1)  # Field name made lowercase.
    acctype = models.ForeignKey(Acctype, models.DO_NOTHING, db_column='AccType', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    creditaspositive = models.CharField(db_column='CreditAsPositive', max_length=1)  # Field name made lowercase.

    class Meta:
 
        db_table = 'PLFormat'


class Po(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', unique=True, max_length=20)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    creditorcode = models.ForeignKey(Branch, models.DO_NOTHING, db_column='CreditorCode', blank=True, null=True)  # Field name made lowercase.
    creditorname = models.CharField(db_column='CreditorName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ref = models.CharField(db_column='Ref', max_length=40, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=80, blank=True, null=True)  # Field name made lowercase.
    displayterm = models.ForeignKey('Terms', models.DO_NOTHING, db_column='DisplayTerm')  # Field name made lowercase.
    purchaseagent = models.ForeignKey('Purchaseagent', models.DO_NOTHING, db_column='PurchaseAgent', blank=True, null=True)  # Field name made lowercase.
    invaddr1 = models.CharField(db_column='InvAddr1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr2 = models.CharField(db_column='InvAddr2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr3 = models.CharField(db_column='InvAddr3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr4 = models.CharField(db_column='InvAddr4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    phone1 = models.CharField(db_column='Phone1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    fax1 = models.CharField(db_column='Fax1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    attention = models.CharField(db_column='Attention', max_length=40, blank=True, null=True)  # Field name made lowercase.
    branchcode = models.ForeignKey(Branch, models.DO_NOTHING, db_column='BranchCode', blank=True, null=True)  # Field name made lowercase.
    deliveraddr1 = models.CharField(db_column='DeliverAddr1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliveraddr2 = models.CharField(db_column='DeliverAddr2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliveraddr3 = models.CharField(db_column='DeliverAddr3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliveraddr4 = models.CharField(db_column='DeliverAddr4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliverphone1 = models.CharField(db_column='DeliverPhone1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    deliverfax1 = models.CharField(db_column='DeliverFax1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    delivercontact = models.CharField(db_column='DeliverContact', max_length=40, blank=True, null=True)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1param = models.DecimalField(db_column='Footer1Param', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1amt = models.DecimalField(db_column='Footer1Amt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1localamt = models.DecimalField(db_column='Footer1LocalAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='Footer1TaxType', blank=True, null=True)  # Field name made lowercase.
    footer2param = models.DecimalField(db_column='Footer2Param', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2amt = models.DecimalField(db_column='Footer2Amt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2localamt = models.DecimalField(db_column='Footer2LocalAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='Footer2TaxType', blank=True, null=True)  # Field name made lowercase.
    footer3param = models.DecimalField(db_column='Footer3Param', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3amt = models.DecimalField(db_column='Footer3Amt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3localamt = models.DecimalField(db_column='Footer3LocalAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='Footer3TaxType', blank=True, null=True)  # Field name made lowercase.
    currencycode = models.ForeignKey(Currency, models.DO_NOTHING, db_column='CurrencyCode')  # Field name made lowercase.
    currencyrate = models.DecimalField(db_column='CurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    nettotal = models.DecimalField(db_column='NetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localnettotal = models.DecimalField(db_column='LocalNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtax = models.DecimalField(db_column='LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    referdepositdockey = models.BigIntegerField(db_column='ReferDepositDocKey', blank=True, null=True)  # Field name made lowercase.
    transferable = models.CharField(db_column='Transferable', max_length=1)  # Field name made lowercase.
    todoctype = models.CharField(db_column='ToDocType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    todockey = models.BigIntegerField(db_column='ToDocKey', blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    remark1 = models.CharField(db_column='Remark1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark2 = models.CharField(db_column='Remark2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark3 = models.CharField(db_column='Remark3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark4 = models.CharField(db_column='Remark4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    printcount = models.SmallIntegerField(db_column='PrintCount')  # Field name made lowercase.
    cancelled = models.CharField(db_column='Cancelled', max_length=1)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    createduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    externallink = models.TextField(db_column='ExternalLink', blank=True, null=True)  # Field name made lowercase.
    refdocno = models.CharField(db_column='RefDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cantransferbyvalue = models.CharField(db_column='CanTransferByValue', max_length=1, blank=True, null=True)  # Field name made lowercase.
    transferedamt = models.DecimalField(db_column='TransferedAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cansync = models.CharField(db_column='CanSync', max_length=1)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    todtlkey = models.BigIntegerField(db_column='ToDtlKey', blank=True, null=True)  # Field name made lowercase.
    fulltransferoption = models.CharField(db_column='FullTransferOption', max_length=1, blank=True, null=True)  # Field name made lowercase.
    shipvia = models.ForeignKey('Shippingmethod', models.DO_NOTHING, db_column='ShipVia', blank=True, null=True)  # Field name made lowercase.
    shipinfo = models.CharField(db_column='ShipInfo', max_length=40, blank=True, null=True)  # Field name made lowercase.
    purchaselocation = models.ForeignKey(Location, models.DO_NOTHING, db_column='PurchaseLocation', blank=True, null=True)  # Field name made lowercase.
    footer1tax = models.DecimalField(db_column='Footer1Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1localtax = models.DecimalField(db_column='Footer1LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2tax = models.DecimalField(db_column='Footer2Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2localtax = models.DecimalField(db_column='Footer2LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3tax = models.DecimalField(db_column='Footer3Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3localtax = models.DecimalField(db_column='Footer3LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    extax = models.DecimalField(db_column='ExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localextax = models.DecimalField(db_column='LocalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    analysisnettotal = models.DecimalField(db_column='AnalysisNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localanalysisnettotal = models.DecimalField(db_column='LocalAnalysisNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.
    totaxcurrencyrate = models.DecimalField(db_column='ToTaxCurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    calcdiscountonunitprice = models.CharField(db_column='CalcDiscountOnUnitPrice', max_length=1, blank=True, null=True)  # Field name made lowercase.
    totalextax = models.DecimalField(db_column='TotalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxableamt = models.DecimalField(db_column='TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    inclusivetax = models.CharField(db_column='InclusiveTax', max_length=1)  # Field name made lowercase.
    footer1taxrate = models.DecimalField(db_column='Footer1TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    footer2taxrate = models.DecimalField(db_column='Footer2TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    footer3taxrate = models.DecimalField(db_column='Footer3TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    roundingmethod = models.IntegerField(db_column='RoundingMethod')  # Field name made lowercase.
    localtaxableamt = models.DecimalField(db_column='LocalTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytax = models.DecimalField(db_column='TaxCurrencyTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxableamt = models.DecimalField(db_column='TaxCurrencyTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    isroundadj = models.CharField(db_column='IsRoundAdj', max_length=1)  # Field name made lowercase.
    roundadj = models.DecimalField(db_column='RoundAdj', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    finaltotal = models.DecimalField(db_column='FinalTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'PO'


class Podtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    indent = models.SmallIntegerField(db_column='Indent', blank=True, null=True)  # Field name made lowercase.
    fontstyle = models.ForeignKey(Fontstyle, models.DO_NOTHING, db_column='FontStyle', blank=True, null=True)  # Field name made lowercase.
    mainitem = models.CharField(db_column='MainItem', max_length=1)  # Field name made lowercase.
    numbering = models.CharField(db_column='Numbering', max_length=6, blank=True, null=True)  # Field name made lowercase.
    itemcode = models.ForeignKey(Itemuom, models.DO_NOTHING, db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    location = models.ForeignKey(Location, models.DO_NOTHING, db_column='Location', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    furtherdescription = models.TextField(db_column='FurtherDescription', blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey(Dept, models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    uom = models.ForeignKey(Itemuom, models.DO_NOTHING, db_column='UOM', blank=True, null=True)  # Field name made lowercase.
    useruom = models.CharField(db_column='UserUOM', max_length=8, blank=True, null=True)  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    smallestqty = models.DecimalField(db_column='SmallestQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    transferedqty = models.DecimalField(db_column='TransferedQty', max_digits=25, decimal_places=8)  # Field name made lowercase.
    focqty = models.DecimalField(db_column='FOCQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    foctransferedqty = models.DecimalField(db_column='FOCTransferedQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    smallestunitprice = models.DecimalField(db_column='SmallestUnitPrice', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    discount = models.CharField(db_column='Discount', max_length=20, blank=True, null=True)  # Field name made lowercase.
    discountamt = models.DecimalField(db_column='DiscountAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='TaxType', blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localsubtotal = models.DecimalField(db_column='LocalSubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    transferable = models.CharField(db_column='Transferable', max_length=1)  # Field name made lowercase.
    printout = models.CharField(db_column='PrintOut', max_length=1)  # Field name made lowercase.
    dtltype = models.CharField(db_column='DtlType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    calcbypercent = models.DecimalField(db_column='CalcByPercent', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    addtosubtotal = models.CharField(db_column='AddToSubTotal', max_length=1)  # Field name made lowercase.
    fromdoctype = models.CharField(db_column='FromDocType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    fromdocno = models.CharField(db_column='FromDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fromdocdtlkey = models.BigIntegerField(db_column='FromDocDtlKey', blank=True, null=True)  # Field name made lowercase.
    fulltransferoption = models.CharField(db_column='FullTransferOption', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fulltransferfromdoclist = models.TextField(db_column='FullTransferFromDocList', blank=True, null=True)  # Field name made lowercase.
    fromsodtlkey = models.BigIntegerField(db_column='FromSODtlKey', blank=True, null=True)  # Field name made lowercase.
    estimateddeliverydate = models.CharField(db_column='EstimatedDeliveryDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fromaodtlkey = models.BigIntegerField(db_column='FromAODtlKey', blank=True, null=True)  # Field name made lowercase.
    packagedockey = models.BigIntegerField(db_column='PackageDocKey', blank=True, null=True)  # Field name made lowercase.
    parentdtlkey = models.BigIntegerField(db_column='ParentDtlKey', blank=True, null=True)  # Field name made lowercase.
    subqty = models.DecimalField(db_column='SubQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    subtotalextax = models.DecimalField(db_column='SubTotalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtax = models.DecimalField(db_column='LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    batchno = models.CharField(db_column='BatchNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.
    fromsodoclist = models.TextField(db_column='FromSODocList', blank=True, null=True)  # Field name made lowercase.
    deliverydate = models.DateTimeField(db_column='DeliveryDate', blank=True, null=True)  # Field name made lowercase.
    taxableamt = models.DecimalField(db_column='TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxadjustment = models.DecimalField(db_column='TaxAdjustment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localsubtotalextax = models.DecimalField(db_column='LocalSubTotalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    extradiscountamt = models.DecimalField(db_column='ExtraDiscountAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxrate = models.DecimalField(db_column='TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    localtaxadjustment = models.DecimalField(db_column='LocalTaxAdjustment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtaxableamt = models.DecimalField(db_column='LocalTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytax = models.DecimalField(db_column='TaxCurrencyTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxableamt = models.DecimalField(db_column='TaxCurrencyTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    salesexemptionno = models.CharField(db_column='SalesExemptionNo', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'PODTL'


class Pr(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', unique=True, max_length=20)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    creditorcode = models.ForeignKey(Branch, models.DO_NOTHING, db_column='CreditorCode', blank=True, null=True)  # Field name made lowercase.
    creditorname = models.CharField(db_column='CreditorName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ref = models.CharField(db_column='Ref', max_length=40, blank=True, null=True)  # Field name made lowercase.
    suppliercnno = models.CharField(db_column='SupplierCNNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=80, blank=True, null=True)  # Field name made lowercase.
    displayterm = models.ForeignKey('Terms', models.DO_NOTHING, db_column='DisplayTerm')  # Field name made lowercase.
    purchaseagent = models.ForeignKey('Purchaseagent', models.DO_NOTHING, db_column='PurchaseAgent', blank=True, null=True)  # Field name made lowercase.
    invaddr1 = models.CharField(db_column='InvAddr1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr2 = models.CharField(db_column='InvAddr2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr3 = models.CharField(db_column='InvAddr3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr4 = models.CharField(db_column='InvAddr4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    phone1 = models.CharField(db_column='Phone1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    fax1 = models.CharField(db_column='Fax1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    attention = models.CharField(db_column='Attention', max_length=40, blank=True, null=True)  # Field name made lowercase.
    branchcode = models.ForeignKey(Branch, models.DO_NOTHING, db_column='BranchCode', blank=True, null=True)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1param = models.DecimalField(db_column='Footer1Param', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1amt = models.DecimalField(db_column='Footer1Amt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1localamt = models.DecimalField(db_column='Footer1LocalAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='Footer1TaxType', blank=True, null=True)  # Field name made lowercase.
    footer2param = models.DecimalField(db_column='Footer2Param', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2amt = models.DecimalField(db_column='Footer2Amt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2localamt = models.DecimalField(db_column='Footer2LocalAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='Footer2TaxType', blank=True, null=True)  # Field name made lowercase.
    footer3param = models.DecimalField(db_column='Footer3Param', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3amt = models.DecimalField(db_column='Footer3Amt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3localamt = models.DecimalField(db_column='Footer3LocalAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='Footer3TaxType', blank=True, null=True)  # Field name made lowercase.
    currencycode = models.ForeignKey(Currency, models.DO_NOTHING, db_column='CurrencyCode')  # Field name made lowercase.
    currencyrate = models.DecimalField(db_column='CurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    nettotal = models.DecimalField(db_column='NetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localnettotal = models.DecimalField(db_column='LocalNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtax = models.DecimalField(db_column='LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    posttostock = models.CharField(db_column='PostToStock', max_length=1)  # Field name made lowercase.
    posttogl = models.CharField(db_column='PostToGL', max_length=1)  # Field name made lowercase.
    referdockey = models.BigIntegerField(db_column='ReferDocKey', blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    remark1 = models.CharField(db_column='Remark1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark2 = models.CharField(db_column='Remark2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark3 = models.CharField(db_column='Remark3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark4 = models.CharField(db_column='Remark4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    printcount = models.SmallIntegerField(db_column='PrintCount')  # Field name made lowercase.
    cancelled = models.CharField(db_column='Cancelled', max_length=1)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    createduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    externallink = models.TextField(db_column='ExternalLink', blank=True, null=True)  # Field name made lowercase.
    refdocno = models.CharField(db_column='RefDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cansync = models.CharField(db_column='CanSync', max_length=1)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    refno2 = models.CharField(db_column='RefNo2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    purchaselocation = models.ForeignKey(Location, models.DO_NOTHING, db_column='PurchaseLocation', blank=True, null=True)  # Field name made lowercase.
    footer1tax = models.DecimalField(db_column='Footer1Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1localtax = models.DecimalField(db_column='Footer1LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2tax = models.DecimalField(db_column='Footer2Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2localtax = models.DecimalField(db_column='Footer2LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3tax = models.DecimalField(db_column='Footer3Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3localtax = models.DecimalField(db_column='Footer3LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    extax = models.DecimalField(db_column='ExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localextax = models.DecimalField(db_column='LocalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    analysisnettotal = models.DecimalField(db_column='AnalysisNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localanalysisnettotal = models.DecimalField(db_column='LocalAnalysisNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.
    totaxcurrencyrate = models.DecimalField(db_column='ToTaxCurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    calcdiscountonunitprice = models.CharField(db_column='CalcDiscountOnUnitPrice', max_length=1, blank=True, null=True)  # Field name made lowercase.
    taxdocno = models.CharField(db_column='TaxDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    totalextax = models.DecimalField(db_column='TotalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxableamt = models.DecimalField(db_column='TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    supplierinvoiceno = models.CharField(db_column='SupplierInvoiceNo', max_length=40, blank=True, null=True)  # Field name made lowercase.
    reason = models.CharField(db_column='Reason', max_length=80, blank=True, null=True)  # Field name made lowercase.
    inclusivetax = models.CharField(db_column='InclusiveTax', max_length=1)  # Field name made lowercase.
    footer1taxrate = models.DecimalField(db_column='Footer1TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    footer2taxrate = models.DecimalField(db_column='Footer2TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    footer3taxrate = models.DecimalField(db_column='Footer3TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    taxdate = models.DateTimeField(db_column='TaxDate', blank=True, null=True)  # Field name made lowercase.
    isroundadj = models.CharField(db_column='IsRoundAdj', max_length=1)  # Field name made lowercase.
    roundadj = models.DecimalField(db_column='RoundAdj', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    finaltotal = models.DecimalField(db_column='FinalTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    roundingmethod = models.IntegerField(db_column='RoundingMethod')  # Field name made lowercase.
    localtaxableamt = models.DecimalField(db_column='LocalTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytax = models.DecimalField(db_column='TaxCurrencyTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxableamt = models.DecimalField(db_column='TaxCurrencyTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    docdate2 = models.DateTimeField(db_column='DocDate2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'PR'


class Prdtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    focdtlkey = models.BigIntegerField(db_column='FOCDtlKey', blank=True, null=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    indent = models.SmallIntegerField(db_column='Indent', blank=True, null=True)  # Field name made lowercase.
    fontstyle = models.ForeignKey(Fontstyle, models.DO_NOTHING, db_column='FontStyle', blank=True, null=True)  # Field name made lowercase.
    mainitem = models.CharField(db_column='MainItem', max_length=1)  # Field name made lowercase.
    numbering = models.CharField(db_column='Numbering', max_length=6, blank=True, null=True)  # Field name made lowercase.
    itemcode = models.ForeignKey(Itemuom, models.DO_NOTHING, db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    location = models.ForeignKey(Location, models.DO_NOTHING, db_column='Location', blank=True, null=True)  # Field name made lowercase.
    batchno = models.ForeignKey(Itembatch, models.DO_NOTHING, db_column='BatchNo', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    furtherdescription = models.TextField(db_column='FurtherDescription', blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey(Dept, models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    yourdono = models.CharField(db_column='YourDONo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    yourdodate = models.DateTimeField(db_column='YourDODate', blank=True, null=True)  # Field name made lowercase.
    ourpono = models.CharField(db_column='OurPONo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ourpodate = models.DateTimeField(db_column='OurPODate', blank=True, null=True)  # Field name made lowercase.
    posttostockdate = models.DateTimeField(db_column='PostToStockDate', blank=True, null=True)  # Field name made lowercase.
    uom = models.ForeignKey(Itemuom, models.DO_NOTHING, db_column='UOM', blank=True, null=True)  # Field name made lowercase.
    useruom = models.CharField(db_column='UserUOM', max_length=8, blank=True, null=True)  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    smallestqty = models.DecimalField(db_column='SmallestQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    focqty = models.DecimalField(db_column='FOCQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    smallestunitprice = models.DecimalField(db_column='SmallestUnitPrice', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    discount = models.CharField(db_column='Discount', max_length=20, blank=True, null=True)  # Field name made lowercase.
    discountamt = models.DecimalField(db_column='DiscountAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='TaxType', blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localsubtotal = models.DecimalField(db_column='LocalSubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    printout = models.CharField(db_column='PrintOut', max_length=1)  # Field name made lowercase.
    dtltype = models.CharField(db_column='DtlType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    calcbypercent = models.DecimalField(db_column='CalcByPercent', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    addtosubtotal = models.CharField(db_column='AddToSubTotal', max_length=1)  # Field name made lowercase.
    fromdoctype = models.CharField(db_column='FromDocType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    fromdocno = models.CharField(db_column='FromDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fromdocdtlkey = models.BigIntegerField(db_column='FromDocDtlKey', blank=True, null=True)  # Field name made lowercase.
    fulltransferoption = models.CharField(db_column='FullTransferOption', max_length=1, blank=True, null=True)  # Field name made lowercase.
    accno = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='AccNo', blank=True, null=True)  # Field name made lowercase.
    fulltransferfromdoclist = models.TextField(db_column='FullTransferFromDocList', blank=True, null=True)  # Field name made lowercase.
    serialnolist = models.TextField(db_column='SerialNoList', blank=True, null=True)  # Field name made lowercase.
    packagedockey = models.BigIntegerField(db_column='PackageDocKey', blank=True, null=True)  # Field name made lowercase.
    parentdtlkey = models.BigIntegerField(db_column='ParentDtlKey', blank=True, null=True)  # Field name made lowercase.
    subqty = models.DecimalField(db_column='SubQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    subtotalextax = models.DecimalField(db_column='SubTotalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtax = models.DecimalField(db_column='LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.
    goodsreturn = models.CharField(db_column='GoodsReturn', max_length=1, blank=True, null=True)  # Field name made lowercase.
    taxpermitno = models.CharField(db_column='TaxPermitNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    taxableamt = models.DecimalField(db_column='TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxadjustment = models.DecimalField(db_column='TaxAdjustment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localsubtotalextax = models.DecimalField(db_column='LocalSubTotalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    extradiscountamt = models.DecimalField(db_column='ExtraDiscountAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxrate = models.DecimalField(db_column='TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    localtaxadjustment = models.DecimalField(db_column='LocalTaxAdjustment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtaxableamt = models.DecimalField(db_column='LocalTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytax = models.DecimalField(db_column='TaxCurrencyTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxableamt = models.DecimalField(db_column='TaxCurrencyTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    supplypurchase = models.CharField(db_column='SupplyPurchase', max_length=1, blank=True, null=True)  # Field name made lowercase.
    salesexemptionno = models.CharField(db_column='SalesExemptionNo', max_length=60, blank=True, null=True)  # Field name made lowercase.
    tariffcode = models.ForeignKey('Tariff', models.DO_NOTHING, db_column='TariffCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'PRDTL'


class Prprocessing(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    fromdtlkey = models.BigIntegerField(db_column='FromDtlKey')  # Field name made lowercase.
    fromdockey = models.BigIntegerField(db_column='FromDocKey')  # Field name made lowercase.
    itemcode = models.ForeignKey(Itemuom, models.DO_NOTHING, db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sodescription = models.CharField(db_column='SODescription', max_length=100, blank=True, null=True)  # Field name made lowercase.
    furtherdescription = models.TextField(db_column='FurtherDescription', blank=True, null=True)  # Field name made lowercase.
    estimateddeliverydate = models.CharField(db_column='EstimatedDeliveryDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    location = models.ForeignKey(Location, models.DO_NOTHING, db_column='Location', blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey(Dept, models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    creditorcode = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='CreditorCode', blank=True, null=True)  # Field name made lowercase.
    requestqty = models.DecimalField(db_column='RequestQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    requestuom = models.ForeignKey(Itemuom, models.DO_NOTHING, db_column='RequestUOM', blank=True, null=True)  # Field name made lowercase.
    isallowopedit = models.CharField(db_column='IsAllowOPEdit', max_length=1)  # Field name made lowercase.
    createduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    fromdoctype = models.CharField(db_column='FromDocType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
    deliverydate = models.DateTimeField(db_column='DeliveryDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'PRProcessing'


class Prprocessingpo(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    prpkey = models.BigIntegerField(db_column='PRPKey')  # Field name made lowercase.
    fromdtlkey = models.BigIntegerField(db_column='FromDtlKey')  # Field name made lowercase.
    fromdockey = models.BigIntegerField(db_column='FromDocKey')  # Field name made lowercase.
    refdockey = models.BigIntegerField(db_column='RefDocKey', blank=True, null=True)  # Field name made lowercase.
    refdocno = models.CharField(db_column='RefDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    refdoctype = models.CharField(db_column='RefDocType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    refdtlkey = models.BigIntegerField(db_column='RefDtlKey', blank=True, null=True)  # Field name made lowercase.
    creditorcode = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='CreditorCode', blank=True, null=True)  # Field name made lowercase.
    itemcode = models.ForeignKey(Itemuom, models.DO_NOTHING, db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    orderqty = models.DecimalField(db_column='OrderQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    orderuom = models.ForeignKey(Itemuom, models.DO_NOTHING, db_column='OrderUOM', blank=True, null=True)  # Field name made lowercase.
    orderrate = models.DecimalField(db_column='OrderRate', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    kiv = models.CharField(db_column='KIV', max_length=1)  # Field name made lowercase.
    createduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    fromdoctype = models.CharField(db_column='FromDocType', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'PRProcessingPO'


class Pwp(models.Model):
    pwpkey = models.BigIntegerField(db_column='PWPKey')  # Field name made lowercase.
    fromdatetime = models.DateTimeField(db_column='FromDateTime', blank=True, null=True)  # Field name made lowercase.
    todatetime = models.DateTimeField(db_column='ToDateTime', blank=True, null=True)  # Field name made lowercase.
    itemcode = models.ForeignKey(Itemuom, models.DO_NOTHING, db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    uom = models.ForeignKey(Itemuom, models.DO_NOTHING, db_column='UOM', blank=True, null=True)  # Field name made lowercase.
    purchasedqty = models.DecimalField(db_column='PurchasedQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    purchasedamount = models.DecimalField(db_column='PurchasedAmount', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    isactive = models.CharField(db_column='IsActive', max_length=1)  # Field name made lowercase.

    class Meta:
 
        db_table = 'PWP'


class Pwpdtl(models.Model):
    pwpdtlkey = models.BigIntegerField(db_column='PWPDtlKey')  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    pwpkey = models.BigIntegerField(db_column='PWPKey')  # Field name made lowercase.
    itemcode = models.ForeignKey(Itemuom, models.DO_NOTHING, db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    uom = models.ForeignKey(Itemuom, models.DO_NOTHING, db_column='UOM', blank=True, null=True)  # Field name made lowercase.
    isfoc = models.CharField(db_column='IsFOC', max_length=1)  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=25, decimal_places=8)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    discount = models.CharField(db_column='Discount', max_length=12, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'PWPDTL'


class Package(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    packagecode = models.CharField(db_column='PackageCode', unique=True, max_length=30)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=80, blank=True, null=True)  # Field name made lowercase.
    expirydate = models.DateTimeField(db_column='ExpiryDate', blank=True, null=True)  # Field name made lowercase.
    openingqty = models.DecimalField(db_column='OpeningQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    limitedqty = models.DecimalField(db_column='LimitedQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    soldqty = models.DecimalField(db_column='SoldQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    nettotal = models.DecimalField(db_column='NetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    isactive = models.CharField(db_column='IsActive', max_length=1, blank=True, null=True)  # Field name made lowercase.
    furtherdescription = models.TextField(db_column='FurtherDescription', blank=True, null=True)  # Field name made lowercase.
    useruom = models.CharField(db_column='UserUOM', max_length=8, blank=True, null=True)  # Field name made lowercase.
    purchasenettotal = models.DecimalField(db_column='PurchaseNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    barcode = models.CharField(db_column='BarCode', max_length=30, blank=True, null=True)  # Field name made lowercase.
    purchasedqty = models.DecimalField(db_column='PurchasedQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'Package'


class Packagedtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    dockey = models.ForeignKey(Package, models.DO_NOTHING, db_column='DocKey')  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    itemcode = models.ForeignKey(Itemuom, models.DO_NOTHING, db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    furtherdescription = models.TextField(db_column='FurtherDescription', blank=True, null=True)  # Field name made lowercase.
    uom = models.ForeignKey(Itemuom, models.DO_NOTHING, db_column='UOM', blank=True, null=True)  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SubTotal', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    printout = models.CharField(db_column='PrintOut', max_length=1)  # Field name made lowercase.
    purchaseprice = models.DecimalField(db_column='PurchasePrice', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    purchasesubtotal = models.DecimalField(db_column='PurchaseSubTotal', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='TaxType', blank=True, null=True)  # Field name made lowercase.
    purchasetaxtype = models.CharField(db_column='PurchaseTaxType', max_length=14, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'PackageDTL'


class Paymentmethod(models.Model):
    paymentmethod = models.CharField(db_column='PaymentMethod', primary_key=True, max_length=20)  # Field name made lowercase.
    bankaccount = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='BankAccount')  # Field name made lowercase.
    bankchargeaccount = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='BankChargeAccount', blank=True, null=True)  # Field name made lowercase.
    bankchargepercent = models.DecimalField(db_column='BankChargePercent', max_digits=18, decimal_places=6)  # Field name made lowercase.
    mergebankchargetrans = models.CharField(db_column='MergeBankChargeTrans', max_length=1)  # Field name made lowercase.
    specialacctype = models.CharField(db_column='SpecialAccType', max_length=3)  # Field name made lowercase.
    journaltype = models.ForeignKey(Journal, models.DO_NOTHING, db_column='JournalType')  # Field name made lowercase.
    acceptchequeno = models.CharField(db_column='AcceptChequeNo', max_length=1)  # Field name made lowercase.
    paymentby = models.CharField(db_column='PaymentBy', max_length=20, blank=True, null=True)  # Field name made lowercase.
    odlimit = models.DecimalField(db_column='ODLimit', max_digits=19, decimal_places=2)  # Field name made lowercase.
    paymentformatname = models.ForeignKey(Docnoformat, models.DO_NOTHING, db_column='PaymentFormatName')  # Field name made lowercase.
    receiptformatname = models.ForeignKey(Docnoformat, models.DO_NOTHING, db_column='ReceiptFormatName')  # Field name made lowercase.
    nextchequeno = models.CharField(db_column='NextChequeNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    isactive = models.CharField(db_column='IsActive', max_length=1)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    paymenttype = models.CharField(db_column='PaymentType', max_length=12, blank=True, null=True)  # Field name made lowercase.
    minbankcharge = models.DecimalField(db_column='MinBankCharge', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    bankchargetaxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='BankChargeTaxType', blank=True, null=True)  # Field name made lowercase.
    bankchargetaxbrno = models.CharField(db_column='BankChargeTaxBRNo', max_length=25, blank=True, null=True)  # Field name made lowercase.
    bankchargetaxbname = models.CharField(db_column='BankChargeTaxBName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bankchargetaxregisterno = models.CharField(db_column='BankChargeTaxRegisterNo', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'PaymentMethod'


class Periodlock(models.Model):
    periodno = models.IntegerField(db_column='PeriodNo', primary_key=True)  # Field name made lowercase.
    lock = models.CharField(db_column='Lock', max_length=1)  # Field name made lowercase.

    class Meta:
 
        db_table = 'PeriodLock'


class Periodlockexception(models.Model):
    periodno = models.IntegerField(db_column='PeriodNo', primary_key=True)  # Field name made lowercase.
    functionname = models.CharField(db_column='FunctionName', max_length=40)  # Field name made lowercase.
    userid = models.CharField(db_column='UserID', max_length=10)  # Field name made lowercase.

    class Meta:
 
        db_table = 'PeriodLockException'
        unique_together = (('periodno', 'functionname', 'userid'),)


class Plugin(models.Model):
    guid = models.CharField(db_column='Guid', primary_key=True, max_length=36)  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=20)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    whatsnew = models.TextField(db_column='WhatsNew', blank=True, null=True)  # Field name made lowercase.
    extractfiles = models.CharField(db_column='ExtractFiles', max_length=1)  # Field name made lowercase.
    assemblyfile = models.TextField(db_column='AssemblyFile', blank=True, null=True)  # Field name made lowercase.
    signature = models.CharField(db_column='Signature', max_length=88, blank=True, null=True)  # Field name made lowercase.
    minimumaccountingversion = models.CharField(db_column='MinimumAccountingVersion', max_length=20, blank=True, null=True)  # Field name made lowercase.
    scriptlanguage = models.CharField(db_column='ScriptLanguage', max_length=2, blank=True, null=True)  # Field name made lowercase.
    installationscript = models.TextField(db_column='InstallationScript', blank=True, null=True)  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp', blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.TextField(db_column='Manufacturer', blank=True, null=True)  # Field name made lowercase.
    manufacturerurl = models.TextField(db_column='ManufacturerUrl', blank=True, null=True)  # Field name made lowercase.
    copyright = models.TextField(db_column='Copyright', blank=True, null=True)  # Field name made lowercase.
    salesphone = models.CharField(db_column='SalesPhone', max_length=25, blank=True, null=True)  # Field name made lowercase.
    supportphone = models.CharField(db_column='SupportPhone', max_length=25, blank=True, null=True)  # Field name made lowercase.
    allowsync = models.CharField(db_column='AllowSync', max_length=1, blank=True, null=True)  # Field name made lowercase.
    supportlicensekey = models.CharField(db_column='SupportLicenseKey', max_length=1, blank=True, null=True)  # Field name made lowercase.
    licensekey = models.TextField(db_column='LicenseKey', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'PlugIn'


class Pluginfiles(models.Model):
    guid = models.OneToOneField(Plugin, models.DO_NOTHING, db_column='Guid', primary_key=True)  # Field name made lowercase.
    filename = models.CharField(db_column='FileName', max_length=260)  # Field name made lowercase.
    creationtimeutc = models.DateTimeField(db_column='CreationTimeUtc', blank=True, null=True)  # Field name made lowercase.
    lastaccesstimeutc = models.DateTimeField(db_column='LastAccessTimeUtc', blank=True, null=True)  # Field name made lowercase.
    lastwritetimeutc = models.DateTimeField(db_column='LastWriteTimeUtc', blank=True, null=True)  # Field name made lowercase.
    executeafterextracted = models.CharField(db_column='ExecuteAfterExtracted', max_length=1)  # Field name made lowercase.
    msiguid = models.CharField(db_column='MsiGuid', max_length=36, blank=True, null=True)  # Field name made lowercase.
    fileimage = models.BinaryField(db_column='FileImage', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'PlugInFiles'
        unique_together = (('guid', 'filename'),)


class Pocketsyncprofile(models.Model):
    profilekey = models.BigIntegerField(db_column='ProfileKey', primary_key=True)  # Field name made lowercase.
    profilename = models.CharField(db_column='ProfileName', unique=True, max_length=60)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=80, blank=True, null=True)  # Field name made lowercase.
    expireddays = models.SmallIntegerField(db_column='ExpiredDays')  # Field name made lowercase.
    criteria = models.BinaryField(db_column='Criteria', blank=True, null=True)  # Field name made lowercase.
    foldername = models.CharField(db_column='FolderName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    lastdate = models.DateTimeField(db_column='LastDate', blank=True, null=True)  # Field name made lowercase.
    lastsynchronized = models.DateTimeField(db_column='LastSynchronized', blank=True, null=True)  # Field name made lowercase.
    syncid = models.CharField(db_column='SyncID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    deviceid = models.CharField(db_column='DeviceID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified', blank=True, null=True)  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastModifiedUserID', blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'PocketSyncProfile'


class Pointtrans(models.Model):
    pointtranskey = models.BigIntegerField(db_column='PointTransKey', primary_key=True)  # Field name made lowercase.
    sourcetype = models.CharField(db_column='SourceType', max_length=2)  # Field name made lowercase.
    memberno = models.ForeignKey(Member, models.DO_NOTHING, db_column='MemberNo')  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', max_length=20)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    points = models.DecimalField(db_column='Points', max_digits=19, decimal_places=2)  # Field name made lowercase.
    sourceguid = models.CharField(db_column='SourceGuid', max_length=36)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.
    pointtype = models.CharField(db_column='PointType', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'PointTrans'


class Pos(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', unique=True, max_length=20)  # Field name made lowercase.
    tableid = models.IntegerField(db_column='TableID', blank=True, null=True)  # Field name made lowercase.
    debtorcode = models.ForeignKey(Debtor, models.DO_NOTHING, db_column='DebtorCode', blank=True, null=True)  # Field name made lowercase.
    guests = models.IntegerField(db_column='Guests')  # Field name made lowercase.
    totalqty = models.DecimalField(db_column='TotalQty', max_digits=25, decimal_places=8)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=19, decimal_places=2)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2)  # Field name made lowercase.
    tax2 = models.DecimalField(db_column='Tax2', max_digits=19, decimal_places=2)  # Field name made lowercase.
    nettotal = models.DecimalField(db_column='NetTotal', max_digits=19, decimal_places=2)  # Field name made lowercase.
    localtotalcost = models.DecimalField(db_column='LocalTotalCost', max_digits=19, decimal_places=2)  # Field name made lowercase.
    cashpayment = models.DecimalField(db_column='CashPayment', max_digits=19, decimal_places=2)  # Field name made lowercase.
    ccpayment = models.DecimalField(db_column='CCPayment', max_digits=19, decimal_places=2)  # Field name made lowercase.
    cccharges = models.DecimalField(db_column='CCCharges', max_digits=19, decimal_places=2)  # Field name made lowercase.
    cctype = models.ForeignKey(Creditcard, models.DO_NOTHING, db_column='CCType', blank=True, null=True)  # Field name made lowercase.
    ccnumber = models.CharField(db_column='CCNumber', max_length=25, blank=True, null=True)  # Field name made lowercase.
    ccexpirydate = models.DateTimeField(db_column='CCExpiryDate', blank=True, null=True)  # Field name made lowercase.
    ccapprovalcode = models.CharField(db_column='CCApprovalCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dcpayment = models.DecimalField(db_column='DCPayment', max_digits=19, decimal_places=2)  # Field name made lowercase.
    chequepayment = models.DecimalField(db_column='ChequePayment', max_digits=19, decimal_places=2)  # Field name made lowercase.
    chequeno = models.CharField(db_column='ChequeNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    voucherpayment = models.DecimalField(db_column='VoucherPayment', max_digits=19, decimal_places=2)  # Field name made lowercase.
    memberno = models.ForeignKey(Member, models.DO_NOTHING, db_column='MemberNo', blank=True, null=True)  # Field name made lowercase.
    userid = models.CharField(db_column='UserID', max_length=10)  # Field name made lowercase.
    terminal = models.CharField(db_column='Terminal', max_length=8)  # Field name made lowercase.
    outlet = models.CharField(db_column='Outlet', max_length=8, blank=True, null=True)  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    paidtime = models.DateTimeField(db_column='PaidTime', blank=True, null=True)  # Field name made lowercase.
    sync = models.CharField(db_column='Sync', max_length=1)  # Field name made lowercase.
    posted = models.CharField(db_column='Posted', max_length=1)  # Field name made lowercase.
    cancelled = models.CharField(db_column='Cancelled', max_length=1)  # Field name made lowercase.
    cardtype = models.CharField(db_column='CardType', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'Pos'


class Posdtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    itemcode = models.ForeignKey(Itemuom, models.DO_NOTHING, db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    uom = models.ForeignKey(Itemuom, models.DO_NOTHING, db_column='UOM', blank=True, null=True)  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=25, decimal_places=8)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=25, decimal_places=8)  # Field name made lowercase.
    discount = models.DecimalField(db_column='Discount', max_digits=19, decimal_places=2)  # Field name made lowercase.
    discountpercent = models.DecimalField(db_column='DiscountPercent', max_digits=18, decimal_places=6)  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SubTotal', max_digits=19, decimal_places=2)  # Field name made lowercase.
    taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='TaxType', blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2)  # Field name made lowercase.
    localtotalcost = models.DecimalField(db_column='LocalTotalCost', max_digits=19, decimal_places=2)  # Field name made lowercase.
    bonuspoint = models.IntegerField(db_column='BonusPoint')  # Field name made lowercase.

    class Meta:
 
        db_table = 'PosDtl'


class Posoption(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=25)  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'PosOption'


class Posuser(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=10)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=112, blank=True, null=True)  # Field name made lowercase.
    outlet = models.ForeignKey(Location, models.DO_NOTHING, db_column='Outlet', blank=True, null=True)  # Field name made lowercase.
    initialcash = models.DecimalField(db_column='InitialCash', max_digits=19, decimal_places=2)  # Field name made lowercase.
    supervisor = models.CharField(db_column='Supervisor', max_length=1)  # Field name made lowercase.
    isactive = models.CharField(db_column='IsActive', max_length=1)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.

    class Meta:
 
        db_table = 'PosUser'


class Postingaccountgroup(models.Model):
    accountgroup = models.CharField(db_column='AccountGroup', primary_key=True, max_length=12)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=40, blank=True, null=True)  # Field name made lowercase.
    desc2 = models.CharField(db_column='Desc2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    salescode = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='SalesCode', blank=True, null=True)  # Field name made lowercase.
    cashsalescode = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='CashSalesCode', blank=True, null=True)  # Field name made lowercase.
    salesreturncode = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='SalesReturnCode', blank=True, null=True)  # Field name made lowercase.
    salesdiscountcode = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='SalesDiscountCode', blank=True, null=True)  # Field name made lowercase.
    purchasediscountcode = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='PurchaseDiscountCode', blank=True, null=True)  # Field name made lowercase.
    purchasecode = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='PurchaseCode', blank=True, null=True)  # Field name made lowercase.
    purchasereturncode = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='PurchaseReturnCode', blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.

    class Meta:
 
        db_table = 'PostingAccountGroup'


class Pricebookmatrix(models.Model):
    matrixkey = models.BigIntegerField(db_column='MatrixKey', primary_key=True)  # Field name made lowercase.
    matrixname = models.CharField(db_column='MatrixName', max_length=20)  # Field name made lowercase.
    fromdate = models.DateTimeField(db_column='FromDate', blank=True, null=True)  # Field name made lowercase.
    todate = models.DateTimeField(db_column='ToDate', blank=True, null=True)  # Field name made lowercase.
    y = models.CharField(db_column='Y', max_length=20)  # Field name made lowercase.
    ycriteria = models.TextField(db_column='YCriteria', blank=True, null=True)  # Field name made lowercase.
    x = models.CharField(db_column='X', max_length=20, blank=True, null=True)  # Field name made lowercase.
    xcriteria = models.TextField(db_column='XCriteria', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.CharField(db_column='UnitPrice', max_length=1, blank=True, null=True)  # Field name made lowercase.
    discount = models.CharField(db_column='Discount', max_length=1, blank=True, null=True)  # Field name made lowercase.
    geqty = models.DecimalField(db_column='GEQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    isactive = models.CharField(db_column='IsActive', max_length=1, blank=True, null=True)  # Field name made lowercase.
    priority = models.SmallIntegerField(db_column='Priority', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'PriceBookMatrix'


class Pricebookrule(models.Model):
    ruleno = models.BigAutoField(db_column='RuleNo', primary_key=True)  # Field name made lowercase.
    fromdate = models.DateTimeField(db_column='FromDate', blank=True, null=True)  # Field name made lowercase.
    todate = models.DateTimeField(db_column='ToDate', blank=True, null=True)  # Field name made lowercase.
    fromitemtype = models.ForeignKey(Itemtype, models.DO_NOTHING, db_column='FromItemType', blank=True, null=True)  # Field name made lowercase.
    toitemtype = models.ForeignKey(Itemtype, models.DO_NOTHING, db_column='ToItemType', blank=True, null=True)  # Field name made lowercase.
    fromitemgroup = models.ForeignKey(Itemgroup, models.DO_NOTHING, db_column='FromItemGroup', blank=True, null=True)  # Field name made lowercase.
    toitemgroup = models.ForeignKey(Itemgroup, models.DO_NOTHING, db_column='ToItemGroup', blank=True, null=True)  # Field name made lowercase.
    fromitemcode = models.ForeignKey(Item, models.DO_NOTHING, db_column='FromItemCode', blank=True, null=True)  # Field name made lowercase.
    toitemcode = models.ForeignKey(Item, models.DO_NOTHING, db_column='ToItemCode', blank=True, null=True)  # Field name made lowercase.
    uom = models.CharField(db_column='UOM', max_length=8, blank=True, null=True)  # Field name made lowercase.
    fromlocation = models.ForeignKey(Location, models.DO_NOTHING, db_column='FromLocation', blank=True, null=True)  # Field name made lowercase.
    tolocation = models.ForeignKey(Location, models.DO_NOTHING, db_column='ToLocation', blank=True, null=True)  # Field name made lowercase.
    fromprojno = models.ForeignKey('Project', models.DO_NOTHING, db_column='FromProjNo', blank=True, null=True)  # Field name made lowercase.
    toprojno = models.ForeignKey('Project', models.DO_NOTHING, db_column='ToProjNo', blank=True, null=True)  # Field name made lowercase.
    fromdeptno = models.ForeignKey(Dept, models.DO_NOTHING, db_column='FromDeptNo', blank=True, null=True)  # Field name made lowercase.
    todeptno = models.ForeignKey(Dept, models.DO_NOTHING, db_column='ToDeptNo', blank=True, null=True)  # Field name made lowercase.
    fromsalesagent = models.ForeignKey('Salesagent', models.DO_NOTHING, db_column='FromSalesAgent', blank=True, null=True)  # Field name made lowercase.
    tosalesagent = models.ForeignKey('Salesagent', models.DO_NOTHING, db_column='ToSalesAgent', blank=True, null=True)  # Field name made lowercase.
    frompricecategory = models.ForeignKey('Pricecategory', models.DO_NOTHING, db_column='FromPriceCategory', blank=True, null=True)  # Field name made lowercase.
    topricecategory = models.ForeignKey('Pricecategory', models.DO_NOTHING, db_column='ToPriceCategory', blank=True, null=True)  # Field name made lowercase.
    fromdebtortype = models.ForeignKey(Debtortype, models.DO_NOTHING, db_column='FromDebtorType', blank=True, null=True)  # Field name made lowercase.
    todebtortype = models.ForeignKey(Debtortype, models.DO_NOTHING, db_column='ToDebtorType', blank=True, null=True)  # Field name made lowercase.
    fromareacode = models.ForeignKey(Area, models.DO_NOTHING, db_column='FromAreaCode', blank=True, null=True)  # Field name made lowercase.
    toareacode = models.ForeignKey(Area, models.DO_NOTHING, db_column='ToAreaCode', blank=True, null=True)  # Field name made lowercase.
    fromdebtorcode = models.ForeignKey(Debtor, models.DO_NOTHING, db_column='FromDebtorCode', blank=True, null=True)  # Field name made lowercase.
    todebtorcode = models.ForeignKey(Debtor, models.DO_NOTHING, db_column='ToDebtorCode', blank=True, null=True)  # Field name made lowercase.
    currencycode = models.ForeignKey(Currency, models.DO_NOTHING, db_column='CurrencyCode', blank=True, null=True)  # Field name made lowercase.
    displayterm = models.ForeignKey('Terms', models.DO_NOTHING, db_column='DisplayTerm', blank=True, null=True)  # Field name made lowercase.
    geqty = models.DecimalField(db_column='GEQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    discount = models.CharField(db_column='Discount', max_length=20, blank=True, null=True)  # Field name made lowercase.
    isactive = models.CharField(db_column='IsActive', max_length=1, blank=True, null=True)  # Field name made lowercase.
    batchno = models.CharField(db_column='BatchNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    matrixkey = models.ForeignKey(Pricebookmatrix, models.DO_NOTHING, db_column='MatrixKey', blank=True, null=True)  # Field name made lowercase.
    priority = models.SmallIntegerField(db_column='Priority', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'PriceBookRule'


class Pricecategory(models.Model):
    pricecategory = models.CharField(db_column='PriceCategory', primary_key=True, max_length=12)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=40, blank=True, null=True)  # Field name made lowercase.
    discountpercent = models.DecimalField(db_column='DiscountPercent', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    detaildiscount = models.CharField(db_column='DetailDiscount', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    markupratio = models.DecimalField(db_column='MarkupRatio', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'PriceCategory'


class Profile(models.Model):
    companyname = models.CharField(db_column='CompanyName', primary_key=True, max_length=80)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=12, blank=True, null=True)  # Field name made lowercase.
    registerno = models.CharField(db_column='RegisterNo', max_length=25, blank=True, null=True)  # Field name made lowercase.
    address1 = models.CharField(db_column='Address1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    address2 = models.CharField(db_column='Address2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    address3 = models.CharField(db_column='Address3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    address4 = models.CharField(db_column='Address4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    postcode = models.CharField(db_column='PostCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    deliveraddr1 = models.CharField(db_column='DeliverAddr1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliveraddr2 = models.CharField(db_column='DeliverAddr2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliveraddr3 = models.CharField(db_column='DeliverAddr3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliveraddr4 = models.CharField(db_column='DeliverAddr4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliverpostcode = models.CharField(db_column='DeliverPostCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    deliverphone1 = models.CharField(db_column='DeliverPhone1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    deliverfax1 = models.CharField(db_column='DeliverFax1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    delivercontact = models.CharField(db_column='DeliverContact', max_length=40, blank=True, null=True)  # Field name made lowercase.
    attention = models.CharField(db_column='Attention', max_length=40, blank=True, null=True)  # Field name made lowercase.
    contact = models.CharField(db_column='Contact', max_length=40, blank=True, null=True)  # Field name made lowercase.
    phone1 = models.CharField(db_column='Phone1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    phone2 = models.CharField(db_column='Phone2', max_length=25, blank=True, null=True)  # Field name made lowercase.
    fax1 = models.CharField(db_column='Fax1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    fax2 = models.CharField(db_column='Fax2', max_length=25, blank=True, null=True)  # Field name made lowercase.
    natureofbusiness = models.CharField(db_column='NatureOfBusiness', max_length=40, blank=True, null=True)  # Field name made lowercase.
    emailaddress = models.CharField(db_column='EmailAddress', max_length=80, blank=True, null=True)  # Field name made lowercase.
    logo = models.BinaryField(db_column='Logo', blank=True, null=True)  # Field name made lowercase.
    logoclass = models.CharField(db_column='LogoClass', max_length=40, blank=True, null=True)  # Field name made lowercase.
    reportheader = models.TextField(db_column='ReportHeader', blank=True, null=True)  # Field name made lowercase.
    remarkcolor = models.IntegerField(db_column='RemarkColor', blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    taxregisterno = models.CharField(db_column='TaxRegisterNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    salestaxregisterno = models.CharField(db_column='SalesTaxRegisterNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    servicetaxregisterno = models.CharField(db_column='ServiceTaxRegisterNo', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'Profile'


class Project(models.Model):
    projno = models.CharField(db_column='ProjNo', primary_key=True, max_length=10)  # Field name made lowercase.
    parentprojno = models.ForeignKey('self', models.DO_NOTHING, db_column='ParentProjNo', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=40, blank=True, null=True)  # Field name made lowercase.
    desc2 = models.CharField(db_column='Desc2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    isactive = models.CharField(db_column='IsActive', max_length=1)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.

    class Meta:
 
        db_table = 'Project'


class Promotion(models.Model):
    promotionkey = models.BigIntegerField(db_column='PromotionKey', primary_key=True)  # Field name made lowercase.
    promotioncode = models.CharField(db_column='PromotionCode', unique=True, max_length=20)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=80, blank=True, null=True)  # Field name made lowercase.
    fromdate = models.DateTimeField(db_column='FromDate', blank=True, null=True)  # Field name made lowercase.
    todate = models.DateTimeField(db_column='ToDate', blank=True, null=True)  # Field name made lowercase.
    fromtime = models.DateTimeField(db_column='FromTime', blank=True, null=True)  # Field name made lowercase.
    totime = models.DateTimeField(db_column='ToTime', blank=True, null=True)  # Field name made lowercase.
    validonweekday1 = models.CharField(db_column='ValidOnWeekDay1', max_length=1)  # Field name made lowercase.
    validonweekday2 = models.CharField(db_column='ValidOnWeekDay2', max_length=1)  # Field name made lowercase.
    validonweekday3 = models.CharField(db_column='ValidOnWeekDay3', max_length=1)  # Field name made lowercase.
    validonweekday4 = models.CharField(db_column='ValidOnWeekDay4', max_length=1)  # Field name made lowercase.
    validonweekday5 = models.CharField(db_column='ValidOnWeekDay5', max_length=1)  # Field name made lowercase.
    validonweekday6 = models.CharField(db_column='ValidOnWeekDay6', max_length=1)  # Field name made lowercase.
    validonweekday7 = models.CharField(db_column='ValidOnWeekDay7', max_length=1)  # Field name made lowercase.
    validforalloutlet = models.CharField(db_column='ValidForAllOutlet', max_length=1)  # Field name made lowercase.
    validforallmember = models.CharField(db_column='ValidForAllMember', max_length=1)  # Field name made lowercase.
    validforallmembertype = models.CharField(db_column='ValidForAllMemberType', max_length=1)  # Field name made lowercase.
    validforallaccount = models.CharField(db_column='ValidForAllAccount', max_length=1)  # Field name made lowercase.
    isactive = models.CharField(db_column='IsActive', max_length=1)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.

    class Meta:
 
        db_table = 'Promotion'


class Promotionaccount(models.Model):
    promotionkey = models.OneToOneField(Promotion, models.DO_NOTHING, db_column='PromotionKey', primary_key=True)  # Field name made lowercase.
    accno = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='AccNo')  # Field name made lowercase.

    class Meta:
 
        db_table = 'PromotionAccount'
        unique_together = (('promotionkey', 'accno'),)


class Promotiondtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    promotionkey = models.ForeignKey(Promotion, models.DO_NOTHING, db_column='PromotionKey')  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    itemcode = models.ForeignKey(Itemuom, models.DO_NOTHING, db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    uom = models.ForeignKey(Itemuom, models.DO_NOTHING, db_column='UOM', blank=True, null=True)  # Field name made lowercase.
    minpurchasedqty = models.DecimalField(db_column='MinPurchasedQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    discount = models.CharField(db_column='Discount', max_length=20, blank=True, null=True)  # Field name made lowercase.
    memberprice1 = models.DecimalField(db_column='MemberPrice1', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    memberdiscount1 = models.CharField(db_column='MemberDiscount1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    memberprice2 = models.DecimalField(db_column='MemberPrice2', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    memberdiscount2 = models.CharField(db_column='MemberDiscount2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    memberprice3 = models.DecimalField(db_column='MemberPrice3', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    memberdiscount3 = models.CharField(db_column='MemberDiscount3', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'PromotionDTL'


class Promotionlocation(models.Model):
    promotionkey = models.OneToOneField(Promotion, models.DO_NOTHING, db_column='PromotionKey', primary_key=True)  # Field name made lowercase.
    location = models.ForeignKey(Location, models.DO_NOTHING, db_column='Location')  # Field name made lowercase.

    class Meta:
 
        db_table = 'PromotionLocation'
        unique_together = (('promotionkey', 'location'),)


class Promotionmember(models.Model):
    promotionkey = models.OneToOneField(Promotion, models.DO_NOTHING, db_column='PromotionKey', primary_key=True)  # Field name made lowercase.
    memberno = models.ForeignKey(Member, models.DO_NOTHING, db_column='MemberNo')  # Field name made lowercase.

    class Meta:
 
        db_table = 'PromotionMember'
        unique_together = (('promotionkey', 'memberno'),)


class Promotionmembertype(models.Model):
    promotionkey = models.OneToOneField(Promotion, models.DO_NOTHING, db_column='PromotionKey', primary_key=True)  # Field name made lowercase.
    membertype = models.ForeignKey(Membertype, models.DO_NOTHING, db_column='MemberType')  # Field name made lowercase.

    class Meta:
 
        db_table = 'PromotionMemberType'
        unique_together = (('promotionkey', 'membertype'),)


class Promotionpwp(models.Model):
    pwpkey = models.BigIntegerField(db_column='PWPKey', primary_key=True)  # Field name made lowercase.
    promotionkey = models.ForeignKey(Promotion, models.DO_NOTHING, db_column='PromotionKey')  # Field name made lowercase.
    itemcode = models.ForeignKey(Itemuom, models.DO_NOTHING, db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    uom = models.ForeignKey(Itemuom, models.DO_NOTHING, db_column='UOM', blank=True, null=True)  # Field name made lowercase.
    purchasedqty = models.DecimalField(db_column='PurchasedQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    purchasedamt = models.DecimalField(db_column='PurchasedAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'PromotionPWP'


class Promotionpwpdtl(models.Model):
    pwpdtlkey = models.BigIntegerField(db_column='PWPDtlKey', primary_key=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    pwpkey = models.ForeignKey(Promotionpwp, models.DO_NOTHING, db_column='PWPKey')  # Field name made lowercase.
    itemcode = models.ForeignKey(Itemuom, models.DO_NOTHING, db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    uom = models.ForeignKey(Itemuom, models.DO_NOTHING, db_column='UOM', blank=True, null=True)  # Field name made lowercase.
    isfoc = models.CharField(db_column='IsFOC', max_length=1)  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=25, decimal_places=8)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    discount = models.CharField(db_column='Discount', max_length=12, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'PromotionPWPDTL'


class Purchaseagent(models.Model):
    purchaseagent = models.CharField(db_column='PurchaseAgent', primary_key=True, max_length=12)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=40, blank=True, null=True)  # Field name made lowercase.
    desc2 = models.CharField(db_column='Desc2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    isactive = models.CharField(db_column='IsActive', max_length=1)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    signature = models.BinaryField(db_column='Signature', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'PurchaseAgent'


class Qt(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', unique=True, max_length=20)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    debtorcode = models.ForeignKey(Branch, models.DO_NOTHING, db_column='DebtorCode', blank=True, null=True)  # Field name made lowercase.
    debtorname = models.CharField(db_column='DebtorName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ref = models.CharField(db_column='Ref', max_length=40, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=80, blank=True, null=True)  # Field name made lowercase.
    displayterm = models.ForeignKey('Terms', models.DO_NOTHING, db_column='DisplayTerm')  # Field name made lowercase.
    salesagent = models.ForeignKey('Salesagent', models.DO_NOTHING, db_column='SalesAgent', blank=True, null=True)  # Field name made lowercase.
    invaddr1 = models.CharField(db_column='InvAddr1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr2 = models.CharField(db_column='InvAddr2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr3 = models.CharField(db_column='InvAddr3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr4 = models.CharField(db_column='InvAddr4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    phone1 = models.CharField(db_column='Phone1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    fax1 = models.CharField(db_column='Fax1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    attention = models.CharField(db_column='Attention', max_length=40, blank=True, null=True)  # Field name made lowercase.
    branchcode = models.ForeignKey(Branch, models.DO_NOTHING, db_column='BranchCode', blank=True, null=True)  # Field name made lowercase.
    deliveraddr1 = models.CharField(db_column='DeliverAddr1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliveraddr2 = models.CharField(db_column='DeliverAddr2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliveraddr3 = models.CharField(db_column='DeliverAddr3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliveraddr4 = models.CharField(db_column='DeliverAddr4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliverphone1 = models.CharField(db_column='DeliverPhone1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    deliverfax1 = models.CharField(db_column='DeliverFax1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    delivercontact = models.CharField(db_column='DeliverContact', max_length=40, blank=True, null=True)  # Field name made lowercase.
    salesexemptionno = models.CharField(db_column='SalesExemptionNo', max_length=60, blank=True, null=True)  # Field name made lowercase.
    salesexemptionexpirydate = models.DateTimeField(db_column='SalesExemptionExpiryDate', blank=True, null=True)  # Field name made lowercase.
    validity = models.CharField(db_column='Validity', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliveryterm = models.CharField(db_column='DeliveryTerm', max_length=40, blank=True, null=True)  # Field name made lowercase.
    paymentterm = models.CharField(db_column='PaymentTerm', max_length=40, blank=True, null=True)  # Field name made lowercase.
    yourref = models.CharField(db_column='YourRef', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cc = models.CharField(db_column='CC', max_length=20, blank=True, null=True)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1param = models.DecimalField(db_column='Footer1Param', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1amt = models.DecimalField(db_column='Footer1Amt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1localamt = models.DecimalField(db_column='Footer1LocalAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='Footer1TaxType', blank=True, null=True)  # Field name made lowercase.
    footer2param = models.DecimalField(db_column='Footer2Param', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2amt = models.DecimalField(db_column='Footer2Amt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2localamt = models.DecimalField(db_column='Footer2LocalAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='Footer2TaxType', blank=True, null=True)  # Field name made lowercase.
    footer3param = models.DecimalField(db_column='Footer3Param', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3amt = models.DecimalField(db_column='Footer3Amt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3localamt = models.DecimalField(db_column='Footer3LocalAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='Footer3TaxType', blank=True, null=True)  # Field name made lowercase.
    currencycode = models.ForeignKey(Currency, models.DO_NOTHING, db_column='CurrencyCode')  # Field name made lowercase.
    currencyrate = models.DecimalField(db_column='CurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    nettotal = models.DecimalField(db_column='NetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localnettotal = models.DecimalField(db_column='LocalNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    analysisnettotal = models.DecimalField(db_column='AnalysisNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localanalysisnettotal = models.DecimalField(db_column='LocalAnalysisNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtax = models.DecimalField(db_column='LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    transferable = models.CharField(db_column='Transferable', max_length=1)  # Field name made lowercase.
    todoctype = models.CharField(db_column='ToDocType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    todockey = models.BigIntegerField(db_column='ToDocKey', blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    remark1 = models.CharField(db_column='Remark1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark2 = models.CharField(db_column='Remark2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark3 = models.CharField(db_column='Remark3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark4 = models.CharField(db_column='Remark4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    printcount = models.SmallIntegerField(db_column='PrintCount')  # Field name made lowercase.
    cancelled = models.CharField(db_column='Cancelled', max_length=1)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    createduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    approvaluserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='ApprovalUserID', blank=True, null=True)  # Field name made lowercase.
    externallink = models.TextField(db_column='ExternalLink', blank=True, null=True)  # Field name made lowercase.
    refdocno = models.CharField(db_column='RefDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cansync = models.CharField(db_column='CanSync', max_length=1)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    todtlkey = models.BigIntegerField(db_column='ToDtlKey', blank=True, null=True)  # Field name made lowercase.
    fulltransferoption = models.CharField(db_column='FullTransferOption', max_length=1, blank=True, null=True)  # Field name made lowercase.
    shipvia = models.ForeignKey('Shippingmethod', models.DO_NOTHING, db_column='ShipVia', blank=True, null=True)  # Field name made lowercase.
    shipinfo = models.CharField(db_column='ShipInfo', max_length=40, blank=True, null=True)  # Field name made lowercase.
    saleslocation = models.ForeignKey(Location, models.DO_NOTHING, db_column='SalesLocation', blank=True, null=True)  # Field name made lowercase.
    footer1tax = models.DecimalField(db_column='Footer1Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1localtax = models.DecimalField(db_column='Footer1LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2tax = models.DecimalField(db_column='Footer2Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2localtax = models.DecimalField(db_column='Footer2LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3tax = models.DecimalField(db_column='Footer3Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3localtax = models.DecimalField(db_column='Footer3LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    extax = models.DecimalField(db_column='ExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localextax = models.DecimalField(db_column='LocalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.
    totaxcurrencyrate = models.DecimalField(db_column='ToTaxCurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    calcdiscountonunitprice = models.CharField(db_column='CalcDiscountOnUnitPrice', max_length=1, blank=True, null=True)  # Field name made lowercase.
    totalextax = models.DecimalField(db_column='TotalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxableamt = models.DecimalField(db_column='TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    inclusivetax = models.CharField(db_column='InclusiveTax', max_length=1)  # Field name made lowercase.
    footer1taxrate = models.DecimalField(db_column='Footer1TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    footer2taxrate = models.DecimalField(db_column='Footer2TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    footer3taxrate = models.DecimalField(db_column='Footer3TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    roundingmethod = models.IntegerField(db_column='RoundingMethod')  # Field name made lowercase.
    localtaxableamt = models.DecimalField(db_column='LocalTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytax = models.DecimalField(db_column='TaxCurrencyTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxableamt = models.DecimalField(db_column='TaxCurrencyTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    isroundadj = models.CharField(db_column='IsRoundAdj', max_length=1)  # Field name made lowercase.
    roundadj = models.DecimalField(db_column='RoundAdj', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    finaltotal = models.DecimalField(db_column='FinalTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'QT'


class Qtdtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    indent = models.SmallIntegerField(db_column='Indent', blank=True, null=True)  # Field name made lowercase.
    fontstyle = models.ForeignKey(Fontstyle, models.DO_NOTHING, db_column='FontStyle', blank=True, null=True)  # Field name made lowercase.
    mainitem = models.CharField(db_column='MainItem', max_length=1)  # Field name made lowercase.
    numbering = models.CharField(db_column='Numbering', max_length=6, blank=True, null=True)  # Field name made lowercase.
    itemcode = models.ForeignKey(Itemuom, models.DO_NOTHING, db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    location = models.ForeignKey(Location, models.DO_NOTHING, db_column='Location', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    furtherdescription = models.TextField(db_column='FurtherDescription', blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey(Project, models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey(Dept, models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    uom = models.ForeignKey(Itemuom, models.DO_NOTHING, db_column='UOM', blank=True, null=True)  # Field name made lowercase.
    useruom = models.CharField(db_column='UserUOM', max_length=8, blank=True, null=True)  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    smallestqty = models.DecimalField(db_column='SmallestQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    transferedqty = models.DecimalField(db_column='TransferedQty', max_digits=25, decimal_places=8)  # Field name made lowercase.
    smallestunitprice = models.DecimalField(db_column='SmallestUnitPrice', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    discount = models.CharField(db_column='Discount', max_length=20, blank=True, null=True)  # Field name made lowercase.
    discountamt = models.DecimalField(db_column='DiscountAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='TaxType', blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localsubtotal = models.DecimalField(db_column='LocalSubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    transferable = models.CharField(db_column='Transferable', max_length=1)  # Field name made lowercase.
    printout = models.CharField(db_column='PrintOut', max_length=1)  # Field name made lowercase.
    dtltype = models.CharField(db_column='DtlType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    calcbypercent = models.DecimalField(db_column='CalcByPercent', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    addtosubtotal = models.CharField(db_column='AddToSubTotal', max_length=1)  # Field name made lowercase.
    estimateddeliverydate = models.CharField(db_column='EstimatedDeliveryDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    packagedockey = models.BigIntegerField(db_column='PackageDocKey', blank=True, null=True)  # Field name made lowercase.
    parentdtlkey = models.BigIntegerField(db_column='ParentDtlKey', blank=True, null=True)  # Field name made lowercase.
    subqty = models.DecimalField(db_column='SubQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    subtotalextax = models.DecimalField(db_column='SubTotalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtax = models.DecimalField(db_column='LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.
    ruleno = models.BigIntegerField(db_column='RuleNo', blank=True, null=True)  # Field name made lowercase.
    deliverydate = models.DateTimeField(db_column='DeliveryDate', blank=True, null=True)  # Field name made lowercase.
    taxableamt = models.DecimalField(db_column='TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxadjustment = models.DecimalField(db_column='TaxAdjustment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localsubtotalextax = models.DecimalField(db_column='LocalSubTotalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    extradiscountamt = models.DecimalField(db_column='ExtraDiscountAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxrate = models.DecimalField(db_column='TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    localtaxadjustment = models.DecimalField(db_column='LocalTaxAdjustment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtaxableamt = models.DecimalField(db_column='LocalTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytax = models.DecimalField(db_column='TaxCurrencyTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxableamt = models.DecimalField(db_column='TaxCurrencyTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    salesexemptionno = models.CharField(db_column='SalesExemptionNo', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'QTDTL'


class Rcv(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', unique=True, max_length=20)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    remark1 = models.CharField(db_column='Remark1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark2 = models.CharField(db_column='Remark2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark3 = models.CharField(db_column='Remark3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark4 = models.CharField(db_column='Remark4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    printcount = models.SmallIntegerField(db_column='PrintCount')  # Field name made lowercase.
    cancelled = models.CharField(db_column='Cancelled', max_length=1)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    createduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    externallink = models.TextField(db_column='ExternalLink', blank=True, null=True)  # Field name made lowercase.
    refdocno = models.CharField(db_column='RefDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    cansync = models.CharField(db_column='CanSync', max_length=1)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.

    class Meta:
 
        db_table = 'RCV'


class Rcvdtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    numbering = models.CharField(db_column='Numbering', max_length=6, blank=True, null=True)  # Field name made lowercase.
    itemcode = models.ForeignKey(Itemuom, models.DO_NOTHING, db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    location = models.ForeignKey(Location, models.DO_NOTHING, db_column='Location', blank=True, null=True)  # Field name made lowercase.
    batchno = models.ForeignKey(Itembatch, models.DO_NOTHING, db_column='BatchNo', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    furtherdescription = models.TextField(db_column='FurtherDescription', blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey(Project, models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey(Dept, models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    uom = models.ForeignKey(Itemuom, models.DO_NOTHING, db_column='UOM', blank=True, null=True)  # Field name made lowercase.
    unitcost = models.DecimalField(db_column='UnitCost', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    printout = models.CharField(db_column='PrintOut', max_length=1)  # Field name made lowercase.
    serialnolist = models.TextField(db_column='SerialNoList', blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.

    class Meta:
 
        db_table = 'RCVDTL'


class Rq(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', unique=True, max_length=20)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    creditorcode = models.ForeignKey(Branch, models.DO_NOTHING, db_column='CreditorCode', blank=True, null=True)  # Field name made lowercase.
    creditorname = models.CharField(db_column='CreditorName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ref = models.CharField(db_column='Ref', max_length=40, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=80, blank=True, null=True)  # Field name made lowercase.
    displayterm = models.ForeignKey('Terms', models.DO_NOTHING, db_column='DisplayTerm')  # Field name made lowercase.
    purchaseagent = models.ForeignKey(Purchaseagent, models.DO_NOTHING, db_column='PurchaseAgent', blank=True, null=True)  # Field name made lowercase.
    invaddr1 = models.CharField(db_column='InvAddr1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr2 = models.CharField(db_column='InvAddr2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr3 = models.CharField(db_column='InvAddr3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr4 = models.CharField(db_column='InvAddr4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    phone1 = models.CharField(db_column='Phone1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    fax1 = models.CharField(db_column='Fax1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    attention = models.CharField(db_column='Attention', max_length=40, blank=True, null=True)  # Field name made lowercase.
    branchcode = models.ForeignKey(Branch, models.DO_NOTHING, db_column='BranchCode', blank=True, null=True)  # Field name made lowercase.
    deliveraddr1 = models.CharField(db_column='DeliverAddr1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliveraddr2 = models.CharField(db_column='DeliverAddr2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliveraddr3 = models.CharField(db_column='DeliverAddr3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliveraddr4 = models.CharField(db_column='DeliverAddr4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliverphone1 = models.CharField(db_column='DeliverPhone1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    deliverfax1 = models.CharField(db_column='DeliverFax1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    delivercontact = models.CharField(db_column='DeliverContact', max_length=40, blank=True, null=True)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1param = models.DecimalField(db_column='Footer1Param', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1amt = models.DecimalField(db_column='Footer1Amt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1localamt = models.DecimalField(db_column='Footer1LocalAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='Footer1TaxType', blank=True, null=True)  # Field name made lowercase.
    footer2param = models.DecimalField(db_column='Footer2Param', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2amt = models.DecimalField(db_column='Footer2Amt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2localamt = models.DecimalField(db_column='Footer2LocalAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='Footer2TaxType', blank=True, null=True)  # Field name made lowercase.
    footer3param = models.DecimalField(db_column='Footer3Param', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3amt = models.DecimalField(db_column='Footer3Amt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3localamt = models.DecimalField(db_column='Footer3LocalAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='Footer3TaxType', blank=True, null=True)  # Field name made lowercase.
    currencycode = models.ForeignKey(Currency, models.DO_NOTHING, db_column='CurrencyCode')  # Field name made lowercase.
    currencyrate = models.DecimalField(db_column='CurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    nettotal = models.DecimalField(db_column='NetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localnettotal = models.DecimalField(db_column='LocalNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtax = models.DecimalField(db_column='LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    transferable = models.CharField(db_column='Transferable', max_length=1)  # Field name made lowercase.
    todoctype = models.CharField(db_column='ToDocType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    todockey = models.BigIntegerField(db_column='ToDocKey', blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    remark1 = models.CharField(db_column='Remark1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark2 = models.CharField(db_column='Remark2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark3 = models.CharField(db_column='Remark3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark4 = models.CharField(db_column='Remark4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    printcount = models.SmallIntegerField(db_column='PrintCount')  # Field name made lowercase.
    cancelled = models.CharField(db_column='Cancelled', max_length=1)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    createduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    externallink = models.TextField(db_column='ExternalLink', blank=True, null=True)  # Field name made lowercase.
    refdocno = models.CharField(db_column='RefDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cansync = models.CharField(db_column='CanSync', max_length=1)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    todtlkey = models.BigIntegerField(db_column='ToDtlKey', blank=True, null=True)  # Field name made lowercase.
    fulltransferoption = models.CharField(db_column='FullTransferOption', max_length=1, blank=True, null=True)  # Field name made lowercase.
    purchaselocation = models.ForeignKey(Location, models.DO_NOTHING, db_column='PurchaseLocation', blank=True, null=True)  # Field name made lowercase.
    footer1tax = models.DecimalField(db_column='Footer1Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1localtax = models.DecimalField(db_column='Footer1LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2tax = models.DecimalField(db_column='Footer2Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2localtax = models.DecimalField(db_column='Footer2LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3tax = models.DecimalField(db_column='Footer3Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3localtax = models.DecimalField(db_column='Footer3LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    extax = models.DecimalField(db_column='ExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localextax = models.DecimalField(db_column='LocalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    analysisnettotal = models.DecimalField(db_column='AnalysisNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localanalysisnettotal = models.DecimalField(db_column='LocalAnalysisNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.
    totaxcurrencyrate = models.DecimalField(db_column='ToTaxCurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    calcdiscountonunitprice = models.CharField(db_column='CalcDiscountOnUnitPrice', max_length=1, blank=True, null=True)  # Field name made lowercase.
    totalextax = models.DecimalField(db_column='TotalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxableamt = models.DecimalField(db_column='TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    inclusivetax = models.CharField(db_column='InclusiveTax', max_length=1)  # Field name made lowercase.
    footer1taxrate = models.DecimalField(db_column='Footer1TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    footer2taxrate = models.DecimalField(db_column='Footer2TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    footer3taxrate = models.DecimalField(db_column='Footer3TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    roundingmethod = models.IntegerField(db_column='RoundingMethod')  # Field name made lowercase.
    localtaxableamt = models.DecimalField(db_column='LocalTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytax = models.DecimalField(db_column='TaxCurrencyTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxableamt = models.DecimalField(db_column='TaxCurrencyTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'RQ'


class Rqdtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    indent = models.SmallIntegerField(db_column='Indent', blank=True, null=True)  # Field name made lowercase.
    fontstyle = models.ForeignKey(Fontstyle, models.DO_NOTHING, db_column='FontStyle', blank=True, null=True)  # Field name made lowercase.
    mainitem = models.CharField(db_column='MainItem', max_length=1)  # Field name made lowercase.
    numbering = models.CharField(db_column='Numbering', max_length=6, blank=True, null=True)  # Field name made lowercase.
    itemcode = models.ForeignKey(Itemuom, models.DO_NOTHING, db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    location = models.ForeignKey(Location, models.DO_NOTHING, db_column='Location', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    furtherdescription = models.TextField(db_column='FurtherDescription', blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey(Project, models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey(Dept, models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    uom = models.ForeignKey(Itemuom, models.DO_NOTHING, db_column='UOM', blank=True, null=True)  # Field name made lowercase.
    useruom = models.CharField(db_column='UserUOM', max_length=8, blank=True, null=True)  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    smallestqty = models.DecimalField(db_column='SmallestQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    transferedqty = models.DecimalField(db_column='TransferedQty', max_digits=25, decimal_places=8)  # Field name made lowercase.
    smallestunitprice = models.DecimalField(db_column='SmallestUnitPrice', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    discount = models.CharField(db_column='Discount', max_length=20, blank=True, null=True)  # Field name made lowercase.
    discountamt = models.DecimalField(db_column='DiscountAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='TaxType', blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localsubtotal = models.DecimalField(db_column='LocalSubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    transferable = models.CharField(db_column='Transferable', max_length=1)  # Field name made lowercase.
    printout = models.CharField(db_column='PrintOut', max_length=1)  # Field name made lowercase.
    dtltype = models.CharField(db_column='DtlType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    calcbypercent = models.DecimalField(db_column='CalcByPercent', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    addtosubtotal = models.CharField(db_column='AddToSubTotal', max_length=1)  # Field name made lowercase.
    estimateddeliverydate = models.CharField(db_column='EstimatedDeliveryDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    packagedockey = models.BigIntegerField(db_column='PackageDocKey', blank=True, null=True)  # Field name made lowercase.
    parentdtlkey = models.BigIntegerField(db_column='ParentDtlKey', blank=True, null=True)  # Field name made lowercase.
    subqty = models.DecimalField(db_column='SubQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    subtotalextax = models.DecimalField(db_column='SubTotalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtax = models.DecimalField(db_column='LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.
    deliverydate = models.DateTimeField(db_column='DeliveryDate', blank=True, null=True)  # Field name made lowercase.
    taxableamt = models.DecimalField(db_column='TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxadjustment = models.DecimalField(db_column='TaxAdjustment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localsubtotalextax = models.DecimalField(db_column='LocalSubTotalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    extradiscountamt = models.DecimalField(db_column='ExtraDiscountAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxrate = models.DecimalField(db_column='TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    localtaxadjustment = models.DecimalField(db_column='LocalTaxAdjustment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtaxableamt = models.DecimalField(db_column='LocalTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytax = models.DecimalField(db_column='TaxCurrencyTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxableamt = models.DecimalField(db_column='TaxCurrencyTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    salesexemptionno = models.CharField(db_column='SalesExemptionNo', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'RQDTL'


class Race(models.Model):
    race = models.CharField(db_column='Race', primary_key=True, max_length=10)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=80, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'Race'


class Registry(models.Model):
    regid = models.IntegerField(db_column='RegID', primary_key=True)  # Field name made lowercase.
    regtype = models.SmallIntegerField(db_column='RegType', blank=True, null=True)  # Field name made lowercase.
    regvalue = models.CharField(db_column='RegValue', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'Registry'


class Remarkname(models.Model):
    doctype = models.CharField(db_column='DocType', primary_key=True, max_length=2)  # Field name made lowercase.
    remark1name = models.CharField(db_column='Remark1Name', max_length=30, blank=True, null=True)  # Field name made lowercase.
    remark2name = models.CharField(db_column='Remark2Name', max_length=30, blank=True, null=True)  # Field name made lowercase.
    remark3name = models.CharField(db_column='Remark3Name', max_length=30, blank=True, null=True)  # Field name made lowercase.
    remark4name = models.CharField(db_column='Remark4Name', max_length=30, blank=True, null=True)  # Field name made lowercase.
    remark1mru = models.CharField(db_column='Remark1MRU', max_length=1)  # Field name made lowercase.
    remark2mru = models.CharField(db_column='Remark2MRU', max_length=1)  # Field name made lowercase.
    remark3mru = models.CharField(db_column='Remark3MRU', max_length=1)  # Field name made lowercase.
    remark4mru = models.CharField(db_column='Remark4MRU', max_length=1)  # Field name made lowercase.

    class Meta:
 
        db_table = 'RemarkName'


class Report(models.Model):
    reportname = models.CharField(db_column='ReportName', primary_key=True, max_length=100)  # Field name made lowercase.
    reporttype = models.CharField(db_column='ReportType', max_length=60, blank=True, null=True)  # Field name made lowercase.
    reporttemplate = models.BinaryField(db_column='ReportTemplate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'Report'


class Reportattributes(models.Model):
    reportname = models.CharField(db_column='ReportName', primary_key=True, max_length=100)  # Field name made lowercase.
    denyusers = models.TextField(db_column='DenyUsers', blank=True, null=True)  # Field name made lowercase.
    attributes = models.TextField(db_column='Attributes', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'ReportAttributes'


class Reversegstdo(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    doctype = models.CharField(db_column='DocType', max_length=2)  # Field name made lowercase.
    jedockey = models.BigIntegerField(db_column='JEDocKey')  # Field name made lowercase.

    class Meta:
 
        db_table = 'ReverseGSTDO'
        unique_together = (('dockey', 'doctype'),)


class Reversegstpayment(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    doctype = models.CharField(db_column='DocType', max_length=2)  # Field name made lowercase.
    applieddockey = models.BigIntegerField(db_column='AppliedDocKey')  # Field name made lowercase.
    applieddoctype = models.CharField(db_column='AppliedDocType', max_length=2)  # Field name made lowercase.
    jedockey = models.BigIntegerField(db_column='JEDocKey')  # Field name made lowercase.

    class Meta:
 
        db_table = 'ReverseGSTPayment'
        unique_together = (('dockey', 'doctype', 'applieddockey', 'applieddoctype'),)


class Reversesstpayment(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    doctype = models.CharField(db_column='DocType', max_length=2)  # Field name made lowercase.
    applieddockey = models.BigIntegerField(db_column='AppliedDocKey')  # Field name made lowercase.
    applieddoctype = models.CharField(db_column='AppliedDocType', max_length=2)  # Field name made lowercase.
    jedockey = models.BigIntegerField(db_column='JEDocKey')  # Field name made lowercase.

    class Meta:
 
        db_table = 'ReverseSSTPayment'
        unique_together = (('dockey', 'doctype', 'applieddockey', 'applieddoctype'),)


class So(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', unique=True, max_length=20)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    debtorcode = models.ForeignKey(Branch, models.DO_NOTHING, db_column='DebtorCode')  # Field name made lowercase.
    debtorname = models.CharField(db_column='DebtorName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ref = models.CharField(db_column='Ref', max_length=40, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=80, blank=True, null=True)  # Field name made lowercase.
    displayterm = models.ForeignKey('Terms', models.DO_NOTHING, db_column='DisplayTerm')  # Field name made lowercase.
    salesagent = models.ForeignKey('Salesagent', models.DO_NOTHING, db_column='SalesAgent', blank=True, null=True)  # Field name made lowercase.
    invaddr1 = models.CharField(db_column='InvAddr1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr2 = models.CharField(db_column='InvAddr2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr3 = models.CharField(db_column='InvAddr3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr4 = models.CharField(db_column='InvAddr4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    phone1 = models.CharField(db_column='Phone1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    fax1 = models.CharField(db_column='Fax1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    attention = models.CharField(db_column='Attention', max_length=40, blank=True, null=True)  # Field name made lowercase.
    branchcode = models.ForeignKey(Branch, models.DO_NOTHING, db_column='BranchCode', blank=True, null=True)  # Field name made lowercase.
    deliveraddr1 = models.CharField(db_column='DeliverAddr1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliveraddr2 = models.CharField(db_column='DeliverAddr2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliveraddr3 = models.CharField(db_column='DeliverAddr3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliveraddr4 = models.CharField(db_column='DeliverAddr4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliverphone1 = models.CharField(db_column='DeliverPhone1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    deliverfax1 = models.CharField(db_column='DeliverFax1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    delivercontact = models.CharField(db_column='DeliverContact', max_length=40, blank=True, null=True)  # Field name made lowercase.
    salesexemptionno = models.CharField(db_column='SalesExemptionNo', max_length=60, blank=True, null=True)  # Field name made lowercase.
    salesexemptionexpirydate = models.DateTimeField(db_column='SalesExemptionExpiryDate', blank=True, null=True)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1param = models.DecimalField(db_column='Footer1Param', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1amt = models.DecimalField(db_column='Footer1Amt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1localamt = models.DecimalField(db_column='Footer1LocalAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='Footer1TaxType', blank=True, null=True)  # Field name made lowercase.
    footer2param = models.DecimalField(db_column='Footer2Param', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2amt = models.DecimalField(db_column='Footer2Amt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2localamt = models.DecimalField(db_column='Footer2LocalAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='Footer2TaxType', blank=True, null=True)  # Field name made lowercase.
    footer3param = models.DecimalField(db_column='Footer3Param', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3amt = models.DecimalField(db_column='Footer3Amt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3localamt = models.DecimalField(db_column='Footer3LocalAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='Footer3TaxType', blank=True, null=True)  # Field name made lowercase.
    currencycode = models.ForeignKey(Currency, models.DO_NOTHING, db_column='CurrencyCode')  # Field name made lowercase.
    currencyrate = models.DecimalField(db_column='CurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    nettotal = models.DecimalField(db_column='NetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localnettotal = models.DecimalField(db_column='LocalNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    analysisnettotal = models.DecimalField(db_column='AnalysisNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localanalysisnettotal = models.DecimalField(db_column='LocalAnalysisNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtax = models.DecimalField(db_column='LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    referdepositdockey = models.BigIntegerField(db_column='ReferDepositDocKey', blank=True, null=True)  # Field name made lowercase.
    transferable = models.CharField(db_column='Transferable', max_length=1)  # Field name made lowercase.
    todoctype = models.CharField(db_column='ToDocType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    todockey = models.BigIntegerField(db_column='ToDocKey', blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    remark1 = models.CharField(db_column='Remark1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark2 = models.CharField(db_column='Remark2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark3 = models.CharField(db_column='Remark3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark4 = models.CharField(db_column='Remark4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    printcount = models.SmallIntegerField(db_column='PrintCount')  # Field name made lowercase.
    cancelled = models.CharField(db_column='Cancelled', max_length=1)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    createduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    externallink = models.TextField(db_column='ExternalLink', blank=True, null=True)  # Field name made lowercase.
    refdocno = models.CharField(db_column='RefDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cantransferbyvalue = models.CharField(db_column='CanTransferByValue', max_length=1, blank=True, null=True)  # Field name made lowercase.
    transferedamt = models.DecimalField(db_column='TransferedAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cansync = models.CharField(db_column='CanSync', max_length=1)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    todtlkey = models.BigIntegerField(db_column='ToDtlKey', blank=True, null=True)  # Field name made lowercase.
    fulltransferoption = models.CharField(db_column='FullTransferOption', max_length=1, blank=True, null=True)  # Field name made lowercase.
    shipvia = models.ForeignKey('Shippingmethod', models.DO_NOTHING, db_column='ShipVia', blank=True, null=True)  # Field name made lowercase.
    shipinfo = models.CharField(db_column='ShipInfo', max_length=40, blank=True, null=True)  # Field name made lowercase.
    saleslocation = models.ForeignKey(Location, models.DO_NOTHING, db_column='SalesLocation', blank=True, null=True)  # Field name made lowercase.
    footer1tax = models.DecimalField(db_column='Footer1Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1localtax = models.DecimalField(db_column='Footer1LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2tax = models.DecimalField(db_column='Footer2Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2localtax = models.DecimalField(db_column='Footer2LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3tax = models.DecimalField(db_column='Footer3Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3localtax = models.DecimalField(db_column='Footer3LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    extax = models.DecimalField(db_column='ExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localextax = models.DecimalField(db_column='LocalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    yourpono = models.CharField(db_column='YourPONo', max_length=25, blank=True, null=True)  # Field name made lowercase.
    yourpodate = models.DateTimeField(db_column='YourPODate', blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.
    totaxcurrencyrate = models.DecimalField(db_column='ToTaxCurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    calcdiscountonunitprice = models.CharField(db_column='CalcDiscountOnUnitPrice', max_length=1, blank=True, null=True)  # Field name made lowercase.
    totalextax = models.DecimalField(db_column='TotalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxableamt = models.DecimalField(db_column='TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    inclusivetax = models.CharField(db_column='InclusiveTax', max_length=1)  # Field name made lowercase.
    footer1taxrate = models.DecimalField(db_column='Footer1TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    footer2taxrate = models.DecimalField(db_column='Footer2TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    footer3taxrate = models.DecimalField(db_column='Footer3TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    isroundadj = models.CharField(db_column='IsRoundAdj', max_length=1)  # Field name made lowercase.
    roundadj = models.DecimalField(db_column='RoundAdj', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    finaltotal = models.DecimalField(db_column='FinalTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    roundingmethod = models.IntegerField(db_column='RoundingMethod')  # Field name made lowercase.
    localtaxableamt = models.DecimalField(db_column='LocalTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytax = models.DecimalField(db_column='TaxCurrencyTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxableamt = models.DecimalField(db_column='TaxCurrencyTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'SO'


class Sodtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    indent = models.SmallIntegerField(db_column='Indent', blank=True, null=True)  # Field name made lowercase.
    fontstyle = models.ForeignKey(Fontstyle, models.DO_NOTHING, db_column='FontStyle', blank=True, null=True)  # Field name made lowercase.
    mainitem = models.CharField(db_column='MainItem', max_length=1)  # Field name made lowercase.
    numbering = models.CharField(db_column='Numbering', max_length=6, blank=True, null=True)  # Field name made lowercase.
    itemcode = models.ForeignKey(Itemuom, models.DO_NOTHING, db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    location = models.ForeignKey(Location, models.DO_NOTHING, db_column='Location', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    furtherdescription = models.TextField(db_column='FurtherDescription', blank=True, null=True)  # Field name made lowercase.
    yourpono = models.CharField(db_column='YourPONo', max_length=25, blank=True, null=True)  # Field name made lowercase.
    yourpodate = models.DateTimeField(db_column='YourPODate', blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey(Project, models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey(Dept, models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    uom = models.ForeignKey(Itemuom, models.DO_NOTHING, db_column='UOM', blank=True, null=True)  # Field name made lowercase.
    useruom = models.CharField(db_column='UserUOM', max_length=8, blank=True, null=True)  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    smallestqty = models.DecimalField(db_column='SmallestQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    transferedqty = models.DecimalField(db_column='TransferedQty', max_digits=25, decimal_places=8)  # Field name made lowercase.
    focqty = models.DecimalField(db_column='FOCQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    foctransferedqty = models.DecimalField(db_column='FOCTransferedQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    smallestunitprice = models.DecimalField(db_column='SmallestUnitPrice', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    discount = models.CharField(db_column='Discount', max_length=20, blank=True, null=True)  # Field name made lowercase.
    discountamt = models.DecimalField(db_column='DiscountAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='TaxType', blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localsubtotal = models.DecimalField(db_column='LocalSubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    transferable = models.CharField(db_column='Transferable', max_length=1)  # Field name made lowercase.
    printout = models.CharField(db_column='PrintOut', max_length=1)  # Field name made lowercase.
    dtltype = models.CharField(db_column='DtlType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    calcbypercent = models.DecimalField(db_column='CalcByPercent', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    addtosubtotal = models.CharField(db_column='AddToSubTotal', max_length=1)  # Field name made lowercase.
    fromdoctype = models.CharField(db_column='FromDocType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    fromdocno = models.CharField(db_column='FromDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fromdocdtlkey = models.BigIntegerField(db_column='FromDocDtlKey', blank=True, null=True)  # Field name made lowercase.
    fulltransferoption = models.CharField(db_column='FullTransferOption', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fulltransferfromdoclist = models.TextField(db_column='FullTransferFromDocList', blank=True, null=True)  # Field name made lowercase.
    transferedpoqty = models.DecimalField(db_column='TransferedPOQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    foctransferedpoqty = models.DecimalField(db_column='FOCTransferedPOQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    estimateddeliverydate = models.CharField(db_column='EstimatedDeliveryDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    packagedockey = models.BigIntegerField(db_column='PackageDocKey', blank=True, null=True)  # Field name made lowercase.
    parentdtlkey = models.BigIntegerField(db_column='ParentDtlKey', blank=True, null=True)  # Field name made lowercase.
    transferedaoqty = models.DecimalField(db_column='TransferedAOQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    subqty = models.DecimalField(db_column='SubQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    stockreceived = models.CharField(db_column='StockReceived', max_length=1)  # Field name made lowercase.
    totalpurchaserequestqty = models.DecimalField(db_column='TotalPurchaseRequestQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    totaldeliveryrequestqty = models.DecimalField(db_column='TotalDeliveryRequestQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    totalassemblyorderrequestqty = models.DecimalField(db_column='TotalAssemblyOrderRequestQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    purchasestatus = models.SmallIntegerField(db_column='PurchaseStatus', blank=True, null=True)  # Field name made lowercase.
    deliverystatus = models.SmallIntegerField(db_column='DeliveryStatus', blank=True, null=True)  # Field name made lowercase.
    assemblyorderstatus = models.SmallIntegerField(db_column='AssemblyOrderStatus', blank=True, null=True)  # Field name made lowercase.
    lastopmodified = models.DateTimeField(db_column='LastOPModified', blank=True, null=True)  # Field name made lowercase.
    lastopmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastOPModifiedUserID', blank=True, null=True)  # Field name made lowercase.
    lastdrpmodified = models.DateTimeField(db_column='LastDRPModified', blank=True, null=True)  # Field name made lowercase.
    lastaorpmodified = models.DateTimeField(db_column='LastAORPModified', blank=True, null=True)  # Field name made lowercase.
    lastdrpmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastDRPModifiedUserID', blank=True, null=True)  # Field name made lowercase.
    lastaorpmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastAORPModifiedUserID', blank=True, null=True)  # Field name made lowercase.
    subtotalextax = models.DecimalField(db_column='SubTotalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtax = models.DecimalField(db_column='LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    batchno = models.CharField(db_column='BatchNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.
    ruleno = models.BigIntegerField(db_column='RuleNo', blank=True, null=True)  # Field name made lowercase.
    deliverydate = models.DateTimeField(db_column='DeliveryDate', blank=True, null=True)  # Field name made lowercase.
    taxableamt = models.DecimalField(db_column='TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxadjustment = models.DecimalField(db_column='TaxAdjustment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localsubtotalextax = models.DecimalField(db_column='LocalSubTotalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    extradiscountamt = models.DecimalField(db_column='ExtraDiscountAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxrate = models.DecimalField(db_column='TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    localtaxadjustment = models.DecimalField(db_column='LocalTaxAdjustment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtaxableamt = models.DecimalField(db_column='LocalTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytax = models.DecimalField(db_column='TaxCurrencyTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxableamt = models.DecimalField(db_column='TaxCurrencyTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    salesexemptionno = models.CharField(db_column='SalesExemptionNo', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'SODTL'


class Sstprocessor(models.Model):
    sstkey = models.BigAutoField(db_column='SSTKey', primary_key=True)  # Field name made lowercase.
    fromdate = models.DateTimeField(db_column='FromDate')  # Field name made lowercase.
    todate = models.DateTimeField(db_column='ToDate')  # Field name made lowercase.
    duration = models.SmallIntegerField(db_column='Duration')  # Field name made lowercase.
    submitted = models.CharField(db_column='Submitted', max_length=1)  # Field name made lowercase.
    taxdatareport = models.BinaryField(db_column='TaxDataReport', blank=True, null=True)  # Field name made lowercase.
    jedockey = models.BigIntegerField(db_column='JEDocKey', blank=True, null=True)  # Field name made lowercase.
    declarantname = models.CharField(db_column='DeclarantName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    icorpassportno = models.CharField(db_column='ICOrPassportNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    declarantdesignation = models.CharField(db_column='DeclarantDesignation', max_length=200, blank=True, null=True)  # Field name made lowercase.
    telephoneno = models.CharField(db_column='TelephoneNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    penaltyrate = models.DecimalField(db_column='PenaltyRate', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    compressed = models.CharField(db_column='Compressed', max_length=1)  # Field name made lowercase.
    parentsstkey = models.BigIntegerField(db_column='ParentSSTKey', blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq', blank=True, null=True)  # Field name made lowercase.
    productversion = models.CharField(db_column='ProductVersion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sstversion = models.IntegerField(db_column='SSTVersion')  # Field name made lowercase.
    declarationdate = models.DateTimeField(db_column='DeclarationDate', blank=True, null=True)  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp', blank=True, null=True)  # Field name made lowercase.
    createduserid = models.CharField(db_column='CreatedUserID', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'SSTProcessor'


class Sstsetting(models.Model):
    sstname = models.CharField(db_column='SSTName', primary_key=True, max_length=100)  # Field name made lowercase.
    sstvalue = models.CharField(db_column='SSTValue', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'SSTSetting'


class Salesagent(models.Model):
    salesagent = models.CharField(db_column='SalesAgent', primary_key=True, max_length=12)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=40, blank=True, null=True)  # Field name made lowercase.
    desc2 = models.CharField(db_column='Desc2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    isactive = models.CharField(db_column='IsActive', max_length=1)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    signature = models.BinaryField(db_column='Signature', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'SalesAgent'


class Serialnotrans(models.Model):
    transkey = models.BigIntegerField(db_column='TransKey', primary_key=True)  # Field name made lowercase.
    doctype = models.CharField(db_column='DocType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey', blank=True, null=True)  # Field name made lowercase.
    dtlkey = models.BigIntegerField(db_column='DtlKey', blank=True, null=True)  # Field name made lowercase.
    fromserialno = models.CharField(db_column='FromSerialNo', max_length=40, blank=True, null=True)  # Field name made lowercase.
    toserialno = models.CharField(db_column='ToSerialNo', max_length=40, blank=True, null=True)  # Field name made lowercase.
    count = models.BigIntegerField(db_column='Count', blank=True, null=True)  # Field name made lowercase.
    itemcode = models.ForeignKey(Item, models.DO_NOTHING, db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    transferedsn = models.TextField(db_column='TransferedSN', blank=True, null=True)  # Field name made lowercase.
    fromdocdtlkey = models.BigIntegerField(db_column='FromDocDtlKey', blank=True, null=True)  # Field name made lowercase.
    manufactureddate = models.DateTimeField(db_column='ManufacturedDate', blank=True, null=True)  # Field name made lowercase.
    expirydate = models.DateTimeField(db_column='ExpiryDate', blank=True, null=True)  # Field name made lowercase.
    lastsalesdate = models.DateTimeField(db_column='LastSalesDate', blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cancelled = models.CharField(db_column='Cancelled', max_length=1, blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'SerialNoTrans'


class Session(models.Model):
    sessionkey = models.AutoField(db_column='SessionKey', primary_key=True)  # Field name made lowercase.
    userid = models.CharField(db_column='UserID', max_length=10)  # Field name made lowercase.
    timestart = models.DateTimeField(db_column='TimeStart', blank=True, null=True)  # Field name made lowercase.
    timeend = models.DateTimeField(db_column='TimeEnd', blank=True, null=True)  # Field name made lowercase.
    computername = models.CharField(db_column='ComputerName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    privatekey = models.IntegerField(db_column='PrivateKey', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'Session'


class Shippingmethod(models.Model):
    shippingmethod = models.CharField(db_column='ShippingMethod', primary_key=True, max_length=20)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=40, blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    isactive = models.CharField(db_column='IsActive', max_length=1)  # Field name made lowercase.

    class Meta:
 
        db_table = 'ShippingMethod'


class Simplesyncsetting(models.Model):
    settingkey = models.BigIntegerField(db_column='SettingKey', primary_key=True)  # Field name made lowercase.
    server = models.CharField(db_column='Server', max_length=50, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=200, blank=True, null=True)  # Field name made lowercase.
    isdefaultpassword = models.CharField(db_column='IsDefaultPassword', max_length=1)  # Field name made lowercase.
    dbname = models.CharField(db_column='DBName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    loginuserid = models.CharField(db_column='LoginUserID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    loginpassword = models.CharField(db_column='LoginPassword', max_length=200, blank=True, null=True)  # Field name made lowercase.
    iscopypricebook = models.CharField(db_column='IsCopyPriceBook', max_length=1)  # Field name made lowercase.
    iscopyopening = models.CharField(db_column='IsCopyOpening', max_length=1)  # Field name made lowercase.
    iscopyqtfromserver = models.CharField(db_column='IsCopyQTFromServer', max_length=1)  # Field name made lowercase.
    iscopysofromserver = models.CharField(db_column='IsCopySOFromServer', max_length=1)  # Field name made lowercase.
    iscopydofromserver = models.CharField(db_column='IsCopyDOFromServer', max_length=1)  # Field name made lowercase.
    iscopyivfromserver = models.CharField(db_column='IsCopyIVFromServer', max_length=1)  # Field name made lowercase.
    iscopycsfromserver = models.CharField(db_column='IsCopyCSFromServer', max_length=1)  # Field name made lowercase.
    isexportqttoserver = models.CharField(db_column='IsExportQTToServer', max_length=1)  # Field name made lowercase.
    isexportsotoserver = models.CharField(db_column='IsExportSOToServer', max_length=1)  # Field name made lowercase.
    isexportdotoserver = models.CharField(db_column='IsExportDOToServer', max_length=1)  # Field name made lowercase.
    isexportivtoserver = models.CharField(db_column='IsExportIVToServer', max_length=1)  # Field name made lowercase.
    isexportcstoserver = models.CharField(db_column='IsExportCSToServer', max_length=1)  # Field name made lowercase.
    salesagentfiltercriteria = models.TextField(db_column='SalesAgentFilterCriteria', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'SimpleSyncSetting'


class Stockdtl(models.Model):
    stockdtlkey = models.BigIntegerField(db_column='StockDTLKey', primary_key=True)  # Field name made lowercase.
    itemcode = models.ForeignKey(Itemuom, models.DO_NOTHING, db_column='ItemCode')  # Field name made lowercase.
    uom = models.ForeignKey(Itemuom, models.DO_NOTHING, db_column='UOM')  # Field name made lowercase.
    location = models.ForeignKey(Location, models.DO_NOTHING, db_column='Location')  # Field name made lowercase.
    batchno = models.CharField(db_column='BatchNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey(Project, models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey(Dept, models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    seq = models.BigIntegerField(db_column='Seq')  # Field name made lowercase.
    doctype = models.CharField(db_column='DocType', max_length=2)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    dtlkey = models.BigIntegerField(db_column='DtlKey')  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=25, decimal_places=8)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=25, decimal_places=8)  # Field name made lowercase.
    adjustedcost = models.DecimalField(db_column='AdjustedCost', max_digits=25, decimal_places=8)  # Field name made lowercase.
    totalcost = models.DecimalField(db_column='TotalCost', max_digits=25, decimal_places=8)  # Field name made lowercase.
    costtype = models.SmallIntegerField(db_column='CostType')  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    referto = models.BigIntegerField(db_column='ReferTo')  # Field name made lowercase.
    inputcost = models.DecimalField(db_column='InputCost', max_digits=25, decimal_places=8)  # Field name made lowercase.

    class Meta:
 
        db_table = 'StockDTL'


class Stockdtlchangeq(models.Model):
    changeqkey = models.BigIntegerField(db_column='ChangeQKey', primary_key=True)  # Field name made lowercase.
    itemcode = models.ForeignKey(Item, models.DO_NOTHING, db_column='ItemCode')  # Field name made lowercase.
    stockdtlkey = models.BigIntegerField(db_column='StockDTLKey')  # Field name made lowercase.
    action = models.CharField(db_column='Action', max_length=1)  # Field name made lowercase.

    class Meta:
 
        db_table = 'StockDTLChangeQ'


class Stockpbalance(models.Model):
    stocksetkey = models.IntegerField(db_column='StockSetKey')  # Field name made lowercase.
    periodno = models.IntegerField(db_column='PeriodNo')  # Field name made lowercase.
    projno = models.ForeignKey(Project, models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey(Dept, models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    balance = models.DecimalField(db_column='Balance', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'StockPBalance'


class Stockset(models.Model):
    stocksetkey = models.IntegerField(db_column='StockSetKey', primary_key=True)  # Field name made lowercase.
    openstock = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='OpenStock')  # Field name made lowercase.
    closestock = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='CloseStock')  # Field name made lowercase.
    balancestock = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='BalanceStock')  # Field name made lowercase.

    class Meta:
 
        db_table = 'StockSet'


class Suppliercsgn(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', unique=True, max_length=20)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    creditorcode = models.ForeignKey(Branch, models.DO_NOTHING, db_column='CreditorCode')  # Field name made lowercase.
    creditorname = models.CharField(db_column='CreditorName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    supplierdono = models.CharField(db_column='SupplierDONo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ref = models.CharField(db_column='Ref', max_length=40, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=60, blank=True, null=True)  # Field name made lowercase.
    purchaseagent = models.ForeignKey(Purchaseagent, models.DO_NOTHING, db_column='PurchaseAgent', blank=True, null=True)  # Field name made lowercase.
    invaddr1 = models.CharField(db_column='InvAddr1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr2 = models.CharField(db_column='InvAddr2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr3 = models.CharField(db_column='InvAddr3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr4 = models.CharField(db_column='InvAddr4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    phone1 = models.CharField(db_column='Phone1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    fax1 = models.CharField(db_column='Fax1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    attention = models.CharField(db_column='Attention', max_length=40, blank=True, null=True)  # Field name made lowercase.
    branchcode = models.ForeignKey(Branch, models.DO_NOTHING, db_column='BranchCode', blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    remark1 = models.CharField(db_column='Remark1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark2 = models.CharField(db_column='Remark2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark3 = models.CharField(db_column='Remark3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark4 = models.CharField(db_column='Remark4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    printcount = models.SmallIntegerField(db_column='PrintCount')  # Field name made lowercase.
    cancelled = models.CharField(db_column='Cancelled', max_length=1)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    createduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    externallink = models.TextField(db_column='ExternalLink', blank=True, null=True)  # Field name made lowercase.
    refdocno = models.CharField(db_column='RefDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    cansync = models.CharField(db_column='CanSync', max_length=1)  # Field name made lowercase.
    sourcetype = models.CharField(db_column='SourceType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    sourcekey = models.BigIntegerField(db_column='SourceKey', blank=True, null=True)  # Field name made lowercase.
    shipvia = models.ForeignKey(Shippingmethod, models.DO_NOTHING, db_column='ShipVia', blank=True, null=True)  # Field name made lowercase.
    shipinfo = models.CharField(db_column='ShipInfo', max_length=40, blank=True, null=True)  # Field name made lowercase.
    purchaselocation = models.ForeignKey(Location, models.DO_NOTHING, db_column='PurchaseLocation', blank=True, null=True)  # Field name made lowercase.
    nettotal = models.DecimalField(db_column='NetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.

    class Meta:
 
        db_table = 'SupplierCSGN'


class Suppliercsgndtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    itemcode = models.ForeignKey(Itemuom, models.DO_NOTHING, db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    uom = models.ForeignKey(Itemuom, models.DO_NOTHING, db_column='UOM', blank=True, null=True)  # Field name made lowercase.
    location = models.ForeignKey(Location, models.DO_NOTHING, db_column='Location', blank=True, null=True)  # Field name made lowercase.
    batchno = models.ForeignKey(Itembatch, models.DO_NOTHING, db_column='BatchNo', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
    furtherdescription = models.TextField(db_column='FurtherDescription', blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey(Project, models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey(Dept, models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    serialnolist = models.TextField(db_column='SerialNoList', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    discount = models.CharField(db_column='Discount', max_length=20, blank=True, null=True)  # Field name made lowercase.
    discountamt = models.DecimalField(db_column='DiscountAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.

    class Meta:
 
        db_table = 'SupplierCSGNDTL'


class Synccriteriaprofile(models.Model):
    criteriakey = models.BigIntegerField(db_column='CriteriaKey', primary_key=True)  # Field name made lowercase.
    criterianame = models.CharField(db_column='CriteriaName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    itemcodefilter = models.TextField(db_column='ItemCodeFilter', blank=True, null=True)  # Field name made lowercase.
    locationfilter = models.TextField(db_column='LocationFilter', blank=True, null=True)  # Field name made lowercase.
    masterdirect = models.IntegerField(db_column='MasterDirect', blank=True, null=True)  # Field name made lowercase.
    qtdirect = models.IntegerField(db_column='QTDirect', blank=True, null=True)  # Field name made lowercase.
    sodirect = models.IntegerField(db_column='SODirect', blank=True, null=True)  # Field name made lowercase.
    dodirect = models.IntegerField(db_column='DODirect', blank=True, null=True)  # Field name made lowercase.
    ivdirect = models.IntegerField(db_column='IVDirect', blank=True, null=True)  # Field name made lowercase.
    csdirect = models.IntegerField(db_column='CSDirect', blank=True, null=True)  # Field name made lowercase.
    cndirect = models.IntegerField(db_column='CNDirect', blank=True, null=True)  # Field name made lowercase.
    dndirect = models.IntegerField(db_column='DNDirect', blank=True, null=True)  # Field name made lowercase.
    drdirect = models.IntegerField(db_column='DRDirect', blank=True, null=True)  # Field name made lowercase.
    xsdirect = models.IntegerField(db_column='XSDirect', blank=True, null=True)  # Field name made lowercase.
    rqdirect = models.IntegerField(db_column='RQDirect', blank=True, null=True)  # Field name made lowercase.
    podirect = models.IntegerField(db_column='PODirect', blank=True, null=True)  # Field name made lowercase.
    grdirect = models.IntegerField(db_column='GRDirect', blank=True, null=True)  # Field name made lowercase.
    pidirect = models.IntegerField(db_column='PIDirect', blank=True, null=True)  # Field name made lowercase.
    cpdirect = models.IntegerField(db_column='CPDirect', blank=True, null=True)  # Field name made lowercase.
    prdirect = models.IntegerField(db_column='PRDirect', blank=True, null=True)  # Field name made lowercase.
    gtdirect = models.IntegerField(db_column='GTDirect', blank=True, null=True)  # Field name made lowercase.
    xpdirect = models.IntegerField(db_column='XPDirect', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'SyncCriteriaProfile'


class Syncprofile(models.Model):
    profilekey = models.BigIntegerField(db_column='ProfileKey', primary_key=True)  # Field name made lowercase.
    profilename = models.CharField(db_column='ProfileName', max_length=50)  # Field name made lowercase.
    uri = models.CharField(db_column='URI', max_length=255)  # Field name made lowercase.
    portnumber = models.IntegerField(db_column='PortNumber')  # Field name made lowercase.
    encryptionkey = models.CharField(db_column='EncryptionKey', max_length=100)  # Field name made lowercase.
    serverpassword = models.CharField(db_column='ServerPassword', max_length=50, blank=True, null=True)  # Field name made lowercase.
    synccriteriaprofilekey = models.BigIntegerField(db_column='SyncCriteriaProfileKey')  # Field name made lowercase.

    class Meta:
 
        db_table = 'SyncProfile'


class Tariff(models.Model):
    tariffcode = models.CharField(db_column='TariffCode', primary_key=True, max_length=12)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    desc2 = models.CharField(db_column='Desc2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    isactive = models.CharField(db_column='IsActive', max_length=1)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.

    class Meta:
 
        db_table = 'Tariff'


class Taxdocno(models.Model):
    taxdocnokey = models.AutoField(db_column='TaxDocNoKey', primary_key=True)  # Field name made lowercase.
    nextnumber = models.BigIntegerField(db_column='NextNumber', blank=True, null=True)  # Field name made lowercase.
    fromnumber = models.BigIntegerField(db_column='FromNumber')  # Field name made lowercase.
    tonumber = models.BigIntegerField(db_column='ToNumber')  # Field name made lowercase.
    count = models.IntegerField(db_column='Count')  # Field name made lowercase.
    usecount = models.IntegerField(db_column='UseCount')  # Field name made lowercase.
    voidcount = models.IntegerField(db_column='VoidCount')  # Field name made lowercase.
    fromdate = models.DateTimeField(db_column='FromDate', blank=True, null=True)  # Field name made lowercase.
    todate = models.DateTimeField(db_column='ToDate', blank=True, null=True)  # Field name made lowercase.
    format = models.CharField(db_column='Format', max_length=30)  # Field name made lowercase.
    isdefault = models.CharField(db_column='IsDefault', max_length=1)  # Field name made lowercase.

    class Meta:
 
        db_table = 'TaxDocNo'


class Taxdocnodtl(models.Model):
    taxdocnodtlkey = models.BigAutoField(db_column='TaxDocNoDTLKey', primary_key=True)  # Field name made lowercase.
    taxdocnokey = models.IntegerField(db_column='TaxDocNoKey')  # Field name made lowercase.
    number = models.CharField(db_column='Number', max_length=20)  # Field name made lowercase.
    useindoctype = models.CharField(db_column='UseInDocType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    useindockey = models.BigIntegerField(db_column='UseInDocKey', blank=True, null=True)  # Field name made lowercase.
    useindocno = models.CharField(db_column='UseInDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    void = models.CharField(db_column='Void', max_length=1)  # Field name made lowercase.

    class Meta:
 
        db_table = 'TaxDocNoDTL'


class Taxexemption(models.Model):
    accno = models.CharField(db_column='AccNo', primary_key=True, max_length=12)  # Field name made lowercase.
    itemcode = models.CharField(db_column='ItemCode', max_length=30)  # Field name made lowercase.
    salesexemptionno = models.CharField(db_column='SalesExemptionNo', max_length=60)  # Field name made lowercase.
    taxtype = models.CharField(db_column='TaxType', max_length=14)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.

    class Meta:
 
        db_table = 'TaxExemption'
        unique_together = (('accno', 'itemcode'),)


class Taxtrans(models.Model):
    taxtranskey = models.BigAutoField(db_column='TaxTransKey', primary_key=True)  # Field name made lowercase.
    sourcetype = models.CharField(db_column='SourceType', max_length=2)  # Field name made lowercase.
    sourcekey = models.BigIntegerField(db_column='SourceKey')  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', max_length=20)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='TaxType')  # Field name made lowercase.
    supplypurchase = models.CharField(db_column='SupplyPurchase', max_length=1)  # Field name made lowercase.
    projno = models.ForeignKey(Project, models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey(Dept, models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    taxableaccno = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='TaxableAccNo', blank=True, null=True)  # Field name made lowercase.
    taxablename = models.CharField(db_column='TaxableName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    taxableamt = models.DecimalField(db_column='TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtaxableamt = models.DecimalField(db_column='LocalTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtax = models.DecimalField(db_column='LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sourcedtlkey = models.BigIntegerField(db_column='SourceDtlKey', blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq', blank=True, null=True)  # Field name made lowercase.
    currencycode = models.ForeignKey(Currency, models.DO_NOTHING, db_column='CurrencyCode')  # Field name made lowercase.
    currencyrate = models.DecimalField(db_column='CurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    taxrate = models.DecimalField(db_column='TaxRate', max_digits=18, decimal_places=6)  # Field name made lowercase.
    taxaccno = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='TaxAccNo', blank=True, null=True)  # Field name made lowercase.
    taxdate = models.DateTimeField(db_column='TaxDate')  # Field name made lowercase.
    registerno = models.CharField(db_column='RegisterNo', max_length=25, blank=True, null=True)  # Field name made lowercase.
    taxregisterno = models.CharField(db_column='TaxRegisterNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    taxrefno = models.CharField(db_column='TaxRefNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    taxpermitno = models.CharField(db_column='TaxPermitNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    taxexportcountry = models.CharField(db_column='TaxExportCountry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    originaldtlkey = models.BigIntegerField(db_column='OriginalDtlKey', blank=True, null=True)  # Field name made lowercase.
    originaldtltype = models.CharField(db_column='OriginalDtlType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tariffcode = models.ForeignKey(Tariff, models.DO_NOTHING, db_column='TariffCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'TaxTrans'


class Taxtransaudit(models.Model):
    taxtransauditkey = models.BigAutoField(db_column='TaxTransAuditKey', primary_key=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime')  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.

    class Meta:
 
        db_table = 'TaxTransAudit'


class Taxtransauditdtl(models.Model):
    taxtransauditdtlkey = models.BigAutoField(db_column='TaxTransAuditDtlKey', primary_key=True)  # Field name made lowercase.
    taxtransauditkey = models.BigIntegerField(db_column='TaxTransAuditKey')  # Field name made lowercase.
    taxtranskey = models.BigIntegerField(db_column='TaxTransKey')  # Field name made lowercase.
    sourcetype = models.CharField(db_column='SourceType', max_length=2)  # Field name made lowercase.
    sourcekey = models.BigIntegerField(db_column='SourceKey')  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', max_length=20)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='TaxType')  # Field name made lowercase.
    supplypurchase = models.CharField(db_column='SupplyPurchase', max_length=1)  # Field name made lowercase.
    projno = models.ForeignKey(Project, models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey(Dept, models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    taxableaccno = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='TaxableAccNo', blank=True, null=True)  # Field name made lowercase.
    taxablename = models.CharField(db_column='TaxableName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    taxableamt = models.DecimalField(db_column='TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtaxableamt = models.DecimalField(db_column='LocalTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtax = models.DecimalField(db_column='LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sourcedtlkey = models.BigIntegerField(db_column='SourceDtlKey', blank=True, null=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq', blank=True, null=True)  # Field name made lowercase.
    currencycode = models.ForeignKey(Currency, models.DO_NOTHING, db_column='CurrencyCode')  # Field name made lowercase.
    currencyrate = models.DecimalField(db_column='CurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    taxrate = models.DecimalField(db_column='TaxRate', max_digits=18, decimal_places=6)  # Field name made lowercase.
    taxaccno = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='TaxAccNo', blank=True, null=True)  # Field name made lowercase.
    taxdate = models.DateTimeField(db_column='TaxDate')  # Field name made lowercase.
    registerno = models.CharField(db_column='RegisterNo', max_length=25, blank=True, null=True)  # Field name made lowercase.
    taxregisterno = models.CharField(db_column='TaxRegisterNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    taxrefno = models.CharField(db_column='TaxRefNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    taxpermitno = models.CharField(db_column='TaxPermitNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    taxexportcountry = models.CharField(db_column='TaxExportCountry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    originaldtlkey = models.BigIntegerField(db_column='OriginalDtlKey', blank=True, null=True)  # Field name made lowercase.
    originaldtltype = models.CharField(db_column='OriginalDtlType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    action = models.SmallIntegerField(db_column='Action')  # Field name made lowercase.
    severity = models.SmallIntegerField(db_column='Severity')  # Field name made lowercase.
    tariffcode = models.ForeignKey(Tariff, models.DO_NOTHING, db_column='TariffCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'TaxTransAuditDTL'


class Taxtype(models.Model):
    taxtype = models.CharField(db_column='TaxType', primary_key=True, max_length=14)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=120, blank=True, null=True)  # Field name made lowercase.
    taxrate = models.DecimalField(db_column='TaxRate', max_digits=18, decimal_places=6)  # Field name made lowercase.
    inclusive = models.CharField(db_column='Inclusive', max_length=1)  # Field name made lowercase.
    isactive = models.CharField(db_column='IsActive', max_length=1)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    taxtypecategory = models.CharField(db_column='TaxTypeCategory', max_length=40, blank=True, null=True)  # Field name made lowercase.
    irastaxcode = models.CharField(db_column='IRASTaxCode', max_length=8, blank=True, null=True)  # Field name made lowercase.
    supplypurchase = models.CharField(db_column='SupplyPurchase', max_length=1)  # Field name made lowercase.
    isdefault = models.CharField(db_column='IsDefault', max_length=1)  # Field name made lowercase.
    taxaccno = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='TaxAccNo', blank=True, null=True)  # Field name made lowercase.
    iszerorate = models.CharField(db_column='IsZeroRate', max_length=1)  # Field name made lowercase.
    usetrxtaxaccno = models.CharField(db_column='UseTrxTaxAccNo', max_length=1)  # Field name made lowercase.
    accountingbasis = models.IntegerField(db_column='AccountingBasis')  # Field name made lowercase.
    addtocost = models.CharField(db_column='AddToCost', max_length=1)  # Field name made lowercase.

    class Meta:
 
        db_table = 'TaxType'


class Tempdocument(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    doctype = models.CharField(db_column='DocType', max_length=2)  # Field name made lowercase.
    savetime = models.DateTimeField(db_column='SaveTime')  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    userid = models.CharField(db_column='UserID', max_length=10)  # Field name made lowercase.
    savereason = models.CharField(db_column='SaveReason', max_length=20, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=80, blank=True, null=True)  # Field name made lowercase.
    compressed = models.CharField(db_column='Compressed', max_length=1)  # Field name made lowercase.
    data = models.BinaryField(db_column='Data', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'TempDocument'


class Temporarycredit(models.Model):
    accno = models.OneToOneField(Glmast, models.DO_NOTHING, db_column='AccNo', primary_key=True)  # Field name made lowercase.
    fromdate = models.DateTimeField(db_column='FromDate')  # Field name made lowercase.
    todate = models.DateTimeField(db_column='ToDate')  # Field name made lowercase.
    creditlimit = models.DecimalField(db_column='CreditLimit', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    overduelimit = models.DecimalField(db_column='OverdueLimit', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'TemporaryCredit'
        unique_together = (('accno', 'fromdate', 'todate'),)


class Terminal(models.Model):
    name = models.CharField(db_column='Name', max_length=8)  # Field name made lowercase.
    outlet = models.ForeignKey(Location, models.DO_NOTHING, db_column='Outlet', blank=True, null=True)  # Field name made lowercase.
    machine = models.CharField(db_column='Machine', primary_key=True, max_length=50)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    format = models.CharField(db_column='Format', unique=True, max_length=20)  # Field name made lowercase.
    nextnumber = models.IntegerField(db_column='NextNumber')  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.

    class Meta:
 
        db_table = 'Terminal'
        unique_together = (('name', 'outlet'),)


class Terms(models.Model):
    displayterm = models.CharField(db_column='DisplayTerm', primary_key=True, max_length=30)  # Field name made lowercase.
    terms = models.CharField(db_column='Terms', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    termtype = models.CharField(db_column='TermType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    termdays = models.IntegerField(db_column='TermDays', blank=True, null=True)  # Field name made lowercase.
    discountdays = models.IntegerField(db_column='DiscountDays', blank=True, null=True)  # Field name made lowercase.
    discountpercent = models.DecimalField(db_column='DiscountPercent', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'Terms'


class Udf(models.Model):
    tablename = models.CharField(db_column='TableName', primary_key=True, max_length=25)  # Field name made lowercase.
    fieldname = models.CharField(db_column='FieldName', max_length=10)  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    fieldtype = models.CharField(db_column='FieldType', max_length=1)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=80, blank=True, null=True)  # Field name made lowercase.
    properties = models.TextField(db_column='Properties', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'UDF'
        unique_together = (('tablename', 'fieldname'),)


class Udflayout(models.Model):
    tablename = models.CharField(db_column='TableName', primary_key=True, max_length=25)  # Field name made lowercase.
    layoutname = models.CharField(db_column='LayoutName', max_length=10)  # Field name made lowercase.
    layout = models.TextField(db_column='Layout', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'UDFLayout'
        unique_together = (('tablename', 'layoutname'),)


class Udflist(models.Model):
    name = models.CharField(db_column='Name', primary_key=True, max_length=10)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'UDFList'


class Uomconv(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', unique=True, max_length=20)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    printcount = models.SmallIntegerField(db_column='PrintCount')  # Field name made lowercase.
    cancelled = models.CharField(db_column='Cancelled', max_length=1)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    createduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    fromdoctype = models.CharField(db_column='FromDocType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    fromdockey = models.BigIntegerField(db_column='FromDocKey', blank=True, null=True)  # Field name made lowercase.
    fromdocno = models.CharField(db_column='FromDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    cansync = models.CharField(db_column='CanSync', max_length=1)  # Field name made lowercase.

    class Meta:
 
        db_table = 'UOMConv'


class Uomconvdtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    indtlkey = models.BigIntegerField(db_column='InDtlKey')  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    itemcode = models.ForeignKey(Itemuom, models.DO_NOTHING, db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    location = models.ForeignKey(Location, models.DO_NOTHING, db_column='Location', blank=True, null=True)  # Field name made lowercase.
    batchno = models.ForeignKey(Itembatch, models.DO_NOTHING, db_column='BatchNo', blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey(Project, models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey(Dept, models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    fromqty = models.DecimalField(db_column='FromQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    fromuom = models.ForeignKey(Itemuom, models.DO_NOTHING, db_column='FromUOM', blank=True, null=True)  # Field name made lowercase.
    touom = models.ForeignKey(Itemuom, models.DO_NOTHING, db_column='ToUOM', blank=True, null=True)  # Field name made lowercase.
    toqty = models.DecimalField(db_column='ToQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'UOMConvDTL'


class Utdstockcost(models.Model):
    utdstockcostkey = models.BigIntegerField(db_column='UTDStockCostKey', primary_key=True)  # Field name made lowercase.
    itemcode = models.ForeignKey(Itemuom, models.DO_NOTHING, db_column='ItemCode')  # Field name made lowercase.
    uom = models.ForeignKey(Itemuom, models.DO_NOTHING, db_column='UOM')  # Field name made lowercase.
    location = models.ForeignKey(Location, models.DO_NOTHING, db_column='Location')  # Field name made lowercase.
    batchno = models.ForeignKey(Itembatch, models.DO_NOTHING, db_column='BatchNo', blank=True, null=True)  # Field name made lowercase.
    utdqty = models.DecimalField(db_column='UTDQty', max_digits=25, decimal_places=8)  # Field name made lowercase.
    utdcost = models.DecimalField(db_column='UTDCost', max_digits=25, decimal_places=8)  # Field name made lowercase.
    adjustedcost = models.DecimalField(db_column='AdjustedCost', max_digits=25, decimal_places=8)  # Field name made lowercase.
    averagecost = models.DecimalField(db_column='AverageCost', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'UTDStockCost'


class Utdstockcostdtl(models.Model):
    utdstockcostdtlkey = models.BigAutoField(db_column='UTDStockCostDTLKey', primary_key=True)  # Field name made lowercase.
    utdstockcostkey = models.BigIntegerField(db_column='UTDStockCostKey')  # Field name made lowercase.
    seq = models.SmallIntegerField(db_column='Seq')  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=25, decimal_places=8)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=25, decimal_places=8)  # Field name made lowercase.

    class Meta:
 
        db_table = 'UTDStockCostDTL'


class Unapproveddocument(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    doctype = models.CharField(db_column='DocType', max_length=2)  # Field name made lowercase.
    savetime = models.DateTimeField(db_column='SaveTime')  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', max_length=20)  # Field name made lowercase.
    accno = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='AccNo', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    nettotal = models.DecimalField(db_column='NetTotal', max_digits=19, decimal_places=2)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=80, blank=True, null=True)  # Field name made lowercase.
    data = models.BinaryField(db_column='Data', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'UnapprovedDocument'


class Unrealizedgainloss(models.Model):
    unrealizedgainlosskey = models.BigIntegerField(db_column='UnrealizedGainLossKey', primary_key=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', max_length=20)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    unrealizedgainaccount = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='UnrealizedGainAccount')  # Field name made lowercase.
    unrealizedlossaccount = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='UnrealizedLossAccount')  # Field name made lowercase.
    gainlossjournaltype = models.ForeignKey(Journal, models.DO_NOTHING, db_column='GainLossJournalType')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    totalgainloss = models.DecimalField(db_column='TotalGainLoss', max_digits=19, decimal_places=2)  # Field name made lowercase.
    jekey = models.BigIntegerField(db_column='JEKey', blank=True, null=True)  # Field name made lowercase.
    printcount = models.SmallIntegerField(db_column='PrintCount', blank=True, null=True)  # Field name made lowercase.
    refcount = models.BigIntegerField(db_column='RefCount')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    createduserid = models.CharField(db_column='CreatedUserID', max_length=10)  # Field name made lowercase.
    usesinglegainlossaccount = models.CharField(db_column='UseSingleGainLossAccount', max_length=1)  # Field name made lowercase.
    glgainaccount = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='GLGainAccount', blank=True, null=True)  # Field name made lowercase.
    gllossaccount = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='GLLossAccount', blank=True, null=True)  # Field name made lowercase.
    jekey2 = models.BigIntegerField(db_column='JEKey2', blank=True, null=True)  # Field name made lowercase.
    docno2 = models.CharField(db_column='DocNo2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reverseglposting = models.CharField(db_column='ReverseGLPosting', max_length=1)  # Field name made lowercase.
    gltrxid = models.BigIntegerField(db_column='GLTrxID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'UnrealizedGainLoss'


class Unrealizedgainlossdocument(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    unrealizedgainlosskey = models.BigIntegerField(db_column='UnrealizedGainLossKey')  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=2)  # Field name made lowercase.
    doctype = models.CharField(db_column='DocType', max_length=2)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', max_length=20)  # Field name made lowercase.
    accno = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='AccNo')  # Field name made lowercase.
    companyname = models.CharField(db_column='CompanyName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    currencycode = models.ForeignKey(Currency, models.DO_NOTHING, db_column='CurrencyCode')  # Field name made lowercase.
    newrate = models.DecimalField(db_column='NewRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    currencyrate = models.DecimalField(db_column='CurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    outstanding = models.DecimalField(db_column='Outstanding', max_digits=19, decimal_places=2)  # Field name made lowercase.
    gainloss = models.DecimalField(db_column='GainLoss', max_digits=19, decimal_places=2)  # Field name made lowercase.
    projno = models.ForeignKey(Project, models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey(Dept, models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'UnrealizedGainLossDocument'


class Unrealizedgainlossglaccount(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    unrealizedgainlosskey = models.BigIntegerField(db_column='UnrealizedGainLossKey')  # Field name made lowercase.
    accno = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='AccNo')  # Field name made lowercase.
    revaluerate = models.DecimalField(db_column='RevalueRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    balance = models.DecimalField(db_column='Balance', max_digits=19, decimal_places=2)  # Field name made lowercase.
    newhomebalance = models.DecimalField(db_column='NewHomeBalance', max_digits=19, decimal_places=2)  # Field name made lowercase.
    homebalance = models.DecimalField(db_column='HomeBalance', max_digits=19, decimal_places=2)  # Field name made lowercase.
    gainloss = models.DecimalField(db_column='GainLoss', max_digits=19, decimal_places=2)  # Field name made lowercase.

    class Meta:
 
        db_table = 'UnrealizedGainLossGLAccount'


class Unrealizedgainlossrate(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    unrealizedgainlosskey = models.BigIntegerField(db_column='UnrealizedGainLossKey')  # Field name made lowercase.
    currencycode = models.ForeignKey(Currency, models.DO_NOTHING, db_column='CurrencyCode')  # Field name made lowercase.
    bankbuyrate = models.DecimalField(db_column='BankBuyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    unrealizedgainaccount = models.CharField(db_column='UnrealizedGainAccount', max_length=12, blank=True, null=True)  # Field name made lowercase.
    unrealizedlossaccount = models.CharField(db_column='UnrealizedLossAccount', max_length=12, blank=True, null=True)  # Field name made lowercase.
    glgainaccount = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='GLGainAccount', blank=True, null=True)  # Field name made lowercase.
    gllossaccount = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='GLLossAccount', blank=True, null=True)  # Field name made lowercase.
    banksellrate = models.DecimalField(db_column='BankSellRate', max_digits=19, decimal_places=12)  # Field name made lowercase.

    class Meta:
 
        db_table = 'UnrealizedGainLossRate'


class Updatecost(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', unique=True, max_length=20)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    printcount = models.SmallIntegerField(db_column='PrintCount')  # Field name made lowercase.
    cancelled = models.CharField(db_column='Cancelled', max_length=1)  # Field name made lowercase.
    updatetorealcost = models.CharField(db_column='UpdateToRealCost', max_length=1)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    createduserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.

    class Meta:
 
        db_table = 'UpdateCost'


class Updatecostdtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    itemcode = models.ForeignKey(Itemuom, models.DO_NOTHING, db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    uom = models.ForeignKey(Itemuom, models.DO_NOTHING, db_column='UOM', blank=True, null=True)  # Field name made lowercase.
    oldcost = models.DecimalField(db_column='OldCost', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    newcost = models.DecimalField(db_column='NewCost', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'UpdateCostDTL'


class Usergroup(models.Model):
    usergroupid = models.CharField(db_column='UserGroupID', primary_key=True, max_length=10)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=40, blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.

    class Meta:
 
        db_table = 'UserGroup'


class Userscript(models.Model):
    scriptname = models.CharField(db_column='ScriptName', primary_key=True, max_length=60)  # Field name made lowercase.
    language = models.CharField(db_column='Language', max_length=5)  # Field name made lowercase.
    script = models.TextField(db_column='Script', blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.

    class Meta:
 
        db_table = 'UserScript'


class Users(models.Model):
    userid = models.CharField(db_column='UserID', primary_key=True, max_length=10)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=40, blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=30, blank=True, null=True)  # Field name made lowercase.
    passwd = models.CharField(db_column='Passwd', max_length=112, blank=True, null=True)  # Field name made lowercase.
    signature = models.BinaryField(db_column='Signature', blank=True, null=True)  # Field name made lowercase.
    emailaddress = models.CharField(db_column='EmailAddress', max_length=80, blank=True, null=True)  # Field name made lowercase.
    filterbysalesagent = models.CharField(db_column='FilterBySalesAgent', max_length=1)  # Field name made lowercase.
    filterbypurchaseagent = models.CharField(db_column='FilterByPurchaseAgent', max_length=1)  # Field name made lowercase.
    isactive = models.CharField(db_column='IsActive', max_length=1)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    mainpage = models.TextField(db_column='MainPage', blank=True, null=True)  # Field name made lowercase.
    passwordage = models.IntegerField(db_column='PasswordAge')  # Field name made lowercase.
    lastpassworddate = models.DateTimeField(db_column='LastPasswordDate', blank=True, null=True)  # Field name made lowercase.
    location = models.ForeignKey(Location, models.DO_NOTHING, db_column='Location', blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey(Project, models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey(Dept, models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    isexportdebtortobranch = models.CharField(db_column='IsExportDebtorToBranch', max_length=1)  # Field name made lowercase.
    isexportcreditortobranch = models.CharField(db_column='IsExportCreditorToBranch', max_length=1)  # Field name made lowercase.
    isexportitemtobranch = models.CharField(db_column='IsExportItemToBranch', max_length=1)  # Field name made lowercase.
    isexportpricehistorytobranch = models.CharField(db_column='IsExportPriceHistoryToBranch', max_length=1)  # Field name made lowercase.
    isexportqttobranch = models.CharField(db_column='IsExportQTToBranch', max_length=1)  # Field name made lowercase.
    isexportsotobranch = models.CharField(db_column='IsExportSOToBranch', max_length=1)  # Field name made lowercase.
    isexportdotobranch = models.CharField(db_column='IsExportDOToBranch', max_length=1)  # Field name made lowercase.
    isexportivtobranch = models.CharField(db_column='IsExportIVToBranch', max_length=1)  # Field name made lowercase.
    isexportcstobranch = models.CharField(db_column='IsExportCSToBranch', max_length=1)  # Field name made lowercase.
    posmainpage = models.TextField(db_column='POSMainPage', blank=True, null=True)  # Field name made lowercase.
    salescreditlimitincrementpercentage = models.DecimalField(db_column='SalesCreditLimitIncrementPercentage', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    salesoverduelimitincrementpercentage = models.DecimalField(db_column='SalesOverdueLimitIncrementPercentage', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    purchasecreditlimitincrementpercentage = models.DecimalField(db_column='PurchaseCreditLimitIncrementPercentage', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    purchaseoverduelimitincrementpercentage = models.DecimalField(db_column='PurchaseOverdueLimitIncrementPercentage', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    filteredbycreateduserid = models.CharField(db_column='FilteredByCreatedUserID', max_length=1, blank=True, null=True)  # Field name made lowercase.
    filteredbylastmodifieduserid = models.CharField(db_column='FilteredByLastModifiedUserID', max_length=1, blank=True, null=True)  # Field name made lowercase.
    passwordstrength = models.CharField(db_column='PasswordStrength', max_length=1, blank=True, null=True)  # Field name made lowercase.
    usertype = models.CharField(db_column='UserType', max_length=1)  # Field name made lowercase.
    filterbyaccno = models.CharField(db_column='FilterByAccNo', max_length=1)  # Field name made lowercase.

    class Meta:
 
        db_table = 'Users'


class Usersaccno(models.Model):
    userid = models.CharField(db_column='UserID', primary_key=True, max_length=10)  # Field name made lowercase.
    accno = models.CharField(db_column='AccNo', max_length=12)  # Field name made lowercase.

    class Meta:
 
        db_table = 'UsersAccNo'
        unique_together = (('userid', 'accno'),)


class Usersgroup(models.Model):
    userid = models.CharField(db_column='UserID', primary_key=True, max_length=10)  # Field name made lowercase.
    usergroupid = models.ForeignKey(Usergroup, models.DO_NOTHING, db_column='UserGroupID')  # Field name made lowercase.

    class Meta:
 
        db_table = 'UsersGroup'
        unique_together = (('userid', 'usergroupid'),)


class Userspurchaseagent(models.Model):
    userid = models.CharField(db_column='UserID', primary_key=True, max_length=10)  # Field name made lowercase.
    purchaseagent = models.CharField(db_column='PurchaseAgent', max_length=12)  # Field name made lowercase.

    class Meta:
 
        db_table = 'UsersPurchaseAgent'
        unique_together = (('userid', 'purchaseagent'),)


class Userssalesagent(models.Model):
    userid = models.CharField(db_column='UserID', primary_key=True, max_length=10)  # Field name made lowercase.
    salesagent = models.CharField(db_column='SalesAgent', max_length=12)  # Field name made lowercase.

    class Meta:
 
        db_table = 'UsersSalesAgent'
        unique_together = (('userid', 'salesagent'),)


class Woff(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', unique=True, max_length=20)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    remark1 = models.CharField(db_column='Remark1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark2 = models.CharField(db_column='Remark2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark3 = models.CharField(db_column='Remark3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark4 = models.CharField(db_column='Remark4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    printcount = models.SmallIntegerField(db_column='PrintCount')  # Field name made lowercase.
    cancelled = models.CharField(db_column='Cancelled', max_length=1)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey(Users, models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    createduserid = models.ForeignKey(Users, models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    externallink = models.TextField(db_column='ExternalLink', blank=True, null=True)  # Field name made lowercase.
    refdocno = models.CharField(db_column='RefDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    cansync = models.CharField(db_column='CanSync', max_length=1)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.

    class Meta:
 
        db_table = 'WOFF'


class Woffdtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    numbering = models.CharField(db_column='Numbering', max_length=6, blank=True, null=True)  # Field name made lowercase.
    itemcode = models.ForeignKey(Itemuom, models.DO_NOTHING, db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    location = models.ForeignKey(Location, models.DO_NOTHING, db_column='Location', blank=True, null=True)  # Field name made lowercase.
    batchno = models.ForeignKey(Itembatch, models.DO_NOTHING, db_column='BatchNo', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    furtherdescription = models.TextField(db_column='FurtherDescription', blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey(Project, models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey(Dept, models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    uom = models.ForeignKey(Itemuom, models.DO_NOTHING, db_column='UOM', blank=True, null=True)  # Field name made lowercase.
    unitcost = models.DecimalField(db_column='UnitCost', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    printout = models.CharField(db_column='PrintOut', max_length=1)  # Field name made lowercase.
    serialnolist = models.TextField(db_column='SerialNoList', blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.

    class Meta:
 
        db_table = 'WOFFDTL'


class Withholdingtax(models.Model):
    withholdingtaxcode = models.CharField(db_column='WithholdingTaxCode', primary_key=True, max_length=14)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=80, blank=True, null=True)  # Field name made lowercase.
    withholdingtaxrate = models.DecimalField(db_column='WithholdingTaxRate', max_digits=18, decimal_places=6)  # Field name made lowercase.
    withholdingtaxaccno = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='WithholdingTaxAccNo')  # Field name made lowercase.
    isactive = models.CharField(db_column='IsActive', max_length=1)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    receiptpayment = models.CharField(db_column='ReceiptPayment', max_length=1)  # Field name made lowercase.
    isdefault = models.CharField(db_column='IsDefault', max_length=1)  # Field name made lowercase.

    class Meta:
 
        db_table = 'WithholdingTax'


class Withholdingtaxdocdtl(models.Model):
    taxdocdtlkey = models.BigIntegerField(db_column='TaxDocDtlKey', primary_key=True)  # Field name made lowercase.
    doctype = models.CharField(db_column='DocType', max_length=2)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    dtlkey = models.BigIntegerField(db_column='DtlKey')  # Field name made lowercase.
    paymentamt = models.DecimalField(db_column='PaymentAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    withholdingtaxcode = models.ForeignKey(Withholdingtax, models.DO_NOTHING, db_column='WithholdingTaxCode', blank=True, null=True)  # Field name made lowercase.
    withholdingtaxrate = models.DecimalField(db_column='WithholdingTaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    withholdingtax = models.DecimalField(db_column='WithholdingTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'WithholdingTaxDocDTL'


class Withholdingtaxtrans(models.Model):
    taxtranskey = models.BigAutoField(db_column='TaxTransKey', primary_key=True)  # Field name made lowercase.
    sourcetype = models.CharField(db_column='SourceType', max_length=2)  # Field name made lowercase.
    sourcekey = models.BigIntegerField(db_column='SourceKey')  # Field name made lowercase.
    sourcedtlkey = models.BigIntegerField(db_column='SourceDtlKey')  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', max_length=20)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    taxableaccno = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='TaxableAccNo', blank=True, null=True)  # Field name made lowercase.
    taxableamt = models.DecimalField(db_column='TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtaxableamt = models.DecimalField(db_column='LocalTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtax = models.DecimalField(db_column='LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    receiptpayment = models.CharField(db_column='ReceiptPayment', max_length=1)  # Field name made lowercase.
    taxablename = models.CharField(db_column='TaxableName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    withholdingtaxcode = models.CharField(db_column='WithholdingTaxCode', max_length=14)  # Field name made lowercase.
    withholdingtaxrate = models.DecimalField(db_column='WithholdingTaxRate', max_digits=18, decimal_places=6)  # Field name made lowercase.
    currencycode = models.CharField(db_column='CurrencyCode', max_length=5)  # Field name made lowercase.
    currencyrate = models.DecimalField(db_column='CurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.

    class Meta:
 
        db_table = 'WithholdingTaxTrans'


class Xfer(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', unique=True, max_length=20)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    fromlocation = models.ForeignKey(Location, models.DO_NOTHING, db_column='FromLocation')  # Field name made lowercase.
    tolocation = models.ForeignKey(Location, models.DO_NOTHING, db_column='ToLocation')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    reason = models.CharField(db_column='Reason', max_length=80, blank=True, null=True)  # Field name made lowercase.
    authorisedby = models.CharField(db_column='AuthorisedBy', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ref = models.CharField(db_column='Ref', max_length=40, blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    remark1 = models.CharField(db_column='Remark1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark2 = models.CharField(db_column='Remark2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark3 = models.CharField(db_column='Remark3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark4 = models.CharField(db_column='Remark4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    printcount = models.SmallIntegerField(db_column='PrintCount')  # Field name made lowercase.
    cancelled = models.CharField(db_column='Cancelled', max_length=1)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey(Users, models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    createduserid = models.ForeignKey(Users, models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    externallink = models.TextField(db_column='ExternalLink', blank=True, null=True)  # Field name made lowercase.
    refdocno = models.CharField(db_column='RefDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    cansync = models.CharField(db_column='CanSync', max_length=1)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.

    class Meta:
 
        db_table = 'XFER'


class Xferdtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    indtlkey = models.BigIntegerField(db_column='InDtlKey')  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    numbering = models.CharField(db_column='Numbering', max_length=6, blank=True, null=True)  # Field name made lowercase.
    itemcode = models.ForeignKey(Itemuom, models.DO_NOTHING, db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    batchno = models.ForeignKey(Itembatch, models.DO_NOTHING, db_column='BatchNo', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    furtherdescription = models.TextField(db_column='FurtherDescription', blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey(Project, models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey(Dept, models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    uom = models.ForeignKey(Itemuom, models.DO_NOTHING, db_column='UOM', blank=True, null=True)  # Field name made lowercase.
    unitcost = models.DecimalField(db_column='UnitCost', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    printout = models.CharField(db_column='PrintOut', max_length=1)  # Field name made lowercase.
    serialnolist = models.TextField(db_column='SerialNoList', blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.

    class Meta:
 
        db_table = 'XFERDTL'


class Xp(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', unique=True, max_length=20)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    creditorcode = models.ForeignKey(Branch, models.DO_NOTHING, db_column='CreditorCode', blank=True, null=True)  # Field name made lowercase.
    creditorname = models.CharField(db_column='CreditorName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ref = models.CharField(db_column='Ref', max_length=40, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=80, blank=True, null=True)  # Field name made lowercase.
    displayterm = models.ForeignKey(Terms, models.DO_NOTHING, db_column='DisplayTerm')  # Field name made lowercase.
    purchaseagent = models.ForeignKey(Purchaseagent, models.DO_NOTHING, db_column='PurchaseAgent', blank=True, null=True)  # Field name made lowercase.
    invaddr1 = models.CharField(db_column='InvAddr1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr2 = models.CharField(db_column='InvAddr2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr3 = models.CharField(db_column='InvAddr3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr4 = models.CharField(db_column='InvAddr4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    phone1 = models.CharField(db_column='Phone1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    fax1 = models.CharField(db_column='Fax1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    attention = models.CharField(db_column='Attention', max_length=40, blank=True, null=True)  # Field name made lowercase.
    branchcode = models.ForeignKey(Branch, models.DO_NOTHING, db_column='BranchCode', blank=True, null=True)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1param = models.DecimalField(db_column='Footer1Param', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1amt = models.DecimalField(db_column='Footer1Amt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1localamt = models.DecimalField(db_column='Footer1LocalAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1taxtype = models.ForeignKey(Taxtype, models.DO_NOTHING, db_column='Footer1TaxType', blank=True, null=True)  # Field name made lowercase.
    footer2param = models.DecimalField(db_column='Footer2Param', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2amt = models.DecimalField(db_column='Footer2Amt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2localamt = models.DecimalField(db_column='Footer2LocalAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2taxtype = models.ForeignKey(Taxtype, models.DO_NOTHING, db_column='Footer2TaxType', blank=True, null=True)  # Field name made lowercase.
    footer3param = models.DecimalField(db_column='Footer3Param', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3amt = models.DecimalField(db_column='Footer3Amt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3localamt = models.DecimalField(db_column='Footer3LocalAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3taxtype = models.ForeignKey(Taxtype, models.DO_NOTHING, db_column='Footer3TaxType', blank=True, null=True)  # Field name made lowercase.
    currencycode = models.ForeignKey(Currency, models.DO_NOTHING, db_column='CurrencyCode')  # Field name made lowercase.
    currencyrate = models.DecimalField(db_column='CurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    nettotal = models.DecimalField(db_column='NetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localnettotal = models.DecimalField(db_column='LocalNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtax = models.DecimalField(db_column='LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    remark1 = models.CharField(db_column='Remark1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark2 = models.CharField(db_column='Remark2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark3 = models.CharField(db_column='Remark3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark4 = models.CharField(db_column='Remark4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    printcount = models.SmallIntegerField(db_column='PrintCount')  # Field name made lowercase.
    cancelled = models.CharField(db_column='Cancelled', max_length=1)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey(Users, models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    createduserid = models.ForeignKey(Users, models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    externallink = models.TextField(db_column='ExternalLink', blank=True, null=True)  # Field name made lowercase.
    refdocno = models.CharField(db_column='RefDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cansync = models.CharField(db_column='CanSync', max_length=1)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    purchaselocation = models.ForeignKey(Location, models.DO_NOTHING, db_column='PurchaseLocation', blank=True, null=True)  # Field name made lowercase.
    footer1tax = models.DecimalField(db_column='Footer1Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1localtax = models.DecimalField(db_column='Footer1LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2tax = models.DecimalField(db_column='Footer2Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2localtax = models.DecimalField(db_column='Footer2LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3tax = models.DecimalField(db_column='Footer3Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3localtax = models.DecimalField(db_column='Footer3LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    extax = models.DecimalField(db_column='ExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localextax = models.DecimalField(db_column='LocalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    analysisnettotal = models.DecimalField(db_column='AnalysisNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localanalysisnettotal = models.DecimalField(db_column='LocalAnalysisNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.
    totaxcurrencyrate = models.DecimalField(db_column='ToTaxCurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    calcdiscountonunitprice = models.CharField(db_column='CalcDiscountOnUnitPrice', max_length=1, blank=True, null=True)  # Field name made lowercase.
    totalextax = models.DecimalField(db_column='TotalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxableamt = models.DecimalField(db_column='TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    inclusivetax = models.CharField(db_column='InclusiveTax', max_length=1)  # Field name made lowercase.
    footer1taxrate = models.DecimalField(db_column='Footer1TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    footer2taxrate = models.DecimalField(db_column='Footer2TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    footer3taxrate = models.DecimalField(db_column='Footer3TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    roundingmethod = models.IntegerField(db_column='RoundingMethod')  # Field name made lowercase.
    localtaxableamt = models.DecimalField(db_column='LocalTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytax = models.DecimalField(db_column='TaxCurrencyTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxableamt = models.DecimalField(db_column='TaxCurrencyTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'XP'


class Xpdtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    indent = models.SmallIntegerField(db_column='Indent', blank=True, null=True)  # Field name made lowercase.
    fontstyle = models.ForeignKey(Fontstyle, models.DO_NOTHING, db_column='FontStyle', blank=True, null=True)  # Field name made lowercase.
    mainitem = models.CharField(db_column='MainItem', max_length=1)  # Field name made lowercase.
    numbering = models.CharField(db_column='Numbering', max_length=6, blank=True, null=True)  # Field name made lowercase.
    itemcode = models.ForeignKey(Itemuom, models.DO_NOTHING, db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    location = models.ForeignKey(Location, models.DO_NOTHING, db_column='Location', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    furtherdescription = models.TextField(db_column='FurtherDescription', blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey(Project, models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey(Dept, models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    uom = models.ForeignKey(Itemuom, models.DO_NOTHING, db_column='UOM', blank=True, null=True)  # Field name made lowercase.
    useruom = models.CharField(db_column='UserUOM', max_length=8, blank=True, null=True)  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    smallestqty = models.DecimalField(db_column='SmallestQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    focqty = models.DecimalField(db_column='FOCQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    smallestunitprice = models.DecimalField(db_column='SmallestUnitPrice', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    discount = models.CharField(db_column='Discount', max_length=20, blank=True, null=True)  # Field name made lowercase.
    discountamt = models.DecimalField(db_column='DiscountAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxtype = models.ForeignKey(Taxtype, models.DO_NOTHING, db_column='TaxType', blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localsubtotal = models.DecimalField(db_column='LocalSubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    printout = models.CharField(db_column='PrintOut', max_length=1)  # Field name made lowercase.
    dtltype = models.CharField(db_column='DtlType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    calcbypercent = models.DecimalField(db_column='CalcByPercent', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    addtosubtotal = models.CharField(db_column='AddToSubTotal', max_length=1)  # Field name made lowercase.
    fromdoctype = models.CharField(db_column='FromDocType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    fromdocno = models.CharField(db_column='FromDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fromdocdtlkey = models.BigIntegerField(db_column='FromDocDtlKey', blank=True, null=True)  # Field name made lowercase.
    fulltransferoption = models.CharField(db_column='FullTransferOption', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fulltransferfromdoclist = models.TextField(db_column='FullTransferFromDocList', blank=True, null=True)  # Field name made lowercase.
    estimateddeliverydate = models.CharField(db_column='EstimatedDeliveryDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    packagedockey = models.BigIntegerField(db_column='PackageDocKey', blank=True, null=True)  # Field name made lowercase.
    parentdtlkey = models.BigIntegerField(db_column='ParentDtlKey', blank=True, null=True)  # Field name made lowercase.
    subqty = models.DecimalField(db_column='SubQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    subtotalextax = models.DecimalField(db_column='SubTotalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtax = models.DecimalField(db_column='LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.
    deliverydate = models.DateTimeField(db_column='DeliveryDate', blank=True, null=True)  # Field name made lowercase.
    taxableamt = models.DecimalField(db_column='TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxadjustment = models.DecimalField(db_column='TaxAdjustment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localsubtotalextax = models.DecimalField(db_column='LocalSubTotalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    extradiscountamt = models.DecimalField(db_column='ExtraDiscountAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxrate = models.DecimalField(db_column='TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    localtaxadjustment = models.DecimalField(db_column='LocalTaxAdjustment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtaxableamt = models.DecimalField(db_column='LocalTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytax = models.DecimalField(db_column='TaxCurrencyTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxableamt = models.DecimalField(db_column='TaxCurrencyTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    salesexemptionno = models.CharField(db_column='SalesExemptionNo', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'XPDTL'


class Xs(models.Model):
    dockey = models.BigIntegerField(db_column='DocKey', primary_key=True)  # Field name made lowercase.
    docno = models.CharField(db_column='DocNo', unique=True, max_length=20)  # Field name made lowercase.
    docdate = models.DateTimeField(db_column='DocDate')  # Field name made lowercase.
    debtorcode = models.ForeignKey(Branch, models.DO_NOTHING, db_column='DebtorCode')  # Field name made lowercase.
    debtorname = models.CharField(db_column='DebtorName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ref = models.CharField(db_column='Ref', max_length=40, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=80, blank=True, null=True)  # Field name made lowercase.
    displayterm = models.ForeignKey(Terms, models.DO_NOTHING, db_column='DisplayTerm')  # Field name made lowercase.
    salesagent = models.ForeignKey(Salesagent, models.DO_NOTHING, db_column='SalesAgent', blank=True, null=True)  # Field name made lowercase.
    invaddr1 = models.CharField(db_column='InvAddr1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr2 = models.CharField(db_column='InvAddr2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr3 = models.CharField(db_column='InvAddr3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invaddr4 = models.CharField(db_column='InvAddr4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    phone1 = models.CharField(db_column='Phone1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    fax1 = models.CharField(db_column='Fax1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    attention = models.CharField(db_column='Attention', max_length=40, blank=True, null=True)  # Field name made lowercase.
    branchcode = models.ForeignKey(Branch, models.DO_NOTHING, db_column='BranchCode', blank=True, null=True)  # Field name made lowercase.
    deliveraddr1 = models.CharField(db_column='DeliverAddr1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliveraddr2 = models.CharField(db_column='DeliverAddr2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliveraddr3 = models.CharField(db_column='DeliverAddr3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliveraddr4 = models.CharField(db_column='DeliverAddr4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    deliverphone1 = models.CharField(db_column='DeliverPhone1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    deliverfax1 = models.CharField(db_column='DeliverFax1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    delivercontact = models.CharField(db_column='DeliverContact', max_length=40, blank=True, null=True)  # Field name made lowercase.
    salesexemptionno = models.CharField(db_column='SalesExemptionNo', max_length=60, blank=True, null=True)  # Field name made lowercase.
    salesexemptionexpirydate = models.DateTimeField(db_column='SalesExemptionExpiryDate', blank=True, null=True)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1param = models.DecimalField(db_column='Footer1Param', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1amt = models.DecimalField(db_column='Footer1Amt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1localamt = models.DecimalField(db_column='Footer1LocalAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1taxtype = models.ForeignKey(Taxtype, models.DO_NOTHING, db_column='Footer1TaxType', blank=True, null=True)  # Field name made lowercase.
    footer2param = models.DecimalField(db_column='Footer2Param', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2amt = models.DecimalField(db_column='Footer2Amt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2localamt = models.DecimalField(db_column='Footer2LocalAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2taxtype = models.ForeignKey(Taxtype, models.DO_NOTHING, db_column='Footer2TaxType', blank=True, null=True)  # Field name made lowercase.
    footer3param = models.DecimalField(db_column='Footer3Param', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3amt = models.DecimalField(db_column='Footer3Amt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3localamt = models.DecimalField(db_column='Footer3LocalAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3taxtype = models.ForeignKey(Taxtype, models.DO_NOTHING, db_column='Footer3TaxType', blank=True, null=True)  # Field name made lowercase.
    currencycode = models.ForeignKey(Currency, models.DO_NOTHING, db_column='CurrencyCode')  # Field name made lowercase.
    currencyrate = models.DecimalField(db_column='CurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    nettotal = models.DecimalField(db_column='NetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localnettotal = models.DecimalField(db_column='LocalNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    analysisnettotal = models.DecimalField(db_column='AnalysisNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localanalysisnettotal = models.DecimalField(db_column='LocalAnalysisNetTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtax = models.DecimalField(db_column='LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    remark1 = models.CharField(db_column='Remark1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark2 = models.CharField(db_column='Remark2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark3 = models.CharField(db_column='Remark3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    remark4 = models.CharField(db_column='Remark4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    printcount = models.SmallIntegerField(db_column='PrintCount')  # Field name made lowercase.
    cancelled = models.CharField(db_column='Cancelled', max_length=1)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey(Users, models.DO_NOTHING, db_column='LastModifiedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    createduserid = models.ForeignKey(Users, models.DO_NOTHING, db_column='CreatedUserID')  # Field name made lowercase.
    externallink = models.TextField(db_column='ExternalLink', blank=True, null=True)  # Field name made lowercase.
    refdocno = models.CharField(db_column='RefDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cansync = models.CharField(db_column='CanSync', max_length=1)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    saleslocation = models.ForeignKey(Location, models.DO_NOTHING, db_column='SalesLocation', blank=True, null=True)  # Field name made lowercase.
    footer1tax = models.DecimalField(db_column='Footer1Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer1localtax = models.DecimalField(db_column='Footer1LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2tax = models.DecimalField(db_column='Footer2Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer2localtax = models.DecimalField(db_column='Footer2LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3tax = models.DecimalField(db_column='Footer3Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    footer3localtax = models.DecimalField(db_column='Footer3LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    extax = models.DecimalField(db_column='ExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localextax = models.DecimalField(db_column='LocalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    yourpono = models.CharField(db_column='YourPONo', max_length=25, blank=True, null=True)  # Field name made lowercase.
    yourpodate = models.DateTimeField(db_column='YourPODate', blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.
    totaxcurrencyrate = models.DecimalField(db_column='ToTaxCurrencyRate', max_digits=19, decimal_places=12)  # Field name made lowercase.
    calcdiscountonunitprice = models.CharField(db_column='CalcDiscountOnUnitPrice', max_length=1, blank=True, null=True)  # Field name made lowercase.
    totalextax = models.DecimalField(db_column='TotalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxableamt = models.DecimalField(db_column='TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    inclusivetax = models.CharField(db_column='InclusiveTax', max_length=1)  # Field name made lowercase.
    footer1taxrate = models.DecimalField(db_column='Footer1TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    footer2taxrate = models.DecimalField(db_column='Footer2TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    footer3taxrate = models.DecimalField(db_column='Footer3TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    roundingmethod = models.IntegerField(db_column='RoundingMethod')  # Field name made lowercase.
    localtaxableamt = models.DecimalField(db_column='LocalTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytax = models.DecimalField(db_column='TaxCurrencyTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxableamt = models.DecimalField(db_column='TaxCurrencyTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'XS'


class Xsdtl(models.Model):
    dtlkey = models.BigIntegerField(db_column='DtlKey', primary_key=True)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    seq = models.IntegerField(db_column='Seq')  # Field name made lowercase.
    indent = models.SmallIntegerField(db_column='Indent', blank=True, null=True)  # Field name made lowercase.
    fontstyle = models.ForeignKey(Fontstyle, models.DO_NOTHING, db_column='FontStyle', blank=True, null=True)  # Field name made lowercase.
    mainitem = models.CharField(db_column='MainItem', max_length=1)  # Field name made lowercase.
    numbering = models.CharField(db_column='Numbering', max_length=6, blank=True, null=True)  # Field name made lowercase.
    itemcode = models.ForeignKey(Itemuom, models.DO_NOTHING, db_column='ItemCode', blank=True, null=True)  # Field name made lowercase.
    location = models.ForeignKey(Location, models.DO_NOTHING, db_column='Location', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    furtherdescription = models.TextField(db_column='FurtherDescription', blank=True, null=True)  # Field name made lowercase.
    yourpono = models.CharField(db_column='YourPONo', max_length=25, blank=True, null=True)  # Field name made lowercase.
    yourpodate = models.DateTimeField(db_column='YourPODate', blank=True, null=True)  # Field name made lowercase.
    projno = models.ForeignKey(Project, models.DO_NOTHING, db_column='ProjNo', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey(Dept, models.DO_NOTHING, db_column='DeptNo', blank=True, null=True)  # Field name made lowercase.
    uom = models.ForeignKey(Itemuom, models.DO_NOTHING, db_column='UOM', blank=True, null=True)  # Field name made lowercase.
    useruom = models.CharField(db_column='UserUOM', max_length=8, blank=True, null=True)  # Field name made lowercase.
    qty = models.DecimalField(db_column='Qty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    smallestqty = models.DecimalField(db_column='SmallestQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    focqty = models.DecimalField(db_column='FOCQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    smallestunitprice = models.DecimalField(db_column='SmallestUnitPrice', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    discount = models.CharField(db_column='Discount', max_length=20, blank=True, null=True)  # Field name made lowercase.
    discountamt = models.DecimalField(db_column='DiscountAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxtype = models.ForeignKey(Taxtype, models.DO_NOTHING, db_column='TaxType', blank=True, null=True)  # Field name made lowercase.
    tax = models.DecimalField(db_column='Tax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localsubtotal = models.DecimalField(db_column='LocalSubTotal', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    printout = models.CharField(db_column='PrintOut', max_length=1)  # Field name made lowercase.
    dtltype = models.CharField(db_column='DtlType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    calcbypercent = models.DecimalField(db_column='CalcByPercent', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    addtosubtotal = models.CharField(db_column='AddToSubTotal', max_length=1)  # Field name made lowercase.
    fromdoctype = models.CharField(db_column='FromDocType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    fromdocno = models.CharField(db_column='FromDocNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fromdocdtlkey = models.BigIntegerField(db_column='FromDocDtlKey', blank=True, null=True)  # Field name made lowercase.
    fulltransferoption = models.CharField(db_column='FullTransferOption', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fulltransferfromdoclist = models.TextField(db_column='FullTransferFromDocList', blank=True, null=True)  # Field name made lowercase.
    estimateddeliverydate = models.CharField(db_column='EstimatedDeliveryDate', max_length=20, blank=True, null=True)  # Field name made lowercase.
    packagedockey = models.BigIntegerField(db_column='PackageDocKey', blank=True, null=True)  # Field name made lowercase.
    parentdtlkey = models.BigIntegerField(db_column='ParentDtlKey', blank=True, null=True)  # Field name made lowercase.
    subqty = models.DecimalField(db_column='SubQty', max_digits=25, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    subtotalextax = models.DecimalField(db_column='SubTotalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtax = models.DecimalField(db_column='LocalTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='Guid', max_length=36)  # Field name made lowercase.
    ruleno = models.BigIntegerField(db_column='RuleNo', blank=True, null=True)  # Field name made lowercase.
    deliverydate = models.DateTimeField(db_column='DeliveryDate', blank=True, null=True)  # Field name made lowercase.
    taxableamt = models.DecimalField(db_column='TaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxadjustment = models.DecimalField(db_column='TaxAdjustment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localsubtotalextax = models.DecimalField(db_column='LocalSubTotalExTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    extradiscountamt = models.DecimalField(db_column='ExtraDiscountAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxrate = models.DecimalField(db_column='TaxRate', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    localtaxadjustment = models.DecimalField(db_column='LocalTaxAdjustment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    localtaxableamt = models.DecimalField(db_column='LocalTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytax = models.DecimalField(db_column='TaxCurrencyTax', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    taxcurrencytaxableamt = models.DecimalField(db_column='TaxCurrencyTaxableAmt', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    salesexemptionno = models.CharField(db_column='SalesExemptionNo', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
 
        db_table = 'XSDTL'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
 
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
 
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
 
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
 
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
 
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
 
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AutocountHello(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
 
        db_table = 'autocount_hello'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
 
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
 
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
 
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
 
        db_table = 'django_session'
