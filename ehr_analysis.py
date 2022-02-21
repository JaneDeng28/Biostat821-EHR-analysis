from datetime import datetime
def parse_data(filename):
    with open(filename) as table:
        return [line.replace('\n','').split('\t') for line in table][1:]

def num_older_than(age, patients):
    DOB = [patient[2] for patient in patients][1:]
    DOB = [datetime.strptime(patient, '%Y-%m-%d %H:%M:%S.%f') for patient in DOB]
    Today = datetime.now()
    diff = [round((Today - DOB).days / 365, 1) for patient in DOB]
    return len([patient for patient in diff if patient > age])  
    

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
    print(sick_patients(thatlab, gtlt, index, labs))
except:
    raise ValueError("Input shold follow the instruction")
    
print(sick_patients(thatlab, gtlt, index, labs))
print(len(sick_patients(labs, 'METABOLIC: ALBUMIN', '>', 5.9)))
