%define src_name umeplus-fonts
%define src_version 20120403

Summary:	Japanese TrueType fonts
Name:		fonts-ttf-japanese
Version:	0.%{src_version}
Release:	%mkrel 1
License:	Distributable
URL:		http://www.geocities.jp/ep3797/modified_fonts_01.html
Group:		System/Fonts/True type

## Original fonts is here
Source0:	http://downloads.sourceforge.net/mdk-ut/umeplus-fonts-%{src_version}.tar.lzma
Source3:	cidinst.japanese
Source4:	cidunin.japanese

BuildRequires:	freetype-tools
BuildRequires:	fontconfig
Obsoletes:	xtt-fonts
Provides:	xtt-fonts
BuildArch:	noarch

%description
This Package provides Free Japanese TrueType fonts (umeplus-gothic,
umeplus-p-gothic)

%prep
%setup -q -n %{src_name}-%{src_version}

%install
rm -fr %{buildroot}
mkdir -p %{buildroot}%{_datadir}/fonts/TTF/japanese
install -m 644 *.ttf %{buildroot}%{_datadir}/fonts/TTF/japanese

mkdir -p %{buildroot}%{_sysconfdir}/X11/fontpath.d/
ln -s ../../..%{_datadir}/fonts/TTF/japanese \
    %{buildroot}%{_sysconfdir}/X11/fontpath.d/ttf-japanese:pri=50

%clean
rm -fr %{buildroot}

%files
%defattr(-,root,root,0755)
%doc ChangeLog README docs-*/
%dir %{_datadir}/fonts/TTF/japanese/
%{_datadir}/fonts/TTF/japanese/*.ttf
%{_sysconfdir}/X11/fontpath.d/ttf-japanese:pri=50
