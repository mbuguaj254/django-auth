from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

departments=[
('ICT','ICT'),
('Legal','Legal'),
('GRM','GRM'),
('Projects','Projects'),
('HR','HR'),
('HR','HR')
] 
bsc=[('Financial','Financial'),
('Customer','Customer' ),
('Internal Processes', 'Internal Processes'),
('Learning & Growth', 'Learning & Growth'),
('Job Description', 'Job Description'),
]

class User_profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/StaffProfilePic/',null=True,blank=True)
    staff_no = models.CharField(max_length=40)
    job_title = models.CharField(max_length=20,null=True)
    division = models.CharField(max_length=50)
    department= models.CharField(max_length=50,choices=departments,default='ICT')
    section= models.CharField(max_length=50)
    station= models.CharField(max_length=50)
    grade = models.IntegerField()
    years_in_current_grade = models.IntegerField()
    years_in_current_position = models.IntegerField()
    evaluator = models.CharField(max_length=50)
    duration_evaluator_has_supervised_employee = models.CharField(max_length=50)
    assessment_period =models.IntegerField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name

class Goal(models.Model):
    user=models.ManyToManyField(User)
    bsc=models.CharField(max_length=50,choices=bsc,default='Financial')
    total_bsc_weight=models.IntegerField()
    strategic_initiative=models.CharField(max_length=50)
    initiative_weight=models.IntegerField()
    kpi=models.CharField(max_length=50)
    target=models.CharField(max_length=50)

    

