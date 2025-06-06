# TODO:
# - libhybris?
#
# Conditional build:
%bcond_with	tests		# test suite

%define		kp_ver		5.27.12
%define		kf_ver		5.102.0
%define		qt_ver		5.15.2
%define		kpname		kwin
#
Summary:	KDE Window manager
Summary(pl.UTF-8):	Zarządca okien KDE
Name:		kp5-%{kpname}
Version:	5.27.12
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/plasma/%{kp_ver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	007e657cd8ef4bc3d7f07e90e49e3aba
Patch0:		kp5-kwin-absolute-path.patch
URL:		http://www.kde.org/
BuildRequires:	EGL-devel
BuildRequires:	Mesa-libgbm-devel >= 21.3
BuildRequires:	OpenGL-devel
BuildRequires:	Qt5AccessibilitySupport-devel >= %{qt_ver}
BuildRequires:	Qt5Concurrent-devel >= %{qt_ver}
BuildRequires:	Qt5Core-devel >= %{qt_ver}
BuildRequires:	Qt5DBus-devel >= %{qt_ver}
BuildRequires:	Qt5EventDispatcherSupport-devel >= %{qt_ver}
BuildRequires:	Qt5FontDatabaseSupport-devel >= %{qt_ver}
BuildRequires:	Qt5Gui-devel >= %{qt_ver}
BuildRequires:	Qt5Multimedia-devel >= %{qt_ver}
BuildRequires:	Qt5Network-devel >= %{qt_ver}
BuildRequires:	Qt5Qml-devel >= %{qt_ver}
BuildRequires:	Qt5Quick-controls >= %{qt_ver}
BuildRequires:	Qt5Quick-devel >= %{qt_ver}
BuildRequires:	Qt5ServiceSupport-devel >= %{qt_ver}
%{?with_tests:BuildRequires:	Qt5Test-devel >= %{qt_ver}}
BuildRequires:	Qt5ThemeSupport-devel >= %{qt_ver}
BuildRequires:	Qt5UiTools-devel >= %{qt_ver}
BuildRequires:	Qt5Widgets-devel >= %{qt_ver}
BuildRequires:	Qt5X11Extras-devel >= %{qt_ver}
BuildRequires:	Qt5XkbCommonSupport-devel >= %{qt_ver}
BuildRequires:	cmake >= 3.16.0
BuildRequires:	docbook-style-xsl
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel >= 2
BuildRequires:	hwdata
BuildRequires:	kf5-extra-cmake-modules >= %{kf_ver}
BuildRequires:	kf5-kactivities-devel >= %{kf_ver}
BuildRequires:	kf5-kauth-devel >= %{kf_ver}
BuildRequires:	kf5-kcmutils-devel >= %{kf_ver}
BuildRequires:	kf5-kconfig-devel >= %{kf_ver}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kf_ver}
BuildRequires:	kf5-kcoreaddons-devel >= %{kf_ver}
BuildRequires:	kf5-kcrash-devel >= %{kf_ver}
BuildRequires:	kf5-kdbusaddons-devel >= %{kf_ver}
BuildRequires:	kf5-kdeclarative-devel >= %{kf_ver}
BuildRequires:	kf5-kdoctools-devel >= %{kf_ver}
BuildRequires:	kf5-kglobalaccel-devel >= %{kf_ver}
BuildRequires:	kf5-ki18n-devel >= %{kf_ver}
BuildRequires:	kf5-kidletime-devel >= %{kf_ver}
BuildRequires:	kf5-kirigami2-devel >= %{kf_ver}
BuildRequires:	kf5-knewstuff-devel >= %{kf_ver}
BuildRequires:	kf5-knotifications-devel >= %{kf_ver}
BuildRequires:	kf5-kpackage-devel >= %{kf_ver}
BuildRequires:	kf5-krunner-devel >= %{kf_ver}
BuildRequires:	kf5-kservice-devel >= %{kf_ver}
BuildRequires:	kf5-kwayland-devel >= %{kf_ver}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kf_ver}
BuildRequires:	kf5-kwindowsystem-devel >= %{kf_ver}
BuildRequires:	kf5-kxmlgui-devel >= %{kf_ver}
BuildRequires:	kf5-plasma-framework-devel >= %{kf_ver}
BuildRequires:	kp5-breeze-devel >= 5.23.0
BuildRequires:	kp5-kdecoration-devel >= %{version}
BuildRequires:	kp5-kscreenlocker-devel
BuildRequires:	lcms2-devel >= 2
BuildRequires:	libcap
BuildRequires:	libcap-devel
BuildRequires:	libdrm-devel >= 2.4.112
BuildRequires:	libepoxy-devel >= 1.3
BuildRequires:	libinput-devel >= 1.19
BuildRequires:	libqaccessibilityclient-qt5-devel
BuildRequires:	libstdc++-devel >= 6:8
BuildRequires:	libxcb-devel >= 1.10
BuildRequires:	ninja
BuildRequires:	pipewire-devel >= 0.3.29
BuildRequires:	pkgconfig
BuildRequires:	plasma-wayland-protocols-devel >= 1.9.0
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	udev-devel
BuildRequires:	wayland-devel >= 1.21
BuildRequires:	wayland-egl-devel
BuildRequires:	wayland-protocols >= 1.31
BuildRequires:	xcb-util-cursor-devel
BuildRequires:	xcb-util-image-devel
BuildRequires:	xcb-util-keysyms-devel
BuildRequires:	xcb-util-wm-devel >= 0.4
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libxcvt-devel >= 0.1.1
BuildRequires:	xorg-lib-libxkbcommon-devel >= 1.5.0
BuildRequires:	xorg-lib-libxkbcommon-x11-devel >= 1.5.0
BuildRequires:	xorg-xserver-Xwayland-devel
BuildRequires:	xz
Requires:	%{name}-data = %{version}-%{release}
Requires:	Mesa-libgbm >= 21.3
Requires:	Qt5Concurrent >= %{qt_ver}
Requires:	Qt5Core >= %{qt_ver}
Requires:	Qt5DBus >= %{qt_ver}
Requires:	Qt5Gui >= %{qt_ver}
Requires:	Qt5Network >= %{qt_ver}
Requires:	Qt5Qml >= %{qt_ver}
Requires:	Qt5Quick >= %{qt_ver}
Requires:	Qt5Quick-controls >= %{qt_ver}
Requires:	Qt5Widgets >= %{qt_ver}
Requires:	Qt5X11Extras >= %{qt_ver}
Requires:	kde-common-dirs >= 0.9
Requires:	kf5-kactivities >= %{kf_ver}
Requires:	kf5-kauth >= %{kf_ver}
Requires:	kf5-kcmutils >= %{kf_ver}
Requires:	kf5-kconfig >= %{kf_ver}
Requires:	kf5-kconfigwidgets >= %{kf_ver}
Requires:	kf5-kcoreaddons >= %{kf_ver}
Requires:	kf5-kcrash >= %{kf_ver}
Requires:	kf5-kdbusaddons >= %{kf_ver}
Requires:	kf5-kdeclarative >= %{kf_ver}
Requires:	kf5-kglobalaccel >= %{kf_ver}
Requires:	kf5-ki18n >= %{kf_ver}
Requires:	kf5-kidletime >= %{kf_ver}
Requires:	kf5-kirigami2 >= %{kf_ver}
Requires:	kf5-knewstuff >= %{kf_ver}
Requires:	kf5-knotifications >= %{kf_ver}
Requires:	kf5-kpackage >= %{kf_ver}
Requires:	kf5-krunner >= %{kf_ver}
Requires:	kf5-kservice >= %{kf_ver}
Requires:	kf5-kwayland >= %{kf_ver}
Requires:	kf5-kwidgetsaddons >= %{kf_ver}
Requires:	kf5-kwindowsystem >= %{kf_ver}
Requires:	kf5-kxmlgui >= %{kf_ver}
Requires:	kf5-plasma-framework >= %{kf_ver}
Requires:	kp5-breeze >= 5.23.0
Requires:	kp5-kdecoration >= %{version}
Requires:	kp5-kscreenlocker
Requires:	libcap
Requires:	libdrm >= 2.4.112
Requires:	libepoxy >= 1.3
Requires:	libinput >= 1.19
Requires:	libxcb >= 1.10
Requires:	pipewire-libs >= 0.3.29
Requires:	wayland >= 1.21
Requires:	xcb-util-wm >= 0.4
Requires:	xorg-lib-libxcvt >= 0.1.1
Requires:	xorg-lib-libxkbcommon >= 1.5.0
Requires:	xorg-lib-libxkbcommon-x11 >= 1.5.0
Suggests:	hwdata
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
KDE Window manager.

