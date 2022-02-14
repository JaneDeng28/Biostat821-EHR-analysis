from datetime import date, timedelta, datetime
from typing import Union

    """Data Parsing"""
def parse_data(filename):
    result = [] # O(1)
    with open(filename, 'r') as f: # O(1)
        lines = f.readlines() # O(1)
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

def sick_patients(lab, gt_lt, value, lab_name):
    stat = lambda lab_value, ref_value: (gt_lt[0] == '>' and lab_value > ref_value) or\
                                        (gt_lt[0] == '<' and lab_value < ref_value) # 0(1)
    sick_list = [row[0] for row in labs[1:] if row[2] == lab_name and stat(float(row[3]), value)] # N * 0(1)
    sick_list = list(set(sick_list)) # 0(1)
    return sick_list
# 0(1) + N * 0(1) + 0(1)
# 0(N)

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
