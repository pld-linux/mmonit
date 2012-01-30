# TODO
# - package
# - use system, libz, etc
Summary:	Proactive monitoring of Linux/Unix systems, network and cloud services
Name:		mmonit
Version:	2.4
Release:	0.1
License:	Binary
Group:		Daemons
Source0:	http://mmonit.com/dist/%{name}-%{version}-linux-x86.tar.gz
# NoSource0-md5:	daeb5d806ef0217e28c34e7a28656571
NoSource:	0
Source1:	http://mmonit.com/dist/%{name}-%{version}-linux-x64.tar.gz
# NoSource1-md5:	6209869dad5e4a5e44d42bbce50acb5c
NoSource:	1
URL:		http://mmonit.com/
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
M/Monit is a system for automatic management and monitoring of
Information Technology Systems. M/Monit can monitor and manage
distributed computer systems, conduct automatic maintenance and repair
and execute meaningful causal actions in error situations.

M/Monit expand upon Monit's capabilities to provide monitoring and
management of all Monit enabled hosts from one easy to use
web-interface.

%prep
%ifarch %{ix86}
%setup -qT -b0
%endif
%ifarch %{x8664}
%setup -qT -b1
%endif

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
