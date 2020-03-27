# Ddepression-survey-Deep-Learning
우울증 설문조사, 항목별 딥러닝   #SVM #PYTHON #DJANGO #REST-API

## 0. 환경
```
- django
	
- react
	
- react-dom
	
- djangorestframework
```	
	

## 1. import 항목
```
- pandas
	
- matplotlib.pyplot
	
- seaborn
	
- sklearn.svm
	
- numpy 
	
- KFold, cross_val_score

- plotly
	
- os

- csv
```

## 2. 라이브러리 항목
```
1. conda install -c plotly plotly-orca psutil requests
	
2. pip install ipython
  
3. pip install notebook
  
4. pip install ipywidgets, matplotlib, sklearn, numpy
  
5. pip install pandas
  
6. pip install psutil requests
```


## 3. 코드 설명

### 모델의 예측률을 보여주는 api인 showmodel, 예측률을 계산하고 데이터베이스의 result에 저장한다.
```python
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer]) 
    def models(self, *args, **kwargs):
        DIR='/Users/corgi/Desktop/cnu/firstrest/post/data'
        train = pd.read_csv(DIR+'/train.csv', delimiter=',')  #  파일 경로를 절대 경로로 할 것
         
        k_fold = KFold(n_splits=10, shuffle=True, random_state=0)
        train_data = train.drop('우울증정도(0,1,2)', axis=1) 
        target = train['우울증정도(0,1,2)']

        #6.2.5 SVM
        clf = SVC()
        scoring = 'accuracy'
        score = cross_val_score(clf, train_data, target, cv=k_fold, n_jobs=1, scoring=scoring)
        datas = {"result" : round(np.mean(score)*100,2) }
        serializer = PostSerializer(data=datas)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
        
    @action( detail=True, renderer_classes=[renderers.StaticHTMLRenderer]) 
    def showmodels(self, *args, **kwargs):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

        #httpResponse를 할 때는 return을 꼭 해줄 것
```

### _
### 모델에 저장된 데이터를 csv파일에 추가한다.(post 요청)
### 우울증 진단 작성 후 -> 결과보기 클릭시 -> csv파일에 새로운 데이터가 추가된다.


```python
    @action(methods=['post'], detail=True, renderer_classes=[renderers.StaticHTMLRenderer]) 
    def insertcsv(self, *args, **kwargs):
        DIR='/Users/corgi/Desktop/cnu/firstrest/post/data'   #절대경로
        f = open(DIR+'/train.csv','a', newline='')
        wr = csv.writer(f)
        # 데이터 형식 : 우울증 진단 /설문1~20 | 입력된 정보가 추가된다.
        wr.writerow([0,2,1,0,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2])
        
        f.close()
```

### _
### 각 항목에 해당하는 그래프들을 이미지로 저장하는 api : 우울증과 귀찮음 drawbother 
### 호출시 이미지로 저장되므로, 프론트 상에서는 이미지만 불러오면 된다.(불러올때마다 새로운 이미지로 덮어짐)

```python
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
        fig.write_image("/Users/corgi/Desktop/cnu/frontend/src/image/fig_bother.png") #저장할 파일명과 절대 경로  
        return HttpResponse(fig.show())
				
				
				    return Response(serializer.data, status=status.HTTP_201_CREATED
				
```

										
## 4. 사용한 알고리즘 
### SVM 알고리즘.
***"How do we divide the space with decision boundaries?"***

: 서포트 벡터 머신(support vector machine)은 기계 학습의 분야 중 하나로 패턴 인식, 자료 분석을 위한 지도 학습 모델이다.
주로 분류와 회귀 분석을 위해 사용한다. 두 카테고리 중 어느 하나에 속한 데이터의 집합이 주어졌을 때, SVM 알고리즘은 주어진 데이터 집합을 바탕으로 하여 
새로운 데이터가 어느 카테고리에 속할지 판단하는 비확률적 이진 선형 분류 모델을 만든다. 
만들어진 분류 모델은 데이터가 사상된 공간에서 경계로 표현되는데 SVM 알고리즘은 그 중 가장 큰 폭을 가진 경계를 찾는 알고리즘이다. 
SVM은 선형 분류와 더불어 비선형 분류에서도 사용될 수 있다. 

SVM 알고리즘 이론 출처) https://ko.wikipedia.org/wiki/%EC%84%9C%ED%8F%AC%ED%8A%B8_%EB%B2%A1%ED%84%B0_%EB%A8%B8%EC%8B%A0
