%define beta %{nil}
%define major %(echo %{version}|cut -d. -f1)

%define core %mklibname qt%{major}3dcore %{major}
%define cored %mklibname qt%{major}3dcore -d
%define animation %mklibname qt%{major}3danimation %{major}
%define animationd %mklibname qt%{major}3danimation -d
%define input %mklibname qt%{major}3dinput %{major}
%define inputd %mklibname qt%{major}3dinput -d
%define logic %mklibname qt%{major}3dlogic %{major}
%define logicd %mklibname qt%{major}3dlogic -d
%define quick %mklibname qt%{major}3dquick %{major}
%define quickd %mklibname qt%{major}3dquick -d
%define quickanimation %mklibname qt%{major}3dquickanimation %{major}
%define quickanimationd %mklibname qt%{major}3dquickanimation -d
%define quickinput %mklibname qt%{major}3dquickinput %{major}
%define quickinputd %mklibname qt%{major}3dquickinput -d
%define quickrender %mklibname qt%{major}3dquickrender %{major}
%define quickrenderd %mklibname qt%{major}3dquickrender -d
%define quickscene2d %mklibname qt%{major}3dquickscene2d %{major}
%define quickscene2dd %mklibname qt%{major}3dquickscene2d -d
%define render %mklibname qt%{major}3drender %{major}
%define renderd %mklibname qt%{major}3drender -d
%define extrasd %mklibname qt%{major}3dextras -d
%define quickextrasd %mklibname qt%{major}3dquickextras -d

Name:		qt5-qt3d
Version:	5.12.0
%if "%{beta}" != ""
Release:	0.%{beta}.1
%define qttarballdir qt3d-everywhere-src-%{version}-%{beta}
Source0:	http://download.qt.io/development_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}%{?beta:-%{beta}}/submodules/%{qttarballdir}.tar.xz
%else
Release:	1
%define qttarballdir qt3d-everywhere-src-%{version}
Source0:	http://download.qt.io/official_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}/submodules/%{qttarballdir}.tar.xz
%endif
Summary:	Qt 3D toolkit
Group:		System/Libraries
License:	LGPLv2 with exceptions or GPLv3 with exceptions and GFDL
URL:		http://www.qt.io/
BuildRequires:	qmake5 >= %{version}
BuildRequires:	pkgconfig(Qt5Core) >= %{version}
BuildRequires:	pkgconfig(Qt5Gui) >= %{version}
BuildRequires:	pkgconfig(Qt5Quick) >= %{version}
BuildRequires:	pkgconfig(Qt5Qml) >= %{version}
BuildRequires:	pkgconfig(Qt5Network) >= %{version}
BuildRequires:	pkgconfig(Qt5XmlPatterns) >= %{version}
BuildRequires:	pkgconfig(Qt5OpenGL) >= %{version}
BuildRequires:	pkgconfig(Qt5Concurrent) >= %{version}
BuildRequires:	pkgconfig(zlib)
#BuildRequires:	pkgconfig(assimp)
BuildRequires:	qt5-qtqml-private-devel >= %{version}
BuildRequires:	qt5-qtquick-private-devel >= %{version}
Requires:	%{core} = %{EVRD}
Requires:	%{animation} = %{EVRD}
Requires:	%{input} = %{EVRD}
Requires:	%{logic} = %{EVRD}
Requires:	%{quick} = %{EVRD}
Requires:	%{quickrender} = %{EVRD}
Requires:	%{quickscene2d} = %{EVRD}
Requires:	%{render} = %{EVRD}
Requires:       qt5-qtimageformats >= %{version}
Obsoletes:	%{mklibname qt53dcollision 5} < 5.6.0
Obsoletes:	%{mklibname qt53dcollision -d} < 5.6.0
# For the Provides: generator
BuildRequires:	cmake >= 3.11.0-1

%description
Qt5 3D API.

%files
%{_libdir}/qt5/plugins/sceneparsers

