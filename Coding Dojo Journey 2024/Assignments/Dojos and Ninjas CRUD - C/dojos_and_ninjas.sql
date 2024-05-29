-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: dojos_and_ninjas.db
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `dojos`
--

DROP TABLE IF EXISTS `dojos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dojos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dojos`
--

LOCK TABLES `dojos` WRITE;
/*!40000 ALTER TABLE `dojos` DISABLE KEYS */;
INSERT INTO `dojos` VALUES (4,'London','2024-03-06 15:11:14','2024-03-06 15:11:14'),(5,'Paris','2024-03-06 15:11:14','2024-03-06 15:11:14'),(6,'Dingle','2024-03-06 15:11:14','2024-03-06 15:11:14'),(9,'Austin','2024-03-24 10:46:25','2024-03-24 10:46:25'),(10,'Knoxville','2024-03-24 12:33:02','2024-03-24 12:33:02'),(13,'Nashville','2024-03-24 22:19:33','2024-03-24 22:19:33'),(14,'Denver','2024-03-24 22:25:15','2024-03-24 22:25:15');
/*!40000 ALTER TABLE `dojos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ninjas`
--

DROP TABLE IF EXISTS `ninjas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ninjas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `age` int NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `dojo_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_ninjas_dojos_idx` (`dojo_id`),
  CONSTRAINT `fk_ninjas_dojos` FOREIGN KEY (`dojo_id`) REFERENCES `dojos` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb3 COMMENT='	';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ninjas`
--

LOCK TABLES `ninjas` WRITE;
/*!40000 ALTER TABLE `ninjas` DISABLE KEYS */;
INSERT INTO `ninjas` VALUES (1,'Katie','Ayers',53,'2024-03-06 19:12:04','2024-03-06 19:12:04',4),(2,'Tom','Ayers',70,'2024-03-06 19:12:04','2024-03-06 19:12:04',4),(3,'Kay','Ayers',70,'2024-03-06 19:12:04','2024-03-06 19:12:04',4),(4,'Sue','Silva',70,'2024-03-06 19:16:08','2024-03-06 19:16:08',5),(5,'Mike','Silva',72,'2024-03-06 19:16:08','2024-03-06 19:16:08',5),(6,'Steven','Silva',36,'2024-03-06 19:16:08','2024-03-06 19:16:08',5),(7,'Michelle','VanSickle',36,'2024-03-06 19:16:08','2024-03-06 19:16:08',6),(8,'Brent','VanSickle',36,'2024-03-06 19:16:08','2024-03-06 19:16:08',6),(9,'Ashley','VanSickle',22,'2024-03-06 19:16:08','2024-03-06 19:16:08',6),(10,'Buttercup','Ayers',1,'2024-03-24 14:51:59','2024-03-24 14:51:59',9),(11,'Petunia','Ayers',1,'2024-03-24 16:17:44','2024-03-24 16:17:44',10),(12,'Apples','Ayers',1,'2024-03-24 17:58:34','2024-03-24 21:51:39',10),(13,'Sid','Ayers',1,'2024-03-24 22:20:09','2024-03-24 22:20:09',13),(14,'Leo','Ayers',19,'2024-03-24 22:27:03','2024-03-24 22:27:03',14);
/*!40000 ALTER TABLE `ninjas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-03-24 22:44:42
