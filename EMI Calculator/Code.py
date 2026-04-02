import os

def parse_headers(header_line):
    return header_line.strip().split(',')


with open('loans3.txt') as f:
    file_lines = f.readlines()


def parse_values(data_line):
    values = []
    for item in data_line.strip().split(','):
        if item != '':
            values.append(float(item))
        else:
            values.append(0)
    return values


# TEST: Only remove # if you want to test parse_values function
# print(parse_values(file_lines[1]))
# print(parse_values(file_lines[2]))


def create_dict(values, headers):
    dict = {}
    for value, header in zip(values, headers):
        dict[header] = value
    return dict


# TEST: Only remove # if you want to test create_dict function
# print(create_dict(parse_values(file_lines[1]), parse_headers(file_lines[0])))
# print(create_dict(parse_values(file_lines[2]), parse_headers(file_lines[0])))


def read_csv(path):
    with open(path) as f:
        file_lines = f.readlines()
    header = parse_headers(file_lines[0])
    result = []
    for i in range(1, len(file_lines)):
        result.append(create_dict(parse_values(file_lines[i]), header))
    return result


# TEST: Only remove # if you want to test read_csv function
# dict_array = read_csv('loans3.txt')
# print(dict_array)


def loan_emi(amount, duration, rate, down_payment):
    try:
        emi = loan_amount * ((1 + rate) ** duration) / (((1 + rate) ** duration) - 1)
    except ZeroDivisionError:
        emi = loan_amount / duration
    return emi


# TEST: Only remove # if you want to test loan_emi function
# print(loan_emi(
#     parse_values(file_lines[1])[0],
#     parse_values(file_lines[1])[1],
#     parse_values(file_lines[1])[2],
#     parse_values(file_lines[1])[3]
# ))


def compute_emis(loans):
    final = []
    for loan in loans:
        emi = loan_emi(
            loan['amount'],
            loan['duration'],
            loan['rate'],
            loan['down_payment']
        )
        loan['emi'] = emi
        final.append(loan)
    return final


# TEST: Only remove # if you want to test compute_emis function
# dict_array = read_csv('loans3.txt')
# print(compute_emis(dict_array))


def final(src, out):
    with open(src) as file:
        file_lines = file.readlines()

    with open(out, 'w') as results:
        results.write('amount,duration,rate,down_payment,emi\n')

        for line in file_lines[1:]:
            values = parse_values(line)
            emi = loan_emi(values[0], values[1], values[2], values[3])
            results.write(f"{values[0]},{values[1]},{values[2]},{values[3]},{emi}\n")


final('loans1.txt', 'emi1.txt')
final('loans2.txt', 'emi2.txt')
final('loans3.txt', 'emi3.txt')
