-- MySQL dump 10.13  Distrib 5.7.24, for osx11.1 (x86_64)
--
-- Host: localhost    Database: cooking_blog_database
-- ------------------------------------------------------
-- Server version	9.2.0

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add cuisine type',1,'add_cuisinetype'),(2,'Can change cuisine type',1,'change_cuisinetype'),(3,'Can delete cuisine type',1,'delete_cuisinetype'),(4,'Can view cuisine type',1,'view_cuisinetype'),(5,'Can add difficulty level',2,'add_difficultylevel'),(6,'Can change difficulty level',2,'change_difficultylevel'),(7,'Can delete difficulty level',2,'delete_difficultylevel'),(8,'Can view difficulty level',2,'view_difficultylevel'),(9,'Can add dish type',3,'add_dishtype'),(10,'Can change dish type',3,'change_dishtype'),(11,'Can delete dish type',3,'delete_dishtype'),(12,'Can view dish type',3,'view_dishtype'),(13,'Can add event type',4,'add_eventtype'),(14,'Can change event type',4,'change_eventtype'),(15,'Can delete event type',4,'delete_eventtype'),(16,'Can view event type',4,'view_eventtype'),(17,'Can add main ingredient',5,'add_mainingredient'),(18,'Can change main ingredient',5,'change_mainingredient'),(19,'Can delete main ingredient',5,'delete_mainingredient'),(20,'Can view main ingredient',5,'view_mainingredient'),(21,'Can add tag',6,'add_tag'),(22,'Can change tag',6,'change_tag'),(23,'Can delete tag',6,'delete_tag'),(24,'Can view tag',6,'view_tag'),(25,'Can add recipe',7,'add_recipe'),(26,'Can change recipe',7,'change_recipe'),(27,'Can delete recipe',7,'delete_recipe'),(28,'Can view recipe',7,'view_recipe'),(29,'Can add log entry',8,'add_logentry'),(30,'Can change log entry',8,'change_logentry'),(31,'Can delete log entry',8,'delete_logentry'),(32,'Can view log entry',8,'view_logentry'),(33,'Can add permission',9,'add_permission'),(34,'Can change permission',9,'change_permission'),(35,'Can delete permission',9,'delete_permission'),(36,'Can view permission',9,'view_permission'),(37,'Can add group',10,'add_group'),(38,'Can change group',10,'change_group'),(39,'Can delete group',10,'delete_group'),(40,'Can view group',10,'view_group'),(41,'Can add user',11,'add_user'),(42,'Can change user',11,'change_user'),(43,'Can delete user',11,'delete_user'),(44,'Can view user',11,'view_user'),(45,'Can add content type',12,'add_contenttype'),(46,'Can change content type',12,'change_contenttype'),(47,'Can delete content type',12,'delete_contenttype'),(48,'Can view content type',12,'view_contenttype'),(49,'Can add session',13,'add_session'),(50,'Can change session',13,'change_session'),(51,'Can delete session',13,'delete_session'),(52,'Can view session',13,'view_session'),(53,'Can add recipe image',14,'add_recipeimage'),(54,'Can change recipe image',14,'change_recipeimage'),(55,'Can delete recipe image',14,'delete_recipeimage'),(56,'Can view recipe image',14,'view_recipeimage'),(57,'Can add gallery image',15,'add_galleryimage'),(58,'Can change gallery image',15,'change_galleryimage'),(59,'Can delete gallery image',15,'delete_galleryimage'),(60,'Can view gallery image',15,'view_galleryimage'),(61,'Can add slide',16,'add_slide'),(62,'Can change slide',16,'change_slide'),(63,'Can delete slide',16,'delete_slide'),(64,'Can view slide',16,'view_slide'),(65,'Can add recipe ingredient',17,'add_recipeingredient'),(66,'Can change recipe ingredient',17,'change_recipeingredient'),(67,'Can delete recipe ingredient',17,'delete_recipeingredient'),(68,'Can view recipe ingredient',17,'view_recipeingredient');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$870000$VizVma58DYc0m4HxVV3vQw$fNlWfRRZOCsg4ffGv6gi11XJPk4erwuvtOW1oidrj9w=','2025-01-23 15:30:50.256350',1,'Meemz','','','meeriamzouein@gmail.com',1,1,'2025-01-23 15:28:13.970044');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb4_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=105 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2025-01-23 15:33:32.148962','1','Facile',1,'[{\"added\": {}}]',2,1),(2,'2025-01-23 15:33:44.095191','2','Intermédiaire',1,'[{\"added\": {}}]',2,1),(3,'2025-01-23 15:33:58.195100','3','Expert',1,'[{\"added\": {}}]',2,1),(4,'2025-01-23 15:34:46.207374','1','Entrées',1,'[{\"added\": {}}]',3,1),(5,'2025-01-23 15:35:03.842394','1','Entrées',3,'',3,1),(6,'2025-01-23 15:36:02.523166','2','Petits-Déjeuners',1,'[{\"added\": {}}]',3,1),(7,'2025-01-23 15:36:27.426261','3','Déjeuners & Dîners',1,'[{\"added\": {}}]',3,1),(8,'2025-01-23 15:36:43.054383','4','Desserts',1,'[{\"added\": {}}]',3,1),(9,'2025-01-23 15:36:56.188893','5','Aperos & Tapas',1,'[{\"added\": {}}]',3,1),(10,'2025-01-23 15:37:11.047121','1','Viande',1,'[{\"added\": {}}]',5,1),(11,'2025-01-23 15:37:17.048434','2','Poisson',1,'[{\"added\": {}}]',5,1),(12,'2025-01-23 15:37:19.214219','3','Poulet',1,'[{\"added\": {}}]',5,1),(13,'2025-01-23 15:37:43.642623','1','Française',1,'[{\"added\": {}}]',1,1),(14,'2025-01-23 15:37:51.531720','2','Italienne',1,'[{\"added\": {}}]',1,1),(15,'2025-01-23 15:37:56.054936','3','Asiatique',1,'[{\"added\": {}}]',1,1),(16,'2025-01-23 15:37:59.220752','4','Libanaise',1,'[{\"added\": {}}]',1,1),(17,'2025-01-23 15:38:06.002042','5','Végétarienne',1,'[{\"added\": {}}]',1,1),(18,'2025-01-23 15:38:11.884991','6','Vegan',1,'[{\"added\": {}}]',1,1),(19,'2025-01-23 15:38:25.997601','1','Repas de fête',1,'[{\"added\": {}}]',4,1),(20,'2025-01-23 15:38:36.109302','2','Cuisine rapide',1,'[{\"added\": {}}]',4,1),(21,'2025-01-23 15:39:05.468558','6','Barbecue',1,'[{\"added\": {}}]',3,1),(22,'2025-01-23 15:39:58.176183','1','En moins de 10 minutes',1,'[{\"added\": {}}]',6,1),(23,'2025-01-23 15:40:18.617407','2','Plat du moment',1,'[{\"added\": {}}]',6,1),(24,'2025-01-23 15:41:11.388158','1','Recette expert francaise de viande',1,'[{\"added\": {}}]',7,1),(25,'2025-01-23 16:04:24.808396','2','Barbecue de viande asiatique',1,'[{\"added\": {}}]',7,1),(26,'2025-01-23 16:04:35.083327','1','Recette expert francaise de viande',2,'[{\"changed\": {\"fields\": [\"Recipe Instructions\"]}}]',7,1),(27,'2025-01-23 16:05:27.061849','3','Dessert intermediaire de poulet à l\'italienne',1,'[{\"added\": {}}]',7,1),(28,'2025-01-23 17:11:29.412000','3','Dessert intermediaire de poulet à l\'italienne',2,'[{\"changed\": {\"fields\": [\"Recipe Image\"]}}]',7,1),(29,'2025-01-23 17:11:45.834917','2','Barbecue de viande asiatique',2,'[{\"changed\": {\"fields\": [\"Recipe Image\"]}}]',7,1),(30,'2025-01-23 17:11:56.232810','2','Barbecue de viande asiatique',2,'[]',7,1),(31,'2025-01-23 17:12:01.113762','1','Recette expert francaise de viande',2,'[{\"changed\": {\"fields\": [\"Recipe Image\"]}}]',7,1),(32,'2025-01-26 09:51:21.981128','3','Dessert intermediaire de poulet à l\'italienne',2,'[{\"changed\": {\"fields\": [\"Recipe Image\"]}}]',7,1),(33,'2025-01-26 14:05:23.975941','3','Dessert intermediaire de poulet à l\'italienne',2,'[{\"changed\": {\"fields\": [\"Recipe Image\", \"Recipe Instructions\"]}}]',7,1),(34,'2025-01-26 14:07:54.030765','3','Dessert intermediaire de poulet à l\'italienne',2,'[{\"changed\": {\"fields\": [\"Recipe Image\"]}}]',7,1),(35,'2025-01-26 14:09:13.612308','3','Dessert intermediaire de poulet à l\'italienne',2,'[{\"changed\": {\"fields\": [\"Recipe Image\"]}}]',7,1),(36,'2025-01-26 14:10:46.663246','3','Dessert intermediaire de poulet à l\'italienne',2,'[{\"changed\": {\"fields\": [\"Recipe Image\"]}}]',7,1),(37,'2025-01-26 14:13:07.278022','3','Dessert intermediaire de poulet à l\'italienne',2,'[{\"changed\": {\"fields\": [\"Recipe Image\"]}}]',7,1),(38,'2025-01-26 14:15:18.254088','3','Dessert intermediaire de poulet à l\'italienne',2,'[{\"changed\": {\"fields\": [\"Recipe Image\"]}}]',7,1),(39,'2025-01-26 14:22:58.951229','3','Dessert intermediaire de poulet à l\'italienne',2,'[{\"changed\": {\"fields\": [\"Recipe Image\"]}}]',7,1),(40,'2025-01-26 14:23:23.832437','3','Dessert intermediaire de poulet à l\'italienne',2,'[{\"changed\": {\"fields\": [\"Recipe Image\"]}}]',7,1),(41,'2025-01-26 14:27:31.907468','3','Dessert intermediaire de poulet à l\'italienne',2,'[{\"changed\": {\"fields\": [\"Recipe Image\"]}}]',7,1),(42,'2025-01-26 14:33:55.100636','3','Dessert intermediaire de poulet à l\'italienne',2,'[{\"changed\": {\"fields\": [\"Recipe Image\"]}}]',7,1),(43,'2025-01-26 14:34:31.473441','3','Dessert intermediaire de poulet à l\'italienne',2,'[{\"changed\": {\"fields\": [\"Recipe Image\"]}}]',7,1),(44,'2025-01-26 14:38:37.227184','3','Dessert intermediaire de poulet à l\'italienne',2,'[{\"changed\": {\"fields\": [\"Recipe Image\"]}}]',7,1),(45,'2025-01-26 17:01:29.833548','3','Dessert intermediaire de poulet à l\'italienne',2,'[{\"changed\": {\"fields\": [\"Recipe Image\"]}}]',7,1),(46,'2025-01-26 17:31:30.157494','3','Dessert intermediaire de poulet à l\'italienne',2,'[{\"changed\": {\"fields\": [\"Recipe Image\"]}}]',7,1),(47,'2025-01-26 17:34:20.695627','3','Dessert intermediaire de poulet à l\'italienne',2,'[{\"added\": {\"name\": \"recipe image\", \"object\": \"Image for Dessert intermediaire de poulet \\u00e0 l\'italienne\"}}]',7,1),(48,'2025-01-26 17:35:40.571208','3','Dessert intermediaire de poulet à l\'italienne',2,'[{\"changed\": {\"name\": \"recipe image\", \"object\": \"Image for Dessert intermediaire de poulet \\u00e0 l\'italienne\", \"fields\": [\"Recipe Gallery Image\"]}}]',7,1),(49,'2025-01-26 17:35:53.013183','3','Dessert intermediaire de poulet à l\'italienne',2,'[{\"changed\": {\"name\": \"recipe image\", \"object\": \"Image for Dessert intermediaire de poulet \\u00e0 l\'italienne\", \"fields\": [\"Alt\"]}}]',7,1),(50,'2025-01-26 17:36:13.512893','3','Dessert intermediaire de poulet à l\'italienne',2,'[{\"added\": {\"name\": \"recipe image\", \"object\": \"Image for Dessert intermediaire de poulet \\u00e0 l\'italienne\"}}]',7,1),(51,'2025-01-26 17:48:37.052457','3','Dessert intermediaire de poulet à l\'italienne',2,'[{\"added\": {\"name\": \"recipe image\", \"object\": \"Image for Dessert intermediaire de poulet \\u00e0 l\'italienne\"}}]',7,1),(52,'2025-01-26 17:49:37.315125','3','Dessert intermediaire de poulet à l\'italienne',2,'[{\"added\": {\"name\": \"recipe image\", \"object\": \"Image for Dessert intermediaire de poulet \\u00e0 l\'italienne\"}}]',7,1),(53,'2025-01-28 17:25:22.963260','6','Barbecue',2,'[{\"changed\": {\"fields\": [\"URL Slug\"]}}]',3,1),(54,'2025-01-28 17:25:33.622905','5','Aperos & Tapas',2,'[{\"changed\": {\"fields\": [\"URL Slug\"]}}]',3,1),(55,'2025-01-28 17:25:38.223255','4','Desserts',2,'[{\"changed\": {\"fields\": [\"URL Slug\"]}}]',3,1),(56,'2025-01-28 17:25:50.519648','3','Déjeuners & Dîners',2,'[{\"changed\": {\"fields\": [\"URL Slug\"]}}]',3,1),(57,'2025-01-28 17:25:56.627990','2','Petits-Déjeuners',2,'[{\"changed\": {\"fields\": [\"URL Slug\"]}}]',3,1),(58,'2025-01-28 17:27:19.087121','6','Barbecue',2,'[]',3,1),(59,'2025-01-29 17:11:01.024964','3','Dessert intermediaire de poulet à l\'italienne',2,'[{\"changed\": {\"fields\": [\"Recipe Image\"]}}]',7,1),(60,'2025-01-29 17:14:17.621511','2','Barbecue de viande asiatique',2,'[{\"changed\": {\"fields\": [\"Recipe Image\", \"Recipe Instructions\"]}}]',7,1),(61,'2025-01-29 17:14:24.404591','1','Recette expert francaise de viande',2,'[{\"changed\": {\"fields\": [\"Recipe Image\", \"Recipe Instructions\"]}}]',7,1),(62,'2025-01-30 17:25:46.129060','1','GalleryImage object (1)',1,'[{\"added\": {}}]',15,1),(63,'2025-01-30 17:25:52.329728','2','GalleryImage object (2)',1,'[{\"added\": {}}]',15,1),(64,'2025-01-30 17:25:57.049629','3','GalleryImage object (3)',1,'[{\"added\": {}}]',15,1),(65,'2025-01-30 17:26:03.005692','4','GalleryImage object (4)',1,'[{\"added\": {}}]',15,1),(66,'2025-01-30 17:26:10.097484','5','GalleryImage object (5)',1,'[{\"added\": {}}]',15,1),(67,'2025-01-30 17:26:15.980392','6','GalleryImage object (6)',1,'[{\"added\": {}}]',15,1),(68,'2025-01-30 17:26:22.174946','7','GalleryImage object (7)',1,'[{\"added\": {}}]',15,1),(69,'2025-01-30 17:26:30.243220','8','GalleryImage object (8)',1,'[{\"added\": {}}]',15,1),(70,'2025-01-31 16:01:38.314150','6','Barbecue',2,'[{\"changed\": {\"fields\": [\"Description\"]}}]',3,1),(71,'2025-01-31 16:01:42.069113','5','Aperos & Tapas',2,'[{\"changed\": {\"fields\": [\"Description\"]}}]',3,1),(72,'2025-01-31 16:01:44.765072','4','Desserts',2,'[{\"changed\": {\"fields\": [\"Description\"]}}]',3,1),(73,'2025-01-31 16:01:47.059973','4','Desserts',2,'[]',3,1),(74,'2025-01-31 16:01:49.702011','3','Déjeuners & Dîners',2,'[{\"changed\": {\"fields\": [\"Description\"]}}]',3,1),(75,'2025-01-31 16:01:52.074332','2','Petits-Déjeuners',2,'[{\"changed\": {\"fields\": [\"Description\"]}}]',3,1),(76,'2025-01-31 16:01:53.839166','4','Desserts',2,'[]',3,1),(77,'2025-01-31 16:02:32.297012','6','Barbecue',2,'[{\"changed\": {\"fields\": [\"Dish Type Image\"]}}]',3,1),(78,'2025-01-31 16:02:44.055540','5','Aperos & Tapas',2,'[{\"changed\": {\"fields\": [\"Dish Type Image\"]}}]',3,1),(79,'2025-01-31 16:02:50.150040','4','Desserts',2,'[{\"changed\": {\"fields\": [\"Dish Type Image\"]}}]',3,1),(80,'2025-01-31 16:03:10.487344','3','Déjeuners & Dîners',2,'[{\"changed\": {\"fields\": [\"Dish Type Image\"]}}]',3,1),(81,'2025-01-31 16:03:19.423480','2','Petits-Déjeuners',2,'[{\"changed\": {\"fields\": [\"Dish Type Image\"]}}]',3,1),(82,'2025-01-31 16:15:40.399251','1','Slider for Nos recettes originales de la cuisine du monde',1,'[{\"added\": {}}]',16,1),(83,'2025-01-31 16:18:35.746816','1','Slider for Nos recettes originales de la cuisine du monde',2,'[{\"changed\": {\"fields\": [\"Cta 2 link\"]}}]',16,1),(84,'2025-01-31 16:18:38.931246','1','Slider for Nos recettes originales de la cuisine du monde',2,'[{\"changed\": {\"fields\": [\"Cta 2 text\"]}}]',16,1),(85,'2025-01-31 16:18:42.838011','1','Slider for Nos recettes originales de la cuisine du monde',2,'[]',16,1),(86,'2025-01-31 16:21:41.289838','2','Slider for Représentez votre marque avec élégance',1,'[{\"added\": {}}]',16,1),(87,'2025-01-31 16:23:36.222792','3','Slider for Saveurs raffinées pour vos événements privés',1,'[{\"added\": {}}]',16,1),(88,'2025-01-31 16:38:52.453067','3','Slider for Saveurs raffinées pour vos événements privés',2,'[{\"changed\": {\"fields\": [\"Cta 2 link\"]}}]',16,1),(89,'2025-01-31 16:39:15.920930','3','Slider for Saveurs raffinées pour vos événements privés',2,'[{\"changed\": {\"fields\": [\"Cta 2 link\"]}}]',16,1),(90,'2025-01-31 21:05:16.853739','2','Barbecue de viande asiatique',2,'[{\"changed\": {\"fields\": [\"Dish Type\"]}}]',7,1),(91,'2025-02-01 07:19:49.649541','1','Recette expert francaise de viande',2,'[{\"changed\": {\"fields\": [\"Recipe Instructions\"]}}]',7,1),(92,'2025-02-01 07:20:24.822995','1','Recette expert francaise de viande',2,'[{\"changed\": {\"fields\": [\"Recipe Instructions\"]}}]',7,1),(93,'2025-02-01 07:20:49.339964','1','Recette expert francaise de viande',2,'[{\"changed\": {\"fields\": [\"Recipe Instructions\"]}}]',7,1),(94,'2025-02-01 07:22:40.671681','1','Recette expert francaise de viande',2,'[{\"changed\": {\"fields\": [\"Recipe Instructions\"]}}]',7,1),(95,'2025-02-01 07:25:28.357918','1','Recette expert francaise de viande',2,'[{\"changed\": {\"fields\": [\"Recipe Instructions\"]}}]',7,1),(96,'2025-02-01 07:27:05.754543','1','Recette expert francaise de viande',2,'[{\"changed\": {\"fields\": [\"Recipe Instructions\"]}}]',7,1),(97,'2025-02-01 07:28:51.151081','1','Recette expert francaise de viande',2,'[{\"changed\": {\"fields\": [\"Recipe Instructions\"]}}]',7,1),(98,'2025-02-01 07:50:06.507344','3','Dessert intermediaire de poulet à l\'italienne',2,'[{\"added\": {\"name\": \"recipe ingredient\", \"object\": \"dzdzzd\"}}, {\"added\": {\"name\": \"recipe ingredient\", \"object\": \"dzdzdz\"}}]',7,1),(99,'2025-02-01 07:54:25.031574','1','Recette expert francaise de viande',2,'[{\"added\": {\"name\": \"recipe ingredient\", \"object\": \"fefe\"}}, {\"added\": {\"name\": \"recipe ingredient\", \"object\": \"fefefe\"}}]',7,1),(100,'2025-02-01 08:01:18.036712','1','Recette expert francaise de viande',2,'[{\"changed\": {\"fields\": [\"Tags\"]}}]',7,1),(101,'2025-02-01 08:01:25.642777','1','Recette expert francaise de viande',2,'[{\"changed\": {\"fields\": [\"Tags\"]}}]',7,1),(102,'2025-02-01 08:04:17.803989','1','Recette expert francaise de viande',2,'[{\"changed\": {\"fields\": [\"Recipe Cover Picture\"]}}]',7,1),(103,'2025-02-02 11:35:11.783807','2','Barbecue de viande asiatique',2,'[{\"changed\": {\"fields\": [\"Recipe Cover Picture\"]}}]',7,1),(104,'2025-02-02 11:50:11.364156','2','Barbecue de viande asiatique',2,'[{\"changed\": {\"fields\": [\"YouTube Video\"]}}]',7,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (8,'admin','logentry'),(10,'auth','group'),(9,'auth','permission'),(11,'auth','user'),(12,'contenttypes','contenttype'),(1,'portfolio','cuisinetype'),(2,'portfolio','difficultylevel'),(3,'portfolio','dishtype'),(4,'portfolio','eventtype'),(15,'portfolio','galleryimage'),(5,'portfolio','mainingredient'),(7,'portfolio','recipe'),(14,'portfolio','recipeimage'),(17,'portfolio','recipeingredient'),(16,'portfolio','slide'),(6,'portfolio','tag'),(13,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2025-01-23 15:24:45.913059'),(2,'auth','0001_initial','2025-01-23 15:24:46.025364'),(3,'admin','0001_initial','2025-01-23 15:24:46.061594'),(4,'admin','0002_logentry_remove_auto_add','2025-01-23 15:24:46.065859'),(5,'admin','0003_logentry_add_action_flag_choices','2025-01-23 15:24:46.079012'),(6,'contenttypes','0002_remove_content_type_name','2025-01-23 15:24:46.103857'),(7,'auth','0002_alter_permission_name_max_length','2025-01-23 15:24:46.119009'),(8,'auth','0003_alter_user_email_max_length','2025-01-23 15:24:46.128153'),(9,'auth','0004_alter_user_username_opts','2025-01-23 15:24:46.131924'),(10,'auth','0005_alter_user_last_login_null','2025-01-23 15:24:46.145542'),(11,'auth','0006_require_contenttypes_0002','2025-01-23 15:24:46.146130'),(12,'auth','0007_alter_validators_add_error_messages','2025-01-23 15:24:46.149280'),(13,'auth','0008_alter_user_username_max_length','2025-01-23 15:24:46.165085'),(14,'auth','0009_alter_user_last_name_max_length','2025-01-23 15:24:46.180914'),(15,'auth','0010_alter_group_name_max_length','2025-01-23 15:24:46.187955'),(16,'auth','0011_update_proxy_permissions','2025-01-23 15:24:46.191388'),(17,'auth','0012_alter_user_first_name_max_length','2025-01-23 15:24:46.205859'),(18,'portfolio','0001_initial','2025-01-23 15:24:46.310838'),(19,'sessions','0001_initial','2025-01-23 15:24:46.316910'),(20,'portfolio','0002_recipe_video_url_alter_recipe_image','2025-01-26 09:49:44.959790'),(21,'portfolio','0003_recipeimage','2025-01-26 13:28:16.992220'),(22,'portfolio','0004_recipeimage_alt_alter_recipe_content','2025-01-26 13:43:54.213986'),(23,'portfolio','0005_alter_recipe_image','2025-01-26 17:29:27.482423'),(24,'portfolio','0006_rename_cuisine_type_recipe_cuisine_type_id_and_more','2025-01-28 16:40:33.237310'),(25,'portfolio','0007_dishtype_slug','2025-01-28 17:24:51.246836'),(26,'portfolio','0008_rename_cuisine_type_id_recipe_cuisine_type_and_more','2025-01-29 09:20:52.331150'),(27,'portfolio','0009_galleryimage','2025-01-30 17:24:55.462783'),(28,'portfolio','0010_slide_dishtype_description_dishtype_image','2025-01-31 16:00:35.778383'),(29,'portfolio','0011_slide_subtitle','2025-01-31 16:12:39.255534'),(30,'portfolio','0012_alter_slide_cta_1_link_alter_slide_cta_1_text_and_more','2025-01-31 16:16:33.778237'),(31,'portfolio','0013_alter_galleryimage_image_alter_recipe_image_and_more','2025-01-31 16:29:41.593012'),(32,'portfolio','0014_recipe_cover_picture_recipeingredient','2025-02-01 07:44:52.372382');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('j4qo4tgucc5symz3bll9n6xcmz5rt0b5','.eJxVjM0OwiAQhN-FsyFuFwh49O4zkF1-pGogKe3J-O7SpAc9znzfzFt42tbit54WP0dxESBOvx1TeKa6g_igem8ytLouM8tdkQft8tZiel0P9--gUC9jjRgJVc4qIiJA0M5MIzskPjtizEbxNCRAMJiUtpxJJwYbyIRglfh8AdJpN74:1tazAQ:fpzVq50bbwvm2Z9rQKHUnn2G6c04uWcHUMri8cSqUps','2025-02-06 15:30:50.265469');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `portfolio_cuisinetype`
--

DROP TABLE IF EXISTS `portfolio_cuisinetype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `portfolio_cuisinetype` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(80) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `portfolio_cuisinetype`
--

LOCK TABLES `portfolio_cuisinetype` WRITE;
/*!40000 ALTER TABLE `portfolio_cuisinetype` DISABLE KEYS */;
INSERT INTO `portfolio_cuisinetype` VALUES (1,'Française'),(2,'Italienne'),(3,'Asiatique'),(4,'Libanaise'),(5,'Végétarienne'),(6,'Vegan');
/*!40000 ALTER TABLE `portfolio_cuisinetype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `portfolio_difficultylevel`
--

DROP TABLE IF EXISTS `portfolio_difficultylevel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `portfolio_difficultylevel` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(80) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `portfolio_difficultylevel`
--

LOCK TABLES `portfolio_difficultylevel` WRITE;
/*!40000 ALTER TABLE `portfolio_difficultylevel` DISABLE KEYS */;
INSERT INTO `portfolio_difficultylevel` VALUES (1,'Facile'),(2,'Intermédiaire'),(3,'Expert');
/*!40000 ALTER TABLE `portfolio_difficultylevel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `portfolio_dishtype`
--

DROP TABLE IF EXISTS `portfolio_dishtype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `portfolio_dishtype` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(80) COLLATE utf8mb4_unicode_ci NOT NULL,
  `slug` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `description` longtext COLLATE utf8mb4_unicode_ci,
  `image` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `portfolio_dishtype`
--

LOCK TABLES `portfolio_dishtype` WRITE;
/*!40000 ALTER TABLE `portfolio_dishtype` DISABLE KEYS */;
INSERT INTO `portfolio_dishtype` VALUES (2,'Petits-Déjeuners','petits-dejeuners','Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.','dish_types/2.png'),(3,'Déjeuners & Dîners','dejeuners-et-diners','Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.','dish_types/2.png'),(4,'Desserts','desserts','Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.','dish_types/2.png'),(5,'Aperos & Tapas','aperos-et-tapas','Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.','dish_types/2.png'),(6,'Barbecue','barbecue','Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.','dish_types/2.png');
/*!40000 ALTER TABLE `portfolio_dishtype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `portfolio_eventtype`
--

DROP TABLE IF EXISTS `portfolio_eventtype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `portfolio_eventtype` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(80) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `portfolio_eventtype`
--

LOCK TABLES `portfolio_eventtype` WRITE;
/*!40000 ALTER TABLE `portfolio_eventtype` DISABLE KEYS */;
INSERT INTO `portfolio_eventtype` VALUES (1,'Repas de fête'),(2,'Cuisine rapide');
/*!40000 ALTER TABLE `portfolio_eventtype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `portfolio_galleryimage`
--

DROP TABLE IF EXISTS `portfolio_galleryimage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `portfolio_galleryimage` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `alt` varchar(150) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `image` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `uploaded_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `portfolio_galleryimage`
--

LOCK TABLES `portfolio_galleryimage` WRITE;
/*!40000 ALTER TABLE `portfolio_galleryimage` DISABLE KEYS */;
INSERT INTO `portfolio_galleryimage` VALUES (1,'1','1.jpg','2025-01-30 17:25:46.127026'),(2,'2','1.jpg','2025-01-30 17:25:52.328614'),(3,'3','1.jpg','2025-01-30 17:25:57.047633'),(4,'4','1.jpg','2025-01-30 17:26:03.004836'),(5,'5','1.jpg','2025-01-30 17:26:10.096390'),(6,'6','1.jpg','2025-01-30 17:26:15.979492'),(7,'7','1.jpg','2025-01-30 17:26:22.173988'),(8,'8','1.jpg','2025-01-30 17:26:30.241254');
/*!40000 ALTER TABLE `portfolio_galleryimage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `portfolio_mainingredient`
--

DROP TABLE IF EXISTS `portfolio_mainingredient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `portfolio_mainingredient` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(80) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `portfolio_mainingredient`
--

LOCK TABLES `portfolio_mainingredient` WRITE;
/*!40000 ALTER TABLE `portfolio_mainingredient` DISABLE KEYS */;
INSERT INTO `portfolio_mainingredient` VALUES (1,'Viande'),(2,'Poisson'),(3,'Poulet');
/*!40000 ALTER TABLE `portfolio_mainingredient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `portfolio_recipe`
--

DROP TABLE IF EXISTS `portfolio_recipe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `portfolio_recipe` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `excerpt` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `image` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `date` date NOT NULL,
  `slug` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `content` longtext COLLATE utf8mb4_unicode_ci,
  `cuisine_type_id` bigint NOT NULL,
  `difficulty_level_id` bigint NOT NULL,
  `dish_type_id` bigint NOT NULL,
  `event_type_id` bigint DEFAULT NULL,
  `main_ingredient_id` bigint NOT NULL,
  `video_url` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `cover_picture` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`),
  KEY `portfolio_recipe_cuisine_type_id_e9a59ee3_fk_portfolio` (`cuisine_type_id`),
  KEY `portfolio_recipe_difficulty_level_id_29a86aaf_fk_portfolio` (`difficulty_level_id`),
  KEY `portfolio_recipe_dish_type_id_82e627df_fk_portfolio_dishtype_id` (`dish_type_id`),
  KEY `portfolio_recipe_event_type_id_76ac3224_fk_portfolio` (`event_type_id`),
  KEY `portfolio_recipe_main_ingredient_id_f62ef5f4_fk_portfolio` (`main_ingredient_id`),
  CONSTRAINT `portfolio_recipe_cuisine_type_id_e9a59ee3_fk_portfolio` FOREIGN KEY (`cuisine_type_id`) REFERENCES `portfolio_cuisinetype` (`id`),
  CONSTRAINT `portfolio_recipe_difficulty_level_id_29a86aaf_fk_portfolio` FOREIGN KEY (`difficulty_level_id`) REFERENCES `portfolio_difficultylevel` (`id`),
  CONSTRAINT `portfolio_recipe_dish_type_id_82e627df_fk_portfolio_dishtype_id` FOREIGN KEY (`dish_type_id`) REFERENCES `portfolio_dishtype` (`id`),
  CONSTRAINT `portfolio_recipe_event_type_id_76ac3224_fk_portfolio` FOREIGN KEY (`event_type_id`) REFERENCES `portfolio_eventtype` (`id`),
  CONSTRAINT `portfolio_recipe_main_ingredient_id_f62ef5f4_fk_portfolio` FOREIGN KEY (`main_ingredient_id`) REFERENCES `portfolio_mainingredient` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `portfolio_recipe`
--

LOCK TABLES `portfolio_recipe` WRITE;
/*!40000 ALTER TABLE `portfolio_recipe` DISABLE KEYS */;
INSERT INTO `portfolio_recipe` VALUES (1,'Recette expert francaise de viande','Recette expert francaise de viande','4.jpg','2025-02-01','recette-expert-francaise-de-viande','<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio. Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio. Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.</p><p><strong>Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio. Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio. Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.</strong></p>',1,3,3,1,1,NULL,'recipe/4.jpg'),(2,'Barbecue de viande asiatique','Barbecue de viande asiatique','4.jpg','2025-02-02','barbecue-de-viande-asiatique','<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio. Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio. Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.</p>',3,1,4,1,1,'https://www.youtube.com/embed/lJIrF4YjHfQ?si=hBXaJkmC_Ryu2B17','recipe/2.jpg'),(3,'Dessert intermediaire de poulet à l\'italienne','Dessert de poulet à l\'italienne','4.jpg','2025-02-01','dessert-intermediaire-de-poulet-a-litalienne','<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio. Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio. Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.</p>',2,2,4,2,3,NULL,'');
/*!40000 ALTER TABLE `portfolio_recipe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `portfolio_recipe_tags`
--

DROP TABLE IF EXISTS `portfolio_recipe_tags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `portfolio_recipe_tags` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `recipe_id` bigint NOT NULL,
  `tag_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `portfolio_recipe_tags_recipe_id_tag_id_a191fba8_uniq` (`recipe_id`,`tag_id`),
  KEY `portfolio_recipe_tags_tag_id_a2899860_fk_portfolio_tag_id` (`tag_id`),
  CONSTRAINT `portfolio_recipe_tags_recipe_id_133a3dd8_fk_portfolio_recipe_id` FOREIGN KEY (`recipe_id`) REFERENCES `portfolio_recipe` (`id`),
  CONSTRAINT `portfolio_recipe_tags_tag_id_a2899860_fk_portfolio_tag_id` FOREIGN KEY (`tag_id`) REFERENCES `portfolio_tag` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `portfolio_recipe_tags`
--

LOCK TABLES `portfolio_recipe_tags` WRITE;
/*!40000 ALTER TABLE `portfolio_recipe_tags` DISABLE KEYS */;
INSERT INTO `portfolio_recipe_tags` VALUES (4,1,1),(5,1,2),(1,2,2),(2,3,1),(3,3,2);
/*!40000 ALTER TABLE `portfolio_recipe_tags` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `portfolio_recipeimage`
--

DROP TABLE IF EXISTS `portfolio_recipeimage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `portfolio_recipeimage` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `image` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `uploaded_at` datetime(6) NOT NULL,
  `recipe_id` bigint NOT NULL,
  `alt` varchar(150) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `portfolio_recipeimage_recipe_id_f8734c81_fk_portfolio_recipe_id` (`recipe_id`),
  CONSTRAINT `portfolio_recipeimage_recipe_id_f8734c81_fk_portfolio_recipe_id` FOREIGN KEY (`recipe_id`) REFERENCES `portfolio_recipe` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `portfolio_recipeimage`
--

LOCK TABLES `portfolio_recipeimage` WRITE;
/*!40000 ALTER TABLE `portfolio_recipeimage` DISABLE KEYS */;
INSERT INTO `portfolio_recipeimage` VALUES (1,'1_NRl95CtTxUi8Os7D_WKgAA.gif','2025-01-26 17:34:20.695062',3,'fezfzefze'),(2,'20180904_114319.jpg','2025-01-26 17:36:13.509777',3,'egre'),(3,'1_NRl95CtTxUi8Os7D_WKgAA.gif','2025-01-26 17:48:37.041302',3,NULL),(4,'1_NRl95CtTxUi8Os7D_WKgAA.gif','2025-01-26 17:49:37.309556',3,NULL);
/*!40000 ALTER TABLE `portfolio_recipeimage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `portfolio_recipeingredient`
--

DROP TABLE IF EXISTS `portfolio_recipeingredient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `portfolio_recipeingredient` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(80) COLLATE utf8mb4_unicode_ci NOT NULL,
  `recipe_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `portfolio_recipeingr_recipe_id_e05b091b_fk_portfolio` (`recipe_id`),
  CONSTRAINT `portfolio_recipeingr_recipe_id_e05b091b_fk_portfolio` FOREIGN KEY (`recipe_id`) REFERENCES `portfolio_recipe` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `portfolio_recipeingredient`
--

LOCK TABLES `portfolio_recipeingredient` WRITE;
/*!40000 ALTER TABLE `portfolio_recipeingredient` DISABLE KEYS */;
INSERT INTO `portfolio_recipeingredient` VALUES (1,'dzdzzd',3),(2,'dzdzdz',3),(3,'fefe',1),(4,'fefefe',1);
/*!40000 ALTER TABLE `portfolio_recipeingredient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `portfolio_slide`
--

DROP TABLE IF EXISTS `portfolio_slide`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `portfolio_slide` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `paragraph` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `cta_1_text` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `cta_1_link` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `cta_2_text` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `cta_2_link` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `image` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `alt` varchar(150) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `uploaded_at` datetime(6) NOT NULL,
  `subtitle` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `portfolio_slide`
--

LOCK TABLES `portfolio_slide` WRITE;
/*!40000 ALTER TABLE `portfolio_slide` DISABLE KEYS */;
INSERT INTO `portfolio_slide` VALUES (1,'Nos recettes originales de la cuisine du monde','Vous trouverez des recettes pour le petit déjeuner, déjeuner et le dîner.','Nos Recettes','recettes',NULL,NULL,'2.jpg',NULL,'2025-01-31 16:15:40.396915','Découvrez et Savourez'),(2,'Représentez votre marque avec élégance','Une expertise culinaire et une image soignée pour promouvoir vos produits.','Devis Gratuit',NULL,'Découvrir',NULL,'2.jpg',NULL,'2025-01-31 16:21:41.288784','Ambassadrice de Marque'),(3,'Saveurs raffinées pour vos événements privés','Organisez un dîner privé inoubliable avec un service sur-mesure.','Devis Gratuit',NULL,'Découvrir',NULL,'2.jpg',NULL,'2025-01-31 16:23:36.221653','Dîner privé et événements');
/*!40000 ALTER TABLE `portfolio_slide` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `portfolio_tag`
--

DROP TABLE IF EXISTS `portfolio_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `portfolio_tag` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `caption` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `portfolio_tag`
--

LOCK TABLES `portfolio_tag` WRITE;
/*!40000 ALTER TABLE `portfolio_tag` DISABLE KEYS */;
INSERT INTO `portfolio_tag` VALUES (1,'En moins de 10 minutes'),(2,'Plat du moment');
/*!40000 ALTER TABLE `portfolio_tag` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-02-11 23:21:17
