import os
from pathlib import Path
from urllib.parse import quote


"""
    Script to add create a markmap taking all files markdown and its subtitles
"""


def clear_map(path_file, flag_to_start="<!-- Map site start -->", flag_to_end="<!-- Map site end -->"): 
    """Replace old file with the content without link to download pdf

    Args:
        path_file (Path): File path to clean text generated automate
        flag_to_start (str): section inside to START the markdown where to put the map
        flag_to_end (str): section inside to END the markdown where to put the map
    """
    
    content = ""

    write= True
    
    with open(path_file, "r+") as md:
        print("Clear file: ", path_file)
        
        for line in md.readlines():
            if line.startswith(flag_to_start):
                write = False
            if line.startswith(flag_to_end):
                write = True
                continue
            
            if write:
                content += f'{line}'

    with open(path_file, "w+") as md:
        md.writelines(content)


def inject_map(file_path, content, **options):
    """Inject str markmap

    Args:
        file_path (Path): Full path document

        for header in section[key]:
            section_str += f"#{header}\n"
        section_str += "\n"
    return section_str
      content (str): All markmap to insert in file
        **options : ["flag_to_start"] || ["header"]
    """
    content_full = ""
    with open(file_path, "r") as md:
        for line in md.readlines():
            content_full += f'{line}'

            if line.find(options["flag_to_insert"]) >= 0:
                content_full += content

    with open(file_path, "w+") as md:
        md.writelines(content_full)


def build_section_markmap(section: dict):
    """Build all markmap with the content from markdown structure, and add a hash before to build the sequence

    Args:
        section (dict): structure from markdown header's sections

    Returns:
        str: All markmap content to insert
    """
    section_str = ""

    for key in section:
        for header in section[key]:
            section_str += f"#{header.strip()}\n"
        section_str += "\n"
    return section_str


def build_section_markmap_with_link(section: dict):
    """Build all markmap with the content from markdown structure, and add a hash before to build the sequence

    Args:
        section (dict): structure from markdown header's sections

    Returns:
        str: All markmap content to insert
    """
    def clean_accent(txt):
        a,b = 'áéíóúüñÁÉÍÓÚÜÑ','aeiouunAEIOUUN'
        trans = str.maketrans(a,b)
        return txt.translate(trans)

    def generate_sub_link(link):        
        return clean_accent(link.lower()).replace("#","").strip().replace(" ","-").replace("(","").replace(")","").replace(":","").lower()
    
    def generate_hash(header:str):
        return header.count("#") * "#"
        
    
    def generate_link(path:str):
        path = path.split("/")[-1].replace(".md","")
        return  quote(path)
        
    section_str = ""
    
    section_headers = section["structure"]
        
    for key in section_headers:
        for header in section_headers[key]:
            section_str += f'#{generate_hash(header)} [{header.replace("#","").strip()}]({generate_link(section["path"])}#{generate_sub_link(header)})\n'
            
        section_str += "\n"
    return section_str


def build_markmap_with_link(list_structure_header: dict, flag_to_start="<!-- Map site start -->", flag_to_end="<!-- Map site end -->"):
    """Build all content of markmap

    Args:
        list_structure_header (dict): All headers
        flag_to_start (str, optional): Flag to know where insert the map. Defaults to "<!-- Map site start -->".
        flag_to_end (str, optional): Flag to know where end the map. Defaults to "<!-- Map site end -->".

    Returns:
        str: All str of markmap of the folder
    """
    
    map_init = "```markmap"
    map_end = "\n```"

    content = f"\n{flag_to_start}\n{'<!-- AUTO GENERATED -->'}\n{map_init}\n"
    content += f'{list_structure_header["structure_index_title"]["h1"][0]}\n\n'

    for structure in list_structure_header["list_structure"]:
        content += build_section_markmap_with_link(structure)

    content += f'\n{map_end}\n{flag_to_end}\n'
    return content


def build_markmap(list_structure_header: dict, flag_to_start="<!-- Map site start -->", flag_to_end="<!-- Map site end -->"):
    """Build all content of markmap

    Args:
        list_structure_header (dict): All headers
        flag_to_start (str, optional): Flag to know where insert the map. Defaults to "<!-- Map site start -->".
        flag_to_end (str, optional): Flag to know where end the map. Defaults to "<!-- Map site end -->".

    Returns:
        str: All str of markmap of the folder
    """
    map_init = "```markmap"
    map_end = "\n```"

    content = f"\n{flag_to_start}\n{map_init}\n"
    content += f'{list_structure_header["structure_index_title"]["h1"][0]}\n\n'

    for structure in list_structure_header["list_structure"]:
        content += build_section_markmap(structure['structure'])

    content += f'\n{map_end}\n{"<!-- AUTO GENERATED -->"}\n{flag_to_end}\n'
    return content


