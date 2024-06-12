UPDATE
    countries
SET
    country_code = lower(reverse(country_code))

RETURNING *;