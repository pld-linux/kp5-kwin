# TODO:
# - libhybris
#
%define		kdeplasmaver	5.5.4
%define		qtver		5.5.1
%define		kpname		kwin
#
Summary:	KDE Window manager
Name:		kp5-%{kpname}
Version:	5.5.4
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	d719b7258a5fa9bf2dae770a20fa4e2d
Patch0:		kp5-kwin-absolute-path.patch
URL:		http://www.kde.org/
BuildRequires:	Mesa-libEGL-devel
BuildRequires:	Mesa-libgbm-devel
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5PlatformSupport-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-kcmutils-devel
BuildRequires:	kf5-kcompletion-devel
BuildRequires:	kf5-kconfig-devel
BuildRequires:	kf5-kconfigwidgets-devel
BuildRequires:	kf5-kcoreaddons-devel
BuildRequires:	kf5-kcrash-devel
BuildRequires:	kf5-kdeclarative-devel
BuildRequires:	kf5-kglobalaccel-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kiconthemes-devel
BuildRequires:	kf5-kinit-devel
BuildRequires:	kf5-kio-devel
BuildRequires:	kf5-knewstuff-devel
BuildRequires:	kf5-knotifications-devel
BuildRequires:	kf5-kpackage-devel
BuildRequires:	kf5-kservice-devel
BuildRequires:	kf5-kwidgetsaddons-devel
BuildRequires:	kf5-kwindowsystem-devel
BuildRequires:	kf5-kxmlgui-devel
BuildRequires:	kf5-plasma-framework-devel
BuildRequires:	kp5-kscreenlocker-devel
BuildRequires:	kp5-kwayland-devel
BuildRequires:	libdrm-devel
BuildRequires:	libepoxy-devel
BuildRequires:	libinput-devel
BuildRequires:	libxcb-devel
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	udev-devel
BuildRequires:	wayland-devel
BuildRequires:	xcb-util-cursor-devel
BuildRequires:	xcb-util-image-devel
BuildRequires:	xcb-util-keysyms-devel
BuildRequires:	xcb-util-wm-devel
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
KDE Window manager.

%package devel
Summary:	Header files for %{kpname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kpname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kpname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kpname}.

%prep
%setup -q -n %{kpname}-%{version}
#%%patch0 -p1

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kwin_wayland
%attr(755,root,root) %{_bindir}/kwin_x11
%attr(755,root,root) %{_libdir}/kconf_update_bin/kwin5_update_default_rules
%attr(755,root,root) %{_libdir}/kwin_killer_helper
%attr(755,root,root) %{_libdir}/kwin_rules_dialog
%attr(755,root,root) %{_libdir}/libkdeinit5_kwin_rules_dialog.so
%attr(755,root,root) %{_libdir}/libkdeinit5_kwin_x11.so
%attr(755,root,root) %ghost %{_libdir}/libkwin.so.5
%attr(755,root,root) %{_libdir}/libkwin.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkwin4_effect_builtins.so.1
%attr(755,root,root) %{_libdir}/libkwin4_effect_builtins.so.*.*.*
%attr(755,root,root) %{_libdir}/libkwineffects.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkwineffects.so.7
%attr(755,root,root) %{_libdir}/libkwinglutils.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkwinglutils.so.7
%attr(755,root,root) %{_libdir}/libkwinxrenderutils.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkwinxrenderutils.so.7
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_kwin_scripts.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_kwindecoration.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_kwindesktop.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_kwinoptions.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_kwinrules.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_kwinscreenedges.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_kwintabbox.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/org.kde.kidletime.platforms/KF5IdleTimeKWinWaylandPrivatePlugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/org.kde.kwin.waylandbackends/KWinWaylandVirtualBackend.so
%attr(755,root,root) %{_libdir}/qt5/plugins/platforms/KWinQpaPlugin.so
%dir %{_libdir}/qt5/plugins/kwin
%dir %{_libdir}/qt5/plugins/kwin/effects
%dir %{_libdir}/qt5/plugins/kwin/effects/configs
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/effects/configs/kcm_kwin4_genericscripted.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/effects/configs/kwin_blur_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/effects/configs/kwin_coverswitch_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/effects/configs/kwin_cube_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/effects/configs/kwin_cubeslide_config.so
#%%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/effects/configs/kwin_dashboard_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/effects/configs/kwin_desktopgrid_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/effects/configs/kwin_diminactive_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/effects/configs/kwin_flipswitch_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/effects/configs/kwin_glide_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/effects/configs/kwin_invert_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/effects/configs/kwin_lookingglass_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/effects/configs/kwin_magiclamp_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/effects/configs/kwin_magnifier_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/effects/configs/kwin_mouseclick_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/effects/configs/kwin_mousemark_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/effects/configs/kwin_presentwindows_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/effects/configs/kwin_resize_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/effects/configs/kwin_showfps_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/effects/configs/kwin_thumbnailaside_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/effects/configs/kwin_trackmouse_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/effects/configs/kwin_windowgeometry_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/effects/configs/kwin_wobblywindows_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/effects/configs/kwin_zoom_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwincompositing.so
%attr(755,root,root) %{_libdir}/qt5/plugins/org.kde.kdecoration2/kwin5_aurorae.so
%attr(755,root,root) %{_libdir}/qt5/plugins/org.kde.kglobalaccel5.platforms/KF5GlobalAccelPrivateKWin.so
%dir %{_libdir}/qt5/plugins/org.kde.kwin.waylandbackends
%attr(755,root,root) %{_libdir}/qt5/plugins/org.kde.kwin.waylandbackends/KWinWaylandDrmBackend.so
%attr(755,root,root) %{_libdir}/qt5/plugins/org.kde.kwin.waylandbackends/KWinWaylandFbdevBackend.so
%attr(755,root,root) %{_libdir}/qt5/plugins/org.kde.kwin.waylandbackends/KWinWaylandWaylandBackend.so
%attr(755,root,root) %{_libdir}/qt5/plugins/org.kde.kwin.waylandbackends/KWinWaylandX11Backend.so
/etc/xdg/aurorae.knsrc
/etc/xdg/kwineffect.knsrc
/etc/xdg/kwinscripts.knsrc
/etc/xdg/kwinswitcher.knsrc
/etc/xdg/org_kde_kwin.categories
%{_libdir}/qt5/qml/org/kde/kwin
%{_datadir}/config.kcfg/kwin.kcfg
%{_datadir}/dbus-1/interfaces/org.kde.KWin.xml
%{_datadir}/dbus-1/interfaces/org.kde.kwin.Compositing.xml
%{_datadir}/dbus-1/interfaces/org.kde.kwin.Effects.xml
%{_iconsdir}/hicolor/*/apps/kwin.png
%{_iconsdir}/hicolor/scalable/apps/kwin.svgz
%{_datadir}/knotifications5/kwin.notifyrc
%{_datadir}/kservices5/*kwin*.desktop
%{_datadir}/kservices5/desktop.desktop
%{_datadir}/kservices5/kwin
%{_datadir}/kservicetypes5/kwin*.desktop
%{_datadir}/kwin
%{_datadir}/kwincompositing

%files devel
%defattr(644,root,root,755)
%{_includedir}/kwin*.h
%attr(755,root,root) %{_libdir}/libkwin4_effect_builtins.so
%attr(755,root,root) %{_libdir}/libkwineffects.so
%attr(755,root,root) %{_libdir}/libkwinglutils.so
%attr(755,root,root) %{_libdir}/libkwinxrenderutils.so
%{_libdir}/cmake/KWinDBusInterface
