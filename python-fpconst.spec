
%include	/usr/lib/rpm/macros.python
%define 	module fpconst

Summary:	IEEE 754 floating point special handling
Summary(pl):	Specjalna obsługa liczb zmiennoprzecinkowych IEEE 754
Name:		python-%{module}
Version:	0.6.0
Release:	2
License:	GPL
Group:		Libraries/Python
Source0:	http://www.analytics.washington.edu/Zope/projects/fpconst/%{module}-%{version}.tar.gz
# Source0-md5:	5eaf8e8d1978ca4bbead5b3f163b23a1
URL:		http://www.analytics.washington.edu/Zope/projects/fpconst/
BuildRequires:	python-devel
Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This python module implements constants and functions for working with
IEEE 754 double-precision special values. It provides constants for
Not-a-Number (NaN), Positive Infinity (Inf), and Negative Infinity
(-Inf), as well as functions to test for these values.

%description -l pl
Ten moduł Pythona jest implementacją stałych i funkcji do pracy z
wartościami specjalnymi liczb podwójnej precyzji zgodnymi z IEEE 754.
Udostępnia stałe dla nie-liczb (NaN, czyli Not-a-Number), dodatniej
nieskończoności (Inf) i ujemnej nieskończoności (-Inf), a także
funkcje do porównywania z tymi wartościami.

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="%{rpmcflags}"
export CLFAGS
python setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}

python setup.py install \
        --root=$RPM_BUILD_ROOT \
	--optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%{py_sitedir}/*.py?
