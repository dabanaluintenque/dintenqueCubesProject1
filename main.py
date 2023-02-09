# author: Dabana Intenque


# Database
from database import getDatabase
# API Data
from get_wufoo_API_data import get_wufoo_data


def get_wufoo_entries(data_entries: list, file_save=None):
    for entry in data_entries:
        for key, value in entry.items():
            print(f"{key}: {value}", file=file_save)
            print("\n_____________________________",
                  file=file_save)


def main():
    # return the data from the get_wufoo_data function
    data = get_wufoo_data()
    # initialize the data entries
    data1 = data['Entries']
    # save as a .txt file format with 'w' (write)
    file_to_save = open("dates.txt", 'w')
    get_wufoo_entries(data1, file_save=file_to_save)


if __name__ == '__main__':
    main()
    getDatabase()
