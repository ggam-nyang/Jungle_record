class Solution3 {
    fun solution(numbers: IntArray, target: Int): Int {
        var answer = 0

        fun dfs(sum: Int, index: Int) {
            if (index < numbers.size - 1) {
                dfs(sum + numbers[index], index + 1)
                dfs(sum - numbers[index], index + 1)
            } else {
                if (sum + numbers[index] == target) answer++
                if (sum - numbers[index] == target) answer++
            }
        }
        dfs(0, 0)

        return answer
    }
}