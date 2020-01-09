from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from django.http import Http404, HttpResponse
from rest_framework import status, renderers, viewsets

# 데이터 형식 가공
from rest_framework.decorators import action
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.svm import SVC
import numpy as np
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
import plotly.graph_objects as go
import os
import csv

#---설치한 라이브러리-----------------------------------------------------------
    #https://plot.ly/python/static-image-export/
    #conda install -c plotly plotly-orca psutil requests
    #pip install ipython
    #pip install notebook
    #pip install ipywidgets
    #pip install psutil requests
    #In most situations, you can omit the call to .show() and allow the figure to display itself.
#-------------------------------------------------------------------------



# -*- coding: utf-8 -*-
class PostViewSet(viewsets.ReadOnlyModelViewSet): #crud가능
    queryset = Post.objects.all()
    serializer_class = PostSerializer

#-----------------------------------------------------------------------------------
# 모델의 예측률을 보여주는 api : showmodel
# https://nachwon.github.io/django-12-post-detail/

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer]) 
    def showmodel(self, *args, **kwargs):
        DIR='/Users/corgi/Desktop/cnu/firstrest/post/data'
        train = pd.read_csv(DIR+'/train.csv', delimiter=',')  #  파일 경로를 절대 경로로 할 것
         
        k_fold = KFold(n_splits=10, shuffle=True, random_state=0)
        train_data = train.drop('우울증정도(0,1,2)', axis=1) 
        target = train['우울증정도(0,1,2)']

        #6.2.5 SVM
        clf = SVC()
        scoring = 'accuracy'
        score = cross_val_score(clf, train_data, target, cv=k_fold, n_jobs=1, scoring=scoring)
        return HttpResponse(round(np.mean(score)*100,2))
        #httpResponse를 할 때는 return을 꼭 해줄 것

#-------------------------------------------------------------------------------------------
# 모델에 저장된 데이터를 -> csv파일에 추가하기(post 요청)
# 우울증 진단 작성 후 -> 결과보기 클릭시 -> csv파일에 새로운 데이터가 추가된다.

    @action(methods=['post'], detail=True, renderer_classes=[renderers.StaticHTMLRenderer]) 
    def insertcsv(self, *args, **kwargs):
        DIR='/Users/corgi/Desktop/cnu/firstrest/post/data'   #절대경로
        f = open(DIR+'/train.csv','a', newline='')
        wr = csv.writer(f)
        # 데이터 형식 : 우울증 진단 /설문1~20 | 입력된 정보가 추가된다.
        wr.writerow([0,2,1,0,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2])
        
        f.close()

#-------------------------------------------------------------------------------------------
    #각 항목에 해당하는 그래프들을 이미지로 저장하는 api : 우울증과 귀찮음 drawbother 
    #호출시 이미지로 저장되므로, 프론트 상에서는 이미지만 불러오면 된다.(불러올때마다 새로운 이미지로 덮어짐)
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer]) 

    def drawbother(self, *args, **kwargs):
        DIR='/Users/corgi/Desktop/cnu/firstrest/post/data'
        train = pd.read_csv(DIR+'/train.csv', delimiter=',')  # 파일 경로를 절대 경로로 할 것
        sns.set()

        #---코드 예시-----------------------------------------------
        #pandas의 경우 조건에 해당하는 데이터프레임이 boolean형태로 가져와짐 -> count시 list로 변환하여 갯수를 셈
        #tests = train.ix[train['우울증정도(0,1,2)'] == 0, ['귀찮음']]
        #listst = list(tests['귀찮음'] == 1)
        #return HttpResponse(listst.count(True))
        #---------------------------------------------------------

        # 우울증0과 귀찮음
        row_both_0 = train.ix[train['우울증정도(0,1,2)'] == 0, ["귀찮음"]]
        row_both_ls_00 = list(row_both_0['귀찮음'] == 0)
        row_both_ls_00_count = row_both_ls_00.count(True)

        row_both_ls_01 = list(row_both_0['귀찮음'] == 1)
        row_both_ls_01_count = row_both_ls_01.count(True)

        row_both_ls_02 = list(row_both_0['귀찮음'] == 2)
        row_both_ls_02_count = row_both_ls_02.count(True)

        row_both_ls_03 = list(row_both_0['귀찮음'] == 3)
        row_both_ls_03_count = row_both_ls_03.count(True)


        # 우울증1과 귀찮음
        row_both_1 = train.ix[train['우울증정도(0,1,2)'] == 1, ["귀찮음"]]
        row_both_ls_10 = list(row_both_1['귀찮음'] == 0)
        row_both_ls_10_count = row_both_ls_10.count(True)

        row_both_ls_11 = list(row_both_1['귀찮음'] == 1)
        row_both_ls_11_count = row_both_ls_11.count(True)

        row_both_ls_12 = list(row_both_1['귀찮음'] == 2)
        row_both_ls_12_count = row_both_ls_12.count(True)

        row_both_ls_13 = list(row_both_1['귀찮음'] == 3)
        row_both_ls_13_count = row_both_ls_13.count(True)


        # 우울증2과 귀찮음
        row_both_2 = train.ix[train['우울증정도(0,1,2)'] == 2, ["귀찮음"]]
        row_both_ls_20 = list(row_both_2['귀찮음'] == 0)
        row_both_ls_20_count = row_both_ls_20.count(True)

        row_both_ls_21 = list(row_both_2['귀찮음'] == 1)
        row_both_ls_21_count = row_both_ls_21.count(True)

        row_both_ls_22 = list(row_both_2['귀찮음'] == 2)
        row_both_ls_22_count = row_both_ls_22.count(True)

        row_both_ls_23 = list(row_both_2['귀찮음'] == 3)
        row_both_ls_23_count = row_both_ls_23.count(True)
   
        results = ["경증", "중증", "심각"]  #경증, 중증, 삼각

        fig = go.Figure(data=[
            go.Bar(name='귀찮음0', x=results, y=[row_both_ls_00_count, row_both_ls_10_count, row_both_ls_20_count]),
            go.Bar(name='귀찮음1', x=results, y=[row_both_ls_01_count, row_both_ls_11_count, row_both_ls_21_count]),
            go.Bar(name='귀찮음2', x=results, y=[row_both_ls_02_count, row_both_ls_12_count, row_both_ls_22_count]),
            go.Bar(name='귀찮음3', x=results, y=[row_both_ls_03_count, row_both_ls_13_count, row_both_ls_23_count])
        ])
   
        fig.update_layout(barmode='stack')
        fig.write_image("/Users/corgi/Desktop/cnu/firstrest/post/data/images/fig_bother.png") #저장할 파일명과 절대 경로  
        return HttpResponse(fig.show())
        

#--------------------------------------------------------------------------------------------
    #각 항목에 해당하는 그래프들을 이미지로 저장하는 api : 우울증과 입맛없음 drawnoeat 
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer]) 
    def drawnoeat(self, *args, **kwargs):

        DIR='/Users/corgi/Desktop/cnu/firstrest/post/data'
        train = pd.read_csv(DIR+'/train.csv', delimiter=',')
        
        sns.set()
    
        # 우울증0과 입맛없음
        row_noeat_0 = train.ix[train['우울증정도(0,1,2)'] == 0, ["입맛없음"]]
        row_noeat_ls_00 = list(row_noeat_0['입맛없음'] == 0)
        row_noeat_ls_00_count = row_noeat_ls_00.count(True)

        row_noeat_ls_01 = list(row_noeat_0['입맛없음'] == 1)
        row_noeat_ls_01_count = row_noeat_ls_01.count(True)

        row_noeat_ls_02 = list(row_noeat_0['입맛없음'] == 2)
        row_noeat_ls_02_count = row_noeat_ls_02.count(True)

        row_noeat_ls_03 = list(row_noeat_0['입맛없음'] == 3)
        row_noeat_ls_03_count = row_noeat_ls_03.count(True)


        # 우울증1과 입맛없음
        row_noeat_1 = train.ix[train['우울증정도(0,1,2)'] == 1, ["입맛없음"]]
        row_noeat_ls_10 = list(row_noeat_1['입맛없음'] == 0)
        row_noeat_ls_10_count = row_noeat_ls_10.count(True)

        row_noeat_ls_11 = list(row_noeat_1['입맛없음'] == 1)
        row_noeat_ls_11_count = row_noeat_ls_11.count(True)

        row_noeat_ls_12 = list(row_noeat_1['입맛없음'] == 2)
        row_noeat_ls_12_count = row_noeat_ls_12.count(True)

        row_noeat_ls_13 = list(row_noeat_1['입맛없음'] == 3)
        row_noeat_ls_13_count = row_noeat_ls_13.count(True)


        # 우울증2과 입맛없음
        row_noeat_2 = train.ix[train['우울증정도(0,1,2)'] == 2, ["입맛없음"]]
        row_noeat_ls_20 = list(row_noeat_2['입맛없음'] == 0)
        row_noeat_ls_20_count = row_noeat_ls_20.count(True)

        row_noeat_ls_21 = list(row_noeat_2['입맛없음'] == 1)
        row_noeat_ls_21_count = row_noeat_ls_21.count(True)

        row_noeat_ls_22 = list(row_noeat_2['입맛없음'] == 2)
        row_noeat_ls_22_count = row_noeat_ls_22.count(True)

        row_noeat_ls_23 = list(row_noeat_2['입맛없음'] == 3)
        row_noeat_ls_23_count = row_noeat_ls_23.count(True)
   
        results = ["경증", "중증", "심각"]  #경증, 중증, 삼각

        fig = go.Figure(data=[
            go.Bar(name='입맛없음0', x=results, y=[row_noeat_ls_00_count, row_noeat_ls_10_count, row_noeat_ls_20_count]),
            go.Bar(name='입맛없음1', x=results, y=[row_noeat_ls_01_count, row_noeat_ls_11_count, row_noeat_ls_21_count]),
            go.Bar(name='입맛없음2', x=results, y=[row_noeat_ls_02_count, row_noeat_ls_12_count, row_noeat_ls_22_count]),
            go.Bar(name='입맛없음3', x=results, y=[row_noeat_ls_03_count, row_noeat_ls_13_count, row_noeat_ls_23_count])
        ])
   
        fig.update_layout(barmode='stack')
        fig.write_image("/Users/corgi/Desktop/cnu/firstrest/post/data/images/fig_noeat.png") #저장할 파일명과 절대 경로  
        return HttpResponse(fig.show())


