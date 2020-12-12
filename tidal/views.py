from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from tidal import models
import json

# 将请求定位到index.html文件中

def home(request):
    return tidalRoad(request, '2019-06-14', 'button')

def tidalRoad(request, date, type):
    #获取表格数据 tableData
    tableSet = models.GirdSplice.objects.filter(date=date).values('startCoor', 'endCoor', 'length', 'name')
    tableData = []
    for v in tableSet:
        tmpS = v['startCoor'].split(':')
        tmpE = v['endCoor'].split(':')
        tableData.append({'startCoor': str(round(float(tmpS[0]), 4)) + ':' + str(round(float(tmpS[1]), 4)),
                          'endCoor': str(round(float(tmpE[0]), 4)) + ':' + str(round(float(tmpE[1]), 4)),
                          'name': v['name'], 'length': v['length']})

    #针对指定日期获取潮汐性网格
    numSet = models.DateGrid.objects.filter(date=date).values('gridNum')
    numList = []
    for gird in numSet:
        numList.append(gird['gridNum'])
    #获取潮汐性网格的属性信息 data
    resSet = models.GridAttr.objects.values('gridNum', 'x_coor', 'y_coor', 'longi', 'lati', 'road_name')
    data = []
    for v in resSet:
        num = v['gridNum']
        if num in numList:
            tmp = []
            tmp.append(v['x_coor'])
            tmp.append(v['y_coor'])
            tmp.append(str(round(float(v['longi']), 4)))
            tmp.append(str(round(float(v['lati']), 4)))
            tmp.append(v['road_name'])
            data.append(tmp)
    print(date)
    if type == "ajax":
        return JsonResponse({'data': data, 'tableData': tableData, 'date': json.dumps(date)})
    return render(request, 'tidalRoad.html', {'data': json.dumps(data), 'tableData': json.dumps(tableData), 'date': json.dumps(date)})

def table(request, date, type):
    #获取表格数据 tableData
    tableSet = models.GirdSplice.objects.filter(date=date).values('startCoor', 'endCoor', 'length', 'name')
    tableData = []
    for v in tableSet:
        tmpS = v['startCoor'].split(':')
        tmpE = v['endCoor'].split(':')
        tableData.append({'startCoor': str(round(float(tmpS[0]), 4)) + ':' + str(round(float(tmpS[1]), 4)),
                          'endCoor': str(round(float(tmpE[0]), 4)) + ':' + str(round(float(tmpE[1]), 4)),
                          'name': v['name'], 'length': v['length']})
    print(date)
    if type == "ajax":
        return JsonResponse({'tableData': tableData, 'date': json.dumps(date)})
    return render(request, 'table.html', {'tableData': json.dumps(tableData), 'date': json.dumps(date)})




