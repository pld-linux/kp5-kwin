# TODO:
# - libhybris
#
#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeplasmaver	5.93.0
%define		kf_ver	5.102.0
%define		qt_ver		5.15.0
%define		kpname		kwin
#
Summary:	KDE Window manager
Summary(pl.UTF-8):	Zarządca okien KDE
Name:		kp5-%{kpname}
Version:	5.93.0
Release:	0.1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/unstable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	74568aba1c606a434396f0b2313aedb8
Patch0:		kp5-kwin-absolute-path.patch
URL:		http://www.kde.org/
BuildRequires:	EGL-devel
BuildRequires:	Mesa-libgbm-devel
BuildRequires:	OpenGL-devel
BuildRequires:	Qt6Core-devel >= %{qt_ver}
BuildRequires:	Qt6DBus-devel >= %{qt_ver}
BuildRequires:	Qt6Gui-devel >= %{qt_ver}
BuildRequires:	Qt6Multimedia-devel >= %{qt_ver}
BuildRequires:	Qt6Network-devel >= %{qt_ver}
#BuildRequires:	Qt6PlatformSupport-devel >= %{qt_ver}
BuildRequires:	Qt6Qml-devel >= %{qt_ver}
BuildRequires:	Qt6Quick-devel >= %{qt_ver}
BuildRequires:	Qt6Sensors-devel >= %{qt_ver}
BuildRequires:	Qt6UiTools-devel >= %{qt_ver}
BuildRequires:	Qt6Widgets-devel >= %{qt_ver}
BuildRequires:	cmake >= 3.16.0
BuildRequires:	docbook-style-xsl
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel >= 2
BuildRequires:	hwdata
BuildRequires:	kf6-extra-cmake-modules >= 5.38
BuildRequires:	kf6-kcmutils-devel >= %{kf_ver}
BuildRequires:	kf6-kcompletion-devel >= %{kf_ver}
BuildRequires:	kf6-kconfig-devel >= %{kf_ver}
BuildRequires:	kf6-kconfigwidgets-devel >= %{kf_ver}
BuildRequires:	kf6-kcoreaddons-devel >= %{kf_ver}
BuildRequires:	kf6-kcrash-devel >= %{kf_ver}
BuildRequires:	kf6-kdeclarative-devel >= %{kf_ver}
BuildRequires:	kf6-kdoctools-devel >= %{kf_ver}
BuildRequires:	kf6-kglobalaccel-devel >= %{kf_ver}
BuildRequires:	kf6-ki18n-devel >= %{kf_ver}
BuildRequires:	kf6-kiconthemes-devel >= %{kf_ver}
BuildRequires:	kf6-kidletime-devel >= %{kf_ver}
BuildRequires:	kf6-kio-devel >= %{kf_ver}
BuildRequires:	kf6-kirigami-devel >= %{kf_ver}
BuildRequires:	kf6-knewstuff-devel >= %{kf_ver}
BuildRequires:	kf6-knotifications-devel >= %{kf_ver}
BuildRequires:	kf6-kpackage-devel >= %{kf_ver}
BuildRequires:	kf6-krunner-devel >= %{kf_ver}
BuildRequires:	kf6-kservice-devel >= %{kf_ver}
BuildRequires:	kf6-ktextwidgets-devel >= %{kf_ver}
BuildRequires:	kf6-kwidgetsaddons-devel >= %{kf_ver}
BuildRequires:	kf6-kwindowsystem-devel >= %{kf_ver}
BuildRequires:	kf6-kxmlgui-devel >= %{kf_ver}
BuildRequires:	kp5-breeze-devel >= 5.23.0
BuildRequires:	kp5-kdecoration-devel >= 5.23.0
BuildRequires:	kp5-kglobalacceld-devel
BuildRequires:	kp5-kscreenlocker-devel
BuildRequires:	kp5-kwayland-devel >= 5.93.0
BuildRequires:	lcms2-devel
BuildRequires:	libcap
BuildRequires:	libcap-devel
BuildRequires:	libdisplay-info-devel
BuildRequires:	libdrm-devel >= 2.4.62
BuildRequires:	libepoxy-devel
BuildRequires:	libinput-devel >= 1.9
BuildRequires:	libstdc++-devel
BuildRequires:	libxcb-devel >= 1.10
BuildRequires:	ninja
BuildRequires:	pipewire-devel >= 0.3
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	udev-devel
BuildRequires:	wayland-devel >= 1.2
BuildRequires:	wayland-egl-devel
BuildRequires:	xcb-util-cursor-devel
BuildRequires:	xcb-util-image-devel
BuildRequires:	xcb-util-keysyms-devel
BuildRequires:	xcb-util-wm-devel >= 0.4
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libxcvt-devel >= 0.1.1
BuildRequires:	xorg-lib-libxkbcommon-devel >= 0.7.0
BuildRequires:	xorg-lib-libxkbcommon-x11-devel >= 0.7.0
BuildRequires:	xorg-xserver-Xwayland-devel
BuildRequires:	xz
Requires:	%{name}-data = %{version}-%{release}
Requires:	Qt6Core >= %{qt_ver}
Requires:	Qt6DBus >= %{qt_ver}
Requires:	Qt6Gui >= %{qt_ver}
Requires:	Qt6Network >= %{qt_ver}
Requires:	Qt6Qml >= %{qt_ver}
Requires:	Qt6Quick >= %{qt_ver}
Requires:	Qt6Widgets >= %{qt_ver}
Requires:	kf6-kcmutils >= %{kf_ver}
Requires:	kf6-kcompletion >= %{kf_ver}
Requires:	kf6-kconfig >= %{kf_ver}
Requires:	kf6-kconfigwidgets >= %{kf_ver}
Requires:	kf6-kcoreaddons >= %{kf_ver}
Requires:	kf6-kcrash >= %{kf_ver}
Requires:	kf6-kdeclarative >= %{kf_ver}
Requires:	kf6-kglobalaccel >= %{kf_ver}
Requires:	kf6-ki18n >= %{kf_ver}
Requires:	kf6-kidletime >= %{kf_ver}
Requires:	kf6-kio >= %{kf_ver}
Requires:	kf6-knewstuff >= %{kf_ver}
Requires:	kf6-knotifications >= %{kf_ver}
Requires:	kf6-kpackage >= %{kf_ver}
Requires:	kf6-kservice >= %{kf_ver}
Requires:	kf6-ktextwidgets >= %{kf_ver}
Requires:	kf6-kwidgetsaddons >= %{kf_ver}
Requires:	kf6-kwindowsystem >= %{kf_ver}
Requires:	kf6-kxmlgui >= %{kf_ver}
Requires:	kp5-kdecoration >= 5.18.0
Requires:	kp5-kscreenlocker
Requires:	kp5-kwayland >= 5.93.0
Requires:	kp5-plasma-activities >= 5.93.0
Requires:	libcap
Requires:	libdrm >= 2.4.62
Requires:	libinput >= 1.9
Requires:	libxcb >= 1.10
Requires:	xcb-util-wm >= 0.4
Requires:	xorg-lib-libxkbcommon >= 0.7.0
Suggests:	hwdata
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt6dir		%{_libdir}/qt6

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
Requires:	Qt6Core-devel >= %{qt_ver}
Requires:	Qt6Gui-devel >= %{qt_ver}
Requires:	kf6-kconfig-devel >= %{kf_ver}
Requires:	kf6-kcoreaddons-devel >= %{kf_ver}
Requires:	kf6-kwindowsystem-devel >= %{kf_ver}
Requires:	libepoxy-devel
Requires:	libstdc++-devel
Requires:	libxcb-devel

