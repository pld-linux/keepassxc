
# NFY
# - qt-designer 4.0 required
# - Qt Modules: QtCore, QtGui, QtXml

######		Unknown group!
Summary:	KeePassX - Cross Platform Password Manager
Summary(pl):	KeePassX - Wieloplatformowy Manager hase³.
Name:		KeePassX
Version:	0.2.2
Release:	0.1
License:	GPL
Group:		Security
Source0:	http://dl.sourceforge.net/keepassx/%{name}-%{version}.tar.gz
# Source0-md5:
URL:		http://keepassx.berlios.de
BuildRequires:	qt
BuildRequires:	qt-designer
BuildRequires:	qt-devel
BuildRequires:	rpmbuild(macros) >= 1.230
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KeePassX is a free/open-source password manager or safe which helps
you to manage your passwords in a secure way. You can put all your
passwords in one database, which is locked with one master key or a
key-disk. So you only have to remember one single master password or
insert the key-disk to unlock the whole database. The databases are
encrypted using the best and most secure encryption algorithms
currently known (AES and Twofish).

%description -l pl
KeePassX to darmowy/open-scourceowy menad¿er do przetrzymywania hase³,
który pozwala na zarz±dzanie has³ami w bardzo bezpieczny sposób.
Mo¿esz umie¶ciæ wszystkie swoje has³a w jednej bazie, któa jest
zabezpieczona poprzez jedno bardzo trudne has³o albo dysk z kluczem.
Musisz wiêc zapamiêtaæ jedno trudne has³o lub umie¶ciæ dysk z kluczem
aby odblokowaæ ca³a baze z kluczami. Baza jest zaszyfrowana
najlepszymi i najbardziej bezpiecznymi algorytmami szyfrowania jakie
sa do tej pory zanane(AES i TwoFish.

%prep
%setup -q -n keepassx-%{version}

%build
qmake PREFIX=$RPM_BUILD_ROOT%{_prefix}/local
%{__make}


%INSTALL
rm -rf $RPM_BUILD_ROOT

%{__make} install

cd $RPM_BUILD_ROOT

find . -type d -fprint $RPM_BUILD_DIR/file.list.%{name}.dirs
find . -type f -fprint $RPM_BUILD_DIR/file.list.%{name}.files.tmp
sed '/\/man\//s/$/.gz/g' $RPM_BUILD_DIR/file.list.%{name}.files.tmp > $RPM_BUILD_DIR/file.list.%{name}.files
find . -type l -fprint $RPM_BUILD_DIR/file.list.%{name}.libs
sed '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' $RPM_BUILD_DIR/file.list.%{name}.dirs > $RPM_BUILD_DIR/file.list.%{name}
sed 's,^\.,\%attr(-\,root\,root) ,' $RPM_BUILD_DIR/file.list.%{name}.files >> $RPM_BUILD_DIR/file.list.%{name}
sed 's,^\.,\%attr(-\,root\,root) ,' $RPM_BUILD_DIR/file.list.%{name}.libs >> $RPM_BUILD_DIR/file.list.%{name}

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_DIR/file.list.%{name}
rm -rf $RPM_BUILD_DIR/file.list.%{name}.libs
rm -rf $RPM_BUILD_DIR/file.list.%{name}.files
rm -rf $RPM_BUILD_DIR/file.list.%{name}.files.tmp
rm -rf $RPM_BUILD_DIR/file.list.%{name}.dirs


%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
