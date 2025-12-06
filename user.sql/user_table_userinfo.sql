
-- --------------------------------------------------------

--
-- Table structure for table `userinfo`
--

DROP TABLE IF EXISTS `userinfo`;
CREATE TABLE IF NOT EXISTS `userinfo` (
  `name` varchar(10) NOT NULL,
  `lastname` varchar(10) NOT NULL,
  `phoneno` varchar(10) NOT NULL,
  `emailid` varchar(40) DEFAULT NULL,
  `user_name` varchar(10) NOT NULL,
  `password` varchar(15) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `userinfo`
--

INSERT INTO `userinfo` (`name`, `lastname`, `phoneno`, `emailid`, `user_name`, `password`) VALUES
('Vishal', 'Kadalagi', '6360430056', 'vishalkadalagi2004@gmail.com', 'vish', '3455'),
('admin', 'admin', 'admin', 'admin', 'admin', 'admin'),
('Manojkumar', 'Patil', '7022820630', 'manojmp81977@gmail.com', 'manoj123', '8722'),
('shrishail', 'terni', '97877333', 'shrishaillterni00', 'shri0407', '4353');
