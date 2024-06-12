SELECT
    population,
    length(CAST(population AS text))
FROM
    countries