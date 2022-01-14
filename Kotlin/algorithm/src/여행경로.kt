class Solutionaasd {
    fun solution(tickets: Array<Array<String>>): MutableList<String> {
        var answer = mutableListOf<String>()

        val graph = hashMapOf<String, MutableSet<String>>()
        tickets.forEach {
            graph.getOrPut(it[0]) { mutableSetOf() } += it[1]
        }

        graph.forEach { k, v ->
            graph[k] = v.toSortedSet()
        }

        answer.add("ICN")
        for (i in tickets.indices) {
            val first = graph[answer[i]]!!.first()
            answer.add(first)
            graph[answer[i]]!!.remove(first)
        }


        return answer
    }
}