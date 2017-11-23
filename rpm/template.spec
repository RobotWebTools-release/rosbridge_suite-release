Name:           ros-kinetic-rosbridge-suite
Version:        0.8.5
Release:        0%{?dist}
Summary:        ROS rosbridge_suite package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rosbridge_suite
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-kinetic-rosapi
Requires:       ros-kinetic-rosbridge-library
Requires:       ros-kinetic-rosbridge-server
BuildRequires:  ros-kinetic-catkin

%description
Rosbridge provides a JSON API to ROS functionality for non-ROS programs. There
are a variety of front ends that interface with rosbridge, including a WebSocket
server for web browsers to interact with. Rosbridge_suite is a meta-package
containing rosbridge, various front end packages for rosbridge like a WebSocket
package, and helper packages.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Thu Nov 23 2017 Russell Toris <rctoris@wpi.edu> - 0.8.5-0
- Autogenerated by Bloom

* Mon Oct 16 2017 Russell Toris <rctoris@wpi.edu> - 0.8.4-0
- Autogenerated by Bloom

* Mon Sep 11 2017 Russell Toris <rctoris@wpi.edu> - 0.8.3-0
- Autogenerated by Bloom

* Wed Aug 30 2017 Russell Toris <rctoris@wpi.edu> - 0.8.1-2
- Autogenerated by Bloom

* Wed Aug 30 2017 Russell Toris <rctoris@wpi.edu> - 0.8.1-1
- Autogenerated by Bloom

* Wed Aug 30 2017 Russell Toris <rctoris@wpi.edu> - 0.8.1-0
- Autogenerated by Bloom

* Wed Jan 25 2017 Russell Toris <rctoris@wpi.edu> - 0.7.17-0
- Autogenerated by Bloom

* Mon Aug 15 2016 Russell Toris <rctoris@wpi.edu> - 0.7.16-0
- Autogenerated by Bloom