#--------------------------------------------------------------------------------------------
    #각 항목에 해당하는 그래프들을 이미지로 저장하는 api : 우울증과 울적한기분 drawdepr
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer]) 
    def drawdepr(self, *args, **kwargs):

        DIR='/Users/corgi/Desktop/cnu/firstrest/post/data'
        train = pd.read_csv(DIR+'/train.csv', delimiter=',')
        
        sns.set()
    
        # 우울증0과 울적함
        row_depr_0 = train.ix[train['우울증정도(0,1,2)'] == 0, ["울적한기분"]]
        row_depr_ls_00 = list(row_depr_0['울적한기분'] == 0)
        row_depr_ls_00_count = row_depr_ls_00.count(True)

        row_depr_ls_01 = list(row_depr_0['울적한기분'] == 1)
        row_depr_ls_01_count = row_depr_ls_01.count(True)

        row_depr_ls_02 = list(row_depr_0['울적한기분'] == 2)
        row_depr_ls_02_count = row_depr_ls_02.count(True)

        row_depr_ls_03 = list(row_depr_0['울적한기분'] == 3)
        row_depr_ls_03_count = row_depr_ls_03.count(True)


        # 우울증1과 울적함
        row_depr_1 = train.ix[train['우울증정도(0,1,2)'] == 1, ["울적한기분"]]
        row_depr_ls_10 = list(row_depr_1['울적한기분'] == 0)
        row_depr_ls_10_count = row_depr_ls_10.count(True)

        row_depr_ls_11 = list(row_depr_1['울적한기분'] == 1)
        row_depr_ls_11_count = row_depr_ls_11.count(True)

        row_depr_ls_12 = list(row_depr_1['울적한기분'] == 2)
        row_depr_ls_12_count = row_depr_ls_12.count(True)

        row_depr_ls_13 = list(row_depr_1['울적한기분'] == 3)
        row_depr_ls_13_count = row_depr_ls_13.count(True)


        # 우울증2과 울적함
        row_depr_2 = train.ix[train['우울증정도(0,1,2)'] == 2, ["울적한기분"]]
        row_depr_ls_20 = list(row_depr_2['울적한기분'] == 0)
        row_depr_ls_20_count = row_depr_ls_20.count(True)

        row_depr_ls_21 = list(row_depr_2['울적한기분'] == 1)
        row_depr_ls_21_count = row_depr_ls_21.count(True)

        row_depr_ls_22 = list(row_depr_2['울적한기분'] == 2)
        row_depr_ls_22_count = row_depr_ls_22.count(True)

        row_depr_ls_23 = list(row_depr_2['울적한기분'] == 3)
        row_depr_ls_23_count = row_depr_ls_23.count(True)
   
        results = ["경증", "중증", "심각"]  #경증, 중증, 삼각

        fig = go.Figure(data=[
            go.Bar(name='울적한기분0', x=results, y=[row_depr_ls_00_count, row_depr_ls_10_count, row_depr_ls_20_count]),
            go.Bar(name='울적한기분1', x=results, y=[row_depr_ls_01_count, row_depr_ls_11_count, row_depr_ls_21_count]),
            go.Bar(name='울적한기분2', x=results, y=[row_depr_ls_02_count, row_depr_ls_12_count, row_depr_ls_22_count]),
            go.Bar(name='울적한기분3', x=results, y=[row_depr_ls_03_count, row_depr_ls_13_count, row_depr_ls_23_count])
        ])
   
        fig.update_layout(barmode='stack')
        fig.write_image("/Users/corgi/Desktop/cnu/firstrest/post/data/images/fig_depr.png") #저장할 파일명과 절대 경로  
        return HttpResponse(fig.show())

#--------------------------------------------------------------------------------------------
    #각 항목에 해당하는 그래프들을 이미지로 저장하는 api : 우울증과 자기능력 drawcapa
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer]) 
    def drawcapa(self, *args, **kwargs):

        DIR='/Users/corgi/Desktop/cnu/firstrest/post/data'
        train = pd.read_csv(DIR+'/train.csv', delimiter=',')
        
        sns.set()
    
        # 우울증0과 자기능력
        row_capa_0 = train.ix[train['우울증정도(0,1,2)'] == 0, ["자기능력"]]
        row_capa_ls_00 = list(row_capa_0['자기능력'] == 0)
        row_capa_ls_00_count = row_capa_ls_00.count(True)

        row_capa_ls_01 = list(row_capa_0['자기능력'] == 1)
        row_capa_ls_01_count = row_capa_ls_01.count(True)

        row_capa_ls_02 = list(row_capa_0['자기능력'] == 2)
        row_capa_ls_02_count = row_capa_ls_02.count(True)

        row_capa_ls_03 = list(row_capa_0['자기능력'] == 3)
        row_capa_ls_03_count = row_capa_ls_03.count(True)


        # 우울증1과 자기능력
        row_capa_1 = train.ix[train['우울증정도(0,1,2)'] == 1, ["자기능력"]]
        row_capa_ls_10 = list(row_capa_1['자기능력'] == 0)
        row_capa_ls_10_count = row_capa_ls_10.count(True)

        row_capa_ls_11 = list(row_capa_1['자기능력'] == 1)
        row_capa_ls_11_count = row_capa_ls_11.count(True)

        row_capa_ls_12 = list(row_capa_1['자기능력'] == 2)
        row_capa_ls_12_count = row_capa_ls_12.count(True)

        row_capa_ls_13 = list(row_capa_1['자기능력'] == 3)
        row_capa_ls_13_count = row_capa_ls_13.count(True)


        # 우울증2과 자기능력
        row_capa_2 = train.ix[train['우울증정도(0,1,2)'] == 2, ["자기능력"]]
        row_capa_ls_20 = list(row_capa_2['자기능력'] == 0)
        row_capa_ls_20_count = row_capa_ls_20.count(True)

        row_capa_ls_21 = list(row_capa_2['자기능력'] == 1)
        row_capa_ls_21_count = row_capa_ls_21.count(True)

        row_capa_ls_22 = list(row_capa_2['자기능력'] == 2)
        row_capa_ls_22_count = row_capa_ls_22.count(True)

        row_capa_ls_23 = list(row_capa_2['자기능력'] == 3)
        row_capa_ls_23_count = row_capa_ls_23.count(True)
   
        results = ["경증", "중증", "심각"]  #경증, 중증, 삼각

        fig = go.Figure(data=[
            go.Bar(name='자기능력0', x=results, y=[row_capa_ls_00_count, row_capa_ls_10_count, row_capa_ls_20_count]),
            go.Bar(name='자기능력1', x=results, y=[row_capa_ls_01_count, row_capa_ls_11_count, row_capa_ls_21_count]),
            go.Bar(name='자기능력2', x=results, y=[row_capa_ls_02_count, row_capa_ls_12_count, row_capa_ls_22_count]),
            go.Bar(name='자기능력3', x=results, y=[row_capa_ls_03_count, row_capa_ls_13_count, row_capa_ls_23_count])
        ])
   
        fig.update_layout(barmode='stack')
        fig.write_image("/Users/corgi/Desktop/cnu/firstrest/post/data/images/fig_capa.png") #저장할 파일명과 절대 경로  
        return HttpResponse(fig.show())

