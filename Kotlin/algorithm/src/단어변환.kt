import java.util.ArrayDeque

class Solutionq {
    fun solution(begin: String, target: String, words: Array<String>): Int {
        var answer = 0

        val visited = BooleanArray(words.size) {false}
        val queue = ArrayDeque<Pair<String, Int>>()

        queue.addLast(Pair(begin, 0))

        while (queue.isNotEmpty()) {
            var (nowWord, count) = queue.removeFirst()
            if (nowWord == target) return count


            words.forEachIndexed { index, s ->
                if (!visited[index] && checkWords(nowWord, s)) {
                    visited[index] = true
                    queue.addLast(Pair(s, count + 1))
                }
            }
        }
        return 0
    }

    fun checkWords(s1: String, s2: String): Boolean {
        var count = 0
        s1.indices.forEach {
            if (s1[it] == s2[it]) count ++
        }

        return s1.length - count == 1
    }
}