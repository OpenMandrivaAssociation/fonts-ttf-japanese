%define src_version 20100418
%define version     0.%{src_version}
%define release     %mkrel 1
%define src_name    umeplus-fonts

Summary:	Japanese TrueType fonts
Name:		fonts-ttf-japanese
Version:	%{version}
Release:	%{release}
License:	Distributable
URL:		http://www.geocities.jp/ep3797/modified_fonts_01.html
Group:		System/Fonts/True type

## Original fonts is here
Source0:	http://www.geocities.jp/ep3797/snapshot/modified_fonts/%{src_name}-%{src_version}.tar.bz2
Source3:	cidinst.japanese
Source4:	cidunin.japanese

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	freetype-tools
Obsoletes:	xtt-fonts
Provides:	xtt-fonts

%description
This Package provides Free Japanese TrueType fonts (umeplus-gothic, 
umeplus-p-gothic)

%prep
%setup -q -n %{src_name}-%{src_version}

%build

%install
rm -fr %buildroot
mkdir -p %buildroot/%{_datadir}/fonts/TTF/japanese
install -m 644 *.ttf %buildroot/%{_datadir}/fonts/TTF/japanese

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/fonts/TTF/japanese \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-japanese:pri=50

%clean
rm -fr %buildroot

%files
%defattr(-,root,root,0755)
%doc ChangeLog README
%doc docs-*/

%dir %_datadir/fonts/TTF/japanese/
%_datadir/fonts/TTF/japanese/*.ttf
%_sysconfdir/X11/fontpath.d/ttf-japanese:pri=50
