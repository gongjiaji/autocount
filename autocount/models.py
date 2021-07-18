from django.db import models
import django_tables2 as tables



class Acctype(models.Model):
    acctype = models.CharField(db_column='AccType', primary_key=True, max_length=2)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=40, blank=True,
                                   null=True)  # Field name made lowercase.
    desc2 = models.CharField(db_column='Desc2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    isbstype = models.CharField(db_column='IsBSType', max_length=1)  # Field name made lowercase.
    issystemtype = models.CharField(db_column='IsSystemType', max_length=1)  # Field name made lowercase.

    class Meta:
        db_table = 'AccType'


class Currency(models.Model):
    currencycode = models.CharField(db_column='CurrencyCode', primary_key=True,
                                    max_length=5)  # Field name made lowercase.
    currencyword = models.CharField(db_column='CurrencyWord', max_length=40, blank=True,
                                    null=True)  # Field name made lowercase.
    currencyword2 = models.CharField(db_column='CurrencyWord2', max_length=40, blank=True,
                                     null=True)  # Field name made lowercase.
    currencysymbol = models.CharField(db_column='CurrencySymbol', max_length=6, blank=True,
                                      null=True)  # Field name made lowercase.
    bankbuyrate = models.DecimalField(db_column='BankBuyRate', max_digits=19,
                                      decimal_places=12)  # Field name made lowercase.
    banksellrate = models.DecimalField(db_column='BankSellRate', max_digits=19,
                                       decimal_places=12)  # Field name made lowercase.
    fcgainaccount = models.ForeignKey("Glmast", models.DO_NOTHING, db_column='FCGainAccount', blank=True, null=True,
                                      related_name="FCGainAccount")  # Field name made lowercase.
    fclossaccount = models.ForeignKey("Glmast", models.DO_NOTHING, db_column='FCLossAccount', blank=True, null=True,
                                      related_name="FCLossAccount")  # Field name made lowercase.
    gainlossjournaltype = models.ForeignKey('Journal', models.DO_NOTHING, db_column='GainLossJournalType', blank=True,
                                            null=True)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.

    class Meta:
        db_table = 'CURRENCY'


class Glmast(models.Model):
    accno = models.CharField(db_column='AccNo', primary_key=True, max_length=12)  # Field name made lowercase.
    parentaccno = models.CharField(db_column='ParentAccNo', max_length=12, blank=True,
                                   null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True,
                                   null=True)  # Field name made lowercase.
    desc2 = models.CharField(db_column='Desc2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    acctype = models.ForeignKey(Acctype, models.DO_NOTHING, db_column='AccType')  # Field name made lowercase.
    specialacctype = models.CharField(db_column='SpecialAccType', max_length=3, blank=True,
                                      null=True)  # Field name made lowercase.
    currencycode = models.ForeignKey(Currency, models.DO_NOTHING,
                                     db_column='CurrencyCode')  # Field name made lowercase.
    cashflowcategory = models.CharField(db_column='CashFlowCategory', max_length=1, blank=True,
                                        null=True)  # Field name made lowercase.
    msiccode = models.CharField(db_column='MSICCode', max_length=5, blank=True, null=True)  # Field name made lowercase.
    inputtaxtype = models.CharField(db_column='InputTaxType', max_length=14, blank=True,
                                    null=True)  # Field name made lowercase.
    outputtaxtype = models.CharField(db_column='OutputTaxType', max_length=14, blank=True,
                                     null=True)  # Field name made lowercase.
    tariffcode = models.ForeignKey('Tariff', models.DO_NOTHING, db_column='TariffCode', blank=True,
                                   null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'GLMast'


class Itemgroup(models.Model):
    itemgroup = models.CharField(db_column='ItemGroup', primary_key=True, max_length=8)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=40, blank=True,
                                   null=True)  # Field name made lowercase.
    desc2 = models.CharField(db_column='Desc2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.

    salescode = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='SalesCode', blank=True, null=True,
                                  related_name="SalesCode")  # Field name made lowercase.
    cashsalescode = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='CashSalesCode', blank=True, null=True,
                                      related_name="CashSalesCode")  # Field name made lowercase.
    salesreturncode = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='SalesReturnCode', blank=True, null=True,
                                        related_name="SalesReturnCode")  # Field name made lowercase.
    salesdiscountcode = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='SalesDiscountCode', blank=True,
                                          null=True, related_name="SalesDiscountCode")  # Field name made lowercase.
    purchasediscountcode = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='PurchaseDiscountCode', blank=True,
                                             null=True,
                                             related_name="PurchaseDiscountCode")  # Field name made lowercase.
    purchasecode = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='PurchaseCode', blank=True, null=True,
                                     related_name="PurchaseCode")  # Field name made lowercase.
    purchasereturncode = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='PurchaseReturnCode', blank=True,
                                           null=True, related_name="PurchaseReturnCode")  # Field name made lowercase.
    balancestockcode = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='BalanceStockCode', blank=True, null=True,
                                         related_name="BalanceStockCode")  # Field name made lowercase.

    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    shortcode = models.CharField(db_column='ShortCode', max_length=8, blank=True,
                                 null=True)  # Field name made lowercase.
    markupratio = models.DecimalField(db_column='MarkupRatio', max_digits=18, decimal_places=6, blank=True,
                                      null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'ItemGroup'


class Itemtype(models.Model):
    itemtype = models.CharField(db_column='ItemType', primary_key=True, max_length=12)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=40, blank=True,
                                   null=True)  # Field name made lowercase.
    desc2 = models.CharField(db_column='Desc2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    shortcode = models.CharField(db_column='ShortCode', max_length=8, blank=True,
                                 null=True)  # Field name made lowercase.
    markupratio = models.DecimalField(db_column='MarkupRatio', max_digits=18, decimal_places=6, blank=True,
                                      null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'ItemType'


class Taxtype(models.Model):
    taxtype = models.CharField(db_column='TaxType', primary_key=True, max_length=14)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=120, blank=True,
                                   null=True)  # Field name made lowercase.
    taxrate = models.DecimalField(db_column='TaxRate', max_digits=18, decimal_places=6)  # Field name made lowercase.
    inclusive = models.CharField(db_column='Inclusive', max_length=1)  # Field name made lowercase.
    isactive = models.CharField(db_column='IsActive', max_length=1)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    taxtypecategory = models.CharField(db_column='TaxTypeCategory', max_length=40, blank=True,
                                       null=True)  # Field name made lowercase.
    irastaxcode = models.CharField(db_column='IRASTaxCode', max_length=8, blank=True,
                                   null=True)  # Field name made lowercase.
    supplypurchase = models.CharField(db_column='SupplyPurchase', max_length=1)  # Field name made lowercase.
    isdefault = models.CharField(db_column='IsDefault', max_length=1)  # Field name made lowercase.
    taxaccno = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='TaxAccNo', blank=True,
                                 null=True)  # Field name made lowercase.
    iszerorate = models.CharField(db_column='IsZeroRate', max_length=1)  # Field name made lowercase.
    usetrxtaxaccno = models.CharField(db_column='UseTrxTaxAccNo', max_length=1)  # Field name made lowercase.
    accountingbasis = models.IntegerField(db_column='AccountingBasis')  # Field name made lowercase.
    addtocost = models.CharField(db_column='AddToCost', max_length=1)  # Field name made lowercase.

    class Meta:
        db_table = 'TaxType'


