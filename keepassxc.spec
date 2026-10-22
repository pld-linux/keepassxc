%define		qtver	6.2.4

Summary:	KeePassXC - Cross Platform Password Manager
Summary(pl.UTF-8):	KeePassXC - Wieloplatformowy zarządca haseł
Name:		keepassxc
Version:	2.8.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	https://github.com/keepassxreboot/keepassxc/releases/download/%{version}/%{name}-%{version}-src.tar.xz
# Source0-md5:	81fc392364506b87be37e771f1341f6c
URL:		https://keepassxc.org/
BuildRequires:	Qt6Concurrent-devel >= %{qtver}
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6DBus-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel >= %{qtver}
BuildRequires:	Qt6Network-devel >= %{qtver}
BuildRequires:	Qt6Svg-devel >= %{qtver}
BuildRequires:	Qt6Test-devel >= %{qtver}
BuildRequires:	Qt6Widgets-devel >= %{qtver}
BuildRequires:	botan2-devel >= 2.19.1
BuildRequires:	cmake >= 3.16.0
BuildRequires:	libstdc++-devel >= 6:8
BuildRequires:	libusb-devel
BuildRequires:	minizip-devel
BuildRequires:	pcsc-lite-devel
BuildRequires:	pkgconfig
BuildRequires:	qrencode-devel
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	qt6-linguist >= %{qtver}
BuildRequires:	readline-devel
BuildRequires:	rpmbuild(find_lang) >= 1.37
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	ruby-asciidoctor
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xorg-lib-libxkbcommon-devel
BuildRequires:	xz
BuildRequires:	ykpers-devel
BuildRequires:	zlib-devel >= 1.2.0
BuildRequires:	zxcvbn-c-devel
Requires:	Qt6Concurrent >= %{qtver}
%requires_ge_to	Qt6Core Qt6Core-devel
Requires:	Qt6DBus >= %{qtver}
Requires:	Qt6Gui >= %{qtver}
Requires:	Qt6Network >= %{qtver}
Requires:	Qt6Svg >= %{qtver}
Requires:	Qt6Widgets >= %{qtver}
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
%cmake -B build \
	-DKEEPASSXC_BUILD_TYPE=Release \
	-DKPXC_FEATURE_BROWSER=ON \
	-DKPXC_FEATURE_SSHAGENT=ON \
	-DKPXC_FEATURE_UPDATES=OFF
%{__make} -C build

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
%{_iconsdir}/hicolor/*x*/apps/keepassxc*.png
%{_iconsdir}/hicolor/scalable/apps/keepassxc*.svg
%{_iconsdir}/hicolor/scalable/mimetypes/application-x-keepassxc.svg
%{_mandir}/man1/keepassxc.1*
%{_mandir}/man1/keepassxc-cli.1*
%{_datadir}/polkit-1/actions/org.keepassxc.KeePassXC.policy
