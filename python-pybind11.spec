# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-pybind11
Epoch: 100
Version: 2.13.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Seamless operability between C++11 and Python
License: BSD-3-Clause
URL: https://github.com/pybind/pybind11/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: cmake >= 3.4
BuildRequires: fdupes
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
pybind11 is a lightweight header-only library that exposes C++ types in
Python and vice versa, mainly to create Python bindings of existing C++
code.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build
%cmake \
    -DPYBIND11_INSTALL="ON" \
    -DPYBIND11_TEST="OFF"
%cmake_build

%install
%py3_install
%cmake_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}
rm -rf %{buildroot}%{_includedir}/python*

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-pybind11
Summary: Module for operability between C++11 and Python
Requires: python3
Provides: python3-pybind11 = %{epoch}:%{version}-%{release}
Provides: python3dist(pybind11) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pybind11 = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pybind11) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pybind11 = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pybind11) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-pybind11
pybind11 is a lightweight header-only library that exposes C++ types in
Python and vice versa, mainly to create Python bindings of existing C++
code.

%package -n python-pybind11-common-devel
Summary: Development files for pybind11
Provides: python2-pybind11-common-devel = %{epoch}:%{version}-%{release}
Provides: python3-pybind11-common-devel = %{epoch}:%{version}-%{release}
Provides: python3dist(pybind11-common-devel) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pybind11-common-devel = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pybind11-common-devel) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pybind11-common-devel = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pybind11-common-devel) = %{epoch}:%{version}-%{release}

%description -n python-pybind11-common-devel
This package contains files for developing applications using pybind11.

%package -n python%{python3_version_nodots}-pybind11-devel
Summary: Development files for pybind11
Requires: python-pybind11-common-devel = %{epoch}:%{version}-%{release}
Requires: python3-devel
Requires: python3-pybind11 = %{epoch}:%{version}-%{release}
Provides: python3-pybind11-devel = %{epoch}:%{version}-%{release}
Provides: python3dist(pybind11-devel) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pybind11-devel = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pybind11-devel) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pybind11-devel = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pybind11-devel) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-pybind11-devel
This package contains files for developing applications using pybind11.

%files -n python%{python3_version_nodots}-pybind11
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%exclude %{python3_sitelib}/pybind11/include

%files -n python-pybind11-common-devel
%dir %{_datadir}/cmake
%{_datadir}/cmake/pybind11
%{_datadir}/pkgconfig/pybind11.pc
%{_includedir}/pybind11

%files -n python%{python3_version_nodots}-pybind11-devel
%{python3_sitelib}/pybind11/include
%endif

%if 0%{?sle_version} > 150000
%package -n python3-pybind11
Summary: Module for operability between C++11 and Python
Requires: python3
Provides: python3-pybind11 = %{epoch}:%{version}-%{release}
Provides: python3dist(pybind11) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pybind11 = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pybind11) = %{epoch}:%{version}-%{release}
Provides: python3-pybind11 = %{epoch}:%{version}-%{release}
Provides: python3dist(pybind11) = %{epoch}:%{version}-%{release}

%description -n python3-pybind11
pybind11 is a lightweight header-only library that exposes C++ types in
Python and vice versa, mainly to create Python bindings of existing C++
code.

%package -n python-pybind11-common-devel
Summary: Development files for pybind11
Provides: python2-pybind11-common-devel = %{epoch}:%{version}-%{release}
Provides: python3-pybind11-common-devel = %{epoch}:%{version}-%{release}
Provides: python3dist(pybind11-common-devel) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pybind11-common-devel = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pybind11-common-devel) = %{epoch}:%{version}-%{release}
Provides: python3-pybind11-common-devel = %{epoch}:%{version}-%{release}
Provides: python3dist(pybind11-common-devel) = %{epoch}:%{version}-%{release}

%description -n python-pybind11-common-devel
This package contains files for developing applications using pybind11.

%package -n python3-pybind11-devel
Summary: Development files for pybind11
Requires: python-pybind11-common-devel = %{epoch}:%{version}-%{release}
Requires: python3-devel
Requires: python3-pybind11 = %{epoch}:%{version}-%{release}
Provides: python3-pybind11-devel = %{epoch}:%{version}-%{release}
Provides: python3dist(pybind11-devel) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pybind11-devel = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pybind11-devel) = %{epoch}:%{version}-%{release}
Provides: python3-pybind11-devel = %{epoch}:%{version}-%{release}
Provides: python3dist(pybind11-devel) = %{epoch}:%{version}-%{release}

%description -n python3-pybind11-devel
This package contains files for developing applications using pybind11.

%files -n python3-pybind11
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%exclude %{python3_sitelib}/pybind11/include

%files -n python-pybind11-common-devel
%dir %{_datadir}/cmake
%{_datadir}/cmake/pybind11
%{_datadir}/pkgconfig/pybind11.pc
%{_includedir}/pybind11

%files -n python3-pybind11-devel
%{python3_sitelib}/pybind11/include
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-pybind11
Summary: Seamless operability between C++11 and Python
Requires: python3
Requires: pybind11-devel = %{epoch}:%{version}-%{release}
Provides: python3-pybind11 = %{epoch}:%{version}-%{release}
Provides: python3dist(pybind11) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pybind11 = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pybind11) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pybind11 = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pybind11) = %{epoch}:%{version}-%{release}

%description -n python3-pybind11
pybind11 is a lightweight header-only library that exposes C++ types in
Python and vice versa, mainly to create Python bindings of existing C++
code.

%package -n pybind11-devel
Summary: Development headers for pybind11
Requires: cmake
Provides: pybind11-static = %{epoch}:%{version}-%{release}
Provides: python3-pybind11-devel = %{epoch}:%{version}-%{release}
Provides: python3dist(pybind11-devel) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pybind11-devel = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pybind11-devel) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pybind11-devel = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pybind11-devel) = %{epoch}:%{version}-%{release}

%description -n pybind11-devel
This package contains the development headers for pybind11.

%files -n python3-pybind11
%license LICENSE
%{_bindir}/pybind11-config
%{python3_sitelib}/*
%exclude %{python3_sitelib}/pybind11/include

%files -n pybind11-devel
%dir %{_datadir}/cmake
%{_datadir}/cmake/pybind11
%{_datadir}/pkgconfig/pybind11.pc
%{_includedir}/pybind11
%{python3_sitelib}/pybind11/include
%endif

%changelog
