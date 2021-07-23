#!/usr/bin/env python3
import os
import json

import urllib.request
import shutil
import urllib.parse


version = "1.1.0"
HTML_URL = f"https://crystal-lang.org/api/{version}/"
URL = f"https://crystal-lang.org/api/{version}/index.json"

# download and read from local
local_json = "/tmp/cr.json"
if not os.path.exists(local_json):
    with urllib.request.urlopen(URL) as f:
        with open(local_json, "wb") as out:
            shutil.copyfileobj(f, out)

with open(local_json) as f:
    data = json.load(f)

prog = data["program"]
types = prog["types"]


def list_modules():
    for idx, t in enumerate(types, start=1):
        print(idx, t["name"])


def find_module(module_name):

    for t in types:
        if module_name.lower() == t["name"].lower():
            return t


def find_method(module, tname, html=False):
    ms = module["class_methods"]
    found = False
    for m in ms + module["instance_methods"]:
        # print(m)
        name = m["name"]
        if name.lower() == tname.lower():
            found = True

            print("Signature:", m["html_id"])
            if m["doc"]:
                print("  ", m["doc"])
                print("=" * 30)

            if html:
                full_url = urllib.parse.urljoin(HTML_URL, module["path"])
                full_url = f"{full_url}#{m['html_id']}"

                print(m["name"], full_url)
                print(f"Opening {full_url}")
                import webbrowser
                webbrowser.open_new_tab(full_url)

    if found:
        return

    for t in module["types"]:
        find_method(t, tname, html)


def find_type(module, tname, html=False):
    for t in module["types"]:
        fullname = t["full_name"]
        if fullname.lower() == tname.lower():
            parent = module["full_name"]
            print(f"{fullname} of {parent}")

            full_url = urllib.parse.urljoin(HTML_URL, t["path"])
            print(t["full_name"], full_url)
            if html:
                print(f"Opening {full_url}")
                import webbrowser

                webbrowser.open_new_tab(full_url)
                exit()

            display_methods(t)
            return
        find_type(t, tname, html)


def display_methods(module, level=0):
    if module is None:
        return

    print(module["doc"])

    ms = module["class_methods"]
    for m in ms + module["instance_methods"]:
        print("Signature:", m["html_id"])
        if m["doc"]:
            print("  ", m["doc"])
        print("=" * 30)
        print()

    for t in module["types"]:
        fullname = t["full_name"]
        parent = module["full_name"]
        h = (level + 1) * "#"
        if h:
            h = h + " "
        print(f"{h}{fullname} of {parent}")

        print(t["full_name"], urllib.parse.urljoin(HTML_URL, t["path"]))
        display_methods(t, level=level + 1)


def main():
    import argparse

    argp = argparse.ArgumentParser()
    argp.add_argument("--module", "-m", help="search a module name")
    argp.add_argument("--type", "-t", help="search a type (class)")
    argp.add_argument("--method", "-f", help="search a method")
    argp.add_argument(
        "--html", action="store_true", help="Open the URL in default browser"
    )

    args = argp.parse_args()

    if not any([args.module, args.type, args.method]):
        list_modules()
        exit()

    if args.module:
        m = find_module(args.module)
        if args.html:
            full_url = urllib.parse.urljoin(HTML_URL, m["path"])
            print(m["full_name"], full_url)
            print(f"Opening {full_url}")
            import webbrowser

            webbrowser.open_new_tab(full_url)
            exit()

        display_methods(m)
    elif args.type:
        m_name, _, _ = args.type.partition("::")
        module = find_module(m_name)
        if module:
            r = find_type(module, args.type, html=args.html)
            display_methods(r)
        else:
            print("Not found")
    elif args.method:
        module_name, *_, method_name = args.method.split("::")
        module = find_module(module_name)
        if module:
            r = find_method(module, method_name, html=args.html)
        else:
            print("Not found")


if __name__ == "__main__":
    main()