class Area(models.Model):
    areacode = models.CharField(db_column='AreaCode', primary_key=True, max_length=12)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=40, blank=True,
                                   null=True)  # Field name made lowercase.
    desc2 = models.CharField(db_column='Desc2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.

    class Meta:
        db_table = 'Area'


class Journal(models.Model):
    journaltype = models.CharField(db_column='JournalType', primary_key=True,
                                   max_length=10)  # Field name made lowercase.
    entrytype = models.CharField(db_column='EntryType', max_length=1)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=40, blank=True,
                                   null=True)  # Field name made lowercase.
    desc2 = models.CharField(db_column='Desc2', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Journal'


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


class Paymentmethod(models.Model):
    paymentmethod = models.CharField(db_column='PaymentMethod', primary_key=True,
                                     max_length=20)  # Field name made lowercase.
    bankaccount = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='BankAccount',
                                    related_name="BankAccount")  # Field name made lowercase.
    bankchargeaccount = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='BankChargeAccount', blank=True,
                                          null=True, related_name="bankchargeaccount")  # Field name made lowercase.
    bankchargepercent = models.DecimalField(db_column='BankChargePercent', max_digits=18,
                                            decimal_places=6)  # Field name made lowercase.
    mergebankchargetrans = models.CharField(db_column='MergeBankChargeTrans',
                                            max_length=1)  # Field name made lowercase.
    specialacctype = models.CharField(db_column='SpecialAccType', max_length=3)  # Field name made lowercase.
    journaltype = models.ForeignKey(Journal, models.DO_NOTHING, db_column='JournalType')  # Field name made lowercase.
    acceptchequeno = models.CharField(db_column='AcceptChequeNo', max_length=1)  # Field name made lowercase.
    paymentby = models.CharField(db_column='PaymentBy', max_length=20, blank=True,
                                 null=True)  # Field name made lowercase.
    odlimit = models.DecimalField(db_column='ODLimit', max_digits=19, decimal_places=2)  # Field name made lowercase.
    paymentformatname = models.ForeignKey(Docnoformat, models.DO_NOTHING, db_column='PaymentFormatName',
                                          related_name="paymentformatname")  # Field name made lowercase.
    receiptformatname = models.ForeignKey(Docnoformat, models.DO_NOTHING, db_column='ReceiptFormatName',
                                          related_name="receiptformatname")  # Field name made lowercase.
    nextchequeno = models.CharField(db_column='NextChequeNo', max_length=20, blank=True,
                                    null=True)  # Field name made lowercase.
    isactive = models.CharField(db_column='IsActive', max_length=1)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    paymenttype = models.CharField(db_column='PaymentType', max_length=12, blank=True,
                                   null=True)  # Field name made lowercase.
    minbankcharge = models.DecimalField(db_column='MinBankCharge', max_digits=19, decimal_places=2, blank=True,
                                        null=True)  # Field name made lowercase.
    bankchargetaxtype = models.ForeignKey(Taxtype, models.DO_NOTHING, db_column='BankChargeTaxType', blank=True,
                                          null=True)  # Field name made lowercase.
    bankchargetaxbrno = models.CharField(db_column='BankChargeTaxBRNo', max_length=25, blank=True,
                                         null=True)  # Field name made lowercase.
    bankchargetaxbname = models.CharField(db_column='BankChargeTaxBName', max_length=100, blank=True,
                                          null=True)  # Field name made lowercase.
    bankchargetaxregisterno = models.CharField(db_column='BankChargeTaxRegisterNo', max_length=20, blank=True,
                                               null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'PaymentMethod'


class Location(models.Model):
    location = models.CharField(db_column='Location', primary_key=True, max_length=8)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=80, blank=True,
                                   null=True)  # Field name made lowercase.
    desc2 = models.CharField(db_column='Desc2', max_length=80, blank=True, null=True)  # Field name made lowercase.
    address1 = models.CharField(db_column='Address1', max_length=40, blank=True,
                                null=True)  # Field name made lowercase.
    address2 = models.CharField(db_column='Address2', max_length=40, blank=True,
                                null=True)  # Field name made lowercase.
    address3 = models.CharField(db_column='Address3', max_length=40, blank=True,
                                null=True)  # Field name made lowercase.
    address4 = models.CharField(db_column='Address4', max_length=40, blank=True,
                                null=True)  # Field name made lowercase.
    postcode = models.CharField(db_column='PostCode', max_length=10, blank=True,
                                null=True)  # Field name made lowercase.
    phone1 = models.CharField(db_column='Phone1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    phone2 = models.CharField(db_column='Phone2', max_length=25, blank=True, null=True)  # Field name made lowercase.
    fax1 = models.CharField(db_column='Fax1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    fax2 = models.CharField(db_column='Fax2', max_length=25, blank=True, null=True)  # Field name made lowercase.
    contact = models.CharField(db_column='Contact', max_length=40, blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    isactive = models.CharField(db_column='IsActive', max_length=1)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    areacode = models.ForeignKey(Area, models.DO_NOTHING, db_column='AreaCode', blank=True, null=True,
                                 related_name="AreaCode")  # Field name made lowercase.
    cashpaymentmethod = models.ForeignKey(Paymentmethod, models.DO_NOTHING, db_column='CashPaymentMethod', blank=True,
                                          null=True, related_name="CashPaymentMethod")  # Field name made lowercase.
    debitcardpaymentmethod = models.ForeignKey(Paymentmethod, models.DO_NOTHING, db_column='DebitCardPaymentMethod',
                                               blank=True, null=True,
                                               related_name="DebitCardPaymentMethod")  # Field name made lowercase.
    voucherpaymentmethod = models.ForeignKey(Paymentmethod, models.DO_NOTHING, db_column='VoucherPaymentMethod',
                                             blank=True, null=True,
                                             related_name="VoucherPaymentMethod")  # Field name made lowercase.
    chequepaymentmethod = models.ForeignKey(Paymentmethod, models.DO_NOTHING, db_column='ChequePaymentMethod',
                                            blank=True, null=True,
                                            related_name="ChequePaymentMethod")  # Field name made lowercase.
    pointpaymentmethod = models.ForeignKey(Paymentmethod, models.DO_NOTHING, db_column='PointPaymentMethod', blank=True,
                                           null=True, related_name="PointPaymentMethod")  # Field name made lowercase.
    roundingaccno = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='RoundingAccNo', blank=True, null=True,
                                      related_name="RoundingAccNo")  # Field name made lowercase.
    depositaccno = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='DepositAccNo', blank=True, null=True,
                                     related_name="DepositAccNo")  # Field name made lowercase.
    forfeitedaccno = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='ForfeitedAccNo', blank=True, null=True,
                                       related_name="ForfeitedAccNo")  # Field name made lowercase.
    creditcardchargesaccno = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='CreditCardChargesAccNo',
                                               blank=True, null=True,
                                               related_name="CreditCardChargesAccNo")  # Field name made lowercase.
    pointpaymentaccno = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='PointPaymentAccNo', blank=True,
                                          null=True, related_name="PointPaymentAccNo")  # Field name made lowercase.
    servicechargeaccno = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='ServiceChargeAccNo', blank=True,
                                           null=True, related_name="ServiceChargeAccNo")  # Field name made lowercase.
    voucherforfeitedaccno = models.ForeignKey(Glmast, models.DO_NOTHING, db_column='VoucherForfeitedAccNo', blank=True,
                                              null=True,
                                              related_name="VoucherForfeitedAccNo")  # Field name made lowercase.
    alipaypaymentmethod = models.ForeignKey(Paymentmethod, models.DO_NOTHING, db_column='AlipayPaymentMethod',
                                            blank=True, null=True,
                                            related_name="AlipayPaymentMethod")  # Field name made lowercase.

    class Meta:
        db_table = 'Location'


