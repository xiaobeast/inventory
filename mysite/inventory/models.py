from django.db import models


# Create your models here.
class Item(models.Model):
    '''物料类'''
    itemId = models.AutoField(primary_key=True)
    itemName = models.CharField(max_length=50)
    itemModel = models.CharField(max_length=50)
    remark = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.itemName


class Inventory(models.Model):
    '''物料库存类'''
    inventoryId = models.AutoField(primary_key=True)
    item = models.ForeignKey(Item, null=False)  # 和物料一对一
    position = models.CharField(max_length=50)
    amount = models.IntegerField(null=True)
    max_amount = models.IntegerField(null=True)
    min_amount = models.IntegerField(null=True)

    # def __str__(self):
    #     return self.item


class StockBill(models.Model):
    '''出入库单类'''
    stockBillId = models.AutoField(primary_key=True)
    stockBillCode = models.CharField(max_length=40)
    stockDate = models.DateTimeField(null=True)
    operator = models.CharField(max_length=40)
    item = models.ForeignKey(Item, null=False)  # 与物料是一对多的关系
    amount = models.IntegerField(null=True)