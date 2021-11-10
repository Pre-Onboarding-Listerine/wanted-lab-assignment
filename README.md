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

- 입력된 문자열에 따라 검색할 회사명을 자동으로 완성합니다.

**구현 내용**

- Query Parameter로 전달된 `query`를 키워드로 사용합니다.
- 해당 키워드가 포함된 회사명을 모두 찾습니다.
- 찾은 회사명들을 이용해 다른 언어로 표현되는 같은 회사의 회사명들을 모두 찾습니다.
- 이후에 `x-wanted-language` 헤더 값에 맞는 언어로 표현된 회사명들을 추려서 반환합니다.

**요청 예시**

```http request
GET /search?query="지오"
x-wanted-language: "en"
```

  **응답 예시**

```commandline
* response status: 200 OK
* response content:
{
    "data": [
        {
            "company_name": "GEOCM Co."
        }
    ]
}
```


### 회사명으로 회사 검색하기

- `/companies/<keyword>`의 url에서 `keyword`에 회사이름을 입력하여 검색합니다.

**구현 내용**

1. Header의 `x-wanted-language`로 ko(한국), en(영어), ja(일본) 등 언어를 선택하여 입력합니다.
2. keyword에 입력된 회사이름과 header에서 선택한 언어를 토대로 회사이름과 태그를 출력할 수 있도록 구현하였습니다.
3. 검색된 회사가 없는 경우 404를 리턴하고 에러메시지가 출력됩니다.
4. 
**요청 예시**

```http request
GET /companies/<keyword>
x-wanted-language: "ko"
content-type: "application/json"
```

**응답 예시**

```commandline
* response status: 200 OK
* response content:
{
    "company_name": "원티드랩",
    "tags": [
        "태그_4",
        "태그_20",
        "태그_16"
    ]
}

* response status: 404 Not Found
* response content:
{
    "message": "company not found"
}
```

### 새로운 회사 추가하기

- 새로운 회사에 대한 회사 이름과 태그를 추가합니다.

**구현 내용**

1. 새로운 회사를 생성합니다.
2. 새로운 회사명을 생성하면서 생성한 회사와 맵핑시켜줍니다.
3. 새로운 태그를 생성하면서 생성한 회사와 맵핑시켜줍니다.
4. 생성한 회사의 회사명과 태그명들을 `x-wanted-language` 헤더 값에 맞게 추려 반환합니다.

**요청 예시**

```http request
GET /companies
x-wanted-language: "ko"
content-type: "application/json"
{
    "company_name": {
        "ko": "라인 프레쉬",
        "tw": "LINE FRESH",
        "en": "LINE FRESH",
    },
    "tags": [
        {
            "tag_name": {
                "ko": "태그_1",
                "tw": "tag_1",
                "en": "tag_1",
            }
        },
        {
            "tag_name": {
                "ko": "태그_8",
                "tw": "tag_8",
                "en": "tag_8",
            }
        },
        {
            "tag_name": {
                "ko": "태그_15",
                "tw": "tag_15",
                "en": "tag_15",
            }
        }
    ]
}
```

**응답 예시**

```commandline
* response status: 201 Create
* response content:
{
    "company_name": "LINE FRESH",
    "tags": [
        "tag_1",
        "tag_8",
        "tag_15",
    ],
}
```

## 모델 관계

[ERD 회의 정리내용](https://github.com/Pre-Onboarding-Listerine/wanted-lab-assignment/wiki/20211108-ERD-%ED%9A%8C%EC%9D%98)

### 존재하는 모델

- `CompanyName`: 회사의 이름 문자열과 표현된 언어를 속성으로 가지는 모델
- `Company`: 회사에 대한 메타정보를 속성으로 가지는 모델
- `CompanyTag`: `Company`와 `Tag` 테이블 사이의 관계 테이블
- `Tag`: 태그의 이름 문자열과 표현된 언어를 속성으로 가지는 모델

### ERD

![image](https://user-images.githubusercontent.com/32446834/140933757-8d82b561-f3ce-41af-8c7f-d1b0988d7047.png)


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
   
2. POSTMAN 확인: https://documenter.getpostman.com/view/12446432/UVC5FnTh

3. 배포된 서버의 주소

    ```commandline
    http://3.37.127.222:8002
    ```

# Reference

이 프로젝트는 원티드x위코드 백엔드 프리온보딩 과제 일환으로 원티드랩에서 출제한 과제를 기반으로 만들었습니다.
