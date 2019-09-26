import pytest
  
@pytest.mark.parametrize("pawprint,section", [
        ("sespwd", 1),
        ("jlp56e", 3),
])

def test_add_TA(pawprint, section):
	TA_assignments = {
		"tcgyyt": 2,
		"stw444": 1,
		"ree24g": 1,
	}
	sectionList = [1, 2]
	
	TA_assignments[pawprint] = section
	assert section in sectionList
