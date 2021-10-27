CREATE DATABASE mqtt;

CREATE TABLE T1 (
created_at DATETIME2(7),
received_at DATETIME2(7),
sensor_data BINARY(2048)
)

CREATE TABLE T2 (
package_id INT,
started_at DATETIME2(7),
created_at DATETIME2(7),
received_at DATETIME2(7),
sensor_data SMALLINT
)

