# update-version-file Action

Github action for updating version files in a repo. 
It will update versions in the following files:
- `version.txt`
- `version.h`
- `version.properties`

> :warning: **Compatability**: This action can only be used on UNIX systems (eg. ubuntu-latest)

## Inputs
| Name                    | Description              | Required | Default Value |
|-------------------------|--------------------------|----------|---------------|
| `version`               | Version to update with   | `true`   |               |
| `version_file_location` | Version file location    |          | `src/`        |
| `branch`                | Branch to push to        |          | `main`        |
| `github_access_token`   | Push to protected branch | `true`   |               |
| `no-push`               | Do not push to branch    |          | `false`       |
| `skip_ci`               | Skip CI                  |          | `true`        |


## Outputs 
| Name          | Description                                                   |
|---------------|---------------------------------------------------------------|
| `commit_hash` | Commit hash of the push, only present if `no-push` is `false` |

## Example usage

```yaml
...
  steps:
    - uses: actions/checkout@v4
    - name: Update version file
      uses: Logos-Payment-Solution/update-version-file@v1.1.0
      id: update-version-file
      with:
        version: <new version>
        github_access_token: ${{ secrets.GITHUB_TOKEN }}
...
```
## Who do I talk to?
- [Frederik Andersen](mailto:fra@logos.dk), @FRA-Logos, Embedded Næreum
- [Emil Schier Langer](mailto:ela@logos.dk), @ELA-Logos, Embedded Odense