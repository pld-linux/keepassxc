%define		qtver	5.12.0

Summary:	KeePassXC - Cross Platform Password Manager
Summary(pl.UTF-8):	KeePassXC - Wieloplatformowy zarządca haseł
Name:		keepassxc
Version:	2.7.8
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	https://github.com/keepassxreboot/keepassxc/releases/download/%{version}/%{name}-%{version}-src.tar.xz
# Source0-md5:	5bf705a6277e17b162a4ad2a8fd60dbf
URL:		https://keepassxc.org/
BuildRequires:	Qt5Concurrent-devel >= %{qtver}
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Network-devel >= %{qtver}
BuildRequires:	Qt5Svg-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	Qt5X11Extras-devel >= %{qtver}
BuildRequires:	botan2-devel >= 2.11.0
BuildRequires:	cmake >= 3.10.0
BuildRequires:	libargon2-devel
BuildRequires:	libusb-devel
BuildRequires:	minizip-devel
BuildRequires:	pcsc-lite-devel
BuildRequires:	pkgconfig
BuildRequires:	qrencode-devel
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	qt5-linguist >= %{qtver}
BuildRequires:	qt5-qmake >= %{qtver}
BuildRequires:	readline-devel
BuildRequires:	rpmbuild(find_lang) >= 1.37
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	ruby-asciidoctor
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xz
BuildRequires:	ykpers-devel
BuildRequires:	zlib-devel >= 1.2.0
Requires:	Qt5Concurrent >= %{qtver}
%requires_ge_to	Qt5Core Qt5Core-devel
Requires:	Qt5DBus >= %{qtver}
Requires:	Qt5Gui >= %{qtver}
Requires:	Qt5Network >= %{qtver}
Requires:	Qt5Svg >= %{qtver}
Requires:	Qt5Widgets >= %{qtver}
Requires:	Qt5X11Extras >= %{qtver}
Requires:	desktop-file-utils
Requires:	hicolor-icon-theme
Requires:	shared-mime-info
Requires:	zlib >= 1.2.0
Obsoletes:	KeePassX
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KeePassXC is a free/open-source password manager or safe which helps
you to manage your passwords in a secure way. You can put all your
passwords in one database, which is locked with one master key or a
key-disk. So you only have to remember one single master password or
insert the key-disk to unlock the whole database. The databases are
encrypted using the best and most secure encryption algorithms
currently known (AES and Twofish).

%description -l pl.UTF-8
KeePassXC to darmowy i mający otwarte źródła zarządca do
przechowywania haseł, który pozwala na zarządzanie hasłami w bardzo
bezpieczny sposób. Pozwala umieścić wszystkie swoje hasła w jednej
bazie, która jest zabezpieczona poprzez jedno bardzo trudne hasło albo
dysk z kluczem. Wystarczy więc zapamiętać jedno trudne hasło lub
umieścić dysk z kluczem aby odblokować całą bazę z kluczami. Baza jest
zaszyfrowana najlepszymi i najbardziej bezpiecznymi algorytmami
szyfrowania jakie są do tej pory znane (AES i TwoFish).

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	-DKEEPASSXC_BUILD_TYPE=Release \
	-DWITH_XC_BROWSER=ON \
	-DWITH_XC_BROWSER_PASSKEYS=ON \
	-DWITH_XC_KEESHARE=ON \
	-DWITH_XC_SSHAGENT=ON \
	-DWITH_XC_YUBIKEY=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-qm

%{__sed} -i -e '
	s/%lang(en_plurals)/%%lang(en)/
	s/%lang(nl_NL)/%%lang(nl)/
' %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%update_desktop_database
%update_mime_database

%postun
%update_icon_cache hicolor
%update_desktop_database_postun
%update_mime_database

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/keepassxc
%attr(755,root,root) %{_bindir}/keepassxc-cli
%attr(755,root,root) %{_bindir}/keepassxc-proxy
%{_datadir}/metainfo/org.keepassxc.KeePassXC.appdata.xml
%{_datadir}/mime/packages/keepassxc.xml
%{_desktopdir}/org.keepassxc.KeePassXC.desktop
%dir %{_datadir}/keepassxc
%{_datadir}/keepassxc/docs
%{_datadir}/keepassxc/icons
%dir %{_datadir}/keepassxc/translations
%{_datadir}/keepassxc/wordlists
%dir %{_libdir}/keepassxc
%attr(755,root,root) %{_libdir}/keepassxc/libkeepassxc-autotype-xcb.so
%{_iconsdir}/hicolor/*x*/apps/keepassxc*.png
%{_iconsdir}/hicolor/scalable/apps/keepassxc*.svg
%{_iconsdir}/hicolor/scalable/mimetypes/application-x-keepassxc.svg
%{_mandir}/man1/keepassxc.1*
%{_mandir}/man1/keepassxc-cli.1*
