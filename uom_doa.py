# from sql_connection import get_sql_connection # extra


# def get_uoms(connection):
#     cursor = connection.cursor()
#     query = ("select * from uom")
#     cursor.execute(query)
#     response = []
#     for (uom_id, uom_name) in cursor:
#         response.append({
#             'uom_id': uom_id,
#             'uom_name': uom_name
#         })
#     return response


# if __name__ == '__main__':
#     from sql_connection import get_sql_connection

#     connection = get_sql_connection()
#     # print(get_all_products(connection))
#     print(get_uoms(connection))

from sql_connection import get_sql_connection  # Ensure proper import

def get_uoms(connection):
    """
    Retrieves all Unit of Measure (UOM) entries from the database.

    Args:
        connection: Database connection object.

    Returns:
        list: A list of dictionaries containing UOM details (id and name).
    """
    cursor = connection.cursor()
    query = "SELECT uom_id, uom_name FROM uom"  # Explicitly specify column names
    cursor.execute(query)

    response = []
    for (uom_id, uom_name) in cursor:
        response.append({
            'uom_id': uom_id,
            'uom_name': uom_name
        })

    cursor.close()  # Close the cursor to free resources
    return response


if __name__ == '__main__':
    connection = get_sql_connection()  # Establish database connection
    uoms = get_uoms(connection)  # Fetch UOMs
    print(uoms)  # Print the retrieved UOMs
