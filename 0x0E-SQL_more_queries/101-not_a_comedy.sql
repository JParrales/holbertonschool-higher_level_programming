-- lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.title NOT IN(
    SELECT m.title FROM tv_shows m
    JOIN tv_show_genres sg
        ON sg.show_id = m.id
    JOIN tv_genres g
        ON sg.genre_id = g.id
    WHERE g.name = 'Comedy'
)
ORDER BY tv_shows.title ASC;