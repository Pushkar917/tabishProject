from django.db import models
from django.utils.translation import gettext_lazy as _


class CryoCart(models.Model):
    assetID = models.CharField(verbose_name=_("Asset ID"), max_length=50, null=False) 
    asset_status = models.CharField(verbose_name=_("Asset Qualification Status"), max_length=50, null=False)
    functional_area = models.CharField(verbose_name=_("functional_area"), max_length=50, null=False) 
    pm_contact = models.CharField(verbose_name=_("PM Contact"), max_length=50, null=False)
    product = models.CharField(verbose_name=_("product"), max_length=50, null=False) 
    execution_priority = models.CharField(verbose_name=_("Execution Priority"), max_length=50, null=True) 
    charge_control = models.CharField(verbose_name=_("Change Control"), max_length=50, null=True) 
    location = models.CharField(verbose_name=_("Location"), max_length=50, null=False) 
    manufacturer = models.CharField(verbose_name=_("Manufacturer"), max_length=50, null=False)
    serial_number = models.IntegerField(verbose_name=_("S/N"), null=False)
    model = models.CharField(verbose_name=_("Model"), max_length=50, null=False)
    firmware_software_version = models.CharField(verbose_name=_("Firmware/Software Version"), max_length=50, null=True)
    equipment_class = models.CharField(verbose_name=_("Equipment Class"), max_length=50, null=False) 
    system_owner = models.CharField(verbose_name=_("System Owner"), max_length=50, null=False)


    def __str__(self):
        return f"{self.assetID}'s CryoCart"



class Implementation_crypto(models.Model):
    cryocart = models.ForeignKey(CryoCart, on_delete=models.CASCADE)
    bemsmonitoring = models.CharField(verbose_name=_("BEMS Monitoring"), max_length=50, null=False) 
    bmramInrollment = models.CharField(verbose_name=_("BMRAM Inrollment"), max_length=50, null=False) 
    brmram_PM_Cal = models.CharField(verbose_name=_("BMRAM PM/Cal"), max_length=50, null=False) 
    regul_determination_status = models.CharField(verbose_name=_("Regulatory Determination Status"), max_length=50, null=False) 
    regul_determination_form_no = models.CharField(verbose_name=_("Regulatory Determination(Form-001404) Number"), max_length=50, null=False) 
    installation_status = models.CharField(verbose_name=_("Installation Status"), max_length=50, null=False) 
    config_specific_status = models.CharField(verbose_name=_("Configuration Specification Status"), max_length=50, null=True) 
    config_specific_number = models.CharField(verbose_name=_("Configuration Specification Number"), max_length=50, null=True) 
    urs_number = models.CharField(verbose_name=_("URS Number"), max_length=50, null=True) 
    urs_status = models.CharField(verbose_name=_("URS Status"), max_length=50, null=True)
    operational_sop = models.CharField(verbose_name=_("operational_sop"), max_length=50, null=True)  
    operational_sop_number = models.CharField(verbose_name=_("Operational SOP Number"), max_length=50, null=True)
    maintaienance_sop_status = models.CharField(verbose_name=_("Maintenance SOP Status"), max_length=50, null=True)  
    maintaienance_sop_number = models.CharField(verbose_name=_("Maintenance SOP Number"), max_length=50, null=True)  
    admin_sop_status = models.CharField(verbose_name=_("Admin SOP Status"), max_length=50, null=True)   
    admin_sop_number = models.CharField(verbose_name=_("Admin SOP Number"), max_length=50, null=True) 
    logbook = models.CharField(verbose_name=_("Logbook"), max_length=50, null=True) 
    it_form_0024_status = models.CharField(verbose_name=_("IT-FRM-0024 Status"), max_length=50, null=True) 
    it_form_0024_number = models.CharField(verbose_name=_("IT-FRM-0024 Number"), max_length=50, null=True)   
    


    def __str__(self):
        return f"{self.cryocart}'s implementation"

