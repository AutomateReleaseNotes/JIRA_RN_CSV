# JIRA Release Note Generator 🚀

The aim of this project is to create release notes by extracting issues from JIRA via a .CSV file. When the release note descriptions are added in JIRA, the .CSV file contains the release note descriptions of the issues that belongs to a release. This helps to ensure consistent output files and automate the routine tasks involved in creating release notes.

## Input and Output Specifications

Input File : .csv file 
Output File: .html file
Script Language: Python

## Prerequisites

1. **Custom Field for Release Notes**: Add a custom field in JIRA to capture the release note content for each issue. Contact your JIRA administrator to create a custom field named **Release Note** in JIRA.
To add a custom field in JIRA, refer [here](https://support.atlassian.com/jira-cloud-administration/docs/create-a-custom-field/).

2. **Custom JIRA Query**: Prepare a custom search query in JIRA to filter the issues ready to be released. To create a custom JIRA query, refer [here](https://support.atlassian.com/jira-software-cloud/docs/manage-custom-filters-in-team-managed-projects/).

3. **CSV File from JIRA**: Download a CSV file from JIRA using Export option. While downloading a CSV file, select Export CSV (all fields)

<div align="center">
<img src="https://user-images.githubusercontent.com/3941590/261223825-415d8715-2a75-4942-a8e7-56fbc1581211.png" width="200px" height="300px">
</div>

4. **Query Parameters**: Define query parameters to categorise issues into subcategories such as Web, Mobile Platforms, What's New, Fixed Issues, and Known Issues. Note down the sample project Issue keys of JIRA as follows Note: The parameters can differ based on your needs.

<div align="center">

| Type   | Sample JIRA Key |
| -------- | ------- |
| Web  | WEB  |
| Mobile |MOB    |
| Issue Type | Bug|
| Status| Open or Close|
| What's New    | Rest of Issues    |

</div>

5. **Python Environment**: Install Python and a code editor such as PyCharm to execute Python files. You can use any Python editor per your preferences. For detailed tutorial, refer [here](https://www.guru99.com/how-to-install-python.html).

6. **Basic Python Knowledge**: A fundamental understanding of Python code will be preferrable. This helps you to modify the code for your input and output specifications.

## Configuration Steps

Follow these steps to generate .html release notes from JIRA's .CSV export file

1. **Create a project in Pycharm**: Create a project in Pycharm and add a suitable name for your project. To know the detailed steps, refer [here](https://www.jetbrains.com/help/pycharm/creating-empty-project.html).

2. **Create a python file** : Create a python file in the newly created project. Say: ***jira-rn.py***

3. **Copy the code**: Copy the code given in ***jira-rn.py***.

4. **Update the Release Note**: Update the release note field in the all the JIRA issues filtered in your release notes query. **This step is an important step before generation of release note.**

5. **Download CSV file from JIRA and copy its file path**: Download the CSV file from JIRA. Copy the absolute path of the .csv file.

6. **Map the Fields of CSV in Python file**: Utilize the query parameters to categorize the filtered issues into subcategories such as Web, Mobile Platforms, What's New, Fixed Issues, and Known Issues.
In the CSV file, note down the following columns and their column numbers. In JIRA the column numbers starts from 0. **The column number given here is for reference and actual columns vary in your instance**.

<div align="center">
   
| Column   | Column Number |
| -------- | ------- |
| Summary |0    |
| Issue Key| 1|
| Issue Type  | 4  |
| Project Key| 6|
|Status| 5|
| Release Note    | Refer in your .csv file   |
|Assignee|14|

</div>

Modify the column numbers accordingly in the Python code starting from **line 27**.

7. **Run the python file**: Run the Python file.

8. **Enter the path of the CSV file**: Enter the path of the .csv file.

9. **Enter the name and path of the output CSV file**: Enter the desired path of the output file with a file name and extension as .html.
   
10. **Open the generated file**: Open the generated .html release notes in a web browser to review the outcome. 

11. **Customize the Output**: Customize the output forms based on your authoring tool such as .xml, .html, etc.

## Sample Output

https://github.com/AutomateReleaseNotes/JIRA_RN_CSV/blob/main/Sample_Output_RN.html

## Conclusion

By following these steps, you can start automating the release note genertion from the JIRA. To fully automate the process, the input and output specifications needs to be modified as per your desired formats.

To send your suggestions and feedbacks, contact me through LinkedIn.

**Author**: **Balaji Jayaraman**

**LinkedIn Profile**: https://www.linkedin.com/in/balajijayaramantechwriter/
