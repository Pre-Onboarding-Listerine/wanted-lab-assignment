import pytest
import json

from django.test import Client


@pytest.fixture
def api():
    return Client()


@pytest.mark.django_db
def test_company_name_autocomplete(api: Client):
    """
    1. 회사명 자동완성
    회사명의 일부만 들어가도 검색이 되어야 합니다.
    header의 x-wanted-language 언어값에 따라 해당 언어로 출력되어야 합니다.
    """
    headers = {"HTTP_x-wanted-language": "ko"}
    api.post(
        "/companies",
        data=json.dumps({
            "company_name": {
                "ko": "주식회사 링크드코리아"
            },
            "tags": [
                {
                    "tag_name": {
                        "ko": "태그_12",
                        "en": "tag_12",
                        "ja": "タグ_12"
                    }
                },
                {
                    "tag_name": {
                        "ko": "태그_6",
                        "en": "tag_6",
                        "ja": "タグ_6"
                    }
                },
                {
                    "tag_name": {
                        "ko": "태그_8",
                        "en": "tag_8",
                        "ja": "タグ_8"
                    }
                }
            ]
        }),
        **headers,
        content_type="application/json"
    )
    api.post(
        "/companies",
        data=json.dumps({
            "company_name": {
                "ko": "스피링크"
            },
            "tags": [
                {
                    "tag_name": {
                        "ko": "태그_19",
                        "en": "tag_19",
                        "ja": "タグ_19"
                    }
                },
                {
                    "tag_name": {
                        "ko": "태그_9",
                        "en": "tag_9",
                        "ja": "タグ_9"
                    }
                }
            ]
        }),
        **headers,
        content_type="application/json"
    )

    resp = api.get("/search?query=링크", **headers)
    searched_companies = json.loads(resp.content)['data']

    assert resp.status_code == 200
    assert searched_companies == [
        {"company_name": "주식회사 링크드코리아"},
        {"company_name": "스피링크"},
    ]


@pytest.mark.django_db
def test_company_search(api: Client):
    """
    2. 회사 이름으로 회사 검색
    header의 x-wanted-language 언어값에 따라 해당 언어로 출력되어야 합니다.
    """
    # 테스트 데이터를 추가합니다.
    headers = {"HTTP_x-wanted-language": "ko"}
    api.post(
        "/companies",
        data=json.dumps({
            "company_name": {
                "ko": "원티드랩",
                "en": "Wantedlab"
            },
            "tags": [
                {
                    "tag_name": {
                        "ko": "태그_4",
                        "en": "tag_4",
                        "ja": "タグ_4"
                    }
                },
                {
                    "tag_name": {
                        "ko": "태그_20",
                        "en": "tag_20",
                        "ja": "タグ_20"
                    }
                },
                {
                    "tag_name": {
                        "ko": "태그_16",
                        "en": "tag_16",
                        "ja": "タグ_16"
                    }
                }
            ]
        }),
        content_type='application/json',
        **headers,
    )

    headers = {"HTTP_x-wanted-language": "ko"}
    resp = api.get(
        "/companies/Wantedlab",
        **headers
    )
    company = json.loads(resp.content)
    assert resp.status_code == 200
    assert company == {
        "company_name": "원티드랩",
        "tags": [
            "태그_4",
            "태그_20",
            "태그_16",
        ],
    }

    # 검색된 회사가 없는경우 404를 리턴합니다.
    resp = api.get(
        "/companies/없는회사", headers=[("x-wanted-language", "ko")]
    )

    assert resp.status_code == 404


@pytest.mark.django_db
def test_new_company(api: Client):
    """
    3.  새로운 회사 추가
    새로운 언어(tw)도 같이 추가 될 수 있습니다.
    저장 완료후 header의 x-wanted-language 언어값에 따라 해당 언어로 출력되어야 합니다.
    """
    headers = {"HTTP_x-wanted-language": "tw"}
    resp = api.post(
        "/companies",
        data=json.dumps({
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
        }),
        content_type='application/json',
        **headers,
    )

    company = json.loads(resp.content)
    assert company == {
        "company_name": "LINE FRESH",
        "tags": [
            "tag_1",
            "tag_8",
            "tag_15",
        ],
    }