#--------------------------------------------------------------------------------------------
    #각 항목에 해당하는 그래프들을 이미지로 저장하는 api : 우울증과 집중불안 drawanxi
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer]) 
    def drawanxi(self, *args, **kwargs):

        DIR='/Users/corgi/Desktop/cnu/firstrest/post/data'
        train = pd.read_csv(DIR+'/train.csv', delimiter=',')
        
        sns.set()
    
        # 우울증0과 집중불안
        row_anxi_0 = train.ix[train['우울증정도(0,1,2)'] == 0, ["집중불안"]]
        row_anxi_ls_00 = list(row_anxi_0['집중불안'] == 0)
        row_anxi_ls_00_count = row_anxi_ls_00.count(True)

        row_anxi_ls_01 = list(row_anxi_0['집중불안'] == 1)
        row_anxi_ls_01_count = row_anxi_ls_01.count(True)

        row_anxi_ls_02 = list(row_anxi_0['집중불안'] == 2)
        row_anxi_ls_02_count = row_anxi_ls_02.count(True)

        row_anxi_ls_03 = list(row_anxi_0['집중불안'] == 3)
        row_anxi_ls_03_count = row_anxi_ls_03.count(True)


        # 우울증1과 집중불안
        row_anxi_1 = train.ix[train['우울증정도(0,1,2)'] == 1, ["집중불안"]]
        row_anxi_ls_10 = list(row_anxi_1['집중불안'] == 0)
        row_anxi_ls_10_count = row_anxi_ls_10.count(True)

        row_anxi_ls_11 = list(row_anxi_1['집중불안'] == 1)
        row_anxi_ls_11_count = row_anxi_ls_11.count(True)

        row_anxi_ls_12 = list(row_anxi_1['집중불안'] == 2)
        row_anxi_ls_12_count = row_anxi_ls_12.count(True)

        row_anxi_ls_13 = list(row_anxi_1['집중불안'] == 3)
        row_anxi_ls_13_count = row_anxi_ls_13.count(True)


        # 우울증2과 집중불안
        row_anxi_2 = train.ix[train['우울증정도(0,1,2)'] == 2, ["집중불안"]]
        row_anxi_ls_20 = list(row_anxi_2['집중불안'] == 0)
        row_anxi_ls_20_count = row_anxi_ls_20.count(True)

        row_anxi_ls_21 = list(row_anxi_2['집중불안'] == 1)
        row_anxi_ls_21_count = row_anxi_ls_21.count(True)

        row_anxi_ls_22 = list(row_anxi_2['집중불안'] == 2)
        row_anxi_ls_22_count = row_anxi_ls_22.count(True)

        row_anxi_ls_23 = list(row_anxi_2['집중불안'] == 3)
        row_anxi_ls_23_count = row_anxi_ls_23.count(True)
   
        results = ["경증", "중증", "심각"]  #경증, 중증, 삼각

        fig = go.Figure(data=[
            go.Bar(name='집중불안0', x=results, y=[row_anxi_ls_00_count, row_anxi_ls_10_count, row_anxi_ls_20_count]),
            go.Bar(name='집중불안1', x=results, y=[row_anxi_ls_01_count, row_anxi_ls_11_count, row_anxi_ls_21_count]),
            go.Bar(name='집중불안2', x=results, y=[row_anxi_ls_02_count, row_anxi_ls_12_count, row_anxi_ls_22_count]),
            go.Bar(name='집중불안3', x=results, y=[row_anxi_ls_03_count, row_anxi_ls_13_count, row_anxi_ls_23_count])
        ])
   
        fig.update_layout(barmode='stack')
        fig.write_image("/Users/corgi/Desktop/cnu/firstrest/post/data/images/fig_anxi.png") #저장할 파일명과 절대 경로  
        return HttpResponse(fig.show())


#--------------------------------------------------------------------------------------------
    #각 항목에 해당하는 그래프들을 이미지로 저장하는 api : 우울증과 우울 drawglo
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer]) 
    def drawglo(self, *args, **kwargs):

        DIR='/Users/corgi/Desktop/cnu/firstrest/post/data'
        train = pd.read_csv(DIR+'/train.csv', delimiter=',')
        
        sns.set()
    
        # 우울증0과 우울
        row_glo_0 = train.ix[train['우울증정도(0,1,2)'] == 0, ["우울"]]
        row_glo_ls_00 = list(row_glo_0['우울'] == 0)
        row_glo_ls_00_count = row_glo_ls_00.count(True)

        row_glo_ls_01 = list(row_glo_0['우울'] == 1)
        row_glo_ls_01_count = row_glo_ls_01.count(True)

        row_glo_ls_02 = list(row_glo_0['우울'] == 2)
        row_glo_ls_02_count = row_glo_ls_02.count(True)

        row_glo_ls_03 = list(row_glo_0['우울'] == 3)
        row_glo_ls_03_count = row_glo_ls_03.count(True)


        # 우울증1과 우울
        row_glo_1 = train.ix[train['우울증정도(0,1,2)'] == 1, ["우울"]]
        row_glo_ls_10 = list(row_glo_1['우울'] == 0)
        row_glo_ls_10_count = row_glo_ls_10.count(True)

        row_glo_ls_11 = list(row_glo_1['우울'] == 1)
        row_glo_ls_11_count = row_glo_ls_11.count(True)

        row_glo_ls_12 = list(row_glo_1['우울'] == 2)
        row_glo_ls_12_count = row_glo_ls_12.count(True)

        row_glo_ls_13 = list(row_glo_1['우울'] == 3)
        row_glo_ls_13_count = row_glo_ls_13.count(True)


        # 우울증2과 우울
        row_glo_2 = train.ix[train['우울증정도(0,1,2)'] == 2, ["우울"]]
        row_glo_ls_20 = list(row_glo_2['우울'] == 0)
        row_glo_ls_20_count = row_glo_ls_20.count(True)

        row_glo_ls_21 = list(row_glo_2['우울'] == 1)
        row_glo_ls_21_count = row_glo_ls_21.count(True)

        row_glo_ls_22 = list(row_glo_2['우울'] == 2)
        row_glo_ls_22_count = row_glo_ls_22.count(True)

        row_glo_ls_23 = list(row_glo_2['우울'] == 3)
        row_glo_ls_23_count = row_glo_ls_23.count(True)
   
        results = ["경증", "중증", "심각"]  #경증, 중증, 삼각

        fig = go.Figure(data=[
            go.Bar(name='우울0', x=results, y=[row_glo_ls_00_count, row_glo_ls_10_count, row_glo_ls_20_count]),
            go.Bar(name='우울1', x=results, y=[row_glo_ls_01_count, row_glo_ls_11_count, row_glo_ls_21_count]),
            go.Bar(name='우울2', x=results, y=[row_glo_ls_02_count, row_glo_ls_12_count, row_glo_ls_22_count]),
            go.Bar(name='우울3', x=results, y=[row_glo_ls_03_count, row_glo_ls_13_count, row_glo_ls_23_count])
        ])
   
        fig.update_layout(barmode='stack')
        fig.write_image("/Users/corgi/Desktop/cnu/firstrest/post/data/images/fig_glo.png") #저장할 파일명과 절대 경로  
        return HttpResponse(fig.show())


#--------------------------------------------------------------------------------------------
    #각 항목에 해당하는 그래프들을 이미지로 저장하는 api : 우울증과 힘듬 drawhard
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer]) 
    def drawhard(self, *args, **kwargs):

        DIR='/Users/corgi/Desktop/cnu/firstrest/post/data'
        train = pd.read_csv(DIR+'/train.csv', delimiter=',')
        
        sns.set()
    
        # 우울증0과 우울
        row_hard_0 = train.ix[train['우울증정도(0,1,2)'] == 0, ["힘듬"]]
        row_hard_ls_00 = list(row_hard_0['힘듬'] == 0)
        row_hard_ls_00_count = row_hard_ls_00.count(True)

        row_hard_ls_01 = list(row_hard_0['힘듬'] == 1)
        row_hard_ls_01_count = row_hard_ls_01.count(True)

        row_hard_ls_02 = list(row_hard_0['힘듬'] == 2)
        row_hard_ls_02_count = row_hard_ls_02.count(True)

        row_hard_ls_03 = list(row_hard_0['힘듬'] == 3)
        row_hard_ls_03_count = row_hard_ls_03.count(True)


        # 우울증1과 우울
        row_hard_1 = train.ix[train['우울증정도(0,1,2)'] == 1, ["힘듬"]]
        row_hard_ls_10 = list(row_hard_1['힘듬'] == 0)
        row_hard_ls_10_count = row_hard_ls_10.count(True)

        row_hard_ls_11 = list(row_hard_1['힘듬'] == 1)
        row_hard_ls_11_count = row_hard_ls_11.count(True)

        row_hard_ls_12 = list(row_hard_1['힘듬'] == 2)
        row_hard_ls_12_count = row_hard_ls_12.count(True)

        row_hard_ls_13 = list(row_hard_1['힘듬'] == 3)
        row_hard_ls_13_count = row_hard_ls_13.count(True)


        # 우울증2과 우울
        row_hard_2 = train.ix[train['우울증정도(0,1,2)'] == 2, ["힘듬"]]
        row_hard_ls_20 = list(row_hard_2['힘듬'] == 0)
        row_hard_ls_20_count = row_hard_ls_20.count(True)

        row_hard_ls_21 = list(row_hard_2['힘듬'] == 1)
        row_hard_ls_21_count = row_hard_ls_21.count(True)

        row_hard_ls_22 = list(row_hard_2['힘듬'] == 2)
        row_hard_ls_22_count = row_hard_ls_22.count(True)

        row_hard_ls_23 = list(row_hard_2['힘듬'] == 3)
        row_hard_ls_23_count = row_hard_ls_23.count(True)
   
        results = ["경증", "중증", "심각"]  #경증, 중증, 삼각

        fig = go.Figure(data=[
            go.Bar(name='힘듬0', x=results, y=[row_hard_ls_00_count, row_hard_ls_10_count, row_hard_ls_20_count]),
            go.Bar(name='힘듬1', x=results, y=[row_hard_ls_01_count, row_hard_ls_11_count, row_hard_ls_21_count]),
            go.Bar(name='힘듬2', x=results, y=[row_hard_ls_02_count, row_hard_ls_12_count, row_hard_ls_22_count]),
            go.Bar(name='힘듬3', x=results, y=[row_hard_ls_03_count, row_hard_ls_13_count, row_hard_ls_23_count])
        ])
   
        fig.update_layout(barmode='stack')
        fig.write_image("/Users/corgi/Desktop/cnu/firstrest/post/data/images/fig_hard.png") #저장할 파일명과 절대 경로  
        return HttpResponse(fig.show())