class Project(models.Model):
    projno = models.CharField(db_column='ProjNo', primary_key=True, max_length=10)  # Field name made lowercase.
    parentprojno = models.ForeignKey('self', models.DO_NOTHING, db_column='ParentProjNo', blank=True,
                                     null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=40, blank=True,
                                   null=True)  # Field name made lowercase.
    desc2 = models.CharField(db_column='Desc2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    isactive = models.CharField(db_column='IsActive', max_length=1)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.

    class Meta:
        db_table = 'Project'


class Dept(models.Model):
    deptno = models.CharField(db_column='DeptNo', primary_key=True, max_length=10)  # Field name made lowercase.
    parentdeptno = models.ForeignKey('self', models.DO_NOTHING, db_column='ParentDeptNo', blank=True,
                                     null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=40, blank=True,
                                   null=True)  # Field name made lowercase.
    desc2 = models.CharField(db_column='Desc2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    isactive = models.CharField(db_column='IsActive', max_length=1)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.

    class Meta:
        db_table = 'Dept'


class Users(models.Model):
    userid = models.CharField(db_column='UserID', primary_key=True, max_length=10)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=40, blank=True,
                                null=True)  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=30, blank=True,
                                  null=True)  # Field name made lowercase.
    passwd = models.CharField(db_column='Passwd', max_length=112, blank=True, null=True)  # Field name made lowercase.
    signature = models.BinaryField(db_column='Signature', blank=True, null=True)  # Field name made lowercase.
    emailaddress = models.CharField(db_column='EmailAddress', max_length=80, blank=True,
                                    null=True)  # Field name made lowercase.
    filterbysalesagent = models.CharField(db_column='FilterBySalesAgent', max_length=1)  # Field name made lowercase.
    filterbypurchaseagent = models.CharField(db_column='FilterByPurchaseAgent',
                                             max_length=1)  # Field name made lowercase.
    isactive = models.CharField(db_column='IsActive', max_length=1)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    mainpage = models.TextField(db_column='MainPage', blank=True, null=True)  # Field name made lowercase.
    passwordage = models.IntegerField(db_column='PasswordAge')  # Field name made lowercase.
    lastpassworddate = models.DateTimeField(db_column='LastPasswordDate', blank=True,
                                            null=True)  # Field name made lowercase.
    location = models.ForeignKey(Location, models.DO_NOTHING, db_column='Location', blank=True,
                                 null=True)  # Field name made lowercase.
    projno = models.ForeignKey(Project, models.DO_NOTHING, db_column='ProjNo', blank=True,
                               null=True)  # Field name made lowercase.
    deptno = models.ForeignKey(Dept, models.DO_NOTHING, db_column='DeptNo', blank=True,
                               null=True)  # Field name made lowercase.
    isexportdebtortobranch = models.CharField(db_column='IsExportDebtorToBranch',
                                              max_length=1)  # Field name made lowercase.
    isexportcreditortobranch = models.CharField(db_column='IsExportCreditorToBranch',
                                                max_length=1)  # Field name made lowercase.
    isexportitemtobranch = models.CharField(db_column='IsExportItemToBranch',
                                            max_length=1)  # Field name made lowercase.
    isexportpricehistorytobranch = models.CharField(db_column='IsExportPriceHistoryToBranch',
                                                    max_length=1)  # Field name made lowercase.
    isexportqttobranch = models.CharField(db_column='IsExportQTToBranch', max_length=1)  # Field name made lowercase.
    isexportsotobranch = models.CharField(db_column='IsExportSOToBranch', max_length=1)  # Field name made lowercase.
    isexportdotobranch = models.CharField(db_column='IsExportDOToBranch', max_length=1)  # Field name made lowercase.
    isexportivtobranch = models.CharField(db_column='IsExportIVToBranch', max_length=1)  # Field name made lowercase.
    isexportcstobranch = models.CharField(db_column='IsExportCSToBranch', max_length=1)  # Field name made lowercase.
    posmainpage = models.TextField(db_column='POSMainPage', blank=True, null=True)  # Field name made lowercase.
    salescreditlimitincrementpercentage = models.DecimalField(db_column='SalesCreditLimitIncrementPercentage',
                                                              max_digits=19, decimal_places=2, blank=True,
                                                              null=True)  # Field name made lowercase.
    salesoverduelimitincrementpercentage = models.DecimalField(db_column='SalesOverdueLimitIncrementPercentage',
                                                               max_digits=19, decimal_places=2, blank=True,
                                                               null=True)  # Field name made lowercase.
    purchasecreditlimitincrementpercentage = models.DecimalField(db_column='PurchaseCreditLimitIncrementPercentage',
                                                                 max_digits=19, decimal_places=2, blank=True,
                                                                 null=True)  # Field name made lowercase.
    purchaseoverduelimitincrementpercentage = models.DecimalField(db_column='PurchaseOverdueLimitIncrementPercentage',
                                                                  max_digits=19, decimal_places=2, blank=True,
                                                                  null=True)  # Field name made lowercase.
    filteredbycreateduserid = models.CharField(db_column='FilteredByCreatedUserID', max_length=1, blank=True,
                                               null=True)  # Field name made lowercase.
    filteredbylastmodifieduserid = models.CharField(db_column='FilteredByLastModifiedUserID', max_length=1, blank=True,
                                                    null=True)  # Field name made lowercase.
    passwordstrength = models.CharField(db_column='PasswordStrength', max_length=1, blank=True,
                                        null=True)  # Field name made lowercase.
    usertype = models.CharField(db_column='UserType', max_length=1)  # Field name made lowercase.
    filterbyaccno = models.CharField(db_column='FilterByAccNo', max_length=1)  # Field name made lowercase.

    class Meta:
        db_table = 'Users'


