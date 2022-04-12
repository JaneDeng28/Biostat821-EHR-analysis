import ehr_analysis
import pytest


def test_parse_data_patient():
    """
    A test function that checks whether the parse_data function returns the correct list for patient data
    """
    assert [
        "64182B95-EB72-4E2B-BE77-8050B71498CE",
        "Male",
        "1952-01-18 19:51:12.917",
        "African American",
        "Separated",
        "English",
        "13.03",
    ] in ehr_analysis.patient_data
    assert len(ehr_analysis.patient_data) == 101


def test_parse_data_lab():
    """
    A test function that checks whether the parse_data function returns the correct list for lab data
    """
    assert [
        "1A8791E3-A61C-455A-8DEE-763EB90C9B2C",
        "1",
        "CBC: MCH",
        "35.8",
        "pg",
        "1992-06-30 03:50:11.777",
    ] in ehr_analysis.lab_data
    assert len(ehr_analysis.lab_data) == 111484


def test_num_older_than():
    """
    A test function that checks whether the num_older_than function returns the correct value
    """
    assert ehr_analysis.num_older_than(50, ehr_analysis.patient_data) == 77


def test_sick_patients():
    """
    A test function that checks whether the sic_patients function returns the correct value
    """
    assert (
        ehr_analysis.sick_patients(ehr_analysis.lab_data, "METABOLIC: ALBUMIN", ">", 5.9)
        == 42
    )


def test_patient_age():
    """
    A test function that checks whether the patient_age function returns the correct age at first admission
    """
    assert (
        ehr_analysis.patient_age(
            ehr_analysis.patient_data, "FB2ABB23-C9D0-4D09-8464-49BF0B982F0F"
        )
        == 74
    )
