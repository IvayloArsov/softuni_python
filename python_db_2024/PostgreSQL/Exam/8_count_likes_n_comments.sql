SELECT 
    p.id AS photo_id,
    COALESCE(l.likes_count, 0) AS likes_count,
    COALESCE(c.comments_count, 0) AS comments_count
FROM 
    photos p
LEFT JOIN (
    SELECT 
        photo_id,
        COUNT(id) AS likes_count
    FROM 
        likes
    GROUP BY 
        photo_id
) l ON p.id = l.photo_id
LEFT JOIN (
    SELECT 
        photo_id,
        COUNT(id) AS comments_count
    FROM 
        comments
    GROUP BY 
        photo_id
) c ON p.id = c.photo_id

ORDER BY
    likes_count DESC,
    comments_count DESC,
    photo_id ASC;
