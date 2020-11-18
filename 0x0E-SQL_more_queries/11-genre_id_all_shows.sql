-- lists all shows contained in the database hbtn_0d_tvshows.
SELECT m.title "title", g.id "genre_id" FROM tv_shows m
LEFT OUTER JOIN tv_show_genres sg 
	ON sg.show_id = m.id 
LEFT OUTER JOIN tv_genres g 
	ON sg.genre_id = g.id
ORDER BY m.title, g.id;