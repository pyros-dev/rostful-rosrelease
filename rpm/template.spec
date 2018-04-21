Name:           ros-kinetic-rostful
Version:        0.2.0
Release:        2%{?dist}
Summary:        ROS rostful package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       PyYAML
Requires:       python-flask
Requires:       python-flask-restful >= 0.3.4
Requires:       python-simplejson
Requires:       ros-kinetic-click >= 6.2.0
Requires:       ros-kinetic-flask-cors >= 3.0.2
Requires:       ros-kinetic-flask-reverse-proxy >= 0.2.0
Requires:       ros-kinetic-pyros >= 0.3.0
Requires:       ros-kinetic-rospy
Requires:       ros-kinetic-tblib >= 1.2.0
Requires:       ros-kinetic-webargs >= 1.3.4
BuildRequires:  PyYAML
BuildRequires:  python-catkin_pkg
BuildRequires:  python-flask
BuildRequires:  python-flask-restful >= 0.3.4
BuildRequires:  python-simplejson
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-catkin-pip >= 0.2.3
BuildRequires:  ros-kinetic-click >= 6.2.0
BuildRequires:  ros-kinetic-flask-cors >= 3.0.2
BuildRequires:  ros-kinetic-flask-reverse-proxy >= 0.2.0
BuildRequires:  ros-kinetic-pyros >= 0.3.0
BuildRequires:  ros-kinetic-roslint
BuildRequires:  ros-kinetic-rospy
BuildRequires:  ros-kinetic-rostest
BuildRequires:  ros-kinetic-rosunit
BuildRequires:  ros-kinetic-tblib >= 1.2.0
BuildRequires:  ros-kinetic-webargs >= 1.3.4

%description
REST API for ROS

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
* Sat Apr 21 2018 AlexV <asmodehn@gmail.com> - 0.2.0-2
- Autogenerated by Bloom

* Sat Apr 21 2018 AlexV <asmodehn@gmail.com> - 0.2.0-1
- Autogenerated by Bloom

* Sat Apr 21 2018 AlexV <asmodehn@gmail.com> - 0.2.0-0
- Autogenerated by Bloom

