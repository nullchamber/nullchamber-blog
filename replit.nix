{ pkgs }: {
    deps = [
        pkgs.python39Packages.virtualenv
        pkgs.python39Packages.pip
        pkgs.python39Full
        pkgs.cowsay
    ];
}