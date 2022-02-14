# Biostat821-EHR-analysis

This Python module provides several simple analytical function on some (synthetic) EHR data.
Example data:
*`PatientCorePopulatedTable.txt`, patient demographic data table
*`LabsCorePopulatedTable.txt` laboratory results table

End user guide:
* setup/installation instructions, including information about the expected input file formats

File need to be in .txt format

* API description: 

The system will ask user enter index age for num_older_than function, TypeError will happened if input is not integar.
The system will ask user enter index value for sick_patients function, TypeError will happened if input is not float.
The system will ask user enter lab name and comparsion symbol for sick_patients function, TypeError will happened if input is nuvalid.

* Examples
```python
>> pt = load_patients("PatientCorePopulatedTable.txt")
>> num_older_than(51.2, pt)
52
>> lt = labs_patients("PatientCorePopulatedTable.txt")
>> sick_patients(lt, 'METABOLIC: ALBUMIN', '>', 5.8)
'1A8791E3-A61C-455A-8DEE-763EB90C9B2C', '1', 'METABOLIC: ALBUMIN', '5.9', 'pg', '1992-06-30 03:50:11.777'
```

* Testing instructions

test_ehr_analysis.py is test functions using 'pytest' framework for functions in ehr_analysis.py
Any change of sample output should result in a failed test, all the test should be passed
