"""Test class and object-oriented functions."""
import ehr_analysis
import ehr_part3

testpat = ehr_analysis.build_patient("test_patient.txt")
testlab = ehr_analysis.build_lab("test_lab.txt")

def test_build_patient():
    assert testpat[0].gender == "Male"

def test_build_lab():
    assert testlab[0].PatientID == "1A8791E3-A61C-455A-8DEE-763EB90C9B2C"

def test_num_older_than():
    """Test function num_older_than."""
    assert (
        ehr_analysis.num_older_than(age=100, patients= testpat)
        == 0
    )

def test_sick_patients():
    """Test function sick_patients."""
    assert (
        len(
            ehr_analysis.sick_patients(
                lablist=testlab,
                lab="CBC: ABSOLUTE LYMPHOCYTES",
                gt_lt=">",
                value=100,
            )
        )
        == 0
    )

def test_patient_age():
    """Test function patient_age."""
    assert (
        ehr_analysis.patient_age(
            patients=testpat,
            patient_id="FB2ABB23-C9D0-4D09-8464-49BF0B982F0F",
        )
        == 74.4
    )