# ===
%package devel
Summary:	Development files for the Qt 3D library
Group:		Development/KDE and Qt
Requires:	%{cored} = %{EVRD}
Requires:	%{animationd} = %{EVRD}
Requires:	%{inputd} = %{EVRD}
Requires:	%{quickd} = %{EVRD}
Requires:	%{quickrenderd} = %{EVRD}
Requires:	%{quickscene2dd} = %{EVRD}
Requires:	%{renderd} = %{EVRD}

%description devel
Development files for the Qt 3D library.

%files devel
# disable examples due bug
# https://bugreports.qt.io/browse/QTBUG-41301
#% {_libdir}/qt5/examples/qt3d
%{_libdir}/qt5/bin/qgltf

# =====
%package -n %{core}
Summary:	Qt3D core library
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{core}
Qt3D core library.

%files -n %{core}
%{_libdir}/libQt%{major}3DCore.so.%{major}*
%dir %{_libdir}/qt5/plugins/geometryloaders
%{_libdir}/qt5/plugins/geometryloaders/libdefaultgeometryloader.so
%{_libdir}/qt5/plugins/geometryloaders/libgltfgeometryloader.so

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
%package -n %{animation}
Summary:	Qt3D animation library
Group:		System/Libraries

%description -n %{animation}
Qt3D animation library.

%files -n %{animation}
%{_libdir}/libQt%{major}3DAnimation.so.%{major}*

%package -n %{animationd}
Summary:	Development files for the Qt3D animation library
Group:		Development/KDE and Qt
Requires:	%{animation} = %{EVRD}

%description -n %{animationd}
Development files for the Qt3D animation library.

%files -n %{animationd}
%{_includedir}/qt%{major}/Qt3DAnimation
%{_libdir}/cmake/Qt%{major}3DAnimation
%{_libdir}/libQt%{major}3DAnimation.so
%{_libdir}/libQt%{major}3DAnimation.prl
%{_libdir}/pkgconfig/Qt%{major}3DAnimation.pc
%{_libdir}/qt%{major}/mkspecs/modules/qt_lib_3danimation.pri
%{_libdir}/qt%{major}/mkspecs/modules/qt_lib_3danimation_private.pri

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

%package -n %{logic}
Summary:	Qt3D logic library
Group:		System/Libraries

%description -n %{logic}
Qt3D logic library.

%files -n %{logic}
%{_libdir}/libQt%{major}3DLogic.so.%{major}*

%package -n %{logicd}
Summary:	Development files for the Qt3D logic library
Group:		Development/KDE and Qt
Requires:	%{logic} = %{EVRD}

%description -n %{logicd}
Development files for the Qt3D logic library.

%files -n %{logicd}
%{_includedir}/qt%{major}/Qt3DLogic
%{_libdir}/cmake/Qt%{major}3DLogic
%{_libdir}/libQt%{major}3DLogic.so
%{_libdir}/libQt%{major}3DLogic.prl
%{_libdir}/pkgconfig/Qt%{major}3DLogic.pc
%{_libdir}/qt%{major}/mkspecs/modules/qt_lib_3dlogic.pri
%{_libdir}/qt%{major}/mkspecs/modules/qt_lib_3dlogic_private.pri
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
%package -n %{quickanimation}
Summary:	Qt3D Quick Animation library
Group:		System/Libraries

%description -n %{quickanimation}
Qt3D Quick Animation library.

%files -n %{quickanimation}
%{_libdir}/libQt%{major}3DQuickAnimation.so.%{major}*

%package -n %{quickanimationd}
Summary:	Development files for the Qt3D Quick Animation library
Group:		Development/KDE and Qt
Requires:	%{quickanimation} = %{EVRD}

%description -n %{quickanimationd}
Development files for the Qt3D Quick Animation library.

