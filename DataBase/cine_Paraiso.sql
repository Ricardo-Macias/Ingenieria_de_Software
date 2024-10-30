-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.4.24-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for cine_paraiso
CREATE DATABASE IF NOT EXISTS `cine_paraiso` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `cine_paraiso`;

-- Dumping structure for view cine_paraiso.combos
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `combos` (
	`idproducto` INT(11) NOT NULL,
	`nombre` VARCHAR(100) NOT NULL COLLATE 'utf8_general_ci',
	`cantidad` INT(11) NOT NULL,
	`idcomboproducto` INT(11) NOT NULL
) ENGINE=MyISAM;

-- Dumping structure for view cine_paraiso.detalle_funcion
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `detalle_funcion` (
	`idfuncion` INT(11) NOT NULL,
	`titulo` VARCHAR(50) NOT NULL COLLATE 'utf8_general_ci',
	`tipo` CHAR(3) NOT NULL COLLATE 'utf8_general_ci',
	`fecha` DATETIME NOT NULL,
	`precio` FLOAT NOT NULL
) ENGINE=MyISAM;

-- Dumping structure for view cine_paraiso.detalle_ticket
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `detalle_ticket` (
	`idtventa` INT(11) NOT NULL,
	`titulo` VARCHAR(50) NOT NULL COLLATE 'utf8_general_ci',
	`tipo` CHAR(3) NOT NULL COLLATE 'utf8_general_ci',
	`asiento` CHAR(3) NULL COLLATE 'utf8_general_ci',
	`fecha` DATETIME NOT NULL,
	`precio` FLOAT NOT NULL
) ENGINE=MyISAM;

-- Dumping structure for view cine_paraiso.detalle_venta
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `detalle_venta` (
	`idpventa` INT(11) NOT NULL,
	`nombre` VARCHAR(100) NOT NULL COLLATE 'utf8_general_ci',
	`cantidad` INT(11) NOT NULL,
	`precio` FLOAT NOT NULL,
	`precio_producto` FLOAT NOT NULL
) ENGINE=MyISAM;

-- Dumping structure for view cine_paraiso.detalle_venta_ticket
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `detalle_venta_ticket` (
	`idtventa` INT(11) NOT NULL,
	`titulo` VARCHAR(50) NOT NULL COLLATE 'utf8_general_ci',
	`tipo` CHAR(3) NOT NULL COLLATE 'utf8_general_ci',
	`asiento` CHAR(3) NULL COLLATE 'utf8_general_ci',
	`fecha` DATETIME NOT NULL,
	`precio` FLOAT NOT NULL
) ENGINE=MyISAM;