def get_structure_without_hash(path_file):
    """Generate a dict with the structure of document, list of title and subtitles

    Args:
        path_file (Path): Path of file markdown

    Returns:
        dict: Structure with all title and subtitles, the key is h#
    """
    structure = {}

    with open(path_file, "r") as file:
        for line in file.readlines():
            if line.strip().startswith("#"):

                number_hash = len(line.split(" ")[0])

                new_line = line.replace("#" * number_hash, "").strip()

                if not structure.get(f"h{number_hash}"):
                    structure[f"h{number_hash}"] = [new_line]
                else:
                    structure[f"h{number_hash}"].append(new_line)

    return structure


def get_structure_with_hash(path_file):
    """Generate a dict with the structure of document, list of title and subtitles

    Args:
        path_file (Path): Path of file markdown

    Returns:
        dict: Structure with all title and subtitles, the key is h#
    """
    structure = {}

    with open(path_file, "r") as file:
        for line in file.readlines():
            if line.strip().startswith("#"):

                number_hash = len(line.split(" ")[0])

                new_line = line.strip()

                if not structure.get(f"h{number_hash}"):
                    structure[f"h{number_hash}"] = [new_line]
                else:
                    structure[f"h{number_hash}"].append(new_line)

    return structure


def get_all_md(path):
    """get alls files markdown from folder and subfolders

    Args:
        path (Path): path for to search files md

    Returns:
        list: markdown files's list
    """
    list_md = []

    for file in Path(path).iterdir():
        if file.is_dir():
            list_md += get_all_md(file)
        if file.is_file() and str(file).endswith(".md"):
            list_md.append(os.path.abspath(file))

    return sorted(list_md)


def get_all_md_from_folder(path):
    """get alls files markdown from folder

    Args:
        path (Path): path for to search files md

    Returns:
        list: markdown files's list
    """

    list_md = [
        os.path.abspath(file)
        for file in (Path(path).iterdir())
        if file.is_file() and str(file).endswith(".md")
    ]

    return sorted(list_md)


def get_paths_abs(base_dir, *args):
    """Generate a list of paths absolutes from base dir and all name of folders

    Args:
        base_dir (Path): Path base to generate path absolute, join base dir and folders

    Returns:
        List: List with all paths from folders
    """

    paths = [os.path.abspath(f"{base_dir}{os.path.sep}{path}") for path in args]

    return sorted(set(paths))


def get_all_folders(path):
    """Get all folders and subfolders from path

    Args:
        path (Path): Receive a path to search folders

    Returns:
        List: List of folders and sobfolders
    """
    list_dir = []
    for file in Path(os.path.abspath(path)).iterdir():
        if file.is_dir():
            list_dir.append(os.path.abspath(file))
            if len(get_all_folders(os.path.abspath(file))):
                list_dir += get_all_folders(os.path.abspath(file))

    if not (os.path.abspath(path) is list_dir):
        list_dir.append(os.path.abspath(path))

    return sorted(set(list_dir))


def clean_list_folder(list_complete: list, list_exclude: list):
    """Clear folders paths

    Args:
        list_complete (list): All paths to search files
        list_exclude (list): Paths to exclude from full list

    Returns:
        list: List purge with the paths
    """
    # delete all equals while have it
    for exclude in list_exclude:
        if exclude in list_complete:
            list_complete.remove(exclude)

    # create a list with paths with wildcard
    list_wildcard = [
        exclude.replace("/*", "") for exclude in list_exclude if exclude.count("*")
    ]

    for path in list_complete:
        for exclude in list_wildcard:
            if path.startswith(exclude):
                list_complete.remove(path)

    return sorted(list_complete)


def main():
    """Need to add in Markdown index.md a section with FLAG_TO_INSERT or SECCION_TO_INSERT, with this the script know where to insert all content
    
    """
    SECCION_TO_INSERT = "## Mapa del "
    FLAG_TO_INSERT = "<!-- Map site insert -->"
    FLAG_START = "<!-- Map site start -->"
    FLAG_END = "<!-- Map site end -->"

    PATH_TO_SEARCH = "../docs/"

    paths_excludes = get_paths_abs(
        PATH_TO_SEARCH,
        "icons",
        "img",
        "javascripts",
        "stylesheets",
        "extras/*",
    )

    for path in clean_list_folder(get_all_folders(PATH_TO_SEARCH), paths_excludes):
        file_path_index = ""
        markmap = ""
        list_structure_md = []
        structure_index_title = None
        for markdown in get_all_md_from_folder(path):
            if markdown.endswith("index.md"):
                file_path_index = markdown
                structure_index_title = get_structure_with_hash(markdown)
                continue

            list_structure_md.append({"path":markdown ,"structure":get_structure_with_hash(markdown)})

        if file_path_index:
            print(file_path_index)
            map_one = {
                "index_file_path": file_path_index,
                "list_structure": list_structure_md,
                "structure_index_title": structure_index_title,
                "base_dir": path
            }

            clear_map(file_path_index, flag_to_start=FLAG_START,
                      flag_to_end=FLAG_END)
            inject_map(
                file_path_index, 
                build_markmap_with_link(list_structure_header=map_one, flag_to_start=FLAG_START, flag_to_end=FLAG_END),
                flag_to_insert=FLAG_TO_INSERT)
        else:
            print("=============== no have index.md, path:",
                  path, "===============================")


if __name__ == "__main__":
    main()
