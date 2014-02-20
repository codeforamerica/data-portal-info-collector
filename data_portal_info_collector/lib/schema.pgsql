CREATE TABLE IF NOT EXISTS data_portals (
    id                serial PRIMARY KEY,
    place             varchar(60) NOT NULL,
    portal_url        varchar(60) NOT NULL,
    data_sets         text,
    included_formats  text,
    press_release_url varchar(60),
    data_completeness varchar(25),
    comments          text
);

ALTER TABLE data_portals ADD COLUMN state varchar(30);

ALTER TABLE data_portals ADD COLUMN created_at timestamp;

ALTER TABLE data_portals ALTER COLUMN press_release_url SET DATA text;
ALTER TABLE data_portals ALTER COLUMN portal_url SET DATA text;
ALTER TABLE data_portals ALTER COLUMN place SET DATA text;
