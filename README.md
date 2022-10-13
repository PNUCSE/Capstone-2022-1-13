# 동영상에서 객체 탐지를 이용한 영상 타임스탬프 시스템 개발

## 1. 프로젝트 소개

프로젝트 명 : 동영상에서 객체 탐지를 이용한 영상 타임스탬프 시스템 개발   

기업체에서 영상매체를 통한 간접광고를 진행하였을 때 실제로 계약한 시간
만큼 기업이 노출되었는지 사후 검증을 위한 간편한 툴 개발이 목적입니다.

이를 구현하기 위해 두가지 목표를 계획했습니다.   
1. 영상에서 기업의 로고를 검출하는 로고 탐지 AI 모델 개발   
2. 주어진 영상에서 찾고자 하는 로고가 언제 나타나는지 알 수 있는 타임 스탬프 기능을 제공하는 웹 프레임워크 개발    

## 2. 팀 소개

### 조원 전승윤
> 이메일 : baka3737baka@gmail.com   
> 역할 :    
> 웹 프레임 워크 개발   
> Github 버전 관리   
> Docker 컨테이너 개발 및 배포 관리   
> Detection 알고리즘 개발   

### 조원 유동운
> 이메일 : baka3737baka@gmail.com   
> 역할 :    
> 모델 학습 및 검증   
> 리펙토링 및 테스트 담당

### 조원 강태환
> 이메일 : baka3737baka@gmail.com    
> 역할 :    
> 학습 데이터 생성 및 전처리   
> 평가 지표 계산 및 평가   

## 3. 구성도

`이미지 넣는 부분`   

YOLOv5의 모델을 기반으로 공개 이미지 데이터셋 LogoDet-3k을 사용해 다양한 학습 데이터셋을 제작 후 학습한다.   
구현된 웹 프레임워크를 이용해 사용자로부터 영상과 이미지를 입력받은 후 학습한 결과인 Detection Model로 전달한다.   
Detection Model은 2nd Classifier로 구현한다. 첫 번째 Classifier은 객체의 위치를 찾는 작업인 `지역화 작업` 수행, 두 번째 Classifier는 객체의 종류를 구분하는 `분류` 수행한다.    
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