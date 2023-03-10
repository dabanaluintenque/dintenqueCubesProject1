import backend_functions
import teacherdb


def test_teacher_table():

    data = teacherdb.getData()
    cursor = data.cursor()
    select = cursor.execute("SELECT * from teacherTable where firt_name=''")
    my_record = cursor.fetchall()
    assert my_record != ''
