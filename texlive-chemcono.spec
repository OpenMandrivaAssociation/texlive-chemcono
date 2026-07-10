%global tl_name chemcono
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3
Release:	%{tl_revision}.1
Summary:	Support for compound numbers in chemistry documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/chemcono
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chemcono.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chemcono.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A LaTeX package for using compound numbers in chemistry documents. It
works like \cite and the \thebibliography, using \fcite and
\theffbibliography instead. It allows compound names in documents to be
numbered and does not affect the normal citation routines.

