%define src_name umeplus-fonts
%define src_version 20120403

Summary:	Japanese TrueType fonts
Name:		fonts-ttf-japanese
Version:	0.%{src_version}
Release:	8
License:	Distributable
Group:		System/Fonts/True type
Url:		http://www.geocities.jp/ep3797/modified_fonts_01.html
## Original fonts is here
Source0:	http://downloads.sourceforge.net/mdk-ut/umeplus-fonts-%{src_version}.tar.lzma
Source3:	cidinst.japanese
Source4:	cidunin.japanese

BuildRequires:	freetype-tools
BuildRequires:	fontconfig
BuildArch:	noarch

%description
This Package provides Free Japanese TrueType fonts (umeplus-gothic,
umeplus-p-gothic)

%prep
%setup -qn %{src_name}-%{src_version}

%install
mkdir -p %{buildroot}%{_datadir}/fonts/TTF/japanese
install -m 644 *.ttf %{buildroot}%{_datadir}/fonts/TTF/japanese

mkdir -p %{buildroot}%{_sysconfdir}/X11/fontpath.d/
ln -s ../../..%{_datadir}/fonts/TTF/japanese \
	%{buildroot}%{_sysconfdir}/X11/fontpath.d/ttf-japanese:pri=50

%files
%doc ChangeLog README docs-*/
%dir %{_datadir}/fonts/TTF/japanese/
%{_datadir}/fonts/TTF/japanese/*.ttf
%{_sysconfdir}/X11/fontpath.d/ttf-japanese:pri=50

