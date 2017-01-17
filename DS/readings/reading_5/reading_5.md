# Distributed Systems: Reading 5

**Author**: Emil A. Sharifullin 
**Date**:   17 November, 2016  

### Consider the processes in Fig. 6.14 have continued execution and process P1 currently having VC1=[1,2,0] receives a message m from process P2, ts(m)=[2,1,1]. What information does P1 have, and what will it do when receiving m?

The next P1 state will be [2,2,1]

### What would happen with the Ricart and Agrawala algorithm if a process crashes? Discuss.

If process that have taken mutex will crash it will not send release message and mutex will be unreleasable forever. This the is main weakness of this algorithm.

### Many distributed algorithms require the use of a coordinating process. To what extent can such algorithms actually be considered distributed? Discuss.

In such algorithms every node can be in role of coordinator and coordinator role swapped eventually in this case there is not a centralized approach and we can assume that this is the distributed approach.

### Which of the mutual exclusion solutions discussed in class requires the fewest messages under heavy contention?

| Algorithm                             | Number of Messages         |
| ------------------------------------- | -------------------------- |
| Ricart–Agrawala                       | $2*(N-1)$                  |
| Lamport's distributed mutex algorithm | $3(N − 1)$                 |
| Maekawa                               | $3\sqrt{N}$ to $6\sqrt{N}$ |
| Raymond                               | $O(log n)$                 |
| Centralized Server                    | $3$                        |
| Voting Distincts                      | $3*(2*\sqrt{N} - 1)$       |

So the lowest nuber of packets have centralized solution but this approach is vulnerable for process crash.


### Consider a bully-based technique for electing a coordinator. What kind of failure would result if multiple coordinators being elected? Under what assumptions is this acceptable?

Processes with higher id will receive more than one election messages and will process only first of them. This is possible if two processes they realise that coordinator is down at same moment. 

### Does the HTTP protocol use a push-based or pull-based approach for updates? Why?

HTTP is a request-response protocol what means that to receive some data we need to request it. In this case we can say that HTTP is pull based protocol. But there is not fare for HTTP/2 because server using HTTP/2 can push to client some data that it thinks is needed for client but didn't requested by client. It means that generally HTTP is pull based but in specific cases it's push based protocol. 

### When using a lease, is it necessary that the clocks of a client and the server, respectively, are tightly synchronized?

Yes it's necessary because if we will use only time periods we need also assume time to deliver messages between two nodes. It means that if coordinator sends lease permission to process and starts timer exactly after it sent but not received by other process. If lease requestor will use resource during all lease time it is possible that lease provider will think that lease released but requestor is thinking that it have time that equal to message delivery time.

### Consider a non blocking primary-backup protocol used to guarantee sequential consistency in a distributed data store. Does such a data store always provide read-your-writes consistency?

Yes sequential consistency is means that every operations happened before inpact on system in sequence they happened also as for spesific transaction.

### A file is replicated on 10 servers. List all the combinations of read quorum and write quorum that are permitted by the voting algorithm.

Quorum-based protocol requires that

* Nr + Nw > N
* Nw > N/2

So this is means that minimum Write quorum contains 6 servers and minimum read quorum contains one server. And if this rule is applied the vote will be passed.

### How would you characterize the consistency model of Facebook?

According to this [paper](http://sigops.org/sosp/sosp15/current/2015-Monterey/printable/240-lu.pdf) facebook have 99.99% of reads is under all types of consistency. But also Facebook do not guarantee that consistency at least one type of consistency will be aplied in 100% reads.