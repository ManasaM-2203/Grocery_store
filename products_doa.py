

# from sql_connection import get_sql_connection

# def get_all_products(connection):
#     cursor = connection.cursor()

#     query = """
#     SELECT products.product_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name 
#     FROM products 
#     INNER JOIN uom ON products.uom_id = uom.uom_id
#     """

#     cursor.execute(query)

#     response = []

#     for (Product_id, name, uom_id, price_per_unit, uom_name) in cursor:
#         response.append({
#             'Product_id': Product_id,
#             'name': name,
#             'uom_id': uom_id,
#             'price_per_unit': price_per_unit,
#             'uom_name': uom_name  # Missing this field in the original code
#         })
    
#     connection.close()  # Use connection.close() instead of cnx.close()
#     return response

# def insert_new_product(connection, product):
#     cursor = connection.cursor()

#     query = """
#     INSERT INTO Products (name, uom_id, price_per_unit)
#     VALUES (%s, %s, %s)
#     """
#     data = (product['product_name'], product['uom_id'], product['price_per_unit'])
    
#     cursor.execute(query, data)
#     connection.commit()  # Added parentheses to call commit()
#     return cursor.lastrowid

# def delete_product(connection, product_id):
#     cursor = connection.cursor()
    
#     query = """
#     DELETE FROM Products WHERE product_id = %s
#     """
#     cursor.execute(query, (product_id,))  # Use parameterized query to prevent SQL injection
    
#     connection.commit()

# if __name__ == "__main__":
#     connection = get_sql_connection()
#     print(delete_product(connection, 2))


from sql_connection import get_sql_connection

def get_all_products(connection):
    cursor = connection.cursor()

    query = """
    SELECT products.product_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name 
    FROM products 
    INNER JOIN uom ON products.uom_id = uom.uom_id
    """

    cursor.execute(query)

    response = []

    for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:  # Fixed variable casing
        response.append({
            'product_id': product_id,  # Changed 'Product_id' to 'product_id' for consistency
            'name': name,
            'uom_id': uom_id,
            'price_per_unit': price_per_unit,
            'uom_name': uom_name  # Added the missing field
        })

    cursor.close()  # Close the cursor
    return response

def insert_new_product(connection, product):
    cursor = connection.cursor()

    query = """
    INSERT INTO products (name, uom_id, price_per_unit)
    VALUES (%s, %s, %s)
    """
    data = (product['product_name'], product['uom_id'], product['price_per_unit'])

    cursor.execute(query, data)
    connection.commit()  # Ensure commit to save changes
    product_id = cursor.lastrowid  # Store the last inserted ID

    cursor.close()  # Close the cursor
    return product_id

def delete_product(connection, product_id):
    cursor = connection.cursor()
    
    query = """
    DELETE FROM products WHERE product_id = %s
    """
    cursor.execute(query, (product_id,))  # Use a tuple (product_id,) for a single parameter

    connection.commit()  # Ensure commit to apply deletion
    affected_rows = cursor.rowcount  # Capture the number of rows affected
    
    cursor.close()  # Close the cursor
    return affected_rows  # Return the number of deleted rows for verification

if __name__ == "__main__":
    connection = get_sql_connection()
    # Test delete_product with product_id = 2
    result = delete_product(connection, 2)
    if result > 0:
        print(f"Product with ID 2 deleted successfully. Rows affected: {result}")
    else:
        print("No product found with ID 2.")
