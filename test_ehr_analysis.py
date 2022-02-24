import ehr_analysis
import pytest

def test_parse_data_patient():
    '''
    A test function that checks whether the parse_data function returns the correct list for patient data
    '''
    assert ['6E70D84D-C75F-477C-BC37-9177C3698C66', 'Male', '1979-01-04 05:45:29.580', 'White', 'Married',
            'English', '16.09'] in ehr_analysis.filename
    assert len(ehr_analysis.filename) == 101

def test_parse_data_lab():
    '''
    A test function that checks whether the parse_data function returns the correct list for lab data
    '''
    assert ['1A8791E3-A61C-455A-8DEE-763EB90C9B2C', '1', 'METABOLIC: SODIUM', '130.4', 'mmol/L',
            '1992-06-30 14:25:18.260'] in ehr_analysis.filename
    assert len(ehr_analysis.filename) == 111484

def test_num_older_than():
    '''
    A test function that checks whether the num_older_than function returns the correct value
    '''
    assert ehr_analysis.num_older_than(50, ehr_analysis.dataname) == 77
def test_sick_patients():
    '''
    A test function that checks whether the sic_patients function returns the correct value
    '''
    assert ehr_analysis.sick_patients(ehr_analysis.labs, "METABOLIC: ALBUMIN", ">", 5.9) == 42

def test_patient_age():
    '''
    A test function that checks whether the patient_age function returns the correct age at first admission
    '''
    assert ehr_analysis.patient_age(ehr_analysis.patient, "FB2ABB23-C9D0-4D09-8464-49BF0B982F0F") == 74