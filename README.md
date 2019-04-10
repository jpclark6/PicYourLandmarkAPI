# Pic Your Landmark API

This is a Django API to serve up the app [Pic Your Landmark](https://github.com/hlhartley/PicYourLandmark), React Native app. It includes user creation, finding landmarks based on latitude and longitude, and saving those landmarks to your user profile with a link to a url for the picture associated with the landmark. 

## Endpoints

Starting endpoint at https://pic-landmark-api.herokuapp.com

#### Get new landmarks at location

Include latitude and longitude to get top 10 results added to full database of locations.

GET */api/v1/locations/?lat=user_latitude&lon=user_longitude*

Ex. GET */api/v1/locations/?lat=39.665196&lon=-105.205788*

Returns:

```
[
    ...
    {
        "id": 73,
        "name": "Matthews Winters Open Space Park",
        "lat": 39.68431,
        "lon": -105.21269,
        "description": null
    },
    {
        "id": 74,
        "name": "South Dinosaur Open Space Park",
        "lat": 39.66777,
        "lon": -105.19186,
        "description": null
    },
    {
        "id": 75,
        "name": "Mt Falcon Open Space Park",
        "lat": 39.65297,
        "lon": -105.20353,
        "description": null
    },
    ...
]
```

#### Create A User

POST */api/v1/users/?email=users_email&username=the_username&password=the_password&password_confirmation=the_password*

Ex. POST */api/v1/users/?email=landmarker@example.com&username=landmarker&password=abc123&password_confirmation=abc123*

Returns:

```
{
    "id": 27,
    "email": "landmarker@example.com",
    "username": "landmarker",
    "profile_url": "",
    "locations": []
}
```

#### Update User Profile Photo

PATCH */api/v1/users/:user_id/?profile_url=the_profile_url*

Ex. PATCH */api/v1/users/27/?profile_url=www.newpicture.com*

Returns:

```
{
    "id": 27,
    "email": "landmarker@example.com",
    "username": "landmarker",
    "profile_url": "www.newpicture.com",
    "locations": []
}
```

#### Add Location To User

POST */api/v1/users/:user_id/landmarks/?url=location_photo_url&location=location_id*

Ex. POST */api/v1/users/27/landmarks/?url=www.pictureloc.com&location=73*

Returns:

```
{
    "user_id": 27,
    "username": "landmarker",
    "profile_url": "www.newpicture.com",
    "user_locations": [
        {
            "name": "Matthews Winters Open Space Park",
            "description": null,
            "lat": 39.68431,
            "lon": -105.21269,
            "landmark_id": 73,
            "photo_url": "www.pictureloc2.com"
        },
        {
            "name": "Sand Creek Park",
            "description": null,
            "lat": 39.75478,
            "lon": -104.84476,
            "landmark_id": 64,
            "photo_url": "www.pictureloc.com"
        }
    ]
}
```

#### Get List Of User's Locations

GET */api/v1/users/?username=the_username&password=the_password*

Ex. GET */api/v1/users/?username=landmarker&password=abc123*

Returns:

```
{
    "user_id": 27,
    "username": "landmarker",
    "profile_url": "www.newpicture.com",
    "user_locations": [
        {
            "name": "Matthews Winters Open Space Park",
            "description": null,
            "lat": 39.68431,
            "lon": -105.21269,
            "landmark_id": 73,
            "photo_url": "www.pictureloc2.com"
        },
        {
            "name": "Sand Creek Park",
            "description": null,
            "lat": 39.75478,
            "lon": -104.84476,
            "landmark_id": 64,
            "photo_url": "www.pictureloc.com"
        }
    ]
}
```

#### Update User's Photo For A Given Location

PATCH */api/v1/users/:user_id/landmarks/:landmark_id/?photo_url=new_url*

Ex. PATCH */api/v1/users/27/landmarks/73/?photo_url=www.new_url.com*

Returns:

```
{
    "user_id": 27,
    "username": "landmarker",
    "profile_url": "www.newpicture.com",
    "user_locations": [
        {
            "name": "Matthews Winters Open Space Park",
            "description": null,
            "lat": 39.68431,
            "lon": -105.21269,
            "landmark_id": 73,
            "photo_url": "www.new_url.com"
        },
        {
            "name": "Sand Creek Park",
            "description": null,
            "lat": 39.75478,
            "lon": -104.84476,
            "landmark_id": 64,
            "photo_url": "www.pictureloc.com"
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

This app tests most endpoints with both happy and sad path testing. It also uses CircleCI for continuous integration. To run the tests enter the following into the terminal:

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

## Tech

* Django
* rest_framework
* gunicorn
* PostgreSQL
* CircleCI

## Authors - Back End

* Justin Clark - https://github.com/jpclark6

## Authors - Front End

* Heather Hartley - https://github.com/hlhartley
* Matthew Foxwell - https://github.com/foxwellm