%files -n %{quickanimationd}
%{_includedir}/qt%{major}/Qt3DQuickAnimation
%{_libdir}/cmake/Qt%{major}3DQuickAnimation
%{_libdir}/libQt%{major}3DQuickAnimation.so
%{_libdir}/libQt%{major}3DQuickAnimation.prl
%{_libdir}/pkgconfig/Qt%{major}3DQuickAnimation.pc
%{_libdir}/qt%{major}/mkspecs/modules/qt_lib_3dquickanimation.pri
%{_libdir}/qt%{major}/mkspecs/modules/qt_lib_3dquickanimation_private.pri

# =====
%package -n %{quickinput}
Summary:	Qt3D QuickInput library
Group:		System/Libraries

%description -n %{quickinput}
Qt3D QuickInput library.

%files -n %{quickinput}
%{_libdir}/libQt%{major}3DQuickInput.so.%{major}*

%package -n %{quickinputd}
Summary:	Development files for the Qt3D QuickInput library
Group:		Development/KDE and Qt
Requires:	%{quickinput} = %{EVRD}

%description -n %{quickinputd}
Development files for the Qt3D QuickInput library.

%files -n %{quickinputd}
%{_includedir}/qt%{major}/Qt3DQuickInput
%{_libdir}/cmake/Qt%{major}3DQuickInput
%{_libdir}/libQt%{major}3DQuickInput.so
%{_libdir}/libQt%{major}3DQuickInput.prl
%{_libdir}/pkgconfig/Qt%{major}3DQuickInput.pc
%{_libdir}/qt%{major}/mkspecs/modules/qt_lib_3dquickinput.pri
%{_libdir}/qt%{major}/mkspecs/modules/qt_lib_3dquickinput_private.pri

# =====
%package -n %{quickrender}
Summary:	Qt3D QuickRender library
Group:		System/Libraries
Obsoletes:	%{_lib}qt53dquickrenderer5 < 5.6.0

%description -n %{quickrender}
Qt3D QuickRenderer library.

%files -n %{quickrender}
%{_libdir}/libQt%{major}3DQuickRender.so.%{major}*

%package -n %{quickrenderd}
Summary:	Development files for the Qt3D QuickRender library
Group:		Development/KDE and Qt
Requires:	%{quickrender} = %{EVRD}
Obsoletes:	%{_lib}qt53dquickrenderer-devel < 5.6.0

%description -n %{quickrenderd}
Development files for the Qt3D QuickRender library.

%files -n %{quickrenderd}
%{_includedir}/qt%{major}/Qt3DQuickRender
%{_libdir}/cmake/Qt%{major}3DQuickRender
%{_libdir}/libQt%{major}3DQuickRender.so
%{_libdir}/libQt%{major}3DQuickRender.prl
%{_libdir}/pkgconfig/Qt%{major}3DQuickRender.pc
%{_libdir}/qt%{major}/mkspecs/modules/qt_lib_3dquickrender.pri
%{_libdir}/qt%{major}/mkspecs/modules/qt_lib_3dquickrender_private.pri

# =====
%package -n %{quickscene2d}
Summary:	Qt3D Quick 2D Scene library
Group:		System/Libraries

%description -n %{quickscene2d}
Qt3D Quick 2D Scene library.

%files -n %{quickscene2d}
%{_libdir}/libQt%{major}3DQuickScene2D.so.%{major}*
%{_libdir}/qt5/qml/QtQuick/Scene2D
%{_libdir}/qt5/plugins/renderplugins/libscene2d.so

%package -n %{quickscene2dd}
Summary:	Development files for the Qt3D Quick 2D Scene library
Group:		Development/KDE and Qt
Requires:	%{quickscene2d} = %{EVRD}

%description -n %{quickscene2dd}
Development files for the Qt3D Quick 2D Scene library.

