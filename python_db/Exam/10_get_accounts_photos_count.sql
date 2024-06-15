CREATE OR REPLACE FUNCTION udf_accounts_photos_count(account_username VARCHAR(30))
RETURNS INTEGER 
AS 
$$
DECLARE
    var_account_id INTEGER;
    photos_count INTEGER;
BEGIN
    SELECT id INTO var_account_id
    FROM accounts
    WHERE username = account_username;

    SELECT COUNT(*)
    INTO photos_count
    FROM accounts_photos
    WHERE account_id = var_account_id;

    RETURN photos_count;
END;
$$ 
LANGUAGE plpgsql;