CREATE USER 'expressoft_admin'@'%' IDENTIFIED BY 'lewylzzvmA2023/';
GRANT ALTER, DELETE, INDEX, INSERT, SELECT, UPDATE, EXECUTE ON expressoft.* TO 'expressoft_admin'@'%';
FLUSH PRIVILEGES;