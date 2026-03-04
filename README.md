# Address Sphere API

A minimal FastAPI-based Address Book API that allows users to create, update, delete, and retrieve addresses with geographic coordinates. The API also supports searching for addresses within a given distance from a specified location.

## Features
- Create address
- Update address
- Delete address
- Retrieve all addresses
- Search addresses within a given distance
- Input validation using Pydantic
- SQLite database using SQLAlchemy
- Logging with rotating log files
- Error handling
- Swagger API documentation

## Tech Stack
- Python 3
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Geopy
- Uvicorn

## Project Structure
```
address-sphere
│
├── app.py
├── core
│   ├── config.py
│   └── logging_config.py
│
├── db
│   ├── base.py
│   ├── models.py
│   └── session.py
│
├── schema
│   └── address.py
│
├── business
│   └── address_logic.py
│
├── requirements.txt
├── .env
└── README.md
```
## Installation

Clone the repository

git clone <your-repository-url>

cd address-sphere

Create virtual environment

python -m venv myenv

Activate virtual environment (Windows)

myenv\Scripts\activate

Install dependencies

pip install -r requirements.txt

## Run the Application

Start the server

python app.py

Application runs at

http://127.0.0.1:8000

## API Documentation

Swagger UI

http://127.0.0.1:8000/docs

ReDoc

http://127.0.0.1:8000/redoc

## API Endpoints

Create Address

POST /address

Example JSON

{
  "address": "MG Road Bangalore",
  "lat": 12.9716,
  "lon": 77.5946
}

Get All Addresses

GET /addresses

Update Address

PUT /address/{address_id}

Example JSON

{
  "address": "MG Road Metro Station",
  "lat": 12.9718,
  "lon": 77.5945
}

Delete Address

DELETE /address/{address_id}

Find Nearby Addresses

GET /addresses/nearby?lat=12.9716&lon=77.5946&distance_km=5

Health Check

GET /health

Response

{
  "status": "OK"
}

## Logging

Logs are stored in

app.log

Rotating log files are used to prevent large log files.

## Environment Variables

Create a `.env` file

DATABASE=sqlite:///./address.db
LOGINFO=INFO

## Author

FastAPI Python Developer Assignment – Address Sphere API
