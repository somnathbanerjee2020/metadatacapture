drop table metadata.job_run_status;

create table metadata.job_run_status
(
	run_id             INT NOT NULL AUTO_INCREMENT,
	job_name           varchar(100),
	start_time         timestamp,
	end_time           timestamp,
	status             varchar(100),
	records_inserted   int,
	primary key(run_id)
);