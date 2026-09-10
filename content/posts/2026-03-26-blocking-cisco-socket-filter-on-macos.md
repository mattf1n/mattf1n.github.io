---
title: Blocking the Cisco Secure Client Socket Filter on macOS
date: 2026-03-26
---

The Cisco Secure Client Socket Filter installed by the Cisco VPN client on my laptop (VPN is necessary to connect to USC compute cluster) was causing problems: sometimes when I started up my laptop I couldn't access the internet even when disconnected from the VPN. It would show "connected" but nothing would load; `ping google.com` would time out.
The socket filter didn't seem to be disable-able from network settings,
and I could only seem to fix it by disabling the network extension.
After disabling it, I would get annoying recurring dialogues asking me to allow the filter. Even after clicking "Do not allow", the dialogue would reappear immediately 3(!) times. 
Deleting the extension did no good: every time I reconnected to the VPN it would reinstall.
Interestingly, I found that I do not need the extension enabled to connect to the VPN.

Claude found a fix for me and wrote this guide.
WARNING: what follows is LLM generated content.

# Blocking the Cisco Secure Client Socket Filter on macOS

If you use Cisco Secure Client for VPN, you may get a recurring dialog:
*"Cisco Secure Client - Socket Filter" Would Like to Filter Network Content.*
Clicking "Don't Allow" doesn't stick — the next time you connect to VPN,
Cisco reinstalls the extension and the dialog comes back.

The fix is to install a configuration profile that explicitly blocks the extension.

First, check your extension's team ID and bundle ID:

```
systemextensionsctl list
```

For Cisco Secure Client, these should be:

- **Team ID:** `DE8Y96K9QP`
- **Bundle ID:** `com.cisco.anyconnect.macos.acsockext`

Create a file called `BlockCiscoSocketFilter.mobileconfig` with the following contents:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>PayloadType</key>
            <string>com.apple.system-extension-policy</string>
            <key>PayloadIdentifier</key>
            <string>com.user.block-cisco-sockfilter.policy</string>
            <key>PayloadUUID</key>
            <string>A1B2C3D4-E5F6-7890-ABCD-EF1234567890</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
            <key>AllowUserOverrides</key>
            <false/>
            <key>AllowedSystemExtensions</key>
            <dict>
                <key>DE8Y96K9QP</key>
                <array/>
            </dict>
        </dict>
    </array>
    <key>PayloadDescription</key>
    <string>Blocks Cisco Secure Client Socket Filter network extension</string>
    <key>PayloadDisplayName</key>
    <string>Block Cisco Socket Filter</string>
    <key>PayloadIdentifier</key>
    <string>com.user.block-cisco-sockfilter</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>B2C3D4E5-F6A7-8901-BCDE-F12345678901</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

Then open it to install:

```
open BlockCiscoSocketFilter.mobileconfig
```

System Settings will prompt you to install the profile.
After rebooting, the dialog should be gone for good.

> Note from Matt: I didn't need to reboot.
