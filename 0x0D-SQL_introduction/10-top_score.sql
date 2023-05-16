-- Lists all records of the table second_table of the database hbtn_0c_0 in mySQL server.
-- Results should display both the score and the name (in this order).
-- Records should be ordered by score (top first).
-- The database name will be passed as an argument of the mySQL command.


SELECT score, name FROM second_table ORDER BY score DESC;
