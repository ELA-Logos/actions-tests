import os
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Script to configure conan with remote login and profiles')

    parser.add_argument('version', help='Version')
    parser.add_argument('-p', '--path', dest='path', default="", help='Remote login username')

    args = parser.parse_args()

    if os.path.exists(args.path + 'version.txt'):
        f = open(args.path + 'version.txt', "w")
        f.write(args.version)
        f.close()

    if os.path.exists(args.path + 'version.h'):
        f = open(args.path + 'version.h', "w")
        L = ["#pragma once\n", f"#define VERSION \"{args.version}\"\n"]
        f.writelines(L)
        f.close()

    if os.path.exists(args.path + 'version.properties'):
        f = open(args.path + 'version.properties', "w")
        L = [f"version={args.version}"]
        f.writelines(L)
        f.close()