# Distributed Systems: Reading 4

**Author**: Emil A. Sharifullin 
**Date**:   10 November, 2016  

### What is the relation between entity, access point, and address?

Access point is a special kind of entity which can provide an access to another entities. Name of entity is called address. Entity can have more that one access points.

### In which case would broadcasting be a better solution than forwarding pointers? In which cases it would not?

The forwarding-pointers solution is better when you know previous location of resource because you can easily find new location without flood. But in LAN's broadcasting can provide access to some entity without any additional information. I mean that in forward pointers you must to know initial location but if you don't know anything like in trully peer-to-peer systems without any centralized approach you cannot apply forward pointing.

### Consider the Chord system as shown in Fig. 5-4 and assume that node 7 has just joined the network. What would its finger table be and would there be any changes to other finger tables?

Reffering to [Wikipedia](https://en.wikipedia.org/wiki/Chord_(peer-to-peer)) In case of addition of new node we need to do following actions

* Initialize node n (the predecessor and the finger table).
* Notify other nodes to update their predecessors and finger tables.
* The new node takes over its responsible keys from its successor.

And seventh node will have following table

| Finger | Node |
| ------ | ---- |
| 1      | 9    |
| 2      | 9    |
| 3      | 11   |
| 4      | 18   |
| 5      | 28   |

So now all nodes must to be updated accordingly this changes.

### Again consider the Chord system in Fig. 5-4 and assume that node 9 has just left the network unexpectedly. Which finger tables would need to be updated and to which values? Explain the process for one affected node.

In this case evey node that have finger for ninth node must to be updated . For example for 4'th node finger table will be 

| Finger | Node |
| ------ | ---- |
| 1      | 11   |
| 2      | 11   |
| 3      | 11   |
| 4      | 14   |
| 5      | 20   |



### Consider an entity moving from location A to B, while passing several intermediate locations where it will reside for only a relatively short time. When arriving at B, it settles down for a while. Changing an address in a hierarchical location service may still take a relatively long time to complete, and should therefore be avoided when visiting an intermediate location. How can the entity be located at an intermediate location?

An entity must to set forward pointer to every intermediate locations it arrives. After entity arrive the B it must to add it's address to centralized name system and after it delete all forward pointers. The good approach in my opinion is to keep both: pointers and centralized name system record for a short time to allow some clients with cache to access entity.

### Which design decisions were made to provide performance and availability of DNS?

DNS have couple of techniques to provide availability and performance. The main of them in my opinion is caching. Caching allows to reduce the amount of messages in network and to provide availability for a time after main servers falls. Duplication and distribution makes DNS system not sensible to filure of one single server.

### LDAP combines two types of naming. Which are they? And what is the advantage of such a combination?

LDAP have two types of naming: structured and attributes-based.