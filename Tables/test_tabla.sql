create table data.account_table
(
	id               INT NOT NULL AUTO_INCREMENT,
	account_id       varchar(100),
	account_name     varchar(200),
	account_revenue  float,
	account_manager  varchar(100),
	revenue_year     int,
	is_current       varchar(2),
	updated_date    date,
	primary key(id)
)
;