%files -n %{quickscene2dd}
%{_includedir}/qt%{major}/Qt3DQuickScene2D
%{_libdir}/cmake/Qt%{major}3DQuickScene2D
%{_libdir}/libQt%{major}3DQuickScene2D.so
%{_libdir}/libQt%{major}3DQuickScene2D.prl
%{_libdir}/pkgconfig/Qt%{major}3DQuickScene2D.pc
%{_libdir}/qt%{major}/mkspecs/modules/qt_lib_3dquickscene2d.pri
%{_libdir}/qt%{major}/mkspecs/modules/qt_lib_3dquickscene2d_private.pri

# =====
%package -n %{render}
Summary:	Qt3D render library
Group:		System/Libraries
Obsoletes:	%{_lib}qt53drender5 < 5.6.0

%description -n %{render}
Qt3D renderer library.

%files -n %{render}
%{_libdir}/libQt%{major}3DRender.so.%{major}*

%package -n %{renderd}
Summary:	Development files for the Qt3D renderer library
Group:		Development/KDE and Qt
Requires:	%{render} = %{EVRD}
Obsoletes:	%{_lib}qt53drender-devel < 5.6.0

%description -n %{renderd}
Development files for the Qt3D renderer library.

%files -n %{renderd}
%{_includedir}/qt%{major}/Qt3DRender
%{_libdir}/cmake/Qt%{major}3DRender
%{_libdir}/libQt%{major}3DRender.so
%{_libdir}/libQt%{major}3DRender.prl
%{_libdir}/pkgconfig/Qt%{major}3DRender.pc
%{_libdir}/qt%{major}/mkspecs/modules/qt_lib_3drender.pri
%{_libdir}/qt%{major}/mkspecs/modules/qt_lib_3drender_private.pri


%libpackage Qt53DExtras 5

%libpackage Qt53DQuickExtras 5


%package -n %{extrasd}
Summary:	Development files for the Qt3DExtras library
Group:		Development/KDE and Qt
Requires:	%{mklibname Qt53DExtras 5} = %{EVRD}

%description -n %{extrasd}
Development files for the Qt3DExtras library.

%files -n %{extrasd}
%{_includedir}/qt%{major}/Qt3DExtras
%{_libdir}/libQt53DExtras.so
%{_libdir}/libQt53DExtras.prl
%{_libdir}/pkgconfig/Qt53DExtras.pc
%{_libdir}/qt5/mkspecs/modules/qt_lib_3dextras.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_3dextras_private.pri
%{_libdir}/cmake/Qt53DExtras

%package -n %{quickextrasd}
Summary:	Development files for the Qt3DQuickExtras library
Group:		Development/KDE and Qt
Requires:	%{mklibname Qt53DQuickExtras 5} = %{EVRD}

%description -n %{quickextrasd}
Development files for the Qt3DQuickExtras library.

%files -n %{quickextrasd}
%{_includedir}/qt%{major}/Qt3DQuickExtras
%{_libdir}/libQt53DQuickExtras.so
%{_libdir}/libQt53DQuickExtras.prl
%{_libdir}/pkgconfig/Qt53DQuickExtras.pc
%{_libdir}/qt5/mkspecs/modules/qt_lib_3dquickextras.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_3dquickextras_private.pri
%{_libdir}/cmake/Qt53DQuickExtras

#------------------------------------------------------------------------------

%prep
%autosetup -n %qttarballdir -p1
# disable examples due bug
# https://bugreports.qt.io/browse/QTBUG-41301
rm -rf examples/

%build
%qmake_qt5
%make_build

#------------------------------------------------------------------------------

%install
%make_install INSTALL_ROOT=%{buildroot}

## .prl/.la file love
# nuke .prl reference(s) to %%buildroot, excessive (.la-like) libs
pushd %{buildroot}%{_libdir}
for prl_file in libQt5*.prl ; do
  sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" ${prl_file}
  if [ -f "$(basename ${prl_file} .prl).so" ]; then
    rm -fv "$(basename ${prl_file} .prl).la"
    sed -i -e "/^QMAKE_PRL_LIBS/d" ${prl_file}
  fi
done
popd
