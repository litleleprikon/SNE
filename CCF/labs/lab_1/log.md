# Cyber Crime and Forensics lab-1:

**date:** 9 Jan 2017

**author:** Emil A. Sharifullin

| Time               | Log Record                               |
| ------------------ | ---------------------------------------- |
| 2:20 pm 9 Jan 2017 | I got flash drive with red plactic pannel and with sticker with "Evidence" text. I need to investigate what certain evidence contain this stick ![evidence_1](/Users/litleleprikon/Yandex.Disk.localized/InnopolisU-EDU/SNE/CCF/labs/lab_1/images/evidence_1.JPG) ![evidence_2](/Users/litleleprikon/Yandex.Disk.localized/InnopolisU-EDU/SNE/CCF/labs/lab_1/images/evidence_2.JPG) ![evidence_3](/Users/litleleprikon/Yandex.Disk.localized/InnopolisU-EDU/SNE/CCF/labs/lab_1/images/evidence_3.JPG) |
| 2:50 pm 9 Jan 2017 | I Inserted flash drive to my investigation computer with DEFT live-USB but not mounted it. I opened GUYMAGER utility and created image of of flash drive and info file. I used GUYMAGER 0.7.3-1. The SHA-256 hash-sum of disk is  69bf6a0a408347390fcbebaa99aef95b1e1df81ca24643186daff935b1e88429 |
| 3:34 pm 9 Jan 2017 | I started to investigate image file. All log of commands to mount file is listed in **Listing 1** |
| 7:05 pm 9 Jan 2017 | I started to investigate files inside image file. |

### Listing 1

Commands to mount disk image.

```bash
ewfmount ~/Desktop/evidence1.E01 /mnt/d
fdisk -l /mnt/d/ewf1
losetup --offser 65536 /dev/loop1
sudo mount -r /dev/loop1 ~/Desktop/mnt
```

### Listing 2

Commands to make image using dd

```bash
ddrescue /dev/sdc1 /mnt/devcopy
dhash -t -f /dev/sdc1 --md5 --sha1 -o /mnt/diskhashes.dd --log /mnt/diskhashes_log.html
```

### Listing 3

Metainformation file of GUYMAGER

```

GUYMAGER ACQUISITION INFO FILE
==============================

Guymager
========

Version              : 0.7.3-1            
Compilation timestamp: 2014-01-17-14.37.05
Compiled with        : gcc 4.4.5          
libewf version       : 20100226           
libguytools version  : 2.0.2              


Device information
==================
Command executed: bash -c "search="`basename /dev/sdc`: H..t P.......d A..a de.....d" && dmesg | grep -A3 "$search" || echo "No kernel HPA messages for /dev/sdc""
Information returned:
----------------------------------------------------------------------------------------------------
   No kernel HPA messages for /dev/sdc

Command executed: bash -c "smartctl -s on /dev/sdc ; smartctl -a /dev/sdc"
Information returned:
----------------------------------------------------------------------------------------------------
   smartctl 5.43 2012-06-30 r3573 [x86_64-linux-3.5.0-30-generic] (local build)
   Copyright (C) 2002-12 by Bruce Allen, http://smartmontools.sourceforge.net
   
   /dev/sdc: Unknown USB bridge [0x0781:0x5576 (0x126)]
   Smartctl: please specify device type with the -d option.
   
   Use smartctl -h to get a usage summary
   
   smartctl 5.43 2012-06-30 r3573 [x86_64-linux-3.5.0-30-generic] (local build)
   Copyright (C) 2002-12 by Bruce Allen, http://smartmontools.sourceforge.net
   
   /dev/sdc: Unknown USB bridge [0x0781:0x5576 (0x126)]
   Smartctl: please specify device type with the -d option.
   
   Use smartctl -h to get a usage summary

Command executed: bash -c "hdparm -I /dev/sdc"
Information returned:
----------------------------------------------------------------------------------------------------
   SG_IO: bad/missing sense data, sb[]:  70 00 05 00 00 00 00 14 00 00 00 00 20 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
   
   /dev/sdc:
   
   Unknown device type:
   	bits 15&14 of general configuration word 0 both set to 1.

Hidden areas: unknown


Acquisition
===========

Linux device            : /dev/sdc                                                           
Device size             : 4004511744 (4.0GB)                                                 
Format                  : Expert Witness Format, sub-format Guymager - file extension is .Exx
Image meta data         
   Case number          : Lab-1                                                              
   Evidence number      : 0001                                                               
   Examiner             : Emil A. Sharifullin                                                
   Description          : Red evidence flash drive                                           
   Notes                : 4C532000060816106053                                               
Image path and file name: /root/Desktop/evidence1.Exx                                        
Info  path and file name: /root/Desktop/evidence1.info                                       
Hash calculation        : MD5 and SHA-256                                                    
Source verification     : off                                                                
Image verification      : on                                                                 

No bad sectors encountered during acquisition.
State: Finished successfully

MD5 hash                   : 50decb45c3d56ffe1a3c538bb7898fd9                                
MD5 hash verified source   : --                                                              
MD5 hash verified image    : 50decb45c3d56ffe1a3c538bb7898fd9                                
SHA1 hash                  : --                                                              
SHA1 hash verified source  : --                                                              
SHA1 hash verified image   : --                                                              
SHA256 hash                : 69bf6a0a408347390fcbebaa99aef95b1e1df81ca24643186daff935b1e88429
SHA256 hash verified source: --                                                              
SHA256 hash verified image : 69bf6a0a408347390fcbebaa99aef95b1e1df81ca24643186daff935b1e88429
Image verification OK. The image contains exactly the data that was written.

Acquisition started : 2017-01-09 11:50:17 (ISO format YYYY-MM-DD HH:MM:SS)   
Verification started: 2017-01-09 11:53:14                                    
Ended               : 2017-01-09 11:53:38 (0 hours, 3 minutes and 20 seconds)
Acquisition speed   : 21.58 MByte/s (0 hours, 2 minutes and 57 seconds)      
Verification speed  : 166.04 MByte/s (0 hours, 0 minutes and 23 seconds)     


Generated image files and their MD5 hashes
==========================================

No MD5 hashes available (configuration parameter CalcImageFileMD5 is off)
MD5                               Image file
n/a                               evidence1.E01

```



