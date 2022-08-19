from django.shortcuts import render
<<<<<<< HEAD
=======
import numpy as np
>>>>>>> first upload
import pandas as pd

def index(request):
    file = 1
    return render(request, 'form.html',{'name':file})

def excel(request):
    file = request.FILES.get("excel_file")
    df = pd.read_excel(file)
    x=0
    for c in df['one']:

        if df['math'][x]=='plus':
            df['answer'][x] = c + df['two'][x]
        elif df['math'][x]=='minus':
            df['answer'][x] = c - df['two'][x]
        elif df['math'][x]=='bibided':
            df['answer'][x] = c / df['two'][x]
        x+=1

    dx = pd.DataFrame(df)
    mydict = {
        "df": dx.to_html()
    }
<<<<<<< HEAD
    return render(request, 'form.html',context=mydict)
=======
    return render(request, 'form.html',context=mydict)

def indnum(request):
    return render(request, 'forma1.html')

def numpy(request):
    file = request.FILES.get("excel_file")
    df = pd.read_excel(file)

    df['average'] = df.mean(axis=1)

    coditions=[
        (df['average'] >= 90),
        (df['average'] < 90) & (df['average'] >= 80),
        (df['average'] < 80) & (df['average'] >= 70),
        (df['average'] < 70) & (df['average'] >= 80),
        (df['average'] < 60),
    ]
    results=['A','B','C','D','F']

    df['letter grade'] = np.select(coditions , results)

    dx = pd.DataFrame(df)
    mydict = {
        "df": dx.to_html()
    }
    return render(request, 'forma1.html',context=mydict)
>>>>>>> first upload
