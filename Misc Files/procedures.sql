#Stored Procedures
#--------------------Query Track Duration----------------
USE music;
DROP PROCEDURE IF EXISTS QueryDuration;

DELIMITER //
USE music //
CREATE PROCEDURE QueryDuration(IN start_dur integer, IN end_dur integer)
BEGIN
	SELECT * FROM musicity_db_track
	WHERE duration >= start_dur
    AND duration <=end_dur;
END//
DELIMITER ;
#testing 
set @sd = 100;
set @ed = 300;
 call QueryDuration(100, 200);
#----------------------------------------------------------