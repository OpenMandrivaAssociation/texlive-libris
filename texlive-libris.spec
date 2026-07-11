%global tl_name libris
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Libris ADF fonts, with LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/libris
License:	lppl1.3c gpl2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/libris.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/libris.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/libris.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
LibrisADF is a sans-serif family designed to mimic Lydian. The bundle
includes: fonts, in Adobe Type 1, TrueType and OpenType formats, and
LaTeX support macros, for use with the Type 1 versions of the fonts. The
LaTeX macros depend on the nfssext-cfr bundle. GPL licensing applies the
fonts themselves; the support macros are distributed under LPPL
licensing.

