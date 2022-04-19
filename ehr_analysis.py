from datetime import datetime
from typing import List

def parse_data(filename:str) -> List[str]:
    with open(filename) as table:
        return [line.replace('\n','').split('\t') for line in table][1:]

def num_older_than(age:float, patients:List[str]) -> int:
    DOB = [patient[2] for patient in patients][1:]
    DOB = [datetime.strptime(patient, '%Y-%m-%d %H:%M:%S.%f') for patient in DOB]
    Today = datetime.now()
    diff = [round((Today - DOB).days / 365, 1) for patient in DOB]
    return len([patient for patient in diff if patient > age])  
    

def sick_patients(lablist: List[List[str]], lab: str, gt_lt: str, value: float) -> List[str]: 
    stat = lambda lab_value, ref_value: (gt_lt == '>' and lab_value > ref_value) or (gt_lt == '<' and lab_value < ref_value)
    sick_list = [row[0] for row in lablist[1:] if row[2] == lab and stat(float(row[3]), value)]
    sick_list = list(set(sick_list))
    return sick_list


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

if __name__ == '__main__':
    patients = parse_data('/Users/jane/2022/SP2022/BIOSTAT821/hw2/PatientCorePopulatedTable.txt')
    labs = parse_data('/Users/jane/2022/SP2022/BIOSTAT821/hw2/LabsCorePopulatedTable.txt')
try:
	thatlab = input("Enter lab name")
	ltgt = input("Enter > or < ")
    index = float(input("Enter a index value"))
    print(sick_patients(thatlab, gtlt, index, labs))
except:
    raise ValueError("Input shold follow the instruction")
    
print(sick_patients(thatlab, gtlt, index, labs))
print(len(sick_patients(labs, 'METABOLIC: ALBUMIN', '>', 5.9)))
