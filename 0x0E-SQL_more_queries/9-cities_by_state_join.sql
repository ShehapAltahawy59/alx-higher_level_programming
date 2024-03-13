-- Lists all cities in the database hbtn_0d_usa.
-- Records are sorted in order of ascending cities.id.
SELECT id name 
FROM cities 
INNER JOIN states 
ON cities.id = state_id 
ORDER BY cities.id;
