from sqlalchemy import inspect

from databases.database import engine


def does_table_exist(table_name):
    
    if inspect(engine).has_table(table_name): # does the table exist
        return True
    return False


def table_schema(table_name):
    inspector = inspect(engine)
    columns = inspector.get_columns(table_name)
    return{'Schema':columns}


def dynamic_serialization(sql, result): 
    serialized_data = []
    for rows in result:
        data = dict(zip(sql.keys(),rows))
        serialized_row = data 
        serialized_data.append(serialized_row)
    return serialized_data

def schema_serialization(schema):
    serialized_data = []
    s_svalues = []
    for i in schema['Schema']:
        for j in i.values():
            s_svalues.append(str(j))
        
        data = dict(zip(i.keys(),s_svalues))
        serialized_row = data
        serialized_data.append(serialized_row)
        s_svalues = []
    return serialized_data