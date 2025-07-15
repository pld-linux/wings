#
Summary:	3D subdivision modeller
Name:		wings
Version:	0.99.04a
Release:	1
License:	BSD
Group:		Applications
Source0:	http://downloads.sourceforge.net/wings/wings-%{version}.tar.bz2
# Source0-md5:	148f28cd97c8d3d2426b34b53c385cb5
Patch0:		%{name}-pic.patch
URL:		http://www.wings3d.com/
BuildRequires:	OpenGL-devel
BuildRequires:	erlang
BuildRequires:	esdl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wings 3D is a subdivision modeler inspired by Nendo and Mirai from Izware.

It is possible to assign materials, vertex color, UV coordinates and
textures, but there will be improvements in those features before Wings goes
1.0.

There is no support in Wings for doing animations. 

%prep
%setup -q
%patch -P0 -p1

%build
%{__make} -j1 unix \
	ESDL_PATH=%{_libdir}/erlang/lib/esdl

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
