class table():
    # spaces = row spaces
    # headers = row titles
    def get_line_length(headers: list, spaces: list):
        # under the first row is a ---- line (length of it)
        line_length = 2  # two for the "| " character
        for element in headers:
            line_length += int(spaces[headers.index(element)])
            line_length += 3  # three for the " | "
        return line_length - 1

    def print_table_spliter(headers: list, spaces: list):
        # under the first row is a ---- line
        print(table.get_line_length(headers, spaces) * "-")

    def print_table_head(headers: list, spaces: list):
        # EXAMPLE
        # | ID   | First Name      | Last Name       |
        # --------------------------------------------

        header_string = "| "
        for element in headers:
            header_string += str(element)
            header_string += (int(spaces[headers.index(element)]) - len(str(element))) * " "
            header_string += " | "
        print(header_string)

    def print_table_contents(spaces: list, row: list):
        # EXAMPLE
        # | ID   | First Name      | Last Name       |  (not printed in this funtion)
        # --------------------------------------------  (not printed in this funtion)
        # | 1    | 89908           | 223fdisoj       |
        # | 2    | gafijopi        | NAME            |
        # | 101  | asgabas         | 25543545        |
        # | 102  | e252345         | 24554           |

        end_string = "| "
        for element in row:
            end_string += str(element)
            end_string += (int(spaces[row.index(element)]) - len(str(element))) * " "
            end_string += " | "
        print(end_string)


if __name__ == '__main__':
    headers = ["ID", "First Name", "Last Name"]
    spaces = [4, 16, 16]
    table.print_table_head(headers, spaces)
    table.print_table_spliter(headers, spaces)  # spliter
    return_values = [[0, "Hi", "Nick"], [1, "hi", "fe"]]
    for person in return_values:
        table.print_table_contents(spaces, person)