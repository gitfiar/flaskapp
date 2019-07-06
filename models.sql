-- MySQL dump 10.13  Distrib 5.7.26-ndb-7.6.10, for Linux (x86_64)
--
-- Host: localhost    Database: flask
-- ------------------------------------------------------
-- Server version	5.7.26-ndb-7.6.10

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
-- Table structure for table `Models`
--

DROP TABLE IF EXISTS `Models`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Models` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(80) DEFAULT NULL,
  `Data` varchar(256) NOT NULL,
  `Slgon` varchar(128) NOT NULL,
  `Video` varchar(128) NOT NULL,
  `Thumbnail` varchar(128) NOT NULL,
  `Pictures` varchar(256) NOT NULL,
  `Hometown` varchar(80) NOT NULL,
  `Job` varchar(80) NOT NULL,
  `Creatime` datetime NOT NULL,
  PRIMARY KEY (`Id`),
  UNIQUE KEY `Name` (`Name`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Models`
--

LOCK TABLES `Models` WRITE;
/*!40000 ALTER TABLE `Models` DISABLE KEYS */;
INSERT INTO `Models` VALUES (6,'林林','身高:165cm,上围:32C,体重:90kg,年龄:95','电视台外勤','IMG_0766.MP4','IMG_0769.JPG','IMG_0769.JPG|IMG_0768.JPG|IMG_0767.JPG|IMG_0765.JPG','湖南','红酒品酒职称','2019-06-26 05:38:11'),(7,'小敏','身高:164cm,上围:32C,体重:80kg,年龄:02','活好不黏人','IMG_0772.MP4','IMG_0770.JPG','IMG_0774.JPG|IMG_0773.JPG|IMG_0771.JPG|IMG_0770.JPG','粤语','高三','2019-06-26 05:40:21'),(8,'唐唐','身高:172cm,上围:34D,体重:102kg,年龄:96','身材火爆','IMG_0760.MOV','IMG_0757.JPG','IMG_0759.JPG|IMG_0758.JPG|IMG_0757.JPG','甘肃','未知','2019-06-26 05:42:10'),(10,'叶子','身高:172cm,上围:32B,体重:88kg,年龄:99','乖巧听话解锁各种姿势','IMG_0827.MP4','IMG_0824.JPG','IMG_0826.JPG|IMG_0825.JPG|IMG_0824.JPG|IMG_0823.JPG','粤语','学生','2019-06-28 20:27:21'),(11,'希希','身高:165cm,上围:32C,体重:90kg,年龄:02','高三在本地学生妹','IMG_0820.MP4','IMG_0819.JPG','IMG_0822.JPG|IMG_0821.JPG|IMG_0819.JPG|IMG_0818.JPG','粤语','学生','2019-06-28 20:31:00'),(12,'小娜','身高:164cm,上围:32C,体重:85kg,年龄:00','日式全套服务','IMG_0820.MP4','IMG_0811.JPG','IMG_0814.JPG|IMG_0813.JPG|IMG_0812.JPG|IMG_0811.JPG','广东','技校','2019-06-28 20:35:25'),(13,'晴子','身高:174cm,上围:32B,体重:100kg,年龄:02','零整容，初次兼职，无纹身不抽烟的好姑娘','IMG_0781.MP4','IMG_0803.JPG','IMG_0803.JPG|IMG_0782.PNG|IMG_0779.JPG|IMG_0777.JPG|IMG_0776.JPG','杭州','网红主播','2019-06-28 20:38:16'),(14,'轻轻','166，32D，98kg，02年','乖巧听话','IMG_0820.MP4','IMG_0821.JPG','IMG_0821.JPG|IMG_0819.JPG','广东','学生','2019-07-02 10:45:01');
/*!40000 ALTER TABLE `Models` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-07-03  2:07:15