#--------------------------------------------------------------------------------------------
    #각 항목에 해당하는 그래프들을 이미지로 저장하는 api : 우울증과 미래희망적 drawhope
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer]) 
    def drawhope(self, *args, **kwargs):

        DIR='/Users/corgi/Desktop/cnu/firstrest/post/data'
        train = pd.read_csv(DIR+'/train.csv', delimiter=',')
        
        sns.set()
    
        # 우울증0과 우울
        row_hope_0 = train.ix[train['우울증정도(0,1,2)'] == 0, ["미래희망적"]]
        row_hope_ls_00 = list(row_hope_0['미래희망적'] == 0)
        row_hope_ls_00_count = row_hope_ls_00.count(True)

        row_hope_ls_01 = list(row_hope_0['미래희망적'] == 1)
        row_hope_ls_01_count = row_hope_ls_01.count(True)

        row_hope_ls_02 = list(row_hope_0['미래희망적'] == 2)
        row_hope_ls_02_count = row_hope_ls_02.count(True)

        row_hope_ls_03 = list(row_hope_0['미래희망적'] == 3)
        row_hope_ls_03_count = row_hope_ls_03.count(True)


        # 우울증1과 우울
        row_hope_1 = train.ix[train['우울증정도(0,1,2)'] == 1, ["미래희망적"]]
        row_hope_ls_10 = list(row_hope_1['미래희망적'] == 0)
        row_hope_ls_10_count = row_hope_ls_10.count(True)

        row_hope_ls_11 = list(row_hope_1['미래희망적'] == 1)
        row_hope_ls_11_count = row_hope_ls_11.count(True)

        row_hope_ls_12 = list(row_hope_1['미래희망적'] == 2)
        row_hope_ls_12_count = row_hope_ls_12.count(True)

        row_hope_ls_13 = list(row_hope_1['미래희망적'] == 3)
        row_hope_ls_13_count = row_hope_ls_13.count(True)


        # 우울증2과 우울
        row_hope_2 = train.ix[train['우울증정도(0,1,2)'] == 2, ["미래희망적"]]
        row_hope_ls_20 = list(row_hope_2['미래희망적'] == 0)
        row_hope_ls_20_count = row_hope_ls_20.count(True)

        row_hope_ls_21 = list(row_hope_2['미래희망적'] == 1)
        row_hope_ls_21_count = row_hope_ls_21.count(True)

        row_hope_ls_22 = list(row_hope_2['미래희망적'] == 2)
        row_hope_ls_22_count = row_hope_ls_22.count(True)

        row_hope_ls_23 = list(row_hope_2['미래희망적'] == 3)
        row_hope_ls_23_count = row_hope_ls_23.count(True)
   
        results = ["경증", "중증", "심각"]  #경증, 중증, 삼각

        fig = go.Figure(data=[
            go.Bar(name='미래희망적0', x=results, y=[row_hope_ls_00_count, row_hope_ls_10_count, row_hope_ls_20_count]),
            go.Bar(name='미래희망적1', x=results, y=[row_hope_ls_01_count, row_hope_ls_11_count, row_hope_ls_21_count]),
            go.Bar(name='미래희망적2', x=results, y=[row_hope_ls_02_count, row_hope_ls_12_count, row_hope_ls_22_count]),
            go.Bar(name='미래희망적3', x=results, y=[row_hope_ls_03_count, row_hope_ls_13_count, row_hope_ls_23_count])
        ])
   
        fig.update_layout(barmode='stack')
        fig.write_image("/Users/corgi/Desktop/cnu/firstrest/post/data/images/fig_hope.png") #저장할 파일명과 절대 경로  
        return HttpResponse(fig.show())

#--------------------------------------------------------------------------------------------
    #각 항목에 해당하는 그래프들을 이미지로 저장하는 api : 우울증과 실패작 drawfail
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer]) 
    def drawfail(self, *args, **kwargs):

        DIR='/Users/corgi/Desktop/cnu/firstrest/post/data'
        train = pd.read_csv(DIR+'/train.csv', delimiter=',')
        
        sns.set()
    
        # 우울증0과 우울
        row_fail_0 = train.ix[train['우울증정도(0,1,2)'] == 0, ["실패작"]]
        row_fail_ls_00 = list(row_fail_0['실패작'] == 0)
        row_fail_ls_00_count = row_fail_ls_00.count(True)

        row_fail_ls_01 = list(row_fail_0['실패작'] == 1)
        row_fail_ls_01_count = row_fail_ls_01.count(True)

        row_fail_ls_02 = list(row_fail_0['실패작'] == 2)
        row_fail_ls_02_count = row_fail_ls_02.count(True)

        row_fail_ls_03 = list(row_fail_0['실패작'] == 3)
        row_fail_ls_03_count = row_fail_ls_03.count(True)


        # 우울증1과 우울
        row_fail_1 = train.ix[train['우울증정도(0,1,2)'] == 1, ["실패작"]]
        row_fail_ls_10 = list(row_fail_1['실패작'] == 0)
        row_fail_ls_10_count = row_fail_ls_10.count(True)

        row_fail_ls_11 = list(row_fail_1['실패작'] == 1)
        row_fail_ls_11_count = row_fail_ls_11.count(True)

        row_fail_ls_12 = list(row_fail_1['실패작'] == 2)
        row_fail_ls_12_count = row_fail_ls_12.count(True)

        row_fail_ls_13 = list(row_fail_1['실패작'] == 3)
        row_fail_ls_13_count = row_fail_ls_13.count(True)


        # 우울증2과 우울
        row_fail_2 = train.ix[train['우울증정도(0,1,2)'] == 2, ["실패작"]]
        row_fail_ls_20 = list(row_fail_2['실패작'] == 0)
        row_fail_ls_20_count = row_fail_ls_20.count(True)

        row_fail_ls_21 = list(row_fail_2['실패작'] == 1)
        row_fail_ls_21_count = row_fail_ls_21.count(True)

        row_fail_ls_22 = list(row_fail_2['실패작'] == 2)
        row_fail_ls_22_count = row_fail_ls_22.count(True)

        row_fail_ls_23 = list(row_fail_2['실패작'] == 3)
        row_fail_ls_23_count = row_fail_ls_23.count(True)
   
        results = ["경증", "중증", "심각"]  #경증, 중증, 삼각

        fig = go.Figure(data=[
            go.Bar(name='실패작0', x=results, y=[row_fail_ls_00_count, row_fail_ls_10_count, row_fail_ls_20_count]),
            go.Bar(name='실패작1', x=results, y=[row_fail_ls_01_count, row_fail_ls_11_count, row_fail_ls_21_count]),
            go.Bar(name='실패작2', x=results, y=[row_fail_ls_02_count, row_fail_ls_12_count, row_fail_ls_22_count]),
            go.Bar(name='실패작3', x=results, y=[row_fail_ls_03_count, row_fail_ls_13_count, row_fail_ls_23_count])
        ])
   
        fig.update_layout(barmode='stack')
        fig.write_image("/Users/corgi/Desktop/cnu/firstrest/post/data/images/fig_fail.png") #저장할 파일명과 절대 경로  
        return HttpResponse(fig.show())

#--------------------------------------------------------------------------------------------
    #각 항목에 해당하는 그래프들을 이미지로 저장하는 api : 우울증과 두려움 drawfear
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer]) 
    def drawfear(self, *args, **kwargs):

        DIR='/Users/corgi/Desktop/cnu/firstrest/post/data'
        train = pd.read_csv(DIR+'/train.csv', delimiter=',')
        
        sns.set()
    
        # 우울증0과 우울
        row_fear_0 = train.ix[train['우울증정도(0,1,2)'] == 0, ["두려움"]]
        row_fear_ls_00 = list(row_fear_0['두려움'] == 0)
        row_fear_ls_00_count = row_fear_ls_00.count(True)

        row_fear_ls_01 = list(row_fear_0['두려움'] == 1)
        row_fear_ls_01_count = row_fear_ls_01.count(True)

        row_fear_ls_02 = list(row_fear_0['두려움'] == 2)
        row_fear_ls_02_count = row_fear_ls_02.count(True)

        row_fear_ls_03 = list(row_fear_0['두려움'] == 3)
        row_fear_ls_03_count = row_fear_ls_03.count(True)


        # 우울증1과 우울
        row_fear_1 = train.ix[train['우울증정도(0,1,2)'] == 1, ["두려움"]]
        row_fear_ls_10 = list(row_fear_1['두려움'] == 0)
        row_fear_ls_10_count = row_fear_ls_10.count(True)

        row_fear_ls_11 = list(row_fear_1['두려움'] == 1)
        row_fear_ls_11_count = row_fear_ls_11.count(True)

        row_fear_ls_12 = list(row_fear_1['두려움'] == 2)
        row_fear_ls_12_count = row_fear_ls_12.count(True)

        row_fear_ls_13 = list(row_fear_1['두려움'] == 3)
        row_fear_ls_13_count = row_fear_ls_13.count(True)


        # 우울증2과 우울
        row_fear_2 = train.ix[train['우울증정도(0,1,2)'] == 2, ["두려움"]]
        row_fear_ls_20 = list(row_fear_2['두려움'] == 0)
        row_fear_ls_20_count = row_fear_ls_20.count(True)

        row_fear_ls_21 = list(row_fear_2['두려움'] == 1)
        row_fear_ls_21_count = row_fear_ls_21.count(True)

        row_fear_ls_22 = list(row_fear_2['두려움'] == 2)
        row_fear_ls_22_count = row_fear_ls_22.count(True)

        row_fear_ls_23 = list(row_fear_2['두려움'] == 3)
        row_fear_ls_23_count = row_fear_ls_23.count(True)
   
        results = ["경증", "중증", "심각"]  #경증, 중증, 삼각

        fig = go.Figure(data=[
            go.Bar(name='두려움0', x=results, y=[row_fear_ls_00_count, row_fear_ls_10_count, row_fear_ls_20_count]),
            go.Bar(name='두려움1', x=results, y=[row_fear_ls_01_count, row_fear_ls_11_count, row_fear_ls_21_count]),
            go.Bar(name='두려움2', x=results, y=[row_fear_ls_02_count, row_fear_ls_12_count, row_fear_ls_22_count]),
            go.Bar(name='두려움3', x=results, y=[row_fear_ls_03_count, row_fear_ls_13_count, row_fear_ls_23_count])
        ])
   
        fig.update_layout(barmode='stack')
        fig.write_image("/Users/corgi/Desktop/cnu/firstrest/post/data/images/fig_fear.png") #저장할 파일명과 절대 경로  
        return HttpResponse(fig.show())

