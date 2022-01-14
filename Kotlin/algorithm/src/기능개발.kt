class Solutiona {
    fun solution(progresses: IntArray, speeds: IntArray): MutableList<Int> {
        var answer = mutableListOf<Int>()

        var day: Int = 0
        var countCompleteProgresses: Int = 0
        while (countCompleteProgresses < progresses.size) {
            day++
            progresses.forEachIndexed { index, i ->
                progresses[index] += speeds[index]
            }

            var tempCompleteCount = 0


            for (i in countCompleteProgresses until progresses.size) {
                if (progresses[i] >= 100) {
                    countCompleteProgresses ++
                    tempCompleteCount ++
                } else {
                    break
                }
            }

            if (tempCompleteCount > 0) answer.add(tempCompleteCount)
        }


        return answer
    }
}