%description devel
Header files for %{kpname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kpname}.

%prep
%setup -q -n %{kpname}-%{version}
#%%patch0 -p1

%build
rm -rf po/id

%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DHTML_INSTALL_DIR=%{_kdedocdir}
%ninja_build -C build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build
rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/{sr,sr@latin}

%find_lang %{kpname} --all-name --with-kde

find $RPM_BUILD_ROOT%{_datadir}/kconf_update -type f -name "*.py" \
-exec sed -i -e 's#/usr/bin/env python3#/usr/bin/python3#' '{}' +

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kwin_wayland
%attr(755,root,root) %{_bindir}/kwin_x11
%attr(755,root,root) %{_libdir}/kconf_update_bin/kwin5_update_default_rules
%ghost %{_libdir}/libkwin.so.6
%attr(755,root,root) %{_libdir}/libkwin.so.*.*.*
%attr(755,root,root) %{_libdir}/qt6/plugins/kwin/effects/configs/kwin_tileseditor_config.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_kwinxwayland.so
%dir %{_libdir}/qt6/plugins/kwin
%dir %{_libdir}/qt6/plugins/kwin/effects
%dir %{_libdir}/qt6/plugins/kwin/effects/configs
%dir %{_libdir}/qt6/plugins/kwin/plugins
%attr(755,root,root) %{_libdir}/qt6/plugins/kwin/effects/configs/kcm_kwin4_genericscripted.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kwin/effects/configs/kwin_blur_config.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kwin/effects/configs/kwin_diminactive_config.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kwin/effects/configs/kwin_glide_config.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kwin/effects/configs/kwin_invert_config.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kwin/effects/configs/kwin_magiclamp_config.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kwin/effects/configs/kwin_magnifier_config.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kwin/effects/configs/kwin_mouseclick_config.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kwin/effects/configs/kwin_mousemark_config.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kwin/effects/configs/kwin_thumbnailaside_config.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kwin/effects/configs/kwin_trackmouse_config.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kwin/effects/configs/kwin_wobblywindows_config.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kwin/effects/configs/kwin_zoom_config.so
%{_libdir}/qt6/qml/org/kde/kwin
%attr(755,root,root) %{_libdir}/qt6/plugins/kwin/effects/configs/kwin_slide_config.so
%attr(755,root,root) %{_prefix}/libexec/kwin_killer_helper
%ghost %{_libdir}/libkcmkwincommon.so.6
%attr(755,root,root) %{_libdir}/libkcmkwincommon.so.*.*
%attr(755,root,root) %{_libdir}/qt6/plugins/kwin/effects/configs/kwin_showpaint_config.so
%attr(755,root,root) %{_bindir}/kwin_wayland_wrapper
%{systemduserunitdir}/plasma-kwin_x11.service
%attr(755,root,root) %{_libdir}/qt6/plugins/kwin/plugins/krunnerintegration.so
%attr(755,root,root) %{_prefix}/libexec/kwin-applywindowdecoration
%attr(755,root,root) %{_libdir}/qt6/plugins/kwin/effects/configs/kwin_overview_config.so
%{systemduserunitdir}/plasma-kwin_wayland.service
%attr(755,root,root) %{_libdir}/qt6/plugins/kwin/effects/configs/kwin_windowview_config.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_kwin_effects.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_kwin_scripts.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_kwin_virtualdesktops.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_kwindecoration.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_kwinrules.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_virtualkeyboard.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings_qwidgets/kcm_kwinoptions.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings_qwidgets/kcm_kwinscreenedges.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings_qwidgets/kcm_kwintabbox.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings_qwidgets/kcm_kwintouchscreen.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings_qwidgets/kwincompositing.so
%attr(755,root,root) %{_libdir}/kconf_update_bin/kwin-6.0-delete-desktop-switching-shortcuts
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/packagestructure/kwin_aurorae.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/packagestructure/kwin_decoration.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/packagestructure/kwin_effect.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/packagestructure/kwin_scripts.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/packagestructure/kwin_windowswitcher.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kwin/effects/configs/kwin_colorblindnesscorrection_config.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kwin/plugins/BounceKeysPlugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kwin/plugins/StickyKeysPlugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kwin/plugins/buttonsrebind.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kwin/plugins/nightcolor.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kwin/plugins/screencast.so
%attr(755,root,root) %{_libdir}/qt6/plugins/org.kde.kdecoration2.kcm/kcm_auroraedecoration.so
%attr(755,root,root) %{_libdir}/qt6/plugins/org.kde.kdecoration2/org.kde.kwin.aurorae.so

