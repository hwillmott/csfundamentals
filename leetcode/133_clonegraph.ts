/**
 * Definition for _Node.
 * class _Node {
 *     val: number
 *     neighbors: _Node[]
 * 
 *     constructor(val?: number, neighbors?: _Node[]) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.neighbors = (neighbors===undefined ? [] : neighbors)
 *     }
 * }
 * 
 */


function cloneGraph(node: _Node | null): _Node | null {
    // first pass: make nodes and put in dictionary linking to originals
    // second pass: make adjacency lists using dictionary

    // bfs or dfs doesn't matter, need "visited" record, will also use hashmap for that

    const nodeMap = {}
    let s = [node]
    let visited = {}

    // first pass
    while(s.length > 0) {
        const curr = s.pop()
        if (!curr) continue
        if (visited[curr.val]) continue

        visited[curr.val] = 1

        const deepCopy = new _Node(curr.val)
        nodeMap[curr.val] = deepCopy
        s.push(...curr.neighbors)
    }

    console.log(nodeMap)

    // second pass
    s = [node] 
    visited = {}
    while(s.length > 0) {
        const curr = s.pop()
        if (!curr) continue
        if (visited[curr.val]) continue

        visited[curr.val] = 1

        const deepCopy = nodeMap[curr.val]
        const neighbors = curr.neighbors
        neighbors.forEach((neighbor) => {
            const nCopy = nodeMap[neighbor.val]
            if (deepCopy.neighbors && !deepCopy.neighbors.some(e => e.val === nCopy.val)) {
                deepCopy.neighbors.push(nCopy)
            } else {
                deepCopy.neighbors = [nCopy]
            }
        })
        s.push(...curr.neighbors)
    }
	return node ? nodeMap[node.val] : null
};
