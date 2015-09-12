%define beta %nil
%define major %(echo %{version}|cut -d. -f1)

%define core %mklibname qt%{major}3dcore %{major}
%define cored %mklibname qt%{major}3dcore -d
%define input %mklibname qt%{major}3dinput %{major}
%define inputd %mklibname qt%{major}3dinput -d
%define quick %mklibname qt%{major}3dquick %{major}
%define quickd %mklibname qt%{major}3dquick -d
%define quickrenderer %mklibname qt%{major}3dquickrenderer %{major}
%define quickrendererd %mklibname qt%{major}3dquickrenderer -d
%define renderer %mklibname qt%{major}3drenderer %{major}
%define rendererd %mklibname qt%{major}3drenderer -d

Name:		qt5-qt3d
Version:	5.5.0
%if "%{beta}" != ""
Release:	1.%{beta}.1
%define qttarballdir qt3d-opensource-src-%{version}-%{beta}
Source0:	http://download.qt.io/development_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}%{?beta:-%{beta}}/submodules/%{qttarballdir}.tar.xz
%else
Release:	3
%define qttarballdir qt3d-opensource-src-%{version}
Source0:	http://download.qt.io/official_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}/submodules/%{qttarballdir}.tar.xz
%endif
Summary:	Qt 3D toolkit
Group:		System/Libraries
License:	LGPLv2 with exceptions or GPLv3 with exceptions and GFDL
URL:		http://www.qt.io/
BuildRequires:	qt5-qtbase-devel
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	qt5-qtqml-private-devel
Requires:	%{core} = %{EVRD}
Requires:	%{input} = %{EVRD}
Requires:	%{quick} = %{EVRD}
Requires:	%{quickrenderer} = %{EVRD}
Requires:	%{renderer} = %{EVRD}

%description
Qt5 3D API.

%files

# ===
%package devel
Summary:	Development files for the Qt 3D library
Group:		Development/KDE and Qt
Requires:	%{cored} = %{EVRD}
Requires:	%{inputd} = %{EVRD}
Requires:	%{quickd} = %{EVRD}
Requires:	%{quickrendererd} = %{EVRD}
Requires:	%{rendererd} = %{EVRD}

%files devel
%{_libdir}/qt5/examples/qt3d

# =====
%package -n %{core}
Summary:	Qt3D core library
Group:		System/Libraries

%description -n %{core}
Qt3D core library.

%files -n %{core}
%{_libdir}/libQt%{major}3DCore.so.%{major}*

%package -n %{cored}
Summary:	Development files for the Qt3D core library
Group:		Development/KDE and Qt
Requires:	%{core} = %{EVRD}

%description -n %{cored}
Development files for the Qt3D core library.

%files -n %{cored}
%{_includedir}/qt%{major}/Qt3DCore
%{_libdir}/cmake/Qt%{major}3DCore
%{_libdir}/libQt%{major}3DCore.so
%{_libdir}/libQt%{major}3DCore.prl
%{_libdir}/pkgconfig/Qt%{major}3DCore.pc
%{_libdir}/qt%{major}/mkspecs/modules/qt_lib_3dcore.pri
%{_libdir}/qt%{major}/mkspecs/modules/qt_lib_3dcore_private.pri

# =====
%package -n %{input}
Summary:	Qt3D input library
Group:		System/Libraries

%description -n %{input}
Qt3D input library.

%files -n %{input}
%{_libdir}/libQt%{major}3DInput.so.%{major}*

%package -n %{inputd}
Summary:	Development files for the Qt3D input library
Group:		Development/KDE and Qt
Requires:	%{input} = %{EVRD}

%description -n %{inputd}
Development files for the Qt3D input library.

%files -n %{inputd}
%{_includedir}/qt%{major}/Qt3DInput
%{_libdir}/cmake/Qt%{major}3DInput
%{_libdir}/libQt%{major}3DInput.so
%{_libdir}/libQt%{major}3DInput.prl
%{_libdir}/pkgconfig/Qt%{major}3DInput.pc
%{_libdir}/qt%{major}/mkspecs/modules/qt_lib_3dinput.pri
%{_libdir}/qt%{major}/mkspecs/modules/qt_lib_3dinput_private.pri

