with (import <nixpkgs> {});
mkShell {
  buildInputs = [
    python310
  ];
}