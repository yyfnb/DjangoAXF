from django.db import models

# Create your models here.

#基础类
class Base(models.Model):
    #图片
    img = models.CharField(max_length=100)
    #name
    name = models.CharField(max_length=100)
    #id
    trackid = models.CharField(max_length=10)

    class Meta:
        abstract = True


#lunbotu
class Wheel(Base):
    class Meta:
        db_table = 'axf_wheel'

#daohang
class Nav(Base):
    class Meta:
        db_table = 'axf_nav'
#mustbay
class Mustbuy(Base):
    class Meta:
        db_table = 'axf_mustbuy'


class Shop(Base):
    class Meta:
        db_table = 'axf_shop'

# 商品主体内容

class MainShow(models.Model):
    trackid = models.CharField(max_length=8)
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    categoryid = models.CharField(max_length=8)
    brandname = models.CharField(max_length=50)

    img1 = models.CharField(max_length=100)
    childcid1 = models.CharField(max_length=8)
    productid1 = models.CharField(max_length=8)
    longname1 = models.CharField(max_length=100)
    price1 = models.FloatField()
    marketprice1 = models.FloatField()

    img2 = models.CharField(max_length=100)
    childcid2 = models.CharField(max_length=8)
    productid2 = models.CharField(max_length=8)
    longname2 = models.CharField(max_length=100)
    price2 = models.FloatField()
    marketprice2 = models.FloatField()

    img3 = models.CharField(max_length=100)
    childcid3 = models.CharField(max_length=8)
    productid3 = models.CharField(max_length=8)
    longname3 = models.CharField(max_length=100)
    price3 = models.FloatField()
    marketprice3 = models.FloatField()

    class Meta:
        db_table = 'axf_mainshow'

# 商品分类

class Foodtypes(models.Model):
    typeid = models.CharField(max_length=8) # 分类ID
    typename = models.CharField(max_length=100) # 分类名称
    childtypenames = models.CharField(max_length=256)   # 子类名称
    typesort = models.IntegerField()    # 显示先后顺序
    class Meta:
        db_table = 'axf_foodtypes'

# 商品信息
class Goods(models.Model):
    productid = models.CharField(max_length=10) # 商品ID
    productimg = models.CharField(max_length=100)   # 商品图片
    productname = models.CharField(max_length=100)  # 商品名称
    productlongname = models.CharField(max_length=100)  # 商品弄名称
    isxf = models.BooleanField(default=False)    # 精选
    pmdesc = models.BooleanField(default=False)  # 买一送一
    specifics = models.CharField(max_length=100)   # 规格
    price = models.DecimalField(max_digits=7, decimal_places=2)    # 价格
    marketprice = models.DecimalField(max_digits=7, decimal_places=2)  # 商场价格
    categoryid= models.IntegerField()   # 分类ID
    childcid = models.IntegerField()    # 子类ID
    childcidname = models.CharField(max_length=100) # 分类名称
    dealerid = models.CharField(max_length=10)  # 详情ID
    storenums = models.IntegerField()   # 库存
    productnum = models.IntegerField()  # 销量

    class Meta:
        db_table = 'axf_goods'

