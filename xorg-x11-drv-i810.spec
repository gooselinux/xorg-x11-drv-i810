%define i810 xf86-video-i810
%define intel xf86-video-intel
%define iversion 2.2.1
%define moduledir %(pkg-config xorg-server --variable=moduledir )
%define driverdir	%{moduledir}/drivers

%define gitdate 20080119
%define _source_filedigest_algorithm 1
%define _default_patch_fuzz 2

Summary:   Xorg X11 i810 video driver(s)
Name:      xorg-x11-drv-i810
Version:   1.6.5
Release:   9.36%{?dist}
URL:       http://www.x.org
License:   MIT/X11
Group:     User Interface/X Hardware Support
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:   http://www.x.org/pub/individual/driver/%{i810}-%{version}.tar.bz2
Source1:   http://www.x.org/pub/individual/driver/%{intel}-%{iversion}.tar.bz2
Source2:   i810.xinf

# stock driver patches
Patch100: i810-1.6.5-to-git-20060911.patch
Patch101: i810-match-server-sync-ranges.patch
Patch102: blank-on-init.patch
Patch103: i810-1.6.5-965-update.patch
Patch104: i810-1.6.5-bearlake.patch
Patch105: i810-1.6.5-bridge-id-fix.patch
Patch106: intel-1.6.5-warn-9xx.patch

# RHEL5 customization
Patch1000: i965-xv-hang-fix.patch

# intel driver
Patch2000: intel-version.patch
Patch2001: intel-no-exa.patch
Patch2002: intel-redetect-on-acpi.patch
Patch2003: intel-lvds-detection.patch
Patch2004: intel-disable-rotation.patch
Patch2006: intel-1.5-misc.patch
Patch2007: intel-dri.patch
Patch2008: intel-2.2.1-g40-backport.patch
Patch2009: intel-2.2.1-g40-no3d.patch
Patch2010: intel-2.2.1-disable-planes.patch
Patch2011: intel-2.2.1-add-845G+855GM-quirk-pipea-force.patch
Patch2012: intel-2.2.1-vga-dpll-init.patch
Patch2013: intel-2.2.1-hdmi.patch
Patch2014: intel-2.2.1-965-overlay.patch
Patch2015: intel-2.2.1-hdmi-2.patch
Patch2016: intel-2.2.1-vt-switch-fixes.patch
Patch2017: intel-2.2.1-vga-disable.patch
Patch2018: intel-2.2.1-g40-setup-fixes.patch
Patch2019: intel-2.2.1-lvds-modes.patch
Patch2020: intel-2.2.1-warn-8xx.patch
Patch2021: intel-2.2.1-g4x-vga-plane-fix.patch

Patch2100: intel-2.2.1-ironlake-pci-ids.patch
Patch2101: intel-2.2.1-ironlake-registers.patch
Patch2102: intel-2.2.1-ironlake-disable-renderaccel.patch
Patch2103: intel-2.2.1-ironlake-mmio-size-fix.patch
Patch2104: intel-2.2.1-ironlake-modesetting.patch
Patch2105: intel-2.2.1-ironlake-no-xv.patch
Patch2106: intel-2.2.1-ironlake-int10-hack.patch
Patch2107: intel-2.2.1-ironlake-vbt-parse-fix.patch
Patch2108: intel-2.2.1-ironlake-fixes.patch

Patch2150: intel-2.2.1-b43.patch

ExclusiveArch: %{ix86} x86_64 ia64

BuildRequires: pkgconfig
BuildRequires: autoconf automake libtool
BuildRequires: xorg-x11-server-sdk >= 1.1.1-48.58.el5
BuildRequires: libXvMC-devel
BuildRequires: mesa-libGL-devel >= 6.5-9
BuildRequires: libdrm-devel >= 2.0-1

Requires:  xorg-x11-server-Xorg >= 1.1.1-48.58.el5

Conflicts:  kudzu < 1.2.42-1

%description 
X.Org X11 i810 video driver.

%package devel
Summary:   Xorg X11 i810 video driver XvMC development package
Group:     Development/System
Requires:  %{name} = %{version}-%{release}

%description devel
X.Org X11 i810 video driver XvMC development package.

