from flask_template import dbConnect
from flask_template.others.format import responseJSON, row_to_dict_list

def getUser():
    conn = None
    try:
        conn = dbConnect()        
        cursor = conn.cursor()
        query = '''
            SELECT u_id, u_username, u_password, u_role
            FROM users
        '''
        cursor.execute(query)
        data = row_to_dict_list(cursor)
            
        return responseJSON(200, 'T', 'Success get User.', data)
    except Exception as e:
        return responseJSON(400, 'F', f'Error: {str(e)}', [])
    finally:
        if (conn):
            cursor.close()
            conn.close()