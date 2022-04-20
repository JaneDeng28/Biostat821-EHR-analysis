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

class Patient:
    def __init__(self, PatientID: str) -> None:
        self.patients = ehr_analysis.parse_patient("test_patient.txt")
        for patient in self.patients:
            if patient[0] == PatientID:
                self.ID = patient[0]
                self.Gender = patient[1]
                self.DOB = datetime.strptime(patient[2], "%Y-%m-%d %H:%M:%S.%f")
                self.Race = patient[3]
                self.MaritalStatus = patient[4]
                self.Language = patient[5]
                self.Poverty = patient[6]
 
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


class Lab:
    def __init__(self, PatientID: str, LabName: str, LabDateTime: datetime):
        self.labs = ehr_analysis.parse_lab("test_lab.txt")
        for lab in self.labs:
            if (
                PatientID == lab[0]
                and LabName == lab[2]
                and LabDateTime == datetime.strptime(lab[5], "%Y-%m-%d %H:%M:%S.%f")
            ):
                self.ID = lab[0]
                self.LabName = lab[2]
                self.LabValue = lab[3]
                self.LabUnits = lab[4]
                self.LabDateTime = datetime.strptime(lab[5], "%Y-%m-%d %H:%M:%S.%f")


if __name__ == "__main__":
    print(Patient("FA157FA5-F488-4884-BF87-E144630D595C") > 90.0)
