CREATE OR REPLACE FUNCTION fn_is_word_comprised (
    set_of_letters VARCHAR,
    word VARCHAR
) RETURNS BOOLEAN

AS
$$
BEGIN
    RETURN TRIM(LOWER(word), LOWER(set_of_letters)) = '';
END;
$$

LANGUAGE plpgsql;
