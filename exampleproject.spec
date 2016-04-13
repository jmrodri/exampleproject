%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name: exampleproject
Version: 1.0.2
Release: 1%{?dist}
Summary: Example hello world project

Group: Development/Tools
License: GPLv2
URL: http://github.com/jmrodri/exampleproject
Source: %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: noarch

%description
Example hello world project
Use merge

%prep
%setup -q -n %{name}-%{version}


%build

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT/%{_datadir}/%{name}/
install -m 755 hello.py $RPM_BUILD_ROOT/%{_datadir}/%{name}/hello.py

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_datadir}/%{name}/hello.py*

%changelog
* Sat Jan 14 2012 jesus m. rodriguez <jmrodri@gmail.com> 1.0.2-1
- test commit (jmrodri@gmail.com)

* Sat Jan 14 2012 jesus m. rodriguez <jmrodri@gmail.com> 1.0.1-1
- new package built with tito


