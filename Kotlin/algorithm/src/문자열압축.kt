import kotlin.math.min

class Solutioncc {
    fun solution(s: String): Int {
        var answer = 1000

        var tempAnswer = 0
        var count = 0
        var temp: String
        for (i in 2 .. s.length / 2) {
            tempAnswer = 0
            count = 1
            temp = s.slice(0 until i)
            for (j in i until s.length - i step(i)) {
                if (s.slice(j until j + i) == temp) {
                    count ++
                } else {
                    temp = s.slice(j until j + i)
                    if (count > 1) tempAnswer += i + 1 else tempAnswer += i
                }
            }
            answer = min(answer, tempAnswer)
        }
        return answer
    }
}