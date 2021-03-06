
%define 	module	fpconst

Summary:	IEEE 754 floating point special handling
Summary(pl.UTF-8):	Specjalna obsługa liczb zmiennoprzecinkowych IEEE 754
Name:		python-%{module}
Version:	0.7.2
Release:	6
License:	Apache v2.0
Group:		Libraries/Python
Source0:	http://cheeseshop.python.org/packages/source/f/fpconst/fpconst-%{version}.tar.gz
# Source0-md5:	10ba9e04129af23108d24c22c3a698b1
URL:		http://research.warnes.net/projects/RStatServer/fpconst/index_html
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	python >= 1:2.5
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This python module implements constants and functions for working with
IEEE 754 double-precision special values. It provides constants for
Not-a-Number (NaN), Positive Infinity (Inf), and Negative Infinity
(-Inf), as well as functions to test for these values.

%description -l pl.UTF-8
Ten moduł Pythona jest implementacją stałych i funkcji do pracy z
wartościami specjalnymi liczb podwójnej precyzji zgodnymi z IEEE 754.
Udostępnia stałe dla nie-liczb (NaN, czyli Not-a-Number), dodatniej
nieskończoności (Inf) i ujemnej nieskończoności (-Inf), a także
funkcje do porównywania z tymi wartościami.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}

%py_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{py_sitescriptdir}/*.py[co]
%{py_sitescriptdir}/*.egg-info
