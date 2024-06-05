CREATE TABLE `test888database`.`sport` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(45) NOT NULL,
  `Slug` VARCHAR(45) NOT NULL,
  `Active` TINYINT NULL,
  PRIMARY KEY (`ID`));


CREATE TABLE `test888database`.`event` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(45) NOT NULL,
  `Active` TINYINT NULL,
  `Slug` VARCHAR(45) NOT NULL,
  `Type` ENUM('PREPLAY', 'INPLAY') NOT NULL,
  `Status` ENUM('Pending', 'Started', 'Ended', 'Cancelled') NOT NULL,
  `start_time` DATETIME NOT NULL,
  `actual_start_time` DATETIME NULL,
  PRIMARY KEY (`ID`),
  CONSTRAINT `Sport`
    FOREIGN KEY (`ID`)
    REFERENCES `test888database`.`sport` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

CREATE TABLE `test888database`.`selection` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(45) NOT NULL,
  `Price` DECIMAL(2) NOT NULL,
  `Active` TINYINT NULL,
  `Outcome` ENUM('Unsettled', 'Void', 'Lose', 'Win') NOT NULL,
  PRIMARY KEY (`ID`),
  CONSTRAINT `Event`
    FOREIGN KEY (`ID`)
    REFERENCES `test888database`.`event` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);