#--------------------------------------------------------------------------------------------
    #각 항목에 해당하는 그래프들을 이미지로 저장하는 api : 우울증과 잠설침 drawinso
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer]) 
    def drawinso(self, *args, **kwargs):

        DIR='/Users/corgi/Desktop/cnu/firstrest/post/data'
        train = pd.read_csv(DIR+'/train.csv', delimiter=',')
        
        sns.set()
    
        # 우울증0과 우울
        row_inso_0 = train.ix[train['우울증정도(0,1,2)'] == 0, ["잠설침"]]
        row_inso_ls_00 = list(row_inso_0['잠설침'] == 0)
        row_inso_ls_00_count = row_inso_ls_00.count(True)

        row_inso_ls_01 = list(row_inso_0['잠설침'] == 1)
        row_inso_ls_01_count = row_inso_ls_01.count(True)

        row_inso_ls_02 = list(row_inso_0['잠설침'] == 2)
        row_inso_ls_02_count = row_inso_ls_02.count(True)

        row_inso_ls_03 = list(row_inso_0['잠설침'] == 3)
        row_inso_ls_03_count = row_inso_ls_03.count(True)


        # 우울증1과 우울
        row_inso_1 = train.ix[train['우울증정도(0,1,2)'] == 1, ["잠설침"]]
        row_inso_ls_10 = list(row_inso_1['잠설침'] == 0)
        row_inso_ls_10_count = row_inso_ls_10.count(True)

        row_inso_ls_11 = list(row_inso_1['잠설침'] == 1)
        row_inso_ls_11_count = row_inso_ls_11.count(True)

        row_inso_ls_12 = list(row_inso_1['잠설침'] == 2)
        row_inso_ls_12_count = row_inso_ls_12.count(True)

        row_inso_ls_13 = list(row_inso_1['잠설침'] == 3)
        row_inso_ls_13_count = row_inso_ls_13.count(True)


        # 우울증2과 우울
        row_inso_2 = train.ix[train['우울증정도(0,1,2)'] == 2, ["잠설침"]]
        row_inso_ls_20 = list(row_inso_2['잠설침'] == 0)
        row_inso_ls_20_count = row_inso_ls_20.count(True)

        row_inso_ls_21 = list(row_inso_2['잠설침'] == 1)
        row_inso_ls_21_count = row_inso_ls_21.count(True)

        row_inso_ls_22 = list(row_inso_2['잠설침'] == 2)
        row_inso_ls_22_count = row_inso_ls_22.count(True)

        row_inso_ls_23 = list(row_inso_2['잠설침'] == 3)
        row_inso_ls_23_count = row_inso_ls_23.count(True)
   
        results = ["경증", "중증", "심각"]  #경증, 중증, 삼각

        fig = go.Figure(data=[
            go.Bar(name='잠설침0', x=results, y=[row_inso_ls_00_count, row_inso_ls_10_count, row_inso_ls_20_count]),
            go.Bar(name='잠설침1', x=results, y=[row_inso_ls_01_count, row_inso_ls_11_count, row_inso_ls_21_count]),
            go.Bar(name='잠설침2', x=results, y=[row_inso_ls_02_count, row_inso_ls_12_count, row_inso_ls_22_count]),
            go.Bar(name='잠설침3', x=results, y=[row_inso_ls_03_count, row_inso_ls_13_count, row_inso_ls_23_count])
        ])
   
        fig.update_layout(barmode='stack')
        fig.write_image("/Users/corgi/Desktop/cnu/firstrest/post/data/images/fig_inso.png") #저장할 파일명과 절대 경로  
        return HttpResponse(fig.show())

#--------------------------------------------------------------------------------------------
    #각 항목에 해당하는 그래프들을 이미지로 저장하는 api : 우울증과 행복 drawhap
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer]) 
    def drawhap(self, *args, **kwargs):

        DIR='/Users/corgi/Desktop/cnu/firstrest/post/data'
        train = pd.read_csv(DIR+'/train.csv', delimiter=',')
        
        sns.set()
    
        # 우울증0과 우울
        row_hap_0 = train.ix[train['우울증정도(0,1,2)'] == 0, ["행복"]]
        row_hap_ls_00 = list(row_hap_0['행복'] == 0)
        row_hap_ls_00_count = row_hap_ls_00.count(True)

        row_hap_ls_01 = list(row_hap_0['행복'] == 1)
        row_hap_ls_01_count = row_hap_ls_01.count(True)

        row_hap_ls_02 = list(row_hap_0['행복'] == 2)
        row_hap_ls_02_count = row_hap_ls_02.count(True)

        row_hap_ls_03 = list(row_hap_0['행복'] == 3)
        row_hap_ls_03_count = row_hap_ls_03.count(True)


        # 우울증1과 우울
        row_hap_1 = train.ix[train['우울증정도(0,1,2)'] == 1, ["행복"]]
        row_hap_ls_10 = list(row_hap_1['행복'] == 0)
        row_hap_ls_10_count = row_hap_ls_10.count(True)

        row_hap_ls_11 = list(row_hap_1['행복'] == 1)
        row_hap_ls_11_count = row_hap_ls_11.count(True)

        row_hap_ls_12 = list(row_hap_1['행복'] == 2)
        row_hap_ls_12_count = row_hap_ls_12.count(True)

        row_hap_ls_13 = list(row_hap_1['행복'] == 3)
        row_hap_ls_13_count = row_hap_ls_13.count(True)


        # 우울증2과 우울
        row_hap_2 = train.ix[train['우울증정도(0,1,2)'] == 2, ["행복"]]
        row_hap_ls_20 = list(row_hap_2['행복'] == 0)
        row_hap_ls_20_count = row_hap_ls_20.count(True)

        row_hap_ls_21 = list(row_hap_2['행복'] == 1)
        row_hap_ls_21_count = row_hap_ls_21.count(True)

        row_hap_ls_22 = list(row_hap_2['행복'] == 2)
        row_hap_ls_22_count = row_hap_ls_22.count(True)

        row_hap_ls_23 = list(row_hap_2['행복'] == 3)
        row_hap_ls_23_count = row_hap_ls_23.count(True)
   
        results = ["경증", "중증", "심각"]  #경증, 중증, 삼각

        fig = go.Figure(data=[
            go.Bar(name='행복0', x=results, y=[row_hap_ls_00_count, row_hap_ls_10_count, row_hap_ls_20_count]),
            go.Bar(name='행복1', x=results, y=[row_hap_ls_01_count, row_hap_ls_11_count, row_hap_ls_21_count]),
            go.Bar(name='행복2', x=results, y=[row_hap_ls_02_count, row_hap_ls_12_count, row_hap_ls_22_count]),
            go.Bar(name='행복3', x=results, y=[row_hap_ls_03_count, row_hap_ls_13_count, row_hap_ls_23_count])
        ])
   
        fig.update_layout(barmode='stack')
        fig.write_image("/Users/corgi/Desktop/cnu/firstrest/post/data/images/fig_hap.png") #저장할 파일명과 절대 경로  
        return HttpResponse(fig.show())

