CREATE TABLE IF NOT EXISTS `workload` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `dados` LONGBLOB,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC))
ENGINE = InnoDB;