SELECT
    ph.id as photo_id,
    ph.capture_date,
    ph.description,
    COUNT(cm.id) as comments_count
FROM
    photos as ph
JOIN
    comments as cm
ON
    ph.id = cm.photo_id

WHERE
    ph.description IS NOT NULL
GROUP BY
    ph.id
ORDER BY
    comments_count DESC,
    photo_id ASC
LIMIT 3;