#--------------------------------------------------------------------------------------------
    #각 항목에 해당하는 그래프들을 이미지로 저장하는 api : 우울증과 말수줄음 drawqui
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer]) 
    def drawqui(self, *args, **kwargs):

        DIR='/Users/corgi/Desktop/cnu/firstrest/post/data'
        train = pd.read_csv(DIR+'/train.csv', delimiter=',')
        
        sns.set()
    
        # 우울증0과 우울
        row_qui_0 = train.ix[train['우울증정도(0,1,2)'] == 0, ["말수줄음"]]
        row_qui_ls_00 = list(row_qui_0['말수줄음'] == 0)
        row_qui_ls_00_count = row_qui_ls_00.count(True)

        row_qui_ls_01 = list(row_qui_0['말수줄음'] == 1)
        row_qui_ls_01_count = row_qui_ls_01.count(True)

        row_qui_ls_02 = list(row_qui_0['말수줄음'] == 2)
        row_qui_ls_02_count = row_qui_ls_02.count(True)

        row_qui_ls_03 = list(row_qui_0['말수줄음'] == 3)
        row_qui_ls_03_count = row_qui_ls_03.count(True)


        # 우울증1과 우울
        row_qui_1 = train.ix[train['우울증정도(0,1,2)'] == 1, ["말수줄음"]]
        row_qui_ls_10 = list(row_qui_1['말수줄음'] == 0)
        row_qui_ls_10_count = row_qui_ls_10.count(True)

        row_qui_ls_11 = list(row_qui_1['말수줄음'] == 1)
        row_qui_ls_11_count = row_qui_ls_11.count(True)

        row_qui_ls_12 = list(row_qui_1['말수줄음'] == 2)
        row_qui_ls_12_count = row_qui_ls_12.count(True)

        row_qui_ls_13 = list(row_qui_1['말수줄음'] == 3)
        row_qui_ls_13_count = row_qui_ls_13.count(True)


        # 우울증2과 우울
        row_qui_2 = train.ix[train['우울증정도(0,1,2)'] == 2, ["말수줄음"]]
        row_qui_ls_20 = list(row_qui_2['말수줄음'] == 0)
        row_qui_ls_20_count = row_qui_ls_20.count(True)

        row_qui_ls_21 = list(row_qui_2['말수줄음'] == 1)
        row_qui_ls_21_count = row_qui_ls_21.count(True)

        row_qui_ls_22 = list(row_qui_2['말수줄음'] == 2)
        row_qui_ls_22_count = row_qui_ls_22.count(True)

        row_qui_ls_23 = list(row_qui_2['말수줄음'] == 3)
        row_qui_ls_23_count = row_qui_ls_23.count(True)
   
        results = ["경증", "중증", "심각"]  #경증, 중증, 삼각

        fig = go.Figure(data=[
            go.Bar(name='말수줄음0', x=results, y=[row_qui_ls_00_count, row_qui_ls_10_count, row_qui_ls_20_count]),
            go.Bar(name='말수줄음1', x=results, y=[row_qui_ls_01_count, row_qui_ls_11_count, row_qui_ls_21_count]),
            go.Bar(name='말수줄음2', x=results, y=[row_qui_ls_02_count, row_qui_ls_12_count, row_qui_ls_22_count]),
            go.Bar(name='말수줄음3', x=results, y=[row_qui_ls_03_count, row_qui_ls_13_count, row_qui_ls_23_count])
        ])
   
        fig.update_layout(barmode='stack')
        fig.write_image("/Users/corgi/Desktop/cnu/firstrest/post/data/images/fig_qui.png") #저장할 파일명과 절대 경로  
        return HttpResponse(fig.show())

#--------------------------------------------------------------------------------------------
    #각 항목에 해당하는 그래프들을 이미지로 저장하는 api : 우울증과 외로움 drawalon
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer]) 
    def drawalon(self, *args, **kwargs):

        DIR='/Users/corgi/Desktop/cnu/firstrest/post/data'
        train = pd.read_csv(DIR+'/train.csv', delimiter=',')
        
        sns.set()
    
        # 우울증0과 우울
        row_alon_0 = train.ix[train['우울증정도(0,1,2)'] == 0, ["외로움"]]
        row_alon_ls_00 = list(row_alon_0['외로움'] == 0)
        row_alon_ls_00_count = row_alon_ls_00.count(True)

        row_alon_ls_01 = list(row_alon_0['외로움'] == 1)
        row_alon_ls_01_count = row_alon_ls_01.count(True)

        row_alon_ls_02 = list(row_alon_0['외로움'] == 2)
        row_alon_ls_02_count = row_alon_ls_02.count(True)

        row_alon_ls_03 = list(row_alon_0['외로움'] == 3)
        row_alon_ls_03_count = row_alon_ls_03.count(True)


        # 우울증1과 우울
        row_alon_1 = train.ix[train['우울증정도(0,1,2)'] == 1, ["외로움"]]
        row_alon_ls_10 = list(row_alon_1['외로움'] == 0)
        row_alon_ls_10_count = row_alon_ls_10.count(True)

        row_alon_ls_11 = list(row_alon_1['외로움'] == 1)
        row_alon_ls_11_count = row_alon_ls_11.count(True)

        row_alon_ls_12 = list(row_alon_1['외로움'] == 2)
        row_alon_ls_12_count = row_alon_ls_12.count(True)

        row_alon_ls_13 = list(row_alon_1['외로움'] == 3)
        row_alon_ls_13_count = row_alon_ls_13.count(True)


        # 우울증2과 우울
        row_alon_2 = train.ix[train['우울증정도(0,1,2)'] == 2, ["외로움"]]
        row_alon_ls_20 = list(row_alon_2['외로움'] == 0)
        row_alon_ls_20_count = row_alon_ls_20.count(True)

        row_alon_ls_21 = list(row_alon_2['외로움'] == 1)
        row_alon_ls_21_count = row_alon_ls_21.count(True)

        row_alon_ls_22 = list(row_alon_2['외로움'] == 2)
        row_alon_ls_22_count = row_alon_ls_22.count(True)

        row_alon_ls_23 = list(row_alon_2['외로움'] == 3)
        row_alon_ls_23_count = row_alon_ls_23.count(True)
   
        results = ["경증", "중증", "심각"]  #경증, 중증, 삼각

        fig = go.Figure(data=[
            go.Bar(name='외로움0', x=results, y=[row_alon_ls_00_count, row_alon_ls_10_count, row_alon_ls_20_count]),
            go.Bar(name='외로움1', x=results, y=[row_alon_ls_01_count, row_alon_ls_11_count, row_alon_ls_21_count]),
            go.Bar(name='외로움2', x=results, y=[row_alon_ls_02_count, row_alon_ls_12_count, row_alon_ls_22_count]),
            go.Bar(name='외로움3', x=results, y=[row_alon_ls_03_count, row_alon_ls_13_count, row_alon_ls_23_count])
        ])
   
        fig.update_layout(barmode='stack')
        fig.write_image("/Users/corgi/Desktop/cnu/firstrest/post/data/images/fig_alon.png") #저장할 파일명과 절대 경로  
        return HttpResponse(fig.show())

#--------------------------------------------------------------------------------------------
    #각 항목에 해당하는 그래프들을 이미지로 저장하는 api : 우울증과 차가운대우 drawcold
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer]) 
    def drawcold(self, *args, **kwargs):

        DIR='/Users/corgi/Desktop/cnu/firstrest/post/data'
        train = pd.read_csv(DIR+'/train.csv', delimiter=',')
        
        sns.set()
    
        # 우울증0과 우울
        row_cold_0 = train.ix[train['우울증정도(0,1,2)'] == 0, ["차가운대우"]]
        row_cold_ls_00 = list(row_cold_0['차가운대우'] == 0)
        row_cold_ls_00_count = row_cold_ls_00.count(True)

        row_cold_ls_01 = list(row_cold_0['차가운대우'] == 1)
        row_cold_ls_01_count = row_cold_ls_01.count(True)

        row_cold_ls_02 = list(row_cold_0['차가운대우'] == 2)
        row_cold_ls_02_count = row_cold_ls_02.count(True)

        row_cold_ls_03 = list(row_cold_0['차가운대우'] == 3)
        row_cold_ls_03_count = row_cold_ls_03.count(True)


        # 우울증1과 우울
        row_cold_1 = train.ix[train['우울증정도(0,1,2)'] == 1, ["차가운대우"]]
        row_cold_ls_10 = list(row_cold_1['차가운대우'] == 0)
        row_cold_ls_10_count = row_cold_ls_10.count(True)

        row_cold_ls_11 = list(row_cold_1['차가운대우'] == 1)
        row_cold_ls_11_count = row_cold_ls_11.count(True)

        row_cold_ls_12 = list(row_cold_1['차가운대우'] == 2)
        row_cold_ls_12_count = row_cold_ls_12.count(True)

        row_cold_ls_13 = list(row_cold_1['차가운대우'] == 3)
        row_cold_ls_13_count = row_cold_ls_13.count(True)


        # 우울증2과 우울
        row_cold_2 = train.ix[train['우울증정도(0,1,2)'] == 2, ["차가운대우"]]
        row_cold_ls_20 = list(row_cold_2['차가운대우'] == 0)
        row_cold_ls_20_count = row_cold_ls_20.count(True)

        row_cold_ls_21 = list(row_cold_2['차가운대우'] == 1)
        row_cold_ls_21_count = row_cold_ls_21.count(True)

        row_cold_ls_22 = list(row_cold_2['차가운대우'] == 2)
        row_cold_ls_22_count = row_cold_ls_22.count(True)

        row_cold_ls_23 = list(row_cold_2['차가운대우'] == 3)
        row_cold_ls_23_count = row_cold_ls_23.count(True)
   
        results = ["경증", "중증", "심각"]  #경증, 중증, 삼각

        fig = go.Figure(data=[
            go.Bar(name='차가운대우0', x=results, y=[row_cold_ls_00_count, row_cold_ls_10_count, row_cold_ls_20_count]),
            go.Bar(name='차가운대우1', x=results, y=[row_cold_ls_01_count, row_cold_ls_11_count, row_cold_ls_21_count]),
            go.Bar(name='차가운대우2', x=results, y=[row_cold_ls_02_count, row_cold_ls_12_count, row_cold_ls_22_count]),
            go.Bar(name='차가운대우3', x=results, y=[row_cold_ls_03_count, row_cold_ls_13_count, row_cold_ls_23_count])
        ])
   
        fig.update_layout(barmode='stack')
        fig.write_image("/Users/corgi/Desktop/cnu/firstrest/post/data/images/fig_cold.png") #저장할 파일명과 절대 경로  
        return HttpResponse(fig.show())