%prep
# fc6 baseline patches
%setup -q -n %{i810}-%{version}
%patch100 -p2 -b .i810-git-20060911
%patch101 -p2 -b .server-ranges
#patch102 -p2 -b .blank-on-init
%patch103 -p1 -b .crestline
%patch104 -p1 -b .bearlake
%patch105 -p2 -b .bridge-id
%patch106 -p1 -b .warn-9xx
# rhel5 customization
%patch1000 -p2 -b .965-xv

cd ..
rm -rf %{intel}-%{iversion}
tar jxf %{SOURCE1}
cd %{intel}-%{iversion}

# any intel patchery goes here
%patch2000 -p1 -b .version
%patch2001 -p1 -b .no-exa
%patch2002 -p1 -b .redetect
%patch2003 -p1 -b .lvds
%patch2004 -p1 -b .rotate
%patch2007 -p1 -b .dri
%patch2008 -p1 -b .g40
%patch2009 -p1 -b .g40no3d
%patch2010 -p1 -b .disable-planes
%patch2011 -p1 -b .pipea
%patch2012 -p1 -b .vga-dpll
%patch2013 -p1 -b .hdmi
%patch2014 -p1 -b .965-overlay
%patch2015 -p1 -b .hdmi2
%patch2016 -p1 -b .vtswitch
%patch2017 -p1 -b .vga-disable
%patch2018 -p1 -b .g40-setup
%patch2019 -p1 -b .lvds-modes
%patch2020 -p1 -b .warn-8xx
%patch2021 -p1 -b .g4x-vga

%patch2006 -p1 -b .misc

%patch2100 -p1 -b .irl0
%patch2101 -p1 -b .irl1
%patch2102 -p1 -b .irl2
%patch2103 -p1 -b .irl3
%patch2104 -p1 -b .irl4
%patch2105 -p1 -b .irl-no-xv
%patch2106 -p1 -b .irl-int10
%patch2107 -p1 -b .irl-vbt
%patch2108 -p1 -b .irl-fixes
%patch2150 -p1 -b .b43

sed -i 's/^.*XORG_MACROS_VERSION.*//' configure.ac

%build
OPTS="--disable-static --libdir=%{_libdir} --mandir=%{_mandir} --enable-dri"

# i810
%configure ${OPTS}
make

# intel
cd ../%{intel}-%{iversion}
# export CFLAGS="$RPM_OPT_FLAGS -O0"
autoreconf -v --install
%configure ${OPTS}
make

%install
rm -rf $RPM_BUILD_ROOT

# intel
cd ../%{intel}-%{iversion}
make install DESTDIR=$RPM_BUILD_ROOT 
rm ${RPM_BUILD_ROOT}/usr/share/man/man4/i810.4*

# i810
cd -
make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/hwdata/videoaliases
install -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/hwdata/videoaliases/

# FIXME: Remove all libtool archives (*.la) from modules directory.  This
# should be fixed in upstream Makefile.am or whatever.
find $RPM_BUILD_ROOT -regex ".*\.la$" | xargs rm -f --

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%dir %{moduledir}
%dir %{driverdir}
%{driverdir}/i810_drv.so
%{driverdir}/intel_drv.so
%{driverdir}/ch7017.so
%{driverdir}/ch7xxx.so
%{driverdir}/ivch.so
%{driverdir}/sil164.so
%{driverdir}/tfp410.so
%{_datadir}/hwdata/videoaliases/i810.xinf
%dir %{_libdir}
%{_libdir}/libI810XvMC.so.1
%{_libdir}/libI810XvMC.so.1.0.0
#%dir %{_mandir}/man4x
%{_mandir}/man4/i*

%files devel
%defattr(-,root,root,-)
%dir %{_libdir}
%{_libdir}/libI810XvMC.so

%changelog
* Tue Mar 09 2010 Adam Jackson <ajax@redhat.com> 1.6.5-9.36
- Fix CFLAGS.

