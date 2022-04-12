from datetime import date, timedelta, datetime
from typing import Union

"""Data Parsing"""


def parse_data(filename: str) -> list[str]:
    result = []
    with open(filename, "r") as f:
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


def num_older_than(age_old: Union[int, float], dataname: str) -> int:
    num = 0
    for record in dataname:  # N
        birth = record["PatientDateOfBirth"]  # 0(1)
        b_str = datetime.strptime(birth, "%Y-%m-%d %H:%M:%S.%f")  # 0(1)
        age_new = (datetime.today() - b_str) / timedelta(days=365.2425)  # 0(1)
        if age_new > age_old:  # 0(1)
            num += 1  # 0(1)
    return num


# 5 * N -> 0(N)


def sick_patients(lab:str, gt_lt:str, value:float, lablist:list[str]) -> list[str]:
    lab_name = 0
    lab_value = 0

    for i in range(len(lablist[0])):  # 6 times
        if lablist[0][i] == "LabName":  # O(1)
            lab_name = i
        if lablist[0][i] == "LabValue":  # O(1)
            lab_value = i

    Larger = []
    Smaller = []

    for i in range(1, len(lablist)):  # N times
        if lablist[i][lab_name] == lab:  # O(1)
            if gt_lt == ">" and float(lablist[i][lab_value]) > value:
                Larger.append(lablist[i][0])
            elif gt_lt == "<" and float(lablist[i][lab_value]) < value:
                Smaller.append(lablist[i][0])

    idlist = []
    newlist = []

    if Larger != [] and gt_lt == ">":
        idlist = Larger
    if Smaller != [] and gt_lt == "<":
        idlist = Smaller
    for i in idlist:
        if i not in newlist:
            newlist.append(i)

    return newlist


def patient_age(patients:list[str], patient_id:list[str]) -> int:
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
    patient_data = parse_data(
        "/Users/jane/2022/SP2022/BIOSTAT821/PatientCorePopulatedTable.txt"
    )
    print(num_older_than(51.2, patient_data))

    lab_data = parse_data(
        "/Users/jane/2022/SP2022/BIOSTAT821/LabsCorePopulatedTable.txt"
    )
    print(sick_patients("METABOLIC: ALBUMIN", ">", 4.0, lab_data))
