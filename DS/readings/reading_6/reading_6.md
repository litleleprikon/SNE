# Distributed Systems: Reading 6

**Author**: Emil A. Sharifullin 
**Date**:   23 November, 2016  

### Consider resilience by process groups. What are the advantages and disadvantages of flat process groups versus hierarchical ones?

Flat groups is more hard to implement but in view of fault tolerance they are more preferable because there is harder to crash fully distributed server.

Hierarchical groups have single point of failure and less fault tolerant but can be easily implemented.

### Consider the 5 different classes of failures in RPC systems. Which of them could lead to orphan computations? What can server do with orphan computations?

According to [http://web.cs.iastate.edu/~cs554/NOTES/Ch8-2.pdf]() there are five failure types.

* Client cannot locate server
* Server crashes after receiving a request
* Client request is lost
* Server response is lost
* Client crashes after sending a request
  At the last problem process which was created for certain request will be orphant. There is solution that is called orphan extermination and with this technic we can release resources.

### What is joint consensus in Raft and how does it work?

Joint consensus is the technique to change configuration of cluster based on previous version of configuration and contains statements from new configuration.

### In Basic Paxos, suppose that a cluster contains 5 servers and 3 of them have accepted proposal 5.1 with value X. Once this has happened, is it possible that any server in the cluster could accept a different value Y? Explain your answer.



### Can the model of triple modular redundancy handle Byzantine problem?

Yes it can handle this problem while number of bad nodes lower than 2. In case when one node generates error other two will give right data and all that needed to do is to chose the version of data which contained on higher number of nodes

### In the two-phase commit protocol, why can blocking never be completely eliminated, even when the participants elect a new coordinator?

The new coordinator can fault exactly after election and in this case another nodes cannot make a desicion.

### The output of a Mapper is written into the local filesystem instead of the global filesystem. Why? Your answer should explain both why writing into the global file system would undesirable as well as why it would be of minimal benefit

The basic approach of MapReduce is that code tranfers over data and data shouldn't transfer often. But in this case we cannot access intermediate results during HDFS and can access it only with access to certain node. But in general view of MapReduce job we don't needed to access this results and this data is accessible by shuffle.

### Why does Hadoop sort records enroute to a Reducer?How would it affect things if these records were processed by the Reducer in the order in which they were received from the various Mappers?

First reason is that in sorted sequence of keys you can search certain key in logarithmic time. Another reason is that in reducers we can easily join oairs with same keys. I mean that if we have sorted input in reducer we can run in cycle while previous and current keys are the same and process both pairs in easy way.

### What happens if a Mapper or Reducer fails?

In Hadoop after job failing  TaskTracker will notify the JobTracker when a task fails. The JobTracker decides what to do then: it may resubmit the job elsewhere, it may mark that specific record as something to avoid, and it may may even blacklist the TaskTracker as unreliable. This approach is possible bacause after every operation(map, shuffle, reduce) the resuls is saved in HDFS and JournalNode creates a new record in journal. It means that in case of every fault we have results of previous operations and we can repair working sequence.


