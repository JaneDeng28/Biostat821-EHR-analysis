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

    def __init__(self, labfilename: List[str]) -> None:
            self.PatientID = labfilename[0]
            self.AdmissionID = labfilename[1]
            self.LabName = labfilename[2]
            self.LabValue = labfilename[3]
            self.LabUnits = labfilename[4]
            self.LabDateTime = datetime.strptime(labfilename[5], '%Y-%m-%d %H:%M:%S.%f')


class Patient:

    def __init__(self, patfilename: List[str]) -> None:
        self.PatientID = patfilename[0]
        self.gender = patfilename[1]
        self.DOB = datetime.strptime(patfilename[2], '%Y-%m-%d %H:%M:%S.%f')
        self.race = patfilename[3]
        self.marital = patfilename[4]
        self.language = patfilename[5]
        self.poverty = patfilename[6]

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

if __name__ == "__main__":
    print(Patient("FA157FA5-F488-4884-BF87-E144630D595C",patfilename="test_patient.txt") > 90.0)
