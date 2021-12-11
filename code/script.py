from datetime import datetime, date


def covid_vaccine(vaccination_status_files, user_meta_file, output_file):
    vac_dict = {}
    user_dict = {}
    output = {}
    string = ""
    for f in vaccination_status_files:
        file = open(f)
        user_vac = file.read().split("\n")[1:-1]
        for x in user_vac:
            arr = x.split('\t')
            user = 0
            if not type(int(arr[0])) is int:
                TypeError("User should be integer")
            else:
                user = int(arr[0])
            vac = arr[1]
            v_date = datetime.strptime(arr[2], '%d-%m-%Y').date()
            # print(user, vac, date)
            if vac not in ['A', 'B', 'C']:
                continue
            if not date(2020, 2, 1) <= v_date <= date(2021, 12, 30):
                continue
            vac_dict[user] = vac
            # print(user, vac, v_date)

    file2 = open(user_meta_file)
    user_info = file2.read().split('\n')[1:-1]
    for x in user_info:
        arr = x.split('\t')
        user = 0
        if not type(int(arr[0])) is int:
            TypeError("User should be integer")
        else:
            user = int(arr[0])
        if user not in vac_dict:
            continue
        gender = arr[1]
        if gender not in ['M', 'F']:
            continue
        city = arr[2]
        state = arr[3]
        # print(user, gender, city, state, vac_dict[user])
        user_dict[user] = (city, state, vac_dict[user], gender)

    # print(vac_dict)
    for y in user_dict:
        if user_dict[y] in output:
            output[user_dict[y]] += 1
        else:
            output[user_dict[y]] = 1
        # print(user_dict[y][1])

    string = "city\tstate\tvaccine\tgender\tunique_vaccinated_people\n"
    for x in sorted(output):
        string += x[0] + '\t' + x[1] + '\t' + x[2] + '\t' + x[3] + '\t' + str(output[x])
        string += '\n'

    # print(string)
    file3 = open(output_file, 'x')
    file3.write(string)
