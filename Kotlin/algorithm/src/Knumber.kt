import kotlin.math.max
import kotlin.math.min

class Solutionaa {
    fun solution(array: IntArray, commands: Array<IntArray>): MutableList<Int> {
        var answer = mutableListOf<Int>()


        commands.forEachIndexed { index, ints ->
            val (start, end, destination) = ints

            val tempArray = array.slice(min(start, end) - 1 until max(start, end))
//            println(tempArray.sorted())
            answer.add(tempArray.sorted()[destination - 1])
        }
        return answer
    }
}