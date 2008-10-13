%define src_version 20081010
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
Source1:	fonts-ttf-japanese_fonts.alias
Source2:	fonts-ttf-japanese_fonts.dir
Source3:	cidinst.japanese
Source4:	cidunin.japanese

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	freetype-tools
Obsoletes:	xtt-fonts
Provides:	xtt-fonts
Requires(post): fontconfig >= 2.4.1
Requires(postun): fontconfig >= 2.4.1

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
install -m 644 %{SOURCE1} %buildroot/%{_datadir}/fonts/TTF/japanese/fonts.alias
# Macromedia Flash looks in fonts.dir file for old Japanese fonts
# (= Kochi Gothic, Kochi Mincho), regardless of the encoding, in order
# to find the TTF file name. So we provide a special fonts.dir file,
# with two extra lines to make Macromedia Flash happy.
# maybe some day it will be fixed and this won't be needed anymore.
#
install -m 644 %{SOURCE2} %buildroot/%{_datadir}/fonts/TTF/japanese/fonts.dir
ln -sf %{_datadir}/fonts/TTF/japanese/fonts.alias %buildroot/%{_datadir}/fonts/TTF/japanese/fonts.scale

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/fonts/TTF/japanese \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-japanese:pri=50

%post
[ -x %{_bindir}/fc-cache ] && %{_bindir}/fc-cache 


%postun
if [ "$1" = "0" ]; then
   [ -x %{_bindir}/fc-cache ] && %{_bindir}/fc-cache 
fi

%clean
rm -fr %buildroot

%files
%defattr(-,root,root,0755)
%doc ChangeLog README
%doc docs-*/ fontforge-scripts-*/

%dir %_datadir/fonts/TTF/japanese/
%_datadir/fonts/TTF/japanese/*.ttf
%config(noreplace) %_datadir/fonts/TTF/japanese/fonts.alias
%_datadir/fonts/TTF/japanese/fonts.dir
%_datadir/fonts/TTF/japanese/fonts.scale
%_sysconfdir/X11/fontpath.d/ttf-japanese:pri=50
