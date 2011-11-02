Name:		texlive-libris
Version:	1.007
Release:	1
Summary:	Libris ADF fonts, with LaTeX support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/libris
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/libris.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/libris.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/libris.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
LibrisADF is a sans-serif family designed to mimic Lydian. The
bundle includes: - fonts, in Adobe Type 1, TrueType and
OpenType formats, and - LaTeX support macros, for use with the
Type 1 versions of the fonts. The LaTeX macros depend on the
nfssext-cfr bundle. GPL licensing applies the the fonts
themselves; the support macros are distributed under LPPL
licensing.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/arkandis/libris/ylyb8a.afm
%{_texmfdistdir}/fonts/afm/arkandis/libris/ylybi8a.afm
%{_texmfdistdir}/fonts/afm/arkandis/libris/ylyr8a.afm
%{_texmfdistdir}/fonts/afm/arkandis/libris/ylyri8a.afm
%{_texmfdistdir}/fonts/enc/dvips/libris/libris-supp.enc
%{_texmfdistdir}/fonts/enc/dvips/libris/t1-cfr-yly.enc
%{_texmfdistdir}/fonts/enc/dvips/libris/ts1-euro-yly.enc
%{_texmfdistdir}/fonts/map/dvips/libris/yly.map
%{_texmfdistdir}/fonts/tfm/arkandis/libris/ylyb-t1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/libris/ylyb-ts1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/libris/ylyb8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/libris/ylyb8s.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/libris/ylyb8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/libris/ylybi-t1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/libris/ylybi-ts1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/libris/ylybi8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/libris/ylybi8s.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/libris/ylybi8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/libris/ylybiw8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/libris/ylybw8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/libris/ylyr-t1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/libris/ylyr-ts1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/libris/ylyr8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/libris/ylyr8s.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/libris/ylyr8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/libris/ylyri-t1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/libris/ylyri-ts1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/libris/ylyri8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/libris/ylyri8s.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/libris/ylyri8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/libris/ylyriw8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/libris/ylyrw8t.tfm
%{_texmfdistdir}/fonts/type1/arkandis/libris/ylyb8a.pfb
%{_texmfdistdir}/fonts/type1/arkandis/libris/ylyb8a.pfm
%{_texmfdistdir}/fonts/type1/arkandis/libris/ylybi8a.pfb
%{_texmfdistdir}/fonts/type1/arkandis/libris/ylybi8a.pfm
%{_texmfdistdir}/fonts/type1/arkandis/libris/ylyr8a.pfb
%{_texmfdistdir}/fonts/type1/arkandis/libris/ylyr8a.pfm
%{_texmfdistdir}/fonts/type1/arkandis/libris/ylyri8a.pfb
%{_texmfdistdir}/fonts/type1/arkandis/libris/ylyri8a.pfm
%{_texmfdistdir}/fonts/vf/arkandis/libris/ylyb8c.vf
%{_texmfdistdir}/fonts/vf/arkandis/libris/ylyb8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/libris/ylybi8c.vf
%{_texmfdistdir}/fonts/vf/arkandis/libris/ylybi8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/libris/ylybiw8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/libris/ylybw8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/libris/ylyr8c.vf
%{_texmfdistdir}/fonts/vf/arkandis/libris/ylyr8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/libris/ylyri8c.vf
%{_texmfdistdir}/fonts/vf/arkandis/libris/ylyri8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/libris/ylyriw8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/libris/ylyrw8t.vf
%{_texmfdistdir}/tex/latex/libris/libris.sty
%{_texmfdistdir}/tex/latex/libris/t1yly.fd
%{_texmfdistdir}/tex/latex/libris/t1ylyw.fd
%{_texmfdistdir}/tex/latex/libris/ts1yly.fd
%{_texmfdistdir}/tex/latex/libris/ts1ylyw.fd
%doc %{_texmfdistdir}/doc/fonts/libris/COPYING
%doc %{_texmfdistdir}/doc/fonts/libris/NOTICE.txt
%doc %{_texmfdistdir}/doc/fonts/libris/README
%doc %{_texmfdistdir}/doc/fonts/libris/librisadf.pdf
%doc %{_texmfdistdir}/doc/fonts/libris/librisadf.tex
%doc %{_texmfdistdir}/doc/fonts/libris/manifest.txt
#- source
%doc %{_texmfdistdir}/source/fonts/libris/libris-supp.etx
%doc %{_texmfdistdir}/source/fonts/libris/reglyph-yly.tex
%doc %{_texmfdistdir}/source/fonts/libris/resetalt.mtx
%doc %{_texmfdistdir}/source/fonts/libris/t1-cfr.etx
%doc %{_texmfdistdir}/source/fonts/libris/t1-libris.etx
%doc %{_texmfdistdir}/source/fonts/libris/t1-librisswash.etx
%doc %{_texmfdistdir}/source/fonts/libris/ts1-euro.etx
%doc %{_texmfdistdir}/source/fonts/libris/yly-drv.tex
%doc %{_texmfdistdir}/source/fonts/libris/yly-map.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
