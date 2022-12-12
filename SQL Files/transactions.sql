#Transactions
#Delete undefined tracks From Track's db
#Mainly for safety so we can rollback
#READ UNCOMMITTED as we don't mind if aaplication rads the data before it commits
SET TRANSACTION  ISOLATION LEVEL READ committed;
START TRANSACTION;
	DELETE FROM musicity_db_track WHERE duration <= 0;
COMMIT;
ROLLBACK;

#SET track_streams if don't exist
#Repeatble read becasue we only want to add definite tracks to the streams table not ones to be deleted
SET TRANSACTION  ISOLATION LEVEL REPEATABLE READ;
DROP PROCEDURE IF EXISTS AddStreams;
DELIMITER //
CREATE PROCEDURE AddStreams()
BEGIN
	DECLARE n INT DEFAULT 0;
	DECLARE i INT DEFAULT 0;
    DECLARE m_id INT DEFAULT 0;
    DECLARE COUNT INT DEFAULT 0;
	SELECT COUNT(*) FROM musicity_db_track INTO n;
	SET i=0;
	WHILE i<n DO 
        SELECT id FROM musicity_db_track LIMIT i,1 INTO m_id;
        call debug_msg(@m_id, (select concat_ws('','arg1:', m_id)));
		SET i = i + 1;
        SELECT COUNT(*) FROM musicity_db_streams WHERE track_id_id = m_id INTO count;
        IF count < 1 THEN
			START TRANSACTION;
				INSERT INTO musicity_db_streams (streams, track_id_id) VALUES (0, m_id);
			COMMIT;
            call debug_msg(@m_id, (select concat_ws('','arg2:', count)));
        END IF;
	END WHILE;
END//
DELIMITER ;
call AddStreams();

#Check to add track to top 100
#READ UNCOMMITTED AS IT SHOULD UPDATE TO NON_CIMMITED TRANSACTIONS TO BE MORE ACCURATE
DROP PROCEDURE IF EXISTS Top10;
SET TRANSACTION  ISOLATION LEVEL READ UNCOMMITTED;

DELIMITER //
CREATE PROCEDURE Top10()
BEGIN
	DECLARE n INT DEFAULT 0;
	DECLARE i INT DEFAULT 0;
	DECLARE m_id INT DEFAULT 0;
    DECLARE ST REAL DEFAULT 0.00;
	START TRANSACTION;
	CREATE TABLE tops AS 
		SELECT t.id, 0 as track_rank, t.name AS name, a.name AS artist, al.name AS album, s.streams AS streams, "hhhhhhhhhhhhhhhhhhhhh" AS stream_w, "Hotubibuibuibu" as hot FROM musicity_db_track AS t
		INNER JOIN musicity_db_artist AS a ON a.id = t.artist_id_id
		INNER JOIN musicity_db_album AS al ON t.album_id_id = al.id
		JOIN musicity_db_streams AS s ON s.track_id_id = t.id
		ORDER BY streams DESC
        LIMIT 10;
	
	SELECT COUNT(*) FROM tops INTO n;
	SET i=0;
	WHILE i< n DO 
        SELECT id FROM tops LIMIT i,1 INTO m_id;
        call debug_msg(@m_id, (select concat_ws('','arg1:', m_id)));
		UPDATE tops SET track_rank = i+1 WHERE id = m_id;
        
        SELECT streams FROM tops LIMIT i,1 INTO ST;
        
        IF ST > 999999 AND ST < 10000000 THEN
			SELECT ST/1000000 INTO ST;
            UPDATE tops SET stream_w = (SELECT CONCAT((SELECT CONVERT((SELECT ROUND(ST, 2)), CHAR)), " Million")) WHERE id = m_id;
        ELSEIF ST > 9999999 AND ST < 100000000 THEN
			SELECT ST/1000000 INTO ST;
            UPDATE tops SET stream_w = (SELECT CONCAT((SELECT CONVERT((SELECT ROUND(ST, 1)), CHAR)), " Million")) WHERE id = m_id;
		ELSEIF ST > 99999999 AND ST < 1000000000 THEN
			SELECT ST/1000000 INTO ST;
            UPDATE tops SET stream_w = (SELECT CONCAT((SELECT CONVERT((SELECT ROUND(ST, 1)), CHAR)), " Million")) WHERE id = m_id;
		ELSEIF ST > 999999999 THEN
			SELECT ST/1000000000 INTO ST;
            UPDATE tops SET stream_w = (SELECT CONCAT((SELECT CONVERT((SELECT ROUND(ST, 2)), CHAR)), " Billion")) WHERE id = m_id;
        ELSEIF ST <= 999999 THEN
			SELECT streams FROM tops  WHERE id=m_id INTO ST;
            UPDATE tops SET stream_w = (SELECT CONVERT(ST, CHAR)) WHERE id = m_id;
        END IF;
        SET i = i + 1;
	END WHILE;
        
	#hotness level
    UPDATE tops SET hot = "Smoldering" WHERE streams >= 0;
    UPDATE tops SET hot = "Heating Up" WHERE streams > 100000;
    UPDATE tops SET hot = "Hot" WHERE streams > 1000000;
    UPDATE tops SET hot = "VERY HOT!" WHERE streams > 10000000;
	UPDATE tops SET hot = "ON FIRE!!" WHERE streams > 100000000;
	UPDATE tops SET hot = "!!!SUPERNOVA!!!" WHERE streams > 1000000000;
    
    SELECT * FROM tops;
    DROP TABLE tops;
    COMMIT;
END//
DELIMITER ;

call Top10();
