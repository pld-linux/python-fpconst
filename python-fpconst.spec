
%define 	module	fpconst

Summary:	IEEE 754 floating point special handling
Summary(pl):	Specjalna obs³uga liczb zmiennoprzecinkowych IEEE 754
Name:		python-%{module}
Version:	0.7.2
Release:	1
License:	Apache License 2.0
Group:		Libraries/Python
Source0:	http://cheeseshop.python.org/packages/source/f/fpconst/fpconst-%{version}.tar.gz
# Source0-md5:	10ba9e04129af23108d24c22c3a698b1
URL:		http://research.warnes.net/projects/RStatServer/fpconst/index_html
BuildRequires:	python >= 1:2.5
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This python module implements constants and functions for working with
IEEE 754 double-precision special values. It provides constants for
Not-a-Number (NaN), Positive Infinity (Inf), and Negative Infinity
(-Inf), as well as functions to test for these values.

%description -l pl
Ten modu³ Pythona jest implementacj± sta³ych i funkcji do pracy z
warto¶ciami specjalnymi liczb podwójnej precyzji zgodnymi z IEEE 754.
Udostêpnia sta³e dla nie-liczb (NaN, czyli Not-a-Number), dodatniej
nieskoñczono¶ci (Inf) i ujemnej nieskoñczono¶ci (-Inf), a tak¿e
funkcje do porównywania z tymi warto¶ciami.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{py_sitescriptdir}/*.py?
%{py_sitescriptdir}/*.egg-info
