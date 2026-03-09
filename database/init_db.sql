CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    product_id VARCHAR(100) NOT NULL UNIQUE,
    product_name VARCHAR(100) NOT NULL,
    product_url TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS prices (
    id SERIAL PRIMARY KEY,
    product_id VARCHAR(100) NOT NULL,
    product_price NUMERIC(10, 2) NOT NULL,
    recorded_at TIMESTAMP NOT NULL DEFAULT NOW(),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

CREATE INDEX IF NOT EXISTS idx_prices_product_id_recorded_at ON prices(product_id, recorded_at);
