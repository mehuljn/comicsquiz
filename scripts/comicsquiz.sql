CREATE TABLE character {
	name		varchar(255),
	real_name 	varchar(255),
	aliases		varchar(255),
	id		real primary key,
	image		varchar(255),
	source_url	varchar(255),
	status 		real
};

CREATE TABLE power {
	name		varchar(255),
	id		real primary key,
	url		varchar(255)
};

CREATE TABLE character_power {
	char_id 	real references character(id),
	power_id	real references power(id),
};

CREATE TABLE character_fande {
	char_id		real,
	fande_id	real,
	flag		real
}; 
