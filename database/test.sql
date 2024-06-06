drop database if exists test888database;
create database test888database;
use test888database;

CREATE TABLE `test888database`.`sport` (
  `ID` INT NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  `Slug` VARCHAR(45) NOT NULL,
  `Active` TINYINT NOT NULL,
  PRIMARY KEY (`ID`));

CREATE TABLE `test888database`.`event` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(45) NOT NULL,
  `Active` TINYINT NOT NULL,
  `Slug` VARCHAR(45) NOT NULL,
  `Type` ENUM('PREPLAY', 'INPLAY') NOT NULL,
  `Status` ENUM('Pending', 'Started', 'Ended', 'Cancelled') NOT NULL,
  `start_time` DATETIME NULL,
  `actual_start_time` DATETIME NULL,
  `sport_id` INT NOT NULL,
  PRIMARY KEY (`ID`),
  INDEX `sport_id_idx` (`sport_id` ASC) VISIBLE,
  CONSTRAINT `sport_id`
    FOREIGN KEY (`sport_id`)
    REFERENCES `test888database`.`sport` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

CREATE TABLE `test888database`.`selection` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(45) NOT NULL,
  `Price` INT NOT NULL,
  `Active` TINYINT NOT NULL,
  `Outcome` ENUM('Unsettled', 'Void', 'Lose', 'Win') NOT NULL,
  `event_id` INT NOT NULL,
  PRIMARY KEY (`ID`),
  INDEX `event_id_idx` (`event_id` ASC) VISIBLE,
  CONSTRAINT `event_id`
    FOREIGN KEY (`event_id`)
    REFERENCES `test888database`.`event` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

INSERT INTO `test888database`.`sport` (Name, Slug, Active) VALUES ('FOOTBALL', 'FOOTBALL', 1);
INSERT INTO `test888database`.`sport` (Name, Slug, Active) VALUES ('BASKETBALL', 'BASKETBALL', 1);
INSERT INTO `test888database`.`sport` (Name, Slug, Active) VALUES ('BASEBALL', 'BASEBALL', 1);
INSERT INTO `test888database`.`sport` (Name, Slug, Active) VALUES ('HOCKEY', 'HOCKEY', 1);

INSERT INTO `test888database`.`event` (Name, Active, Slug, Type, Status, start_time, actual_start_time, sport_id) VALUES ('FOOTBALL', 1,'FOOTBALL', 'INPLAY', 'PENDING', '2022-08-21 16:30:00', '2022-08-21 16:30:00', 1);
INSERT INTO `test888database`.`event` (Name, Active, Slug, Type, Status, start_time, actual_start_time, sport_id) VALUES ('BASKETBALL', 1,'BASKETBALL', 'INPLAY', 'PENDING', '2022-08-21 18:30:00', '2022-08-21 18:30:00', 2);

INSERT INTO `test888database`.`selection` (Name, Price, Active, Outcome, event_id) VALUES ('FOOTBALL', 2, 1, "Unsettled", 1);
INSERT INTO `test888database`.`selection` (Name, Price, Active, Outcome, event_id) VALUES ('BASKETBALL', 2, 1, "Unsettled", 2);