# Memory Forensic of Modern In-Memory Storage

## Emil Sharifullin

## System and Network Engineering, Innopolis University

### Abstract

> In-memory storages became very popular last years. A lot of highload applications use in-memory storages as a cache or to store latency-sensitive data(sessions, user preferences, etc.). In-memory storages usually cannot be investigated with disk imaging tools because they are don't store data on the disks by default. 

> In this paper I am going to check is it possible to create memory image of popular in-memory database(Redis/Memcache) and create tools to extract structured data from this image.

#### Related Works

Xu *et all*[1] proposed methods to read RDP and AOF files in which Redis store data in persistent mode. They are defined  couple of methods to parse files and created couple of tools to extract data.

Mun *et. all* [2] explored methods of recovery data from running Redis instance.

#### Research Goals

- Investigate methods of creation memory images of in-memory database
- Investigate is it possible to make structured database dump from memory image
- Create tools for automated memory image parsing

#### Application

This methods will be very useful in cases when investigators have physical access to server with in-memory storage and can make memory image. Usually this sorts of storages store important data as a sessions and it can be great to get access to user's profile on criminal web service.

#### References

[1] Xiaowei Xu, Jian Xu, Yizhi Ren, Haiping Zhang, Ning Zheng, *"A Forensic Analysis Method for Redis Database Based on RDB and AOF File"*ollege of Computer, Hangzhou Dianzi University, Hangzhou, China, 2014

[2] C. J. Mun, J. D. Won, Y. J. Seong, and L. S. Jin, _"Digital Forensics Investigation of Redis Database"_ KIPS Transactions on Computer and Communication Systems, Vol.5, No.5, pp.117-126, 2016, DOI: 10.3745/KTCCS.2016.5.5.117.