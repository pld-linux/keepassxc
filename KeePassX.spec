Summary:	KeePassX - Cross Platform Password Manager
Summary(pl.UTF-8):	KeePassX - Wieloplatformowy zarządca haseł
Name:		KeePassX
Version:	0.4.3
Release:	2
License:	GPL v2+
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/keepassx/keepassx-%{version}.tar.gz
# Source0-md5:	1df67bb22b2e08df49f09e61d156f508
URL:		http://keepassx.sourceforge.net/
Patch1:		keepassx-0.3.3-gcc43.patch
Patch2:		keepassx-0.4.3-gcc47.patch
BuildRequires:	Qt3Support-devel >= 4.0
BuildRequires:	QtGui-devel >= 4.0
BuildRequires:	QtXml-devel >= 4.0
BuildRequires:	qt4-build >= 4.3.3-3
BuildRequires:	qt4-qmake >= 4.3.3-3
BuildRequires:	rpmbuild(macros) >= 1.230
BuildRequires:	xorg-lib-libXtst-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KeePassX is a free/open-source password manager or safe which helps
you to manage your passwords in a secure way. You can put all your
passwords in one database, which is locked with one master key or a
key-disk. So you only have to remember one single master password or
insert the key-disk to unlock the whole database. The databases are
encrypted using the best and most secure encryption algorithms
currently known (AES and Twofish).

%description -l pl.UTF-8
KeePassX to darmowy i mający otwarte źródła zarządca do przechowywania
haseł, który pozwala na zarządzanie hasłami w bardzo bezpieczny
sposób. Pozwala umieścić wszystkie swoje hasła w jednej bazie, która
jest zabezpieczona poprzez jedno bardzo trudne hasło albo dysk z
kluczem. Wystarczy więc zapamiętać jedno trudne hasło lub umieścić
dysk z kluczem aby odblokować całą bazę z kluczami. Baza jest
zaszyfrowana najlepszymi i najbardziej bezpiecznymi algorytmami
szyfrowania jakie są do tej pory znane (AES i TwoFish).

%prep
%setup -q -n keepassx-%{version}
%patch1 -p0
%patch2 -p1

%build
qmake-qt4 \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install

rm -r $RPM_BUILD_ROOT%{_datadir}/mimelnk

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/mime/packages/keepassx.xml
%{_desktopdir}/keepassx.desktop
%{_pixmapsdir}/keepassx.xpm
%{_datadir}/keepassx
