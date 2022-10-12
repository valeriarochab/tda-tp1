import os
import sys

partners = {}


def main():
    arguments = sys.argv[1:]
    n = int(arguments[0])
    file_name = arguments[1]

    if n <= 4:
        print("n debe ser mayor a 4")
        return

    get_partners(file_name, n)

    for x in range(n):
        min = get_min()
        known_partners = min[2]
        partner_number = min[0]
        if known_partners < 4:
            remove_partner(partner_number)
        else:
            break

    show_result()


def get_min():
    return min(partners.values(), key=lambda x: x[2])


def get_partners(file_name, n):
    current_path = os.path.dirname(os.path.abspath(__file__))
    with open("{}/{}".format(current_path, file_name)) as fp:
        lines = fp.readlines()
        for line in lines:
            line = line.replace("\n", "")
            elements = line.split(",")
            partner_number = elements[0]
            partner_name = elements[1]
            known_partners = elements[2:]
            known_partners_length = len(known_partners)

            completed_partners = [0] * int(n)
            for x in known_partners:
                completed_partners[int(x) - 1] = 1

            partners[partner_number] = (
                partner_number, partner_name, known_partners_length, completed_partners)


def remove_partner(number):
    del partners[number]
    for key, value in partners.items():
        partner_number = value[0]
        partner_name = value[1]
        known_partners_length = value[2]
        completed_partners = value[3]
        if completed_partners[int(number) - 1] == 1:
            known_partners_length = known_partners_length - 1
            completed_partners[int(number) - 1] = 0
            partners[key] = (partner_number, partner_name, known_partners_length, completed_partners)


def show_result():
    if len(list(partners.items())) == 0:
        print("Ningun socio puede asistir al evento.")
    else:
        for partner in partners.items():
            print(partner[0] + ", " + partner[1][1])


main()
