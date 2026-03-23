import os


def create_file(path, content=""):
    if os.path.isdir(path):
        return
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def parse_structure(structure_text):
    lines = structure_text.splitlines()
    paths = []
    stack = []

    for line in lines:
        if not line.strip():
            continue

        if "├──" in line or "└──" in line:
            marker = "├──" if "├──" in line else "└──"
            prefix = line[: line.index(marker)]
            # Each │ character = one extra level of depth
            depth = prefix.count("│") + 1
            name = line[line.index(marker) + 3 :].strip().rstrip("/")
        else:
            # Root folder line (no tree symbols)
            depth = 0
            name = line.strip().rstrip("/")

        if not name:
            continue

        stack = stack[:depth]
        stack.append(name)
        paths.append(list(stack))

    return paths


def get_starter_content(name):
    if name.endswith(".py"):
        return "# Python file\n"
    elif name.endswith(".jsx"):
        base = name.replace(".jsx", "")
        return f"export default function {base}() {{\n  return <div>{base}</div>;\n}}\n"
    elif name.endswith(".js"):
        return "// JS file\n"
    elif name.endswith(".html"):
        return "<!DOCTYPE html>\n<html lang='en'><head><meta charset='UTF-8'/><title>Project</title></head><body></body></html>\n"
    elif name.endswith(".css"):
        return "/* CSS */\n"
    elif name.endswith(".md"):
        return "# Project\n\nAdd your documentation here.\n"
    elif name.endswith(".json"):
        return "{}\n"
    elif name.endswith(".txt"):
        return ""
    else:
        return ""


def create_project(base_path, structure_text):
    paths = parse_structure(structure_text)

    if not paths:
        print("❌ Invalid structure")
        return

    root_folder = paths[0][0]
    project_root = os.path.join(base_path, root_folder)

    os.makedirs(project_root, exist_ok=True)
    print(f"\n📁 Creating project at: {project_root}\n")

    for path_parts in paths:
        if path_parts == [root_folder]:
            continue

        relative_parts = path_parts[1:]
        full_path = os.path.join(project_root, *relative_parts)
        name = path_parts[-1]

        # A name with a dot (and not ending in dot) = file
        is_file = "." in name and not name.endswith(".")

        if is_file:
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            content = get_starter_content(name)
            create_file(full_path, content)
            print(f"  📄 {os.path.join(*relative_parts)}")
        else:
            os.makedirs(full_path, exist_ok=True)
            print(f"  📂 {os.path.join(*relative_parts)}/")

    print(f"\n✅ Project created successfully at:\n   {project_root}")


if __name__ == "__main__":
    base_path = input("Enter base path (e.g. D:\\Projects): ").strip()

    print("\nPaste your project structure (press ENTER twice to finish):\n")

    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    structure_text = "\n".join(lines)
    create_project(base_path, structure_text)