SELECT 
    id,
    concat(number, ' ', street) as address, 
    city_id
FROM addresses
WHERE id >= 20