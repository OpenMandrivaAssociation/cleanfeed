Summary:	A spam filter for Usenet news servers.
Name:		cleanfeed
%define version 0.95.7b
Version:	%{version}
Release:	%mkrel 14
License:	distributable
Group:		System/Servers
Source0:	ftp://ftp.exit109.com/users/jeremy/cleanfeed-%{version}.tar.bz2
Patch0:		cleanfeed-0.95.7b-redhat.patch
BuildRoot:	%{_tmppath}/%{name}-root
BuildArch:	noarch

%description
Cleanfeed is an automatic spam filter for Usenet news servers and
routers (INN, Cyclone, Typhoon, Breeze and NNTPRelay).  Cleanfeed is
highly configurable, easily modified and very fast.  It can be configured
to block binary posts to non-binary newsgroups, to cancel already-rejected
articles, and to reject some spamming from local users.

Install the cleanfeed package if you need a spam filter for a Usenet news
server.

%prep
%setup
%patch0 -p1 -b .rh

chmod 644 CHANGES README

%install
mkdir -p $RPM_BUILD_ROOT/{%{_sysconfdir}/news,%{_mandir}/man8,%{_libdir}/news/bin/control}
install -m 0644 cleanfeed.conf $RPM_BUILD_ROOT/%{_sysconfdir}/news/
install -m 0644 cleanfeed.8 $RPM_BUILD_ROOT/%{_mandir}/man8/
install -m 0755 cleanfeed $RPM_BUILD_ROOT/%{_libdir}/news/bin/control/filter_innd.pl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGES README
%{_mandir}/man8/cleanfeed.8*
%attr(-,news,news) %config(noreplace) %{_sysconfdir}/news/cleanfeed.conf
%attr(-,news,news) %{_libdir}/news/bin/control/filter_innd.pl

