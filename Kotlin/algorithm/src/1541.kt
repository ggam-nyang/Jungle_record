import java.io.BufferedReader
import java.io.InputStreamReader


fun main(args:Array<String>) {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val input = br.readLine()

    var temp: String = ""
    var answer: Int = 0
    var isMinus: Boolean = false

    input.forEach {
        if (it == '+') {
            if (isMinus) answer -= temp.toInt() else answer += temp.toInt()
            temp = ""
        } else if (it == '-') {
            if (isMinus) answer -= temp.toInt() else answer += temp.toInt()
            isMinus = true
            temp = ""
        } else {
            temp += it
        }
    }
    if (isMinus) answer -= temp.toInt() else answer += temp.toInt()

    println(answer)

}