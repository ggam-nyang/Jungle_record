class Solutiondd {
    fun solution(n: Int, path: Array<IntArray>, order: Array<IntArray>): Boolean {
        var answer = true

        val graph = Array<MutableList<Int>>(n){ mutableListOf() }
        val visited = Array<Boolean>(n){false}
        val orderGraph = Array<MutableList<Int>>(n){ mutableListOf() }

        path.forEach {
            graph[it[0]].add(it[1])
            graph[it[1]].add(it[0])
        }

        order.forEach {
            orderGraph[it[1]].add(it[0])
        }

        val test = mutableSetOf<Int>()

        test += 1
        println(test)


        return answer
    }

    fun dfs(start:Int, graph: Array<MutableList<Int>>, visited: Array<Boolean>, order: Array<MutableList<Int>>): Boolean {
        visited[start] = true

        graph[start].forEach {
            if (!visited[it]) {
                order[it].forEach { needPath ->
                    if (!visited[needPath]) return false
                }
                dfs(it, graph, visited, order)
            }
        }
        return true
    }
}