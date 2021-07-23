#!/usr/bin/env python
# coding: utf-8
import os
import json

import urllib.request
import shutil


URL = "https://crystal-lang.org/api/1.1.0/index.json"
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


def display_methods(module):
    ms = module["class_methods"]
    for m in ms + module['instance_methods']:
        print("Signature:", m["html_id"])
        print("  ", m["doc"])
        print("=" * 30)
        print()


def main():
    import argparse
    argp = argparse.ArgumentParser()
    argp.add_argument("--module", "-m")

    args = argp.parse_args()

    if args.module is None:
        list_modules()
        exit()

    m = find_module(args.module)
    display_methods(m)


if __name__ == "__main__":
    main()
