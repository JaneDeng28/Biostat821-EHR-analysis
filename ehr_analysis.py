from datetime import datetime
from typing import Union
from typing import List

"""Data Parsing"""

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

def num_older_than(age: float, patient: List[List[str]]) -> int:
    now = datetime.today() 
    num = 0 
    for i in range(1, len(patient) - 1): 
        born = datetime.strptime(patient[i][2], "%Y-%m-%d %H:%M:%S.%f") 
        if (now.year - born.year - ((now.month, now.day) < (born.month, born.day))) > age: 
            num += 1 
    return num  


def sick_patients(lab: str, gt_lt: str, value: float, lablist: List[List[str]] ) -> List[str]:
    patid = set()
    for i in range(1, len(lablist)-1):
        if lablist[i][2] == lab:
            if gt_lt == ">":
                if float(lablist[i][3]) > value:
                    patid.add(lablist[i][0])
            elif gt_lt == "<":
                if float(lablist[i][3]) < value:
                    patid.add(lablist[i][0])
            else: 
                raise ValueError("Please input vaild '<' or '>'") 
    return list(patid)

def patient_age(patients:List[str], patient_id:List[str]) -> int:
    """
    A function that computes the age at first admission of any given patient
    @param patients: input data
    @param patient_id: specific patient
    @return: age of the specific patient
    """
    date0 = datetime.now()
    for patient in patients:
        birth = datetime.strptime(patient[2], "%Y-%m-%d %H:%M:%S.%f")
        if patient[0] == patient_id:
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
