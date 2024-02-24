from django.db import models

# Create your models here.
class giamhieu(models.Model):
    giamhieu_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,null=False)
    chuc_vu=models.CharField(max_length=50,null=False)
    sdt=models.CharField(max_length=12,null=False)
    email=models.CharField(max_length=50,null=False)
    nhiem_vu=models.CharField(max_length=100,null=False)
    anh=models.ImageField(upload_to='img',null=False,default=None)

    def __str__(self):
        return f"{self.giamhieu_id},{self.name},{self.chuc_vu},{self.sdt},{self.email},{self.nhiem_vu},{self.anh}"
    
class comments(models.Model):
    cmt_id=models.AutoField(primary_key=True)
    cmt=models.CharField(max_length=1000,null=False)
    ho_ten=models.CharField(max_length=50,null=False)

    def __str__(self):
        return f"{self.cmt_id},{self.cmt},{self.ho_ten}"