class Itembrand(models.Model):
    itembrand = models.CharField(db_column='ItemBrand', primary_key=True, max_length=20)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=40, blank=True,
                                   null=True)  # Field name made lowercase.
    desc2 = models.CharField(db_column='Desc2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    markupratio = models.DecimalField(db_column='MarkupRatio', max_digits=18, decimal_places=6, blank=True,
                                      null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'ItemBrand'


class Itemmodel(models.Model):
    itemmodel = models.CharField(db_column='ItemModel', primary_key=True, max_length=20)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=40, blank=True,
                                   null=True)  # Field name made lowercase.
    desc2 = models.CharField(db_column='Desc2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    markupratio = models.DecimalField(db_column='MarkupRatio', max_digits=18, decimal_places=6, blank=True,
                                      null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'ItemModel'


class Tariff(models.Model):
    tariffcode = models.CharField(db_column='TariffCode', primary_key=True, max_length=12)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True,
                                   null=True)  # Field name made lowercase.
    desc2 = models.CharField(db_column='Desc2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    isactive = models.CharField(db_column='IsActive', max_length=1)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.

    class Meta:
        db_table = 'Tariff'


class Item(models.Model):
    itemgroup = models.ForeignKey(Itemgroup, models.DO_NOTHING, db_column='ItemGroup', blank=True,
                                  null=True)  # Field name made lowercase.
    itemtype = models.ForeignKey(Itemtype, models.DO_NOTHING, db_column='ItemType', blank=True,
                                 null=True)  # Field name made lowercase.
    taxtype = models.ForeignKey(Taxtype, models.DO_NOTHING, db_column='Taxtype', blank=True, null=True,
                                related_name="Taxtype")  # Field name made lowercase.
    purchasetaxtype = models.ForeignKey(Taxtype, models.DO_NOTHING, db_column='PurchaseTaxType', blank=True, null=True,
                                        related_name="PurchaseTaxType")  # Field name made lowercase.

    lastmodifieduserid = models.ForeignKey(Users, models.DO_NOTHING, db_column='LastModifiedUserID',
                                           related_name="LastModifiedUserID")  # Field name made lowercase.
    createduserid = models.ForeignKey(Users, models.DO_NOTHING, db_column='CreatedUserID',
                                      related_name="CreatedUserID")  # Field name made lowercase.
    itembrand = models.ForeignKey(Itembrand, models.DO_NOTHING, db_column='ItemBrand', blank=True,
                                  null=True)  # Field name made lowercase.
    itemmodel = models.ForeignKey(Itemmodel, models.DO_NOTHING, db_column='ItemModel', blank=True,
                                  null=True)  # Field name made lowercase.
    tariffcode = models.ForeignKey(Tariff, models.DO_NOTHING, db_column='TariffCode', blank=True,
                                   null=True)  # Field name made lowercase.

    itemcode = models.CharField(db_column='ItemCode', primary_key=True, max_length=30)  # Field name made lowercase.
    dockey = models.BigIntegerField(db_column='DocKey')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True,
                                   null=True)  # Field name made lowercase.
    desc2 = models.CharField(db_column='Desc2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    furtherdescription = models.TextField(db_column='FurtherDescription', blank=True,
                                          null=True)  # Field name made lowercase.
    assemblycost = models.DecimalField(db_column='AssemblyCost', max_digits=25, decimal_places=8, blank=True,
                                       null=True)  # Field name made lowercase.
    leadtime = models.CharField(db_column='LeadTime', max_length=40, blank=True,
                                null=True)  # Field name made lowercase.
    stockcontrol = models.CharField(db_column='StockControl', max_length=1)  # Field name made lowercase.
    hasserialno = models.CharField(db_column='HasSerialNo', max_length=1)  # Field name made lowercase.
    hasbatchno = models.CharField(db_column='HasBatchNo', max_length=1)  # Field name made lowercase.
    dutyrate = models.DecimalField(db_column='DutyRate', max_digits=18, decimal_places=6)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    imagefilename = models.CharField(db_column='ImageFileName', max_length=120, blank=True,
                                     null=True)  # Field name made lowercase.
    costingmethod = models.SmallIntegerField(db_column='CostingMethod')  # Field name made lowercase.
    salesuom = models.CharField(db_column='SalesUOM', max_length=8)  # Field name made lowercase.
    purchaseuom = models.CharField(db_column='PurchaseUOM', max_length=8)  # Field name made lowercase.
    reportuom = models.CharField(db_column='ReportUOM', max_length=8)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    isactive = models.CharField(db_column='IsActive', max_length=1)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    snformatname = models.CharField(db_column='SNFormatName', max_length=20, blank=True,
                                    null=True)  # Field name made lowercase.
    iscalcbonuspoint = models.CharField(db_column='IsCalcBonusPoint', max_length=1, blank=True,
                                        null=True)  # Field name made lowercase.
    markupratio = models.DecimalField(db_column='MarkupRatio', max_digits=18, decimal_places=6, blank=True,
                                      null=True)  # Field name made lowercase.
    haspromoter = models.CharField(db_column='HasPromoter', max_length=1)  # Field name made lowercase.
    globalcode = models.CharField(db_column='GlobalCode', max_length=30, blank=True,
                                  null=True)  # Field name made lowercase.
    leadtimeday = models.IntegerField(db_column='LeadTimeDay', blank=True, null=True)  # Field name made lowercase.
    externallink = models.TextField(db_column='ExternalLink', blank=True, null=True)  # Field name made lowercase.
    discontinued = models.CharField(db_column='Discontinued', max_length=1)  # Field name made lowercase.
    autouomconversion = models.CharField(db_column='AutoUOMConversion', max_length=1, blank=True,
                                         null=True)  # Field name made lowercase.
    baseuom = models.CharField(db_column='BaseUOM', max_length=8)  # Field name made lowercase.
    backordercontrol = models.CharField(db_column='BackOrderControl', max_length=1)  # Field name made lowercase.

    class Meta:
        db_table = 'Item'

    def __str__(self) -> str:
        return self.itemcode


