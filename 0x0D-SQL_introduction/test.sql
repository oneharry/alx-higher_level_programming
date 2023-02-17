DROP TABLE IF EXISTS `temperatures`;

CREATE TABLE `temperatures` (
  `city` varchar(256) DEFAULT NULL,
  `state` varchar(128) DEFAULT NULL,
  `year` int(11) DEFAULT NULL,
  `month` int(11) DEFAULT NULL,
  `value` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `temperatures` WRITE;
INSERT INTO `temperatures` VALUES ('San Francisco','CA',2000,1,45),('San Francisco','CA',2000,2,94),('San Francisco','CA',2000,3,60),('San Francisco','CA',2000,4,95),('San Francisco','CA',2000,5,72),('San Francisco','CA',2000,6,70),('San Francisco','CA',2000,7,88),('San Francisco','CA',2000,8,58),('San Francisco','CA',2000,9,90),('San Francisco','CA',2000,10,80),('San Francisco','CA',2000,11,52),('San Francisco','CA',2000,12,93),('San Francisco','CA',2001,1,64),('San Francisco','CA',2001,2,91),('San Francisco','CA',2001,3,55),('San Francisco','CA',2001,4,107),('San Francisco','CA',2001,5,54),('San Francisco','CA',2001,6,51),('San Francisco','CA',2001,7,53),('San Francisco','CA',2001,8,41),('San Francisco','CA',2001,9,44),('San Francisco','CA',2001,10,93),('San Francisco','CA',2001,11,70),('San Francisco','CA',2001,12,46),('San Francisco','CA',2002,1,102),('San Francisco','CA',2002,2,70),('San Francisco','CA',2002,3,39),('San Francisco','CA',2002,4,90),('San Francisco','CA',2002,5,100),('San Francisco','CA',2002,6,77),('San Francisco','CA',2002,7,54),('Oakland','CA',2011,5,107),('Oakland','CA',2011,6,41),('Oakland','CA',2011,7,81),('San Diego','CA',2009,10,64),('San Diego','CA',2009,11,106),('Sunnyvale','CA',2010,3,106),('Sunnyvale','CA',2010,4,97),('Sonoma','CA',2003,11,65),('Sonoma','CA',2003,12,46),('Sonoma','CA',2004,1,89),('San Jose','CA',2008,11,51),('San Jose','CA',2008,12,92),('Pismo beach','CA',2014,5,34),('Pismo beach','CA',2014,6,98),('Pismo beach','CA',2014,7,53);

UNLOCK TABLES;
