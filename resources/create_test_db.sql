-- MySQL Workbench Forward Engineering
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
-- -----------------------------------------------------
-- Schema library
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `test_library` DEFAULT CHARACTER SET utf8 ;
USE `test_library` ;
-- -----------------------------------------------------
-- Table `test_library`.`author`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test_library`.`author` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `borne` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;
-- -----------------------------------------------------
-- Table `test_library`.`book`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test_library`.`book` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(45) NOT NULL,
  `text` LONGTEXT NOT NULL,
  `genre` VARCHAR(45) NOT NULL,
  `author_id` INT NOT NULL,
  PRIMARY KEY (`id`, `author_id`),
  INDEX `fk_books_author_idx` (`id` ASC) VISIBLE,
  CONSTRAINT `fk_books_author`
    FOREIGN KEY (`author_id`)
    REFERENCES `test_library`.`author` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
