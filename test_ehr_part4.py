"""Test class and object-oriented functions."""
from ehr_analysis_part4 import (sick_patients, num_older_than, patient_age)

def test_number_older_than():
    assert num_older_than(100) == 0

def test_sick_pats():
    assert sick_patients('CBC: ABSOLUTE LYMPHOCYTES', '>', 100) == []

def test_patient_age():
    assert patient_age(PatientID='FB2ABB23-C9D0-4D09-8464-49BF0B982F0F') == [(74.4,)]
