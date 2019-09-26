import pytest
  
@pytest.mark.parametrize("student,grade,TA", [
        ("sasp34", 89, "sespwd"),
        ("thy678", 90, "sespwd"),
])        

def test_submit_grade(student, grade, TA):
	TA_sections = {
		"sespwd": 1,
		"dtw45t": 2
	}

	sections = {
		1: ["trw456", "rty9yt", "sasp34"],
		2: ["wqrttt", "thy678", "yll22h"],
	}

	grades = {
		"trw456": 87,
		"rty9yt": 100,
		"sasp34": 68,
		"wqrttt": 70,
		"yll22h": 96,
	}
	
	grades[student] = grade
	
	assert student in sections[TA_sections[TA]] and grades[student] == grade
	
