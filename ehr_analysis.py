from datetime import datetime
from typing import Union
from typing import List

"""Data Parsing"""


from datetime import datetime
from typing import List


def parse_patient(patient: str) -> List[List[str]]:
    with open(patient, "r") as file:
        rows = file.readlines()
        lists = []
    for row in rows:
        row = row.strip()
        row = row.split("\t")
        lists.append(row)
    return lists


def parse_lab(lab: str) -> List[List[str]]:
    with open(lab, "r") as file:
        rows = file.readlines()
        lists = []
    for row in rows:
        row = row.strip()
        row = row.split("\t")
        lists.append(row)
    return lists


def num_older_than(age: float, patients: List[str]) -> int:
    count = 0
    for i in range(len(patients)):
        if patients[i].age > age:
            count += 1
    return count


def sick_patients(
    lablist: List[str], lab: str, gt_lt: str, value: float
) -> List[str]:
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


def patient_age(patients: List[str], patient_id: List[str]) -> int:
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
        "/Users/jane/2022/SP2022/BIOSTAT821/PatientCorePopulatedTable.txt"
    )
    print(num_older_than(51.2, patient_data))
    lab_data = parse_lab(
        "/Users/jane/2022/SP2022/BIOSTAT821/LabsCorePopulatedTable.txt"
    )
    print(sick_patients(lab_data, "METABOLIC: ALBUMIN", ">", 4.0))
