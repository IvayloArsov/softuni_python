DELETE FROM addresses
WHERE 
    id % 2 = 0  
    AND lower(street) LIKE '%r%';