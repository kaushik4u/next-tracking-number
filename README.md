# Tracking Number Generator API

This is a RESTful API that generates unique tracking numbers for parcels. The API is built with Django and Django REST Framework.

## Prerequisites

Ensure you have the following installed:
- Python 3.x
- pip (Python package manager)
- A virtual environment tool like `virtualenv` (optional but recommended)

## Set up a Virtual Environment

pip install virtualenv
virtualenv djangoceleryenv
source djangoceleryenv/bin/activate  # On Windows: djangoceleryenv\Scripts\activate

## Install Required Dependencies

pip install -r requirements.txt

## Run Migrations

python manage.py migrate
python manage.py runserver

The API will be available at http://127.0.0.1:8000/next-tracking-number/

## API Endpoint

- **GET /next-tracking-number/**
  - **Query Parameters**:
    - `origin_country_id` (e.g., "MY")
    - `destination_country_id` (e.g., "ID")
    - `weight` (e.g., "1.234")
    - `created_at` (e.g., "2018-11-20T19:29:32+08:00")
    - `customer_id` (e.g., "de619854-b59b-425e-9db4-943979e1bd49")
    - `customer_name` (e.g., "RedBox Logistics")
    - `customer_slug` (e.g., "redbox-logistics")

  - **Response**:
    ```json
  {
      "tracking_number": "J760J96DHWLYU2AF",
      "created_at": "2024-09-17T23:24:19.768057+05:30",
      "origin_country_id": "MY",
      "destination_country_id": "ID",
      "customer_id": "de619854-b59b-425e-9db4-943979e1bd49"
  }
    ```

This setup ensures that the response includes all the requested parameters along with the generated tracking number and its creation timestamp.