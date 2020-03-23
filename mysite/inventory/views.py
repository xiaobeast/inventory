from django.shortcuts import render, render_to_response
from inventory.models import Item, Inventory, StockBill
from django.http import HttpResponseRedirect, HttpResponse


# 通过物料名称查找库存
def getInventoryByItemName(request, itemName):
    inventorys = None
    # 输入物料名称，依据模糊匹配模式显示所有匹配的物料库存，用列表的方式显示在界面上
    if itemName:
        inventorys = Inventory.objects.filter(item__itemName__contains=itemName)
    # 不输入查询条件时，点击查询按钮返回当前所有的物料库存数据
    else:
        inventorys = Inventory.objects.all()
    return inventorys


def inventoryQuery(request):
    '''查询功能'''
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        elif len(q) > 20:
            error = True
        else:
            inventorys = getInventoryByItemName('', q)
            return render_to_response('inventory/inventoryQuery.html',
                                      {'inventorys': inventorys, 'query': q})
    return render_to_response('inventory/inventoryQuery.html')


def add_stock_bill(request):
    errors = []
    items = Item.objects.all()
    ItemId = ''
    if request.method == 'POST':
        if not request.POST.get('stockBillCode', ''):
            errors.append('请输入入库单号!')
        if not request.POST.get('stockDate', ''):
            errors.append('请输入入库时间!')
        if not request.POST.get('amount', ''):
            errors.append('请输入入库数量!')
        if not request.POST.get('operator', ''):
            errors.append('请输入入库人员姓名!')
        else:
            ItemId = int(request.POST.get('itemId', ''))
        if not errors:
            add_stock_bill = StockBill()
            add_stock_bill.stockBillCode = request.POST.get('stockBillCode', '')
            add_stock_bill.stockDate = request.POST.get('stockDate', '')
            add_stock_bill.amount = request.POST.get('amount', '')
            add_stock_bill.operator = request.POST.get('operator', '')
            # ItemId = request.POST.get('itemId', '')
            add_stock_bill.item = Item.objects.get(itemId=ItemId)  # 注意物料需要保持Model对象
            add_stock_bill.save()
            return HttpResponseRedirect('/success/')
    return render(request, 'inventory/add_stock_bill.html',
                  {'errors': errors, 'items':items,
                   'stockBillCode':request.POST.get('stockBillCode', ''),
                   'stockDate':request.POST.get('stockDate', ''),
                   'amount': request.POST.get('amount', ''),
                   'itemId': ItemId,
                   'operator': request.POST.get('operator', '')})


def success(request):
    return HttpResponse('入库成功！')

# 更新入库后的库存量
def updatingInventoryIn(request, stockBill, inventory):
    if (inventory.inventoryId == None):
        inventory.item = stockBill.item
        inventory.amount = 0
    inventory.amount += stockBill.amount


#
def getInventoryByItem(request, item):
    if (item != None):
        inventorys = item.inventory_set.all()
        if (inventorys.count() == 0):
            currentInventory = Inventory()
        else:
            currentInventory = inventorys[0]
    return currentInventory


