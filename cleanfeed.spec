%define name	cleanfeed
%define version 20020501
%define release %mkrel 11

Summary:	A spam filter for Usenet news servers
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic
Group:		System/Servers
URL:		http://www.bofh.it/~md/cleanfeed/
Source0:	http://www.bofh.it/~md/cleanfeed/%{name}-%{version}.tgz
Patch0:		cleanfeed-20020501-config.patch
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
%setup -q
%patch0 -p1 -b .config

chmod 644 CHANGES README

%install
mkdir -p $RPM_BUILD_ROOT/{%{_sysconfdir}/news,%{_mandir}/man8,%{_libdir}/news/bin/control}
install -m 0644 cleanfeed.local.sample $RPM_BUILD_ROOT/%{_sysconfdir}/news/cleanfeed.local
install -m 0644 bad_adult_paths $RPM_BUILD_ROOT/%{_sysconfdir}/news
install -m 0644 bad_cancel_paths $RPM_BUILD_ROOT/%{_sysconfdir}/news
install -m 0644 bad_paths $RPM_BUILD_ROOT/%{_sysconfdir}/news
install -m 0644 bad_hosts $RPM_BUILD_ROOT/%{_sysconfdir}/news
install -m 0755 cleanfeed $RPM_BUILD_ROOT/%{_libdir}/news/bin/control/filter_innd.pl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGES README
%attr(-,news,news) %config(noreplace) %{_sysconfdir}/news/cleanfeed.local
%attr(-,news,news) %config(noreplace) %{_sysconfdir}/news/bad_adult_paths
%attr(-,news,news) %config(noreplace) %{_sysconfdir}/news/bad_cancel_paths
%attr(-,news,news) %config(noreplace) %{_sysconfdir}/news/bad_paths
%attr(-,news,news) %config(noreplace) %{_sysconfdir}/news/bad_hosts
%attr(-,news,news) %{_libdir}/news/bin/control/filter_innd.pl



%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 20020501-9mdv2011.0
+ Revision: 663382
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 20020501-8mdv2011.0
+ Revision: 603837
- rebuild

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 20020501-7mdv2010.1
+ Revision: 520022
- rebuilt for 2010.1

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 20020501-6mdv2010.0
+ Revision: 413241
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 20020501-5mdv2009.1
+ Revision: 350404
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 20020501-4mdv2009.1
+ Revision: 350236
- 2009.1 rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 20020501-3mdv2009.0
+ Revision: 220502
- rebuild

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 20020501-2mdv2008.1
+ Revision: 149100
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- fix summary-ended-with-dot

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Jun 19 2007 Adam Williamson <awilliamson@mandriva.org> 20020501-1mdv2008.0
+ Revision: 41211
- 'new' release 20020501; no more man page; new config files; correct license; update patch; rebuild for 2008


* Mon Aug 14 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/14/06 09:33:59 (55905)
- mkrelisation

* Mon Aug 14 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/14/06 09:32:07 (55904)
Import cleanfeed

* Wed Sep 01 2004 Arnaud de Lorbeau <adelorbeau@mandrakesoft.com> 0.95.7b-13mdk
- rebuild

