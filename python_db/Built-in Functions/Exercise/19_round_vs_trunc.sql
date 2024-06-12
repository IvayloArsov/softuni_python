SELECT
    latitude,
    ROUND(latitude, 2) as round,
    TRUNC(latitude, 2) as trunc
FROM
    apartments