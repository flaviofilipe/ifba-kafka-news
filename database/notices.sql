CREATE TABLE IF NOT EXISTS Notices (
    id SERIAL PRIMARY KEY ,
    title text,
    link varchar(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);