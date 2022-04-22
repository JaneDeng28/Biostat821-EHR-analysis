"""Test class and object-oriented functions."""
import ehr_analysis
import ehr_analysis_part4

"""
patlocation = "/Users/jane/2022/SP2022/BIOSTAT821/ehr-project/patient.db"
lablocation = "/Users/jane/2022/SP2022/BIOSTAT821/ehr-project/lab.db"
"""
patient_a = ehr_analysis_part4.Patient(
    PatientID="FB2ABB23-C9D0-4D09-8464-49BF0B982F0F", 
    PATDB_location = "patient.db",
    patfilename = "test_patient.txt"
)

patient_b = ehr_analysis_part4.Patient(
    PatientID="7FD13988-E58A-4A5C-8680-89AC200950FA",
    PATDB_location = "patient.db",
    patfilename = "test_patient.txt"
)

patient_c = ehr_analysis_part4.Patient(
    PatientID="B39DC5AC-E003-4E6A-91B6-FC07625A1285",
    PATDB_location = "patient.db",
    patfilename = "test_patient.txt"
)

lab_a1 = ehr_analysis_part4.Lab(
    PatientID="1A8791E3-A61C-455A-8DEE-763EB90C9B2C",
    PATDB_location = "lab.db",
    patfilename = "test_lab.txt"
)

lab_a2 = ehr_analysis_part4.Lab(
    PatientID="81C5B13B-F6B2-4E57-9593-6E7E4C13B2CE",
    PATDB_location = "lab.db",
    patfilename = "test_lab.txt"
)

lab_b = ehr_analysis_part4.Lab(
    PatientID="220C8D43-1322-4A9D-B890-D426942A3649",
    PATDB_location = "lab.db",
    patfilename = "test_lab.txt"
)

lab_c = ehr_analysis_part4.Lab(
    PatientID="C242E3A4-E785-4DF1-A0E4-3B568DC88F2E",
    PATDB_location = "lab.db",
    patfilename = "test_lab.txt"
)

def test_num_older_than():
    """Test function num_older_than."""
    assert (
        ehr_analysis_part4.num_older_than(age=100, patients=[patient_a, patient_b, patient_c])
        == 0
    )

def test_sick_patients():
    """Test function sick_patients."""
    assert (
        len(
            ehr_analysis_part4.sick_patients(
                lablist=[lab_a1, lab_b, lab_c],
                lab="CBC: ABSOLUTE LYMPHOCYTES",
                gt_lt=">",
                value=5.9,
            )
        )
        == 0
    )

def test_patient_age():
    """Test function patient_age."""
    assert (
        ehr_analysis_part4.patient_age(
            patients=[patient_a],
            patient_id="FB2ABB23-C9D0-4D09-8464-49BF0B982F0F",
        )
        == 74.4
    )
