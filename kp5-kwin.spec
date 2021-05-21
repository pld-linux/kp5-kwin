# TODO:
# - libhybris
#
%define		kdeplasmaver	5.21.5
%define		qtver		5.9.0
%define		kpname		kwin
#
Summary:	KDE Window manager
Summary(pl.UTF-8):	Zarządca okien KDE
Name:		kp5-%{kpname}
Version:	5.21.5
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	537f40058190d829041cce3bf8b77928
Patch0:		kp5-kwin-absolute-path.patch
URL:		http://www.kde.org/
BuildRequires:	Mesa-libEGL-devel
BuildRequires:	Mesa-libgbm-devel
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5EventDispatcherSupport-devel >= %{qtver}
BuildRequires:	Qt5FontDatabaseSupport-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
#BuildRequires:	Qt5PlatformSupport-devel >= %{qtver}
BuildRequires:	Qt5ThemeSupport-devel >= %{qtver}
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
BuildRequires:	kf5-kwayland-devel
BuildRequires:	kf5-kwidgetsaddons-devel
BuildRequires:	kf5-kwindowsystem-devel
BuildRequires:	kf5-kxmlgui-devel
BuildRequires:	kf5-plasma-framework-devel
BuildRequires:	kp5-kdecoration-devel
BuildRequires:	kp5-kscreenlocker-devel
BuildRequires:	kp5-kwayland-server-devel
BuildRequires:	libdrm-devel
BuildRequires:	libepoxy-devel
BuildRequires:	libinput-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libxcb-devel
BuildRequires:	ninja
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

%description -l pl.UTF-8
Zarządca okien KDE.

