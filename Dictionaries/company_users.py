command = input()
companies = {}

while command != 'End':
    info = command.split(" -> ")
    company_name = info[0]
    id = info[1]

    if company_name not in companies:
        companies[company_name] = []

    if id not in companies[company_name]:
        companies[company_name].append(id)

    command = input()

for company, empl_id in companies.items():
    print(company)
    for employee in empl_id:
        print(f"-- {employee}")



