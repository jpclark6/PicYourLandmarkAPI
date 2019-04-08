# Pic Your Landmark API

DIg into gogole api to see if it also includes description and if it is better overall

## Endpoints

Starting endpoint at https://pic-landmark-api.herokuapp.com

#### Get new landmarks at location

Include latitude and longitude to get top 10 results added to full database of locations.

Ex. GET 

Returns:

```
[
    ...
    {
        "id": 18,
        "name": "Fairmount Cemetery",
        "lat": 39.70553,
        "lon": -104.89692
    },
    {
        "id": 19,
        "name": "Crescent Park",
        "lat": 39.72875,
        "lon": -104.90018
    },
    {
        "id": 20,
        "name": "Crestmoor Park",
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