# revision 23089
# category TLCore
# catalog-ctan /support/chktex
# catalog-date 2011-06-08 17:43:41 +0200
# catalog-license gpl
# catalog-version 1.6.4
Name:		texlive-chktex
Version:	1.6.4
Release:	2
Summary:	Check for errors in LaTeX documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/chktex
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chktex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chktex.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chktex.x86_64-linux.tar.xz
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
%{_texmfdir}/chktex/chktexrc
%{_texmfdir}/scripts/chktex/deweb.pl
%doc %{_texmfdir}/doc/chktex/ChkTeX.pdf
%doc %{_mandir}/man1/chktex.1*
%doc %{_texmfdir}/doc/man/man1/chktex.man1.pdf
%doc %{_mandir}/man1/chkweb.1*
%doc %{_texmfdir}/doc/man/man1/chkweb.man1.pdf
%doc %{_mandir}/man1/deweb.1*
%doc %{_texmfdir}/doc/man/man1/deweb.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_bindir}
# shell script
cp -fa bin/x86_64-linux/chkweb %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdir}/scripts/a2ping/deweb.pl deweb
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
