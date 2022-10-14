# 동영상에서 객체 탐지를 이용한 영상 타임스탬프 시스템 개발

## 1. 프로젝트 소개

프로젝트 명 : 동영상에서 객체 탐지를 이용한 영상 타임스탬프 시스템 개발   

기업체에서 영상매체를 통한 간접광고를 진행하였을 때 실제로 계약한 시간
만큼 기업이 노출되었는지 사후 검증을 위한 간편한 툴 개발이 목적이다.

이를 구현하기 위해 두가지 목표를 계획했다.   
1. 영상에서 기업의 로고를 검출하는 로고 탐지 AI 모델 개발   
2. 주어진 영상에서 찾고자 하는 로고가 언제 나타나는지 알 수 있는 타임 스탬프 기능을 제공하는 웹 프레임워크 개발    

## 2. 팀 소개

### 조원 전승윤
이메일 : 
> baka3737baka@gmail.com     

역할 :    
> 웹 프레임 워크 개발   
> Github 버전 관리   
> Docker 컨테이너 개발 및 배포 관리   
> Detection 알고리즘 개발   

### 조원 유동운
이메일 : 
> dopia976@naver.com   

역할 :    
> 모델 학습 및 검증   
> 리펙토링 및 테스트 담당

### 조원 강태환
이메일 : 
> thkang727@naver.com    

역할 :    
> 학습 데이터 생성 및 전처리   
> 평가 지표 계산 및 평가   

## 3. 구성도

![Flowchart](https://user-images.githubusercontent.com/64539267/195662092-92c5c4af-83d6-49d4-9987-b43aec554d11.png)

`YOLOv5`의 모델을 기반으로 공개 이미지 데이터셋 `LogoDet-3k`을 사용해 다양한 학습 데이터셋을 제작 후 학습한다.   

구현된 웹 프레임워크를 이용해 사용자로부터 영상과 이미지를 입력받은 후 학습한 결과인 `Detection Model`로 전달한다.   

`Detection Model`은 `2nd Classifier`로 구현한다. 첫 번째 Classifier은 객체의 위치를 찾는 작업인 `지역화 작업` 수행, 두 번째 Classifier는 객체의 종류를 구분하는 `분류` 수행한다.    

결과를 TimeStamp로 전처리 이후 다시 웹 프레임워크로 전달한다. 이를 통해 사용자에게 결과를 출력한다.

## 4. 소개 및 시연 영상

`시연 영상 넣는 부분`   

## 5. 사용법

`web` 폴더에는 `back`과 `front` 폴더가 존재하며, 각각 백엔드, 프론트엔드가 구현된 프로젝트가 존재한다.   

각 프로젝트를 작동하는 방법을 여기 기술한다.   

### 백엔드 - Django
```Bash
# python 설치 필요, 전용 아나콘다 가상환경 후 실행 권장
# git clone 이후 첫 실행
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate

# 백그라운드로 프로젝트 실행
nohup python manage.py runserver 0.0.0.0:8011 &
```

### 프론트엔드 - React.js
```Bash
# 최신 Docker 설치 필요. 
# 최신 Docker 에서는 docker-compose가 따로 설치하는 기능이 아닌 내장되어 있음
# 백그라운드로 프로젝트 실행
sudo docker compose up --build -d
```

### 웹 프레임워크
![main_page](https://user-images.githubusercontent.com/64539267/195752610-54c4ef06-a6b5-4320-97f4-3160cbf9addb.png)

메인 페이지에서는 검출 작업을 수행할려는 `영상`과 검출 대상이 되는 `로고 이미지`, 그리고 detection 작업에서 구별 기준이 되는 `threshold value`를 입력 받는다.   

전부 입력 후 `Submit 버튼`을 통해 서버로 입력한 데이터들을 전송한다.

![result_page](https://user-images.githubusercontent.com/64539267/195752675-14087151-e119-479c-9cb5-5df813946deb.png)

`Detection Model`로부터 도출된 결과를 `Timestamp`로 전처리해 Result 페이지에서 보여준다.

왼쪽의 동영상은 입력한 동영상이며, 오른쪽의 버튼들은 각 로고가 검출된 `timestamp`이다. 각 timestamp 버튼을 누르면 그 시간 범위의 시작 시간으로 넘어갈 수 있다.

영상 아래의 `download video 버튼`은 detection 결과를 labeling한 영상을 다운받을 수 있다.