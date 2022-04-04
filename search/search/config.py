"""Search development configuration."""


# Database file is var/insta485.sqlite3
DATABASE_FILENAME = 'var/index.sqlite3'

SEARCH_INDEX_SEGMENT_API_URLS = [
    "http://localhost:9000/api/v1/hits/",
    "http://localhost:9001/api/v1/hits/",
    "http://localhost:9002/api/v1/hits/",
]
