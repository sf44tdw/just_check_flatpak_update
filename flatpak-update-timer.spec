Name:           flatpak-update-timer
Version:        1.0
Release:        1%{?dist}
Summary:        Daily systemd timer for updating Flatpaks
License:        GPL-3.0-only
BuildArch:      noarch
Source0:        flatpak-update.service
Source1:        flatpak-update.timer
Requires:       flatpak
%{?systemd_requires}

%description
Installs a systemd service and timer that run
"flatpak update --noninteractive" daily.

%prep

%build

%install
mkdir -p %{buildroot}%{_unitdir}
install -pm 0644 %{SOURCE0} %{buildroot}%{_unitdir}/flatpak-update.service
install -pm 0644 %{SOURCE1} %{buildroot}%{_unitdir}/flatpak-update.timer

%post
%systemd_post flatpak-update.timer
if [ "$1" -eq 1 ] && [ -d /run/systemd/system ]; then
    systemctl enable --now flatpak-update.timer
fi

%preun
%systemd_preun flatpak-update.timer

%postun
%systemd_postun flatpak-update.timer

%files
%{_unitdir}/flatpak-update.service
%{_unitdir}/flatpak-update.timer
