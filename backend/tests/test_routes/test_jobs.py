import json


def test_create_job(client):
    data = {
        "title": "SDE 1 Yahoo",
        "company": "hoo",
        "company_url": "https://www.fdj.com",
        "location": "USA, NY",
        "description": "Testing",
        "date_posted": "2023-04-23"
    }
    # noinspection PyTypeChecker
    response = client.post("/jobs/create-job", data=json.dumps(data))
    assert response.status_code == 200
    assert response.json()["title"] == "SDE 1 Yahoo"


def test_retrieve_job_by_id(client):
    data = {
        "title": "SDE 1 Yahoo",
        "company": "hoo",
        "company_url": "https://www.fdj.com",
        "location": "USA, NY",
        "description": "Testing",
        "date_posted": "2023-04-23"
    }
    # noinspection PyTypeChecker
    client.post("/jobs/create-job", data=json.dumps(data))
    response = client.get("/jobs/get/1")
    assert response.status_code == 200
    assert response.json()["title"] == "SDE 1 Yahoo"
