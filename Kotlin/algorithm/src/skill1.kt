class Solution {
    fun solution(relation: Array<Array<String>>): Int {
        var answer = 0
        val uniqueBit = mutableListOf<Int>()
        val rowN = relation.size
        val colN = relation[0].size

        for (i in 1 until (1 shl colN)) {
            if (uniqueBit.any { (i and it) == it }) continue

            if (checkUnique(i, rowN, colN, relation)) uniqueBit.add(i)
        }

        answer = uniqueBit.size
        return answer
    }

    fun checkUnique(bit: Int, row: Int, col: Int, relation:Array<Array<String>>): Boolean {
        val tempHash = hashSetOf<String>()

        for (r in 0 until row) {
            var temp = ""
            for (c in 0 until col) {
//                println("$r $c")
                if (bit and (1 shl c) != 0) {
                    temp += relation[r][c]
                }
            }

            if (tempHash.contains(temp)) return false

            tempHash.add(temp)

//            tempHash.forEach {
//                println(it)
//            }
        }
        return true
    }
}