-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: login_and_registration
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
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `password` varchar(250) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Ringo','Ayers','ringoayers@gmail.com','$2b$12$BCNCmAkKZMDx97CkaFc6F.kfwXIA4HsNQKaVtYR9nvis7jgPtzLmC','2024-03-25 21:28:54','2024-03-25 21:28:54'),(2,'Ringo','Ayers','ringothedog@gmail.com','$2b$12$l5ymE6KESZPmlNOXSKNCBOsNEpq4qwqn8nswdJVEI4CVsL/8B/1XW','2024-03-25 21:33:52','2024-03-25 21:33:52'),(3,'Buttercup','Ayers','buttercupayers@gmail.com','$2b$12$tB8H.fJXJ5VyIQYpXkRmb.M2IBGQDM2pxRTrIBZcgInvagXzYQYtC','2024-03-25 21:50:23','2024-03-25 21:50:23'),(4,'Petunia','Ayers','petuniaayers@gmail.com','$2b$12$uHK4p4ZwKOgKcCdYdxA.Auma3Q2QWS/NQgw7.8gpflVTk675FFAJi','2024-03-25 21:56:22','2024-03-25 21:56:22'),(5,'Sid','Ayers','sidayers@gmail.com','$2b$12$SU/Rlbg250bFrJSVGPBf0.hd9ATXRBsyHmdYVzFo4Ga.sXmcGUqLC','2024-03-25 22:00:23','2024-03-25 22:00:23'),(6,'Apples','Ayers','applesayers@gmail.com','$2b$12$hqzQO.fmRqGVq2Mi.qcNxeq.MOFOzKDeE.8gllXzzYnrRe9dihlIC','2024-03-26 12:10:08','2024-03-26 12:10:08'),(7,'Leo','Ayers','leoayers@gmail.com','$2b$12$ZiEBhb5qBE83UAFeEeyiIeBveyFPskyy8pdZVFmHoDncofJnGNnsi','2024-03-26 12:33:15','2024-03-26 12:33:15');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-03-26 14:30:39
