from django.db import models
from Core.models import *
from LabTest.models import *
from Radiology.models import *
from Diet.models import *
from Medicines.models import *
from django.db.models import Sum
from PhysicalTherapy.models import Device, Exercise


# Create your models here.
class Complain(models.Model):
    name = models.CharField(verbose_name="الشكوي", max_length=128)

    def __str__(self):
        return self.name


class Disease(models.Model):
    name = models.CharField(verbose_name='المرض', max_length=128)

    def __str__(self):
        return self.name


class Diagnosis(models.Model):
    name = models.CharField(verbose_name='التشخيص', max_length=128)

    def __str__(self):
        return self.name


class CancerType(models.Model):
    name = models.CharField(verbose_name='نوع السرطان', max_length=128)

    def __str__(self):
        return self.name


class Patient(models.Model):
    gender_choices = (
        (1, 'ذكر'),
        (2, 'أنثي')
    )
    martial_status_choices = (
        (1, 'أعزب / آنسة'),
        (2, 'متزوج/ة'),
        (3, 'مطلق/ة'),
        (4, 'أرمل/أرملة'),
    )
    blood_group_choices = (
        (1, 'A+'),
        (2, 'A-'),
        (3, 'AB+'),
        (4, 'AB-'),
        (5, 'B+'),
        (6, 'B-'),
        (7, 'O+'),
        (8, 'O-'),
    )
    instance = models.ForeignKey(Instance, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=128, verbose_name='الاسم')
    gender = models.IntegerField(choices=gender_choices, verbose_name='الجنس')
    birthday = models.DateField(verbose_name='تاريخ الميلاد', null=True, blank=True)
    email = models.EmailField(verbose_name='البريد الإلكتروني', null=True, blank=True)
    telephone = models.CharField(max_length=11, verbose_name='رقم الهاتف', null=True, blank=True)
    job = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='الوظيفة')
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='المدينة')
    area = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='المنطقة')
    patient_history = models.ManyToManyField(Disease, verbose_name='التاريخ المرضي', blank=True)
    visits = models.IntegerField(verbose_name='الزيارات', default=0)
    electricity_img = models.ImageField(upload_to='electricity/', verbose_name='صورة الكهرباء', null=True, blank=True)
    added_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإضافة')
    deleted = models.BooleanField(default=False, verbose_name='حذف')

    def __str__(self):
        return self.name

    def balance(self):
        invoices = self.invoice_set.all()
        if invoices:
            balance = invoices.aggregate(balance=Sum('after_discount')-Sum('paid'))
            return balance['balance']
        else:
            return 0

    def get_last_height(self):
        heights = self.heightandweight_set.all()
        last_height = heights.last()
        return last_height

    def get_last_visit(self):
        return self.patientinvestigation_set.last()


class PatientViralProcess(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='المريض')
    added_at = models.DateTimeField(auto_now_add=True, verbose_name='التاريخ')
    temperature = models.FloatField(verbose_name='درجة الحرارة', null=True, blank=True)
    Pulse = models.FloatField(verbose_name='معدل النبض', null=True, blank=True)
    blood_pressure_high = models.IntegerField(verbose_name='الضغط الانقباضي', null=True, blank=True)
    blood_pressure_low = models.IntegerField(verbose_name='الضغط الانبساطي', null=True, blank=True)
    respiratory_rate = models.IntegerField(verbose_name='معدل التنفس', null=True, blank=True)

    def __str__(self):
        return self.patient.name

    class Meta:
        ordering = ['added_at']


class HeightAndWeight(models.Model):
    weight_status_choices = (
        (1, 'تحت الوزن الطبيعي'),
        (2, 'طبيعي'),
        (3, 'وزن زائد'),
        (4, 'سمنة I'),
        (5, 'سمنة II'),
        (6, 'سمنة III')
    )
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='المريض')
    added_at = models.DateTimeField(auto_now_add=True, verbose_name='التاريخ')
    height = models.FloatField(verbose_name='الطول بالـ cm')
    weight = models.FloatField(verbose_name='الوزن بالـ kg')
    bmi = models.FloatField(verbose_name='معدل الكتلة', null=True, blank=True)
    weight_status = models.IntegerField(choices=weight_status_choices, verbose_name='حالة الوزن', null=True, blank=True)

    def __str__(self):
        return self.patient.name

    def calculate_bmi(self):
        bmi = self.weight / ((self.height / 100) * (self.height / 100))
        self.bmi = bmi
        if bmi <= 18.4:
            self.weight_status_choices = 1
        elif 18.5 <= bmi <= 24.9:
            self.weight_status_choices = 2
        elif 25 <= bmi <= 29.9:
            self.weight_status_choices = 3
        elif 30 <= bmi <= 34.9:
            self.weight_status_choices = 4
        elif 35 <= bmi <= 39.9:
            self.weight_status_choices = 5
        elif bmi >= 40:
            self.weight_status_choices = 6
        self.save()
        return bmi

    class Meta:
        ordering = ['added_at']


