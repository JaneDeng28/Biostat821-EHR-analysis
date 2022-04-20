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
    def __init__(
        self, PatientID: str, LabName: str, LabValue: float, LabUnits: str, LabDateTime: str
    ) -> None:
        self.PatientID = PatientID
        self.LabName = LabName
        self.LabValue = LabValue
        self.LabUnits = LabUnits
        self.LabDateTime = datetime.strptime(LabDateTime, "%Y-%m-%d %H:%M:%S.%f")


class Patient:
    def __init__(self, PatientID: str, Gender: str, DOB: str, Race: str) -> None:
        self.PatientID = PatientID
        self.Gender = Gender
        self.DOB = datetime.strptime(DOB, "%Y-%m-%d %H:%M:%S.%f")
        self.Race = Race
        self.Labs: List = []

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
    print(Patient("FA157FA5-F488-4884-BF87-E144630D595C") > 90.0)
