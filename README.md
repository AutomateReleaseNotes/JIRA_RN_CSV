# JIRA Release Note Generator 🚀

This project aims to simplify the process of generating release notes in .html format using data from a CSV file obtained through JIRA. By following this guide, you'll be able to filter JIRA issues, extract relevant information, and create organized release notes for different subcategories.

## Introduction
This project is designed to generate release notes by using a CSV file sourced from the Atlassian's JIRA platform. The release notes will be generated in .html format, providing an easily readable and shareable format for your team or stakeholders.

## Input and Output Formats

<div align="center">

| I/O   | Value|
| -------- | ------- |
| Input  | .csv  |
| Output |.html    |
| Script Language Type | Python|


</div>


## Prerequisites

Before you begin, ensure you have the following items are considered.

1. **Custom Field for Release Notes**: Set up a custom field in JIRA to capture the release note content for each issue. Contact your JIRA administrator to create a custom field in JIRA for release notes. Say the field name as **Release Note**. 
To add a custom field in JIRA, refer [here](https://support.atlassian.com/jira-cloud-administration/docs/create-a-custom-field/).

2. **Custom JIRA Query**: Prepare a custom search query in JIRA to filter the release note issues required for a release. To create a custom JIRA query, refer [here](https://support.atlassian.com/jira-software-cloud/docs/manage-custom-filters-in-team-managed-projects/).

3. **CSV File from JIRA**: Obtain a CSV file from the JIRA portal containing the necessary issue details. While downloading a CSV file, select Export CSV (all fields)

<div align="center">
<img src="https://user-images.githubusercontent.com/3941590/261223825-415d8715-2a75-4942-a8e7-56fbc1581211.png" width="200px" height="300px">
</div>

4. **Query Parameters**: Define query parameters to categorise issues into subcategories such as Web, Mobile Platforms, What's New, Fixed Issues, and Known Issues. Note down the sample project Issue keys of JIRA as follows (the parameters can differ based on your needs

<div align="center">

| Type   | Sample JIRA Key |
| -------- | ------- |
| Web  | WEB  |
| Mobile |MOB    |
| Issue Type | Bug|
| Status| Open or Close|
| What's New    | Rest of Issues    |

</div>

5. **Python Environment**: Install Python and a code editor such as PyCharm. For detailed tutorial, refer [here](https://www.guru99.com/how-to-install-python.html).

6. **Basic Python Knowledge**: A fundamental understanding of Python coding concepts will be beneficial.

## Configuration Steps

Follow these steps to configure and utilize the JIRA Release Note Generator:

1. **Create a project in Pycharm**: Create a project in Pycharm and add a suitable name for your project. To know the detailed steps, refer [here](https://www.jetbrains.com/help/pycharm/creating-empty-project.html).

2. **Create a python file** : Create a python file in the newly created project. Say: ***jira-rn.py***

3. **Copy the code**: Copy the code given in ***jira-rn.py***.

4. **Update the Release Note**: Update the release note field in the all the JIRA issues filtered in your release notes query. **This step is important before generation of release note.**

5. **Download CSV file from JIRA and copy its file path**: Download the CSV file from JIRA. Copy the absolute path of the .csv file.

6. **Map the Fields of CSV in Python file**: Utilize the query parameters to categorize the filtered issues into subcategories such as Web, Mobile Platforms, What's New, Fixed Issues, and Known Issues.
In the CSV file, note down the following columns and their column numbers. In JIRA the column numbers starts from 0. The column number given here is for reference and actual columns vary in your instance.

<div align="center">
   
| Column   | Column Number |
| -------- | ------- |
| Summary |0    |
| Issue Key| 1|
| Issue Type  | 4  |
| Project Key| 6|
|Status| 5|
| Release Note    | May vary   |
|Assignee|14|

</div>

Modify the column numbers starting from **line 27**.

7. **Execute the python file**: Run the python file.

8. **Enter the path of the CSV file**: Enter the path of the .csv file.

9. **Enter the name and path of the output CSV file**: Enter the desired path of the output file with its name and extension as .html.
   
10. **Open the generated file**: Open the generated .html release notes in a web browser to review the outcome. 

11. **Customize the Output**: Customize the output forms based on your authoring tool such as .xml, .html, etc.

## Sample Generated Output

## What's New and Enhancements-Web

| Jira ID | Release Note | Assignee |
| --- | --- | --- |
|  |  |  |

## Resolved Issues-Web

| Jira ID | Release Note | Assignee |
| --- | --- | --- |
|  |  |  |

## What's New and Enhancements-Mobile(iOS)

| Jira ID | Release Note | Assignee |
| --- | --- | --- |
|  |  |  |

## Resolved Issues-Mobile(iOS)

| Jira ID | Release Note | Assignee |
| --- | --- | --- |
|  |  |  |

## What's New and Enhancements- Mobile(Android)

| Jira ID | Release Note | Assignee |
| --- | --- | --- |
|  |  |  |

## Resolved Issues-Mobile(Android)

| Jira ID | Release Note | Assignee |
| --- | --- | --- |
|  |  |  |

## Conclusion

By following these steps, you can automate the process of generating release notes using a CSV file sourced from JIRA.

Feel free to customize and expand upon this project to suit your specific requirements. If you encounter any issues or have suggestions for improvement, please don't hesitate to raise them in the project's GitHub repository. 

Happy documenting! 📝🌟


**Author**: **Balaji Jayaraman**

**LinkedIn Profile**: https://www.linkedin.com/in/balajijayaramantechwriter/
