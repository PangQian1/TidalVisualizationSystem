from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import  HttpResponse
from django.http import JsonResponse
from tidal import models
import json

# 将请求定位到index.html文件中

def home(request):
    date = '2019-06-14'
    numSet = models.DateGrid.objects.filter(date=date).values('gridNum')
    numList = []
    for gird in numSet:
        numList.append(gird['gridNum'])
    resSet = models.GridAttr.objects.values('gridNum', 'x_coor', 'y_coor', 'road_name')
    data = []
    for v in resSet:
        num = v['gridNum']
        if num in numList:
            tmp = []
            tmp.append(v['x_coor'])
            tmp.append(v['y_coor'])
            tmp.append(v['road_name'])
            data.append(tmp)
    return render(request, 'road.html', {'data': json.dumps(data)})

def tidalRoad(request, date):
    numSet = models.DateGrid.objects.filter(date=date).values('gridNum')
    numList = []
    for gird in numSet:
        numList.append(gird['gridNum'])
    resSet = models.GridAttr.objects.values('gridNum', 'x_coor', 'y_coor', 'road_name')
    data = []
    for v in resSet:
        num = v['gridNum']
        if num in numList:
            tmp = []
            tmp.append(v['x_coor'])
            tmp.append(v['y_coor'])
            tmp.append(v['road_name'])
            data.append(tmp)

    #if type == "ajax":
        #return JsonResponse({'data': json.dumps(data), 'date': date})
    return render(request, 'road.html', {'data': json.dumps(data), 'date': date})