import pytest
  
@pytest.mark.parametrize("student", [
        ("sasp34"),
        ("thy678"),
])

def test_search_student(student):
	students = {
		"sasp34": [1, "Computer Science", 89],
		"rtre4r": [1, "Information Technology", 75],
		"rwe211": [2, "Computer Science", 102],
	}
	
	assert student in students

