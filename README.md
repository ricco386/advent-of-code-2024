# Advent of Code 2024

Simple repo to have a little bit of fun before christmas 2024.

Challenges are at [AoC 2024 website](https://adventofcode.com/2024).

Solutions are in Python with file names for that particular day.

# Python development environment

Minimal code to run Python environment using [nix flakes](https://nix.dev/concepts/flakes.html).

## Setup

In order to start I had to enable flakes. Once that is done create a new flake environment:

```
nix init
```

Modify the `flake.nix` file.

## Usage

```
nix develop
```

Initial build of Python takes roughly 10 minutes as it is building exact version from the source. It will also create `flake.lock` file to lock the current environment.
