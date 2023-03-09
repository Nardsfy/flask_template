from flask_template import dbConnect
from flask_template.others.format import responseJSON, row_to_dict_list

def getUserById(p_id):
    conn = None
    try:
        conn = dbConnect()        
        cursor = conn.cursor()
        query = '''
            SELECT u_id, u_username, u_password, u_role
            FROM users
            WHERE 
                u_id = %(id)s
        '''
        params = {
            "id": p_id
        }
        cursor.execute(query, params)
        data = row_to_dict_list(cursor)
        return responseJSON(200, 'T', 'Success get data User.', data)
    except Exception as e:
        return responseJSON(400, 'F', f'Error: {str(e)}', [])
    finally:
        if (conn):
            cursor.close()
            conn.close()

def getUser(p_username, p_password):
    conn = None
    try:
        conn = dbConnect()        
        cursor = conn.cursor()
        query = '''
            SELECT u_id, u_username, u_password, u_role
            FROM users
            WHERE 
                u_username = %(username)s AND
                u_password = %(password)s
        '''
        params = {
            "username": p_username,
            "password": p_password
        }
        cursor.execute(query, params)
        data = row_to_dict_list(cursor)
        return responseJSON(200, 'T', 'Success get User.', data)
    except Exception as e:
        return responseJSON(400, 'F', f'Error: {str(e)}', [])
    finally:
        if (conn):
            cursor.close()
            conn.close()