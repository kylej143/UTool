"""
Converts a tex file format table to Test Vector valid table.
"""
import os
import view


def convert(path: str):
    try:
        # validate path
        if path is None or not os.path.isfile(path):
            view.MessageBox("File Not Found")
            return Exception

        lst = []
        line_counter = 0
        with open(path, "r") as file:
            for line in file:
                line_counter += 1
                if line_counter != 2:
                    lst.append(line.replace("&", " ").replace("\\\\", "").replace("$", ""))
        file.close()

        with open(path, "w") as file:
            for line in lst:
                file.write("%s" % line)
        file.close()
        view.MessageBox("Success!")

    except Exception as e:
        view.MessageBox("Error has occurred while trying to convert the tex format file!")
