from datetime import datetime
from typing import List
import sqlite3
import ehr_analysis

"""
patlocation = "/Users/jane/2022/SP2022/BIOSTAT821/ehr-project/patient.db"
lablocation = "/Users/jane/2022/SP2022/BIOSTAT821/ehr-project/lab.db"
"""

class Patient:

    def __init__(self, PatientID:str, PATDB_location:str, patfilename:List[str]) -> None:
        self.patient = ehr_analysis.parse_patient(patfilename)
        self.PATDB = sqlite3.connect(
            PATDB_location,
            detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES,
        )
        self.cursor = self.PATDB.cursor()
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS PATIENT(
            PATID TEXT PRIMARY KEY,
            GENDER TEXT NOT NULL,
            DOB TIMESTAMP,
            RACE TEXT NOT NULL,
            MARTIAL TEXT NOT NULL,
            LANGUAGE TEXT NOT NULL,
            PERCT_BELOW_PROVERTY NUMERIC
            )
        """
        )
        for row in self.patient:
            self.cursor.execute(
                "INSERT OR REPLACE INTO PATIENT (PATID, GENDER, DOB, RACE, MARITAL, LANGUAGE, PERCT_BELOW_PROVERTY) VALUES (?,?,?,?,?,?,?)",
                (
                    row[0],
                    row[1],
                    datetime.strptime(row[2], "%Y-%m-%d %H:%M:%S.%f"),
                    row[3],
                    row[4],
                    row[5],
                    row[6],
                ),
            )
        self.cursor.execute(
            "CREATE UNIQUE INDEX IF NOT EXISTS idx_id ON PATIENT (PATID)"
        )
        self.cursor.execute(
            "SELECT * FROM PATIENT INDEXED BY idx_id WHERE PATID=?", (PatientID,)
        )
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)


class Lab:

    def __init__(self, PatientID:str, LABDB_location:str, labfilename:List[str]) -> None:

        self.lab = ehr_analysis.parse_patient(labfilename)
        self.LABDB = sqlite3.connect(
            LABDB_location,
            detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES,
        )
        self.cursor = self.LABDB.cursor()
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS LAB(
            PATID TEXT NOT NULL,
            NAME TEXT NOT NULL,
            VALUE NUMERIC,
            UNIT TEXT NOT NULL,
            ORDER_TIME TIMESTAMP
            )
        """
        )
        for row in self.lab:
            self.cursor.execute(
                "INSERT OR REPLACE INTO Labs (PATID, NAME, VALUE, UNIT, ORDER_TIME) VALUES (?,?,?,?,?)",
                (
                    row[0],
                    row[2],
                    row[3],
                    row[4],
                    datetime.strptime(row[5], "%Y-%m-%d %H:%M:%S.%f"),
                ),
            )
        self.cursor.execute("CREATE INDEX IF NOT EXISTS idx_id ON LAB (PATID)")
        self.cursor.execute(
            "SELECT * FROM LAB INDEXED BY idx_id WHERE PATID = ?", (PatientID,)
        )
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)


if __name__ == "__main__":
    Patient("FB2ABB23-C9D0-4D09-8464-49BF0B982F0F")
    Lab("1A8791E3-A61C-455A-8DEE-763EB90C9B2C")
