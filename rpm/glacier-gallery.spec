Name:       glacier-gallery

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}

Summary:    Photo Gallery for Nemo
Version:    0.2.2
Release:    2
Group:      Applications/System
License:    BSD
URL:        https://github.com/nemomobile-ux/glacier-gallery
Source0:    %{name}-%{version}.tar.bz2

Requires:   glacier-gallery-qmlplugin
Requires:   mapplauncherd-booster-qtcomponents-qt5
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(qdeclarative5-boostable)
BuildRequires:  pkgconfig(libresourceqt5)
BuildRequires:  desktop-file-utils
Provides:   meego-handset-video > 0.2.5
Obsoletes:   meego-handset-video <= 0.2.5


%package qmlplugin
Summary: QML Plugin for gallery view
Requires:   qt-components-qt5
Requires:   qt5-qtquickcontrols
Requires:   qt5-qtquickcontrols-nemo
Requires:   qt5-qtdeclarative-import-multimedia
Requires:   nemo-qml-plugin-thumbnailer-qt5
Requires:   qt5-qtdocgallery

%description
Photo Gallery application using Qt Quick for Nemo Mobile.

%description qmlplugin
This pligin contants qml api for glacier gallery

%prep
%setup -q -n %{name}-%{version}

%build

%qtc_qmake5
%qtc_make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%qmake5_install

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%{_bindir}/glacier-gallery
%{_datadir}/applications/glacier-gallery.desktop
%{_datadir}/glacier-gallery

%files qmlplugin
%{_libdir}/qt5/qml/org/nemomobile/gallery/*
