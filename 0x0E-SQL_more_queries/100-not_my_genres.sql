-- uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter.
SELECT tv_genres.name
FROM tv_genres
WHERE tv_genres.name NOT IN(
    SELECT g.name FROM tv_shows m
    JOIN tv_show_genres sg
        ON sg.show_id = m.id
    JOIN tv_genres g
        ON sg.genre_id = g.id
    WHERE m.title = 'Dexter' 
)
ORDER BY tv_genres.name ASC;