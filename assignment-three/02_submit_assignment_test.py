import pytest
  
@pytest.mark.parametrize("pawprint,submissionIncluded", [
        ("tyc3tt", True),
        ("sespwd", False),
])

def test_submit_assignment(pawprint, submissionIncluded):
	submittedAssignments = ("sty5l7", "tyc3tt", "btw2e4", "sespwd", "sceptx")
	
	assert pawprint in submittedAssignments and submissionIncluded == True
	
	
