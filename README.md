# Advent of Code 2024

Simple repo to have a little bit of fun before christmas 2024.

Challenges are at [AoC 2024 website](https://adventofcode.com/2024).

Solutions are in Python with file names for that particular day.

# Python development environment

Minimal code to run Python environment using [nix flakes](https://nix.dev/concepts/flakes.html).

## Usage

```
nix develop
```

Initial build of Python takes roughly 10 minutes as it is building exact version from the source. It will also create `flake.lock` file to lock the current environment.

## Setup

In order to start I had to enable flakes in NixOS configuration `/etc/nixos/configuration.nix`:

```
nix.settings.experimental-features = [ "nix-command" "flakes" ];
```

Rebuild the system `nixos-rebuild switch` and I can create a new flake environment:

```
nix init
```

Modify the `flake.nix` file as needed...

## Acknowledgement

Thanks to [nixpkgs-python](https://github.com/cachix/nixpkgs-python) for the hard work.
