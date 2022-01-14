class Solution1 {
    fun solution(citations: IntArray): Int {
        var answer = 0
        val lenArr = citations.size

        val sortedArray = citations.sortedArrayDescending()

        for (i: Int in 0 until lenArr) {
            if (sortedArray[i] < i + 1)
                return i
        }


        return lenArr
    }
}

