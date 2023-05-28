SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
-- -----------------------------------------------------
-- Schema library
-- mysql -uroot -proot27
-- source D:\Projects\bookworms\script.sql
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `library` DEFAULT CHARACTER SET utf8 ;
USE `library` ;
-- -----------------------------------------------------
-- Table `library`.`author`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `library`.`author` (
  `id_author` INT NOT NULL,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `borne` VARCHAR(45) NOT NULL,
  `died` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_author`))
ENGINE = InnoDB;
-- -----------------------------------------------------
-- Table `library`.`books`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `library`.`books` (
  `id` INT NOT NULL,
  `title` VARCHAR(45) NOT NULL,
  `text` LONGTEXT NOT NULL,
  `genre` VARCHAR(45) NOT NULL,
  `author_id` INT NOT NULL,
  PRIMARY KEY (`id`, `author_id`),
  INDEX `fk_books_author_idx` (`author_id` ASC) VISIBLE,
  CONSTRAINT `fk_books_author`
    FOREIGN KEY (`author_id`)
    REFERENCES `mydb`.`author` (`id_author`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;