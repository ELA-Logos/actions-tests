import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Script to create a commit message for updating version file')
    parser.add_argument('version', help='Version')
    parser.add_argument('-s', '--skip-ci', dest='skip_ci', choices=['true', 'false', 'True', 'False'], required=True, help='Skip CI')
    args = parser.parse_args()

    skip_ci = args.skip_ci.lower() == 'true'

    commit_message = f"Update version file to {args.version}"
    if skip_ci:
        commit_message += " [skip ci]"
    print(f'commit_message={commit_message}')