#--------------------------------------------------------------------------------------------
    #각 항목에 해당하는 그래프들을 이미지로 저장하는 api : 우울증과 즐거운생활 drawfun
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer]) 
    def drawfun(self, *args, **kwargs):

        DIR='/Users/corgi/Desktop/cnu/firstrest/post/data'
        train = pd.read_csv(DIR+'/train.csv', delimiter=',')
        
        sns.set()
    
        # 우울증0과 우울
        row_fun_0 = train.ix[train['우울증정도(0,1,2)'] == 0, ["즐거운생활"]]
        row_fun_ls_00 = list(row_fun_0['즐거운생활'] == 0)
        row_fun_ls_00_count = row_fun_ls_00.count(True)

        row_fun_ls_01 = list(row_fun_0['즐거운생활'] == 1)
        row_fun_ls_01_count = row_fun_ls_01.count(True)

        row_fun_ls_02 = list(row_fun_0['즐거운생활'] == 2)
        row_fun_ls_02_count = row_fun_ls_02.count(True)

        row_fun_ls_03 = list(row_fun_0['즐거운생활'] == 3)
        row_fun_ls_03_count = row_fun_ls_03.count(True)


        # 우울증1과 우울
        row_fun_1 = train.ix[train['우울증정도(0,1,2)'] == 1, ["즐거운생활"]]
        row_fun_ls_10 = list(row_fun_1['즐거운생활'] == 0)
        row_fun_ls_10_count = row_fun_ls_10.count(True)

        row_fun_ls_11 = list(row_fun_1['즐거운생활'] == 1)
        row_fun_ls_11_count = row_fun_ls_11.count(True)

        row_fun_ls_12 = list(row_fun_1['즐거운생활'] == 2)
        row_fun_ls_12_count = row_fun_ls_12.count(True)

        row_fun_ls_13 = list(row_fun_1['즐거운생활'] == 3)
        row_fun_ls_13_count = row_fun_ls_13.count(True)


        # 우울증2과 우울
        row_fun_2 = train.ix[train['우울증정도(0,1,2)'] == 2, ["즐거운생활"]]
        row_fun_ls_20 = list(row_fun_2['즐거운생활'] == 0)
        row_fun_ls_20_count = row_fun_ls_20.count(True)

        row_fun_ls_21 = list(row_fun_2['즐거운생활'] == 1)
        row_fun_ls_21_count = row_fun_ls_21.count(True)

        row_fun_ls_22 = list(row_fun_2['즐거운생활'] == 2)
        row_fun_ls_22_count = row_fun_ls_22.count(True)

        row_fun_ls_23 = list(row_fun_2['즐거운생활'] == 3)
        row_fun_ls_23_count = row_fun_ls_23.count(True)
   
        results = ["경증", "중증", "심각"]  #경증, 중증, 삼각

        fig = go.Figure(data=[
            go.Bar(name='즐거운생활0', x=results, y=[row_fun_ls_00_count, row_fun_ls_10_count, row_fun_ls_20_count]),
            go.Bar(name='즐거운생활1', x=results, y=[row_fun_ls_01_count, row_fun_ls_11_count, row_fun_ls_21_count]),
            go.Bar(name='즐거운생활2', x=results, y=[row_fun_ls_02_count, row_fun_ls_12_count, row_fun_ls_22_count]),
            go.Bar(name='즐거운생활3', x=results, y=[row_fun_ls_03_count, row_fun_ls_13_count, row_fun_ls_23_count])
        ])
   
        fig.update_layout(barmode='stack')
        fig.write_image("/Users/corgi/Desktop/cnu/firstrest/post/data/images/fig_fun.png") #저장할 파일명과 절대 경로  
        return HttpResponse(fig.show())

#--------------------------------------------------------------------------------------------
    #각 항목에 해당하는 그래프들을 이미지로 저장하는 api : 우울증과 갑작스런울음 drawcry
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer]) 
    def drawcry(self, *args, **kwargs):

        DIR='/Users/corgi/Desktop/cnu/firstrest/post/data'
        train = pd.read_csv(DIR+'/train.csv', delimiter=',')
        
        sns.set()
    
        # 우울증0과 우울
        row_cry_0 = train.ix[train['우울증정도(0,1,2)'] == 0, ["갑작스런울음"]]
        row_cry_ls_00 = list(row_cry_0['갑작스런울음'] == 0)
        row_cry_ls_00_count = row_cry_ls_00.count(True)

        row_cry_ls_01 = list(row_cry_0['갑작스런울음'] == 1)
        row_cry_ls_01_count = row_cry_ls_01.count(True)

        row_cry_ls_02 = list(row_cry_0['갑작스런울음'] == 2)
        row_cry_ls_02_count = row_cry_ls_02.count(True)

        row_cry_ls_03 = list(row_cry_0['갑작스런울음'] == 3)
        row_cry_ls_03_count = row_cry_ls_03.count(True)


        # 우울증1과 우울
        row_cry_1 = train.ix[train['우울증정도(0,1,2)'] == 1, ["갑작스런울음"]]
        row_cry_ls_10 = list(row_cry_1['갑작스런울음'] == 0)
        row_cry_ls_10_count = row_cry_ls_10.count(True)

        row_cry_ls_11 = list(row_cry_1['갑작스런울음'] == 1)
        row_cry_ls_11_count = row_cry_ls_11.count(True)

        row_cry_ls_12 = list(row_cry_1['갑작스런울음'] == 2)
        row_cry_ls_12_count = row_cry_ls_12.count(True)

        row_cry_ls_13 = list(row_cry_1['갑작스런울음'] == 3)
        row_cry_ls_13_count = row_cry_ls_13.count(True)


        # 우울증2과 우울
        row_cry_2 = train.ix[train['우울증정도(0,1,2)'] == 2, ["갑작스런울음"]]
        row_cry_ls_20 = list(row_cry_2['갑작스런울음'] == 0)
        row_cry_ls_20_count = row_cry_ls_20.count(True)

        row_cry_ls_21 = list(row_cry_2['갑작스런울음'] == 1)
        row_cry_ls_21_count = row_cry_ls_21.count(True)

        row_cry_ls_22 = list(row_cry_2['갑작스런울음'] == 2)
        row_cry_ls_22_count = row_cry_ls_22.count(True)

        row_cry_ls_23 = list(row_cry_2['갑작스런울음'] == 3)
        row_cry_ls_23_count = row_cry_ls_23.count(True)
   
        results = ["경증", "중증", "심각"]  #경증, 중증, 삼각

        fig = go.Figure(data=[
            go.Bar(name='갑작스런울음0', x=results, y=[row_cry_ls_00_count, row_cry_ls_10_count, row_cry_ls_20_count]),
            go.Bar(name='갑작스런울음1', x=results, y=[row_cry_ls_01_count, row_cry_ls_11_count, row_cry_ls_21_count]),
            go.Bar(name='갑작스런울음2', x=results, y=[row_cry_ls_02_count, row_cry_ls_12_count, row_cry_ls_22_count]),
            go.Bar(name='갑작스런울음3', x=results, y=[row_cry_ls_03_count, row_cry_ls_13_count, row_cry_ls_23_count])
        ])
   
        fig.update_layout(barmode='stack')
        fig.write_image("/Users/corgi/Desktop/cnu/firstrest/post/data/images/fig_cry.png") #저장할 파일명과 절대 경로  
        return HttpResponse(fig.show())

