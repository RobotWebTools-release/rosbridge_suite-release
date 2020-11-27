%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-rosbridge-server
Version:        0.11.12
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS rosbridge_server package

License:        BSD
URL:            http://ros.org/wiki/rosbridge_server
Source0:        %{name}-%{version}.tar.gz

Requires:       python3-autobahn
Requires:       python3-tornado
Requires:       python3-twisted
Requires:       ros-noetic-rosapi
Requires:       ros-noetic-rosauth
Requires:       ros-noetic-rosbridge-library
Requires:       ros-noetic-rosbridge-msgs
Requires:       ros-noetic-rospy
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-rostest
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
A WebSocket interface to rosbridge.

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Fri Nov 27 2020 Russell Toris <rctoris@wpi.edu> - 0.11.12-1
- Autogenerated by Bloom

* Tue Nov 24 2020 Russell Toris <rctoris@wpi.edu> - 0.11.11-1
- Autogenerated by Bloom

* Tue Sep 08 2020 Russell Toris <rctoris@wpi.edu> - 0.11.10-1
- Autogenerated by Bloom

* Fri May 29 2020 Russell Toris <rctoris@wpi.edu> - 0.11.9-1
- Autogenerated by Bloom

* Wed May 27 2020 Russell Toris <rctoris@wpi.edu> - 0.11.8-1
- Autogenerated by Bloom

