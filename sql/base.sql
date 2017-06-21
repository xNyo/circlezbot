-- phpMyAdmin SQL Dump
-- version 4.6.6
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Creato il: Giu 21, 2017 alle 09:05
-- Versione del server: 10.1.24-MariaDB
-- Versione PHP: 7.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `circle`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `invited`
--

CREATE TABLE `invited` (
  `id` int(11) NOT NULL,
  `telegram_id` bigint(20) NOT NULL,
  `time` bigint(20) NOT NULL,
  `referral_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Struttura della tabella `latest_referral`
--

CREATE TABLE `latest_referral` (
  `latest_referral` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dump dei dati per la tabella `latest_referral`
--

INSERT INTO `latest_referral` (`latest_referral`) VALUES
(0);

-- --------------------------------------------------------

--
-- Struttura della tabella `referrals`
--

CREATE TABLE `referrals` (
  `id` int(11) NOT NULL,
  `referral` varchar(16) COLLATE utf8mb4_unicode_ci NOT NULL,
  `telegram_id` bigint(20) NOT NULL,
  `telegram_username` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `invited`
--
ALTER TABLE `invited`
  ADD PRIMARY KEY (`id`);

--
-- Indici per le tabelle `referrals`
--
ALTER TABLE `referrals`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `invited`
--
ALTER TABLE `invited`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT per la tabella `referrals`
--
ALTER TABLE `referrals`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
