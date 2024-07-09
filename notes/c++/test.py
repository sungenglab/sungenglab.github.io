import re

def add_section_numbers(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    section_counts = [0] * 6  # To keep track of counts for headers from # to ######
    new_lines = []
    in_code_block = False

    header_pattern = re.compile(r'^(#+)\s*(\d+(\.\d+)*)?\s*(.*)$')

    for line in lines:
        if line.strip().startswith("```"):
            in_code_block = not in_code_block

        if not in_code_block:
            match = header_pattern.match(line)
            if match:
                hashes, old_number, _, title = match.groups()
                level = len(hashes) - 1

                # Increment the current level count
                section_counts[level] += 1
                # Reset counts for all lower levels
                for i in range(level + 1, len(section_counts)):
                    section_counts[i] = 0

                # Generate new section number
                new_number = '.'.join(str(section_counts[i]) for i in range(level + 1) if section_counts[i] > 0)

                # Construct the new header line with a trailing dot
                new_line = f"{hashes} {new_number}. {title}\n"
                new_lines.append(new_line)
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

if __name__ == "__main__":
    file_path = 'D:\Workspaces\MyBlog\SunGengBlog\SunGengHugoBlogSrc\content\\notes\C++\C++八股.md'  # Replace with your file path
    add_section_numbers(file_path)