# =====
%package -n %{quick}
Summary:	Qt3D QtQuick library
Group:		System/Libraries

%description -n %{quick}
Qt3D QtQuick library.

%files -n %{quick}
%{_libdir}/libQt%{major}3DQuick.so.%{major}*
%{_libdir}/qt%{major}/qml/Qt3D
%{_libdir}/qt%{major}/qml/QtQuick/Scene3D

%package -n %{quickd}
Summary:	Development files for the Qt3D QtQuick library
Group:		Development/KDE and Qt
Requires:	%{quick} = %{EVRD}

%description -n %{quickd}
Development files for the Qt3D QtQuick library.

%files -n %{quickd}
%{_includedir}/qt%{major}/Qt3DQuick
%{_libdir}/cmake/Qt%{major}3DQuick
%{_libdir}/libQt%{major}3DQuick.so
%{_libdir}/libQt%{major}3DQuick.prl
%{_libdir}/pkgconfig/Qt%{major}3DQuick.pc
%{_libdir}/qt%{major}/mkspecs/modules/qt_lib_3dquick.pri
%{_libdir}/qt%{major}/mkspecs/modules/qt_lib_3dquick_private.pri

# =====
%package -n %{quickrenderer}
Summary:	Qt3D QuickRenderer library
Group:		System/Libraries

%description -n %{quickrenderer}
Qt3D QuickRenderer library.

%files -n %{quickrenderer}
%{_libdir}/libQt%{major}3DQuickRenderer.so.%{major}*

%package -n %{quickrendererd}
Summary:	Development files for the Qt3D QuickRenderer library
Group:		Development/KDE and Qt
Requires:	%{quickrenderer} = %{EVRD}

%description -n %{quickrendererd}
Development files for the Qt3D QuickRenderer library.

%files -n %{quickrendererd}
%{_includedir}/qt%{major}/Qt3DQuickRenderer
%{_libdir}/cmake/Qt%{major}3DQuickRenderer
%{_libdir}/libQt%{major}3DQuickRenderer.so
%{_libdir}/libQt%{major}3DQuickRenderer.prl
%{_libdir}/pkgconfig/Qt%{major}3DQuickRenderer.pc
%{_libdir}/qt%{major}/mkspecs/modules/qt_lib_3dquickrenderer.pri
%{_libdir}/qt%{major}/mkspecs/modules/qt_lib_3dquickrenderer_private.pri

# =====
%package -n %{renderer}
Summary:	Qt3D renderer library
Group:		System/Libraries

%description -n %{renderer}
Qt3D renderer library.

%files -n %{renderer}
%{_libdir}/libQt%{major}3DRenderer.so.%{major}*

%package -n %{rendererd}
Summary:	Development files for the Qt3D renderer library
Group:		Development/KDE and Qt
Requires:	%{renderer} = %{EVRD}

%description -n %{rendererd}
Development files for the Qt3D renderer library.

%files -n %{rendererd}
%{_includedir}/qt%{major}/Qt3DRenderer
%{_libdir}/cmake/Qt%{major}3DRenderer
%{_libdir}/libQt%{major}3DRenderer.so
%{_libdir}/libQt%{major}3DRenderer.prl
%{_libdir}/pkgconfig/Qt%{major}3DRenderer.pc
%{_libdir}/qt%{major}/mkspecs/modules/qt_lib_3drenderer.pri
%{_libdir}/qt%{major}/mkspecs/modules/qt_lib_3drenderer_private.pri

#------------------------------------------------------------------------------

%prep
%setup -q -n %qttarballdir

%build
%qmake_qt5
%make

#------------------------------------------------------------------------------

%install
%makeinstall_std INSTALL_ROOT=%{buildroot}
