from rest_framework.test import APIClient
from resume.models import Resume
from django.contrib.auth.models import User
import pytest


@pytest.fixture
def setup():
    owner = User.objects.create_user("owner", "lennon@thebeatles.com", "pass1")
    resume = Resume(
        id=1, status="status", grade="grade", specialty="spec",
        salary="selary", education="education", experience="exp",
        portfolio="www.123.com", phone="3131231", email="ab@cd.ef",
        owner=owner)
    resume.save()
    yield


@pytest.fixture
def client():
    return APIClient()


@pytest.mark.django_db
def test_list(setup, client):
    resp = client.get('/api/resume/')
    assert resp.status_code == 200


@pytest.mark.django_db
def test_retrieve(setup, client):
    resp = client.get('/api/resume/1/')
    assert resp.status_code == 200


@pytest.mark.django_db
def test_partial_update(setup, client):
    resp = client.patch('/api/resume/1/', data={"status": "NEW_status"})
    assert resp.status_code == 403
    client.login(username='owner', password='pass1')
    resp = client.patch('/api/resume/1/', data={"status": "NEW_status"})
    assert resp.status_code == 200


@pytest.mark.django_db
def test_not_allowed(setup, client):
    client.login(username='owner', password='pass1')

    resp = client.post('/api/resume/')
    assert resp.status_code == 405

    resp = client.put('/api/resume/1/')
    assert resp.status_code == 405

    resp = client.delete('/api/resume/1/')
    assert resp.status_code == 405
