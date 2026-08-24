# disable empty debuh
%global debug_package %{nil}

Name:           noctalia-shell
Version:		4.1.1
Release:        1
Summary:        A Quickshell-based custom shell setup
License:        MIT
URL:            https://github.com/noctalia-dev/noctalia-shell
Source0:        https://github.com/noctalia-dev/noctalia-shell/releases/download/v%{version}/noctalia-v%{version}.tar.gz

Requires: brightnessctl
Requires: dejavu-sans-fonts
Requires: gpu-screen-recorder-gtk
Requires: %{_lib}Qt6Multimedia
Requires: quickshell
Requires: xdg-desktop-portal-gtk

Recommends: cava
Recommends: cliphist
Recommends: ddcutil
Recommends: matugen
Recommends: power-profiles-daemon
Recommends: wlsunset

%description
A beautiful, minimal desktop shell for Wayland that actually gets out of your way. 
Built on Quickshell with a warm lavender aesthetic that you can easily customize to match your vibe.

%prep
%autosetup -n noctalia-release -p1

%build
# Nothing to build

%install
install -dm755 "%{buildroot}%{_sysconfdir}/xdg/quickshell/noctalia-shell"
cp -r ./* "%{buildroot}%{_sysconfdir}/xdg/quickshell/noctalia-shell/"
install -dm755 "%{buildroot}%{_prefix}/lib/systemd/user"
install -Dm644 ./Assets/Services/systemd/noctalia.service %{buildroot}%{_userunitdir}/noctalia.service

%files
%license LICENSE
%doc README.md
#dir %{_sysconfdir}/xdg/quickshell/noctalia-shell/
%{_userunitdir}/noctalia.service
%config %{_sysconfdir}/xdg/quickshell/noctalia-shell/
