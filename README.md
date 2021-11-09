# wanted-lab-assignment

## 기업과제

- 기업명: 원티드랩
- 기업사이트: https://www.wantedlab.com/
- 기업채용공고: https://www.wanted.co.kr/company/79

### 과제 내용

✔️ **데이터**

- 회사 정보
    - 회사 이름 (다국어 지원 가능)
- 회사 정보 예제
    - 회사 이름 (원티드랩 / Wantedlab)
- 데이터 셋은 원티드에서 제공
- 데이터셋 예제
    - 원티드랩 회사는 한국어, 영어 회사명을 가지고 있습니다. (모든 회사가 모든 언어의 회사명을 가지고 있지는 않습니다.)

✔️ **REST API 기능**

- 회사명 자동완성
    - 회사명의 일부만 들어가도 검색이 되어야 합니다.
- 회사 이름으로 회사 검색
- 새로운 회사 추가

**✔️ 개발 조건**

- 제공되는 test case를 통과할 수 있도록 개발해야 합니다.
- ORM 사용해야 합니다.
- 결과는 JSON 형식이어야 합니다.
- database는 RDB를 사용해야 합니다.
- database table 갯수는 제한없습니다.
- 필요한 조건이 있다면 추가하셔도 좋습니다.
- Docker로 개발하면 가산점이 있습니다.

## 팀: 리스테린(Listerine)

* 팀원

| 이름 | 역할 | GITHUB | BLOG |
| :---: | :---: | :---: | :---: |
| `김주완` | 개발환경 및 배포 세팅, 테스트 연동, 과제 데이터 정제 | [joowankim](https://github.com/joowankim) | https://make-easy-anything.tistory.com |
| `박은혜` | 개발환경 및 배포 세팅, 회사 검색 API 구현 | [eunhye43](https://github.com/eunhye43) | https://velog.io/@majaeh43 |
| `윤수진` | 개발환경 및 배포 세팅, 회사명 자동완성 API 구현 | [study-by-myself](https://github.com/study-by-myself)| https://pro-yomi.tistory.com |
| `주종민` | 개발환경 및 배포 세팅, 새로운 회사 추가 API 구현 | [Gouache-studio](https://github.com/Gouache-studio) | https://gouache-studio.tistory.com/ |

## 구현 기능

### 회사명 자동완성하기

<어떤 로직으로 동작하는지 HTTP request 생성부터 HTTP response 반환까지 설명하기>

### 회사명으로 회사 검색하기

<어떤 로직으로 동작하는지 HTTP request 생성부터 HTTP response 반환까지 설명하기>

### 새로운 회사 추가하기

<어떤 로직으로 동작하는지 HTTP request 생성부터 HTTP response 반환까지 설명하기>

## 모델 관계

[ERD 회의 정리내용](https://github.com/Pre-Onboarding-Listerine/wanted-lab-assignment/wiki/20211108-ERD-%ED%9A%8C%EC%9D%98)

### 존재하는 모델

- `CompanyName`: 회사의 이름 문자열과 표현된 언어를 속성으로 가지는 모델
- `Company`: 회사에 대한 메타정보를 속성으로 가지는 모델
- `CompanyTag`: `Company`와 `Tag` 테이블 사이의 관계 테이블
- `Tag`: 태그의 이름 문자열과 표현된 언어를 속성으로 가지는 모델

### ERD

![image](https://user-images.githubusercontent.com/32446834/140742775-762f9b50-2b0d-4f9d-85f1-dc229d478587.png)

## 실행환경 설절 방법

> `git`과 `docker`, `docker-compose`가 설치되어 있어야 합니다.

1. 레포지토리 git 클론

    ```bash
    $ git clone https://github.com/Pre-Onboarding-Listerine/wanted-lab-assignment.git
    ```

2. `my_settings.py` 프로젝트 루트 디렉토리에 위치시키기

3. 애플리케이션 실행하기

    ```bash
    $ docker-compose up

    # 애플리케이션을 백그라운드에서 실행하고 싶다면
    $ docker-compose up -d
    
    # 어플리케이션이 실행이 되고 난 후에 데이터베이스 migration이 필요하다면
    $ docker-compose exec api python manage.py migrate
    ```

4. 애플리케이션에 접근하기

    django의 디폴트 포트인 8000포트가 아닌 8002번 포트와 연결되어 있습니다. 따라서 아래 주소로 로컬에 실행한 애플리케이션에 접근하실 수 있습니다.
    ```
    http://localhost:8002
    ```

## 과제 결과물 테스트 및 확인 방법

[`test_app.py` 연동 설정 PR](https://github.com/Pre-Onboarding-Listerine/wanted-lab-assignment/pull/1)

1. `test_app.py` 실행시키기
    
    ```
    $ pytest
    ```
   
2. POSTMAN 확인: <post api document 주소>

3. 배포된 서버의 주소

    ```commandline
    
    ```

# Reference

이 프로젝트는 원티드x위코드 백엔드 프리온보딩 과제 일환으로 원티드랩에서 출제한 과제를 기반으로 만들었습니다.
