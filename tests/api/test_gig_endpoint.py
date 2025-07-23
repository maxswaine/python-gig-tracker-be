import pytest


@pytest.fixture
def gig_data():
    return {
        "artists": [
            "Loyle Carner"
        ],
        "venue": "O2 Brixton",
        "date": "2017-10-06",
        "location": "London",
        "favourite": True
    }

def assert_unchanged_gig_fields(data, gig_data):
    assert data["id"] is not None
    assert data["venue"] == gig_data["venue"]
    assert data["location"] == gig_data["location"]
    assert data["favourite"] == gig_data["favourite"]


def assert_gig_request_to_gig_creation_defaults(response_data, gig_data):
    response_artists_names = [artist["name"] for artist in response_data["artists"]]
    expected_artist_names = gig_data["artists"]
    assert response_artists_names == expected_artist_names

def assert_get_gig_to_gig_creation_defaults(response_data, gig_data):
    response_artists_names = [artist["name"] for artist in response_data["artists"]]
    expected_artist_names = [artist["name"] for artist in gig_data["artists"]]
    assert response_artists_names == expected_artist_names


@pytest.fixture
def created_gig(client, gig_data):
    response = client.post("/gigs/", json=gig_data)
    assert response.status_code == 200
    data = response.json()
    assert_gig_request_to_gig_creation_defaults(data, gig_data)
    return data


def test_post_gig(created_gig):
    # Sanity check that fixture returns correct data
    assert created_gig["venue"] == "O2 Brixton"


def test_post_gig_moments(client, created_gig):
    endpoint = f"/gigs/{created_gig['id']}/moments/"

    moments_payload = {
        "moments": [
            {"description": "They played my favorite song"},
            {"description": "The encore was amazing"}
        ]
    }

    response = client.post(endpoint, json=moments_payload)
    assert response.status_code == 200

    moments = response.json()
    assert len(moments) == 2
    assert moments[0]["description"] == "They played my favorite song"
    assert moments[1]["description"] == "The encore was amazing"

def test_get_gig_by_id(client, created_gig):
    created_gig_id = created_gig['id']
    endpoint = f"/gigs/{created_gig_id}/"

    response = client.get(endpoint)
    data = response.json()
    assert response.status_code == 200

    assert data['id'] == created_gig_id
    assert_get_gig_to_gig_creation_defaults(data, created_gig)