%description -l pl.UTF-8
Zarządca okien KDE.

%package data
Summary:	Data files for %{kpname}
Summary(pl.UTF-8):	Dane dla %{kpname}
Group:		X11/Applications
BuildArch:	noarch

%description data
Data files for %{kpname}.

%description data -l pl.UTF-8
Dane dla %{kpname}.

%package devel
Summary:	Header files for %{kpname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kpname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5Core-devel >= %{qt_ver}
Requires:	Qt5Gui-devel >= %{qt_ver}
Requires:	kf5-kconfig-devel >= %{kf_ver}
Requires:	kf5-kcoreaddons-devel >= %{kf_ver}
Requires:	kf5-kwindowsystem-devel >= %{kf_ver}
Requires:	libepoxy-devel >= 1.3
Requires:	libstdc++-devel >= 6:8
Requires:	libxcb-devel >= 1.10

%description devel
Header files for %{kpname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kpname}.

%prep
%setup -q -n %{kpname}-%{version}
#%%patch -P 0 -p1

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DXwayland_EXECUTABLE:PATH=/usr/bin/Xwayland \
	-Dhwdata_DIR=/lib/hwdata \
	-Dhwdata_PNPIDS_FILE=/lib/hwdata/pnp.ids

%ninja_build -C build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{kpname} --all-name --with-kde

find $RPM_BUILD_ROOT%{_datadir}/kconf_update -type f -name "*.py" \
	-exec sed -i -e 's#/usr/bin/env python3#/usr/bin/python3#' '{}' +

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/kwin_wayland
%attr(755,root,root) %{_bindir}/kwin_wayland_wrapper
%attr(755,root,root) %{_bindir}/kwin_x11
%attr(755,root,root) %{_libdir}/libkcmkwincommon.so.*.*.*
%ghost %{_libdir}/libkcmkwincommon.so.5
%attr(755,root,root) %{_libdir}/libkwin.so.*.*.*
%ghost %{_libdir}/libkwin.so.5
%attr(755,root,root) %{_libdir}/libkwineffects.so.*.*.*
%ghost %{_libdir}/libkwineffects.so.14
%attr(755,root,root) %{_libdir}/libkwinglutils.so.*.*.*
%ghost %{_libdir}/libkwinglutils.so.14
%attr(755,root,root) %{_libdir}/kconf_update_bin/kwin5_update_default_rules
%dir %{_libdir}/qt5/plugins/kwin
%dir %{_libdir}/qt5/plugins/kwin/effects
%dir %{_libdir}/qt5/plugins/kwin/effects/configs
%attr(755,root,root) %{_libdir}/qt5/plugins/kpackage/packagestructure/kwin_aurorae.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kpackage/packagestructure/kwin_decoration.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kpackage/packagestructure/kwin_effect.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kpackage/packagestructure/kwin_script.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kpackage/packagestructure/kwin_windowswitcher.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/effects/configs/kcm_kwin4_genericscripted.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/effects/configs/kwin_blur_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/effects/configs/kwin_desktopgrid_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/effects/configs/kwin_diminactive_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/effects/configs/kwin_glide_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/effects/configs/kwin_invert_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/effects/configs/kwin_magiclamp_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/effects/configs/kwin_magnifier_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/effects/configs/kwin_mouseclick_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/effects/configs/kwin_mousemark_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/effects/configs/kwin_overview_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/effects/configs/kwin_showpaint_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/effects/configs/kwin_slide_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/effects/configs/kwin_thumbnailaside_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/effects/configs/kwin_tileseditor_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/effects/configs/kwin_trackmouse_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/effects/configs/kwin_windowview_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/effects/configs/kwin_wobblywindows_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/effects/configs/kwin_zoom_config.so
%dir %{_libdir}/qt5/plugins/kwin/plugins
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/plugins/MouseButtonToKeyPlugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/plugins/colordintegration.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/plugins/krunnerintegration.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/plugins/libKWinNightColorPlugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/org.kde.kdecoration2/kwin5_aurorae.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_kwin_effects.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_kwin_scripts.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_kwin_virtualdesktops.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_kwindecoration.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_kwinrules.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_kwinxwayland.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_virtualkeyboard.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_kwinoptions.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_kwinscreenedges.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_kwintabbox.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_kwintouchscreen.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kwincompositing.so
%{_libdir}/qt5/qml/org/kde/kwin
%dir %{_libdir}/qt5/qml/org/kde/kwin.2
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/kwin.2/DesktopThumbnailItem.qml
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/kwin.2/qmldir
%attr(755,root,root) %{_libexecdir}/kwin-applywindowdecoration
%attr(755,root,root) %{_libexecdir}/kwin_killer_helper
%attr(755,root,root) %{_libexecdir}/kwin_rules_dialog
%{systemduserunitdir}/plasma-kwin_wayland.service
%{systemduserunitdir}/plasma-kwin_x11.service

%files data -f %{kpname}.lang
%defattr(644,root,root,755)
%{_datadir}/config.kcfg/kwin.kcfg
%{_datadir}/config.kcfg/kwindecorationsettings.kcfg
%{_datadir}/config.kcfg/nightcolorsettings.kcfg
%{_datadir}/config.kcfg/virtualdesktopssettings.kcfg
%{_datadir}/dbus-1/interfaces/org.kde.KWin.xml
%{_datadir}/dbus-1/interfaces/org.kde.KWin.Plugins.xml
%{_datadir}/dbus-1/interfaces/org.kde.KWin.TabletModeManager.xml
%{_datadir}/dbus-1/interfaces/org.kde.KWin.VirtualDesktopManager.xml
%{_datadir}/dbus-1/interfaces/org.kde.kwin.ColorCorrect.xml
%{_datadir}/dbus-1/interfaces/org.kde.kwin.Compositing.xml
%{_datadir}/dbus-1/interfaces/org.kde.kwin.Effects.xml
%{_datadir}/dbus-1/interfaces/org.kde.kwin.InputDevice.xml
%{_datadir}/dbus-1/interfaces/org.kde.kwin.VirtualKeyboard.xml
%attr(755,root,root) %{_datadir}/kconf_update/kwin-5.16-auto-bordersize.sh
%attr(755,root,root) %{_datadir}/kconf_update/kwin-5.18-move-animspeed.py
%attr(755,root,root) %{_datadir}/kconf_update/kwin-5.21-desktop-grid-click-behavior.py
%attr(755,root,root) %{_datadir}/kconf_update/kwin-5.21-no-swap-encourage.py
%attr(755,root,root) %{_datadir}/kconf_update/kwin-5.23-disable-translucency-effect.sh
%attr(755,root,root) %{_datadir}/kconf_update/kwin-5.23-remove-cover-switch.py
%attr(755,root,root) %{_datadir}/kconf_update/kwin-5.23-remove-cubeslide.py
%attr(755,root,root) %{_datadir}/kconf_update/kwin-5.23-remove-flip-switch.py
%attr(755,root,root) %{_datadir}/kconf_update/kwin-5.23-remove-xrender-backend.py
%attr(755,root,root) %{_datadir}/kconf_update/kwin-5.25-effect-pluginid-config-group.py
%attr(755,root,root) %{_datadir}/kconf_update/kwin-5.27-replace-cascaded-zerocornered.sh
%attr(755,root,root) %{_datadir}/kconf_update/kwinrules-5.19-placement.pl
%attr(755,root,root) %{_datadir}/kconf_update/kwinrules-5.23-virtual-desktop-ids.py
%{_datadir}/kconf_update/kwin.upd
%{_datadir}/kconf_update/kwinrules.upd
%{_datadir}/knotifications5/kwin.notifyrc
%{_datadir}/knsrcfiles/aurorae.knsrc
%{_datadir}/knsrcfiles/kwineffect.knsrc
%{_datadir}/knsrcfiles/kwinscripts.knsrc
%{_datadir}/knsrcfiles/kwinswitcher.knsrc
%{_datadir}/knsrcfiles/window-decorations.knsrc
%{_datadir}/kpackage/kcms/kcm_kwin_effects
%{_datadir}/kpackage/kcms/kcm_kwin_scripts
%{_datadir}/kpackage/kcms/kcm_kwin_virtualdesktops
%{_datadir}/kpackage/kcms/kcm_kwindecoration
%{_datadir}/kpackage/kcms/kcm_kwinrules
%{_datadir}/kpackage/kcms/kcm_kwinxwayland
%{_datadir}/kpackage/kcms/kcm_virtualkeyboard
%dir %{_datadir}/krunner
%dir %{_datadir}/krunner/dbusplugins
%{_datadir}/krunner/dbusplugins/kwin-runner-windows.desktop
%{_datadir}/kservicetypes5/kwin*.desktop
%{_datadir}/kwin
%{_datadir}/qlogging-categories5/org_kde_kwin.categories
%{_desktopdir}/kcm_kwin_effects.desktop
%{_desktopdir}/kcm_kwin_scripts.desktop
%{_desktopdir}/kcm_kwin_virtualdesktops.desktop
%{_desktopdir}/kcm_kwindecoration.desktop
%{_desktopdir}/kcm_kwinoptions.desktop
%{_desktopdir}/kcm_kwinrules.desktop
%{_desktopdir}/kcm_kwintabbox.desktop
%{_desktopdir}/kcm_kwinxwayland.desktop
%{_desktopdir}/kcm_virtualkeyboard.desktop
%{_desktopdir}/kwincompositing.desktop
%{_desktopdir}/org.kde.kwin_rules_dialog.desktop
%{_iconsdir}/hicolor/*/apps/kwin.png
%{_iconsdir}/hicolor/scalable/apps/kwin.svgz

%files devel
%defattr(644,root,root,755)
%{_libdir}/libkwineffects.so
%{_libdir}/libkwinglutils.so
%{_includedir}/kwin*.h
%{_libdir}/cmake/KWinDBusInterface
%{_libdir}/cmake/KWinEffects