-- Dumping structure for table cine_paraiso.empleado
CREATE TABLE IF NOT EXISTS `empleado` (
  `idempleado` int(11) NOT NULL,
  `rfc` varchar(13) DEFAULT NULL,
  `nombre` varchar(100) NOT NULL,
  `correo` varchar(80) DEFAULT NULL,
  `telefono` int(12) DEFAULT NULL,
  `direccion` varchar(40) NOT NULL,
  `cargo` char(3) DEFAULT NULL,
  `fecha_contratacion` date DEFAULT NULL,
  `fecha_baja` date DEFAULT NULL,
  PRIMARY KEY (`idempleado`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.

-- Dumping structure for table cine_paraiso.funcion
CREATE TABLE IF NOT EXISTS `funcion` (
  `idfuncion` int(11) NOT NULL,
  `idpelicula` int(11) NOT NULL,
  `idsala` int(11) NOT NULL,
  `fecha` datetime NOT NULL,
  `precio` float NOT NULL,
  PRIMARY KEY (`idfuncion`),
  KEY `idpelicula` (`idpelicula`),
  KEY `idsala` (`idsala`),
  CONSTRAINT `funcion_ibfk_1` FOREIGN KEY (`idpelicula`) REFERENCES `pelicula` (`idpelicula`),
  CONSTRAINT `funcion_ibfk_2` FOREIGN KEY (`idsala`) REFERENCES `sala` (`idsala`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.

-- Dumping structure for table cine_paraiso.membresia
CREATE TABLE IF NOT EXISTS `membresia` (
  `idmembresia` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `email` varchar(80) NOT NULL,
  `tipo` char(3) NOT NULL,
  `fecha_alta` date NOT NULL,
  `fecha_baja` date DEFAULT NULL,
  `Puntos` smallint(6) NOT NULL,
  PRIMARY KEY (`idmembresia`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.

-- Dumping structure for table cine_paraiso.pelicula
CREATE TABLE IF NOT EXISTS `pelicula` (
  `idpelicula` int(11) NOT NULL,
  `titulo` varchar(50) NOT NULL,
  `idioma` char(3) NOT NULL,
  `subtitulos` tinyint(1) DEFAULT 0,
  `sinopsis` varchar(280) NOT NULL,
  `reparto` varchar(280) NOT NULL,
  `poster` varchar(512) NOT NULL,
  `duracion` int(11) NOT NULL,
  `generos` varchar(100) NOT NULL,
  PRIMARY KEY (`idpelicula`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.

-- Dumping structure for table cine_paraiso.producto
CREATE TABLE IF NOT EXISTS `producto` (
  `idproducto` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `precio` float NOT NULL,
  `stock` int(11) NOT NULL,
  PRIMARY KEY (`idproducto`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.

-- Dumping structure for table cine_paraiso.productocombo
CREATE TABLE IF NOT EXISTS `productocombo` (
  `idproductocombo` int(11) NOT NULL,
  `idproducto` int(11) NOT NULL,
  `idcomboproducto` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL,
  PRIMARY KEY (`idproductocombo`),
  KEY `idproducto` (`idproducto`),
  KEY `idcomboproducto` (`idcomboproducto`),
  CONSTRAINT `productocombo_ibfk_1` FOREIGN KEY (`idproducto`) REFERENCES `producto` (`idproducto`),
  CONSTRAINT `productocombo_ibfk_2` FOREIGN KEY (`idcomboproducto`) REFERENCES `producto` (`idproducto`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.

-- Dumping structure for table cine_paraiso.pventa
CREATE TABLE IF NOT EXISTS `pventa` (
  `idpventa` int(11) NOT NULL,
  `idmembresia` int(11) NOT NULL,
  `idempleado` int(11) NOT NULL,
  `fecha` date DEFAULT NULL,
  PRIMARY KEY (`idpventa`),
  KEY `idmembresia` (`idmembresia`),
  KEY `idempleado` (`idempleado`),
  CONSTRAINT `pventa_ibfk_1` FOREIGN KEY (`idmembresia`) REFERENCES `membresia` (`idmembresia`),
  CONSTRAINT `pventa_ibfk_2` FOREIGN KEY (`idempleado`) REFERENCES `empleado` (`idempleado`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.

-- Dumping structure for table cine_paraiso.pventaproducto
CREATE TABLE IF NOT EXISTS `pventaproducto` (
  `idpventaproducto` int(11) NOT NULL,
  `idventa` int(11) NOT NULL,
  `idproducto` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `precio_producto` float NOT NULL,
  PRIMARY KEY (`idpventaproducto`),
  KEY `idventa` (`idventa`),
  KEY `idproducto` (`idproducto`),
  CONSTRAINT `pventaproducto_ibfk_1` FOREIGN KEY (`idventa`) REFERENCES `pventa` (`idpventa`),
  CONSTRAINT `pventaproducto_ibfk_2` FOREIGN KEY (`idproducto`) REFERENCES `producto` (`idproducto`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.

-- Dumping structure for table cine_paraiso.sala
CREATE TABLE IF NOT EXISTS `sala` (
  `idsala` int(11) NOT NULL,
  `tipo` char(3) NOT NULL,
  `mapa` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  PRIMARY KEY (`idsala`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.

-- Dumping structure for table cine_paraiso.ticket
CREATE TABLE IF NOT EXISTS `ticket` (
  `idticket` int(11) NOT NULL,
  `idfuncion` int(11) NOT NULL,
  `asiento` char(3) DEFAULT NULL,
  PRIMARY KEY (`idticket`),
  KEY `idfuncion` (`idfuncion`),
  CONSTRAINT `ticket_ibfk_1` FOREIGN KEY (`idfuncion`) REFERENCES `funcion` (`idfuncion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.

-- Dumping structure for table cine_paraiso.tventa
CREATE TABLE IF NOT EXISTS `tventa` (
  `idtventa` int(11) NOT NULL,
  `idmembresia` int(11) NOT NULL,
  `idempleado` int(11) NOT NULL,
  `fecha` date DEFAULT NULL,
  `cantidad` int(11) NOT NULL,
  `precio_funcion` float NOT NULL,
  PRIMARY KEY (`idtventa`),
  KEY `idmembresia` (`idmembresia`),
  KEY `idempleado` (`idempleado`),
  CONSTRAINT `tventa_ibfk_1` FOREIGN KEY (`idmembresia`) REFERENCES `membresia` (`idmembresia`),
  CONSTRAINT `tventa_ibfk_2` FOREIGN KEY (`idempleado`) REFERENCES `empleado` (`idempleado`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.

-- Dumping structure for table cine_paraiso.tventaticket
CREATE TABLE IF NOT EXISTS `tventaticket` (
  `idtventaticket` int(11) NOT NULL,
  `idticket` int(11) NOT NULL,
  `idtventa` int(11) NOT NULL,
  PRIMARY KEY (`idtventaticket`),
  KEY `idticket` (`idticket`),
  KEY `idtventa` (`idtventa`),
  CONSTRAINT `tventaticket_ibfk_1` FOREIGN KEY (`idticket`) REFERENCES `ticket` (`idticket`),
  CONSTRAINT `tventaticket_ibfk_2` FOREIGN KEY (`idtventa`) REFERENCES `tventa` (`idtventa`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.

-- Dumping structure for view cine_paraiso.combos
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `combos`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `combos` AS SELECT producto.idproducto, producto.nombre, productocombo.cantidad, productocombo.idcomboproducto
FROM producto, productocombo
WHERE producto.idproducto = productocombo.idproducto ;

-- Dumping structure for view cine_paraiso.detalle_funcion
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `detalle_funcion`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `detalle_funcion` AS SELECT funcion.idfuncion ,pelicula.titulo, sala.tipo, funcion.fecha, funcion.precio
FROM pelicula, sala, funcion
WHERE funcion.idpelicula = pelicula.idpelicula AND funcion.idsala = sala.idsala ;

-- Dumping structure for view cine_paraiso.detalle_ticket
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `detalle_ticket`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `detalle_ticket` AS SELECT tventa.idtventa ,pelicula.titulo, sala.tipo, ticket.asiento, funcion.fecha, funcion.precio
FROM pelicula, sala, ticket, funcion, tventa, tventaticket
WHERE funcion.idpelicula = pelicula.idpelicula AND funcion.idsala = sala.idsala AND ticket.idticket = tventaticket.idticket AND tventa.idtventa = tventaticket.idtventa ;

-- Dumping structure for view cine_paraiso.detalle_venta
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `detalle_venta`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `detalle_venta` AS select `pventa`.`idpventa` AS `idpventa`,`producto`.`nombre` AS `nombre`,`pventaproducto`.`cantidad` AS `cantidad`,`producto`.`precio` AS `precio`,`pventaproducto`.`precio_producto` AS `precio_producto` from ((`pventa` join `producto`) join `pventaproducto`) where `pventa`.`idpventa` = `pventaproducto`.`idventa` and `producto`.`idproducto` = `pventaproducto`.`idproducto` ;

-- Dumping structure for view cine_paraiso.detalle_venta_ticket
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `detalle_venta_ticket`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `detalle_venta_ticket` AS SELECT tventa.idtventa ,pelicula.titulo, sala.tipo, ticket.asiento, funcion.fecha, funcion.precio
FROM pelicula, sala, ticket, funcion, tventa, tventaticket
WHERE funcion.idfuncion = ticket.idfuncion  AND funcion.idpelicula = pelicula.idpelicula AND funcion.idsala = sala.idsala AND ticket.idticket = tventaticket.idticket AND tventa.idtventa = tventaticket.idtventa ;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
