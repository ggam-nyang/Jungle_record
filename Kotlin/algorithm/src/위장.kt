    class Solution2 {
        fun solution(clothes: Array<Array<String>>): Int {
            var answer = 1
            val clothesSet = hashMapOf<String, MutableSet<String>>()

            clothes.forEach {
                val (cloth, type) = it
                if (clothesSet.contains(type)) clothesSet[type]?.add(cloth) else clothesSet[type] = mutableSetOf(cloth)
            }

            for ((key, value) in clothesSet) {
                answer *= (value.size + 1)
            }


            return answer - 1
        }
    }