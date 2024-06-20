CREATE OR REPLACE PROCEDURE udp_modify_account(
    IN address_street VARCHAR(30),
    IN address_town VARCHAR(30)
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_account_id INTEGER;
    v_current_job_title VARCHAR(40);
    v_new_job_title VARCHAR(50);
BEGIN
    SELECT a.id, a.job_title
    INTO v_account_id, v_current_job_title
    FROM accounts a
    JOIN addresses ad ON a.id = ad.account_id
    WHERE ad.street = address_street AND ad.town = address_town;
    v_new_job_title := '(Remote) ' || v_current_job_title;

    UPDATE accounts
    SET job_title = v_new_job_title
    WHERE id = v_account_id;

END;
$$;

CALL udp_modify_account('97 Valley Edge Parkway', 'Divinópolis');
SELECT a.username, a.gender, a.job_title FROM accounts AS a
WHERE a.job_title ILIKE '(Remote)%';