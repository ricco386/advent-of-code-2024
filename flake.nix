{
  description = "Python flake for AoC to learn nix flakes";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
    nixpkgs-python.url = "github:cachix/nixpkgs-python";
  };

  outputs = { self, nixpkgs, nixpkgs-python }:
      let
          system = "x86_64-linux";
          pythonVersion = "3.13.0";
          pkgs = import nixpkgs { inherit system; };
          python = nixpkgs-python.packages.${system}.${pythonVersion};
      in
      {
          devShells.${system}.default = pkgs.mkShell {
              buildInputs = [
                  python
              ];
              shellHook = ''
                  python --version
              '';
          };
      };

}
