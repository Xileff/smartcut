-- MySQL dump 10.13  Distrib 8.0.26, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: smartcut
-- ------------------------------------------------------
-- Server version	8.0.26-google

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `smartcut`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `smartcut` /*!40100 DEFAULT CHARACTER SET utf8 */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `smartcut`;

--
-- Table structure for table `appointments`
--

DROP TABLE IF EXISTS `appointments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `appointments` (
  `id` varchar(21) NOT NULL,
  `schedule` datetime NOT NULL,
  `is_finished` tinyint(1) NOT NULL,
  `is_canceled` tinyint(1) NOT NULL,
  `will_be_canceled` tinyint(1) NOT NULL,
  `date_canceled` datetime DEFAULT NULL,
  `barbershop_id` varchar(27) NOT NULL,
  `user_id` varchar(21) NOT NULL,
  `message` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `barbershop_id` (`barbershop_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `appointments_ibfk_1` FOREIGN KEY (`barbershop_id`) REFERENCES `barbershops` (`id`) ON DELETE CASCADE,
  CONSTRAINT `appointments_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `appointments`
--

LOCK TABLES `appointments` WRITE;
/*!40000 ALTER TABLE `appointments` DISABLE KEYS */;
INSERT INTO `appointments` VALUES ('app-9G6UGu9WHd6CffnN','2023-06-12 00:00:00',1,0,0,NULL,'barbershop-eJqG-UPbr2E_-Xip','user-s6Xo2yHN6JbuG6jG','Tolong bikin doi kagum'),('app-d_jq7NJe5m65RNJm','2023-06-11 00:00:00',1,0,0,NULL,'barbershop-ko55iWI5pIbw3uhl','user-s6Xo2yHN6JbuG6jG','Two block ya bang'),('app-h25dlkhxFEiUskf5','2023-06-10 00:00:00',1,0,0,NULL,'barbershop-RLb8_mdMt1R0-aR1','user-ZixecUQ9U7QUUZb7','Rapiin aja ya bang'),('app-jxBWJtUnxLoQ2Pn2','2023-06-10 00:00:00',1,0,0,NULL,'barbershop-RLb8_mdMt1R0-aR1','user-s6Xo2yHN6JbuG6jG','Om tolong dirapihin'),('app-mY1X18HY-ZlcjYLJ','2023-06-11 00:00:00',1,0,0,NULL,'barbershop-ko55iWI5pIbw3uhl','user-ZixecUQ9U7QUUZb7','Coba dibikin kece bang'),('app-PL-thlp4R86UGJue','2023-06-12 00:00:00',1,0,0,NULL,'barbershop-eJqG-UPbr2E_-Xip','user-ZixecUQ9U7QUUZb7','Dibikin tampan dan menawan bang'),('app-qfd4E9PvwcBP-L0I','2023-06-11 00:00:00',1,0,0,NULL,'barbershop-ko55iWI5pIbw3uhl','user-2DPOpNv1VRDT5JVE','Pompadour bang'),('app-WTeX5YOy5-C_5ghD','2023-06-10 00:00:00',1,0,0,NULL,'barbershop-RLb8_mdMt1R0-aR1','user-2DPOpNv1VRDT5JVE','Kak tolong dirapihin buat kuliah'),('app-yS7_3W0VwF-4cz4a','2023-06-12 00:00:00',1,0,0,NULL,'barbershop-eJqG-UPbr2E_-Xip','user-2DPOpNv1VRDT5JVE','Rapihin bang untuk interview kerja');
/*!40000 ALTER TABLE `appointments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `barbershops`
--

