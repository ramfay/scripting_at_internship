import csv


def main():
    names = load_names()
    write_script(names)


def load_names():
    old_names = open("oldnames.csv", "r")
    delimit_file = csv.reader(old_names, delimiter=",")
    stored_names = []
    for line in delimit_file:
        stored_names.append(line)
    return stored_names


def write_script(names):
    write_new_names = open("thescript.txt", "w")
    for name in names:
        print("Set-Mailbox \"{}\" -DisplayName \"{}\"".format(name[0], name[1]), file=write_new_names)
    write_new_names.close()

main()