class Pricecategory(models.Model):
    pricecategory = models.CharField(db_column='PriceCategory', primary_key=True,
                                     max_length=12)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=40, blank=True,
                                   null=True)  # Field name made lowercase.
    discountpercent = models.DecimalField(db_column='DiscountPercent', max_digits=18, decimal_places=6, blank=True,
                                          null=True)  # Field name made lowercase.
    detaildiscount = models.CharField(db_column='DetailDiscount', max_length=20, blank=True,
                                      null=True)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    markupratio = models.DecimalField(db_column='MarkupRatio', max_digits=18, decimal_places=6, blank=True,
                                      null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'PriceCategory'


class Terms(models.Model):
    displayterm = models.CharField(db_column='DisplayTerm', primary_key=True,
                                   max_length=30)  # Field name made lowercase.
    terms = models.CharField(db_column='Terms', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    termtype = models.CharField(db_column='TermType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    termdays = models.IntegerField(db_column='TermDays', blank=True, null=True)  # Field name made lowercase.
    discountdays = models.IntegerField(db_column='DiscountDays', blank=True, null=True)  # Field name made lowercase.
    discountpercent = models.DecimalField(db_column='DiscountPercent', max_digits=18, decimal_places=6, blank=True,
                                          null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Terms'


class Itemuom(models.Model):
    itemcode = models.CharField(db_column='ItemCode', primary_key=True, max_length=30)  # Field name made lowercase.
    uom = models.CharField(db_column='UOM', max_length=8)  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=25, decimal_places=8)  # Field name made lowercase.
    shelf = models.CharField(db_column='Shelf', max_length=20, blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=25, decimal_places=8, blank=True,
                                null=True)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=25, decimal_places=8, blank=True,
                               null=True)  # Field name made lowercase.
    realcost = models.DecimalField(db_column='RealCost', max_digits=25, decimal_places=8, blank=True,
                                   null=True)  # Field name made lowercase.
    mostrecentlycost = models.DecimalField(db_column='MostRecentlyCost', max_digits=25, decimal_places=8, blank=True,
                                           null=True)  # Field name made lowercase.
    minsaleprice = models.DecimalField(db_column='MinSalePrice', max_digits=25, decimal_places=8, blank=True,
                                       null=True)  # Field name made lowercase.
    maxsaleprice = models.DecimalField(db_column='MaxSalePrice', max_digits=25, decimal_places=8, blank=True,
                                       null=True)  # Field name made lowercase.
    minpurchaseprice = models.DecimalField(db_column='MinPurchasePrice', max_digits=25, decimal_places=8, blank=True,
                                           null=True)  # Field name made lowercase.
    maxpurchaseprice = models.DecimalField(db_column='MaxPurchasePrice', max_digits=25, decimal_places=8, blank=True,
                                           null=True)  # Field name made lowercase.
    balqty = models.DecimalField(db_column='BalQty', max_digits=25, decimal_places=8)  # Field name made lowercase.
    minqty = models.DecimalField(db_column='MinQty', max_digits=25, decimal_places=8, blank=True,
                                 null=True)  # Field name made lowercase.
    maxqty = models.DecimalField(db_column='MaxQty', max_digits=25, decimal_places=8, blank=True,
                                 null=True)  # Field name made lowercase.
    normallevel = models.DecimalField(db_column='NormalLevel', max_digits=25, decimal_places=8, blank=True,
                                      null=True)  # Field name made lowercase.
    reolevel = models.DecimalField(db_column='ReOLevel', max_digits=25, decimal_places=8, blank=True,
                                   null=True)  # Field name made lowercase.
    reoqty = models.DecimalField(db_column='ReOQty', max_digits=25, decimal_places=8, blank=True,
                                 null=True)  # Field name made lowercase.
    foclevel = models.DecimalField(db_column='FOCLevel', max_digits=25, decimal_places=8, blank=True,
                                   null=True)  # Field name made lowercase.
    focqty = models.DecimalField(db_column='FOCQty', max_digits=25, decimal_places=8, blank=True,
                                 null=True)  # Field name made lowercase.
    bonuspointqty = models.DecimalField(db_column='BonusPointQty', max_digits=25, decimal_places=8, blank=True,
                                        null=True)  # Field name made lowercase.
    bonuspoint = models.DecimalField(db_column='BonusPoint', max_digits=19, decimal_places=2, blank=True,
                                     null=True)  # Field name made lowercase.
    weight = models.DecimalField(db_column='Weight', max_digits=25, decimal_places=8, blank=True,
                                 null=True)  # Field name made lowercase.
    weightuom = models.CharField(db_column='WeightUOM', max_length=8, blank=True,
                                 null=True)  # Field name made lowercase.
    volume = models.DecimalField(db_column='Volume', max_digits=25, decimal_places=8, blank=True,
                                 null=True)  # Field name made lowercase.
    volumeuom = models.CharField(db_column='VolumeUOM', max_length=8, blank=True,
                                 null=True)  # Field name made lowercase.
    barcode = models.CharField(db_column='BarCode', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    redeembonuspoint = models.DecimalField(db_column='RedeemBonusPoint', max_digits=19, decimal_places=2, blank=True,
                                           null=True)  # Field name made lowercase.
    csgnqty = models.DecimalField(db_column='CSGNQty', max_digits=25, decimal_places=8, blank=True,
                                  null=True)  # Field name made lowercase.
    price2 = models.DecimalField(db_column='Price2', max_digits=25, decimal_places=8, blank=True,
                                 null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'ItemUOM'
        unique_together = (('itemcode', 'uom'),)


    def __str__(self) -> str:
        return self.itemcode + self.uom


class Salesagent(models.Model):
    salesagent = models.CharField(db_column='SalesAgent', primary_key=True, max_length=12)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=40, blank=True,
                                   null=True)  # Field name made lowercase.
    desc2 = models.CharField(db_column='Desc2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    isactive = models.CharField(db_column='IsActive', max_length=1)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    signature = models.BinaryField(db_column='Signature', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'SalesAgent'


class Debtortype(models.Model):
    debtortype = models.CharField(db_column='DebtorType', primary_key=True, max_length=20)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=40, blank=True,
                                   null=True)  # Field name made lowercase.
    desc2 = models.CharField(db_column='Desc2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    isactive = models.CharField(db_column='IsActive', max_length=1)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.

    class Meta:
        db_table = 'DebtorType'

class Debtor(models.Model):
    accno = models.OneToOneField('Glmast', models.DO_NOTHING, db_column='AccNo',
                                 primary_key=True)  # Field name made lowercase.
    companyname = models.CharField(db_column='CompanyName', max_length=100, blank=True,
                                   null=True)  # Field name made lowercase.
    desc2 = models.CharField(db_column='Desc2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    registerno = models.CharField(db_column='RegisterNo', max_length=25, blank=True,
                                  null=True)  # Field name made lowercase.
    address1 = models.CharField(db_column='Address1', max_length=40, blank=True,
                                null=True)  # Field name made lowercase.
    address2 = models.CharField(db_column='Address2', max_length=40, blank=True,
                                null=True)  # Field name made lowercase.
    address3 = models.CharField(db_column='Address3', max_length=40, blank=True,
                                null=True)  # Field name made lowercase.
    address4 = models.CharField(db_column='Address4', max_length=40, blank=True,
                                null=True)  # Field name made lowercase.
    postcode = models.CharField(db_column='PostCode', max_length=10, blank=True,
                                null=True)  # Field name made lowercase.
    deliveraddr1 = models.CharField(db_column='DeliverAddr1', max_length=40, blank=True,
                                    null=True)  # Field name made lowercase.
    deliveraddr2 = models.CharField(db_column='DeliverAddr2', max_length=40, blank=True,
                                    null=True)  # Field name made lowercase.
    deliveraddr3 = models.CharField(db_column='DeliverAddr3', max_length=40, blank=True,
                                    null=True)  # Field name made lowercase.
    deliveraddr4 = models.CharField(db_column='DeliverAddr4', max_length=40, blank=True,
                                    null=True)  # Field name made lowercase.
    deliverpostcode = models.CharField(db_column='DeliverPostCode', max_length=10, blank=True,
                                       null=True)  # Field name made lowercase.
    attention = models.CharField(db_column='Attention', max_length=40, blank=True,
                                 null=True)  # Field name made lowercase.
    phone1 = models.CharField(db_column='Phone1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    phone2 = models.CharField(db_column='Phone2', max_length=25, blank=True, null=True)  # Field name made lowercase.
    fax1 = models.CharField(db_column='Fax1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    fax2 = models.CharField(db_column='Fax2', max_length=25, blank=True, null=True)  # Field name made lowercase.
    areacode = models.ForeignKey(Area, models.DO_NOTHING, db_column='AreaCode', blank=True,
                                 null=True)  # Field name made lowercase.
    salesagent = models.ForeignKey('Salesagent', models.DO_NOTHING, db_column='SalesAgent', blank=True,
                                   null=True, related_name='Salesagent')  # Field name made lowercase.
    debtortype = models.ForeignKey('Debtortype', models.DO_NOTHING, db_column='DebtorType', blank=True,
                                   null=True, related_name='Debtor_debtortype')  # Field name made lowercase.
    natureofbusiness = models.CharField(db_column='NatureOfBusiness', max_length=40, blank=True,
                                        null=True)  # Field name made lowercase.
    weburl = models.CharField(db_column='WebURL', max_length=80, blank=True, null=True)  # Field name made lowercase.
    emailaddress = models.CharField(db_column='EmailAddress', max_length=80, blank=True,
                                    null=True)  # Field name made lowercase.
    displayterm = models.ForeignKey('Terms', models.DO_NOTHING, db_column='DisplayTerm')  # Field name made lowercase.
    creditlimit = models.DecimalField(db_column='CreditLimit', max_digits=19, decimal_places=2, blank=True,
                                      null=True)  # Field name made lowercase.
    agingon = models.CharField(db_column='AgingOn', max_length=1, blank=True, null=True)  # Field name made lowercase.
    statementtype = models.CharField(db_column='StatementType', max_length=1, blank=True,
                                     null=True)  # Field name made lowercase.
    currencycode = models.ForeignKey(Currency, models.DO_NOTHING,
                                     db_column='CurrencyCode')  # Field name made lowercase.
    allowexceedcreditlimit = models.CharField(db_column='AllowExceedCreditLimit',
                                              max_length=1)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    exemptno = models.CharField(db_column='ExemptNo', max_length=60, blank=True,
                                null=True)  # Field name made lowercase.
    expirydate = models.DateTimeField(db_column='ExpiryDate', blank=True, null=True)  # Field name made lowercase.
    pricecategory = models.ForeignKey('Pricecategory', models.DO_NOTHING, db_column='PriceCategory', blank=True,
                                      null=True, related_name='Debtor_pricecategory')  # Field name made lowercase.
    taxtype = models.ForeignKey('Taxtype', models.DO_NOTHING, db_column='TaxType', blank=True,
                                null=True, related_name='Debtor_taxtype')  # Field name made lowercase.
    discountpercent = models.DecimalField(db_column='DiscountPercent', max_digits=18,
                                          decimal_places=6)  # Field name made lowercase.
    detaildiscount = models.CharField(db_column='DetailDiscount', max_length=20, blank=True,
                                      null=True)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified')  # Field name made lowercase.
    lastmodifieduserid = models.ForeignKey('Users', models.DO_NOTHING,
                                           db_column='LastModifiedUserID', related_name='Debtor_LastModifiedUserID')  # Field name made lowercase.
    createdtimestamp = models.DateTimeField(db_column='CreatedTimeStamp')  # Field name made lowercase.
    createduserid = models.ForeignKey('Users', models.DO_NOTHING,
                                      db_column='CreatedUserID', related_name='createduserid')  # Field name made lowercase.
    overduelimit = models.DecimalField(db_column='OverdueLimit', max_digits=19, decimal_places=2, blank=True,
                                       null=True)  # Field name made lowercase.
    hasbonuspoint = models.CharField(db_column='HasBonusPoint', max_length=1)  # Field name made lowercase.
    openingbonuspoint = models.DecimalField(db_column='OpeningBonusPoint', max_digits=19, decimal_places=2, blank=True,
                                            null=True)  # Field name made lowercase.
    qtblockstatus = models.SmallIntegerField(db_column='QTBlockStatus', blank=True,
                                             null=True)  # Field name made lowercase.
    soblockstatus = models.SmallIntegerField(db_column='SOBlockStatus', blank=True,
                                             null=True)  # Field name made lowercase.
    doblockstatus = models.SmallIntegerField(db_column='DOBlockStatus', blank=True,
                                             null=True)  # Field name made lowercase.
    ivblockstatus = models.SmallIntegerField(db_column='IVBlockStatus', blank=True,
                                             null=True)  # Field name made lowercase.
    csblockstatus = models.SmallIntegerField(db_column='CSBlockStatus', blank=True,
                                             null=True)  # Field name made lowercase.
    qtblockmessage = models.CharField(db_column='QTBlockMessage', max_length=40, blank=True,
                                      null=True)  # Field name made lowercase.
    soblockmessage = models.CharField(db_column='SOBlockMessage', max_length=40, blank=True,
                                      null=True)  # Field name made lowercase.
    doblockmessage = models.CharField(db_column='DOBlockMessage', max_length=40, blank=True,
                                      null=True)  # Field name made lowercase.
    ivblockmessage = models.CharField(db_column='IVBlockMessage', max_length=40, blank=True,
                                      null=True)  # Field name made lowercase.
    csblockmessage = models.CharField(db_column='CSBlockMessage', max_length=40, blank=True,
                                      null=True)  # Field name made lowercase.
    externallink = models.TextField(db_column='ExternalLink', blank=True, null=True)  # Field name made lowercase.
    isgroupcompany = models.CharField(db_column='IsGroupCompany', max_length=1)  # Field name made lowercase.
    isactive = models.CharField(db_column='IsActive', max_length=1)  # Field name made lowercase.
    lastupdate = models.IntegerField(db_column='LastUpdate')  # Field name made lowercase.
    contactinfo = models.TextField(db_column='ContactInfo', blank=True, null=True)  # Field name made lowercase.
    accountgroup = models.CharField(db_column='AccountGroup', max_length=12, blank=True,
                                    null=True)  # Field name made lowercase.
    markupratio = models.DecimalField(db_column='MarkupRatio', max_digits=18, decimal_places=6, blank=True,
                                      null=True)  # Field name made lowercase.
    taxregisterno = models.CharField(db_column='TaxRegisterNo', max_length=20, blank=True,
                                     null=True)  # Field name made lowercase.
    calcdiscountonunitprice = models.CharField(db_column='CalcDiscountOnUnitPrice', max_length=1, blank=True,
                                               null=True)  # Field name made lowercase.
    gststatusverifieddate = models.DateTimeField(db_column='GSTStatusVerifiedDate', blank=True,
                                                 null=True)  # Field name made lowercase.
    inclusivetax = models.CharField(db_column='InclusiveTax', max_length=1)  # Field name made lowercase.
    roundingmethod = models.IntegerField(db_column='RoundingMethod')  # Field name made lowercase.
    istaxregistered = models.CharField(db_column='IsTaxRegistered', max_length=1, blank=True,
                                       null=True)  # Field name made lowercase.
    receiptwithholdingtaxcode = models.CharField(db_column='ReceiptWithholdingTaxCode', max_length=14, blank=True,
                                                 null=True)  # Field name made lowercase.
    paymentwithholdingtaxcode = models.CharField(db_column='PaymentWithholdingTaxCode', max_length=14, blank=True,
                                                 null=True)  # Field name made lowercase.
    servicetaxregisterno = models.CharField(db_column='ServiceTaxRegisterNo', max_length=20, blank=True,
                                            null=True)  # Field name made lowercase.
    selfbilledapprovalno = models.CharField(db_column='SelfBilledApprovalNo', max_length=30, blank=True,
                                            null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Debtor'

    def __str__(self):
        return self.accno+self.companyname

class ItemTable(tables.Table):
    class Meta:
        model = Item
        fields = ['itemcode', 'description','baseuom',]

#
class CustomerTable(tables.Table):
    class Meta:
        model = Debtor
        fields = ['accno', 'companyname']