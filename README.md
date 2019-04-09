# Pic Your Landmark API

This is a Django API to serve up the app [Pic Your Landmark](https://github.com/hlhartley/PicYourLandmark). It includes user creation, finding landmarks based on latitude and longitude, and saving those landmarks to your user profile with a link to a url for the picture associated with the landmark. 

## Endpoints

Starting endpoint at https://pic-landmark-api.herokuapp.com

#### Get new landmarks at location

Include latitude and longitude to get top 10 results added to full database of locations.

Ex. GET /api/v1/locations/?lat=39.719683&lon=-104.498445

Returns:

```
[
    ...
    {
        "id": 18,
        "name": "Fairmount Cemetery",
        "description": "Good cemetary",
        "lat": 39.70553,
        "lon": -104.89692
    },
    {
        "id": 19,
        "name": "Crescent Park",
        "description": "Ok park",
        "lat": 39.72875,
        "lon": -104.90018
    },
    {
        "id": 20,
        "name": "Crestmoor Park",
        "description": "Better park",
        "lat": 39.71309,
        "lon": -104.91708
    }
    ...
]
```

#### Create A User

Ex. POST /api/v1/users/?email=joe44@example.com&username=joe55&password=abc123&password_confirmation=abc123

Returns:

```
{
    "id": 4
    "email": "joe44@example.com",
    "username": "joe55",
    "locations": []
}
```

#### Add Location To User

Ex. POST /api/v1/users/4/landmarks/?url=www.pictureloc.com&location=20

Returns list of user's locations:

```
{
    "user_id": 1,
    "username": "joe55",
    "user_locations": [
        {
            "name": "Great Lawn Park",
            "description": "Beautiful Park",
            "lat": 39.72386,
            "lon": -104.88715,
            "landmark_id": 6,
            "photo_url": "www.myimage.com/2"
        },
        {
            "name": "Buckley Annex",
            "description": "Beautiful Park",
            "lat": 39.7159,
            "lon": -104.90379,
            "landmark_id": 3,
            "photo_url": "www.myimage.com"
        }
    ]
}
```

#### Get List Of User's Locations

Ex. GET /api/v1/users/?username=joe55&password=abc123

```
{
    "user_id": 1,
    "username": "joe55",
    "user_locations": [
        {
            "name": "Great Lawn Park",
            "description": "Beautiful Park",
            "lat": 39.72386,
            "lon": -104.88715,
            "landmark_id": 6,
            "photo_url": "www.myimage.com/2"
        },
        {
            "name": "Buckley Annex",
            "description": "Beautiful Park",
            "lat": 39.7159,
            "lon": -104.90379,
            "landmark_id": 3,
            "photo_url": "www.myimage.com"
        }
    ]
}
```

## Getting Started

### Prerequisites

Make sure you have the following installed before installing the app:

* Python 3.7
* PostgreSQL
* Pip3

### Setup

Run these commands in your terminal once you're in the directory you'd like to save the project:

```
git clone git@github.com:jpclark6/PicYourLandmarkAPI.git
cd PicYourLandmarkAPI
psql
create database landmarks;
quit
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver
```

## Running the Tests

This app has most endpoints happy and sad path tested. To run the tests enter the following into the terminal:

```
python3 manage.py test
```

The tests test the endpoints and database to make sure everything is in working order. This is an example of the user creation test:

```
def test_create_a_user(self):
        email = 'test1'
        username = 'joe'
        password = 'test2'
        response = self.client.post(
            f'/api/v1/users/?email={email}&username={username}&password={password}&password_confirmation={password}'
        )
        self.assertEqual(response.data['email'], email)
        self.assertEqual(response.data['username'], username)
```

## Authors - Back End

* Justin Clark - https://github.com/jpclark6

## Authors - Front End

* Heather Hartley - https://github.com/hlhartley
* Matthew Foxwell - https://github.com/foxwellm