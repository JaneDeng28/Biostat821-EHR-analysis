from datetime import datetime
from typing import List
from ehr_part3 import Patient, Lab

"""Data Parsing"""

def parse_patient(patfilename:List[str]) -> List[Patient]:
	with open(patfilename) as patient_table:
		return [line.replace('\n','').split('\t') for line in patient_table][1:]

def parse_lab(labfilename:List[str]) -> List[Lab]:
	with open(labfilename) as labs_table:
		return [line.replace('\n','').split('\t') for line in labs_table][1:]

"""Functions"""

def num_older_than(age: float, patients: List[str]) -> int:
    count = 0
    for i in range(len(patients)):
        if patients[i].age > age:
            count += 1
    return count


def sick_patients(
    lablist: List[str], lab: str, gt_lt: str, value: float
) -> List[Lab]:
    patid = set()
    for i in range(1, len(lablist) - 1):
        if lablist[i].LabName == lab:
            if gt_lt == ">":
                if float(lablist[i].LabValue) > value:
                    patid.add(lablist[i].PatientID)
            elif gt_lt == "<":
                if float(lablist[i].LabValue) < value:
                    patid.add(lablist[i].PatientID)
            else:
                raise ValueError("Please input vaild '<' or '>'")
    return list(patid)


def patient_age(patients: List[str], patient_id: List[str]) -> float:
    """
    A function that computes the age at first admission of any given patient
    @param patients: input data
    @param patient_id: specific patient
    @return: age of the specific patient
    """
    date0 = datetime.now()
    for patient in patients:
        birth = patient.DOB
        if patient.PatientID == patient_id:
            return round((date0 - birth).days / 365, 1)


if __name__ == "__main__ ":
    patient_data = parse_patient(
        "PatientCorePopulatedTable.txt"
    )
    print(num_older_than(51.2, patient_data))
    lab_data = parse_lab(
        "LabsCorePopulatedTable.txt"
    )
    print(sick_patients(lab_data, "METABOLIC: ALBUMIN", ">", 4.0))
