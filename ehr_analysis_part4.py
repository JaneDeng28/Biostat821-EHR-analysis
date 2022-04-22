from datetime import datetime
import sqlite3
import ehr_analysis

class Patient:
    def __init__(self, patientID, PATDB_location, filename):
        self.patient = ehr_analysis.parse_patient(filename)
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
            "SELECT * FROM PATIENT INDEXED BY idx_id WHERE PATID=?", (patientID,)
        )
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)


class Lab:
    def __init__(self, patientID, LABDB_location, filename):

        self.lab = ehr_analysis.parse_patient(filename)
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
            "SELECT * FROM LAB INDEXED BY idx_id WHERE PATID = ?", (patientID,)
        )
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)


if __name__ == "__main__":
    Patient("6E70D84D-C75F-477C-BC37-9177C3698C66")
    Lab("6E70D84D-C75F-477C-BC37-9177C3698C66")