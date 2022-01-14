import java.io.BufferedReader
import java.io.InputStreamReader


fun main(args:Array<String>) {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val (noListenCount, noSeeCount) = br.readLine().split(' ').map { it.toInt() }

    val noListenMember = mutableSetOf<String>()
    val noSeeMember = Array<String?>(noSeeCount) { null }
    val answer = mutableListOf<String>()

    for (i: Int in 0 until noListenCount) {
        noListenMember.add(br.readLine())
    }

    for (i: Int in 0 until noSeeCount) {
        var name = br.readLine()
        if (noListenMember.contains(name)) answer.add(name)
    }

    answer.sort()

    println(answer.size)
    answer.forEach {
        println(it)
    }
}