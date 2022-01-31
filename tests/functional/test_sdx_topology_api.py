"""
SDX Topology API test
"""
import json
import requests


def test_oxp_url(api_data):
    """ test a POST and GET request to SDX topology APi to retrieve the current
    oxp_url"""
    response = requests.post(
            url=api_data["url"]+"oxp_url", data=json.dumps("amlight.net"),
            headers=api_data["headers"])
    assert response.status_code == 200
    response = requests.get(
            url=api_data["url"]+"oxp_url", headers=api_data["headers"])
    assert response.status_code == 200
    assert "amlight.net" in response.json()
