"""Test class and object-oriented functions."""
import ehr_analysis
import ehr_part3

"""
patient_a = ehr_part3.Patient(
    PatientID="FB2ABB23-C9D0-4D09-8464-49BF0B982F0F",
    Gender="Male",
    DOB="1947-12-28 02:45:40.547",
    Race="Unknown",
)"""

patient_a = ehr_part3.Patient(
    PatientID="FB2ABB23-C9D0-4D09-8464-49BF0B982F0F", 
    patfilename="test_patient.txt"
)
"""
patient_b = ehr_part3.Patient(
    PatientID="7FD13988-E58A-4A5C-8680-89AC200950FA",
    Gender="Male",
    DOB="1965-07-12 15:41:20.523",
    Race="White",
)
"""
patient_b = ehr_part3.Patient(
    PatientID="7FD13988-E58A-4A5C-8680-89AC200950FA",
    patfilename="test_patient.txt"
)
"""
patient_c = ehr_part3.Patient(
    PatientID="B39DC5AC-E003-4E6A-91B6-FC07625A1285",
    Gender="Female",
    DOB="1935-11-03 21:07:09.040",
    Race="White",
)
"""
patient_c = ehr_part3.Patient(
    PatientID="B39DC5AC-E003-4E6A-91B6-FC07625A1285",
    patfilename="test_patient.txt"
)

"""
lab_a1 = ehr_part3.Lab(
    PatientID="1A8791E3-A61C-455A-8DEE-763EB90C9B2C",
    LabName="CBC: ABSOLUTE LYMPHOCYTES",
    LabValue=33.3,
    LabUnits="%",
    LabDateTime="1992-06-30 09:39:02.830",
)
"""
lab_a1 = ehr_part3.Lab(
    PatientID="1A8791E3-A61C-455A-8DEE-763EB90C9B2C",
    LabName="CBC: ABSOLUTE LYMPHOCYTES",
    LabDateTime="1992-06-30 09:39:02.830",
    labfilename="test_lab.txt"
)
"""
lab_a2 = ehr_part3.Lab(
    PatientID="81C5B13B-F6B2-4E57-9593-6E7E4C13B2CE",
    LabName="CBC: ABSOLUTE LYMPHOCYTES",
    LabValue=18.2,
    LabUnits="%",
    LabDateTime="2005-07-27 12:03:25.640",
)
"""
lab_a2 = ehr_part3.Lab(
    PatientID="81C5B13B-F6B2-4E57-9593-6E7E4C13B2CE",
    LabName="CBC: ABSOLUTE LYMPHOCYTES",
    LabDateTime="2005-07-27 12:03:25.640",
    labfilename="test_lab.txt"
)
"""
lab_a3 = ehr_part3.Lab(
    PatientID="220C8D43-1322-4A9D-B890-D426942A3649",
    LabName="CBC: ABSOLUTE LYMPHOCYTES",
    LabValue=10.6,
    LabUnits="gm/dl",
    LabDateTime="2000-10-03 11:39:30.210",
)

lab_b = ehr_part3.Lab(
    PatientID="220C8D43-1322-4A9D-B890-D426942A3649",
    LabName="URINALYSIS: RED BLOOD CELLS",
    LabValue=0.3,
    LabUnits="rbc/hpf",
    LabDateTime="2011-02-01 21:46:21.930",
)
"""

lab_b = ehr_part3.Lab(
    PatientID="220C8D43-1322-4A9D-B890-D426942A3649",
    LabName="URINALYSIS: RED BLOOD CELLS",
    LabDateTime="2011-02-01 21:46:21.930",
    labfilename="test_lab.txt"
)
"""
lab_c = ehr_part3.Lab(
    PatientID="C242E3A4-E785-4DF1-A0E4-3B568DC88F2E",
    LabName="URINALYSIS: PH",
    LabValue=5.8,
    LabUnits="no unit",
    LabDateTime="1987-10-10 12:40:17.297",
)
"""
lab_c = ehr_part3.Lab(
    PatientID="C242E3A4-E785-4DF1-A0E4-3B568DC88F2E",
    LabName="URINALYSIS: PH",
    LabDateTime="1987-10-10 12:40:17.297",
    labfilename="test_lab.txt"
)

def test_num_older_than():
    """Test function num_older_than."""
    assert (
        ehr_analysis.num_older_than(age=100, patients=[patient_a, patient_b, patient_c])
        == 0
    )

def test_sick_patients():
    """Test function sick_patients."""
    assert (
        len(
            ehr_analysis.sick_patients(
                lablist=[lab_a1, lab_a2, lab_b, lab_c],
                lab="METABOLIC: GLUCOSE",
                gt_lt=">",
                value=5.9,
            )
        )
        == 0
    )

def test_patient_age():
    """Test function patient_age."""
    assert (
        ehr_analysis.patient_age(
            patients=[patient_a, patient_b, patient_c],
            patient_id="FB2ABB23-C9D0-4D09-8464-49BF0B982F0F",
        )
        == 74.4
    )
