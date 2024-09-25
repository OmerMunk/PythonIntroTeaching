CREATE TABLE IF NOT EXISTS customers (
    customer_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100),
    phone_numbers TEXT,
    address VARCHAR(255),
    city VARCHAR(100),
    favorite_product VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT,
    product_ids TEXT,
    total_amount NUMERIC(10, 2),
    order_date DATE
);

CREATE TABLE IF NOT EXISTS products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100),
    categories TEXT,
    supplier_name VARCHAR(100),
    price NUMERIC(10, 2)
);

DO $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1..1000 LOOP
        INSERT INTO customers (customer_name, phone_numbers, address, city, favorite_product)
        VALUES (
            'Customer ' || i,
            '1234567890,0987654321',
            'Address ' || i,
            'City ' || i,
            'Product ' || (i % 10)
        );

        INSERT INTO products (product_name, categories, supplier_name, price)
        VALUES (
            'Product ' || i,
            'Category1,Category2',
            'Supplier ' || (i % 5),
            (i * 10.0)  -- Random price
        );

        INSERT INTO orders (customer_id, product_ids, total_amount, order_date)
        VALUES (
            i,
            '1,2,3',
            100.0,
            CURRENT_DATE - i
        );
    END LOOP;
END $$;
