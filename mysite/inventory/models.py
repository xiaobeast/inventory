from django.db import models


# Create your models here.
class Item(models.Model):
    '''物料类'''
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=50)
    item_model = models.CharField(max_length=50)
    remark = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.item_name


class Inventory(models.Model):
    '''物料库存类'''
    inventory_id = models.AutoField(primary_key=True)
    inventory_item = models.ForeignKey(Item, null=False)  # 和物料一对一
    inventory_position = models.CharField(max_length=50)
    inventory_amount = models.IntegerField(null=True)
    inventory_max_amount = models.IntegerField(null=True)
    inventory_min_amount = models.IntegerField(null=True)

    # def __str__(self):
    #     return self.item


class Bill(models.Model):
    '''出入库单类'''
    bill_id = models.AutoField(primary_key=True)
    bill_code = models.CharField(max_length=40)
    bill_date = models.DateTimeField(null=True)
    bill_operator = models.CharField(max_length=40)
    bill_item = models.ForeignKey(Item, null=False)  # 与物料是一对多的关系
    bill_amount = models.IntegerField(null=True)