/*
-->> Problem Statement:
Write a query to fetch the record of brand whose amount is increasing every year.
*/

-->> Dataset:
drop table brands;
create table brands
(
    Year    int,
    Brand   varchar(20),
    Amount  int
);
insert into brands values (2018, 'Apple', 45000);
insert into brands values (2019, 'Apple', 35000);
insert into brands values (2020, 'Apple', 75000);
insert into brands values (2018, 'Samsung',	15000);
insert into brands values (2019, 'Samsung',	20000);
insert into brands values (2020, 'Samsung',	25000);
insert into brands values (2018, 'Nokia', 21000);
insert into brands values (2019, 'Nokia', 17000);
insert into brands values (2020, 'Nokia', 14000);

select * from brands;
/*
- Among the three brands Samsung is the only brand which is increasing for every year
- Let's see we have grouped based on brand,, then if records are not sorted based on year we have to sort them
- So when we have to process/check we need to get access to the next row of the same group
- If the Amount in current record and amnt in next record are in increasing fashion then okay
	- Also we how to do that kind of comparision for each brand group(have to do paritition)
- Best window function to fetch the Next record is "Lead" window function
- Lead Function : 
	The LEAD window function in SQL is used to access data from subsequent rows in a result set
     without the need for a self-join. 	
- Some issue may happen when our current row is the last row of the corresponding group
	- As at that time there will be no next record,, the default value should be taken care
- We create a "flag" column which represents 0 if not increasing && 
	1 if increasing for the current and next rows
*/

select *,
 lead(amount) over(partition by brand order by year)
from brands;
/*
-- From above code,, in Output we got a Separate column for the Lead Amount & what we saw is
--  For the Last Row of each Group the Default value is coming as NULL,,
-- Okay but for the flag column, we need 0 or 1 that means we how to make comparison
-- We can Compare that Lead Output using "CASE"
*/

select *, 
(case when amount < lead(amount) over(partition by brand order by year) 
     then 1 else 0 
 end) flag
from brands;
-- From Above Output,, For Last Row(of each group) got 0

select *, 
(case when amount > lead(amount) over(partition by brand order by year) 
     then 0 else 1 
 end) flag
from brands;
-- From Above Output,, For Last Row(of each group) got 1

-- Also,, we can change Default Value
select *, 
(case when amount < lead(amount, 1, amount + 1) over(partition by brand order by year)
	 then 1 else 0
end) as flag 
from brands;

-- Next we have to make a Partition based on brand and have to check whether each row contains
--  flag as one or not (if yes then that brand is our output)
-- Let's use that as CTE
with cte as 
(
	select *, 
	(case when amount < lead(amount, 1, amount + 1) over(partition by brand order by year)
		  then 1 else 0
	end) as flag 
	from brands
)
select distinct brand -- Displaying the Brand Name Only Once
from brands
where brand not in (select brand from cte where flag = 0);
	-- Selecting the Brand Name,, which does not contain flag as 0
