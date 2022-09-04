import os

partners = {}



def main(n, file_name):
    current_path = os.path.dirname(os.path.abspath(__file__))
    with open("{}/{}".format(current_path, file_name)) as fp:
        lines = fp.readlines()
        for line in lines:
            elements = line.split(",")
            partner_number = elements[0]
            partner_name = elements[1]
            known_partners = elements[2:]
            partners[partner_number] = (partner_name, known_partners)

    print(partners)

main(5, "test.txt")