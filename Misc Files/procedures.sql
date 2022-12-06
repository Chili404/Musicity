#Stored Procedures
DROP PROCEDURE IF EXISTS `debug_msg`;
DELIMITER //
CREATE PROCEDURE debug_msg(enabled INTEGER, msg VARCHAR(255))
BEGIN
  IF enabled THEN
    select concat('** ', msg) AS '** DEBUG:';
  END IF;
END //

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

#-----------------------------------------------------
#--------------------Query Track Artist----------------
#-----------------------------------------------------
USE music;
DROP PROCEDURE IF EXISTS QueryArtist;

DELIMITER //
USE music //
CREATE PROCEDURE QueryArtist(IN in_artist varchar(100))
BEGIN
	SELECT * FROM musicity_db_track
	WHERE artist_id_id IN (
		SELECT id FROM musicity_db_artist
		WHERE name = in_artist
	);
END//
DELIMITER ;

#-----------------------------------------------------
#--------------------Query Track Album----------------
#-----------------------------------------------------
USE music;
DROP PROCEDURE IF EXISTS QueryAlbum;

DELIMITER //
USE music //
CREATE PROCEDURE QueryAlbum(IN in_album varchar(100))
BEGIN
	SELECT * FROM musicity_db_track
	WHERE album_id_id IN (
		SELECT id FROM musicity_db_album
		WHERE name = in_album
	);
END//
DELIMITER ;

#-----------------------------------------------------
#--------------------Query Track Name----------------
#-----------------------------------------------------
USE music;
DROP PROCEDURE IF EXISTS QueryName;

DELIMITER //
USE music //
CREATE PROCEDURE QueryName(IN in_name varchar(100))
BEGIN
	SELECT * FROM musicity_db_track
	WHERE name = in_name;
END//
DELIMITER ;