* Tue Mar 09 2010 Adam Jackson <ajax@redhat.com> 1.6.5-9.35
- intel-2.2.1-ironlake-fixes.patch: Fix Ironlake LVDS setup and FDI training,
  disable output scanning, and other small fixes. (#559116)

* Wed Mar 03 2010 Adam Jackson <ajax@redhat.com> 1.6.5-9.34
- intel-2.2.1-ironlake-vbt-parse-fix.patch: Fix VBT parse on Ironlake.
  (#559116)

* Mon Feb 22 2010 Adam Jackson <ajax@redhat.com> 1.6.5-9.33
- intel-2.2.1-g40-setup-fixes.patch: Drop DDC bus create/destroy. (#521350)
- intel-2.2.1-ironlake-modesetting.patch: Rediff to match.

* Tue Feb 16 2010 Adam Jackson <ajax@redhat.com> 1.6.5-9.32
- intel-2.2.1-ironlake-int10-hack.patch: Fix VT switch on Ironlake. (#560137)

* Tue Feb 16 2010 Adam Jackson <ajax@redhat.com> 1.6.5-9.31
- intel-2.2.1-ironlake-no-xv.patch: Disable Xv on ironlake. (#560132)

* Mon Feb 15 2010 Adam Jackson <ajax@redhat.com> 1.6.5-9.30
- intel-2.2.1-g40-no3d.patch: Also disable DRI on ironlake. (#560126)

* Mon Jan 11 2010 Adam Jackson <ajax@redhat.com> 1.6.5-9.29
- intel-2.2.1-b43.patch: Add B43 support. (#525276)

* Fri Dec 18 2009 Adam Jackson <ajax@redhat.com> 1.6.5-9.27
- intel-2.2.1-ironlake-*.patch: Add Ironlake support. (#517356)
- i810.xinf: Add Ironlake PCI IDs.

* Mon Nov 23 2009 Adam Jackson <ajax@redhat.com> 1.6.5-9.26
- intel-2.2.1-g4x-vga-plane-fix.patch: Yet more VGA plane setup fixes (#511896)

* Thu May 14 2009 Adam Jackson <ajax@redhat.com> 1.6.5-9.25
- intel-1.6.5-warn-9xx.patch, intel-2.2.1-warn-8xx.patch: Warn about
  unsupported configurations. (#479067)

* Wed May 13 2009 Adam Jackson <ajax@redhat.com> 1.6.5-9.24
- Rebuild for new X server RANDR source.
- intel-2.2.1-g40-setup-fixes.patch: Various VT switch fixes. (#470450)
- intel-2.2.1-lvds-modes.patch: Add default modes to LVDS outputs if there's
  no EDID or if it claims to not be continuous-freq.

* Tue May 12 2009 Kristian Høgsberg <krh@redhat.com> - 1.6.5-9.23
- Add intel-2.2.1-vga-disable.patch to fix vga disable sequence (#487657).

* Mon May 11 2009 Adam Jackson <ajax@redhat.com> 1.6.5-9.22
- intel-2.2.1-hdmi-2.patch: Backport more HDMI setup. (#476831)
- intel-2.2.1-vt-switch-fixes.patch: Backport more save/restore magic (#476831)

* Mon Dec 08 2008 Adam Jackson <ajax@redhat.com> 1.6.5-9.21
- intel-2.2.1-965-overlay.patch: Enable YUV overlay on 965. (#469633)

* Thu Nov 06 2008 Adam Jackson <ajax@redhat.com> 1.6.5-9.20
- i810.xinf: Update for G40. (#468661)

* Fri Oct 24 2008 Adam Jackson <ajax@redhat.com> 1.6.5-9.19
- intel-2.2.1-hdmi.patch: Backport SDVO HDMI support. (#465881)

* Wed Oct 15 2008 Adam Jackson <ajax@redhat.com> 1.6.5-9.18
- intel-2.2.1-vga-dpll-init.patch: Fix initialization on Montevina. (#457208)

* Wed Oct 15 2008 Adam Jackson <ajax@redhat.com> 1.6.5-9.17
- intel-2.2.1-disable-planes.patch: And...
- intel-2.2.1-add-845G+855GM-quirk-pipea-force.patch: Fix VT switching on
  845 in the intel driver.  (#454305)

* Wed Oct 15 2008 Dave Airlie <airlied@redhat.com> 1.6.5-9.16
- intel-2.2.1-g40-backport.patch: Add fix from upstream kernel
- intel-2.2.1-g40-no3d.patch: block 3D driver from loading.

* Fri Sep 19 2008 Adam Jackson <ajax@redhat.com> 1.6.5-9.15
- intel-2.2.1-g40-backport.patch: Add Intel 4 series support (#438400)

* Thu Sep 04 2008 Dave Airlie <airlied@redhat.com> 1.6.5-9.14
- rebase the i810 driver on top of the server randr source

* Thu Apr 24 2008 Dave Airlie <airlied@redhat.com> 1.6.5-9.13
- bump up another one to make it build (#437922)

* Thu Apr 24 2008 Dave Airlie <airlied@redhat.com> 1.6.5-9.12
- fix DRI on 64-bit (#437922)
- add cantiga pci id to the xinf file (#318761)

* Fri Apr 04 2008 Adam Jackson <ajax@redhat.com> 1.6.5-9.11
- Restore the default 1024x768 sync range for connected-but-EDID-less
  outputs. (ajax)

* Fri Apr 04 2008 Adam Jackson <ajax@redhat.com> 1.6.5-9.10
- Re-enable DRI in intel driver. (airlied)

* Wed Apr 02 2008 Adam Jackson <ajax@redhat.com> 1.6.5-9.9
- Reset output CRTC routing in xf86InitialConfigutation (kem)
- Set compat output to be the one with smallest maximum size and fewest
  modes (kem)
- Do not steal in-use CRTCs during load detection (airlied)
- Fall back to DDC when no CRTC is available for VGA detection (kem)
- Print output configuration after hotkey events (kem)
- Don't invalidate pSize in RRSetScreenConfig (kem)

* Wed Mar 26 2008 Adam Jackson <ajax@redhat.com> 1.6.5-9.8
- Update RANDR config on hotkey switch. (Kevin Martin)

* Tue Mar 25 2008 Adam Jackson <ajax@redhat.com> 1.6.5-9.7
- Fix a corner case that could throw BadImplementation. (Kevin Martin)

* Wed Mar 19 2008 Adam Jackson <ajax@redhat.com> 1.6.5-9.6.0.12
- Fix the initial mode selection heuristic so that the first pass is "largest
  preferred mode that works on all heads" rather than "preferred mode is
  identical on all heads." (Kevin Martin)

* Tue Mar 18 2008 Adam Jackson <ajax@redhat.com> 1.6.5-9.6.0.11
- Set compat output to be least capable output.
- Stretch synthesize output sync ranges to cover the probed modes.

* Mon Mar 17 2008 Adam Jackson <ajax@redhat.com> 1.6.5-9.6.0.10
- Additional compat output and VT switch fixes.

* Fri Mar 14 2008 Adam Jackson <ajax@redhat.com> 1.6.5-9.6.0.9
- Update to new server randr source.

* Fri Mar 07 2008 Adam Jackson <ajax@redhat.com> 1.6.5-9.6.0.8
- intel-disable-rotation.patch: Disable rotation and reflection report,
  since it doesn't work without updated server shadow bits.

* Fri Mar 07 2008 Adam Jackson <ajax@redhat.com> 1.6.5-9.6.0.7
- intel-fix-square-screen.patch: Fix square screen sizes.

* Thu Feb 28 2008 Adam Jackson <ajax@redhat.com> 1.6.5-9.6.0.6
- intel-initial-config-redo.patch: Temporary hack for fixing initial
  configuration heuristic.  This needs to go in the server.

* Mon Feb 25 2008 Adam Jackson <ajax@redhat.com> 1.6.5-9.6.0.5
- intel 2.2.1 (#292871)
- intel-lvds-detection.patch: When LVDS is powered off, consider it
  disconnected.

* Wed Feb 06 2008 Dave Airlie <airlied@redhat.com> 1.6.5-9.6.0.3
- intel-redetect-on-acpi.patch - add support for ACPI on thinkpad
- just redetect the outputs (#249290)

* Sat Jan 19 2008 Adam Jackson <ajax@redhat.com> 1.6.5-9.6.0.2
- Update intel driver to today's git snapshot.

* Wed Dec 12 2007 Adam Jackson <ajax@redhat.com> 1.6.5-9.6.0.1
- Update intel driver to 2.1.99. (#292871)
- i810.xinf: i915 and later use the intel driver.

* Wed Aug 15 2007 Adam Jackson <ajax@redhat.com> 1.6.5-9.6
- i810-1.6.5-bridge-id-fix.patch: Fix PCI bridge IDs for 9[46]5GME.

* Thu Jul 05 2007 Adam Jackson <ajax@redhat.com> 1.6.5-9.5
- i810-1.6.5-bearlake.patch: Additional fixes for Bearlake. (#246658, #227384)

* Mon Jun 25 2007 Adam Jackson <ajax@redhat.com> 1.6.5-9.4
- i810.xinf: Add PCI IDs for same. (#227392)

* Fri Jun 22 2007 Adam Jackson <ajax@redhat.com> 1.6.5-9.3
- i810-1.6.5-965-update.patch: Add support for 945GM, 965GM, and G30
  series chips. (#227384)

* Tue Nov 07 2006 Soren Sandmann <sandmann@redhat.com> 1.6.5-9.2.el5
- blank-on-init.patch: Blank framebuffer in both drivers before setting
  the mode.  (#210297).

* Tue Oct 31 2006 Adam Jackson <ajackson@redhat.com> 1.6.5-9.1.el5
- i965-xv-hang-fix.patch: Backport Xv hang fix for G965.  (#211605)

* Sun Oct 01 2006 Jesse Keating <jkeating@redhat.com> - 1.6.5-9
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Fri Sep 22 2006 Adam Jackson <ajackson@redhat.com> 1.6.5-8.fc6
- Change 'Requires: kudzu >= foo' to 'Conflicts: kudzu < foo' since we don't
  actually require kudzu to run.

* Fri Sep 15 2006 Adam Jackson <ajackson@redhat.com> 1.6.5-7.fc6
- i810.xinf: Whitelist Apple 945GM machines and Aopen Mini PC onto intel(4)

* Tue Sep 12 2006 Adam Jackson <ajackson@redhat.com> 1.6.5-6.fc6
- i810-1.6.5-to-git-20060911.patch: Backport post-1.6.5 fixes from git.
- i810-match-server-sync-ranges.patch: Make a terrible heuristic in the
  driver match the corresponding terrible heuristic in the server.

* Mon Aug 28 2006 Adam Jackson <ajackson@redhat.com> 1.6.5-5.fc6
- intel-945gm-lfp-blacklist.patch: Tweak the Apple blacklist to (hopefully)
  correctly distinguish between Mac Mini and Macbook Pro.

* Mon Aug 21 2006 Adam Jackson <ajackson@redhat.com> 1.6.5-4.fc6
- i810.xinf: PCI IDs for i965.

* Thu Aug 17 2006 Adam Jackson <ajackson@redhat.com> 1.6.5-3.fc6
- i810.xinf: Uppercase PCI IDs.

* Fri Aug 10 2006 Adam Jackson <ajackson@redhat.com> 1.6.5-2.fc6
- Update i810 to 1.6.5, should fix DRI.
- Add kuzdu requires.
- i810.xinf: Start whitelisting devices over to intel.

* Wed Aug  9 2006 Adam Jackson <ajackson@redhat.com> 1.6.4-3.fc6
- intel-driver-rename.patch: Fix the driver name in more places so it'll,
  you know, load.

* Wed Aug  9 2006 Adam Jackson <ajackson@redhat.com> 1.6.4-2.fc6
- intel-945gm-lfp-blacklist.patch: At anholt's suggestion, remove the other
  LFP special casing in favor of the blacklist.

* Wed Aug  9 2006 Adam Jackson <ajackson@redhat.com> 1.6.4-1.fc6
- Admit defeat, kinda.  Package both i810 stable and modesetting drivers.
  The modesetting driver is installed as intel_drv.so instead of i810_drv.so,
  and is selected with Driver "intel" in xorg.conf.  Individual devices will
  whitelist over to "intel" until that branch gets merged into head.
- Update the stable branch driver to 1.6.4 from upstream, adds i965 support.
- intel-945gm-lfp-blacklist.patch: Blacklist LFP detection on machines where
  the BIOS is known to lie.

* Tue Aug  8 2006 Adam Jackson <ajackson@redhat.com> 1.6.0-14.20060808modeset.fc6
- Today's snapshot: I2C bus creation fix.

* Wed Aug  2 2006 Adam Jackson <ajackson@redhat.com> 1.6.0-13.20060717modeset.fc6
- intel-prune-by-edid-pixclock.patch: Honor the EDID-reported maximum pixel
  clock when computing the modes list.
- intel-virtual-sizing-bogon.patch: Don't interpret the size of the display
  in centimeters as the size of the display in pixels.

* Mon Jul 24 2006 Adam Jackson <ajackson@redhat.com> 1.6.0-12.20060717modeset.fc6
- Disable spread-spectrum LVDS, various crash and hang fixes, saner output
  probing.

* Thu Jul 13 2006 Adam Jackson <ajackson@redhat.com> 1.6.0-11.20060713modeset.fc6
- Update again for a mode comparison bugfix.

* Thu Jul 13 2006 Adam Jackson <ajackson@redhat.com> 1.6.0-10.20060713modeset.fc6
- Update to today's git; crash fixes, better pre-915 support, slightly better
  autoconfigurability.

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> 1.6.0-9.20060707modeset.1.fc6
- rebuild

* Tue Jul 11 2006 Adam Jackson <ajackson@redhat.com> 1.6.0-9.20060707modeset
- Fix Revision number to match naming policy.

* Tue Jul 11 2006 Kristian Høgsberg <krh@redhat.com> 1.6.0-8.modeset20060707
- Add back modesetting changes.

* Mon Jul 10 2006 Kristian Høgsberg <krh@redhat.com> 1.6.0-7
- Roll back modesetting changes and build for fc5 aiglx repo.

* Fri Jul  7 2006 Adam Jackson <ajackson@redhat.com> 1.6.0-6.modeset20060707
- Snapshot of the git modesetting branch.

* Fri Jul  7 2006 Adam Jackson <ajackson@redhat.com> 1.6.0-6
- Update i810.xinf to include entries for E7221 and 945GM.

* Fri Jun 23 2006 Mike A. Harris <mharris@redhat.com> 1.6.0-5
- Add with_dri macro to spec file, and conditionalize build time DRI support

* Fri May 26 2006 Mike A. Harris <mharris@redhat.com> 1.6.0-4
- Added "BuildRequires: libdrm >= 2.0-1" for (#192334), and updated sdk dep
  to pick up proto-devel as well.

* Tue May 23 2006 Adam Jackson <ajackson@redhat.com> 1.6.0-3
- Rebuild for 7.1 ABI fix.

* Tue Apr 11 2006 Kristian Høgsberg <krh@redhat.com> 1.6.0-2
- Bump for fc5-bling build.

* Sun Apr 09 2006 Adam Jackson <ajackson@redhat.com> 1.6.0-1
- Update to 1.6.0 from 7.1RC1.

* Tue Apr 04 2006 Kristian Høgsberg <krh@redhat.com> 1.4.1.3-4.cvs20060322.1
- Add patch to add missing #include's, specifically assert.h.

* Wed Mar 22 2006 Kristian Høgsberg <krh@redhat.com> 1.4.1.3-4.cvs20060322
- Update to CVS snapshot of 20060322.

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> 1.4.1.3-3.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Sat Feb 04 2006 Mike A. Harris <mharris@redhat.com> 1.4.1.3-3
- Added 8086:2772 mapping to i810.xinf for bug (#178451)

* Fri Feb 03 2006 Mike A. Harris <mharris@redhat.com> 1.4.1.3-2
- Added 8086:2592 mapping to i810.xinf for bug (#172884)

* Wed Jan 18 2006 Mike A. Harris <mharris@redhat.com> 1.4.1.3-1
- Updated xorg-x11-drv-i810 to version 1.4.1.3 from X11R7.0

* Tue Dec 20 2005 Mike A. Harris <mharris@redhat.com> 1.4.1.2-1
- Updated xorg-x11-drv-i810 to version 1.4.1.2 from X11R7 RC4
- Removed 'x' suffix from manpage dirs to match RC4 upstream.

* Wed Nov 16 2005 Mike A. Harris <mharris@redhat.com> 1.4.1-1
- Updated xorg-x11-drv-i810 to version 1.4.1 from X11R7 RC2

* Fri Nov 04 2005 Mike A. Harris <mharris@redhat.com> 1.4.0.1-1
- Updated xorg-x11-drv-i810 to version 1.4.0.1 from X11R7 RC1
- Fix *.la file removal.
- Added 'devel' subpackage for XvMC .so
- Added 'BuildRequires: libXvMC-devel' for XvMC drivers.

* Mon Oct 03 2005 Mike A. Harris <mharris@redhat.com> 1.4.0-1
- Update BuildRoot to use Fedora Packaging Guidelines.
- Deglob file manifest.
- Limit "ExclusiveArch" to x86, x86_64, ia64

* Fri Sep 02 2005 Mike A. Harris <mharris@redhat.com> 1.4.0-0
- Initial spec file for i810 video driver generated automatically
  by my xorg-driverspecgen script.
