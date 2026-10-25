# Movie Catalog API

REST API for browsing a movie and director catalog. Built with FastAPI.

## Setup and Installation

### 1. Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Server

```bash
fastapi dev main.py
```

The server will be available at `http://127.0.0.1:8000`

## API Endpoints

### GET /movies
Get a list of movies with filters and pagination

**Query Parameters:**
- `genre` - movie genre (case-insensitive)
- `year_from` - year from (inclusive)
- `year_to` - year to (inclusive)
- `q` - search query in title (case-insensitive)
- `limit` - number of items per page (default: 10)
- `offset` - pagination offset (default: 0)

**Example Requests:**

1. Get all movies (first page):
```bash
curl http://127.0.0.1:8000/movies
```

2. Get drama movies:
```bash
curl "http://127.0.0.1:8000/movies?genre=drama"
```

3. Get movies from 2015 to 2020:
```bash
curl "http://127.0.0.1:8000/movies?year_from=2015&year_to=2020"
```

4. Search for movies containing "API":
```bash
curl "http://127.0.0.1:8000/movies?q=API"
```

5. Combined filters with pagination:
```bash
curl "http://127.0.0.1:8000/movies?genre=drama&year_from=2012&limit=5&offset=0"
```

### GET /movies/{m_id}
Get a single movie by ID

```bash
curl http://127.0.0.1:8000/movies/1
```

### GET /directors/{director_id}
Get a director by ID

```bash
curl http://127.0.0.1:8000/directors/1
```

### GET /directors/{director_id}/movies
Get all movies by a specific director

```bash
curl http://127.0.0.1:8000/directors/1/movies
```

## Project Structure

```
Movie Catalog API/
├── main.py          - API endpoints
├── data.py          - sample data (movies and directors)
├── requirements.txt - project dependencies
└── README.md        - documentation
```

## Sample API Responses

### GET /movies Response:
```json
{
  "total": 9,
  "limit": 10,
  "offset": 0,
  "items": [
    {
      "id": 1,
      "title": "API Keys for beginners",
      "year": 2010,
      "genre": "drama",
      "rating": 8.1,
      "director_id": 1
    }
  ]
}
```

### GET /movies/{id} Response:
```json
{
  "id": 1,
  "title": "API Keys for beginners",
  "year": 2010,
  "genre": "drama",
  "rating": 8.1,
  "director_id": 1
}
```

### GET /directors/{id} Response:
```json
{
  "id": 1,
  "name": "Max Sntxzss",
  "country": "The USA"
}
```
