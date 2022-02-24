from datetime import date, timedelta, datetime
from tempfile import TemporaryFile
from typing import Union

    """Data Parsing"""

def parse_data(filename):
    result = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        headers = lines[0].encode("utf-8").decode("utf-8-sig").strip().split()  # O(1)
        for line in lines[1:]:  # N - 1, start from 2 nd line
            d = dict()  # O(1)
            data = line.strip().split("\t")  # O(1)
            for i in range(len(data)):  # M times -> constant : 7
                key = headers[i]  # O(1)
                d[key] = data[i]  # O(1)
            result.append(d)  # O(1)
    return result
    # O(1) + O(1) + O(1) + O(1) + (N - 1) * O(1) + (N - 1) * O(1) + (N - 1) * (M * O(1) + M * O(1)) + (N - 1) * O(1)
    # (N - 1) * (3 * O(1) + (M * O(1) + M * O(1))
    # -> (N - 1) * 2M * O(1) - > (N - 1) * 2M -> N * M -> O(N * M)
    # -> O(N)

from datetime import datetime
def parse_data(filename):
    with open(filename) as table:
        return [line.replace('\n','').split('\t') for line in table][1:]


def num_older_than(age_old:Union[int, float], dataname):
    num = 0
    for record in dataname: # N
        birth = record["PatientDateOfBirth"]# 0(1)
        b_str = datetime.strptime(birth, "%Y-%m-%d %H:%M:%S.%f")# 0(1)
        age_new = (datetime.today() - b_str) / timedelta(days=365.2425)# 0(1)
        if age_new > age_old:# 0(1)
            num += 1# 0(1)
    return num
# 5 * N -> 0(N)

def num_older_than(age, patients):
    DOB = [patient[2] for patient in patients][1:]
    DOB = [datetime.strptime(patient, '%Y-%m-%d %H:%M:%S.%f') for patient in DOB]
    Today = datetime.now()
    diff = [round((Today - DOB).days / 365, 1) for patient in DOB]
    return len([patient for patient in diff if patient > age])  


def sick_patients(lab, gt_lt, value, lablist): 
    lab_name = 0
    lab_value = 0
    
    for i in range(len(lablist[0])): # 6 times
        if lablist[0][i] == 'LabName': #O(1)
            lab_name = i
        if lablist[0][i] == 'LabValue': #O(1)
            lab_value = i
    
    Larger = []
    Smaller = []

    for i in range(1, len(lablist)): # N times
        if lablist[i][lab_name] == lab: #O(1)
            if gt_lt == '>' and float(lablist[i][lab_value]) > value: 
                Larger.append(lablist[i][0])
            elif gt_lt == '<' and float(lablist[i][lab_value]) < value:
                Smaller.append(lablist[i][0])
    
    idlist = []
    newlist = []
    
    if Larger != [] and gt_lt == '>':
        idlist = Larger
    if Smaller != [] and gt_lt == '<':
        idlist = Smaller
    

def sick_patients(lab, gt_lt, value, lablist): 
    stat = lambda lab_value, ref_value: (gt_lt == '>' and lab_value > ref_value) or (gt_lt == '<' and lab_value < ref_value)
    sick_list = [row[0] for row in lablist[1:] if row[2] == lab and stat(float(row[3]), value)]
    sick_list = list(set(sick_list))
    return sick_list


if __name__ == '__main__':
    patients = parse_data('/Users/jane/2022/SP2022/BIOSTAT821/hw2/PatientCorePopulatedTable.txt')
    labs = parse_data('/Users/jane/2022/SP2022/BIOSTAT821/hw2/LabsCorePopulatedTable.txt')
try:
	thatlab = input("Enter lab name")
	ltgt = input("Enter > or < ")
    index = float(input("Enter a index value"))
    print(sick_patients(labs, thatlab, ltgt,index))
except:
    raise ValueError("Input shold follow the instruction")


def patient_age(patients, patient_id):
    '''
    A function that computes the age at first admission of any given patient
    @param patients: input data
    @param patient_id: specific patient
    @return: age of the specific patient
    '''
    date0 = datetime.now()
    for patient in patients:
        birth = datetime.strptime(patient[2], '%Y-%m-%d %H:%M:%S.%f')
        if patient[0] == patient_id:
            return round((date0 - birth).days / 365, 1)
            break


if __name__ == "__main__ ":
    patient_data = parse_data(
        "/Users/jane/2022/SP2022/BIOSTAT821/PatientCorePopulatedTable.txt"
    )
    print(num_older_than(51.2, dataname))

    lab_data = parse_data(
        "/Users/jane/2022/SP2022/BIOSTAT821/LabsCorePopulatedTable.txt"
    )
    print(sick_patients("METABOLIC: ALBUMIN", ">", 4.0, lab_name))
