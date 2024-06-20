SELECT 
    REPLACE(title, 'The', '***')
AS 
    title_censored
FROM 
    books
WHERE 
    SUBSTRING(title, 1, 3) = 'The'