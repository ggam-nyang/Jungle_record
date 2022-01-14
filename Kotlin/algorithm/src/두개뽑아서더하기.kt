import java.util.*

class aa {
    fun solution(numbers: IntArray): IntArray {
        var answer: IntArray = intArrayOf()

        val temp = mutableSetOf<Int>()

        for (i in numbers.indices) {
            for (j in i + 1 until numbers.size) {
                temp.add(numbers[i] + numbers[j])
            }
        }

        answer = temp.sorted().toIntArray()
        return answer
    }
}