class PatientInvestigation(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='المريض')
    added_at = models.DateTimeField(auto_now_add=True)
    complain = models.ForeignKey(Complain, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='الشكوي')
    diagnosis = models.ForeignKey(Diagnosis, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='التشخيص')
    devices = models.ManyToManyField(Device, blank=True, verbose_name='الأجهزة')
    exercises = models.ManyToManyField(Exercise, blank=True, verbose_name='التمرينات')
    medical_plan = models.TextField(verbose_name='الخطة العلاجية', null=True, blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ['added_at']


class MedicalPrescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='المريض')
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ['added_at']


class PatientHistory(models.Model):
    history_type_choices = (
        (1, 'كشف'),
        (2, 'تسجيل عمليات حيوية'),
        (3, 'تسجيل وزن وطول'),
        (4, 'روشتة'),
        (5, 'طلب تحاليل'),
        (6, 'طلب آشعة'),

    )
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='المريض')
    added_at = models.DateTimeField(auto_now_add=True)
    note = models.TextField()

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ['added_at']


class LabTestRequest(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='المريض')
    added_at = models.DateTimeField(auto_now_add=True)
    lab_test = models.ForeignKey(LabTest, on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name='التحليل المطلوب')

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ['added_at']


class LabTestResult(models.Model):
    lab_test = models.ForeignKey(LabTestRequest, on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name='التحليل')
    attribute = models.ForeignKey(LabTestAttribute, on_delete=models.CASCADE, verbose_name='الخاصية')
    value = models.FloatField(verbose_name='القيمة', null=True, blank=True)

    def __str__(self):
        return str(self.id)


class LabTestImages(models.Model):
    lab_test = models.ForeignKey(LabTestRequest, on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name='التحليل')
    image = models.ImageField(verbose_name='الصورة')
    added_at = models.DateTimeField(auto_now_add=True, verbose_name='التاريخ', null=True)

    def __str__(self):
        return str(self.id)


class RadiologyRequest(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True, verbose_name='المريض')
    radiology = models.ForeignKey(Radiology, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='الآشعة')
    added_at = models.DateTimeField(auto_now_add=True, verbose_name='التاريخ', null=True)

    def __str__(self):
        return str(self.id)


class RadiologyResult(models.Model):
    radiology = models.ForeignKey(RadiologyRequest, on_delete=models.CASCADE, null=True, blank=True,
                                  verbose_name='الآشعة')
    comment = models.TextField(verbose_name='الملخص')
    added_at = models.DateTimeField(auto_now_add=True, verbose_name='التاريخ', null=True)

    def __str__(self):
        return str(self.id)


class RadiologyImages(models.Model):
    radiology = models.ForeignKey(RadiologyRequest, on_delete=models.SET_NULL, null=True, blank=True,
                                  verbose_name="الآشعة")
    image = models.ImageField(verbose_name='الصورة')
    added_at = models.DateTimeField(auto_now_add=True, verbose_name='التاريخ', null=True)

    def __str__(self):
        return str(self.id)


class Session(models.Model):
    added_at = models.DateTimeField(auto_now_add=True, verbose_name='التاريخ')
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    instance = models.ForeignKey(Instance, on_delete=models.CASCADE, null=True, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
    devices = models.ManyToManyField(Device, verbose_name='الأجهزة المستخدمة')
    exercises = models.ManyToManyField(Exercise, verbose_name='التمارين المستخدمة')

    def __str__(self):
        return str(self.id)


class PatientDiet(models.Model):
    added_at = models.DateTimeField(auto_now_add=True, verbose_name='التاريخ')
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    instance = models.ForeignKey(Instance, on_delete=models.CASCADE, null=True, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True, verbose_name='المريض')
    diet = models.ForeignKey(Diet, on_delete=models.CASCADE, null=True, blank=True, verbose_name='النظام الغذائي')
    description = models.TextField(verbose_name='وصف النظام', null=True, blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ['id']


class Prescription(models.Model):
    added_at = models.DateTimeField(auto_now_add=True, verbose_name='التاريخ')
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    instance = models.ForeignKey(Instance, on_delete=models.CASCADE, null=True, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True, verbose_name='المريض')

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ['id']


class PrescriptionItem(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE, null=True, blank=True)
    medicine = models.ForeignKey(Medicine, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='الدواء')
    dose = models.ForeignKey(Dose, on_delete=models.SET_NULL, null=True, verbose_name='الجرعة')
    timing = models.ForeignKey(Timing, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='التوقيت')

    def __str__(self):
        return self.medicine.trade_name + ' - ' + self.dose.__str__() + ' - ' + self.timing.__str__()


class PatientImage(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    img = models.ImageField(verbose_name='الصورة', upload_to='upload/patient_images/')
    added_at = models.DateTimeField(auto_now_add=True, verbose_name='التاريخ')
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.id)