DROP TABLE IF EXISTS `barbershops`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `barbershops` (
  `id` varchar(27) NOT NULL,
  `name` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `picture` varchar(255) NOT NULL,
  `description` text NOT NULL,
  `latitude` decimal(10,8) NOT NULL,
  `longitude` decimal(11,8) NOT NULL,
  `user_id` varchar(21) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `barbershops_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `barbershops`
--

LOCK TABLES `barbershops` WRITE;
/*!40000 ALTER TABLE `barbershops` DISABLE KEYS */;
INSERT INTO `barbershops` VALUES ('barbershop-eJqG-UPbr2E_-Xip','Kings Barbershop','Jl. Duri Utara 1 No.1, RW.3, Duri Utara, Kec. Tambora, Kota Jakarta Barat, Daerah Khusus Ibukota Jakarta 11270','https://storage.googleapis.com/smartcut-backend-bucket/barbershop/pictures/barbershop-eJqG-UPbr2E_-Xip.jpg','We will make u as glorious as king after u have a cut here',-6.15402100,106.80705000,'user-ginfJbhm-nbk9DuL'),('barbershop-ko55iWI5pIbw3uhl','BOW BARBERSHOP','Jl. KH.Moh.Mansyur No.3, RW.5, Jemb. Lima, Kec. Tambora, Kota Jakarta Barat, Daerah Khusus Ibukota Jakarta 11250','https://storage.googleapis.com/smartcut-backend-bucket/barbershop/pictures/barbershop-ko55iWI5pIbw3uhl.jpg','We\'re a group of young barbers who are truly passionate about men\'s grooming & giving you the best experience every time.',-6.15015000,106.80743200,'user-vBmfMxyg5mN4Oj3N'),('barbershop-RLb8_mdMt1R0-aR1','The Men’s Barbershop','Jl. KH.Moh.Mansyur, RT.3/RW.8, Tanah Sereal, Kec. Tambora, Kota Jakarta Barat, Daerah Khusus Ibukota Jakarta 11270','https://storage.googleapis.com/smartcut-backend-bucket/barbershop/pictures/barbershop-RLb8_mdMt1R0-aR1.jpg','The Men’s Barbershop Jembatan 5 is a Barber shop located at Jl. KH.Moh.Mansyur, RT.3/RW.8, Tanah Sereal, Tambora, West Jakarta City, Jakarta  11270, ID. The business is listed under barber shop category. It has received 83 reviews with an average rating of 4.7 stars.',-6.15164500,106.80762700,'user-x3ZVceOO46noGG5l');
/*!40000 ALTER TABLE `barbershops` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `email_verification_codes`
--

DROP TABLE IF EXISTS `email_verification_codes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `email_verification_codes` (
  `code` varchar(8) NOT NULL,
  `created_at` datetime NOT NULL,
  `expired_time` datetime NOT NULL,
  `user_id` varchar(21) NOT NULL,
  PRIMARY KEY (`code`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `email_verification_codes_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `email_verification_codes`
--

LOCK TABLES `email_verification_codes` WRITE;
/*!40000 ALTER TABLE `email_verification_codes` DISABLE KEYS */;
/*!40000 ALTER TABLE `email_verification_codes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hairstyle_categories`
--

DROP TABLE IF EXISTS `hairstyle_categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hairstyle_categories` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hairstyle_categories`
--

LOCK TABLES `hairstyle_categories` WRITE;
/*!40000 ALTER TABLE `hairstyle_categories` DISABLE KEYS */;
INSERT INTO `hairstyle_categories` VALUES (1,'asian'),(2,'western');
/*!40000 ALTER TABLE `hairstyle_categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hairstyles`
--

DROP TABLE IF EXISTS `hairstyles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hairstyles` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `picture` varchar(255) DEFAULT NULL,
  `description` text NOT NULL,
  `category_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `category_id` (`category_id`),
  CONSTRAINT `hairstyles_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `hairstyle_categories` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=81 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hairstyles`
--

LOCK TABLES `hairstyles` WRITE;
/*!40000 ALTER TABLE `hairstyles` DISABLE KEYS */;
INSERT INTO `hairstyles` VALUES (40,'Cepak Mekar','cepmek.jpg','Cepmek atau cepak mekar baru-baru ini populer di platform TikTok berkat kreator bernama Alif. Gaya ini sebenarnya sudah lama ada tetapi dengan istilah yang berbeda-beda, mulai dari long fringe, long quiff, long trim haircut, hingga Morrisey.',1),(41,'Comma Hair','comma-hair.jpg','Terdengar unik, gaya potongan rambut comma hair rupanya memang model rambut pria yang membentuk poni seperti koma di depan. Dapat dikatakan, gaya rambut comma hair merupakan gaya rambut yang sederhana namun memikat. Pasalnya, model potongan rambut pendek pria ini menjadi andalan model rambut pria Korea Selatan.',1),(42,'Two Block','two-block.jpg','Two block haircut merupakan potongan di mana bagian sisi samping dan belakang rambut dipotong atau dicukur pendek, sementara rambut bagian atas panjang. Potongan ini memiliki kesamaan dengan yang sering disebut model undercut, namun rambut bagian atas dan bagian lain di model undercut memiliki gradasi yang lebih jelas.',1),(43,'Messy Medium','messy-medium.jpg','Selain bikin macho, gaya rambut berantakan disukai karena maintenance-nya yang mudah, dan hasilnya yang lebih bervolume dan bikin rambut lo terlihat tebal. Yang lo butuhin cuma pomade atau wax rambut yang sesuai dengan tipe rambut lo.',1),(44,'Long Layered','long-layered.jpg','Layer adalah potongan rambut bertingkat yang menyerupai tangga dengan bagian paling pendek berada di depan. Potongan layer sebahu ini populer di kalangan pria.',1),(45,'Textured Spiky','textured-spiky.jpg','Ciri khas gaya rambut spike adalah rambut yang mencuat acak ke arah atas. Agar tekstur rambut tampak lebih tegas dan lurus, kamu bisa mencatok rambut searah menuju atas.',1),(46,'Curtain','curtain.jpg','Curtain bangs adalah model poni belah tengah yang bentuknya seperti huruf V terbalik. Seperti namanya, model poni ini seperti bentuk tirai yang sedang terbuka. Hanya, bagian tengahnya lebih pendek dibandingkan bagian samping.',1),(47,'Brown Undercut','brown-undercut.jpg','Gaya rambut undercut adalah model yang memisahkan bagian atas rambut dengan bagian bawah dan samping. Biasanya, pada rambut bagian atas lebih panjang/tebal dibandingkan bagian samping maupun belakang',1),(48,'Almond Middle Part','almond-middle-part.jpg','Middle hair atau yang sering disebut juga dengan medium hair memang sedang jadi tren belakangan ini. Potongan middle hair ini bisa dibilang enggak terlalu pendek, tapi juga enggak terlalu panjang. Jadi, untukmu yang tidak terlalu suka rambut yang terlalu pendek atau panjang, bisa memilih potongan rambut ini.',1),(49,'Voluminous Top with Undercut','voluminous-top-with-undercut.jpg','Gaya rambut ini menampilkan kesan rambut yang lebih bervolume pada bagian atas dan rapi di sisi kiri dan kanan.',1),(50,'Short High Taper Fade','short-high-taper-fade.jpg','Gaya rambut taper fade tergolong potongan rambut klasik yang juga dikenal sebagai model long trim haircut. Seperti yang sudah disinggung di atas, taper fade menggabungkan model rambut taper dan fade, yang sebenarnya merujuk pada model rambut yang cukup berbeda.',1),(51,'Asian Pompadour','asian-pompadour.jpg','Pompadour adalah gaya rambut jambul yang cukup populer di kalangan para pria. Karena memberikan kesan penampilan klasik, agar lebih modern bisa ditambah dengan Taper Fade, dengan begitu akan membuat jambul lebih terlihat rapi dan tampil stand out. Potong tipis bagian samping rambut hingga kebagian belakang rambut, bisa sampai terlihat kulit kepala ataupun 2-3cm bagi yang tidak suka terlihat kulit kepalanya.',1),(52,'Comb Over Bangs','comb-over-bangs.jpg','Gaya rambut comb over mungkin masuk dalam jajaran gaya rambut paling klasik di antara semua gaya rambut pria yang ada. Bahkan orangtua kita pun sering menyisirkan rambut kita dengan gaya belah pinggir. Gaya rambut ini kembali populer dan tifak eksklusif sebagai gaya rambut formal saja. Variasi gaya rambutnya semakin banyak dan modern.',1),(53,'Asian Slick Back','asian-slick-back.jpg','Slick back merupakan gaya rambut yang dipotong undercut, kemudian rambut bagian atas dibuat memanjang agar bisa disisir ke belakang. Slick back menonjolkan tampilan rambut yang disisir rapi ke belakang dengan tambahan produk penata rambut supaya lebih mengilap. ',1),(54,'Side Part','side-part.jpg','Side part merupakan gaya rambut dengan menyisir bagian atas kemudian diarahkan ke samping. Gaya ini sebenarnya cukup simpel, tetapi kamu perlu menyisakan rambut yang cukup panjang dengan bagian samping rambut bervolume tipis. \n\nUntuk membuatnya semakin rapi, gunakan produk wax dan gel, lalu sisir rambut ke salah satu sisinya. Banyak laki-laki Indonesia yang senang dengan potongan ini karena bisa memberikan kesan dewasa dan macho.',1),(55,'Fringe Up Medium','fringe-up.jpg','Fringe haircut adalah gaya rambut berponi juga. Bedanya dengan curtain haircut adalah cara penataannya. Kalau curtain haircut punya poni mirip tirai, maka fringe haircut bermain pada variasi poni. Karena bervariasi, fringe haircut bisa dikombinasikan dengan berbagai gaya rambut, mulai dari French crop, textured style, hingga bowl cut!',1),(56,'Super Classic','super-classic.jpg','Gaya rambut ini mirip seperti undercut. Potongan rambut bagian samping sengaja dipangkas lebih rapi untuk membentuk fitur wajah yang lebih oval. Kemudian bagian atasnya dibiarkan memanjang, tetapi dengan arah sisiran rambut ke atas agak ke samping dengan tambahan pomade untuk memberikan kesan fresh.',1),(57,'Mullet','mullet.jpg','Beda dengan classic mullet yang nggak ada gradasinya, versi modern mullet memberikan kesan modern karena punya transisi rambut dari panjang ke pendek, jadi cocok banget buat lo yang punya rambut tebal dan ngembang!',1),(58,'French Crop','french-crop.jpg','Kamu mungkin kerap menjumpai orang dengan potongan ini, tetapi belum mengerti nama modelnya. French crop merupakan model rambut laki-laki yang memiliki detail sangat pendek di bagian samping dan belakang kepala. \n\nSementara itu, bagian atas kepala dipotong cepak dan di-trim menyisakan poni yang tipis. Gaya ini sering juga disebut dengan potongan cepak ABRI di Indonesia. Kamu bisa memadukan model French crop dengan tekstur, layer, ataupun variasi lainnya supaya semakin keren.',1),(59,'Men\'s Bob','mens-bob.jpg','Tidak perlu ribet dalam menata model rambut gondrong pria rapi. Style rambut pria panjang ini bisa kamu tata dengan blow dry. Untuk acara formal, kamu bisa menatanya menjadi gaya rambut gondrong rapi, tapi untuk sehari-hari, kamu bisa coba style rambut gondrong yang lebih messy.',1),(60,'Bowl Cut','bowl-cut.jpg','Bowl cut menonjolkan tampilan rambut dengan bentuk model mangkok yang bisa memberikan kesan segar secara visual. Meski model rambut ini sempat populer di masa lalu, namun belakangan bowl cut kembali populer bahkan sampai diterapkan beberapa aktor Korea Selatan.',1),(61,'Afro','afro.jpg','Model rambut yang satu ini tidak hanya bisa ditujukan pada rambut lurus. Low fade pun bisa diterapkan pada pemilik rambut kribo. Caranya, potong rambut hingga tipis di bagian bawah kanan, kiri hingga belakang. Model rambut kribo low fade ini bisa membuat tampilanmu terlihat segar dan modern.',2),(62,'Brush Over','brush-over.jpg','Brush Over ialah model rambut yang cocok bagi Anda yang berambut agak panjang. \n\nBrush Over mirip dengan Brush Up, hanya saja yang ini disisir menyamping.\n\nBagian samping rambut dipotong sedikit pendek, sedang bagian tengahnya biasanya sepanjang 5 hingga 10 sentimeter.',2),(63,'Brush Up','brush-up.jpg','Brushed Up ialah model rambut yang cocok bagi Anda yang berambut agak panjang.\n\nBagian samping rambut dipotong sedikit pendek, sedang bagian tengahnya biasanya sepanjang 5 hingga 10 sentimeter.',2),(64,'Classic Crew Cut','classic-crew-cut.jpg','Crew cut adalah gaya rambut meruncing yang relatif sederhana, dengan bagian atas kepala dipotong pendek, dan yang lainnya lebih pendek. Ini bekerja dengan baik pada semua jenis bentuk wajah, itulah sebabnya kamu mungkin sering melihatnya dalam kehidupan sehari-hari.',2),(65,'Comb Over','comb-over.jpg','Gaya rambut comb over mungkin masuk dalam jajaran gaya rambut paling klasik di antara semua gaya rambut pria yang ada. Bahkan orangtua kita pun sering menyisirkan rambut kita dengan gaya belah pinggir. Gaya rambut ini kembali populer dan tifak eksklusif sebagai gaya rambut formal saja. Variasi gaya rambutnya semakin banyak dan modern.',2),(66,'Conventional Hipster','conventional-hipster.jpg','Gaya rambut ini adalah yang paling utama dan populer untuk kamu yang suka berpenampilan hipster. Gaya ini memiliki kesan kasual dan bebas, jika kamu rajin merawatnya kamu akan mendapatkan hasil yang memukau!\n\nDengan rambut seperti ini kamu masih tetap mendapatkan rambut yang bervolume yang dapat kamu rapikan menggunakan jari saja. Apalagi jika kamu pasangkan dengan jenggot yang rapi. Itu akan menjadi perpaduan yang sangat menarik. Yakinlah bahwa kamu akan selalu terlihat keren dengan gaya ini meskipun baru bangun tidur.',2),(67,'Dumpy Spikes','dumpy-spikes.jpg','Selain cepak dan undercut, gaya rambut spike jadi salah satu hairstyle universal yang tak pernah ketinggalan zaman. Sekilas, gaya rambut yang hits pada 2002 ini memang mirip dengan potongan mohawk.\n\nHanya saja, gaya rambut spike lebih disukai banyak pria karena sangat mudah dibuat. Yang dibutuhkan hanyalah pomade atau gel yang konsistensinya bisa disesuaikan dengan selera masing-masing.',2),(68,'Faux Hawk','faux-hawk.jpg','Gaya rambut yang cukup populer di kalangan cowok ini punya karakter potongan yang lebih soft dan modern dari mohawk. Selain itu, gaya rambut faux hawk ini cocok buat semua bentuk wajah dan hair texture.',2),(69,'High and Tide','high-and-tide.jpg','Gaya rambut high and tight adalah salah satu gaya rambut favorit di kalangan pria di dunia. Gaya ini cukup disenangi karena tampilannya yang anti ribet, cocok untuk situasi apapun, dan mudah untuk merawatnya.\n\nTidak perlu khawatir, model rambut high and tight juga cocok dipakai sepanjang masa. Gayanya yang simpel bisa membuat Anda tetap terlihat tampan meski sudah diterapkan bertahun-tahun. Tak heran gaya ini selalu menjadi andalan pria di dunia',2),(70,'Ivy League','ivy-league.jpg','Gaya rambut Ivy League atau Princeton Haircut adalah jenis potongan cepak. Model ini, rambut pria di bagian atas cukup panjang untuk dibelah dan disisir ke samping.\n\nGaya rambut ini direkomendasikan untuk pria yang ingin memberikan kesan cerdas sekaligus stylish. Gaya ini juga cukup populer karena memberikan banyak pilihan sehingga tidak membosankan atau bahkan menjadi tren.',2),(71,'Long Hairstyles','long-hairstyles.jpg','Rambut panjang adalah gaya rambut di mana rambut kepala dibiarkan tumbuh cukup panjang. Tepatnya apa yang dimaksud dengan rambut panjang dapat berubah dari budaya ke budaya, atau bahkan di dalam budaya.',2),(72,'Low Half Updo','low-half-updo.jpg','Lorem ipsum dolor sit amet',2),(73,'Middle Part With Low Fade Men','middle-part-with-low-fade-men.jpg','Undercut dengan mid fade atau medium fade punya konsep yang sama. Penipisan di bagian samping dengan efek fading alias memudar. Efek pudarnya dimulai dari middle atau tengah, sedikit naik dibanding low fade.',2),(74,'Mullet Hairstyle','mullet-hairstyle.jpg','Potongan rambut mullet cocok untuk rambut lurus maupun keriting atau ikal. Nah, pada pemilik rambut ikal, model mullet satu ini adalah pilihan yang tepat kamu pertimbangkan. Rambut dibuat lebih panjang di bagian belakang dan adanya sentuhan ikal. Hasilnya rambut lebih bervolume.',2),(75,'Pompadour','pompadour.jpg','Dulu, classic pompadour dihasilkan dengan menggunakan lemak hewani agar tetap licin. Nah, gaya rambut serba licin dan bervolume ini diadopsi oleh beberapa ikon populer seperti Elvis Presley, Everly Brothers, bahkan Conan O\'Brien!\nTapi, seperti apa sih gaya rambut pompadour? Style pompadour memiliki volume di bagian atas yang berbentuk seperti jambul. Banyak orang sering bingung membedakan gaya rambut ini dengan quiff, karena gaya jambulnya yang tampak sama.',2),(76,'Razored Shag','razored-shag.jpg','Potongan rambut shag terlihat modern, tajam dan indah, sekaligus menjadi solusi gaya yang mudah. Shags modern memvariasikan jumlah lapisan dan finishing untuk bagian tepinya. Setiap ketebalan dan panjang rambut memiliki gaya yang ideal.',2),(77,'Short Conservative','short-conservative.jpg','Model rambut short comb-over telah lama menjadi pilihan utama bagi kaum adam, karena terkesan lebih rapi. Penampilan ini sangat ideal untuk pria dengan rambut lurus yang sedikit dan mudah diatur.',2),(78,'Short Messy','short-messy.jpg','Model rambut messy hair adalah istilah untuk menyebut gaya rambut yang terkesan \'berantakan\', meski aslinya dibentuk dengan sengaja. Bukan masalah rambut yang kusut dan awut-awutan, melainkan gaya rambut messy yang keren!',2),(79,'Straight Texture','straight-texture.jpg','Sederhananya, potongan rambut lurus disebut potongan rambut tumpul karena dipotong tanpa menambahkan lapisan pada rambut Anda.',2),(80,'Textured Fringe','textured-fringe.jpg','Fringe haircut merupakan salah satu model rambut pria modern yang cukup populer. Ada beragam pilihan fringe haircut pria yang bisa bikin penampilan makin keren, mulai dari French crop, choppy crop hingga bowl cut. Tentunya, model rambut kekinian ini cocok untuk semua jenis rambut pria apa saja, mulai dari yang lurus, keriting, tebal atau pun tipis.',2);
/*!40000 ALTER TABLE `hairstyles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `id_cards`
--

DROP TABLE IF EXISTS `id_cards`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `id_cards` (
  `id` bigint NOT NULL,
  `picture` varchar(255) NOT NULL,
  `user_id` varchar(21) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `picture` (`picture`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `id_cards_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `id_cards`
--

LOCK TABLES `id_cards` WRITE;
/*!40000 ALTER TABLE `id_cards` DISABLE KEYS */;
INSERT INTO `id_cards` VALUES (3173317331733173,'https://storage.googleapis.com/smartcut-backend-bucket/user/id-card/user-x3ZVceOO46noGG5l.jpeg','user-x3ZVceOO46noGG5l'),(3174317431743174,'https://storage.googleapis.com/smartcut-backend-bucket/user/id-card/user-vBmfMxyg5mN4Oj3N.jpg','user-vBmfMxyg5mN4Oj3N'),(3175317531753175,'https://storage.googleapis.com/smartcut-backend-bucket/user/id-card/user-ginfJbhm-nbk9DuL.jpg','user-ginfJbhm-nbk9DuL');
/*!40000 ALTER TABLE `id_cards` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `predictions`
--

DROP TABLE IF EXISTS `predictions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `predictions` (
  `id` varchar(20) NOT NULL,
  `picture` varchar(255) NOT NULL,
  `compatibility` decimal(4,2) NOT NULL,
  `hairstyle_id` int NOT NULL,
  `user_id` varchar(21) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `hairstyle_id` (`hairstyle_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `predictions_ibfk_1` FOREIGN KEY (`hairstyle_id`) REFERENCES `hairstyles` (`id`) ON DELETE CASCADE,
  CONSTRAINT `predictions_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `predictions`
--

LOCK TABLES `predictions` WRITE;
/*!40000 ALTER TABLE `predictions` DISABLE KEYS */;
/*!40000 ALTER TABLE `predictions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reviews`
--

DROP TABLE IF EXISTS `reviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reviews` (
  `id` varchar(23) NOT NULL,
  `stars` int NOT NULL,
  `message` varchar(100) DEFAULT NULL,
  `appointment_id` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `appointment_id` (`appointment_id`),
  CONSTRAINT `reviews_ibfk_1` FOREIGN KEY (`appointment_id`) REFERENCES `appointments` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reviews`
--

LOCK TABLES `reviews` WRITE;
/*!40000 ALTER TABLE `reviews` DISABLE KEYS */;
INSERT INTO `reviews` VALUES ('7ZLDBNmiTJ_gYW03',4,'Boleh lah bang lumayan','app-qfd4E9PvwcBP-L0I'),('98llNjjry7Kq0VmZ',3,'Boleh lah bang lumayan','app-h25dlkhxFEiUskf5'),('aqkzM1MCpUqRlwbE',4,'Boleh lah bang lumayan','app-mY1X18HY-ZlcjYLJ'),('cfAvpcvGNwI7c4h9',5,'Boleh lah bang lumayan','app-jxBWJtUnxLoQ2Pn2'),('jmldSLA7HiivStvS',5,'Boleh lah bang lumayan','app-PL-thlp4R86UGJue'),('pW5Fp7_5lP0IOeRk',3,'Boleh lah bang lumayan','app-9G6UGu9WHd6CffnN'),('qAB3VVm3CW2LLnDy',5,'Boleh lah bang lumayan','app-WTeX5YOy5-C_5ghD'),('quVv4YBWoQZ1pjRh',3,'Boleh lah bang lumayan','app-yS7_3W0VwF-4cz4a'),('xvkk-yg8UzfbAzef',4,'Boleh lah bang lumayan','app-d_jq7NJe5m65RNJm');
/*!40000 ALTER TABLE `reviews` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` varchar(21) NOT NULL,
  `name` varchar(255) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(102) NOT NULL,
  `email` varchar(120) NOT NULL,
  `phone` bigint NOT NULL,
  `picture` varchar(255) DEFAULT NULL,
  `date_joined` datetime NOT NULL,
  `is_email_verified` tinyint(1) NOT NULL DEFAULT '0',
  `is_barber` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `phone` (`phone`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('user-0u4uM6McIYeLLBHj','Budi','Budi','pbkdf2:sha256:600000$Wirzsz2J7uZj89SN$dfc9041947a50f1c44e2f143971e5d548497fcc90b4e6b6ddde396cf82d58244','budi@gmail.com',621234567890,NULL,'2023-06-13 06:39:23',0,0),('user-2DPOpNv1VRDT5JVE','Feri Firmansah','ferifirmansah123','pbkdf2:sha256:600000$BrQu2vZzvtPGeDn0$1b88e56ac0733bade2b0ee4b0722f0700c64744bf44e3c0d21678e3aeb03be39','feri@gmail.com',6288909204321,NULL,'2023-06-12 03:18:27',0,0),('user-dVpaI-D0CHpnnAiX','Joe Momo','whoisjoe123','pbkdf2:sha256:600000$TRVcZ5AIanLu0yMa$2315c27105517cd7ad7ac14a5635b30ef805dda09da226c4e91cd61743cbc7e0','joemomo@gmail.com',6289880299507,'https://storage.googleapis.com/smartcut-backend-bucket/user/profile-picture/user-dVpaI-D0CHpnnAiX.jpg','2023-06-12 03:12:14',0,0),('user-gd8vSseoU5Xo9nmG','test7t','test7username','pbkdf2:sha256:600000$gADwl2KlvtZKKrY2$3ed1c78ba8e764c27b696df5ef8a25e764376c704c55cd007025b5b0e767d5ac','test7@gmail.com',62189888888888,NULL,'2023-06-12 08:07:56',0,0),('user-ginfJbhm-nbk9DuL','Nicholas Sky Salvatio','skysalvatio123','pbkdf2:sha256:600000$R302EAjzTy318tGX$0ea98214a7befe5df1e519fb6ca58f02b11b04ec8ae6278982d16db088c0a83e','sky@gmail.com',6288909201423,NULL,'2023-06-11 09:21:27',0,1),('user-HeyjtiBGK2P347QM','test2','test2','pbkdf2:sha256:600000$JVcfB1NU7ulGTxFf$37adb87d400e84473888b18119f4cedef2c43d4b7521f818b437549a100ea5db','test2@gmail.com',6288888888788,NULL,'2023-06-12 07:42:14',0,0),('user-PhEWYvqmcb7fKiIF','test1','test1','pbkdf2:sha256:600000$C2kSfrPDGKTDdmPv$9c5f50cbcefa1fc8f12375b4b727b66b77c77102807739325997a92dfd6fce34','test1@gmail.com',6288888888888,NULL,'2023-06-12 05:27:43',0,0),('user-s6Xo2yHN6JbuG6jG','Rafli Dwi Putra','raflidwi123','pbkdf2:sha256:600000$25Wu3CujETiWJxPY$83e531d7d49d785d007aea7afedafc51e6005a719b7337ed4508ca77407193d1','rafli@gmail.com',6288909203231,NULL,'2023-06-12 03:18:35',0,0),('user-v13nyTt66HJnT_ED','Xamarin','xamarin123','pbkdf2:sha256:600000$umcEcIa0pcQV3UW8$cec1c136ff957ef1525e8a6f95fb3f0b9733008e0639999b541503b2cc277d00','xamarin@gmail.com',6212356789123,NULL,'2023-06-12 08:08:29',0,0),('user-vBmfMxyg5mN4Oj3N','Farrell Liko Tanlimhuijaya','farrell12345','pbkdf2:sha256:600000$SO6yCgSKkGkvQPzQ$368ba0d6b80ea672daf6bfa65715368a73f90e6f6bf13e6b93de95fff12d5824','farrell@gmail.com',6288909201234,NULL,'2023-06-11 09:20:41',0,1),('user-WEOg0e81tc0NC3Qj','Felixaaaa','felixsavero2','pbkdf2:sha256:600000$AwPfPEO4nJCCGIE6$d273205e372ee6bee37e7d498ff88659e75490e9ffe52481d55a71427f4f0bc2','felixs@gmail.com',2222222222222,NULL,'2023-06-12 04:33:20',0,0),('user-x3ZVceOO46noGG5l','Felix Savero','felixsavero','pbkdf2:sha256:600000$8yuXgO7qZb8yFuzW$c6db5e98d12281beaba864fb7f2514764ed46b98cbae733722800bf220564928','felix@gmail.com',6288909201010,'https://storage.googleapis.com/smartcut-backend-bucket/user/profile-picture/user-x3ZVceOO46noGG5l.jpg','2023-06-11 09:09:29',0,1),('user-XylLryg14RBmu4kp','Felixaaaa','felixsavero12aaaa','pbkdf2:sha256:600000$7VrBah0usD2x71jq$c9e99f709aeba8e920cb479e14615b878a27698a36cbab95e5226d57b30c8d54','felixaaa@gmail.com',11111111111,NULL,'2023-06-11 11:04:48',0,0),('user-yWU6SYTWGVsDA46U','Ulala','ulala','pbkdf2:sha256:600000$lpJRSODISG76GBbZ$53d9d143174b4c8dab895a32e96689054ded5ea09ef54295b1673fb399a306e5','ulala@gmail.com',6286767676767,NULL,'2023-06-14 03:55:57',0,0),('user-ZixecUQ9U7QUUZb7','Rizki Aji Mahardika','rizkiaji123','pbkdf2:sha256:600000$sYL8YhRmGbbfKAfJ$d8b684b005faf1326ff3609790095fa7321e93129dd569be137cf91241e9bae5','rizkiaji@gmail.com',6288909204221,NULL,'2023-06-12 03:18:37',0,0);
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

-- Dump completed on 2023-06-14  7:30:13
