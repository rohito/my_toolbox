def love_movies():
    print("""
          # pylint: disable=missing-docstring, C0103
          # import sqlite3
# from unittest import result

conn = sqlite3.connect('data/movies.sqlite')
conn.row_factory = sqlite3.Row

def love_movies(db):
    # return the list of all movies which contain the exact word "love"
    # in their title, sorted in alphabetical order
    db = conn.cursor()
    query = " (triple quote)
    SELECT movies.title
FROM movies
WHERE UPPER(movies.title) LIKE  "% LOVE %" OR
UPPER(movies.title) LIKE  "LOVE %" OR
UPPER(movies.title) LIKE  "% LOVE" OR
UPPER(movies.title) LIKE  "LOVE" OR
UPPER(movies.title) LIKE  "%LOVE,%" OR
UPPER(movies.title) LIKE  "%LOVE.%" OR
UPPER(movies.title) LIKE  "%LOVE'%"
ORDER BY movies.title
    " (triple quote)
    db.execute(query)
    results = db.fetchall()
    return [movies[0] for movies in results]
    """)
