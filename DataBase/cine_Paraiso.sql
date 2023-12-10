-- MariaDB dump 10.19  Distrib 10.4.24-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: cine_paraiso
-- ------------------------------------------------------
-- Server version	10.4.24-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Temporary table structure for view `combos`
--

DROP TABLE IF EXISTS `combos`;
/*!50001 DROP VIEW IF EXISTS `combos`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `combos` (
  `idproducto` tinyint NOT NULL,
  `nombre` tinyint NOT NULL,
  `cantidad` tinyint NOT NULL,
  `idcomboproducto` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `detalle_funcion`
--

DROP TABLE IF EXISTS `detalle_funcion`;
/*!50001 DROP VIEW IF EXISTS `detalle_funcion`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `detalle_funcion` (
  `idfuncion` tinyint NOT NULL,
  `titulo` tinyint NOT NULL,
  `tipo` tinyint NOT NULL,
  `fecha` tinyint NOT NULL,
  `precio` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `detalle_ticket`
--

DROP TABLE IF EXISTS `detalle_ticket`;
/*!50001 DROP VIEW IF EXISTS `detalle_ticket`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `detalle_ticket` (
  `idtventa` tinyint NOT NULL,
  `titulo` tinyint NOT NULL,
  `tipo` tinyint NOT NULL,
  `asiento` tinyint NOT NULL,
  `fecha` tinyint NOT NULL,
  `precio` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `detalle_venta`
--

DROP TABLE IF EXISTS `detalle_venta`;
/*!50001 DROP VIEW IF EXISTS `detalle_venta`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `detalle_venta` (
  `idpventa` tinyint NOT NULL,
  `nombre` tinyint NOT NULL,
  `cantidad` tinyint NOT NULL,
  `precio` tinyint NOT NULL,
  `precio_producto` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `detalle_venta_ticket`
--

DROP TABLE IF EXISTS `detalle_venta_ticket`;
/*!50001 DROP VIEW IF EXISTS `detalle_venta_ticket`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `detalle_venta_ticket` (
  `idtventa` tinyint NOT NULL,
  `titulo` tinyint NOT NULL,
  `tipo` tinyint NOT NULL,
  `asiento` tinyint NOT NULL,
  `fecha` tinyint NOT NULL,
  `precio` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `empleado`
--

DROP TABLE IF EXISTS `empleado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `empleado` (
  `idempleado` int(11) NOT NULL,
  `rfc` varchar(13) DEFAULT NULL,
  `nombre` varchar(100) NOT NULL,
  `correo` varchar(80) DEFAULT NULL,
  `telefono` int(10) DEFAULT NULL,
  `direccion` varchar(40) NOT NULL,
  `cargo` char(3) DEFAULT NULL,
  `fecha_contratacion` date DEFAULT NULL,
  `fecha_baja` date DEFAULT NULL,
  PRIMARY KEY (`idempleado`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empleado`
--

LOCK TABLES `empleado` WRITE;
/*!40000 ALTER TABLE `empleado` DISABLE KEYS */;
/*!40000 ALTER TABLE `empleado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `funcion`
--

DROP TABLE IF EXISTS `funcion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `funcion` (
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `funcion`
--

LOCK TABLES `funcion` WRITE;
/*!40000 ALTER TABLE `funcion` DISABLE KEYS */;
/*!40000 ALTER TABLE `funcion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `membresia`
--

DROP TABLE IF EXISTS `membresia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `membresia` (
  `idmembresia` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `email` varchar(80) NOT NULL,
  `tipo` char(3) NOT NULL,
  `fecha_alta` date NOT NULL,
  `fecha_baja` date DEFAULT NULL,
  `Puntos` smallint(6) NOT NULL,
  PRIMARY KEY (`idmembresia`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `membresia`
--

LOCK TABLES `membresia` WRITE;
/*!40000 ALTER TABLE `membresia` DISABLE KEYS */;
/*!40000 ALTER TABLE `membresia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pelicula`
--

DROP TABLE IF EXISTS `pelicula`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pelicula` (
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pelicula`
--

LOCK TABLES `pelicula` WRITE;
/*!40000 ALTER TABLE `pelicula` DISABLE KEYS */;
/*!40000 ALTER TABLE `pelicula` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `producto`
--

DROP TABLE IF EXISTS `producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `producto` (
  `idproducto` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `precio` float NOT NULL,
  `stock` int(11) NOT NULL,
  PRIMARY KEY (`idproducto`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producto`
--

LOCK TABLES `producto` WRITE;
/*!40000 ALTER TABLE `producto` DISABLE KEYS */;
/*!40000 ALTER TABLE `producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productocombo`
--

DROP TABLE IF EXISTS `productocombo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `productocombo` (
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productocombo`
--

LOCK TABLES `productocombo` WRITE;
/*!40000 ALTER TABLE `productocombo` DISABLE KEYS */;
/*!40000 ALTER TABLE `productocombo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pventa`
--

DROP TABLE IF EXISTS `pventa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pventa` (
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pventa`
--

LOCK TABLES `pventa` WRITE;
/*!40000 ALTER TABLE `pventa` DISABLE KEYS */;
/*!40000 ALTER TABLE `pventa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pventaproducto`
--

DROP TABLE IF EXISTS `pventaproducto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pventaproducto` (
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pventaproducto`
--

LOCK TABLES `pventaproducto` WRITE;
/*!40000 ALTER TABLE `pventaproducto` DISABLE KEYS */;
/*!40000 ALTER TABLE `pventaproducto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sala`
--

DROP TABLE IF EXISTS `sala`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sala` (
  `idsala` int(11) NOT NULL,
  `tipo` char(3) NOT NULL,
  `mapa` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  PRIMARY KEY (`idsala`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sala`
--

LOCK TABLES `sala` WRITE;
/*!40000 ALTER TABLE `sala` DISABLE KEYS */;
/*!40000 ALTER TABLE `sala` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ticket`
--

DROP TABLE IF EXISTS `ticket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ticket` (
  `idticket` int(11) NOT NULL,
  `idfuncion` int(11) NOT NULL,
  `asiento` char(3) DEFAULT NULL,
  PRIMARY KEY (`idticket`),
  KEY `idfuncion` (`idfuncion`),
  CONSTRAINT `ticket_ibfk_1` FOREIGN KEY (`idfuncion`) REFERENCES `funcion` (`idfuncion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ticket`
--

LOCK TABLES `ticket` WRITE;
/*!40000 ALTER TABLE `ticket` DISABLE KEYS */;
/*!40000 ALTER TABLE `ticket` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tventa`
--

DROP TABLE IF EXISTS `tventa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tventa` (
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tventa`
--

LOCK TABLES `tventa` WRITE;
/*!40000 ALTER TABLE `tventa` DISABLE KEYS */;
/*!40000 ALTER TABLE `tventa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tventaticket`
--

DROP TABLE IF EXISTS `tventaticket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tventaticket` (
  `idtventaticket` int(11) NOT NULL,
  `idticket` int(11) NOT NULL,
  `idtventa` int(11) NOT NULL,
  PRIMARY KEY (`idtventaticket`),
  KEY `idticket` (`idticket`),
  KEY `idtventa` (`idtventa`),
  CONSTRAINT `tventaticket_ibfk_1` FOREIGN KEY (`idticket`) REFERENCES `ticket` (`idticket`),
  CONSTRAINT `tventaticket_ibfk_2` FOREIGN KEY (`idtventa`) REFERENCES `tventa` (`idtventa`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tventaticket`
--

LOCK TABLES `tventaticket` WRITE;
/*!40000 ALTER TABLE `tventaticket` DISABLE KEYS */;
/*!40000 ALTER TABLE `tventaticket` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `combos`
--

/*!50001 DROP TABLE IF EXISTS `combos`*/;
/*!50001 DROP VIEW IF EXISTS `combos`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `combos` AS select `producto`.`idproducto` AS `idproducto`,`producto`.`nombre` AS `nombre`,`productocombo`.`cantidad` AS `cantidad`,`productocombo`.`idcomboproducto` AS `idcomboproducto` from (`producto` join `productocombo`) where `producto`.`idproducto` = `productocombo`.`idproducto` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `detalle_funcion`
--

/*!50001 DROP TABLE IF EXISTS `detalle_funcion`*/;
/*!50001 DROP VIEW IF EXISTS `detalle_funcion`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `detalle_funcion` AS select `funcion`.`idfuncion` AS `idfuncion`,`pelicula`.`titulo` AS `titulo`,`sala`.`tipo` AS `tipo`,`funcion`.`fecha` AS `fecha`,`funcion`.`precio` AS `precio` from ((`pelicula` join `sala`) join `funcion`) where `funcion`.`idpelicula` = `pelicula`.`idpelicula` and `funcion`.`idsala` = `sala`.`idsala` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `detalle_ticket`
--

/*!50001 DROP TABLE IF EXISTS `detalle_ticket`*/;
/*!50001 DROP VIEW IF EXISTS `detalle_ticket`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `detalle_ticket` AS select `tventa`.`idtventa` AS `idtventa`,`pelicula`.`titulo` AS `titulo`,`sala`.`tipo` AS `tipo`,`ticket`.`asiento` AS `asiento`,`funcion`.`fecha` AS `fecha`,`funcion`.`precio` AS `precio` from (((((`pelicula` join `sala`) join `ticket`) join `funcion`) join `tventa`) join `tventaticket`) where `funcion`.`idpelicula` = `pelicula`.`idpelicula` and `funcion`.`idsala` = `sala`.`idsala` and `ticket`.`idticket` = `tventaticket`.`idticket` and `tventa`.`idtventa` = `tventaticket`.`idtventa` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `detalle_venta`
--

/*!50001 DROP TABLE IF EXISTS `detalle_venta`*/;
/*!50001 DROP VIEW IF EXISTS `detalle_venta`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `detalle_venta` AS select `pventa`.`idpventa` AS `idpventa`,`producto`.`nombre` AS `nombre`,`pventaproducto`.`cantidad` AS `cantidad`,`producto`.`precio` AS `precio`,`pventaproducto`.`precio_producto` AS `precio_producto` from ((`pventa` join `producto`) join `pventaproducto`) where `pventa`.`idpventa` = `pventaproducto`.`idventa` and `producto`.`idproducto` = `pventaproducto`.`idproducto` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `detalle_venta_ticket`
--

/*!50001 DROP TABLE IF EXISTS `detalle_venta_ticket`*/;
/*!50001 DROP VIEW IF EXISTS `detalle_venta_ticket`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `detalle_venta_ticket` AS select `tventa`.`idtventa` AS `idtventa`,`pelicula`.`titulo` AS `titulo`,`sala`.`tipo` AS `tipo`,`ticket`.`asiento` AS `asiento`,`funcion`.`fecha` AS `fecha`,`funcion`.`precio` AS `precio` from (((((`pelicula` join `sala`) join `ticket`) join `funcion`) join `tventa`) join `tventaticket`) where `funcion`.`idfuncion` = `ticket`.`idfuncion` and `funcion`.`idpelicula` = `pelicula`.`idpelicula` and `funcion`.`idsala` = `sala`.`idsala` and `ticket`.`idticket` = `tventaticket`.`idticket` and `tventa`.`idtventa` = `tventaticket`.`idtventa` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-10 12:51:59
