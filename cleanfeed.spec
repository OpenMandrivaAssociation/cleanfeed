Summary:	A spam filter for Usenet news servers
Name:		cleanfeed
Version:	20020501
Release:	21
License:	Artistic
Group:		System/Servers
Url:		https://www.bofh.it/~md/cleanfeed/
Source0:	http://www.bofh.it/~md/cleanfeed/%{name}-%{version}.tgz
Patch0:		cleanfeed-20020501-config.patch
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
%autopatch -p1

chmod 644 CHANGES README

%install
mkdir -p %{buildroot}/{%{_sysconfdir}/news,%{_mandir}/man8,%{_libdir}/news/bin/control}
install -m 0644 cleanfeed.local.sample %{buildroot}/%{_sysconfdir}/news/cleanfeed.local
install -m 0644 bad_adult_paths %{buildroot}/%{_sysconfdir}/news
install -m 0644 bad_cancel_paths %{buildroot}/%{_sysconfdir}/news
install -m 0644 bad_paths %{buildroot}/%{_sysconfdir}/news
install -m 0644 bad_hosts %{buildroot}/%{_sysconfdir}/news
install -m 0755 cleanfeed %{buildroot}/%{_libdir}/news/bin/control/filter_innd.pl

%files
%doc CHANGES README
%attr(-,news,news) %config(noreplace) %{_sysconfdir}/news/cleanfeed.local
%attr(-,news,news) %config(noreplace) %{_sysconfdir}/news/bad_adult_paths
%attr(-,news,news) %config(noreplace) %{_sysconfdir}/news/bad_cancel_paths
%attr(-,news,news) %config(noreplace) %{_sysconfdir}/news/bad_paths
%attr(-,news,news) %config(noreplace) %{_sysconfdir}/news/bad_hosts
%attr(-,news,news) %{_libdir}/news/bin/control/filter_innd.pl

