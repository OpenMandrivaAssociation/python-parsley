%define	oname	Parsley

Name:		python-parsley
Version:	1.2
Release:	1
Summary:	Parsing and pattern matching made easy
Source0:	http://pypi.python.org/packages/source/P/%{oname}/%{oname}-%{version}.tar.gz
License:	MIT
Group:		Development/Python
Url:		http://launchpad.net/parsley
BuildRequires:	pythonegg(setuptools)

BuildArch:	noarch

%description
Parsley is a parsing library for people who find parsers scary or
annoying. I wrote it because I wanted to parse a programming language,
and tools like PLY or ANTLR or Bison were very hard to understand and
integrate into my Python code. Most parser generators are based on LL
or LR parsing algorithms that compile to big state machine
tables. It was like I had to wake up a different section of my brain
to understand or work on grammar rules.

Parsley, like pyparsing and ZestyParser, uses the PEG algorithm, so
each expression in the grammar rules works like a Python
expression. In particular, alternatives are evaluated in order, unlike
table-driven parsers such as yacc, bison or PLY.

Parsley is an implementation of OMeta, an object-oriented
pattern-matching language developed by Alessandro Warth at
http://tinlizzie.org/ometa/ . For further reading, see Warth's PhD
thesis, which provides a detailed description of OMeta:
http://www.vpri.org/pdf/tr2008003_experimenting.pdf.


%prep
%setup -q -n %{oname}-%{version}

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

%files
%doc README
%{py_puresitedir}/ometa/*.py*
%{py_puresitedir}/ometa/_generated/*.py*
%{py_puresitedir}/ometa/test/*.py*
%{py_puresitedir}/parsley.py*
%{py_puresitedir}/terml/*.py*
%{py_puresitedir}/terml/_generated/*.py*
%{py_puresitedir}/terml/test/*.py*
%{py_puresitedir}/Parsley*.egg-info
