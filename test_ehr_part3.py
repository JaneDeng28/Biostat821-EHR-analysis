"""Test class and object-oriented functions."""
import ehr_analysis
import ehr_part3
from datetime import datetime

patient_data = ehr_analysis.parse_patient(
    "test_patient.txt"
)
lab_data = ehr_analysis.parse_lab(
    "test_lab.txt"
)

patient_a = ehr_part3.Patient(
    PatientID = "FB2ABB23-C9D0-4D09-8464-49BF0B982F0F"
)
patient_b = ehr_part3.Patient(
    PatientID = "7FD13988-E58A-4A5C-8680-89AC200950FA"
)
patient_c = ehr_part3.Patient(
    PatientID = "B39DC5AC-E003-4E6A-91B6-FC07625A1285"
)

lab_a1 = ehr_part3.Lab(
    PatientID = "1A8791E3-A61C-455A-8DEE-763EB90C9B2C", 
    LabName = "CBC: ABSOLUTE LYMPHOCYTES", 
    LabDateTime = datetime.strptime("1992-06-30 09:39:02.830", "%Y-%m-%d %H:%M:%S.%f")
    )

lab_a2 = ehr_part3.Lab(
    PatientID = "81C5B13B-F6B2-4E57-9593-6E7E4C13B2CE", 
    LabName = "CBC: ABSOLUTE LYMPHOCYTES", 
    LabDateTime = datetime.strptime("2005-07-27 12:03:25.640", "%Y-%m-%d %H:%M:%S.%f")
    )

lab_a3 = ehr_part3.Lab(
    PatientID = "220C8D43-1322-4A9D-B890-D426942A3649", 
    LabName = "CBC: ABSOLUTE LYMPHOCYTES", 
    LabDateTime = datetime.strptime("2000-10-03 11:39:30.210", "%Y-%m-%d %H:%M:%S.%f")
    )

lab_b = ehr_part3.Lab(
    PatientID = "220C8D43-1322-4A9D-B890-D426942A3649", 
    LabName = "URINALYSIS: RED BLOOD CELLS", 
    LabDateTime = datetime.strptime("2011-02-01 21:46:21.930", "%Y-%m-%d %H:%M:%S.%f")
)

lab_c = ehr_part3.Lab(
    PatientID = "C242E3A4-E785-4DF1-A0E4-3B568DC88F2E", 
    LabName = "URINALYSIS: PH", 
    LabDateTime = datetime.strptime("1987-10-10 12:40:17.297", "%Y-%m-%d %H:%M:%S.%f")
)

def test_num_older_than():
    """Test function num_older_than."""
    assert ehr_analysis.num_older_than(
        age = 100, 
        patients = [patient_a, patient_b, patient_c]) == 0


def test_sick_patients():
    """Test function sick_patients."""
    assert len(ehr_analysis.sick_patients(
        lablist = [lab_c, lab_b], 
        lab = 'METABOLIC: GLUCOSE', 
        gt_lt = '>', 
        value = 5.9)) == 0


def test_patient_age():
    """Test function patient_age."""
    assert ehr_analysis.patient_age(
        patients = [patient_a,patient_b,patient_c], 
        patient_id = 'FB2ABB23-C9D0-4D09-8464-49BF0B982F0F') == 74.4