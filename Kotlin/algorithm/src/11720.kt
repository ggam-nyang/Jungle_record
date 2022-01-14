import java.io.BufferedReader
import java.io.InputStreamReader


fun main(args:Array<String>) {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val N = br.readLine().toInt()
    val num = br.readLine().toString()

    var answer = 0
//    for (i: Int in 0 until N) {
//        answer += num[i].toInt() - '0'.toInt()
//    }

    num.forEach {
        answer += it.toString().toInt()
    }
    println(answer)



}