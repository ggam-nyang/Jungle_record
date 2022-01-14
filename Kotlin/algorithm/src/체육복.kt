class Solutionasd {
    fun solution(n: Int, lost: IntArray, reserve: IntArray): Int {
        var answer = 0

        val total = IntArray(n) {1}
        lost.forEach {
            total[it - 1] --
        }
        reserve.forEach {
            total[it - 1] ++
        }

        total.forEachIndexed { index, i ->
            if (i == 2) {
                if (index > 0 && total[index - 1] == 0) {
                    total[index - 1] = 1
                    total[index] = 1
                } else if (index < n - 1 && total[index + 1] == 0) {
                    total[index + 1] = 1
                    total[index] = 1
                }
            }
        }

        total.forEach {
            if (it > 0) answer++
        }
        return answer
    }
}