#--------------------------------------------------------------------------------------------
    #각 항목에 해당하는 그래프들을 이미지로 저장하는 api : 우울증과 슬픔 drawsad
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer]) 
    def drawsad(self, *args, **kwargs):

        DIR='/Users/corgi/Desktop/cnu/firstrest/post/data'
        train = pd.read_csv(DIR+'/train.csv', delimiter=',')
        
        sns.set()
    
        # 우울증0과 우울
        row_sad_0 = train.ix[train['우울증정도(0,1,2)'] == 0, ["슬픔"]]
        row_sad_ls_00 = list(row_sad_0['슬픔'] == 0)
        row_sad_ls_00_count = row_sad_ls_00.count(True)

        row_sad_ls_01 = list(row_sad_0['슬픔'] == 1)
        row_sad_ls_01_count = row_sad_ls_01.count(True)

        row_sad_ls_02 = list(row_sad_0['슬픔'] == 2)
        row_sad_ls_02_count = row_sad_ls_02.count(True)

        row_sad_ls_03 = list(row_sad_0['슬픔'] == 3)
        row_sad_ls_03_count = row_sad_ls_03.count(True)


        # 우울증1과 우울
        row_sad_1 = train.ix[train['우울증정도(0,1,2)'] == 1, ["슬픔"]]
        row_sad_ls_10 = list(row_sad_1['슬픔'] == 0)
        row_sad_ls_10_count = row_sad_ls_10.count(True)

        row_sad_ls_11 = list(row_sad_1['슬픔'] == 1)
        row_sad_ls_11_count = row_sad_ls_11.count(True)

        row_sad_ls_12 = list(row_sad_1['슬픔'] == 2)
        row_sad_ls_12_count = row_sad_ls_12.count(True)

        row_sad_ls_13 = list(row_sad_1['슬픔'] == 3)
        row_sad_ls_13_count = row_sad_ls_13.count(True)


        # 우울증2과 우울
        row_sad_2 = train.ix[train['우울증정도(0,1,2)'] == 2, ["슬픔"]]
        row_sad_ls_20 = list(row_sad_2['슬픔'] == 0)
        row_sad_ls_20_count = row_sad_ls_20.count(True)

        row_sad_ls_21 = list(row_sad_2['슬픔'] == 1)
        row_sad_ls_21_count = row_sad_ls_21.count(True)

        row_sad_ls_22 = list(row_sad_2['슬픔'] == 2)
        row_sad_ls_22_count = row_sad_ls_22.count(True)

        row_sad_ls_23 = list(row_sad_2['슬픔'] == 3)
        row_sad_ls_23_count = row_sad_ls_23.count(True)
   
        results = ["경증", "중증", "심각"]  #경증, 중증, 삼각

        fig = go.Figure(data=[
            go.Bar(name='슬픔0', x=results, y=[row_sad_ls_00_count, row_sad_ls_10_count, row_sad_ls_20_count]),
            go.Bar(name='슬픔1', x=results, y=[row_sad_ls_01_count, row_sad_ls_11_count, row_sad_ls_21_count]),
            go.Bar(name='슬픔2', x=results, y=[row_sad_ls_02_count, row_sad_ls_12_count, row_sad_ls_22_count]),
            go.Bar(name='슬픔3', x=results, y=[row_sad_ls_03_count, row_sad_ls_13_count, row_sad_ls_23_count])
        ])
   
        fig.update_layout(barmode='stack')
        fig.write_image("/Users/corgi/Desktop/cnu/firstrest/post/data/images/fig_sad.png") #저장할 파일명과 절대 경로  
        return HttpResponse(fig.show())

#--------------------------------------------------------------------------------------------
    #각 항목에 해당하는 그래프들을 이미지로 저장하는 api : 우울증과 사람들이나를싫어 drawhate
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer]) 
    def drawhate(self, *args, **kwargs):

        DIR='/Users/corgi/Desktop/cnu/firstrest/post/data'
        train = pd.read_csv(DIR+'/train.csv', delimiter=',')
        
        sns.set()
    
        # 우울증0과 우울
        row_hate_0 = train.ix[train['우울증정도(0,1,2)'] == 0, ["사람들이나를싫어"]]
        row_hate_ls_00 = list(row_hate_0['사람들이나를싫어'] == 0)
        row_hate_ls_00_count = row_hate_ls_00.count(True)

        row_hate_ls_01 = list(row_hate_0['사람들이나를싫어'] == 1)
        row_hate_ls_01_count = row_hate_ls_01.count(True)

        row_hate_ls_02 = list(row_hate_0['사람들이나를싫어'] == 2)
        row_hate_ls_02_count = row_hate_ls_02.count(True)

        row_hate_ls_03 = list(row_hate_0['사람들이나를싫어'] == 3)
        row_hate_ls_03_count = row_hate_ls_03.count(True)


        # 우울증1과 우울
        row_hate_1 = train.ix[train['우울증정도(0,1,2)'] == 1, ["사람들이나를싫어"]]
        row_hate_ls_10 = list(row_hate_1['사람들이나를싫어'] == 0)
        row_hate_ls_10_count = row_hate_ls_10.count(True)

        row_hate_ls_11 = list(row_hate_1['사람들이나를싫어'] == 1)
        row_hate_ls_11_count = row_hate_ls_11.count(True)

        row_hate_ls_12 = list(row_hate_1['사람들이나를싫어'] == 2)
        row_hate_ls_12_count = row_hate_ls_12.count(True)

        row_hate_ls_13 = list(row_hate_1['사람들이나를싫어'] == 3)
        row_hate_ls_13_count = row_hate_ls_13.count(True)


        # 우울증2과 우울
        row_hate_2 = train.ix[train['우울증정도(0,1,2)'] == 2, ["사람들이나를싫어"]]
        row_hate_ls_20 = list(row_hate_2['사람들이나를싫어'] == 0)
        row_hate_ls_20_count = row_hate_ls_20.count(True)

        row_hate_ls_21 = list(row_hate_2['사람들이나를싫어'] == 1)
        row_hate_ls_21_count = row_hate_ls_21.count(True)

        row_hate_ls_22 = list(row_hate_2['사람들이나를싫어'] == 2)
        row_hate_ls_22_count = row_hate_ls_22.count(True)

        row_hate_ls_23 = list(row_hate_2['사람들이나를싫어'] == 3)
        row_hate_ls_23_count = row_hate_ls_23.count(True)
   
        results = ["경증", "중증", "심각"]  #경증, 중증, 삼각

        fig = go.Figure(data=[
            go.Bar(name='사람들이나를싫어0', x=results, y=[row_hate_ls_00_count, row_hate_ls_10_count, row_hate_ls_20_count]),
            go.Bar(name='사람들이나를싫어1', x=results, y=[row_hate_ls_01_count, row_hate_ls_11_count, row_hate_ls_21_count]),
            go.Bar(name='사람들이나를싫어2', x=results, y=[row_hate_ls_02_count, row_hate_ls_12_count, row_hate_ls_22_count]),
            go.Bar(name='사람들이나를싫어3', x=results, y=[row_hate_ls_03_count, row_hate_ls_13_count, row_hate_ls_23_count])
        ])
   
        fig.update_layout(barmode='stack')
        fig.write_image("/Users/corgi/Desktop/cnu/firstrest/post/data/images/fig_hate.png") #저장할 파일명과 절대 경로  
        return HttpResponse(fig.show())

#--------------------------------------------------------------------------------------------
    #각 항목에 해당하는 그래프들을 이미지로 저장하는 api : 우울증과 시작한기운없음 drawtor
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer]) 
    def drawtor(self, *args, **kwargs):

        DIR='/Users/corgi/Desktop/cnu/firstrest/post/data'
        train = pd.read_csv(DIR+'/train.csv', delimiter=',')
        
        sns.set()
    
        # 우울증0과 우울
        row_tor_0 = train.ix[train['우울증정도(0,1,2)'] == 0, ["시작한기운없음"]]
        row_tor_ls_00 = list(row_tor_0['시작한기운없음'] == 0)
        row_tor_ls_00_count = row_tor_ls_00.count(True)

        row_tor_ls_01 = list(row_tor_0['시작한기운없음'] == 1)
        row_tor_ls_01_count = row_tor_ls_01.count(True)

        row_tor_ls_02 = list(row_tor_0['시작한기운없음'] == 2)
        row_tor_ls_02_count = row_tor_ls_02.count(True)

        row_tor_ls_03 = list(row_tor_0['시작한기운없음'] == 3)
        row_tor_ls_03_count = row_tor_ls_03.count(True)


        # 우울증1과 우울
        row_tor_1 = train.ix[train['우울증정도(0,1,2)'] == 1, ["시작한기운없음"]]
        row_tor_ls_10 = list(row_tor_1['시작한기운없음'] == 0)
        row_tor_ls_10_count = row_tor_ls_10.count(True)

        row_tor_ls_11 = list(row_tor_1['시작한기운없음'] == 1)
        row_tor_ls_11_count = row_tor_ls_11.count(True)

        row_tor_ls_12 = list(row_tor_1['시작한기운없음'] == 2)
        row_tor_ls_12_count = row_tor_ls_12.count(True)

        row_tor_ls_13 = list(row_tor_1['시작한기운없음'] == 3)
        row_tor_ls_13_count = row_tor_ls_13.count(True)


        # 우울증2과 우울
        row_tor_2 = train.ix[train['우울증정도(0,1,2)'] == 2, ["시작한기운없음"]]
        row_tor_ls_20 = list(row_tor_2['시작한기운없음'] == 0)
        row_tor_ls_20_count = row_tor_ls_20.count(True)

        row_tor_ls_21 = list(row_tor_2['시작한기운없음'] == 1)
        row_tor_ls_21_count = row_tor_ls_21.count(True)

        row_tor_ls_22 = list(row_tor_2['시작한기운없음'] == 2)
        row_tor_ls_22_count = row_tor_ls_22.count(True)

        row_tor_ls_23 = list(row_tor_2['시작한기운없음'] == 3)
        row_tor_ls_23_count = row_tor_ls_23.count(True)
   
        results = ["경증", "중증", "심각"]  #경증, 중증, 삼각

        fig = go.Figure(data=[
            go.Bar(name='시작한기운없음0', x=results, y=[row_tor_ls_00_count, row_tor_ls_10_count, row_tor_ls_20_count]),
            go.Bar(name='시작한기운없음1', x=results, y=[row_tor_ls_01_count, row_tor_ls_11_count, row_tor_ls_21_count]),
            go.Bar(name='시작한기운없음2', x=results, y=[row_tor_ls_02_count, row_tor_ls_12_count, row_tor_ls_22_count]),
            go.Bar(name='시작한기운없음3', x=results, y=[row_tor_ls_03_count, row_tor_ls_13_count, row_tor_ls_23_count])
        ])
   
        fig.update_layout(barmode='stack')
        fig.write_image("/Users/corgi/Desktop/cnu/firstrest/post/data/images/fig_tor.png") #저장할 파일명과 절대 경로  
        return HttpResponse(fig.show())

