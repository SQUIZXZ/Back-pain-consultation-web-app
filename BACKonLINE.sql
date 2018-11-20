CREATE TABLE `Clinitions` (
  `ID` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `clinitionID` INTEGER NOT NULL,
  `clinitionName` TEXT NOT NULL );

CREATE TABLE `Options` (
  `optionID` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `optionText` TEXT NOT NULL,
  `questionID` INTEGER ,
  `questionValue` INTEGER NOT NULL,
  FOREIGN KEY(`questionID`) REFERENCES Questions(`questionID`)
);

CREATE TABLE "Patients" (
  `patientID` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `ID` INTEGER NOT NULL,
  `patientName` TEXT NOT NULL );

CREATE TABLE `Questions` (
  `questionID` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `quetsion` TEXT NOT NULL,
  `sectionID` NUMERIC,
  FOREIGN KEY(`sectionID`) REFERENCES Sections(`sectionID`)
 );

CREATE TABLE "Results" (
  `resultID` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `patientID` INTEGER ,
  `questionID` INTEGER ,
  `optionID` INTEGER ,
  `optionValue` INTEGER NOT NULL,
  FOREIGN KEY(`questionID`) REFERENCES Questions(`questionID`),
  FOREIGN KEY(`patientID`) REFERENCES Patients(`patientID`),
  FOREIGN KEY(`optionID`) REFERENCES Options(`optionID`)
);

CREATE TABLE `Sections` (
  `sectionID` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `section` TEXT NOT NULL
);
