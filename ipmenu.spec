%include	/usr/lib/rpm/macros.perl
Summary:	Netfilter/IPtables Rule Editor
Summary(pl.UTF-8):	Edytor regułek Netfiltera/IPtables
Name:		ipmenu
Version:	0.0.3
Release:	2
License:	GPL
Group:		Networking/Admin
Source0:	http://users.pandora.be/stes/%{name}-%{version}.tar.gz
# Source0-md5:	16e7747978074254c25240c1876a6bf9
Patch0:		%{name}-path.patch
URL:		http://users.pandora.be/stes/ipmenu.html
Requires:	cursel
Requires:	iproute2
Requires:	iptables
Conflicts:	kernel =< 2.4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It's a user interface to Netfilter/iptables and Linux policy routing
or traffic control, allowing you to edit firewall rules and configure
the firewall to "mark" packets for policy routing or for class based
queueing (CBQ). Netfilter is the Linux 2.4 subsystem for configuring a
multi-homed Linux server as a packet filter or as a NAT (network
address translation) device.

%description -l pl.UTF-8
Interfejs użytkownika do tablic polityki routingu, kontroli ruchu
pozwalając na edycję regułek firewalla (iptables) z możliwością
,,znakowania'' pakietów oraz szeregowania ich na podstawie polityki
routingu lub kolejkowania bazującego na klasach (CBQ).

%prep
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}

install *	$RPM_BUILD_ROOT%{_datadir}/%{name}/
ln -sf		%{_datadir}/%{name}/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ipmenu
%attr(-, root,root)  %{_datadir}/%{name}
