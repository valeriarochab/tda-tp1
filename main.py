import os
import sys
import heapq

partners = {}


def main():
    arguments = sys.argv[1:]
    n = int(arguments[0])
    file_name = arguments[1]

    if n <= 4:
        print("n debe ser mayor a 4")
        return

    get_partners(file_name)
    partners_list = create_heap()

    while len(partners.items()) >= 5:
        candidate = partners_list[0]
        print("len: ", len(partners.items()))
        print("candidate: ", candidate)
        if candidate[0] <= 3:
            del partners[candidate[1]]
            remove_partner(candidate[1])
            partners_list = create_heap()
        else:
            break

    show_result()


def get_partners(file_name):
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

            completed_partners = [0] * int(known_partners[-1])

            for x in known_partners:
                completed_partners[int(x) - 1] = 1

            partners[partner_number] = (partner_name, known_partners_length, completed_partners) # {'4': ('4', 'Lituania', 3, [0, 0, 0, 0, 1, 1, 1]),


def create_heap():
    partners_list = [(v[1], k) for k, v in partners.items()]
    heapq.heapify(partners_list)
    return partners_list


def remove_partner(partner_number):
    print("remove partner")
    for key, value in partners.items():
        print("key", key, "value", value)
        partner_name = value[0]
        known_partners_length = value[1]
        completed_partners = value[2]
        if int(partner_number) <= len(completed_partners) and completed_partners[int(partner_number) - 1] == 1:
            known_partners_length = known_partners_length - 1
            completed_partners[int(partner_number) - 1] = 0
            partners[key] = (partner_name, known_partners_length, completed_partners)


def show_result():
    print("show result: ", partners)
    for partner in partners.items():
        print(partner[0] + ", " + partner[1][0])


main()
