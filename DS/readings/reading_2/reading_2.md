# Distributed Systems: Reading 2

**Author**: Emil A. Sharifullin 
**Date**:   27 October, 2016  

- **[DS]** Chapter 1. Distributed systems: principles and paradigms, Andrew S.Tanenbaum, Maarten Van Steen


- **[TAX]** Section 3.2 “Storage Architecture”; A Taxonomy of Distributed StorageSystems, Martin Placek and Rajkumar Buyya

#### According to [DS], there are three types of system architectures: centralized, decentralized and hybrid. And according to [TAX] there are five of them. How do you think to which type of architecture by [DS] should we correspond the types that were proposed in the [TAX] and why?

In my opinion Globally Centralised(Client-Server and Peer-to-Peer) systems from [TAX] is an analogue of Centralized systems in [DS]. Locally centralised(Client-Server and Peer-to-Peer) systems from [TAX] is a hybrid systems in [DS]. And pure Peer-to-Peer is an decentralised systems.

#### What is the difference between a process and a thread?

Process and thread both are independent execution sequences. In UNIX systems processes and threads very similar except threads share virtual memory and system resources inside one process. In windows machine processes and threads differs more but also threads share memory and resources(file descriptors, sockets, etc.) and processes cannot do this.

#### What is an asynchronous (non-blocking) I/O operation?

Asynchronous I/O is an approach when program do not wait for completion of started I/O operation. Usually program starts I/O operation and execute it parallel with main execution sequence(in another thread/another device/in switchable finite state automata like Node.js or python asyncio lib) and when I/O operation ends it thow interruption and run code for certain I/O operation result.

#### Does it make sense to use threads on a single-core CPU?

Multithread application can be useful in single-core CPU in couple of reasons

* If some functions waste a lot of CPU time and block execution sequence another thread can be good solution to make application responsive.
* Resources can be shared in more efficient way between couple of processes depending on kind of operations in thread.

#### VM images such as AMIs can be quite big. How does this impact cloud providers that have many customers creating many different virtual machines all the time?

The main technique that allows cloud providers to maintain a lot of huge images is deduplcation. With deduplication providers can do both: minimize space on disks and in memory. Deduplication means that files which are same on two different images can be stored as one entity and use COW principle when this files is changed.

#### Are Web servers stateless or stateful?

Traditional web servers are stateless because HTTP is stateless prortocol that don't provide saving of state of connection. But there are two exceptions:

* Web sites that save user session
* Web sites that use HTTP/2 protocol which allow to save state of connection.

#### What is the difference in request dispatching for local-area and wide-area clusters? At what point will we need a redirection policy?

In local-area clusters there is two ways to provide dispatching: NAT and TCP handoff. In wide-area networks the one possible way to do dispatching is to manipulate with DNS records.

#### Wide-area redirection requires a method for measuring the distance between two IP addresses. Think of two different methods and discuss pros and cons.

There is couple of possible possibilities to measure the distance:

* Measure geographical distance - possible with using geoip services, but can have a low precision because geoip databases can have mistakes.
* Measure latency between two IP - it requires to send small amount of data between client and server and this approach can give more precision when client and server contact directly without NAT but will have fails when client use NAT. Also it increase time to create initial connection.

#### What problems will you need to solve to allow live migration of virtual machines between different wide-area clusters?

The main difficulty is how to migrate machine without downtime. To solve this problem usually old copy of virtual machine works during the end of migration. Also there is need to transfer a lot of data by network and this can spend a lot of time. During this time the state of machine can be changed and this is another problem. 

#### According to Fuggetta (Note 3.9) there are three segments in a process. Which segment do you think is typically more difficult to migrate?

In my opinion the hardest to migration segment is state segment because migrating this segment means to copy virtual memory and reestablish it on new node. Also resource segmant can be hart to migrate if some references are local(on this certain node).