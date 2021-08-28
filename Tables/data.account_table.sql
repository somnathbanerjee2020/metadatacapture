drop table data.account_table;

create table data.account_table
(
	id               INT NOT NULL AUTO_INCREMENT,
	run_id           INT,
	account_id       varchar(100),
	account_name     varchar(200),
	account_revenue  float,
	account_manager  varchar(100),
	revenue_year     int,
	updated_date    datetime,
	primary key(id)
)
;