%files data -f %{kpname}.lang
%defattr(644,root,root,755)
%{_datadir}/config.kcfg/kwin.kcfg
%{_datadir}/dbus-1/interfaces/org.kde.KWin.xml
%{_datadir}/dbus-1/interfaces/org.kde.kwin.Compositing.xml
%{_datadir}/dbus-1/interfaces/org.kde.kwin.Effects.xml
%{_iconsdir}/hicolor/*/apps/kwin.png
%{_iconsdir}/hicolor/scalable/apps/kwin.svgz
%{_datadir}/kwin
%{_datadir}/dbus-1/interfaces/org.kde.kwin.ColorCorrect.xml
%{_datadir}/kconf_update/kwin.upd
%{_datadir}/knsrcfiles/aurorae.knsrc
%{_datadir}/knsrcfiles/kwineffect.knsrc
%{_datadir}/knsrcfiles/kwinscripts.knsrc
%{_datadir}/knsrcfiles/kwinswitcher.knsrc
%{_datadir}/knsrcfiles/window-decorations.knsrc
%{_datadir}/config.kcfg/kwindecorationsettings.kcfg
%{_datadir}/config.kcfg/virtualdesktopssettings.kcfg
%{_datadir}/dbus-1/interfaces/org.kde.KWin.Plugins.xml
%dir %{_datadir}/krunner
%dir %{_datadir}/krunner/dbusplugins
%{_datadir}/krunner/dbusplugins/kwin-runner-windows.desktop
%{_datadir}/dbus-1/interfaces/org.kde.kwin.VirtualKeyboard.xml
%{_datadir}/dbus-1/interfaces/org.kde.KWin.TabletModeManager.xml
%{_datadir}/dbus-1/interfaces/org.kde.kwin.InputDevice.xml
%{_desktopdir}/kcm_kwin_effects.desktop
%{_desktopdir}/kcm_kwin_scripts.desktop
%{_desktopdir}/kcm_kwin_virtualdesktops.desktop
%{_desktopdir}/kcm_kwindecoration.desktop
%{_desktopdir}/kcm_kwinoptions.desktop
%{_desktopdir}/kcm_kwinrules.desktop
%{_desktopdir}/kcm_virtualkeyboard.desktop
%{_desktopdir}/kwincompositing.desktop
%{_desktopdir}/kcm_kwintabbox.desktop
%{_desktopdir}/kcm_kwinxwayland.desktop
%{_datadir}/config.kcfg/nightcolorsettings.kcfg
%{_desktopdir}/org.kde.kwin.killer.desktop
%{_datadir}/dbus-1/interfaces/org.kde.KWin.VirtualDesktopManager.xml
%attr(755,root,root) %{_datadir}/kconf_update/kwin-6.0-overview-activities-shortcuts.py
%{_datadir}/knotifications6/kwin.notifyrc
%{_datadir}/qlogging-categories6/org_kde_kwin.categories

%files devel
%defattr(644,root,root,755)
%{_includedir}/kwin
%{_libdir}/cmake/KWinDBusInterface
%{_libdir}/cmake/KWin
%{_libdir}/libkwin.so
