-- Create a non-normalized customers table
CREATE TABLE IF NOT EXISTS customers (
    customer_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100),
    phone_numbers TEXT,  -- Comma-separated list of phone numbers (1NF violation)
    address VARCHAR(255),
    city VARCHAR(100),
    favorite_product VARCHAR(100)  -- Redundant, unrelated to the customer (3NF violation)
);

-- Create a non-normalized orders table
CREATE TABLE IF NOT EXISTS orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT,
    product_ids TEXT,  -- Comma-separated list of product IDs (1NF violation)
    total_amount NUMERIC(10, 2),  -- Redundant, derived from product prices (2NF violation)
    order_date DATE
);

-- Create a non-normalized products table
CREATE TABLE IF NOT EXISTS products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100),
    categories TEXT,  -- Comma-separated list of categories (1NF violation)
    supplier_name VARCHAR(100),  -- Redundant, suppliers should be in a separate table (3NF violation)
    price NUMERIC(10, 2)
);

-- Insert sample data with a loop
DO $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1..1000 LOOP
        -- Insert into customers
        INSERT INTO customers (customer_name, phone_numbers, address, city, favorite_product)
        VALUES (
            'Customer ' || i,
            '1234567890,0987654321',  -- Comma-separated phone numbers
            'Address ' || i,
            'City ' || i,
            'Product ' || (i % 10)  -- Favorite product (unrelated to customer)
        );

        -- Insert into products
        INSERT INTO products (product_name, categories, supplier_name, price)
        VALUES (
            'Product ' || i,
            'Category1,Category2',  -- Comma-separated categories
            'Supplier ' || (i % 5),  -- Redundant supplier information
            (i * 10.0)  -- Random price
        );

        -- Insert into orders
        INSERT INTO orders (customer_id, product_ids, total_amount, order_date)
        VALUES (
            i,
            '1,2,3',  -- Comma-separated product IDs
            100.0,  -- Redundant total amount (should be derived)
            CURRENT_DATE - i  -- Random order date
        );
    END LOOP;
END $$;
