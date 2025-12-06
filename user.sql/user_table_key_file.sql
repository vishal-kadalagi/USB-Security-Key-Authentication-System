
-- --------------------------------------------------------

--
-- Table structure for table `key_file`
--

DROP TABLE IF EXISTS `key_file`;
CREATE TABLE IF NOT EXISTS `key_file` (
  `dongle_key` varchar(20) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `key_file`
--

INSERT INTO `key_file` (`dongle_key`) VALUES
('ABCD');