%package devel
Summary:	Header files for %{kpname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kpname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5Core-devel >= %{qtver}
Requires:	Qt5Gui-devel >= %{qtver}
Requires:	kf5-kconfig-devel
Requires:	kf5-kcoreaddons-devel
Requires:	kf5-kwindowsystem-devel
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
install -d build
rm -rf po/id

cd build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	../
%ninja_build

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

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kwin_wayland
%attr(755,root,root) %{_bindir}/kwin_x11
%attr(755,root,root) %{_libdir}/kconf_update_bin/kwin5_update_default_rules
%ghost %{_libdir}/libkwin.so.5
%attr(755,root,root) %{_libdir}/libkwin.so.*.*.*
%ghost %{_libdir}/libkwin4_effect_builtins.so.1
%attr(755,root,root) %{_libdir}/libkwin4_effect_builtins.so.*.*.*
%attr(755,root,root) %{_libdir}/libkwineffects.so.*.*.*
%attr(755,root,root) %{_libdir}/libkwinglutils.so.*.*.*
%attr(755,root,root) %{_libdir}/libkwinxrenderutils.so.*.*.*

%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_kwintouchscreen.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kpackage/packagestructure/kwin_packagestructure_aurorae.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kpackage/packagestructure/kwin_packagestructure_decoration.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kpackage/packagestructure/kwin_packagestructure_scripts.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kpackage/packagestructure/kwin_packagestructure_windowswitcher.so
%dir %{_libdir}/qt5/plugins/org.kde.kwin.platforms
%attr(755,root,root) %{_libdir}/qt5/plugins/org.kde.kwin.platforms/KWinX11Platform.so

%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_kwin_scripts.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_kwinoptions.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_kwinscreenedges.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_kwintabbox.so
%attr(755,root,root) %{_libdir}/qt5/plugins/org.kde.kwin.waylandbackends/KWinWaylandVirtualBackend.so
%dir %{_libdir}/qt5/plugins/kwin
%dir %{_libdir}/qt5/plugins/kwin/effects
%dir %{_libdir}/qt5/plugins/kwin/effects/configs
%dir %{_libdir}/qt5/plugins/kwin/plugins
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/effects/configs/kcm_kwin4_genericscripted.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/effects/configs/kwin_blur_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/effects/configs/kwin_coverswitch_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/effects/configs/kwin_cube_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/effects/configs/kwin_cubeslide_config.so
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
%dir %{_libdir}/qt5/plugins/org.kde.kwin.waylandbackends
%attr(755,root,root) %{_libdir}/qt5/plugins/org.kde.kwin.waylandbackends/KWinWaylandDrmBackend.so
%attr(755,root,root) %{_libdir}/qt5/plugins/org.kde.kwin.waylandbackends/KWinWaylandFbdevBackend.so
%attr(755,root,root) %{_libdir}/qt5/plugins/org.kde.kwin.waylandbackends/KWinWaylandWaylandBackend.so
%attr(755,root,root) %{_libdir}/qt5/plugins/org.kde.kwin.waylandbackends/KWinWaylandX11Backend.so
%dir %{_libdir}/qt5/plugins/org.kde.kwin.scenes
%attr(755,root,root) %{_libdir}/qt5/plugins/org.kde.kwin.scenes/KWinSceneQPainter.so
%attr(755,root,root) %{_libdir}/qt5/plugins/org.kde.kwin.scenes/KWinSceneXRender.so
%{_libdir}/qt5/qml/org/kde/kwin
%{_datadir}/config.kcfg/kwin.kcfg
%{_datadir}/dbus-1/interfaces/org.kde.KWin.xml
%{_datadir}/dbus-1/interfaces/org.kde.kwin.Compositing.xml
%{_datadir}/dbus-1/interfaces/org.kde.kwin.Effects.xml
%{_iconsdir}/hicolor/*/apps/kwin.png
%{_iconsdir}/hicolor/scalable/apps/kwin.svgz
%{_datadir}/knotifications5/kwin.notifyrc
%{_datadir}/kservices5/*kwin*.desktop
%{_datadir}/kservices5/kwin
%{_datadir}/kservicetypes5/kwin*.desktop
%{_datadir}/kwin
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/effects/configs/kwin_slide_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/org.kde.kwin.scenes/KWinSceneOpenGL.so
%attr(755,root,root) %{_prefix}/libexec/kwin_killer_helper
%attr(755,root,root) %{_prefix}/libexec/kwin_rules_dialog
%{_datadir}/config.kcfg/kwin_colorcorrect.kcfg
%{_datadir}/dbus-1/interfaces/org.kde.kwin.ColorCorrect.xml
%{_datadir}/kconf_update/kwin.upd
%ghost %{_libdir}/libkcmkwincommon.so.5
%attr(755,root,root) %{_libdir}/libkcmkwincommon.so.5.*.*
%attr(755,root,root) %{_libdir}/qt5/plugins/kcms/kcm_kwin_virtualdesktops.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kpackage/packagestructure/kwin_packagestructure_effect.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/effects/configs/kwin_showpaint_config.so
%{_datadir}/dbus-1/interfaces/org.kde.KWin.VirtualDesktopManager.xml
%dir %{_datadir}/kpackage/kcms/kcm_kwin_virtualdesktops
%dir %{_datadir}/kpackage/kcms/kcm_kwin_virtualdesktops/contents
%dir %{_datadir}/kpackage/kcms/kcm_kwin_virtualdesktops/contents/ui
%{_datadir}/kpackage/kcms/kcm_kwin_virtualdesktops/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcm_kwin_virtualdesktops/metadata.desktop
%{_datadir}/kpackage/kcms/kcm_kwin_virtualdesktops/metadata.json
%{_datadir}/knsrcfiles/aurorae.knsrc
%{_datadir}/knsrcfiles/kwineffect.knsrc
%{_datadir}/knsrcfiles/kwinscripts.knsrc
%{_datadir}/knsrcfiles/kwinswitcher.knsrc
%{_datadir}/knsrcfiles/window-decorations.knsrc
%dir %{_datadir}/kpackage/kcms
%dir %{_datadir}/kpackage/kcms/kcm_kwin_effects
%dir %{_datadir}/kpackage/kcms/kcm_kwin_effects/contents
%dir %{_datadir}/kpackage/kcms/kcm_kwin_effects/contents/ui
%{_datadir}/kpackage/kcms/kcm_kwin_effects/contents/ui/Effect.qml
%{_datadir}/kpackage/kcms/kcm_kwin_effects/contents/ui/Video.qml
%{_datadir}/kpackage/kcms/kcm_kwin_effects/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcm_kwin_effects/metadata.desktop
%{_datadir}/kpackage/kcms/kcm_kwin_effects/metadata.json
%dir %{_datadir}/kpackage/kcms/kcm_kwindecoration
%dir %{_datadir}/kpackage/kcms/kcm_kwindecoration/contents
%dir %{_datadir}/kpackage/kcms/kcm_kwindecoration/contents/ui
%{_datadir}/kpackage/kcms/kcm_kwindecoration/contents/ui/ButtonGroup.qml
%{_datadir}/kpackage/kcms/kcm_kwindecoration/contents/ui/Buttons.qml
%{_datadir}/kpackage/kcms/kcm_kwindecoration/contents/ui/Themes.qml
%{_datadir}/kpackage/kcms/kcm_kwindecoration/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcm_kwindecoration/metadata.desktop
%{_datadir}/kpackage/kcms/kcm_kwindecoration/metadata.json
%attr(755,root,root) %{_libdir}/qt5/plugins/kcms/kcm_kwin_effects.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcms/kcm_kwindecoration.so
%attr(755,root,root) %{_datadir}/kconf_update/kwin-5.16-auto-bordersize.sh
%{_datadir}/qlogging-categories5/org_kde_kwin.categories

%attr(755,root,root) %{_bindir}/kwin_wayland_wrapper
%{systemduserunitdir}/plasma-kwin_x11.service
%ghost %{_libdir}/libkwineffects.so.13
%ghost %{_libdir}/libkwinglutils.so.13
%ghost %{_libdir}/libkwinxrenderutils.so.13
%attr(755,root,root) %{_libdir}/qt5/plugins/kcms/kcm_kwinrules.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/plugins/colordintegration.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/plugins/krunnerintegration.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwin/plugins/libKWinNightColorPlugin.so
%{_datadir}/config.kcfg/kwindecorationsettings.kcfg
%{_datadir}/config.kcfg/virtualdesktopssettings.kcfg
%{_datadir}/dbus-1/interfaces/org.kde.KWin.Plugins.xml
%attr(755,root,root) %{_datadir}/kconf_update/kwin-5.18-move-animspeed.py
%attr(755,root,root) %{_datadir}/kconf_update/kwin-5.21-desktop-grid-click-behavior.py
%attr(755,root,root) %{_datadir}/kconf_update/kwin-5.21-no-swap-encourage.py
%attr(755,root,root) %{_datadir}/kconf_update/kwinrules-5.19-placement.pl
%{_datadir}/kconf_update/kwinrules.upd
%dir %{_datadir}/kpackage/kcms/kcm_kwinrules
%dir %{_datadir}/kpackage/kcms/kcm_kwinrules/contents
%dir %{_datadir}/kpackage/kcms/kcm_kwinrules/contents/ui
%{_datadir}/kpackage/kcms/kcm_kwinrules/contents/ui/FileDialogLoader.qml
%{_datadir}/kpackage/kcms/kcm_kwinrules/contents/ui/OptionsComboBox.qml
%{_datadir}/kpackage/kcms/kcm_kwinrules/contents/ui/RuleItemDelegate.qml
%{_datadir}/kpackage/kcms/kcm_kwinrules/contents/ui/RulesEditor.qml
%{_datadir}/kpackage/kcms/kcm_kwinrules/contents/ui/RulesList.qml
%{_datadir}/kpackage/kcms/kcm_kwinrules/contents/ui/ValueEditor.qml
%{_datadir}/kpackage/kcms/kcm_kwinrules/metadata.desktop
%{_datadir}/kpackage/kcms/kcm_kwinrules/metadata.json
%dir %{_datadir}/krunner
%dir %{_datadir}/krunner/dbusplugins
%{_datadir}/krunner/dbusplugins/kwin-runner-windows.desktop

%files devel
%defattr(644,root,root,755)
%{_includedir}/kwin*.h
%{_libdir}/libkwin4_effect_builtins.so
%{_libdir}/libkwineffects.so
%{_libdir}/libkwinglutils.so
%{_libdir}/libkwinxrenderutils.so
%{_libdir}/cmake/KWinDBusInterface
%{_libdir}/cmake/KWinEffects
