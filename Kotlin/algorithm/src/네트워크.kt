class Solution4 {
    fun solution(n: Int, computers: Array<IntArray>): Int {
        var answer = 0

        val visited = BooleanArray(n){false}

        for (i in computers.indices) {
            if (!visited[i]) {
                dfs(i, computers, visited)
                answer ++
            }
        }

        val queue = ArrayDeque<Int>()
        queue.add(1)


        return answer
    }

    fun dfs(start: Int, computers: Array<IntArray>, visited: BooleanArray) {
        visited[start] = true
        computers[start].forEachIndexed { index, i ->
            if (i == 1 && !visited[index]) {
                dfs(index, computers, visited)
            }
        }
    }
}