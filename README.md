Use Jarl with [pre-commit](https://pre-commit.com/) or [prek](https://prek.j178.dev/).

## Quick start

### `pre-commit`

Use this in `.pre-commit-config.yaml`:

```yaml
repos:
-   repo: https://github.com/etiennebacher/jarl-pre-commit
    rev: 0.4.0
    hooks:
      - id: jarl-check
```

You can pass additional arguments with `args`, for instance:

```yaml
repos:
-   repo: https://github.com/etiennebacher/jarl-pre-commit
    rev: 0.4.0
    hooks:
      - id: jarl-check
        args: [--fix]
```

### `prek`

`prek` can read `.pre-commit-config.yaml` but also has its own format, `prek.toml`.

Use this in `prek.toml`:

```toml
[[repos]]
repo = "https://github.com/etiennebacher/jarl-pre-commit"
rev = "0.4.0"
hooks = [
  { id = "jarl-check" },
]
```

You can pass additional arguments with `args`, for instance:

```toml
[[repos]]
repo = "https://github.com/etiennebacher/jarl-pre-commit"
rev = "0.4.0"
hooks = [
  { id = "jarl-check", args = ["--fix"] },
]
```

### Choosing the version of Jarl to use

The `rev` parameter determines the version of Jarl to use. Starting from 0.4.0, all releases of Jarl have a matching release in `jarl-pre-commit`.

### How the jarl binary is installed

The hook uses `language: python`. When pre-commit sets up the hook environment (via `pip install .`), a custom build step automatically downloads the jarl binary for your platform from the corresponding GitHub release. This means:

- **No network access is needed at hook execution time.** The binary is downloaded once during environment setup and cached by pre-commit.
- **Works on [pre-commit.ci](https://pre-commit.ci)** and other CI services that restrict network access during hook execution but allow it during environment setup.
- **Version pinning is respected:** the `rev:` value in your config determines which tag of this repo is checked out, and that tag's `setup.py` encodes the matching jarl version to download.
The pre-commit environment cache means the download only happens once per `rev:`. You may have projects using different versions of jarl simultaneously without them interfering with each other or with any system-wide jarl installation.
