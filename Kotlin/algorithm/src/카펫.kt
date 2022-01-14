class Solutionccc {
    fun solution(brown: Int, yellow: Int): IntArray {
        var answer = intArrayOf()

        val totalTile = brown + yellow

        var b: Int = 0
        for (a in 1 until totalTile) {
            if (totalTile % a == 0) b = totalTile / a else continue

            if (a + b - 2 == brown / 2) answer = intArrayOf(a, b)
        }
        return answer
    }


}