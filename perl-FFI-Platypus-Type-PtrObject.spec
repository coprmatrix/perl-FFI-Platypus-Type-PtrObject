#
# spec file for package perl-FFI-Platypus-Type-PtrObject (Version 0.03)
#
# Copyright (c) 124 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

%define cpan_name FFI-Platypus-Type-PtrObject
Name:           perl-FFI-Platypus-Type-PtrObject
Version:        0.03
Release:        0
License:        Artistic-1.0 or GPL-1.0-or-later
Summary:        Platypus custom type for an object wrapped around an opaque pointer
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/%{cpan_name}-%{version}.tar.gz
BuildRequires:  perl-generators
BuildRequires:  perl-macros-suse
BuildRequires:  perl(FFI::Build::MM) >= 0.83
BuildRequires:  perl(FFI::Platypus) >= 1.11
BuildRequires:  perl(FFI::Platypus::Memory)
BuildRequires:  perl(Ref::Util)
BuildRequires:  perl(Test2::Tools::FFI)
BuildRequires:  perl(Test2::V0) >= 0.000060
Requires:       perl(FFI::Platypus) >= 1.11
Requires:       perl(Ref::Util)
Provides:       perl(FFI::Platypus::Type::PtrObject)

%description
This is a helper type for FFI::Platypus that handles type checking for the
common pattern where a Perl class is a simple wrapper around an opaque
pointer. The class should be implemented as a hash reference, and the
pointer itself is expected to be stored on the 'ptr' key. If the caller of
the interface (Perl) is responsible for cleaning up the memory, then it
normally should be done in the 'DESTROY' method (as above).

If you do not pass in the correct type, it will be detected before the C
code is called and an exception will be thrown. (otherwise you would
probably get a segment violation SEGV).

%prep
%autosetup  -n %{cpan_name}-%{version}

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README
%license LICENSE

%changelog
