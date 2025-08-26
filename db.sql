CREATE DATABASE  IF NOT EXISTS `hospital`;
USE `hospital`;

CREATE TABLE `apptdb` (
  `id` int(10) NOT NULL,
  `ptid` int(5) NOT NULL,
  `appt_date` date NOT NULL,
  `doctor` int(3) NOT NULL,
  `doctor_dept` int(3) NOT NULL,
  `vital_signs` varchar(100) DEFAULT NULL,
  `appt_status` char(10) DEFAULT 'scheduled',
  `diagnosis` varchar(200) DEFAULT NULL,
  `meds` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
);


INSERT INTO `apptdb` VALUES (2,5,'2024-12-12',3,2,'Blood Pressure: 69/20 \nTemperature: 70c \nAdditional Comments: bro is acting sus','Completed','He is currently having skill issues','Panadol,2tabs,per day after lunch|Laxatives,1tabs,whenever u want'),(3,11,'2024-11-11',3,1,NULL,'Completed','NONE','NONE'),(4,1,'2024-12-13',2,2,'Blood Pressure: 40/50 \nTemperature: 60c \nAdditional Comments: bro is addicted to genshin','Completed','Lay off genshin','Panadol,1tablet,for when you get a headache playing'),(5,1,'2012-12-12',3,1,'Blood Pressure: 182/80 \nTemperature: 50c \nAdditional Comments: bros acting sus','Completed','too much genshin','panadol,1tablet,when u get headache from playing genshin'),(6,5,'2024-12-13',2,2,NULL,'cancelled',NULL,NULL),(7,12,'2024-12-15',2,2,NULL,'Completed','Sick','Panadol,1table,per day'),(8,13,'2001-12-13',4,3,'tgffg','Completed','sick','panadol,1tablet,after lunch|panadrex,1tablet,before bed'),(9,5,'2024-12-12',2,2,NULL,'scheduled',NULL,NULL),(10,9,'2024-03-23',3,1,NULL,'Completed',NULL,NULL);


CREATE TABLE `dept` (
  `id` int(3) NOT NULL,
  `name` varchar(3) NOT NULL,
  PRIMARY KEY (`id`)
);



INSERT INTO `dept` VALUES (1,'PED'),(2,'ORG'),(3,'ENT');


CREATE TABLE `doctors` (
  `id` int(3) NOT NULL,
  `name` varchar(30) NOT NULL,
  `dept` int(3) NOT NULL,
  `specialty` char(15) DEFAULT 'Consultant',
  PRIMARY KEY (`id`)
);


INSERT INTO `doctors` VALUES (1,'Usama',1,'Consultant'),(2,'Phil',2,'Consultant'),(3,'Ducktor',1,'Surgeon'),(4,'Wahid',3,'Surgeon'),(5,'Nihaal',2,'Consultant');


CREATE TABLE `nurses` (
  `id` int(3) NOT NULL,
  `name` varchar(30) NOT NULL,
  `assigned_to` int(11) DEFAULT NULL,
  `dept` int(11) DEFAULT NULL,
  `username` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
);

INSERT INTO `nurses` VALUES (1,'Sophia',3,1,'sophia'),(2,'Christina',1,1,'lol'),(3,'Chad Prakash',2,2,'chad'),(4,'Homie',NULL,NULL,'hom'),(5,'Aisha',NULL,NULL,'aisha'),(6,'najad',5,2,'najad');



CREATE TABLE `patients` (
  `ptID` int(5) NOT NULL,
  `ptName` varchar(30) NOT NULL,
  `govtid` int(10) NOT NULL,
  `dob` date DEFAULT NULL,
  `insurance` varchar(20) DEFAULT 'N/A - CASH',
  `allergies` varchar(100) DEFAULT NULL,
  `upc_appt_date` date DEFAULT NULL,
  `upc_appt_doctor` int(3) DEFAULT NULL,
  `upc_appt_dept` int(3) DEFAULT NULL,
  `rec_appt_date` date DEFAULT NULL,
  `rec_appt_doctor` int(3) DEFAULT NULL,
  `rec_appt_dept` int(3) DEFAULT NULL,
  PRIMARY KEY (`ptID`),
  UNIQUE KEY `govtid` (`govtid`)
);

INSERT INTO `patients` VALUES (1,'Rehan Hanif',2147483647,'2001-01-28','Bupa - GOLD','computer science',NULL,NULL,NULL,'0000-00-00',3,1),(2,'Najad Ahmed',52618,'2003-04-13','Tawuniya-SILVER','library club',NULL,NULL,NULL,NULL,NULL,NULL),(4,'Edmund Hillary',500,'1900-05-12','ARAMCO-GOLD','autism',NULL,NULL,NULL,NULL,NULL,NULL),(5,'Shayan Najib',223283412,'2006-10-04','tawuniya-gold','math','2024-12-12',2,2,NULL,NULL,NULL),(6,'hmza',53622,'2000-11-11','golf','farhan',NULL,NULL,NULL,NULL,NULL,NULL),(7,'Mustafa',22418344,'2011-02-23','N/A - CASH','having a functional brain, having a heart',NULL,NULL,NULL,NULL,NULL,NULL),(8,'Abu John',9823,'1999-12-12','NONE','His son',NULL,NULL,NULL,NULL,NULL,NULL),(9,'Abu Johns Son',21123,'2021-09-09','gold','His father','2024-03-23',3,1,NULL,NULL,NULL),(10,'Mohammad Abu Usama',984344,'2000-04-23','Bronze','none',NULL,NULL,NULL,NULL,NULL,NULL),(11,'Roco',53466,'2000-11-11','Bronze','Water','2024-11-11',3,1,NULL,NULL,NULL),(12,'Rehan Veeran',23432332,'2021-12-13','None','Cat',NULL,NULL,NULL,'0000-00-00',2,2),(13,'Ahmed',98769,'2002-12-15','none','none',NULL,NULL,NULL,'0000-00-00',4,3);



CREATE TABLE `ptmedhis` (
  `id` int(5) NOT NULL,
  `ptid` int(5) NOT NULL,
  `medicine` varchar(100) DEFAULT NULL,
  `diagnosis` varchar(100) NOT NULL,
  `appt_date` date NOT NULL,
  `doctor` int(3) DEFAULT NULL,
  `vital_signs` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
);


CREATE TABLE `users` (
  `username` varchar(20) NOT NULL,
  `pwd` varchar(20) NOT NULL,
  `access` varchar(100) DEFAULT NULL,
  `name` varchar(30) DEFAULT NULL,
  `linked` int(11) DEFAULT NULL,
  PRIMARY KEY (`username`)
);


INSERT INTO `users` VALUES ('aisha','123','nurse','Aisha',NULL),('chad','123','nurse','Chad Prakash',2),('ducktor','123','doctor','Ducktor',3),('hom','123','nurse','Homie',NULL),('lol','123','pharma,doctor,emergency','Christina',1),('najad','najad123','nurse','najad',5),('nihaal','123','doctor','Nihaal',5),('phil','123','doctor','Phil',2),('pranav','admin123','reception','Praveer',NULL),('sophia','123','nurse','Sophia',3),('test','admin','\"admin,nurse,doctor,emergency,pharma,reception\"','Monkey Man',NULL),('wahid2024','1234','doctor','Wahid',4);

