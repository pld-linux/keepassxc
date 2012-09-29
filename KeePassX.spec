# TODO
# - forcing our cflags breaks build
Summary:	KeePassX - Cross Platform Password Manager
Summary(pl.UTF-8):	KeePassX - Wieloplatformowy zarządca haseł
Name:		KeePassX
Version:	0.4.3
Release:	3
License:	GPL v2+
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/keepassx/keepassx-%{version}.tar.gz
# Source0-md5:	1df67bb22b2e08df49f09e61d156f508
URL:		http://keepassx.sourceforge.net/
Patch1:		keepassx-0.3.3-gcc43.patch
Patch2:		keepassx-0.4.3-gcc47.patch
BuildRequires:	ImageMagick
BuildRequires:	Qt3Support-devel >= 4.0
BuildRequires:	QtGui-devel >= 4.0
BuildRequires:	QtXml-devel >= 4.0
BuildRequires:	qt4-build >= 4.3.3-3
BuildRequires:	qt4-qmake >= 4.3.3-3
BuildRequires:	rpmbuild(macros) >= 1.230
BuildRequires:	xorg-lib-libXtst-devel
Requires:	desktop-file-utils
Requires:	hicolor-icon-theme
Requires:	shared-mime-info
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
	PREFIX=%{_prefix}

%{__make} \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	_CFLAGS="%{rpmcflags}" \
	_CXXFLAGS="%{rpmcxxflags}" \
	%{nil}

# use png icon
convert share/pixmaps/keepassx.xpm share/pixmaps/keepassx.png

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_pixmapsdir}/keepassx.xpm
cp -p share/pixmaps/keepassx.png $RPM_BUILD_ROOT%{_pixmapsdir}/keepassx.png

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/mimelnk

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

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/keepassx
%{_datadir}/mime/packages/keepassx.xml
%{_desktopdir}/keepassx.desktop
%{_pixmapsdir}/keepassx.png
%dir %{_datadir}/keepassx
%{_datadir}/keepassx/icons
%{_datadir}/keepassx/license.html
%dir %{_datadir}/keepassx/i18n
%lang(de) %{_datadir}/keepassx/i18n/keepassx-de_DE.qm
%lang(es) %{_datadir}/keepassx/i18n/keepassx-es_ES.qm
%lang(fi) %{_datadir}/keepassx/i18n/keepassx-fi_FI.qm
%lang(fi) %{_datadir}/keepassx/i18n/qt_fi.qm
%lang(fr) %{_datadir}/keepassx/i18n/keepassx-fr_FR.qm
%lang(gl) %{_datadir}/keepassx/i18n/keepassx-gl_ES.qm
%lang(gl) %{_datadir}/keepassx/i18n/qt_gl_ES.qm
%lang(hu) %{_datadir}/keepassx/i18n/keepassx-hu_HU.qm
%lang(hu) %{_datadir}/keepassx/i18n/qt_hu.qm
%lang(it) %{_datadir}/keepassx/i18n/keepassx-it_IT.qm
%lang(it) %{_datadir}/keepassx/i18n/qt_it.qm
%lang(ja) %{_datadir}/keepassx/i18n/keepassx-ja_JP.qm
%lang(nb) %{_datadir}/keepassx/i18n/keepassx-nb_NO.qm
%lang(nl) %{_datadir}/keepassx/i18n/keepassx-nl_NL.qm
%lang(nl) %{_datadir}/keepassx/i18n/qt_nl.qm
%lang(pl) %{_datadir}/keepassx/i18n/keepassx-pl_PL.qm
%lang(pt) %{_datadir}/keepassx/i18n/keepassx-pt_PT.qm
%lang(ru) %{_datadir}/keepassx/i18n/keepassx-ru_RU.qm
%lang(sk) %{_datadir}/keepassx/i18n/keepassx-sk_SK.qm
%lang(sr) %{_datadir}/keepassx/i18n/keepassx-sr_RS.qm
%lang(sr) %{_datadir}/keepassx/i18n/qt_sr.qm
%lang(tr) %{_datadir}/keepassx/i18n/keepassx-tr_TR.qm
%lang(tr) %{_datadir}/keepassx/i18n/qt_tr.qm
%lang(uk) %{_datadir}/keepassx/i18n/keepassx-uk_UA.qm
%lang(zh_CN) %{_datadir}/keepassx/i18n/keepassx-zh_CN.qm
