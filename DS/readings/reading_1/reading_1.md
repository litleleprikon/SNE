# Distributed Systems: Reading 1

**Author**: Emil A. Sharifullin 
**Date**:   19 October, 2016  

First chapter of book "Distributed systems: principles and paradigms, Andrew S. Tanenbaum, Maarten Van Steen"

##### An alternative definition for a distributed system is that of a collection of independent computers providing the view of being a single system, that is, it is completely hidden from users that there even exist multiple computers. Give an example where this view would come in very handy.

This approach is very useful. For example huge internet sites(Facebook, Google) for users can be like regular sites with single access point but actually they have to communicate with distributed system. Another example is distributed filesystems or data storages like a CEPH or HDFS.

##### What is the role of middleware in a distributed system?

In distributed systems software can be ran on different  types of hardware/operating systems. Middleware is a spesial sowtware that provides homoheneous API in heterogeneous distributed system.

##### Explain what is meant by (distribution) transparency, and give examples of different types of transparency.

Distribution transparency means that user can access the system without knowledge that this system is distributed. In table below I concidered exmples of different types of transparency.

| Transparency | Example                                  |
| ------------ | ---------------------------------------- |
| Access       | REST API provides access tranparency because independently from data you have uniform API. Usually via rest API you can access web sites and also you can access DBMS for example. |
| Location     | In CDNs you can access data by URL without any assumptions wherever data located physically. |
| Migration    | With changing DNS record you can relocate your web application without users understand that their access different physical server. |
| Relocation   | Some of hypervisors allows chunks to hot relocate during clients access them. |
| Replication  | Some ORMs allow to use replications and hide from program that is works with data locaten on different replicas |
| Concurrency  | In DBMS there is exists types of concurrent access to rows, called "Transaction isolation": Read uncommitted, Read committed, Repeatable read, Serializable. |
| Failure      | Hadoop have mechanism that restart task it it fails. |

##### Why is it sometimes so hard to hide the occurrence of and recovery from failures in a distributed system?

There is very hard to determine that server is failed because most of monitoring systems measure time to response and time can be huge in two cases: when system is failed and when system just have big load.

##### Why is it not always a good idea to aim at implementing the highest degree of transparency possible?

There is not always possible to aim highest distribution transparency degree. There is a lot of reasons like physical rules that cannot be breakable and some actions that will increase distribution transparency degree can decrease availability or performance of whole system.

##### What is an open distributed system and what benefits does openness provide?

Open distributed system is a system that uses conponents that can be used in other systems. It means that components should implement standard protocols and agreements. This approach allows you to easily change some components and use components from other systems.

##### Describe precisely what is meant by a scalable system.

Scalability is an ability to insrease number of nodes, number of datacenters and number of administrative domains without loss of availability or performance.

##### Scalability can be achieved by applying different techniques. What are suitable techniques for size and geographical scaling? And for administrative scaling?

There is three techniques to scale system: hiding communication latencies, partitioning/distribution and replication.

#####  We argued that distribution transparency may not be adequate for pervasive systems. This statement is not true for all types of transparencies. Give an example.

In general pervasive systems not provide homogeneous environment and there is hard to provide distribution transparency between different types of devices. But for example migration transparency can be aimed with physical relocation of device if it for example works with wireless connection client will not realise that device is relocated.