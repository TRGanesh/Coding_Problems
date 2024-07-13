/*
-->> Problem Statement:
Write a SQL query to convert the given input into the expected output as shown below:

-- INPUT:
SRC         DEST        DISTANCE
Bangalore	Hyderbad	400
Hyderbad	Bangalore	400
Mumbai	    Delhi	    400
Delhi	    Mumbai	    400
Chennai	    Pune	    400
Pune        Chennai	    400

-- EXPECTED OUTPUT:
SRC         DEST        DISTANCE
Bangalore	Hyderbad	400
Mumbai	    Delhi	    400
Chennai	    Pune	    400
*/

use sql_problems;
create table src_dest_distance
(
    source          varchar(20),
    destination     varchar(20),
    distance        int
);

insert into src_dest_distance values ('Bangalore', 'Hyderbad', 400);
insert into src_dest_distance values ('Hyderbad', 'Bangalore', 400);
insert into src_dest_distance values ('Mumbai', 'Delhi', 400);
insert into src_dest_distance values ('Delhi', 'Mumbai', 400);
insert into src_dest_distance values ('Chennai', 'Pune', 400);
insert into src_dest_distance values ('Pune', 'Chennai', 400);

select * from src_dest_distance;

/*
- As we need to Process(Compare) the Current Row with Other Row(s),, 
- Self Join would be a better option
Process: 
- In given Table,, There is No Unique Identifier(ID)
- So, we create the ID ---> 1st Step 
	- For creating the Row Number use Row_Number Function
- We can see that Records(which needs to be removed),, 
	- Have same Destination as Other Complement Record
- As we have 2 Copies of same Table,, 
	T1.ID < T2.ID && T1.source = T2.destination
    - T1.ID < T2.ID : Checks for the Matching Records for T1 in T2
					  Such that if T1 has ID 1,, then Checks for Matching in Range of Ids(2,..)
                      Not Checks for Same ID Rows in Both Tables
- If we take 1st 2 Records,, 
	T1.ID(1) gets Matches with T2.ID(2) as 2 Conditions gets satisfies
    T1.ID(2) not Matches with T2.ID(1) as 
		- T1.source = T2.destination Satisfies But.. T1.ID < T2.ID not
*/

-- Creation if Row Number For entire Table(Without any Partitions & Ordering)
select *,
row_number() over() as id
from src_dest_distance;

