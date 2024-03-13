-- Lists all cities in the database hbtn_0d_usa.
-- Records are sorted in order of ascending cities.id.
SELECT c.id ,c.name ,s.name
FROM cities AS C 
INNER JOIN states AS s
ON c.id = s.id 
ORDER BY c.id;
