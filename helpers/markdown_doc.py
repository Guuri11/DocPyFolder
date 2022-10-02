from mdutils import MdUtils

def package_json_md(package_json, file_name, title):
    mdFile = MdUtils(file_name=file_name,title=title)
    for key, value in package_json.items():
        if "dependencies" in key.lower():
            mdFile.new_header(level=2, title=str(key).capitalize(), add_table_of_contents="n")
            list_of_strings = ["Package", "Version"]
            for dependency_key, dependency_value in value.items():
                list_of_strings.extend([dependency_key, dependency_value])
            mdFile.new_line()
            mdFile.new_table(columns=2, rows=len(value.items()) + 1, text=list_of_strings, text_align='center')
        else:
            mdFile.new_header(level=2, title=str(key).capitalize(), add_table_of_contents="n")
            mdFile.new_paragraph(str(value))
    mdFile.create_md_file()