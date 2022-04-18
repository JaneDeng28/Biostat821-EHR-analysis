import ehr_analysis

patient_data = ehr_analysis.parse_patient(
    "https://github.com/JaneDeng28/Biostat821-EHR-analysis/blob/077fbfefd6f2ad1c982fa3de946585e4b9c7040a/test_patient.txt"
)
lab_data = ehr_analysis.parse_lab(
    "https://github.com/JaneDeng28/Biostat821-EHR-analysis/blob/077fbfefd6f2ad1c982fa3de946585e4b9c7040a/test_lab.txt"
)


def test_parse_patient():
    """
    A test function that checks whether the parse_data function returns the correct list for patient data
    """
    assert [
        "FB2ABB23-C9D0-4D09-8464-49BF0B982F0F",
        "Male",
        "1947-12-28 02:45:40.547",
        "Unknown",
        "Married",
        "Icelandic",
        "18.08",
    ] in patient_data
    assert len(patient_data) == 1


def test_parse_lab():
    """
    A test function that checks whether the parse_data function returns the correct list for lab data
    """
    assert [
        "FB2ABB23-C9D0-4D09-8464-49BF0B982F0F",
        "1",
        "URINALYSIS: RED BLOOD CELLS",
        "1.8",
        "rbc/hpf",
        "1992-07-01 01:36:17.910",
    ] in lab_data
    assert len(lab_data) == 2


def test_num_older_than():
    """
    A test function that checks whether the num_older_than function returns the correct value
    """
    assert ehr_analysis.num_older_than(50, patient_data) == 78


def test_sick_patients():
    """
    A test function that checks whether the sic_patients function returns the correct value
    """
    assert ehr_analysis.sick_patients(lab_data, "METABOLIC: ALBUMIN", ">", 5.9) == 42


def test_patient_age():
    """
    A test function that checks whether the patient_age function returns the correct age at first admission
    """
    assert (
        ehr_analysis.patient_age(patient_data, "FB2ABB23-C9D0-4D09-8464-49BF0B982F0F")
        == 74
    )
