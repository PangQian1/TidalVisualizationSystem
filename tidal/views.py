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
    numSet = models.DateGrid.objects.filter(date=date).values('gridNum')
    numList = []
    for gird in numSet:
        numList.append(gird['gridNum'])
    resSet = models.GridAttr.objects.values('gridNum', 'x_coor', 'y_coor', 'longi', 'lati', 'road_name')
    data = []
    for v in resSet:
        num = v['gridNum']
        if num in numList:
            tmp = []
            tmp.append(v['x_coor'])
            tmp.append(v['y_coor'])
            tmp.append(v['longi'])
            tmp.append(v['lati'])
            tmp.append(v['road_name'])
            data.append(tmp)
    print(date)
    if type == "ajax":
        return JsonResponse({'data': data, 'date': json.dumps(date)})
    return render(request, 'tidalRoad.html', {'data': json.dumps(data), 'date': json.dumps(date)})