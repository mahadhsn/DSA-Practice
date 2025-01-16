# LinkedLists
## Self explanatory
- imagine a train
    - each section is connected to the next

- each node contains:
    - data
    - pointer to next node


### Singly Linked List
`      node                node                node        `
` [data | address] -> [data | address] -> [data | address] `

### Doubly Linked List
`           node                                node      `
` [address| data | address] <-> [address | data | address]`

## Keywords:
### Head
- the address of the first entry
- contains data and a pointer to the next node

### Tail
- end of the list
- points to nothing (NULL)

### Node
- each section
    - think of this 1 of the train carriages 

## Advantages
1. dynamic data structure 
    - allocates needed memory while running
2. insertion and deletion of nodes is easy O(1)
3. No/Low memory waste

## Disadvantages
1. greater memory usage 
    - addtional pointer
2. no random access of elements 
    - no index[i]
3. accessing/searching elements is more time consuming
    - O(n)