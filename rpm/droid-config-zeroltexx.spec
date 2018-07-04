# These and other macros are documented in
# ../droid-configs-device/droid-configs.inc

%define device zeroltexx
%define vendor samsung
%define vendor_pretty Samsung
%define device_pretty Galaxy S6 Edge (zeroltexx)
%define dcd_path ./
# Adjust this for your device
%define pixel_ratio 1.5
# We assume most devices will
%define have_modem 1

Provides: ofono-configs

# Community HW adaptations need this
%define community_adaptation 1

%define ofono_enable_plugins hfp_ag_bluez5

%include droid-configs-device/droid-configs.inc
