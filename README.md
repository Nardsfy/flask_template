# flask_template
Template project for Flask Python

Link assets: https://drive.google.com/drive/folders/1C_RVtgKaufwPaFMr1PX-f9eBec3q6si5?usp=drive_link

DDL for PostgreSQL is required to test with flask login:
CREATE TABLE users (
    u_username varchar(12) NOT NULL,
    u_password varchar(200) NOT NULL,
    u_role varchar(2) NOT NULL,
    u_status varchar(1) NOT NULL,
    u_ins_date timestamp NOT NULL DEFAULT (CURRENT_TIMESTAMP AT TIME ZONE 'Asia/Jakarta'::text),
    u_ins_user varchar(12) NOT NULL,
    u_upd_date timestamp NULL,
    u_upd_user varchar(12) NULL,
    CONSTRAINT users_pk PRIMARY KEY (u_username)
);