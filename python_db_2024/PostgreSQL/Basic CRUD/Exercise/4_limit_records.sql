SELECT 
    id,
    concat(first_name, ' ', last_name) as full_name,
    job_title
FROM  employees
ORDER BY first_name 
LIMIT 50