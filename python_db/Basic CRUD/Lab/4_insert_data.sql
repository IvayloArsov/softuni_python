INSERT INTO employees(first_name, last_name, job_title, department_id, salary)
VALUES 
	('Samantha', 'Young', 'Housekeeping', 4, 900.00),
    ('Roger', 'Palmer', 'Waiter', 3, 928.33);


SELECT 
    id,
	first_name,
	last_name,
    job_title,
    department_id,
    salary
FROM 
    employees
ORDER BY
    id;