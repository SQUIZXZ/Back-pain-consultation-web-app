BEGIN TRANSACTION;
DROP TABLE IF EXISTS `Sections`;
CREATE TABLE IF NOT EXISTS `Sections` (
	`sectionID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`section`	TEXT NOT NULL
);
INSERT INTO `Sections` (sectionID,section) VALUES (1,'Pain Behaviour');
INSERT INTO `Sections` (sectionID,section) VALUES (2,'Back pain and work');
INSERT INTO `Sections` (sectionID,section) VALUES (3,'Back pain and lifestyle');
DROP TABLE IF EXISTS `Results`;
CREATE TABLE IF NOT EXISTS `Results` (
	`resultID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`patientID`	INTEGER,
	`questionID`	INTEGER,
	`optionID`	TEXT NOT NULL,
	`textField`	TEXT,
	`optionValue`	TEXT NOT NULL,
	`form_id`	INTEGER NOT NULL,
	FOREIGN KEY(`form_id`) REFERENCES `FormSubmissions`(`id`),
	FOREIGN KEY(`patientID`) REFERENCES `Patients`(`patientID`),
	FOREIGN KEY(`questionID`) REFERENCES `Questions`(`questionID`)
);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (200,36,1,'1','','0',10);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (201,36,2,'4','','1',10);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (202,36,3,'12','dawfwag','0',10);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (203,36,4,'13','','0',10);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (204,36,5,'17,22,25','','1,1,1',10);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (205,36,6,'33','','0',10);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (207,36,7,'37,41,44','','1,1,1',10);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (208,36,8,'50','','0',10);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (209,36,9,'58,62','','1,1',10);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (210,36,10,'65','','1',10);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (211,36,11,'70','','2',10);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (212,36,12,'71','','0',10);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (213,36,13,'82','','0',10);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (214,36,14,'85','','0',10);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (215,36,15,'97','','0',10);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (216,36,16,'101','','0',10);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (217,36,17,'104','','1',10);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (218,36,18,'109','','0',10);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (219,36,19,'116,117','','1,1',10);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (220,36,20,'130','','1',10);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (221,36,21,'136','','0',10);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (222,36,22,'139','','1',10);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (223,36,23,'142','','1',10);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (224,36,24,'146','','2',10);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (225,36,25,'150','','1',10);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (226,36,26,'153','','0',10);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (227,36,27,'156','','0',10);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (228,36,28,'160','','1',10);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (229,36,29,'162','','2',10);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (230,36,30,'166','','1',10);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (231,36,31,'168','','2',10);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (232,36,32,'172','','1',10);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (233,36,33,'175','','1',10);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (234,36,34,'178','','1',10);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (235,36,35,'181','','1',10);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (236,36,36,'184','','1',10);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (237,36,37,'187','','1',10);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (238,36,38,'190','','1',10);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (239,36,39,'192','','2',10);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (240,42,1,'1','','0',12);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (241,42,2,'6','','0',12);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (242,43,1,'1','','0',14);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (243,43,2,'5','','0',14);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (244,43,3,'12','this is soe things','0',14);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (245,43,7,'37,38,40','','1,1,1',14);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (246,43,5,'32','','0',14);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (247,43,20,'130','','1',14);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (248,43,39,'192','','2',14);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (249,36,1,'1','','0',15);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (250,42,1,'1','','0',17);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (251,42,2,'11','','1',17);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (252,42,3,'12','jkjkj','0',17);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (253,42,4,'16','','NaN',17);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (254,43,1,'1','','0',18);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (255,43,2,'4','','1',18);
INSERT INTO `Results` (resultID,patientID,questionID,optionID,textField,optionValue,form_id) VALUES (256,43,1,'3','','1',19);
DROP TABLE IF EXISTS `Questions`;
CREATE TABLE IF NOT EXISTS `Questions` (
	`questionID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`question`	TEXT NOT NULL,
	`sectionID`	NUMERIC,
	`questionType`	TEXT,
	`maxScores`	INTEGER,
	FOREIGN KEY(`sectionID`) REFERENCES `Sections`(`sectionID`)
);
INSERT INTO `Questions` (questionID,question,sectionID,questionType,maxScores) VALUES (1,'Do you know what caused your back pain?',1,'1',2);
INSERT INTO `Questions` (questionID,question,sectionID,questionType,maxScores) VALUES (2,'If yes, choose an option from the list below:',1,'1',1);
INSERT INTO `Questions` (questionID,question,sectionID,questionType,maxScores) VALUES (3,'What do you think is wrong with your back?',1,'3',0);
INSERT INTO `Questions` (questionID,question,sectionID,questionType,maxScores) VALUES (4,'If you have been treated for back pain, were you satisfied with your treatment?',1,'1',2);
INSERT INTO `Questions` (questionID,question,sectionID,questionType,maxScores) VALUES (5,'What medication do you take to manage your back pain? ',1,'2',15);
INSERT INTO `Questions` (questionID,question,sectionID,questionType,maxScores) VALUES (6,'How effective is the medication in reducing your back pain?',1,'1',2);
INSERT INTO `Questions` (questionID,question,sectionID,questionType,maxScores) VALUES (7,'Where is your pain? Please tick all body areas that apply',1,'2',13);
INSERT INTO `Questions` (questionID,question,sectionID,questionType,maxScores) VALUES (8,'Is your pain there all the time?',1,'1',2);
INSERT INTO `Questions` (questionID,question,sectionID,questionType,maxScores) VALUES (9,'What type of pain is it? Please tick all options that apply ',1,'2',14);
INSERT INTO `Questions` (questionID,question,sectionID,questionType,maxScores) VALUES (10,'When is your pain at its worst? ',1,'1',2);
INSERT INTO `Questions` (questionID,question,sectionID,questionType,maxScores) VALUES (11,'Can you ease your back pain?',1,'1',2);
INSERT INTO `Questions` (questionID,question,sectionID,questionType,maxScores) VALUES (12,'How do you ease your back pain? Please tick all options that apply',1,'2',2);
INSERT INTO `Questions` (questionID,question,sectionID,questionType,maxScores) VALUES (13,'In general, is your back pain getting better, staying the same or getting worse?',1,'1',2);
INSERT INTO `Questions` (questionID,question,sectionID,questionType,maxScores) VALUES (14,'From the list below, please tick all the activities that make your pain worse. ',1,'2',2);
INSERT INTO `Questions` (questionID,question,sectionID,questionType,maxScores) VALUES (15,'From the list below, please tick all the activities that stop or decrease your pain.',1,'2',2);
INSERT INTO `Questions` (questionID,question,sectionID,questionType,maxScores) VALUES (16,'Is this the first time you have experienced this type of pain?',1,'1',2);
INSERT INTO `Questions` (questionID,question,sectionID,questionType,maxScores) VALUES (17,'If you had a previous episode of back pain, what helped in making your pain better? Please tick all options that apply',1,'2',3);
INSERT INTO `Questions` (questionID,question,sectionID,questionType,maxScores) VALUES (18,'Other than your back pain, do you experience other odd sensations in your back or legs (for example: crawling sensation, stinging, pressure) ',1,'1',2);
INSERT INTO `Questions` (questionID,question,sectionID,questionType,maxScores) VALUES (19,'Please tick all the areas where you experience this feeling:',1,'2',13);
INSERT INTO `Questions` (questionID,question,sectionID,questionType,maxScores) VALUES (20,'On average, how many hours do you sleep?',1,'4',2);
INSERT INTO `Questions` (questionID,question,sectionID,questionType,maxScores) VALUES (21,'Does your back pain wake you up every night?',1,'1',2);
INSERT INTO `Questions` (questionID,question,sectionID,questionType,maxScores) VALUES (22,'If you wake up with back pain, can you get back to sleep?',1,'1',2);
INSERT INTO `Questions` (questionID,question,sectionID,questionType,maxScores) VALUES (23,'How strongly do you agree with this statement : ‘I believe that my job caused /contributed to my back pain’ ',2,'1',2);
INSERT INTO `Questions` (questionID,question,sectionID,questionType,maxScores) VALUES (24,'Do you feel supported by your boss and/or co-workers?',2,'1',2);
INSERT INTO `Questions` (questionID,question,sectionID,questionType,maxScores) VALUES (25,'How is your back pain affecting your work?',2,'1',2);
INSERT INTO `Questions` (questionID,question,sectionID,questionType,maxScores) VALUES (26,'Are you off work right now because of your back pain?',2,'1',2);
INSERT INTO `Questions` (questionID,question,sectionID,questionType,maxScores) VALUES (27,'How long have you been off work?',2,'1',2);
INSERT INTO `Questions` (questionID,question,sectionID,questionType,maxScores) VALUES (28,'How likely it is that you would return to work within six months?',2,'1',2);
INSERT INTO `Questions` (questionID,question,sectionID,questionType,maxScores) VALUES (29,'‘I can’t do my normal daily activities because of my back pain’',3,'1',2);
INSERT INTO `Questions` (questionID,question,sectionID,questionType,maxScores) VALUES (30,'‘My back pain is negatively affecting my social life’',3,'1',2);
INSERT INTO `Questions` (questionID,question,sectionID,questionType,maxScores) VALUES (31,'‘My back pain is affecting my relationship with my significant other’',3,'1',2);
INSERT INTO `Questions` (questionID,question,sectionID,questionType,maxScores) VALUES (32,'‘I don’t know what makes my back pain worse or what eases it ‘',3,'1',2);
INSERT INTO `Questions` (questionID,question,sectionID,questionType,maxScores) VALUES (33,'‘My back pain makes me feel stressed/anxious’',3,'1',2);
INSERT INTO `Questions` (questionID,question,sectionID,questionType,maxScores) VALUES (34,'‘Stress increases my back pain’',3,'1',2);
INSERT INTO `Questions` (questionID,question,sectionID,questionType,maxScores) VALUES (35,'‘Physical activity increases my back pain’',3,'1',2);
INSERT INTO `Questions` (questionID,question,sectionID,questionType,maxScores) VALUES (36,'‘Since my back pain started, I feel more tired’',3,'1',2);
INSERT INTO `Questions` (questionID,question,sectionID,questionType,maxScores) VALUES (37,'‘I have lost interest and/or pleasure in doing things because of my back pain’',3,'1',2);
INSERT INTO `Questions` (questionID,question,sectionID,questionType,maxScores) VALUES (38,'‘I don’t think my family and friends understand what I’m going through with my back pain.’',3,'1',2);
INSERT INTO `Questions` (questionID,question,sectionID,questionType,maxScores) VALUES (39,'‘I don’t think my back pain will ever go away.’',3,'1',2);
DROP TABLE IF EXISTS `QuestionTypes`;
CREATE TABLE IF NOT EXISTS `QuestionTypes` (
	`typeID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`questionType`	TEXT NOT NULL
);
INSERT INTO `QuestionTypes` (typeID,questionType) VALUES (1,'Single-Answer');
INSERT INTO `QuestionTypes` (typeID,questionType) VALUES (2,'Multiple-Answer');
INSERT INTO `QuestionTypes` (typeID,questionType) VALUES (3,'Text-Field');
INSERT INTO `QuestionTypes` (typeID,questionType) VALUES (4,'Slider');
DROP TABLE IF EXISTS `Patients`;
CREATE TABLE IF NOT EXISTS `Patients` (
	`patientID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`patientName`	TEXT NOT NULL,
	`Password`	TEXT NOT NULL,
	`Email`	TEXT NOT NULL,
	`Gender`	TEXT,
	`Age`	INTEGER
);
INSERT INTO `Patients` (patientID,patientName,Password,Email,Gender,Age) VALUES (36,'anson','gurung','anson@gmail.com','Male',18);
INSERT INTO `Patients` (patientID,patientName,Password,Email,Gender,Age) VALUES (37,'fin','kklj','email@gmail.com','Error','Error');
INSERT INTO `Patients` (patientID,patientName,Password,Email,Gender,Age) VALUES (38,'aaron','dwd','wdwdwd@gmail.com','Female',12);
INSERT INTO `Patients` (patientID,patientName,Password,Email,Gender,Age) VALUES (39,'dad','password','mail@gmail.com','Male',12);
INSERT INTO `Patients` (patientID,patientName,Password,Email,Gender,Age) VALUES (40,'anson','gurung','email@gmail.com','Male',21);
INSERT INTO `Patients` (patientID,patientName,Password,Email,Gender,Age) VALUES (41,'Dave','mills','dave@gmail.com','Male',25);
INSERT INTO `Patients` (patientID,patientName,Password,Email,Gender,Age) VALUES (42,'Finlay','password','finlay@gmail.com','Male',19);
INSERT INTO `Patients` (patientID,patientName,Password,Email,Gender,Age) VALUES (43,'Fin','fin','fin@gmail.com','Male',19);
DROP TABLE IF EXISTS `Options`;
CREATE TABLE IF NOT EXISTS `Options` (
	`optionID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`optionText`	TEXT NOT NULL,
	`questionID`	INTEGER,
	`questionValue`	INTEGER NOT NULL,
	FOREIGN KEY(`questionID`) REFERENCES `Questions`(`questionID`)
);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (1,'Yes',1,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (2,'No',1,2);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (3,'Not Sure',1,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (4,'Car Accident',2,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (5,'Sport injury',2,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (6,'Lifting/bending accident',2,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (7,'Falling down',2,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (8,'Other Trauma',2,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (9,'Work related',2,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (10,'Other',2,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (11,'Nothing Specific',2,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (12,'Text Field',3,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (13,'Yes, I was satisfied with the treatment',4,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (14,'I was neither satisfied nor dissatisfied with the treatment',4,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (15,'No, I was not satisfied with the treatment',4,2);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (16,'I was never treated for back pain',4,'NaN');
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (17,'Paracetamol',5,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (18,'Ibuprofen',5,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (19,'Codeine',5,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (20,'Diazepam',5,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (21,'Amitriptyline',5,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (22,'Duloxetine/Cymbalta',5,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (23,'Gabapentin',5,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (24,'Tramadol',5,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (25,'Hydrocodone',5,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (26,'Cortisone',5,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (27,'Acetaminophen',5,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (28,'Glucosamine',5,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (29,'Valium',5,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (30,'Naproxen',5,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (31,'Other',5,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (32,'I don''t take any medication for my back pain',5,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (33,'Effective',6,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (34,'Not sure',6,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (35,'Ineffective',6,2);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (36,'Neck',7,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (37,'Right shoulder',7,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (38,'Left shoulder',7,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (39,'Right arm',7,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (40,'Left arm',7,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (41,'Upper back',7,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (42,'Lower back',7,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (43,'Right buttock',7,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (44,'Left buttock',7,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (45,'Right hip',7,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (46,'Left hip',7,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (47,'Right leg',7,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (48,'Left leg',7,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (49,'My pain is there all the time',8,2);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (50,'My pain comes and goes',8,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (51,'Not sure',8,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (52,'Deep',9,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (53,'Nagging',9,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (54,'Dull',9,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (55,'Sharp',9,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (56,'Shooting',9,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (57,'Dull ache',9,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (58,'Like lightning',9,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (59,'Burning',9,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (60,'Pressure',9,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (61,'Stinging',9,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (62,'Aching',9,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (63,'Throbbing',9,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (64,'Spread over a wide area',9,2);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (65,'in the morning',10,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (66,'at the end of the day',10,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (67,'My pain is there all day long',10,2);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (68,'Yes',11,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (69,'Sometimes',11,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (70,'No',11,2);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (71,'Medication/pain killers',12,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (72,'Rest',12,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (73,'Walking',12,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (74,'Standing',12,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (75,'Sitting',12,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (76,'Exercise',12,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (77,'Massage',12,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (78,'Hot pack',12,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (79,'Cold pack',12,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (80,'Other',12,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (81,'I am unable to ease my back pain',12,2);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (82,'My pain is getting better',13,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (83,'My pain has stayed the same',13,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (84,'My pain is getting worse',13,2);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (85,'Sitting relaxed',14,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (86,'Sitting up straight',14,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (87,'Standing',14,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (88,'Walking',14,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (89,'Lifting',14,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (90,'Forward bending',14,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (91,'Any activity that I do for a long period of time increases my back pain',14,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (92,'Everything I do causes me pain',14,2);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (93,'Walking',15,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (94,'Changing positions',15,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (95,'Sitting down',15,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (96,'Avoiding activities that causes me pain',15,2);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (97,'Stretching my back',15,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (98,'Moving about',15,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (99,'Painkillers',15,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (100,'Nothing I do stops my pain',15,2);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (101,'Yes',16,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (102,'No',16,2);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (103,'Not sure',16,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (104,'Medication/ painkillers/ injections',17,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (105,'Rest',17,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (106,'Exercise',17,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (107,'massage/ physiotherapy/ chiropractic/ osteopathy',17,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (108,'Nothing helped',17,2);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (109,'Yes',18,2);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (110,'No',18,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (111,'I don''t know',18,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (112,'Neck',19,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (113,'Right shoulder',19,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (114,'Left shoulder',19,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (115,'Right arm',19,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (116,'Left arm',19,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (117,'Upper back',19,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (118,'Lower back',19,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (119,'Right buttock',19,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (120,'Left buttock',19,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (121,'Right hip',19,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (122,'Left hip',19,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (123,'Right leg',19,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (124,'Left leg',19,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (125,'0',20,2);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (126,'1',20,2);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (127,'2',20,2);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (128,'3',20,2);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (129,'4',20,2);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (130,'5',20,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (131,'6',20,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (132,'7',20,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (133,'8',20,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (134,'9',20,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (135,'10',20,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (136,'Yes',21,2);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (137,'No',21,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (138,'Yes',22,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (139,'Sometimes',22,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (140,'No',22,2);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (141,'Agree',23,2);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (142,'Neither agree nor disagree',23,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (143,'Disagree',23,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (144,'I don''t work',23,'NaN');
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (145,'Yes',24,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (146,'No',24,2);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (147,'I don''t work',24,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (148,'Not applicable',24,'NaN');
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (149,'Not at all',25,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (150,'Sometimes',25,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (151,'Frequently',25,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (152,'I am unable to work because of my back pain',25,2);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (153,'Yes',26,2);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (154,'No',26,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (155,'I don''t work',26,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (156,'Less than 3 months',27,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (157,'Between 1 to 6 months',27,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (158,'More than 6 months',27,2);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (159,'Likely',28,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (160,'Not sure',28,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (161,'Unlikely',28,2);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (162,'agree',29,2);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (163,'neither agree nor disagree',29,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (164,'disagree',29,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (165,'agree',30,2);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (166,'neither agree nor disagree',30,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (167,'disagree',30,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (168,'agree',31,2);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (169,'neither agree nor disagree',31,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (170,'disagree',31,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (171,'agree',32,2);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (172,'neither agree nor disagree',32,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (173,'disagree',32,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (174,'agree',33,2);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (175,'neither agree nor disagree',33,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (176,'disagree',33,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (177,'agree',34,2);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (178,'neither agree nor disagree',34,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (179,'disagree',34,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (180,'agree',35,2);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (181,'neither agree nor disagree',35,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (182,'disagree',35,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (183,'agree',36,2);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (184,'neither agree nor disagree',36,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (185,'disagree',36,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (186,'agree',37,2);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (187,'neither agree nor disagree',37,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (188,'disagree',37,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (189,'agree',38,2);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (190,'neither agree nor disagree',38,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (191,'disagree',38,0);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (192,'agree',39,2);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (193,'neither agree nor disagree',39,1);
INSERT INTO `Options` (optionID,optionText,questionID,questionValue) VALUES (194,'disagree',39,0);
DROP TABLE IF EXISTS `FormSubmissions`;
CREATE TABLE IF NOT EXISTS `FormSubmissions` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`patientID`	INTEGER,
	`completed`	TEXT NOT NULL,
	`dateCreated`	TEXT NOT NULL,
	`dateSubmitted`	TEXT NOT NULL,
	`totalScores`	TEXT NOT NULL,
	FOREIGN KEY(`patientID`) REFERENCES `Patients`(`patientID`)
);
INSERT INTO `FormSubmissions` (id,patientID,completed,dateCreated,dateSubmitted,totalScores) VALUES (10,36,'True','11-12-2018,07:08:14:450973','10-12-2018,09:52:44:573196','36/123');
INSERT INTO `FormSubmissions` (id,patientID,completed,dateCreated,dateSubmitted,totalScores) VALUES (12,42,'False','11-12-2018,09:57:53:894442',' ',' ');
INSERT INTO `FormSubmissions` (id,patientID,completed,dateCreated,dateSubmitted,totalScores) VALUES (14,43,'True','11-12-2018,10:13:21:986440','11-12-2018,10:15:52:142936','6/35');
INSERT INTO `FormSubmissions` (id,patientID,completed,dateCreated,dateSubmitted,totalScores) VALUES (15,36,'False','11-12-2018,10:16:47:439577',' ',' ');
INSERT INTO `FormSubmissions` (id,patientID,completed,dateCreated,dateSubmitted,totalScores) VALUES (16,42,'False','11-12-2018,10:18:47:549350',' ',' ');
INSERT INTO `FormSubmissions` (id,patientID,completed,dateCreated,dateSubmitted,totalScores) VALUES (17,42,'False','11-12-2018,14:01:06:206351',' ',' ');
INSERT INTO `FormSubmissions` (id,patientID,completed,dateCreated,dateSubmitted,totalScores) VALUES (18,43,'False','11-12-2018,14:28:11:459281',' ',' ');
INSERT INTO `FormSubmissions` (id,patientID,completed,dateCreated,dateSubmitted,totalScores) VALUES (19,43,'False','11-12-2018,14:30:04:758830',' ',' ');
DROP TABLE IF EXISTS `Clinitions`;
CREATE TABLE IF NOT EXISTS `Clinitions` (
	`clinitionID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`clinitionName`	TEXT NOT NULL,
	`Password`	TEXT NOT NULL,
	`Email`	TEXT NOT NULL
);
INSERT INTO `Clinitions` (clinitionID,clinitionName,Password,Email) VALUES (1,'Dalal','password','Dalal@gmail.com');
INSERT INTO `Clinitions` (clinitionID,clinitionName,Password,Email) VALUES (2,'admin','admin','admin@gmail.com');
COMMIT;
