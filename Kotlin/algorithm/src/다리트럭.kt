import java.util.*

class Solution56 {
    fun solution(bridge_length: Int, weight: Int, truck_weights: IntArray): Int {
        var answer = 0

        val truckNumber = truck_weights.size
        val bridgeQueue = ArrayDeque<Pair<Int, Int>>()
        var timeTick: Int = 1

        bridgeQueue.offer(Pair(truck_weights[0], timeTick))
        var currWeight = truck_weights[0]
        var truckIdx = 1
        while (bridgeQueue.isNotEmpty()) {
            timeTick++
            val currTruck = bridgeQueue.first
            if (timeTick - currTruck.second >= bridge_length) {
                bridgeQueue.pollFirst()
                currWeight -= currTruck.first
            }

            if (truckIdx < truckNumber && currWeight + truck_weights[truckIdx] <= weight) {
                bridgeQueue.offer(Pair(truck_weights[truckIdx], timeTick))
                currWeight += truck_weights[truckIdx]
                truckIdx++
            }
        }

        answer = timeTick

        return answer
    }
}