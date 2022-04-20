from datetime import datetime
import sqlite3


def parse_data(filename):
    with open(filename) as table:
        return [line.replace("\n", "").split("\t") for line in table][1:]


class Patient:
    global patients
    patients = parse_data(
        "/Users/jane/2022/SP2022/BIOSTAT821/ehr-project/PatientCorePopulatedTable.txt"
    )

    def __init__(self, patientID):
        PATDB = sqlite3.connect(
            "/Users/jane/2022/SP2022/BIOSTAT821/ehr-project/patient.db"
        )
        cursor = PATDB.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS PATIENT(
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
        for row in patients:
            cursor.execute(
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
        cursor.execute("CREATE UNIQUE INDEX IF NOT EXISTS idx_id ON PATIENT (PATID)")
        cursor.execute(
            "SELECT * FROM PATIENT INDEXED BY idx_id WHERE PATID=?", (patientID,)
        )
        rows = cursor.fetchall()
        for row in rows:
            print(row)


class Observation:
    global labs
    labs = parse_data(
        "/Users/jane/2022/SP2022/BIOSTAT821/ehr-project/LabsCorePopulatedTable.txt"
    )

    def __init__(self, patientID):
        labdb = sqlite3.connect("/Users/jane/2022/SP2022/BIOSTAT821/ehr-project/lab.db")
        cursor = labdb.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS LAB(
            PATID TEXT NOT NULL,
            NAME TEXT NOT NULL,
            VALUE NUMERIC,
            UNIT TEXT NOT NULL,
            ORDER_TIME TIMESTAMP
            )
        """
        )
        for row in labs:
            cursor.execute(
                "INSERT OR REPLACE INTO Labs (PATID, NAME, VALUE, UNIT, ORDER_TIME) VALUES (?,?,?,?,?)",
                (
                    row[0],
                    row[2],
                    row[3],
                    row[4],
                    datetime.strptime(row[5], "%Y-%m-%d %H:%M:%S.%f"),
                ),
            )
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_id ON LAB (PATID)")
        cursor.execute(
            "SELECT * FROM LAB INDEXED BY idx_id WHERE PATID = ?", (patientID,)
        )
        rows = cursor.fetchall()
        for row in rows:
            print(row)


if __name__ == "__main__":
    Patient("6E70D84D-C75F-477C-BC37-9177C3698C66")
    Observation("6E70D84D-C75F-477C-BC37-9177C3698C66")
