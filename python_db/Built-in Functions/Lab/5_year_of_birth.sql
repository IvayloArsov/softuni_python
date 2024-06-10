SELECT
    first_name,
    last_name,
    EXTRACT(year FROM born)
FROM
    authors