import ehr_analysis
from datetime import datetime
from typing import List

"""
At minimum you should end up with:

* a Patient class with:
  * instance attributes for gender, DOB, race, etc.
  * a [property](https://docs.python.org/3/library/functions.html#property) called `age`
* a Lab class with:
  * instance attributes for value, units, etc.

"""


class Lab:

    def __init__(self, PatientID: str, LabName: str, LabDateTime: str, labfilename: List[str]):
        self.lab = ehr_analysis.parse_lab(labfilename)
        for row in self.lab:
            if PatientID == row[0] and LabName == row[2] and LabDateTime == datetime.strptime(row[5], '%Y-%m-%d %H:%M:%S.%f'):
                self.PatientID = row[0]
                self.LabName = row[2]
                self.LabValue = row[3]
                self.LabUnits = row[4]
                self.LabDateTime = datetime.strptime(row[5], '%Y-%m-%d %H:%M:%S.%f')


class Patient:

    def __init__(self, PatientID: str, patfilename: List[str]):
        self.patient = ehr_analysis.parse_patient(patfilename)
        for row in self.patient:
            if row[0] == PatientID:
                self.PatientID = row[0]
                self.gender = row[1]
                self.DOB = datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S.%f')
                self.race = row[3]
                self.marital = row[4]
                self.language = row[5]
                self.poverty = row[6]

    @property
    def age(self) -> float:
        return round((datetime.now() - self.DOB).days / 365, 1)

    def __lt__(self, other: float):
        if isinstance(other, float):
            return self.age < other
        if isinstance(other, self.patients):
            return self.age < other.age

    def __gt__(self, other: float):
        if isinstance(other, float):
            return self.age > other
        if isinstance(other, self.patients):
            return self.age > other.age

def build_patient(filname:str) -> List[Patient]:
    pat = []
    with open(filname) as file:
        for row in file.readlines()[1:]:
            pat.append(Patient(row.split("\t")))
    return pat

def build_lab(filname:str) -> List[Lab]:
    lab = []
    with open(filname) as file:
        for row in file.readlines()[1:]:
            lab.append(Patient(row.split("\t")))
    return lab

if __name__ == "__main__":
    print(Patient("FA157FA5-F488-4884-BF87-E144630D595C",patfilename="test_patient.txt") > 90.0)
