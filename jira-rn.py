import csv

# define your JIRA base url
base_url = "http://yourorg.atlassian.net/"


def categorize_jira_tickets():
    # Modify this text for input file prompt
    file_path = input("Enter the path to the Jira issues CSV file: ")

    # Initialize the HTML page code
    html_code = ""

    # Read the CSV file
    with open(file_path, 'r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader)  # Get header row

        # Initialize the categories
        whats_new_web = []
        resolved_issues_web = []
        whats_new_mobile_ios = []
        resolved_issues_mobile_ios = []
        whats_new_mobile_android = []
        resolved_issues_mobile_android = []

        # Categorize tickets based on the criteria
        for row in reader:
            # Refer JIRA issue type in .csv file and modify the columns
            ticket_type = row[4]
            ticket_releasenote = row[0]
            ticket_assignee = row[14]
            ticket_key = row[1]

            if "MOB" not in ticket_key:
                if ticket_type == "Bug":
                    resolved_issues_web.append([ticket_key, ticket_releasenote, ticket_assignee])
                else:
                    whats_new_web.append([ticket_key, ticket_releasenote, ticket_assignee])
            else:
                if "[iOS]" in ticket_releasenote:
                    if ticket_type == "Bug":
                        resolved_issues_mobile_ios.append([ticket_key, ticket_releasenote, ticket_assignee])
                    else:
                        whats_new_mobile_ios.append([ticket_key, ticket_releasenote, ticket_assignee])
                elif "[Android]" in ticket_releasenote:
                    if ticket_type == "Bug":
                        resolved_issues_mobile_android.append([ticket_key, ticket_releasenote, ticket_assignee])
                    else:
                        whats_new_mobile_android.append([ticket_key, ticket_releasenote, ticket_assignee])

        # Generate Notion page code for What's New for Web
        html_code += "<h2>What's New and Enhancements-Web</h2>\n"
        html_code += "<toggle>\n"
        html_code += "<table>\n"
        html_code += "<tr><th>Jira ID</th><th>Release Note</th><th>Assignee</th></tr>\n"
        for ticket in whats_new_web:
            issue_url = base_url + ticket[0]
            html_code += f'<tr><td><a href="{issue_url}">{ticket[0]}</a></td><td>{ticket[1]}</td><td>{ticket[2]}</td></tr>\n'
        html_code += "</table>\n"
        html_code += "</toggle>\n"

        # Generate Notion page code for Resolved Issues for Web
        html_code += "<h2>Resolved Issues-Web</h2>\n"
        html_code += "<toggle>\n"
        html_code += "<table>\n"
        html_code += "<tr><th>Jira ID</th><th>Release Note</th><th>Assignee</th></tr>\n"
        for ticket in resolved_issues_web:
            issue_url = base_url + ticket[0]
            html_code += f'<tr><td><a href="{issue_url}">{ticket[0]}</a></td><td>{ticket[1]}</td><td>{ticket[2]}</td></tr>\n'
        html_code += "</table>\n"
        html_code += "</toggle>\n"

        # Generate Notion page code for What's New for Mobile (iOS)
        html_code += "<h2>What's New and Enhancements-Mobile(iOS)</h2>\n"
        html_code += "<toggle>\n"
        html_code += "<table>\n"
        html_code += "<tr><th>Jira ID</th><th>Release Note</th><th>Assignee</th></tr>\n"
        for ticket in whats_new_mobile_ios:
            issue_url = base_url + ticket[0]
            html_code += f'<tr><td><a href="{issue_url}">{ticket[0]}</a></td><td>{ticket[1]}</td><td>{ticket[2]}</td></tr>\n'
        html_code += "</table>\n"
        html_code += "</toggle>\n"

        # Generate Notion page code for Resolved Issues for Mobile (iOS)
        html_code += "<h2>Resolved Issues-Mobile(iOS)</h2>\n"
        html_code += "<toggle>\n"
        html_code += "<table>\n"
        html_code += "<tr><th>Jira ID</th><th>Release Note</th><th>Assignee</th></tr>\n"
        for ticket in resolved_issues_mobile_ios:
            issue_url = base_url + ticket[0]
            html_code += f'<tr><td><a href="{issue_url}">{ticket[0]}</a></td><td>{ticket[1]}</td><td>{ticket[2]}</td></tr>\n'
        html_code += "</table>\n"
        html_code += "</toggle>\n"

        # Generate Notion page code for What's New for Mobile (Android)
        html_code += "<h2>What's New and Enhancements- Mobile(Android)</h2>\n"
        html_code += "<toggle>\n"
        html_code += "<table>\n"
        html_code += "<tr><th>Jira ID</th><th>Release Note</th><th>Assignee</th></tr>\n"
        for ticket in whats_new_mobile_android:
            issue_url = base_url + ticket[0]
            html_code += f'<tr><td><a href="{issue_url}">{ticket[0]}</a></td><td>{ticket[1]}</td><td>{ticket[2]}</td></tr>\n'
        html_code += "</table>\n"
        html_code += "</toggle>\n"

        # Generate Notion page code for Resolved Issues for Mobile (Android)
        html_code += "<h2>Resolved Issues-Mobile(Android)</h2>\n"
        html_code += "<toggle>\n"
        html_code += "<table>\n"
        html_code += "<tr><th>Jira ID</th><th>Release Note</th><th>Assignee</th></tr>\n"
        for ticket in resolved_issues_mobile_android:
            issue_url = base_url + ticket[0]
            html_code += f'<tr><td><a href="{issue_url}">{ticket[0]}</a></td><td>{ticket[1]}</td><td>{ticket[2]}</td></tr>\n'
        html_code += "</table>\n"
        html_code += "</toggle>\n"

    # Save the Notion page code in a result file
    save_path = input("Enter the path to save the result file: ")
    with open(save_path, 'w') as result_file:
        result_file.write(html_code)

    print("\nCongratulations, your release note is successfully generated!")


# Run the categorization function
categorize_jira_tickets()
