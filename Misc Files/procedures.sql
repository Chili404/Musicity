#Stored Procedures
#-----------------------------------------------------
#--------------------Query Track Duration----------------
#-----------------------------------------------------
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

#-----------------------------------------------------
#--------------------Query Track Genre----------------
#-----------------------------------------------------
USE music;
DROP PROCEDURE IF EXISTS QueryGenre;

DELIMITER //
USE music //
CREATE PROCEDURE QueryGenre(IN in_genre varchar(2))
BEGIN
	SELECT * FROM musicity_db_track
	WHERE genre = in_genre;
END//
DELIMITER ;
#testing 
set @test = "rb";
call QueryGenre(@test);
