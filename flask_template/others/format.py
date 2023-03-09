def row_to_dict_list(cursor):
    return [dict(zip([column[0] for column in cursor.description], row)) for row in cursor.fetchall()]

def responseJSON(status_code, status, message, result):
    return {
        "status_code": status_code, 
        "status": status, 
        "message": message, 
        "result": result
    }