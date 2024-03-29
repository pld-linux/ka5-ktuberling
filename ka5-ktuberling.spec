#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	23.08.5
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		ktuberling
Summary:	ktuberling
Name:		ka5-%{kaname}
Version:	23.08.5
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	3acb0fa9df06d4a8a763eba636cfaabd
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
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-devel
BuildRequires:	ka5-libkdegames-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kcompletion-devel >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf5-kdelibs4support-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	%{name}-data = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KTuberling a simple constructor game suitable for children and adults
alike. The idea of the game is based around a once popular doll making
concept.

%description -l pl.UTF-8
KTuberling jest prostą grą konstrukcyjną odpowiednią dla dzieci jak
i dorosłych. Pomysł gry jest oparty na popularnej grze w ubieranie
lalek.

%package data
Summary:	Data files for %{kaname}
Summary(pl.UTF-8):	Dane dla %{kaname}
Group:		X11/Applications/Games
BuildArch:	noarch

%description data
Data files for %{kaname}.

%description data -l pl.UTF-8
Dane dla %{kaname}.


%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ktuberling

%files data  -f %{kaname}.lang
%defattr(644,root,root,755)
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
%{_datadir}/metainfo/org.kde.ktuberling.appdata.xml
%{_datadir}/qlogging-categories5/ktuberling.categories
