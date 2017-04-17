from django.shortcuts import render
from .models import Category,DataSet
# Create your views here.

def showcategory(request):
    categories = Category.objects.all()
    return render(request, 'DataInventoryMgmt/category.html', {'data':categories})

def datasets(request,category):
    cat = Category.objects.get(title=category)
    data = cat.dataset_set.all()
    print request.user.__dict__
    return render(request, 'DataInventoryMgmt/datasets.html', {'data':data})

def datainfo(request,info):
    datainfo = DataSet.objects.get(slug=info)
    # Converting metadata info to data
    md_list = datainfo.metadata.split(',')
    md_list = map(lambda x : x.split(':'), md_list)
    # Removing empty data
    md_list = filter(lambda x: len(x) > 1, md_list)
    
    #Finding similar datasets
    similar = []
    for elem in datainfo.categories.all():
        for e in elem.dataset_set.all():
            if e != datainfo:
                similar.append(e)
            else:
                pass
    #print(similar)
    
    return render(request, 'DataInventoryMgmt/datainfo.html', {'data':datainfo, 'metadata':md_list, 'similar':similar})

