import java.util.ArrayDeque

class Solutionb {
    fun solution(priorities: IntArray, location: Int): Int {
        var answer = 0

        val queue = ArrayDeque<Pair<Int, Int>>()

        var maxPri = 0
        priorities.forEachIndexed { index, i ->
            queue.add(Pair(index, i))
        }

        priorities.sort()
        var i = priorities.size - 1


        while (i > 0) {
            val (tempIdx, tempPri) = queue.removeFirst()
            if (tempPri < priorities[i]) {
                queue.addLast(Pair(tempIdx, tempPri))
            } else {
                if (tempIdx == location) return priorities.size - i
                i --
            }
        }
        answer = priorities.size
        return answer
    }
}