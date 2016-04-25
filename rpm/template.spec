Name:           ros-indigo-rosapi
Version:        0.7.14
Release:        1%{?dist}
Summary:        ROS rosapi package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rosapi
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-rosbridge-library
Requires:       ros-indigo-rosgraph
Requires:       ros-indigo-rosnode
Requires:       ros-indigo-rospy
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-rospy

%description
Provides service calls for getting ros meta-information, like list of topics,
services, params, etc.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Apr 25 2016 Russell Toris <rctoris@wpi.edu> - 0.7.14-1
- Autogenerated by Bloom

* Thu Feb 11 2016 Russell Toris <rctoris@wpi.edu> - 0.7.14-0
- Autogenerated by Bloom

* Fri Aug 14 2015 Russell Toris <rctoris@wpi.edu> - 0.7.13-0
- Autogenerated by Bloom

* Tue Apr 07 2015 Russell Toris <rctoris@wpi.edu> - 0.7.12-0
- Autogenerated by Bloom

* Mon Mar 23 2015 Russell Toris <rctoris@wpi.edu> - 0.7.11-0
- Autogenerated by Bloom

* Wed Feb 25 2015 Russell Toris <rctoris@wpi.edu> - 0.7.10-0
- Autogenerated by Bloom

* Tue Feb 24 2015 Russell Toris <rctoris@wpi.edu> - 0.7.9-0
- Autogenerated by Bloom

* Fri Jan 16 2015 Russell Toris <rctoris@wpi.edu> - 0.7.8-0
- Autogenerated by Bloom

* Tue Jan 06 2015 Russell Toris <rctoris@wpi.edu> - 0.7.7-0
- Autogenerated by Bloom

* Fri Dec 26 2014 Russell Toris <rctoris@wpi.edu> - 0.7.6-0
- Autogenerated by Bloom

* Fri Dec 26 2014 Russell Toris <rctoris@wpi.edu> - 0.7.5-0
- Autogenerated by Bloom

* Tue Dec 16 2014 Russell Toris <rctoris@wpi.edu> - 0.7.4-0
- Autogenerated by Bloom

