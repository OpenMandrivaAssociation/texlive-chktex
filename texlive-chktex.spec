Name:		texlive-chktex
Version:	71205
Release:	1
Summary:	Check for errors in LaTeX documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/chktex
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chktex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chktex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-chktex.bin

%description
The program reports typographic and other errors in LaTeX
documents. Filters are also provided for checking the LaTeX
parts of CWEB documents.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_bindir}/chkweb
%{_bindir}/deweb
%{_texmfdistdir}/chktex/chktexrc
%{_texmfdistdir}/scripts/chktex/chkweb.sh
%{_texmfdistdir}/scripts/chktex/deweb.pl
%doc %{_texmfdistdir}/doc/chktex/ChkTeX.pdf
%doc %{_mandir}/man1/chktex.1*
%doc %{_texmfdistdir}/doc/man/man1/chktex.man1.pdf
%doc %{_mandir}/man1/chkweb.1*
%doc %{_texmfdistdir}/doc/man/man1/chkweb.man1.pdf
%doc %{_mandir}/man1/deweb.1*
%doc %{_texmfdistdir}/doc/man/man1/deweb.man1.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/chktex/chkweb.sh chkweb
ln -sf %{_texmfdistdir}/scripts/chktex/deweb.pl deweb
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
