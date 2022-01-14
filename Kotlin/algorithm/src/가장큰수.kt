class Solutionbas {
    fun solution(numbers: IntArray): String {
        var answer = ""

        val strNumbers = numbers.map {
            it.toString()
        }.toMutableList()


        strNumbers.sortWith(Comparator { a, b ->
            -"$a$b".compareTo("$b$a")
        })

        strNumbers.map {
            answer += it
        }

        if (answer.toInt() == 0) answer = "0"
        if (answer[0] == '0') answer = "0"

        return answer
    }
}