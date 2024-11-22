Network Monitoring System

This project is a simple network monitoring system built with Python and Flask. It continuously pings specific addresses (such as Google's DNS server or your local gateway), saves the results in an SQLite database, and displays the average, minimum, and maximum response times on a web-based dashboard.

Features:

Ping Monitoring: Periodically pings addresses to check network status.

SQLite Database: Stores ping results in an SQLite database.

Web Interface: A Flask web app that displays network statistics (average, min, max response times).
API: Exposes network statistics through a RESTful API.

Requirements -
To run the project, make sure you have the following dependencies installed:

*Python 3.x
*Flask
*ping3 (for pinging network addresses)
*SQLite (for database management)
