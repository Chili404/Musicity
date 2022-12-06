#Transactions
#Delete undefined tracks From Track's db
#Mainly for safety so we can rollback
#READ UNCOMMITTED as we don't mind if aaplication rads the data before it commits
SET TRANSACTION  ISOLATION LEVEL READ UNCOMMITTED;
START TRANSACTION;
	DELETE FROM musicity_db_track WHERE duration <= 0;
COMMIT;
ROLLBACK;

#SET track_streams if don't exist
#Repeatble read becasue we only want to add definite tracks to the streams table not ones to be deleted
SET TRANSACTION  ISOLATION LEVEL REPEATABLE READ;
USE music;
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
#Display Latest song/album release 
