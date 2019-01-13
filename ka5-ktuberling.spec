%define		kdeappsver	18.12.1
%define		qtver		5.9.0
%define		kaname		ktuberling
Summary:	ktuberling
Name:		ka5-%{kaname}
Version:	18.12.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	a525dbc9879c3a1d0e2107b82e64a124
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Multimedia-devel
BuildRequires:	Qt5Network-devel >= 5.11.1
BuildRequires:	Qt5PrintSupport-devel
BuildRequires:	Qt5Qml-devel >= 5.11.1
BuildRequires:	Qt5Quick-devel >= 5.11.1
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	Qt5Xml-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-libkdegames-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= 5.30.0
BuildRequires:	kf5-kcompletion-devel >= 5.15.0
BuildRequires:	kf5-kconfig-devel >= 5.15.0
BuildRequires:	kf5-kconfigwidgets-devel >= 5.15.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.15.0
BuildRequires:	kf5-kcrash-devel >= 5.15.0
BuildRequires:	kf5-kdbusaddons-devel >= 5.15.0
BuildRequires:	kf5-kdelibs4support-devel >= 5.15.0
BuildRequires:	kf5-kdoctools-devel >= 5.15.0
BuildRequires:	kf5-ki18n-devel >= 5.15.0
BuildRequires:	kf5-kio-devel >= 5.15.0
BuildRequires:	kf5-kwidgetsaddons-devel >= 5.15.0
BuildRequires:	kf5-kxmlgui-devel >= 5.15.0
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KTuberling a simple constructor game suitable for children and adults
alike. The idea of the game is based around a once popular doll making
concept. The idea of the game is based around a once popular doll
making concept.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ktuberling
%{_desktopdir}/org.kde.ktuberling.desktop
%{_iconsdir}/hicolor/128x128/apps/ktuberling.png
%{_iconsdir}/hicolor/128x128/mimetypes/application-x-tuberling.png
%{_iconsdir}/hicolor/16x16/apps/ktuberling.png
%{_iconsdir}/hicolor/16x16/mimetypes/application-x-tuberling.png
%{_iconsdir}/hicolor/22x22/apps/ktuberling.png
%{_iconsdir}/hicolor/22x22/mimetypes/application-x-tuberling.png
%{_iconsdir}/hicolor/32x32/apps/ktuberling.png
%{_iconsdir}/hicolor/32x32/mimetypes/application-x-tuberling.png
%{_iconsdir}/hicolor/48x48/apps/ktuberling.png
%{_iconsdir}/hicolor/48x48/mimetypes/application-x-tuberling.png
%{_iconsdir}/hicolor/64x64/apps/ktuberling.png
%{_iconsdir}/hicolor/64x64/mimetypes/application-x-tuberling.png
%{_datadir}/ktuberling
%{_datadir}/kxmlgui5/ktuberling
%{_datadir}/metainfo/org.kde.ktuberling.appdata.xml
